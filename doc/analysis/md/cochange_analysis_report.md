# Co-change Analysis Report

## Purpose of this document

This document summarizes the analysis of the co-change reports generated from the Git history of Freeplane.

The goal of this file is not to list every pair of files in the reports. Instead, the purpose is to identify the main areas of the system that tend to change together and that are therefore worth checking in the code during the design analysis.

In this work, co-change is used as an indication of **knowledge dependency**. If two files are often modified in the same commits, it is likely that developers need to understand both of them when making certain changes. This does not automatically mean that there is a direct code dependency, but it gives us useful hints about where to look.

For this reason, the results of this analysis will later be compared with the static structure of the code, such as packages, imports, interfaces, controllers and module organization.

---

## Method

The analysis is based on three co-change reports:

- **last 5 years**, to focus on the most recent evolution of the project;
- **last 10 years**, to check whether the same relations are also stable over a longer period;
- **full history**, to get a broader historical view of the project.

Each report contains pairs of files/classes, together with the number of times they changed together.

Instead of only taking the highest pairs one by one, the pairs were grouped by functional area. This makes the analysis more meaningful, because a single pair may be too specific, while a group of related pairs can point to a subsystem or to a recurring maintenance area.

The analysis was done in three steps:

1. first, the last-5-years report was used to identify the main recent clusters;
2. then, these clusters were compared with the last-10-years report;
3. finally, the full-history report was used to understand which relations are long-term and which ones are mainly historical.

For each cluster, the report considers:

- the main classes that appear;
- how the cluster changes across the three time windows;
- possible reasons for this behavior;
- what should be checked later in the code.

---

## Overview of the main clusters

| Cluster | Main emerging classes | General interpretation |
|---|---|---|
| Swing map view | `MapView`, `NodeView`, `MainView`, `NodeViewFactory`, layout classes | strongest and most stable area |
| Outline subsystem | `ScrollableTreePanel`, `BreadcrumbPanel`, `OutlinePane`, `MapAwareOutlinePane`, `OutlineController` | strong recent feature area |
| API and scripting | `Node`, `NodeRO`, `NodeProxy`, `Proxy`, `MapProxy`, `ControllerProxy` | important cross-module dependency |
| Text rendering plugins | `FormulaTextTransformer`, `LatexRenderer`, `MarkdownRenderer`, `MTextController` | separate plugins that evolve together |
| Tag and icon management | `TagCategories`, `TagCategoryEditor`, `TagEditor`, `MIconController` | cohesive recent feature area |
| Code Explorer plugin | `CodeNode`, `ClassNode`, `PackageNode`, `ProjectRootNode`, `CodeMapController` | mainly internal plugin cohesion |
| Map controllers and headless mode | `IMapViewManager`, `MapViewController`, `HeadlessMapViewController` | controller-related area visible especially in the 10-year report |
| Historical infrastructure | mode controller factories, startup classes, file managers | useful mainly as historical context |

---

## 1. Swing map view

The strongest cluster is related to the Swing map view.

The main classes that appear are:

- `MapView`;
- `NodeView`;
- `MainView`;
- `NodeViewFactory`;
- `VerticalNodeViewLayoutStrategy`;
- `NodeViewLayoutHelper`;
- `NodeViewLayoutAdapter`;
- `RootMainView`;
- `ForkMainView`;
- `BubbleMainView`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `MapView` – `NodeView` | 68 | 75 | 89 |
| `MainView` – `NodeView` | 37 | 46 | 80 |
| `MainView` – `MapView` | 21 | 28 | 55 |
| `NodeView` – `VerticalNodeViewLayoutStrategy` | 26 | 27 | - |
| `NodeViewLayoutHelper` – `VerticalNodeViewLayoutStrategy` | 25 | 25 | - |
| `NodeView` – `NodeViewFactory` | - | - | 53 |

This cluster is already very strong in the last-5-years report. It remains strong in the last-10-years report, and it is also one of the most visible areas in the full-history report. This means that the relation between map view, node view and layout classes is not only recent, but has been important for a long part of the project history.

This result is quite expected, because Freeplane is mainly a mind-mapping application. The visual representation of the map is one of the core parts of the system. If the way nodes are displayed, arranged or rendered changes, several classes probably need to be updated together.

For this reason, the Swing map view is the clearest example of a stable knowledge dependency.

Things to verify in the code:

- what responsibilities `MapView`, `NodeView` and `MainView` have;
- whether these classes are located in the same package or subsystem;
- how the layout-related classes are connected to `NodeView`;
- whether the co-change corresponds to direct code dependencies;
- whether this is normal cohesion inside the UI subsystem or a sign of strong coupling.

