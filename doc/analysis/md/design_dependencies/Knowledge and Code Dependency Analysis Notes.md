# Dependency Analysis Notes

## Purpose

This file collects the working notes for the dependency analysis of Freeplane.

The goal is not to list every dependency found in the project. Freeplane is too large, and a long list of file pairs, imports or class references would not be very useful. Instead, the idea is to use two complementary views:

- knowledge dependencies, estimated from the Git history through co-change analysis;
- code dependencies, checked later in the current source code.

The first part of the file focuses on knowledge dependencies. If two files are often modified in the same commits, this may mean that developers usually need to understand both of them when working on that part of the system. This is what we use as a sign of possible knowledge dependency.

A co-change does not automatically prove that there is a direct dependency in the code. For example, two files may change together even if one does not import the other. However, it is still useful because it shows where maintenance work tends to spread.

The second part of the file uses these results as a guide for the code dependency analysis. For the most relevant clusters, we check whether the historical relations are also visible in the source code, looking at packages, imports, interfaces, controllers, factories and module boundaries.

---

## Part 1 — Knowledge dependencies from co-change analysis

### Method

The co-change reports were generated automatically from the Git history of Freeplane.

We used three time windows:

- **last 5 years**, to see the most recent co-change relations;
- **last 10 years**, to check whether the same relations are also stable over a longer period;
- **full history**, to understand the long-term evolution of the project.

For each report, we looked at the file `top_pairs.csv`, which contains pairs of files and the number of times they changed together.

Instead of reading the pairs one by one, we grouped them by functional area. This is more useful because a single pair can be too specific, while a group of related pairs can show a real subsystem or feature area.

The main idea is simple:

- if many classes in the same area change together, this may show normal cohesion;
- if classes from different modules change together, this may suggest a hidden or stronger dependency;
- if a cluster appears in all time windows, it is probably a stable maintenance concern;
- if it appears only in recent reports, it may be a newer feature or a recently modified area.

The full-history report was useful, but we read it more carefully because it also includes older paths, such as:

`freeplane/src/org/freeplane/...`

while newer code uses paths such as:

`freeplane/src/main/java/org/freeplane/...`

So the full-history report is good for historical context, but not always enough to describe the current design.

---

### Main knowledge dependency clusters found

The same main areas appear several times in the reports:

| Cluster | Main classes | First interpretation |
|---|---|---|
| Swing map view | `MapView`, `NodeView`, `MainView`, layout classes | strongest and most stable cluster |
| Outline subsystem | `ScrollableTreePanel`, `BreadcrumbPanel`, `OutlinePane`, `OutlineController` | strong recent UI feature |
| API and scripting | `Node`, `NodeRO`, `NodeProxy`, `Proxy` | important cross-module dependency |
| Text rendering plugins | `FormulaTextTransformer`, `LatexRenderer`, `MarkdownRenderer` | separate plugins with similar maintenance concerns |
| Tag and icon management | `TagCategories`, `TagCategoryEditor`, `TagEditor`, `MIconController` | cohesive feature area |
| Code Explorer plugin | `CodeNode`, `ClassNode`, `PackageNode`, `CodeMapController` | mostly internal plugin cohesion |
| Map controllers/headless mode | `IMapViewManager`, `MapViewController`, `HeadlessMapViewController` | visible especially in the 10-year report |
| Historical infrastructure | mode factories, startup classes, file managers | useful mostly as historical context |

---

### 1. Swing map view

The clearest cluster is the Swing map view.

The main classes are:

- `freeplane/src/main/java/org/freeplane/view/swing/map/MapView.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/NodeView.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/MainView.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/NodeViewFactory.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/VerticalNodeViewLayoutStrategy.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/NodeViewLayoutHelper.java`
- `freeplane/src/org/freeplane/view/swing/map/RootMainView.java`
- `freeplane/src/org/freeplane/view/swing/map/ForkMainView.java`
- `freeplane/src/org/freeplane/view/swing/map/BubbleMainView.java`

