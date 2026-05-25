## Design dependencies

In this section, we analyse two kinds of dependencies in Freeplane. **Knowledge dependencies** are estimated from the Git history and show which files tend to change together during maintenance. **Code dependencies** are observed directly in the source code, through packages, class references, construction points and structural relations.

The goal is not to list dependencies mechanically, but to compare these two views. The interesting point is to understand whether the historical relations found in the commits are also visible in the current code, and whether they represent good cohesion or more delicate coupling.

### Knowledge dependencies

To study knowledge dependencies, we generated co-change reports from the Git history. These reports list pairs of files modified in the same commits, together with the number of times this happened. This does not mean that the two files necessarily import each other. However, if two files often change in the same commit, there may be a maintenance relation between them: developers probably need to understand both when modifying that part of the system.

Since Freeplane is large, we used these reports as a first map of the codebase. Instead of analysing isolated file pairs, we grouped them into functional domains. A domain is a group of files that seem to evolve together because they belong to the same feature, responsibility or integration point.

This idea is connected to the **Common Closure Principle** discussed in class: classes that tend to change for the same reason should usually be grouped together. For this reason, co-change is not automatically a problem. Sometimes it shows good cohesion. In other cases, especially when files belong to different modules, it may suggest a hidden dependency that is worth checking in the code.

The main domains found from the co-change reports are:

1. **Swing map view domain**  
   This domain includes `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout classes. It represents the main graphical view of Freeplane: the part responsible for showing the mind map, drawing nodes, arranging them on screen and updating their visual state. Since these classes appear together in all reports (anche le altre apparigano togheder, ma quetse sono quelle con piu commit assieme, quindi l'accoppiamenti + forti!), this was the first domain we inspected in the source code.

2. **Outline subsystem domain**  
   This domain includes `ScrollableTreePanel`, `BreadcrumbPanel`, `BlockPanel`, `OutlinePane`, `MapAwareOutlinePane`, `OutlineController` and `OutlineViewport`. Many co-change pairs are centered around `ScrollableTreePanel`, suggesting that it plays a central role. This domain is still related to map visualisation, but it represents the same map content in a tree-like structure instead of the normal graphical map view.

3. **API and scripting domain**  
   This domain includes `Node`, `NodeRO` and `NodeProxy`. It is interesting because it crosses module boundaries: `Node` and `NodeRO` belong to `freeplane_api`, while `NodeProxy` belongs to `freeplane_plugin_script`. This suggests that the scripting plugin must stay aligned with the public API.

4. **Text rendering plugins domain**  
   This domain includes `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer`. These classes belong to different plugin modules (non capisco cosa significhi... puoi essere + chiaro????? o e se èe cpme l'api domaina anche qui metti i path), related to formula, LaTeX and Markdown support. However, they all work on the same general concern: rendering or transforming text inside nodes. Their co-change may indicate that changes in node text handling can affect multiple plugins at the same time.

This first analysis gives us a set of relevant domains to inspect in the code, so that we can compare knowledge dependencies with actual code dependencies.

### Code dependencies

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