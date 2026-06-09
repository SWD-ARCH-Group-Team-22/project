## Design dependencies

We first used Git history to identify possible **knowledge dependencies**. Then, for the main domains found, we inspected the related source files to check the **code dependencies**, comparing the two levels and analysing the interesting aspects that emerged.

### Knowledge dependencies

Knowledge dependencies describe how much knowledge of one part of the system is needed to modify another part. To estimate them, we generated co-change reports from Git history, using three time windows: last 5 years, last 10 years and full history. Frequent co-change does not prove a direct code dependency: two files may not import or use each other, but they can still be linked by the same maintenance reason if developers often need to understand both when making a change.

Starting from these reports, we grouped related pairs into functional domains, based on the feature, responsibility or integration point they seemed to share. This is related to the **Common Closure Principle**: classes that tend to change for the same reason should usually be grouped and managed together. Therefore, co-change is not automatically a problem: it may show good cohesion or a hidden dependency worth checking.

The main domains are:

1. **Swing map view domain**: `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and layout classes. It is the main graphical view and contains the strongest co-change pairs.
2. **Outline subsystem domain**: `ScrollableTreePanel`, `BreadcrumbPanel`, `BlockPanel`, `OutlinePane`, `MapAwareOutlinePane`, `OutlineController` and `OutlineViewport`. It shows the same map content as a tree.
3. **API and scripting domain**: `Node`, `NodeRO`, `MindMap`, `NodeProxy`, and `MapProxy`. This case crosses module boundaries between `freeplane_api` and `freeplane_plugin_script`.
4. **Text rendering plugins domain**: `FormulaTextTransformer`, `LatexRenderer`, `MarkdownRenderer` and `MTextController`. They are different plugins, but all work on special text inside nodes.

<p align="center">
  <img src="../../../deliverables/img/design/cochange_domain_evolution.png" alt="Co-change domain evolution graph" width="700"/>
</p>

<p align="center"><em>Figure 1: Co-change domain evolution</em></p>

### Code dependencies

Code dependencies are visible in the source code, for example through class usage, object creation, interfaces and package structure. We use them to check the domains identified through co-change.

#### 1. Swing map view domain

The code confirms that the Swing map view domain is not only a historical relation. `MapView`, `NodeView` and `MainView` form the main visual structure of the map: `MapView` manages the overall graphical view, `NodeView` represents a single node linked to its `NodeModel`, and `MainView` shows the visible content of the node.

<p align="center">
  <img src="../../../deliverables/img/design/SwingMapView.png" alt="Swing map view" width="700"/>
</p>

<p align="center"><em>Figure 1: Swing map view.</em></p>

This explains why these classes often changed together. Changes in selection, folding or style can affect more than one level of the visual structure. The dependency is strong, but mostly justified, because these classes share the same responsibility: showing and updating the visual map. This also fits the Common Closure Principle, because the main classes are in the same package area, `org.freeplane.view.swing.map`.

However, the map view also needs information from styles, filters, text, links, icons, UI listeners and the map model. This creates high fan-out, meaning many outgoing links to other packages. It is understandable, because a visual node contains many elements, but it also increases cognitive load: modifying this area requires understanding several connected classes and subsystems.

The code also shows one useful choice: `NodeViewFactory`. When `MapView` displays nodes, the program must create visual objects such as `NodeView`, `MainView` and other components. This is a construction dependency: the issue is not only using an object, but also where it is created. Freeplane concentrates this creation logic in `NodeViewFactory`.

<p align="center">
  <img src="../../../deliverables/puml/swing_map_view_dependencies.svg" alt="Swing map view dependencies" width="700"/>
</p>

<p align="center"><em>Figure 2: Swing map view dependencies.</em></p>

#### 2. Outline subsystem domain

We then analysed another visualisation domain: the outline subsystem. While the Swing map view shows the mind map graphically, the outline shows the same nodes in a more linear tree structure.

<p align="center">
  <img src="../../../deliverables/img/design/outlineView.png" alt="Outline view" width="700"/>
</p>

<p align="center"><em>Figure 3: Outline view.</em></p>

Starting from the co-change report, the main class to check was `ScrollableTreePanel`, because many outline pairs were centred around it. The code confirms this role: it manages the tree-like list shown in the outline, including visible nodes, selection, navigation and scrolling.

`OutlinePane` builds the outline area by creating `BreadcrumbPanel`, `ScrollableTreePanel`, `OutlineController`, the toolbar and the menu. Other classes manage smaller parts of the same view: `BlockPanel` shows visible node groups and sends actions back to `ScrollableTreePanel`, `BreadcrumbPanel` shows the current path, and `OutlineViewport` helps with scrolling.

This also fits the Common Closure Principle: the classes that often changed together are grouped in the same package, `org.freeplane.view.swing.map.outline`, and work on the same feature. Therefore, the co-change mainly indicates internal cohesion.

The most interesting point is `MapAwareOutlinePane`. The co-change reports mainly showed internal relations in the outline domain; no direct pair with the Swing map view domain was very evident. However, the code shows that the outline is also connected to the main map view through `MapAwareOutlinePane`. This dependency is expected, because the outline shows the same map and must stay aligned with `MapView`, `NodeView`, `NodeModel` and map/node listeners. Still, it increases cognitive load, because modifying the outline also requires understanding its interaction with the main map view.

<p align="center">
  <img src="../../../deliverables/img/design/outline_dependencies.png" alt="Outline subsystem dependencies" width="700"/>
</p>

<p align="center"><em>Figure 4: Outline subsystem dependencies.</em></p>

#### 3. API and scripting domain

The API and scripting domain is different from the UI domains because it connects different parts of Freeplane: the public API, the scripting plugin and the internal model.


Scripts automate actions on mind maps. To support them, Freeplane exposes a public API: `NodeRO` gives read-only access to a node, `Node` adds modification operations, and `MindMap` represents the map available to scripts.

The co-change relation suggested that the public API and the scripting plugin evolve together. The code confirms this relation, but in a controlled way: scripts do not access the internal model directly, but pass through proxy classes. `NodeProxy` exposes the node API while internally working with `NodeModel`; similarly, `MapProxy` exposes `MindMap` while working with `MapModel`.

Therefore, this is not just internal cohesion. It is a real dependency between scripting and the Freeplane core, but the proxy layer keeps it organised. The design is good because the API remains a stable access layer. However, the proxies are still delicate: they protect the internal model, but they must know both the public API and the internal model.

<p align="center">
  <img src="../../../deliverables/img/design/api_scripting_dependencies.png" alt="API and scripting dependencies" width="700"/>
</p>

<p align="center"><em>Figure 5: API and scripting dependencies.</em></p>

#### 4. Text rendering plugins domain

This smaller case shows a different kind of dependency. `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer` belong to three different plugins: formulas, LaTeX and Markdown.

In the co-change reports, these classes often changed together. However, in the code they do not import or use each other, so this is not direct coupling between plugins.

The reason for their connection is that they all handle special text inside nodes. When Freeplane displays or edits a node, its content may require a specific transformation before being shown. These transformations pass through the same content-transformer mechanism used by `MTextController`.

Therefore, the co-change is confirmed as a shared maintenance concern, not as a direct code dependency. The design is mostly good: the plugins remain separated, but changes in the central text mechanism can still affect more than one plugin.

<p align="center">
  <img src="../../../deliverables/img/design/text_rendering_dependencies.png" alt="Text rendering plugins dependencies" width="700"/>
</p>

<p align="center"><em>Figure 6: Text rendering plugins dependencies.</em></p>

### Final observations

Overall, co-change is not always bad design. In the Swing map view and outline domains, knowledge dependencies mostly match code dependencies inside cohesive UI subsystems. In the API and scripting domain, co-change crosses module boundaries, but the dependency is controlled through proxies. In the text rendering plugins domain, co-change does not reveal direct coupling, but a shared maintenance concern. Therefore, Freeplane is generally modular, but some central areas, especially the visual map and the proxy layer, require more knowledge and careful maintenance.