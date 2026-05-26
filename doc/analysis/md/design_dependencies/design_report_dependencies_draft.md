## Design dependencies

In this section, we analyse two types of design dependencies in Freeplane:

- **Knowledge dependencies**
- **Code dependencies**

We first use Git history to find files that changed together, then inspect the code to check whether those relations are visible in the current implementation.

### Knowledge dependencies

Knowledge dependencies are related to maintenance work. Two files may not directly depend on each other in the code, but they can still be connected because they are often modified together.

To estimate these dependencies, we generated co-change reports from the Git commit history. These reports show which pairs of files were modified in the same commits, and how many times this happened. Frequent co-change does not prove a direct code dependency, but it suggests that the files may be affected by the same kind of change.

Starting from these reports, we grouped related file pairs into functional domains instead of analysing isolated pairs. A domain is a group of files that seem to evolve together because they belong to the same feature, responsibility or integration point.

This is related to the **Common Closure Principle** discussed in class: classes that tend to change for the same reason should usually be grouped together. Therefore, co-change is not automatically a problem. It may show good cohesion, or, especially across modules, a hidden dependency worth checking in the code.

The main domains found from the co-change reports are:

1. **Swing map view domain**  
   Includes `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout classes. It represents the main graphical view of Freeplane and contains the strongest repeated co-change pairs, so it was the first domain inspected in the source code.

2. **Outline subsystem domain**  
   Includes `ScrollableTreePanel`, `BreadcrumbPanel`, `BlockPanel`, `OutlinePane`, `MapAwareOutlinePane`, `OutlineController` and `OutlineViewport`. It is still related to map visualisation, but it represents the same map content in a tree-like structure.

3. **API and scripting domain**  
   Includes `Node`, `NodeRO` and `NodeProxy`. This case crosses module boundaries: `Node` and `NodeRO` belong to `freeplane_api`, while `NodeProxy` belongs to `freeplane_plugin_script`.

4. **Text rendering plugins domain**  
   Includes `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer`. These classes are in different plugin modules, but all work on rendering or transforming text inside nodes.

### Code dependencies

Code dependencies are visible in the source code, for example through class usage, object creation, interfaces and package structure. We use them to check the domains identified through co-change.

#### 1. Swing map view domain

The code inspection confirms that the Swing map view domain is not only a historical relation. `MapView`, `NodeView` and `MainView` form the main visual structure of the map: `MapView` manages the overall graphical view, `NodeView` represents a single node linked to its `NodeModel`, and `MainView` shows the visible content of the node.

<p align="center">
  <img src="../../../deliverables/img/design/SwingMapView.png" alt="Swing map view" width="700"/>
</p>

<p align="center"><em>Figure 1: Swing map view.</em></p>

This explains why these classes often changed together. A change in how nodes are displayed, selected, folded, styled or updated can affect more than one level of the visual structure. The dependency seems mostly justified: it is strong, but linked to the same responsibility, showing and updating the visual map. This also fits the Common Closure Principle: the main classes belong to the same package area, `org.freeplane.view.swing.map`, so the code keeps together classes that tend to change for the same reason.

At the same time, the map view needs information from styles, filters, text, links, icons, UI listeners and the map model. This creates high fan-out, meaning many outgoing links to other packages. This is understandable, because a visual node contains many elements, but it also increases cognitive load: modifying this area requires understanding several connected classes and subsystems.

The code also shows one useful choice: `NodeViewFactory`. When `MapView` displays nodes, the program must create visual objects such as `NodeView`, `MainView` and other components. This is a construction dependency: the issue is not only using an object, but also where it is created. Freeplane concentrates this creation logic in `NodeViewFactory` instead of spreading it inside `MapView`, so the dependency is easier to locate.

<p align="center">
  <img src="../../../deliverables/puml/swing_map_view_dependencies.svg" alt="Swing map view dependencies" width="700"/>
</p>

<p align="center"><em>Figure 2: Swing map view dependencies.</em></p>

#### 2. Outline subsystem domain

After the Swing map view, we analysed another visualisation domain: the outline subsystem. While the Swing map view shows the mind map graphically, the outline shows the same nodes in a more linear structure, similar to a tree.

<p align="center">
  <img src="../../../deliverables/img/design/outlineView.png" alt="Outline view" width="700"/>
</p>

<p align="center"><em>Figure 3: Outline view.</em></p>

Starting from the co-change report, the main class to check was `ScrollableTreePanel`, because many outline pairs were centered around it. The code confirms this role: `ScrollableTreePanel` manages the tree-like list shown in the outline, including visible nodes, selection, navigation and scrolling.

`OutlinePane` builds the outline area by creating `BreadcrumbPanel`, `ScrollableTreePanel`, `OutlineController`, the toolbar and the menu. So, `OutlinePane` prepares the outline view, while `ScrollableTreePanel` manages the tree displayed inside it.

The other classes manage smaller parts of the same view. `BlockPanel` shows groups of visible nodes and sends user actions back to `ScrollableTreePanel`. `BreadcrumbPanel` shows the path of the current node and uses `OutlineController` for selection and expansion. `OutlineViewport` helps decide which part of the outline should be visible while scrolling.

This domain also fits the Common Closure Principle: the classes that often changed together are grouped in the same package, `org.freeplane.view.swing.map.outline`, and work on the same feature. Therefore, the co-change mainly indicates internal cohesion.

The most interesting point is `MapAwareOutlinePane`. The co-change reports mainly showed internal relations in the outline domain; no direct pair with the Swing map view domain appeared. However, the code inspection shows that the outline is also connected to the main map view, and this connection is handled by `MapAwareOutlinePane`.

This dependency is expected, because the outline shows the same map in a tree-like form and must stay aligned with `MapView`, `NodeView`, `NodeModel` and map/node listeners. Still, it increases cognitive load: modifying the outline also requires understanding how it interacts with the map view and the node model.

<!-- Add outline PlantUML dependency diagram here when export is fixed. -->

## 3. API and scripting domain

The API and scripting cluster is different from the UI clusters because it connects different parts of Freeplane: the public API, the scripting plugin and the internal model.

<p align="center">
  <img src="../../../deliverables/img/design/API_and_scripting_schema.png" alt="API and scripting" width="700"/>
</p>

<p align="center"><em>Figure 4: API and scripting access path.</em></p>

Scripts are small pieces of code used to automate actions on mind maps. To support them, Freeplane exposes a public API. `NodeRO` gives read-only access to a node, while `Node` extends it by adding operations that can modify the node. `MindMap` represents the map that scripts can access and work on.

The co-change relation suggested that the public API and the scripting plugin evolve together. The code confirms this: scripts do not work directly on the internal model, but pass through proxy classes. `NodeProxy` exposes the node API to scripts, while internally working with `NodeModel`, which stores the real node data. Similarly, `MapProxy` exposes `MindMap`, while internally working with `MapModel`, which stores the real map structure.

Therefore, this is not just internal cohesion. It is a real dependency between scripting and the Freeplane core, but it is controlled by the proxy layer. The design is well organised because the API remains a stable access layer. However, this point is still delicate: the proxies protect the internal model, but they also need to know both the public API and the internal model.

#### 4. Text rendering plugins domain

The text rendering plugins domain is a smaller case, but it is useful because it shows a different kind of dependency. `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer` belong to three different plugins: one handles formulas, one handles LaTeX and one handles Markdown.

In the co-change reports, these classes often change together. However, in the code they do not import or use each other, so this is not direct coupling between plugins.

The reason for their connection in the co-change reports is that they all handle special text inside nodes. When Freeplane displays or edits a node, its content may require a specific transformation before being shown to the user. These transformations pass through the same content-transformer mechanism used by `MTextController`.

Therefore, the co-change is confirmed as a shared maintenance concern, not as direct code dependency. The design is mostly good: the plugins remain separated, but changes in the central text mechanism can still affect more than one plugin.