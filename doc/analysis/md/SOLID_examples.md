# Analisi SOLID su `org.freeplane.features.map`

Focus principale: package `org.freeplane.features.map` (con riferimenti puntuali a sottopackage strettamente collegati: `mindmapmode`, `filemode`, `clipboard`).

## S — Single Responsibility Principle (SRP)

### Esempi di compliance (2)

1. `org.freeplane.features.map.MapReader` e `org.freeplane.features.map.MapWriter` separano responsabilita di lettura/parsing e scrittura/serializzazione.
2. `org.freeplane.features.map.INodeChangeListener` ha responsabilita singola: notificare `nodeChanged`.

### Esempi di violazione (2)

1. `org.freeplane.features.map.MapController`: aggrega troppe responsabilita (setup IO, registrazione azioni, navigation/selection, folding, orchestrazione eventi/listener).
2. `org.freeplane.features.map.mindmapmode.MMapController`: include CRUD nodi, UI editing, loading mappe, restore, clipboard, folding persistence.

#### Snippet che certificano la violazione

```java
public MapController(ModeController modeController) {
    ...
    mapWriter = new MapWriter(this);
    ...
    mapReader = new MapReader(readManager);
    ...
    createActions(modeController);
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/MapController.java`

```java
private void createActions(ModeController modeController) {
    modeController.addAction(new NewMapViewAction());
    modeController.addAction(new NewSiblingAction());
    modeController.addAction(new NewPreviousSiblingAction());
    modeController.addAction(new NewChildAction());
    ...
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/mindmapmode/MMapController.java`

---

## O — Open/Closed Principle (OCP)

### Esempi di compliance (2)

1. `org.freeplane.features.map.filemode.FMapController` estende `MapController` e personalizza comportamento via override (`fireFoldingChanged`) senza modificare la base.
2. Le interfacce listener (`IMapChangeListener`, `IMapLifeCycleListener`) consentono estensioni comportamentali tramite nuove implementazioni.

### Esempi di violazione (2)

1. `org.freeplane.features.map.NodeLevelConditionController`: per nuovi tipi di condizione bisogna modificare catene di `if`.
2. `org.freeplane.features.map.mindmapmode.MMapController#createActions`: nuove azioni richiedono modifica diretta del metodo.

#### Snippet che certificano la violazione

```java
protected ASelectableCondition createASelectableCondition(...) {
    if (simpleCondition.objectEquals(ConditionFactory.FILTER_IS_EQUAL_TO)) {
        return new NodeLevelCompareCondition(...);
    }
    ...
    if (simpleCondition.objectEquals(NodeLevelConditionController.FILTER_LEAF))
        return new LeafCondition();
    return null;
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/NodeLevelConditionController.java`

```java
private void createActions(ModeController modeController) {
    modeController.addAction(new NewMapViewAction());
    modeController.addAction(new NewSiblingAction());
    ...
    modeController.addAction(new OpenSelectionAsNewViewRootAction());
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/mindmapmode/MMapController.java`

---

## L — Liskov Substitution Principle (LSP)

### Esempi di compliance (2)

1. `org.freeplane.features.map.filemode.FMapModel` e sostituibile come `MapModel` mantenendo il contratto base.
2. `org.freeplane.features.map.filemode.FMapController` e sostituibile come `MapController` nelle operazioni comuni.

### Esempi di violazione (2)

1. `org.freeplane.features.map.clipboard.SingleCopySource extends NodeModel` ma numerosi metodi ereditati lanciano `RuntimeException("method not supported")`.
2. `org.freeplane.features.map.MapController#getMap(URL)` esiste nel base type ma lancia `"Method not implemented"`.

#### Snippet che certificano la violazione

```java
class SingleCopySource extends NodeModel {
    private static final String METHOD_NOT_SUPPORTED = "method not supported";
```

```java
@Override
public void acceptViewVisitor(INodeViewVisitor visitor) {
   throw new RuntimeException(METHOD_NOT_SUPPORTED);
}

@Override
public IExtension putExtension(IExtension extension) {
   throw new RuntimeException(METHOD_NOT_SUPPORTED);
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/clipboard/SingleCopySource.java`

```java
public MapModel getMap(URL url) {
    throw new RuntimeException("Method not implemented");
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/MapController.java`

---

## I — Interface Segregation Principle (ISP)

### Esempi di compliance (2)

1. `org.freeplane.features.map.INodeChangeListener` e minimale (solo `nodeChanged`).
2. `org.freeplane.features.map.IMapSelectionListener` e snella (solo before/after map change, con default methods).

### Esempi di violazione (2)

1. `org.freeplane.features.map.IMapSelection` e molto ampia: selezione, navigazione, scrolling, filtri, visibilita/folding.
2. `SingleCopySource` che disabilita molti metodi ereditati e un segnale pratico che il contratto astratto e troppo largo per alcuni use case.

#### Snippet che certificano la violazione

```java
public interface IMapSelection {
    public void moveNodeTo(final NodeModel node, NodePosition position);
    public void slowlyMoveNodeTo(final NodeModel node, NodePosition position);
    public NodeModel getSelected();
```

```java
public void scrollNodeToVisible(NodeModel node);
...
Filter getFilter();
void setFilter(Filter filter);
...
public boolean isFolded(NodeModel node);
public boolean isVisible(NodeModel node);
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/IMapSelection.java`

---

## D — Dependency Inversion Principle (DIP)

### Esempi di compliance (2)

1. `org.freeplane.features.map.MapModel` dipende da astrazione `INodeDuplicator` (costruttore e `duplicate`).
2. `org.freeplane.features.map.MapController` usa astrazioni listener (`IMapChangeListener`, `INodeChangeListener`, `IMapLifeCycleListener`) invece di concrete class specifiche.

### Esempi di violazione (2)

1. Uso esteso di singleton globali concreti (`Controller.getCurrentController()`, `ResourceController.getResourceController()`) in controller ad alto livello.
2. `MapWriter` costruisce direttamente dipendenze concrete (`TreeXmlWriter`, `LinkBuilder`, `NodeWriter`) invece di riceverle via inversione.

#### Snippet che certificano la violazione

```java
private boolean shouldAutoscroll(String propertyName) {
    ResourceController resourceController = ResourceController.getResourceController();
    final boolean shouldAutoscroll = resourceController.getBooleanProperty(propertyName)
        && !(MouseEventActor.INSTANCE.isActive()
            && resourceController.getBooleanProperty("autoscroll_disabled_for_mouse_interaction"));
    return shouldAutoscroll;
}
```

```java
Filter filter = Controller.getCurrentController().getSelection().getFilter();
toggleFolded(node, filter);
```

Path: `freeplane/src/main/java/org/freeplane/features/map/MapController.java`

```java
LinkBuilder currentLinkBuilder = new LinkBuilder(
    mapController.getModeController().getExtension(LinkController.class));
currentNodeWriter = new NodeWriter(mapController, currentLinkBuilder, nodeTag, writeChildren, copiedNodeSet);
```

```java
TreeXmlWriter createTreeWriter(final Writer writer) {
    return new TreeXmlWriter(writeManager, writer,
        ResourceController.getResourceController().getBooleanProperty("useAsciiCharset"));
}
```

Path: `freeplane/src/main/java/org/freeplane/features/map/MapWriter.java`

---

## Nota metodologica

- Le "violazioni" sono valutate in ottica design/SOLID e non implicano necessariamente bug funzionali.
- In un codebase legacy e ricco di estensioni come Freeplane, possono rappresentare trade-off storici/architetturali.