---

## 2. Outline subsystem

Another important cluster is the outline subsystem.

The main classes that appear are:

- `ScrollableTreePanel`;
- `BreadcrumbPanel`;
- `BlockPanel`;
- `OutlinePane`;
- `MapAwareOutlinePane`;
- `OutlineController`;
- `NavigationButtons`;
- `NodePositioning`;
- `OutlineViewport`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `BreadcrumbPanel` – `ScrollableTreePanel` | 47 | 47 | 47 |
| `BlockPanel` – `ScrollableTreePanel` | 34 | 34 | 34 |
| `MapAwareOutlinePane` – `ScrollableTreePanel` | 33 | 33 | 33 |
| `OutlinePane` – `ScrollableTreePanel` | 30 | 30 | 30 |
| `OutlineController` – `ScrollableTreePanel` | 24 | 24 | - |

This cluster is very strong in the last-5-years report, but the values remain almost the same in the last-10-years and full-history reports. This suggests that most of the relevant co-change activity for the outline subsystem happened in the most recent years.

A possible explanation is that the outline view is a recent or recently modified part of the application. Many pairs are centered around `ScrollableTreePanel`, so this class probably has an important role in the implementation of the outline view.

This cluster looks compact and feature-oriented. It may simply show that the classes of the outline feature evolve together, which is not necessarily a design problem. However, it is still useful to check whether the outline is independent or whether it is strongly connected to the main map view.

Things to verify in the code:

- whether these classes are in the same outline package;
- what `ScrollableTreePanel` does;
- how `OutlinePane`, `MapAwareOutlinePane` and `OutlineController` interact;
- whether the outline depends directly on the main map view;
- whether this cluster represents good feature cohesion or tight coupling with other UI parts.

---

## 3. API and scripting

One of the most interesting clusters is the relation between the public API and the scripting plugin.

The main classes that appear are:

- `Node`;
- `NodeRO`;
- `NodeProxy`;
- `Proxy`;
- `MapProxy`;
- `ControllerProxy`;
- `MindMap`;
- `HeadlessMapCreator`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `Node` – `NodeRO` | 19 | 25 | - |
| `Node` – `NodeProxy` | 17 | 20 | - |
| `NodeRO` – `NodeProxy` | 16 | 27 | 27 |
| `NodeProxy` – `Proxy` | - | 13 | 49 |
| `MindMap` – `MapProxy` | - | 10 | - |
| `HeadlessMapCreator` – `ControllerProxy` | - | 10 | - |

This cluster is already visible in the last-5-years report, becomes stronger in the last-10-years report, and is also confirmed in the full-history report through scripting-related classes such as `NodeProxy`, `Proxy`, `ScriptingEngine` and `ScriptingRegistration`.

This is important because it crosses module boundaries. `Node` and `NodeRO` belong to the public API area, while `NodeProxy` and the other proxy classes belong to the scripting plugin. This suggests that when the public node API changes, the scripting layer may need to change as well.

A possible reason is that scripts need to access Freeplane concepts such as maps and nodes, but they do it through proxy classes. These proxy classes probably have to stay aligned with the public API. So even if the modules are separated in the repository, they are still connected from a maintenance point of view.

This is one of the best candidates for the final Design report, because it shows a knowledge dependency between separate modules.

Things to verify in the code:

- which methods are exposed by `Node` and `NodeRO`;
- whether `NodeProxy` implements, wraps or adapts these interfaces;
- how scripts access nodes and maps;
- whether this dependency is visible through imports, inheritance or interface implementation;
- whether the scripting plugin depends only on public APIs or also on internal classes.

---

## 4. Text rendering plugins

Another relevant cluster concerns text rendering and transformation.

The main classes that appear are:

- `FormulaTextTransformer`;
- `LatexRenderer`;
- `MarkdownRenderer`;
- `MTextController`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `LatexRenderer` – `MarkdownRenderer` | 17 | 17 | - |
| `FormulaTextTransformer` – `LatexRenderer` | 14 | 16 | - |
| `FormulaTextTransformer` – `MarkdownRenderer` | 13 | 13 | - |
| `MTextController` – `FormulaTextTransformer` | 10 | 10 | - |
| `MTextController` – `MarkdownRenderer` | 9 | - | - |
| `MTextController` – `LatexRenderer` | 9 | - | - |

This cluster appears in the last-5-years report and is confirmed in the last-10-years report. It is less visible in the full-history report, so it seems more related to recent plugin evolution than to the oldest phases of the project.

The interesting point is that the classes belong to different plugins or text-related areas, but they still appear together in the co-change data. A possible explanation is that Formula, LaTeX and Markdown all deal with special text content inside nodes. Therefore, when the handling or rendering of node text changes, more than one plugin may be affected.