The last three paths belong to the older project structure found in the full-history report, while the current implementation mainly uses the `freeplane/src/main/java/...` structure.

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `MapView` – `NodeView` | 68 | 75 | 89 |
| `MainView` – `NodeView` | 37 | 46 | 80 |
| `MainView` – `MapView` | 21 | 28 | 55 |
| `NodeView` – `VerticalNodeViewLayoutStrategy` | 26 | 27 | - |
| `NodeViewLayoutHelper` – `VerticalNodeViewLayoutStrategy` | 25 | 25 | - |
| `NodeView` – `NodeViewFactory` | - | - | 53 |

This is the strongest result of the analysis. `MapView` and `NodeView` are always among the top pairs, in all three time windows.

This makes sense because Freeplane is mainly a visual mind-mapping application. The map view and the node view are central parts of the system. If the way nodes are drawn, arranged or updated changes, several UI classes probably need to change together.

At this stage, this looks like a normal and expected knowledge dependency inside the main UI subsystem. However, because the cluster is very strong, it is still worth checking in the code. The important question is whether these classes are well grouped in the same subsystem, or whether the map view depends on too many unrelated parts of the application.

Things to check later:

- what `MapView`, `NodeView` and `MainView` are responsible for;
- whether they are in the same package/subsystem;
- how layout classes are connected to `NodeView`;
- whether this is good UI cohesion or excessive coupling.

---

### 2. Outline subsystem

Another clear cluster is the outline subsystem.

Main classes:

- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/ScrollableTreePanel.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/BreadcrumbPanel.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/BlockPanel.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/OutlinePane.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/MapAwareOutlinePane.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/OutlineController.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/NavigationButtons.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/NodePositioning.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/outline/OutlineViewport.java`

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `BreadcrumbPanel` – `ScrollableTreePanel` | 47 | 47 | 47 |
| `BlockPanel` – `ScrollableTreePanel` | 34 | 34 | 34 |
| `MapAwareOutlinePane` – `ScrollableTreePanel` | 33 | 33 | 33 |
| `OutlinePane` – `ScrollableTreePanel` | 30 | 30 | 30 |
| `OutlineController` – `ScrollableTreePanel` | 24 | 24 | - |

The outline cluster is very visible in the 5-year report, and the values remain the same in the 10-year and full-history reports. This suggests that most of this co-change activity is recent.

Many pairs are centered around `ScrollableTreePanel`, so this class probably plays an important role in the outline view.

This does not necessarily mean bad design. The outline is a specific feature, and it is normal that its panels, controller and positioning classes change together. It may simply be a cohesive subsystem.

The interesting point is that the outline is another representation of the same map content. So it may need to stay aligned with the main map view, especially for selection, scrolling and node positioning.

Things to check later:

- whether the outline classes are in the same package;
- how `ScrollableTreePanel` works;
- how `OutlinePane`, `MapAwareOutlinePane` and `OutlineController` interact;
- whether the outline is cleanly separated from the main map view.

---

### 3. API and scripting

This is probably the most interesting cluster from a design point of view.

Main classes:

- `freeplane_api/src/main/java/org/freeplane/api/Node.java`
- `freeplane_api/src/main/java/org/freeplane/api/NodeRO.java`
- `freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/proxy/NodeProxy.java`
- `freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/proxy/Proxy.java`
- `freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/proxy/MapProxy.java`
- `freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/proxy/ControllerProxy.java`
- `freeplane_api/src/main/java/org/freeplane/api/MindMap.java`
- `freeplane_plugin_script/src/main/java/org/freeplane/plugin/script/proxy/HeadlessMapCreator.java`

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `Node` – `NodeRO` | 19 | 25 | - |
| `Node` – `NodeProxy` | 17 | 20 | - |
| `NodeRO` – `NodeProxy` | 16 | 27 | 27 |
| `NodeProxy` – `Proxy` | - | 13 | 49 |
| `MindMap` – `MapProxy` | - | 10 | - |
| `HeadlessMapCreator` – `ControllerProxy` | - | 10 | - |

This cluster crosses module boundaries. `Node` and `NodeRO` are part of `freeplane_api`, while `NodeProxy` and the other proxy classes belong to `freeplane_plugin_script`.

This suggests that the scripting plugin must stay aligned with the public API. Scripts need to access maps, nodes and controllers, but they do so through proxy classes. So, when the public API changes, the scripting proxies may need to change too.

This is a good example of knowledge dependency that is not just internal cohesion. The modules are separated in the repository, but the Git history shows that they evolve together.

This can be a good design if the scripting plugin depends only on public interfaces. It would be more problematic if it also depends on internal implementation details.

Things to check later:

- which methods are exposed by `Node` and `NodeRO`;
- whether `NodeProxy` implements, wraps or adapts those interfaces;
- how scripts access nodes and maps;
- whether the scripting plugin depends only on API classes or also on internal classes.

---

### 4. Text rendering plugins

Another useful case is the group of text rendering plugins.

Main classes:

- `freeplane_plugin_formula/src/main/java/org/freeplane/plugin/formula/FormulaTextTransformer.java`
- `freeplane_plugin_latex/src/main/java/org/freeplane/plugin/latex/LatexRenderer.java`
- `freeplane_plugin_markdown/src/main/java/org/freeplane/plugin/markdown/MarkdownRenderer.java`
- `freeplane/src/main/java/org/freeplane/features/text/mindmapmode/MTextController.java`

Representative pairs:

| Pair | 5 years | 10 years | Full history |
|---|---:|---:|---:|
| `LatexRenderer` – `MarkdownRenderer` | 17 | 17 | - |
| `FormulaTextTransformer` – `LatexRenderer` | 14 | 16 | - |
| `FormulaTextTransformer` – `MarkdownRenderer` | 13 | 13 | - |
| `MTextController` – `FormulaTextTransformer` | 10 | 10 | - |
| `MTextController` – `MarkdownRenderer` | 9 | - | - |
| `MTextController` – `LatexRenderer` | 9 | - | - |

Formula, LaTeX and Markdown are separate plugin areas, but their renderer or transformer classes appear together in the co-change reports.

A possible reason is that they all work on special text content inside nodes. So, if Freeplane changes how node text is transformed or rendered, several plugins may be affected at the same time.

This is useful because it shows that plugin separation does not always mean full maintenance independence. Different plugins can still share the same general concern.

Things to check later:

- what each renderer/transformer does;
- whether they share common text APIs;
- what role `MTextController` has;
- whether this is a direct code dependency or just a similar maintenance concern.

---

### 5. Other clusters

Some other clusters are useful, but probably secondary for the final report.

#### Tag and icon management

Main classes:

- `freeplane/src/main/java/org/freeplane/features/icon/mindmapmode/TagCategories.java`
- `freeplane/src/main/java/org/freeplane/features/icon/mindmapmode/TagCategoryEditor.java`
- `freeplane/src/main/java/org/freeplane/features/icon/mindmapmode/TagEditor.java`
- `freeplane/src/main/java/org/freeplane/features/icon/mindmapmode/MIconController.java`

This looks like a cohesive feature area. Model/data classes, editors and controllers change together. This is probably expected: if the structure of tags changes, the editor and controller may need updates.

#### Code Explorer plugin

Main classes:

- `freeplane_plugin_codeexplorer/src/main/java/org/freeplane/plugin/codeexplorer/CodeNode.java`
- `freeplane_plugin_codeexplorer/src/main/java/org/freeplane/plugin/codeexplorer/ClassNode.java`
- `freeplane_plugin_codeexplorer/src/main/java/org/freeplane/plugin/codeexplorer/PackageNode.java`
- `freeplane_plugin_codeexplorer/src/main/java/org/freeplane/plugin/codeexplorer/ProjectRootNode.java`
- `freeplane_plugin_codeexplorer/src/main/java/org/freeplane/plugin/codeexplorer/CodeMapController.java`

This is mostly internal to the Code Explorer plugin. It may be useful as an example of internal plugin cohesion, but it is less interesting than API/scripting because it does not clearly cross module boundaries.

#### Map controllers and headless mode

Main classes:

- `freeplane/src/main/java/org/freeplane/features/ui/IMapViewManager.java`
- `freeplane/src/main/java/org/freeplane/view/swing/map/MapViewController.java`
- `freeplane/src/main/java/org/freeplane/main/headlessmode/HeadlessMapViewController.java`

This appears especially in the 10-year report. It may help us understand how Freeplane separates normal UI mode from headless behavior.

#### Historical infrastructure

The full-history report also shows older clusters:

- mode controller factories;
- startup classes;
- `Controller`, `ViewController`, `MenuBuilder`;
- file management and import/export actions.

These are useful to understand the old evolution of the system. However, some paths belong to older project structures, so they should be used carefully when discussing the current design.

---

## Part 2 — Code dependency analysis

After the co-change analysis, we inspected the source code of the main clusters found in the Git history. The goal is not to list all imports mechanically, but to understand whether the historical relations are also visible in the current code structure.

For each cluster, we check packages, class references, interfaces, construction points and module boundaries. Then we ask whether the dependency is expected cohesion inside one subsystem, or whether it suggests stronger coupling between different parts of Freeplane.

This follows the idea discussed in class: dependencies are not automatically bad. They become problematic when they are hidden, too strong, fragile, or when they force developers to understand too many other parts of the system before making a change.

The following sections analyse the main clusters found in the co-change reports, starting from the Swing map view.

### 1. Swing map view

![Map view dependency diagram](../../../img/design/map_view_dependencies.png)

*Figure: simplified relation between `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and `NodeModel`.*

