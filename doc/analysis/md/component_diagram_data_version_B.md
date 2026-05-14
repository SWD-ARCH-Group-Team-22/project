# C4 Level 3 Component Diagram — Option B (Single Container)

**Modeling choice:** Freeplane is treated as a **single container** (one JVM process, one deployable unit). All internal modules — core internals AND plugins — are **components**.

All dependencies verified against actual `import` statements in the source code.

---

## Components (inside the single Freeplane Container)

### Core Internal Components

| Component | Package | Size | Responsibility |
|---|---|---|---|
| **Controller** | `features.mode` | 321 lines | Global application hub. Mode selection, map lifecycle, shutdown. Singleton via `getCurrentController()` |
| **ModeController** | `features.mode` | 491 lines | Mode orchestrator. Extension/action management, tooltip rendering, UI lifecycle |
| **MapController** | `features.map` | ~800 lines | Map orchestration. Selection, navigation, folding, event dispatching, reader/writer coordination |
| **MapModel** | `features.map` | — | Domain entity: the mind map (root node, node registry, file URL, state) |
| **NodeModel** | `features.map` | — | Domain entity: a single node (parent/child hierarchy, folding, text, icons, extensions) |
| **FilterController** | `features.filter` | 1,179 lines | Filter/search subsystem. Condition evaluation, toolbar, filter persistence |
| **MapReader / MapWriter** | `features.map` | ~200 each | Persistence I/O. XML serialization/deserialization of `.mm` files |
| **Extension Framework** | `core.extension` | — | `IExtension`, `ExtensionContainer` — enables the Extension Object Pattern |
| **View Layer** | `view.swing.map` | 207 classes | MapView + NodeView. Swing-based mind map rendering |

### Plugin Components

| Component | Module | Size | Responsibility | Depends on Core via |
|---|---|---|---|---|
| **Script Engine** | `freeplane_plugin_script` | 124 files | Groovy scripting, script management, API proxy implementation | `features.map`, `features.mode`, `features.text`, `features.filter`, `view.swing`, `core.ui` + **heavily uses `freeplane_api`** |
| **Formula Plugin** | `freeplane_plugin_formula` | 11 files | Evaluates formulas in node text | `features.map`, `features.text`, `features.mode` + **depends on Script Engine** |
| **AI Plugin** | `freeplane_plugin_ai` | 344 files | LLM integration, AI-assisted node manipulation | `features.map`, `features.mode`, `core.ui` (large, many core deps) |
| **Code Explorer** | `freeplane_plugin_codeexplorer` | 87 files | Code analysis mode, dependency graphs | `features.map`, `features.mode`, `view.swing` (registers new app mode) |
| **SVG Plugin** | `freeplane_plugin_svg` | 7 files | SVG rendering and PDF export | `features.map`, `features.export`, `features.mode`, `view.swing`, `core.awt` |
| **LaTeX Plugin** | `freeplane_plugin_latex` | 11 files | LaTeX rendering in nodes | `features.map`, `features.mode`, `view.swing` |
| **Markdown Plugin** | `freeplane_plugin_markdown` | 5 files | Markdown rendering | `features.map`, `features.mode` |
| **OpenMaps Plugin** | `freeplane_plugin_openmaps` | 12 files | OpenStreetMap visualization in nodes | `features.map`, `features.mode`, `view.swing` |
| **Bug Report Plugin** | `freeplane_plugin_bugreport` | 7 files | Error reporting | `features.mode`, `core.resources` |
| **JSyntaxPane Plugin** | `freeplane_plugin_jsyntaxpane` | 3 files | Syntax-highlighted text editing | `features.mode`, `core.ui` |

---

## Dependencies Between Components

### Core Internal Dependencies

*(Same as Option A — see component_diagram_data.md for full details)*

**Controller** → ModeController, MapModel, IMapViewManager, ViewController, ResourceController
**ModeController** → Controller, MapController, MapModel, NodeModel, Filter, java.awt.* (**violation**)
**MapController** → Controller, ModeController, MapModel, NodeModel, MapReader/Writer, FilterController, NodeView (**violation**)
**MapModel** → Controller, ModeController (**violation**: Entity → Adapter), ExtensionContainer
**NodeModel** → ExtensionContainer, Filter, INodeViewVisitor (clean)
**FilterController** → Controller (16×), MapModel, NodeModel, java.awt.* + javax.swing.* (**violation**)
**View Layer** → Controller, ModeController, MapController, MapModel, NodeModel, FilterController (many feature deps)

