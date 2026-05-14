# C4 Level 3 Component Diagram — Dependency Data

All dependencies verified against actual `import` statements in the source code.

---

## Components (inside the Core Engine container)

| Component | Package | Technology | Responsibility |
|---|---|---|---|
| **Controller** | `features.mode` | Java class (321 lines) | Global application hub. Mode selection, map lifecycle events, shutdown. Singleton via `getCurrentController()` |
| **ModeController** | `features.mode` | Java class (491 lines) | Mode orchestrator. Extension management, action management, tooltip rendering, UI lifecycle |
| **MapController** | `features.map` | Java class (~800 lines) | Map orchestration. Selection, navigation, folding, reader/writer coordination, event dispatching |
| **MapModel** | `features.map` | Java class | Domain entity. Represents the whole mind map (root node, node registry, file URL, state) |
| **NodeModel** | `features.map` | Java class | Domain entity. Represents a single node (parent/child, folding, text, icons, extensions) |
| **FilterController** | `features.filter` | Java class (1,179 lines) | Filter/search subsystem. Condition evaluation, toolbar, filter persistence |
| **MapReader / MapWriter** | `features.map` | Java classes | Persistence I/O. XML serialization/deserialization of `.mm` files |
| **Extension Framework** | `core.extension` | Java interfaces | `IExtension`, `ExtensionContainer` — enables the Extension Object Pattern |
| **MapView** | `view.swing.map` | Swing component | Renders the mind map visually. Handles painting, layout, zoom |
| **NodeView** | `view.swing.map` | Swing component | Renders individual nodes. Layout, edge painting, content display |

---

## Verified Dependencies (arrows in the diagram)

### Controller depends on:
- `ModeController` (holds a map of mode controllers)
- `MapModel` (via `getMap()`)
- `IMapViewManager` (interface — compliant)
- `ViewController` (concrete — violation)
- `ResourceController` (concrete singleton)
- `IMapLifeCycleListener` (implements it)

### ModeController depends on:
- `Controller` (holds a reference, calls `getController()`)
- `MapController` (holds a reference, calls `getMapController()`)
- `MapModel`, `NodeModel` (domain entities)
- `NodeStyleController`, `MapStyle`, `MapStyleModel` (style components)
- `Filter` (filter component)
- `ResourceController` (concrete singleton)
- `java.awt.Color`, `Component`, `Container`, `Font` (**Clean Architecture violation**)

### MapController depends on:
- `Controller`, `ModeController` (mode hub — via static singleton)
- `MapModel`, `NodeModel` (domain entities)
- `MapReader`, `MapWriter` (persistence)
- `FilterController`, `Filter`, `ConditionFactory` (filter subsystem)
- `IMapViewChangeListener`, `IMapViewManager` (UI interfaces — compliant)
- `NodeView` (concrete view class — **violation**)
- `MouseEventActor` (concrete view class — **violation**)
- `ResourceController` (concrete singleton)
- `ClipboardControllers` (clipboard)
- `UrlManager` (URL handling)

### MapModel depends on:
- `Controller`, `ModeController` (**Clean Architecture violation** — Entity depends on Adapter)
- `ExtensionContainer`, `IExtension` (extension framework)
- `IconRegistry`, `TagCategories` (icon subsystem)
- `Filter` (filter)
- NO `java.awt` imports ✅

### NodeModel depends on:
- `ExtensionContainer`, `IExtension` (extension framework)
- `Filter` (filter)
- `LayoutController` (layout)
- `INodeViewVisitor` (interface — compliant)
- `NamedIcon` (icon)
- NO `java.awt` imports ✅
- NO `Controller` dependency ✅

### FilterController depends on:
- `Controller` (16 singleton calls)
- `MapModel`, `NodeModel` (domain entities)
- `MapController.Direction` (map navigation)
- `IMapSelection`, `IMapViewChangeListener` (interfaces)
- `ViewController` (concrete — violation)
- `ConditionalStyleModel` (styles)
- `HighlightController`, `NodeHighlighter` (highlight subsystem)
- `java.awt.*` (40+ imports — **major violation**)
- `javax.swing.*` (17+ imports — **major violation**)

### MapView (View Layer) depends on:
- `Controller`, `ModeController` (mode hub)
- `MapController`, `MapModel`, `NodeModel` (features layer)
- `FilterController`, `Filter` (filter)
- `EdgeController`, `LinkController`, `NoteController` (feature controllers)
- `NodeStyleController`, `MapStyle`, `MapStyleModel` (styles)
- `TextController` (text)
- `IMapViewManager` (interface)
- `UrlManager` (URL handling)

---

## Key Dependency Patterns for the Diagram

### Clean boundaries (draw with green/normal arrows):
- `NodeModel` → `IExtension` (interface)
- `NodeModel` → `INodeViewVisitor` (interface)
- `MapController` → `IMapViewChangeListener` (interface)
- `MapController` → `IMapViewManager` (interface)
- `MapView` → `IMapChangeListener` (interface, observer pattern)

### Violated boundaries (draw with red/dashed arrows):
- `MapModel` → `Controller` (Entity depends on Adapter — **inward dependency broken**)
- `ModeController` → `java.awt.*` (Hub imports GUI classes)
- `FilterController` → `java.awt.*` / `javax.swing.*` (Business logic builds Swing UI)
- `MapController` → `NodeView` (Feature layer imports concrete View)
- All controllers → `Controller.getCurrentController()` (Global singleton, no DI)

---

## Suggested Diagram Layout

```
┌─────────────────── Core Engine Container ───────────────────┐
│                                                              │
│  ┌──────────────┐          ┌──────────────────┐             │
│  │  Controller   │◄────────│  ModeController   │             │
│  │  (mode hub)   │─────────►  (orchestrator)   │             │
│  └──────┬───────┘          └────────┬─────────┘             │
│         │                           │                        │
│         ▼                           ▼                        │
│  ┌──────────────┐          ┌──────────────────┐             │
│  │  MapModel     │          │  MapController    │             │
│  │  (entity)     │◄─────────  (map logic)      │             │
│  └──────┬───────┘          └────────┬─────────┘             │
│         │                           │                        │
│         ▼                           ▼                        │
│  ┌──────────────┐          ┌──────────────────┐             │
│  │  NodeModel    │          │  FilterController │             │
│  │  (entity)     │          │  (filter logic)   │             │
│  └──────────────┘          └──────────────────┘             │
│         │                           │                        │
│         ▼                           ▼                        │
│  ┌──────────────┐          ┌──────────────────┐             │
│  │  Extension    │          │  MapReader/Writer │             │
│  │  Framework    │          │  (persistence)    │             │
│  └──────────────┘          └──────────────────┘             │
│                                                              │
│  ┌──────────────────────────────────────────────┐           │
│  │  View Layer (MapView, NodeView) [Swing]      │           │
│  └──────────────────────────────────────────────┘           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

Red arrows (violations): MapModel→Controller, ModeController→java.awt, FilterController→javax.swing, MapController→NodeView
Green arrows (compliant): NodeModel→IExtension, MapController→IMapViewManager, MapView→IMapChangeListener