The first code dependency case we analysed is the Swing map view cluster. It was the strongest cluster in the co-change analysis: `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout classes appeared together in all three time windows. For this reason, we used it as the first area to inspect in the source code.

The code confirms that this is not just an accidental historical relation. These classes work together to show the mind map on the screen. The basic structure is:

- `MapView` is the graphical area where the whole mind map is shown;
- `NodeView` is the graphical representation of a single node inside that map;
- `MainView` is the internal part of the node where the main content is displayed, such as text, icons, borders and link indicators.

In practice, `MapView` coordinates the general visualisation of the map. It does not represent one single node, but manages the overall view, selection, scrolling and updates. Inside `MapView`, each node is represented by a `NodeView`. This `NodeView` is connected both to the `NodeModel`, which contains the data of the node, and to the `MapView`, because the node has to be displayed inside a specific map view. Inside the `NodeView`, the `MainView` shows the part that the user sees immediately, namely the main content of the node.

This explains why these classes often change together. If the way nodes are shown or behave on screen changes, the modification can involve several levels of the view: the whole map (`MapView`), the graphical node (`NodeView`) and the node content (`MainView`). For example, changes related to selection, folding, style, icons or text rendering can easily affect more than one of these classes.

From a design point of view, this dependency seems largely justified. It is a strong dependency, but also a well-motivated one: the classes are connected because they contribute to the same responsibility, which is showing and updating the visual map. This is consistent with the Common Closure Principle discussed in class: classes that often change for the same reason should stay in the same subsystem or at least be organised together.

The most delicate point is that the Swing map view does not work only with these three classes. To display a node correctly, it needs information coming from many other parts of the system: the map model, styles, filters, text, links, icons and UI listeners. This creates high fan-out, meaning many connections towards other packages. In this case it is understandable, because a node on screen is not just text: it also has style, icons, links, folding state, visibility depending on filters and user interactions. However, the more connections there are, the more the cognitive load increases: to understand or modify this area, a developer cannot look at one class only, but has to follow how it collaborates with several other parts of the system.

The code also shows some choices that make these dependencies more organised. A clear example is `NodeViewFactory`. When `MapView` shows the nodes of the map, the program has to create the graphical objects needed to represent them, such as `NodeView`, `MainView` and other visual components. If this creation were done directly inside `MapView`, that class would also need to know many details about how each graphical part of a node is built.

This is where the concept of construction dependency appears. A construction dependency means that a class does not only use another class, but is also responsible for creating its objects. In Freeplane this dependency does not disappear completely, because `NodeView`, `MainView` and the other components still have to be created somewhere. However, it is handled better: the creation logic is concentrated in `NodeViewFactory` instead of being spread inside `MapView`. In this way, `MapView` can stay more focused on managing the map, while `NodeViewFactory` collects the construction of the visual node components. This makes the relation more ordered and easier to control.

In conclusion, the Swing map view cluster confirms what we had already seen in the historical analysis. The co-change analysis showed that these files often change together; the code explains why this happens: they really work on the same part of the system, the visualisation of the map. So the dependency does not seem random or negative by itself. It is an expected and motivated dependency. At the same time, it is a heavy area of the code: understanding it requires following how several UI elements and connected subsystems work together, not just reading one isolated class.