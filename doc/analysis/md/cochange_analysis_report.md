# Co-change Analysis Notes

## Purpose

This file collects the first notes from the co-change analysis of Freeplane.

The goal is not to list every file pair found in the reports. The project is too large for that, and a long list would not be very useful. Instead, the idea is to use the co-change data as a first map of the system.

If two files are often modified in the same commits, this may mean that developers usually need to understand both of them when working on that part of the system. This is what we use as a sign of **knowledge dependency**.

A co-change does not automatically prove that there is a direct dependency in the code. For example, two files may change together even if one does not import the other. However, it is still useful because it shows where maintenance work tends to spread.

The next step will be to compare these results with the code structure: packages, modules, imports, interfaces, controllers and plugins.

---

## Method

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

## Main clusters found

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

## 1. Swing map view

The clearest cluster is the Swing map view.

The main classes are:

- `MapView`
- `NodeView`
- `MainView`
- `NodeViewFactory`
- `VerticalNodeViewLayoutStrategy`
- `NodeViewLayoutHelper`
- `RootMainView`
- `ForkMainView`
- `BubbleMainView`

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

## 2. Outline subsystem

Another clear cluster is the outline subsystem.

Main classes:

- `ScrollableTreePanel`
- `BreadcrumbPanel`
- `BlockPanel`
- `OutlinePane`
- `MapAwareOutlinePane`
- `OutlineController`
- `NavigationButtons`
- `NodePositioning`
- `OutlineViewport`

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

## 3. API and scripting

This is probably the most interesting cluster from a design point of view.

Main classes:

- `Node`
- `NodeRO`
- `NodeProxy`
- `Proxy`
- `MapProxy`
- `ControllerProxy`
- `MindMap`
- `HeadlessMapCreator`

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

## 4. Text rendering plugins

Another useful case is the group of text rendering plugins.

Main classes:

- `FormulaTextTransformer`
- `LatexRenderer`
- `MarkdownRenderer`
- `MTextController`

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

## 5. Other clusters

Some other clusters are useful, but probably secondary for the final report.

### Tag and icon management

Main classes:

- `TagCategories`
- `TagCategoryEditor`
- `TagEditor`
- `MIconController`

This looks like a cohesive feature area. Model/data classes, editors and controllers change together. This is probably expected: if the structure of tags changes, the editor and controller may need updates.

### Code Explorer plugin

Main classes:

- `CodeNode`
- `ClassNode`
- `PackageNode`
- `ProjectRootNode`
- `CodeMapController`

This is mostly internal to the Code Explorer plugin. It may be useful as an example of internal plugin cohesion, but it is less interesting than API/scripting because it does not clearly cross module boundaries.

### Map controllers and headless mode

Main classes:

- `IMapViewManager`
- `MapViewController`
- `HeadlessMapViewController`

This appears especially in the 10-year report. It may help us understand how Freeplane separates normal UI mode from headless behavior.

### Historical infrastructure

The full-history report also shows older clusters:

- mode controller factories;
- startup classes;
- `Controller`, `ViewController`, `MenuBuilder`;
- file management and import/export actions.

These are useful to understand the old evolution of the system. However, some paths belong to older project structures, so they should be used carefully when discussing the current design.

---