This is useful because it shows that a modular plugin structure does not always mean complete independence during maintenance.

Things to verify in the code:

- what `FormulaTextTransformer` does;
- how `LatexRenderer` and `MarkdownRenderer` work;
- whether they share common interfaces or text APIs;
- what role `MTextController` has;
- whether the co-change is caused by direct dependencies or by similar maintenance concerns across plugins.

---

## 5. Tag and icon management

Another cluster is related to tags, tag categories and icons.

The main classes that appear are:

- `TagCategories`;
- `TagCategoryEditor`;
- `TagEditor`;
- `MIconController`;
- `IconController`;
- `Tag`;
- `IconRegistry`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `TagCategories` – `TagCategoryEditor` | 32 | 32 | 32 |
| `TagCategoryEditor` – `TagEditor` | 23 | 23 | - |
| `MIconController` – `TagEditor` | 21 | 21 | - |
| `MIconController` – `TagCategoryEditor` | 18 | 18 | - |
| `TagCategories` – `TagEditor` | 14 | 14 | - |
| `TagCategories` – `MIconController` | 12 | 12 | - |

The values are almost identical in the last-5-years and last-10-years reports. In the full-history report, this area is only partially visible. This suggests that tag and icon management is mainly a recent co-change area.

A possible explanation is that tags and icons are related user-facing features. If the structure of tag categories changes, the editor and controller logic may also need to change. The co-change connects model/data classes, UI editors and controllers.

This cluster seems to show feature cohesion. It is useful as supporting evidence, but probably less important than Swing map view or API/scripting for the final Design report.

Things to verify in the code:

- whether `TagCategories` represents the model/data structure;
- what `TagCategoryEditor` and `TagEditor` do;
- how `MIconController` connects tags and icons;
- whether related tests also appear in the co-change data;
- whether the cluster remains inside one feature or spreads across different modules.

---

## 6. Code Explorer plugin

The Code Explorer plugin appears as another cohesive cluster.

The main classes that appear are:

- `CodeNode`;
- `ClassNode`;
- `ClassesNode`;
- `PackageNode`;
- `ProjectRootNode`;
- `CodeMap`;
- `CodeMapController`;
- `CodeExplorerConfigurator`;
- `CodeProjectController`;
- `CodeExplorerConfiguration`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `ClassNode` – `CodeNode` | 18 | 18 | - |
| `ClassesNode` – `PackageNode` | 18 | 18 | - |
| `CodeExplorerConfigurator` – `CodeProjectController` | 17 | 17 | - |
| `CodeMapController` – `CodeExplorerConfiguration` | 17 | 17 | - |
| `ClassesNode` – `CodeNode` | 16 | 16 | - |
| `CodeNode` – `ProjectRootNode` | 16 | 16 | - |

The values are almost identical in the last-5-years and last-10-years reports. This suggests that the relevant co-change activity is concentrated in the recent part of the history.

This cluster is mostly internal to a plugin. A possible explanation is that the Code Explorer plugin contains several classes that represent elements of a code structure, such as classes, packages and project roots. When the internal model or behavior of the plugin changes, several of these classes may need to be updated together.

This is useful as an example of internal plugin cohesion, but it is probably not a primary case for the final Design report unless the code analysis reveals strong dependencies with the core.

Things to verify in the code:

- how `CodeNode`, `ClassNode`, `PackageNode` and `ProjectRootNode` are related;
- what `CodeMapController` coordinates;
- whether the plugin is mostly isolated from the core;
- whether the plugin uses common Freeplane APIs or depends on internal classes.

---

## 7. Map controllers and headless mode

A cluster that becomes more visible in the last-10-years report is related to map controllers and headless mode.

The main classes that appear are:

- `IMapViewManager`;
- `MapViewController`;
- `HeadlessMapViewController`;
- `FrameController`;
- `ViewController`;
- `HeadlessUIController`.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `IMapViewManager` – `HeadlessMapViewController` | - | 27 | - |
| `IMapViewManager` – `MapViewController` | - | 27 | - |
| `HeadlessMapViewController` – `MapViewController` | - | 26 | - |
| `FrameController` – `ViewController` | - | 18 | present |
| `ViewController` – `HeadlessUIController` | - | 14 | present |

This cluster is not very visible in the last-5-years report, but it appears clearly in the last-10-years report. In the full-history report, related controller and UI infrastructure classes are also present, although usually as part of broader historical clusters.

A possible explanation is that Freeplane supports both normal graphical usage and headless behavior. If both modes share part of the map management logic, then changes in one controller may require changes in the other.

