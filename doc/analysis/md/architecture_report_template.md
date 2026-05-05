# Architectural Analysis of Freeplane – Reverse Engineering and Evaluation

#### 1. Introduction and Analysis Methodology (Target: ~200 words) -> 208 words
This report presents an architectural analysis of Freeplane with the objective of identifying its main structural characteristics, architectural style, and design principles. The analysis aims to reconstruct the system architecture and understand how its components are organized and interact.

The reverse engineering process was conducted using static code analysis and documentation review. The codebase was examined to identify packages, modules, and dependencies, while repository documentation was used to support architectural interpretation.

The system can be described as a **modular monolith enhanced with a micro-kernel (plug-in) pattern**, where a central core is extended through independently developed components. The codebase is organized into packages such as core, features, and view, which separate fundamental logic, functional behavior, and user interface concerns. This reflects a modular structure within a single deployable application. In addition, extensible elements within the features package indicate a micro-kernel (plug-in) pattern, allowing new functionality to be introduced without modifying the core. The presence of multiple modules and a large number of packages further confirms a structured and layered organization.

This architectural combination is well suited to mind-mapping software. The modular monolith ensures simplicity, consistency, and ease of deployment, while the micro-kernel pattern enables extensibility to support diverse user needs. Together, these approaches support maintainability, adaptability, and long-term evolution.


#### 2. The System in its Ecosystem: C4 Context Model (Target: ~300 words) - 314 words
The context diagram illustrates how Freeplane operates within its external environment and interacts with both users and supporting systems. Two main user roles are identified. Beginner users interact with the system to create and manage mind maps using basic functionality, while advanced users extend the system through scripting and plugins, enabling automation and customization.

Freeplane interacts with several external systems that support its core functionality. The most fundamental is the file system, which is responsible for storing and retrieving mind map data in XML-based formats, as well as associated resources such as images. This interaction reflects the system’s reliance on local persistence rather than external databases.

In addition, Freeplane communicates with external tools to enhance usability and interoperability. External document visualizers are used to export and display mind maps in formats such as PDF or HTML, while web browsers are invoked to open hyperlinks embedded within maps. The system also integrates with external services such as email tools, cloud APIs, and task management tools, enabling users to share, synchronize, or repurpose their data in different contexts. Furthermore, advanced integrations such as LLM-based tools support extended functionality for automation and intelligent processing.

From an architectural perspective, these interactions are mediated by the Freeplane application as a central component that encapsulates core logic and coordinates external communication. User inputs are handled through the user interface layer and translated into operations on the internal data model. These operations are then persisted via the file system using XML-based storage, or transformed into external representations through export services. Interactions with external tools and services, such as browsers, email systems, or external APIs, are triggered through defined integration points, ensuring that communication remains controlled within a clear system boundary.

Overall, the context model highlights Freeplane as a standalone desktop application that integrates with a variety of external systems to provide flexibility and extended capabilities while preserving a clear system boundary.
*   **Action:** *[Insert C4 Level 1 Diagram: Context]*

#### 3. Decomposition and Runtime: C4 Container Model (Target: ~400 words)
*   **Objective:** Show the deployable/executable units. For a desktop app like Freeplane, the "containers" are typically the base framework, the Core Engine, and the bundles/plugins.
*   **Action:** *[Insert C4 Level 2 Diagram: Container]*
*   **Questions to answer:**
    *   How is the runtime structured? What is the role of the plugin framework (e.g., OSGi / Equinox) that acts as the host?
    *   Which logical/physical modules make up the unalterable "Core," and which are identified as external "Plugins" (e.g., PDF export plugin, scripting plugin, LaTeX plugin)?
    *   How do these containers communicate at runtime (e.g., separate classloading, direct in-memory calls)?

#### 4. Mapping to Clean Architecture: Theory vs. Reality (Target: ~500 words)
*   **Objective:** Apply the lens of Clean Architecture to Freeplane's source code. Since this is legacy software, it is crucial to highlight both adherence and violations.
*   **Questions to answer:**
    *   Which classes/packages in Freeplane represent the *Entities* (e.g., the logical model of the node, the map) and the *Use Cases* (e.g., tree manipulation actions)?
    *   Are the user interface layer (Swing/AWT) and the persistence layer (XML parser) truly relegated to the outer layers (*Interface Adapters / Frameworks*) as Clean Architecture dictates?
    *   **Critical Evaluation:** Is the *Dependency Rule* strictly followed? Or did you find instances where the inner domain (Core/Entities) has direct dependencies on GUI elements or external libraries?

#### 5. Zooming into the Engine: C4 Component Model of the Core (Target: ~600 words)
*   **Objective:** Detail the internal design of the Core and showcase the extension points.
*   **Action:** *[Insert C4 Level 3 Diagram: Component for the main Controller and Plugin Management]*
*   **Questions to answer:**
    *   How is the typical MVC (Model-View-Controller) pattern of Freeplane (e.g., `MapModel`, `NodeModel`, `ModeController`) structured at the component level?
    *   What is the anatomy of the internal Plugin Manager? How does it discover, load, and register a plugin within the application's lifecycle?
    *   Which architectural components are responsible for event dispatching (e.g., model changes that need to update the UI and notify plugins)?

#### 6. Boundary Management and Core-Plugin Interaction (Target: ~400 words)
*   **Objective:** Explain the engineering mechanisms by which plugins cross architectural boundaries to extend Freeplane without modifying its core.
*   **Questions to answer:**
    *   How are the *Boundaries* between the Core and a generic Plugin defined? (e.g., via pure Java interfaces abstracted in the Core).
    *   How does Freeplane apply the *Dependency Inversion Principle (DIP)* to ensure that plugins depend on the Core, but not vice versa?
    *   Do plugins interact with the Core by sending DTOs (Data Transfer Objects), or do they have direct write access to domain objects (Entities)? *(Note: This is a common architectural vulnerability in desktop software).*
    *   How does the *Event Delegation / Listeners* mechanism work to bridge boundaries when a modification occurs on the map?

#### 7. Architectural Evaluation and Conclusions (Target: ~100 words)
*   **Objective:** Summarize your analysis with a critical eye.
*   **Questions to answer:**
    *   In light of your analysis, how robust, maintainable, and extensible is Freeplane's architecture?
    *   If you had to propose an architectural refactoring based on Clean Architecture principles, which part would you isolate first (e.g., stronger decoupling between the Swing UI and the map logic)?

