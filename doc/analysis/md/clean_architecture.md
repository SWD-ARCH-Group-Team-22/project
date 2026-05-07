This section aims to clarify the architectural choices made to build the software. The official documentation describes Freeplane as an Extension-object-driven application: objects are built to be extensible from the outside while remaining independent from their extensions.  
The Extension-Object pattern is a Design Pattern defined by Erich Gamma in 1998. However, it provides a useful starting point to better understand how it fits in the broader architectural environment.  
The first step was to define _entities_, _use cases_ and _external layers_. To figure out a starting point, Freeplane developers were contacted, and they provided an AI tool, deepwiki.com, to ask questions to to gather information about the codebase. The chatbot gave us a hint: entites could be found in many packages. `org.freeplane.features.map` was among them. This package is responsible for the definition of basic business rules for managing nodes and maps.  
To double check, a statistical analysis was carried out: data from commits throughout the software's lifecycle was extracted, and metrics were calcuated: A stability measure was computed, considering average time between commits, number of commits and package age. This first analysis returned a strange result: `org.freeplane.features.map` is a very unstable component, with a commit every 3 days on average.  
This can be explained by the high coupling between the package and ui components. A deeper analysis reveals that almost 43% commit number shares changes with freeplane ui components, and this number grows if we look at subpackages such as `org.freeplane.features.map.filemode` or `org.freeplane.features.map.clipboard` (both at almost 61% of shared commit number with ui components).  
Code analysis reveals that most classes in the package have dependencies on ui components, both on custom Freeplane UI classes and standard Java awt ones. The approach is different: while dependencies towards `org.freeplane.ui` packages respect Clean Architecture rules, such as dependencies ruled by Interfaces, java ui standard classes are directly imported, thus violating the same principles developers tried to respect with custom packages.  

```plantuml
    @startuml
    title Freeplane Clean Architecture Violations - Case Study

    skinparam shadowing false
    skinparam roundcorner 8
    skinparam DefaultFontName Helvetica
    skinparam class {
        BackgroundColor White
        ArrowColor #555555
        BorderColor #444444
        HeaderBackgroundColor #F4F6F7
    }
    skinparam package {
        FontSize 14
        Style folder
    }
    skinparam note {
        BackgroundColor #FFFCDF
        BorderColor #F1C40F
        FontColor #333333
    }

    top to bottom direction

    package "Presentation Layer (UI)" as UILayer #E8F4F8 {
        
        class "java.awt.Color" as JavaColor #FFF0F0
        class "java.awt.GraphicEnvironment" as GraphicEnvironment #FFF0F0



        package "UI Features" as UIFeatures <<org.freeplane.features.ui>> #FFFFFF {
            class IMapViewChangeListener {
            }
            class IMapViewManager {
            }
            class ViewController {}
        }
    }

    package "Domain Layer (Logic)" as LogicLayer #EAF8E8 {
        
        package "NodeManagementLogic" as NodeLogic <<org.freeplane.features.node>> #FFFFFF {

            class MapController <<central map orchestrator>> {
            }

        }

        package "MindMap Mode" as MM <<org.freeplane.map.mindmap>> #FFFFFF {
            class MMapController {}
        }
    }

    UILayer -[hidden]down-> LogicLayer

    MapController -[#E74C3C,thickness=2]up-> JavaColor : <<violates>>

    MapController -[#2ECC71,thickness=2]up-> IMapViewChangeListener : <<complies>>
    MapController -[#2ECC71,thickness=2]up-> IMapViewManager : <<complies>>

    MMapController -[#2ECC71,thickness=2]up-> IMapViewChangeListener : <<complies>>
    MMapController -[#E74C3C,thickness=2]up-> GraphicEnvironment : <<violates>>


    note right of UIFeatures
    **COMPLIANT:**
    This set of dependencies is compliant 
    with clean architecture: the business 
    logic doesn't know anything about the 
    concrete UI object.
    end note

    legend right
        <back:#E74C3C>   </back> : Architectural violation -> points to the dependent package
        <back:#2ECC71>   </back> : Dependency Compliant -> points to the dependent package
    endlegend

    @enduml

```



There are other crucial violations of the Clean Architecture pattern: there is no clear definition of _entities_, _use cases_ and other layers. Some classes may look similar to one of these concepts: `MapModel` could be classified as an _entity_, `MapController` as a _use case_, `Controller` from `org.freeplane.features.mode` as an _adapter_. Most critic violations of the Clean Architecture pattern can be found in the dependency among these three classes: `MapModel` and `MapController` depend on the `Controller`: flow of dependencies is broken and therefore inner business logic cannot be tested in isolation. 


```plantuml
    @startuml

    title Class Diagram: Dependency Violation

    package "Node" as node <<org.freeplane.features.map>> {
        class MapModel{
            + getCurrentModeController()
        }

        class MapController {
            + getCurrentController()
        }

    }


    package "Mode" as mode <<org.freeplane.features.mode>>{
        
        class Controller {
        + Adapter()
        }    
    }

    MapModel --> Controller : depends on
    MapController --> Controller : depends on


    @enduml

```

```plantuml
    @startuml

    title Class Diagram: Dependency Violation - Possible refactor solution

    package "Node" as node <<org.freeplane.features.map>> {
        class MapModel{
            + getCurrentModeController()
        }

        class MapController {
            + getCurrentController()
        }

    }


    package "Mode" as mode <<org.freeplane.features.mode>>{

        class Controller {
            + ConcreteAdapter()
        }  

        interface IController {
            + exposedAdapter()
        }

    
    }

    MapModel --> IController : depends on
    MapController --> IController : depends on
    Controller -[hidden]up-> IController
    Controller --> IController : implements

    @enduml
```

Compliance with the principles from the Clean Architecture pattern can be found in the _persistence layer_: classes such as `MapReader` and `MapWriter` are at the outer layer of the architecture, and there are no dependency violations.
These architectural flaws can be extended to the application as a whole: the analysis of the `org.freeplane.features.map` package is a case study which can fairly represent the overall structure of the software. Freeplane does not comply with modern architectural patterns and particularly with the Clean Architecture one, and it can be explained by the age of the software, whose development started in 2009.
