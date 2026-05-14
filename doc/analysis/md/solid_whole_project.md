# SOLID Systemic Analysis — Raw Data from Source Code Mining

Source: `freeplane-sourcecode/freeplane/src/main/java/org/freeplane/features/`

---

## Scope

- **Total Java files in `features` layer:** 849
- **Key packages analyzed:** `features.map`, `features.mode`, `features.filter`, `features.styles`

---

## DIP: Singleton Abuse — `Controller.getCurrentController()`

**454 occurrences** across the entire `features` layer.

This concrete global singleton is the primary way classes access application state. It is not injected — it is fetched statically, creating invisible coupling everywhere.

### Examples by package:
- `FilterController.java` alone: **16 calls**
- Used in static utility methods like `FilterController.getCurrentFilterController()` which itself calls `Controller.getCurrentController()`
- `MapController`, `ModeController`, and nearly every Controller-type class uses it

### Code pattern:
```java
// This pattern repeats 454 times across the features layer
Controller.getCurrentController().getSelection()
Controller.getCurrentController().getMapViewManager()
Controller.getCurrentModeController().getMapController()
ResourceController.getResourceController().getBooleanProperty(...)
```

---

## Clean Architecture: AWT/Swing Imports in Business Logic Layer

| Metric | Count | Percentage |
|---|---|---|
| Files importing `java.awt.*` | 440 | **52%** of 849 files |
| Files importing `javax.swing.*` | 265 | **31%** of 849 files |

This means over half the "business logic" layer directly depends on GUI framework classes. These should be in the outer View layer per Clean Architecture.

### `ModeController.java` — The Central Hub's AWT Dependencies

```java
import java.awt.Color;
import java.awt.Component;
import java.awt.Container;
import java.awt.Font;
```

`ModeController` is the central orchestrator that every mode (MindMap, File) extends. Its direct dependency on 4 AWT classes propagates to every subclass.

### `FilterController.java` — AWT/Swing in Business Logic

Lines 22–61 of `FilterController.java` contain **40 import lines** of `java.awt.*` and `javax.swing.*`:
```java
import java.awt.Color;
import java.awt.Component;
import java.awt.Cursor;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Graphics2D;
import java.awt.GridBagConstraints;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.AbstractButton;
import javax.swing.BorderFactory;
import javax.swing.ButtonModel;
import javax.swing.DefaultComboBoxModel;
import javax.swing.Icon;
import javax.swing.JComboBox;
import javax.swing.JComponent;
import javax.swing.JPanel;
import javax.swing.JSeparator;
import javax.swing.JToggleButton;
import javax.swing.JToolBar;
import javax.swing.JToolTip;
import javax.swing.SwingConstants;
// ... and more
```

A class named "FilterController" — which should handle filter logic — is building Swing toolbars, handling mouse events, and managing UI state.

---

## SRP: God Objects — Class Size Analysis

| Class | Lines | Package | Responsibilities |
|---|---|---|---|
| `FilterController.java` | **1,179** | `features.filter` | Filter logic, toolbar construction, XML persistence, UI state, action registration, event handling |
| `ModeController.java` | **491** | `features.mode` | Extension management, action management, tooltip rendering, undo coordination, UI lifecycle, node view lifecycle |
| `MapController.java` | ~800+ | `features.map` | IO setup, action registration, navigation, folding, selection, event orchestration, reader/writer coordination |
| `MMapController.java` | ~600+ | `features.map.mindmapmode` | CRUD, UI editing, clipboard, loading, restore, folding persistence |

For comparison, well-separated classes:
| Class | Lines | Role |
|---|---|---|
| `MapReader.java` | ~200 | XML parsing only |
| `MapWriter.java` | ~200 | XML serialization only |
| `INodeChangeListener.java` | ~10 | Single method interface |

---

## SRP: `ModeController` Responsibilities Breakdown

From reading the source (`ModeController.java`, 491 lines), it handles:

1. **Extension management:** `addExtension`, `getExtension`, `containsExtension`, `removeExtension`
2. **Extension copying (with undo):** `copyExtensions`, `undoableCopyExtensions`, `removeExtensions`, `undoableRemoveExtensions`, `resolveParentExtensions`
3. **Action management:** `addAction`, `removeAction`, `getAction` (with fallback to parent Controller)
4. **UI builder registration:** `addUiBuilder` (3 overloads)
5. **Node view lifecycle:** `addINodeViewLifeCycleListener`, `onViewCreated`, `onViewRemoved`
6. **Tooltip rendering:** `createToolTip` (builds HTML with CSS, queries styles, manages colors/fonts — 35 lines of HTML construction)
7. **Tooltip provider management:** `addToolTipProvider`
8. **Edit state management:** `canEdit`, `isEditingLocked`, `isBlocked`, `setBlocked`
9. **Menu updates:** `updateMenus`
10. **Mode lifecycle:** `startup`, `shutdown`, `setVisible`, `commit`, `rollback`

**At least 10 distinct responsibilities in one class.**

---

## DIP: `Controller.java` as Global State Hub

`Controller.java` (321 lines) uses a `ThreadLocal` + static field pattern:

```java
private static ThreadLocal<Controller> threadController = new ThreadLocal<Controller>();
private static Controller currentController = null;

public static Controller getCurrentController() {
    final Controller controller = threadController.get();
    return controller != null ? controller : currentController;
}
```

Every class that calls `Controller.getCurrentController()` creates an invisible dependency on this global state. There is no way to inject a test double.

---

## OCP Compliance Example: `features.filter.condition`

The `condition` subpackage uses a proper Strategy/Decorator pattern:

- `ICondition` — base interface
- `ASelectableCondition` — abstract base class
- `ConjunctConditions`, `DisjunctConditions` — composite conditions
- `DecoratedCondition`, `ConditionNotSatisfiedDecorator` — decorators
- `AllChildrenConditionDecorator`, `AnyDescendantConditionDecorator`, etc. — scope decorators

New condition types can be added by creating new classes implementing `ICondition` without modifying existing ones. **This is the strongest OCP compliance in the codebase.**

---

## LSP Violations

### `SingleCopySource extends NodeModel`
```java
class SingleCopySource extends NodeModel {
    private static final String METHOD_NOT_SUPPORTED = "method not supported";

    @Override
    public void acceptViewVisitor(INodeViewVisitor visitor) {
       throw new RuntimeException(METHOD_NOT_SUPPORTED);
    }

    @Override
    public IExtension putExtension(IExtension extension) {
       throw new RuntimeException(METHOD_NOT_SUPPORTED);
    }
}
```
Path: `features/map/clipboard/SingleCopySource.java`

### `MapController.getMap(URL)`
```java
public MapModel getMap(URL url) {
    throw new RuntimeException("Method not implemented");
}
```
Path: `features/map/MapController.java`

---

## ISP Violation: `IMapSelection`

```java
public interface IMapSelection {
    public void moveNodeTo(final NodeModel node, NodePosition position);
    public void slowlyMoveNodeTo(final NodeModel node, NodePosition position);
    public NodeModel getSelected();
    public void scrollNodeToVisible(NodeModel node);
    // ...
    Filter getFilter();
    void setFilter(Filter filter);
    // ...
    public boolean isFolded(NodeModel node);
    public boolean isVisible(NodeModel node);
}
```

Combines: selection, navigation, scrolling, filtering, folding visibility — **5 concerns in 1 interface.**

Path: `features/map/IMapSelection.java`

---

## Summary Table

| Principle | Systemic? | Key Evidence |
|---|---|---|
| **SRP** | ✅ Yes | God Objects repeat: `MapController`, `FilterController` (1,179 lines), `ModeController` (10+ responsibilities) |
| **OCP** | ⚠️ Mixed | Violations in `NodeLevelConditionController` if-chains and `createActions()`. Compliance in `filter.condition` Strategy pattern |
| **LSP** | ⚠️ Localized | `SingleCopySource` and `MapController.getMap(URL)` — limited to `features.map` |
| **ISP** | ⚠️ Localized | `IMapSelection` fat interface — limited to `features.map` |
| **DIP** | ✅ Yes | **454 singleton calls** across 849 files. **52% of files import `java.awt.*`**. Zero dependency injection |