### Plugin → Core Dependencies

All plugins depend on the core. The dependency direction is strictly **plugin → core** (never core → plugin), enforced by the OSGi framework.

```
Script Engine ──→ features.map, features.mode, features.text, features.filter, view.swing, core.*
Formula        ──→ features.map, features.text, features.mode + Script Engine
AI Plugin      ──→ features.map, features.mode, core.ui
Code Explorer  ──→ features.map, features.mode, view.swing
SVG            ──→ features.map, features.export, features.mode, view.swing
LaTeX          ──→ features.map, features.mode, view.swing
Markdown       ──→ features.map, features.mode
OpenMaps       ──→ features.map, features.mode, view.swing
Bug Report     ──→ features.mode, core.resources
JSyntaxPane    ──→ features.mode, core.ui
```

### Plugin → Plugin Dependencies

Only ONE inter-plugin dependency exists:
- **Formula → Script Engine** (formulas are evaluated via Groovy)

All other plugins are fully independent of each other. ✅

---

## Key Observations for This Diagram

### What the diagram should show

```
┌──────────────────── Freeplane (Single Container / JVM) ────────────────────┐
│                                                                             │
│  ┌─── Core Engine ──────────────────────────────────────────────┐          │
│  │                                                               │          │
│  │  Controller ←──→ ModeController                               │          │
│  │      ↓                ↓                                       │          │
│  │  MapModel ←── MapController ──→ FilterController              │          │
│  │      ↓                ↓                                       │          │
│  │  NodeModel      MapReader/Writer                              │          │
│  │      ↓                                                        │          │
│  │  Extension Framework                                          │          │
│  │                                                               │          │
│  │  ┌─── View Layer (Swing) ──────────────────┐                 │          │
│  │  │  MapView, NodeView                       │                 │          │
│  │  └─────────────────────────────────────────┘                 │          │
│  └───────────────────────────────────────────────────────────────┘          │
│       ↑          ↑          ↑          ↑          ↑          ↑              │
│       │          │          │          │          │          │              │
│  ┌────┴──┐  ┌───┴───┐  ┌──┴──┐  ┌───┴──┐  ┌───┴──┐  ┌───┴────┐          │
│  │Script │  │Formula│  │ AI  │  │ SVG  │  │LaTeX │  │CodeExp │  ...      │
│  │Engine │←─│Plugin │  │     │  │      │  │      │  │        │          │
│  └───────┘  └───────┘  └─────┘  └──────┘  └──────┘  └────────┘          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Clean boundaries (solid arrows):
- All plugins → Core (one-way dependency, enforced by OSGi)
- NodeModel → IExtension, INodeViewVisitor (interfaces)
- MapController → IMapViewManager (interface)
- No core → plugin dependencies ✅
- Only 1 inter-plugin dependency (Formula → Script) ✅

### Violated boundaries (dashed/red arrows):
- MapModel → Controller (Entity → Adapter)
- ModeController → java.awt.* (Hub → GUI)
- FilterController → javax.swing.* (Logic builds UI)
- MapController → NodeView (Feature → concrete View)
- 454× Controller.getCurrentController() (global singleton everywhere)

---

## Comparison: Option A vs Option B

| Aspect | Option A (current) | Option B (this file) |
|---|---|---|
| Level 2 containers | Core, Persistence, Plugins, Scripting | **1 container:** "Freeplane Application" |
| Level 3 scope | Core Engine internals only | Core internals + 10 plugins |
| Diagram complexity | ~10 boxes | ~20 boxes |
| C4 correctness | Pragmatic (plugins treated as containers) | **Strict** (plugins are components within one deployable unit) |
| Shows plugin isolation | At Level 2 (separate containers) | At Level 3 (OSGi boundary within container) |
| Best for | Cleaner diagrams, easier to explain | Technically accurate, shows everything in one view |
v
