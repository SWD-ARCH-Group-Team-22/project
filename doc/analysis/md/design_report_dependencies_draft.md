### Knowledge dependencies from co-change analysis

To complement the static analysis of code dependencies, we also analysed the knowledge dependencies of Freeplane using its Git history.

In this context, a knowledge dependency is not necessarily a dependency that can be seen directly in the source code. Instead, it is inferred from files that frequently changed together in the same commits. The idea is that, if two files are often modified together, developers probably need to understand both of them when they work on certain maintenance or evolution tasks.

For this analysis, we considered three different co-change reports:

- full repository history;
- last 10 years;
- last 5 years.

This distinction was useful because each report gives a slightly different perspective. The last-5-years report is the closest to the current evolution of the project, while the last-10-years report helps check whether the same dependencies are stable over a longer period. The full-history report gives a broader view, but it must be interpreted more carefully, because it also includes older project structures and file paths that are no longer fully representative of the current system.

The analysis was not based only on the highest-ranked pairs taken individually. Instead, we grouped the most frequent co-change pairs into functional clusters, in order to understand which parts of the system tend to evolve together.

The strongest and most stable cluster is related to the Swing map view. Classes such as `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout-related classes appear repeatedly in all three reports. In particular, the pair `MapView`–`NodeView` is the strongest one across the analysed time windows. This suggests that the visual representation of maps and nodes is one of the central areas of Freeplane and often requires coordinated changes.

A second relevant cluster is the outline subsystem, with classes such as `ScrollableTreePanel`, `BreadcrumbPanel`, `OutlinePane`, `MapAwareOutlinePane` and `OutlineController`. This cluster is very strong in the recent reports, but its values remain almost unchanged when moving from the last-5-years report to the last-10-years and full-history reports. For this reason, it seems to represent an important recent area of co-change, rather than a dependency that has grown continuously across the whole history of the project.

Another interesting result is the relation between the API and the scripting plugin. Classes such as `Node`, `NodeRO` and `NodeProxy` appear together in the co-change reports, even if they belong to different modules. This is one of the most useful cases for the design analysis, because it suggests a cross-module knowledge dependency: when the public node API changes, the scripting layer that exposes nodes to scripts may also need to be updated.

The reports also show co-change among text rendering plugins, especially around classes such as `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer`. Although these classes belong to separate plugins, they seem to evolve together because they address similar concerns related to rendering or transforming node text.

### Knowledge dependencies from co-change analysis

We analysed knowledge dependencies in Freeplane by looking at the Git history and, in particular, at the co-change reports generated from it.

Here, a knowledge dependency does not necessarily mean that two classes are directly connected in the source code. It means that two files often changed together in the same commits. The idea is that, when this happens many times, developers probably need to understand both files when they work on certain changes.

For this analysis, we considered three different time windows:

- the full repository history;
- the last 10 years;
- the last 5 years.

This choice helped us separate different types of information. The last-5-years report is closer to the current evolution of the project. The last-10-years report helps us understand whether the same relations are stable over a longer period. The full-history report gives a broader view, but it must be read more carefully, because it also includes older project structures and file paths that are not fully representative of the current system.

We did not use the reports only as rankings of file pairs. Instead, we grouped the most frequent co-change pairs into functional clusters, so that we could understand which parts of the system tend to evolve together.

The strongest and most stable cluster is the Swing map view. Classes such as `MapView`, `NodeView`, `MainView`, `NodeViewFactory` and the layout-related classes appear repeatedly in all three reports. In particular, the pair `MapView`–`NodeView` is the strongest one across the analysed time windows. This suggests that the visual representation of maps and nodes is one of the central areas of Freeplane and often requires coordinated changes.

A second relevant cluster is the outline subsystem, with classes such as `ScrollableTreePanel`, `BreadcrumbPanel`, `OutlinePane`, `MapAwareOutlinePane` and `OutlineController`. This cluster is very strong in the recent reports, but its values remain almost unchanged when moving from the last-5-years report to the last-10-years and full-history reports. For this reason, it seems to represent an important recent area of co-change, rather than a dependency that has grown continuously across the whole history of the project.

Another important result is the relation between the API and the scripting plugin. Classes such as `Node`, `NodeRO` and `NodeProxy` appear together in the co-change reports, even if they belong to different modules. This is one of the most useful cases for the design analysis, because it suggests a cross-module knowledge dependency: when the public node API changes, the scripting layer that exposes nodes to scripts may also need to be updated.

The reports also show co-change among text rendering plugins, especially around classes such as `FormulaTextTransformer`, `LatexRenderer` and `MarkdownRenderer`. Although these classes belong to separate plugins, they seem to evolve together because they deal with similar concerns related to rendering or transforming node text.

In conclusion, the co-change analysis points to four areas that should be checked in the code: the Swing map view, the outline subsystem, the API/scripting boundary and the text rendering plugins. These clusters will be compared with the static code dependencies, to understand whether Freeplane’s historical evolution is consistent with its current modular structure.