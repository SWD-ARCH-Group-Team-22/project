### Knowledge dependencies from co-change analysis

As a first step of the dependency analysis, we focused on the knowledge dependencies of Freeplane. Since the project is large, we did not start directly from the source code. Instead, we used the Git history to understand which parts of the system usually changed together.

We generated co-change reports from the commit history. These reports show which pairs of files were modified in the same commits, and how many times this happened. This does not automatically prove that there is a direct code dependency. However, it tells us something useful about maintenance work: if two files often change together, then a change in one file probably requires developers to check or understand the other one too.

This is connected to what we discussed in class about software complexity. Dependencies are not always wrong, but they become dangerous when they increase cognitive load, because developers need to know too many parts of the system, or when they cause change amplification, because a small change spreads to many files. In our case, the co-change analysis was used as a first map of the system and helped us choose the areas to inspect in the code.

The reports were generated for three time windows: the last 5 years, the last 10 years, and the full repository history. This helped us distinguish recent co-change from more stable relations. We read the full-history report more carefully, because it also includes older paths and older project structures.

Instead of reporting all the pairs one by one, we grouped them into functional areas. This follows the same reasoning behind the Common Closure Principle: if classes tend to change together, they may belong to the same responsibility or at least to the same maintenance concern. This does not mean that every co-change is a problem. Sometimes it simply shows good cohesion: files change together because they are part of the same feature; in other cases, especially when the files are in different modules, it may suggest a stronger hidden dependency.

The clearest cluster is the Swing map view. Classes such as `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout classes appear together in all three reports. This is not surprising: Freeplane is mainly a mind-mapping application, so the way maps and nodes are shown on screen is a central part of the system. Our first interpretation is that this is probably normal cohesion inside the main UI subsystem. Still, because this area is so central, the code analysis must check whether this cohesion remains local to the map view or whether it forces the map view to interact with many other parts of the application.

Another important cluster is the outline subsystem, with classes such as `ScrollableTreePanel`, `BreadcrumbPanel`, `OutlinePane`, `MapAwareOutlinePane` and `OutlineController`. The outline is another way of looking at the same map content, but in a more tree-like structure. For this reason, it may need to stay aligned with the main map view: if selection, scrolling or node positioning changes in the map, the outline may also need updates.

The most interesting case is the relation between the public API and the scripting plugin. The repository has a separate `freeplane_api` module and a separate `freeplane_plugin_script` module, but classes such as `Node`, `NodeRO` and `NodeProxy` still appear together in the co-change reports. In simple terms, scripts need a way to access Freeplane concepts such as nodes and maps. If the public node API changes, the proxy used by scripts may also need to change. This could be a good and controlled dependency if the scripting plugin uses only public interfaces. It would be more problematic if it also depended on internal implementation details.

Finally, the text rendering plugins show another useful case. `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer` belong to different plugin areas, but they all deal with the same general concern: transforming or rendering text inside nodes. Their co-change may therefore mean that, when Freeplane changes how node text is handled, more than one text-related plugin has to be updated.

This first analysis does not prove design problems by itself. It gives us a set of meaningful areas to inspect next in the code dependencies analysis.

### Code dependencies in the Swing map view

The code inspection confirms that the Swing map view cluster is not only a historical relation. `MapView`, `NodeView` and `MainView` form the main visual structure of the map: `MapView` manages the overall graphical view, `NodeView` represents a single node linked to its `NodeModel`, and `MainView` shows the visible content of the node.

This explains why these classes often changed together in the co-change reports. A change in how nodes are displayed, selected, folded, styled or updated can affect more than one level of the visual structure. For this reason, the dependency seems mostly justified: it is strong, but linked to the same responsibility, namely showing and updating the visual map. This is consistent with the Common Closure Principle, because classes that change for the same reason are kept in the same subsystem.

At the same time, to display nodes correctly, the map view needs information from many other parts of the system, such as styles, filters, text, links, icons, UI listeners and the map model. This creates high fan-out, meaning many outgoing links to other packages. This is understandable, because a visual node contains many different elements, but it also increases cognitive load: modifying this area requires understanding several connected classes and subsystems.

`NodeViewFactory` helps keep part of this complexity more controlled, because the creation of visual node components is concentrated there instead of being spread inside `MapView`.