This cluster is useful because it can help connect the co-change analysis with the static dependency analysis. In particular, it can show whether Freeplane separates UI-dependent and UI-independent logic clearly.

Things to verify in the code:

- what `IMapViewManager` defines;
- how `MapViewController` and `HeadlessMapViewController` differ;
- whether the headless controller reuses or duplicates UI controller logic;
- whether this area clearly separates UI and non-UI behavior.

---

## 8. Historical clusters from the full-history report

The full-history report also highlights some older areas that are not central in the recent reports.

Examples include:

| Historical area | Example classes/pairs | Possible interpretation |
|---|---|---|
| Mode controllers and startup | `BModeControllerFactory`, `MModeControllerFactory`, `FModeControllerFactory`, `FreeplaneStarter` | older work around application modes and initialization |
| Core controllers and UI infrastructure | `Controller`, `ViewController`, `MenuBuilder`, `ResourceController` | central infrastructure evolved together with the UI |
| File management and import/export | `MFileManager`, `RevertAction`, `ExportBranchAction`, `ImportLinkedBranchAction` | older concerns related to persistence and map file operations |
| Scripting internals | `NodeProxy`, `Proxy`, `ScriptingEngine`, `ScriptingRegistration` | scripting has been historically important |

These clusters are useful to understand the long-term evolution of Freeplane, but they should be used carefully. Some paths in the full-history report refer to older project structures, for example `freeplane/src/org/freeplane/...`, instead of the more recent `freeplane/src/main/java/org/freeplane/...`.

For this reason, the full-history report should not be used alone to describe the current design. It is more useful as historical context and as confirmation of long-term recurring areas, especially the Swing map view and scripting.

---

## Main conclusions

The co-change analysis shows that the most relevant knowledge dependencies are not randomly distributed across the repository. They are concentrated in a limited number of recurring areas.

The strongest result is the **Swing map view**, which appears as a dominant cluster in all three time windows. This makes it the best example of a stable and central knowledge dependency.

The **outline subsystem**, **tag/icon management** and **Code Explorer plugin** appear mainly as strong recent clusters. Their values are mostly unchanged between the last-5-years and last-10-years reports, so their co-change activity seems concentrated in the recent history of the project.

The **API and scripting** cluster is particularly important because it crosses module boundaries. It becomes stronger in the last-10-years report and is also supported by the full-history report. This makes it a good example of a knowledge dependency that may be less obvious from the repository structure alone.

The **text rendering plugins** show that separated plugins can still evolve together when they address similar concerns. This can be useful to discuss hidden maintenance dependencies between modular parts of the system.

Finally, the full-history report shows older clusters related to startup, mode controllers, UI infrastructure and file management. These areas are useful as historical context, but they are less representative of the current design and should probably not be the main focus of the final report.

---

## Suggested next steps for code analysis

Based on the co-change results, the next code inspection phase should focus on the following areas.

1. **Swing map view**  
   Check `MapView`, `NodeView`, `MainView` and layout-related classes.  
   The goal is to verify whether the strongest historical co-change cluster corresponds to strong static dependencies.

2. **API and scripting**  
   Check `Node`, `NodeRO`, `NodeProxy`, `Proxy`, `MapProxy` and `ControllerProxy`.  
   The goal is to analyse a cross-module dependency between the public API and the scripting plugin.

3. **Outline subsystem**  
   Check `ScrollableTreePanel`, `OutlinePane`, `MapAwareOutlinePane` and `OutlineController`.  
   The goal is to understand whether this is a cohesive independent subsystem or whether it is tightly connected to the main map view.

4. **Text rendering plugins**  
   Check `FormulaTextTransformer`, `LatexRenderer`, `MarkdownRenderer` and `MTextController`.  
   The goal is to understand why separated text-related plugins evolve together.

5. **Map controllers and headless mode**  
   Check `IMapViewManager`, `MapViewController` and `HeadlessMapViewController`.  
   The goal is to understand how normal UI mode and headless mode share controller logic.

Secondary areas, such as tag/icon management, Code Explorer, command search and style editing, can be used as supporting examples if needed.

---

## Use in the Design report

This file is an intermediate analysis document. The final Design report should not include all the tables and observations in full. Instead, it should use this analysis to select a small number of meaningful examples.

The most useful examples for the final report are:

- **Swing map view**, as the strongest stable knowledge dependency;
- **API and scripting**, as the clearest cross-module dependency;
- **Outline subsystem**, as a strong recent cohesive subsystem;
- **Text rendering plugins**, as an example of separate plugins that evolve together.

These examples will then be compared with the static code dependencies, to understand whether the historical evolution of Freeplane is consistent with its current modular structure.