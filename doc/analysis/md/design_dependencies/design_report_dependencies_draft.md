## Design dependencies

In this section, we analyse two types of design dependencies in Freeplane:

- **Knowledge dependencies**
- **Code dependencies**

The idea is to look at the system from two different points of view. First, we use the Git history to understand which files tend to change together during maintenance. Then, we inspect the source code to see whether these historical relations are also visible in the current code structure.

### Knowledge dependencies

Knowledge dependencies are related to maintenance work. Two files may not directly depend on each other in the code, but they can still be connected because they are often modified together.

To estimate these dependencies, we generated co-change reports from the Git commit history. These reports show which pairs of files were modified in the same commits, and how many times this happened. If two files often change together, they may be affected by the same kind of modification. This does not prove a direct code dependency, but it gives us a useful signal about possible maintenance relations.

Starting from the co-change reports, we grouped related file pairs into functional domains instead of analysing isolated pairs. A domain is a group of files that seem to evolve together because they belong to the same feature, responsibility or integration point.

This is related to the **Common Closure Principle** discussed in class: classes that tend to change for the same reason should usually be grouped together. Therefore, co-change is not automatically a problem. It may show good cohesion, or, especially across modules, a hidden dependency worth checking in the code.

The main domains found from the co-change reports are:

1. **Swing map view domain**  
   This domain includes `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout classes. It represents the main graphical view of Freeplane: the part responsible for showing the mind map, drawing nodes, arranging them on screen and updating their visual state. This domain contains the strongest repeated co-change pairs, so it was the first one we inspected in the source code.

2. **Outline subsystem domain**  
   This domain includes `ScrollableTreePanel`, `BreadcrumbPanel`, `BlockPanel`, `OutlinePane`, `MapAwareOutlinePane`, `OutlineController` and `OutlineViewport`. Many co-change pairs are centered around `ScrollableTreePanel`, suggesting that it plays a central role. This domain is still related to map visualisation, but it represents the same map content in a tree-like structure.

3. **API and scripting domain**  
   This domain includes `Node`, `NodeRO` and `NodeProxy`. It is interesting because it crosses module boundaries: `Node` and `NodeRO` belong to `freeplane_api`, while `NodeProxy` belongs to `freeplane_plugin_script`. This suggests that the scripting plugin must stay aligned with the public API.

4. **Text rendering plugins domain**  
   This domain includes `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer`. These classes are in different plugin modules: `freeplane_plugin_formula`, `freeplane_plugin_latex` and `freeplane_plugin_markdown`. Even if they are separated, they all work on rendering or transforming text inside nodes. Their co-change may indicate that changes in node text handling can affect multiple plugins.

### Code dependencies

Code dependencies are the dependencies that can be observed directly in the source code. They appear when classes or modules are structurally connected, for example because one class uses another one, creates its objects, implements an interface, or belongs to the same package structure.

After identifying the main domains from the co-change analysis, we inspected the code to understand whether those historical relations are also present in the current implementation. The goal is not to list every import, but to interpret the dependencies: whether they show expected cohesion inside one domain, or stronger coupling between different parts of the system.

#### 1. Swing map view domain

The code inspection confirms that the Swing map view domain is not only a historical relation. `MapView`, `NodeView` and `MainView` form the main visual structure of the map: `MapView` manages the overall graphical view, `NodeView` represents a single node linked to its `NodeModel`, and `MainView` shows the visible content of the node.

<p align="center">
  <img src="../../../deliverables/img/design/SwingMapView.png" alt="Example of the Swing map view" width="700"/>
</p>

<p align="center"><em>Figure 1: example of the Swing map view in Freeplane.</em></p>

This explains why these classes often changed together. A change in how nodes are displayed, selected, folded, styled or updated can affect more than one level of the visual structure. The dependency seems mostly justified: it is strong, but linked to the same responsibility, showing and updating the visual map. This also fits the Common Closure Principle: the main classes belong to the same package area, `org.freeplane.view.swing.map`, so the code keeps together classes that tend to change for the same reason.

At the same time, to display nodes correctly, the map view needs information from many other parts of the system, such as styles, filters, text, links, icons, UI listeners and the map model. This creates high fan-out, meaning many outgoing links to other packages. This is understandable, because a visual node contains many different elements, but it also increases cognitive load: modifying this area requires understanding several connected classes and subsystems.

The code also shows one useful choice: `NodeViewFactory`. When `MapView` displays nodes, the program must create visual objects such as `NodeView`, `MainView` and other components. This is a construction dependency: the issue is not only using an object, but also where it is created. Freeplane concentrates this creation logic in `NodeViewFactory` instead of spreading it inside `MapView`, so the dependency is easier to locate.

<p align="center">
  <img src="../../../deliverables/puml/swing_map_view_dependencies.svg" alt="Swing map view dependency diagram" width="700"/>
</p>

<p align="center"><em>Figure 2: simplified code dependencies in the Swing map view domain.</em></p>

#### 2. Outline subsystem domain

After the Swing map view, we analysed another visualisation domain: the outline subsystem. While the Swing map view shows the mind map graphically, the outline shows the same nodes in a more linear structure, similar to a tree.

<p align="center">
  <img src="../../../deliverables/img/design/outlineView.png" alt="Example of the outline view" width="700"/>
</p>

<p align="center"><em>Figure 3: example of the outline view in Freeplane.</em></p>

Starting from the co-change report, the main class to check was `ScrollableTreePanel`, because many outline pairs were centered around it. The code confirms this role: `ScrollableTreePanel` manages the tree-like list shown in the outline, including visible nodes, selection, navigation and scrolling. This explains why it often changes together with other classes in the same package.

`OutlinePane` has a more external role: it builds the outline area by creating `BreadcrumbPanel`, `ScrollableTreePanel`, `OutlineController`, the toolbar and the menu. In simple terms, `OutlinePane` prepares the outline view, while `ScrollableTreePanel` manages the tree displayed inside it.

The other classes manage smaller parts of the same view. `BlockPanel` shows groups of visible nodes and sends user actions back to `ScrollableTreePanel`, such as selecting a node or opening/closing a branch. `BreadcrumbPanel` shows the path of the current node and uses `OutlineController` for selection and expansion. `OutlineViewport` helps decide which part of the outline should be visible while scrolling.

This domain also fits the Common Closure Principle: the classes that often changed together are grouped in the same package, `org.freeplane.view.swing.map.outline`, and work on the same feature. Therefore, the co-change mainly indicates internal cohesion.

The most interesting point is `MapAwareOutlinePane`. The co-change reports mainly showed internal relations in the outline domain; no direct pair with the Swing map view domain appeared. However, the code inspection shows something more: the outline is also connected to the main map view, and this connection is handled by `MapAwareOutlinePane`.

This dependency is expected, because the outline shows the same map in a tree-like form and must stay aligned with `MapView`, `NodeView`, `NodeModel` and map/node listeners. Still, it increases cognitive load: modifying the outline also requires understanding how it interacts with the map view and the node model.