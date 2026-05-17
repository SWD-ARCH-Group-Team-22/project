# Journal
## Author: Luca Robustelli

### 18/04/2026
**In-depth analysis of the Launcher module in `freeplane_framework`**
*   Started a detailed study of the `Launcher.java` class located in the repository: `../freeplane/freeplane_framework/`.
*   Identified the implementation of the **Singleton Pattern** using `AtomicBoolean` for thread-safe state management. This mechanism prevents catastrophic crashes caused by double-starting the OSGi framework (Knopflerfish).
*   Analyzed the advantages of using `compareAndSet(false, true)` over traditional `synchronized` blocks to ensure lock-free performance and zero contention during the initialization phase.

### 19/04/2026
**Creational Patterns: Builder and Factory**
*   Examined the **Builder Pattern** (Fluent Interface) implementation within the `Launcher` class.
    *   Methods like `disableSecurityManager()` and `userDirectory(File)` return `this`, allowing for readable and flexible configuration chaining.
    *   This approach avoids "Constructor Telescoping," making the setup of approximately 15 different configuration aspects manageable.
*   Analyzed the **Factory Pattern** through static methods `create()` and `createForInstallation(File)`.
    *   These methods centralize the logic for deducing the installation directory, whether the application is running standalone or embedded.

### 20/04/2026
**Structural Patterns: Facade and Adapter**
*   Mapped the **Facade Pattern** roles. The `Launcher` acts as a simplified interface to the highly complex OSGi subsystem (bundles, services, and classloader isolation).
    *   Clients can use `launchWithUI(args)` without needing to understand the underlying Knopflerfish `Main` class or `BundleContext` logic.
*   Studied the **Adapter Pattern** used for the `SecurityManager`.
    *   Implemented via an anonymous class to adapt the `checkConnect` behavior, specifically handling cases where the `pContext` might be null to prevent `NullPointerExceptions`.

### 21/04/2026 - 22/04/2026
**Behavioral Patterns: Template Method and Strategy**
*   Identified the **Template Method Pattern** in `launchWithoutUICheck(String[] args)`.
    *   This method defines a rigid execution skeleton: `setDefines()` -> `setSecurityManager()` -> `setArgProperties()` -> `startFramework()`.
    *   This ensures the critical startup sequence is always respected, preventing initialization bugs.
*   Analyzed the implicit **Strategy Pattern** for different execution modes.
    *   The framework offers two distinct strategies: `launchHeadless()` for server-side map processing and `launchWithUI()` for full desktop interaction.
*   Completed the technical documentation of the module, highlighting how these patterns interact to provide a robust plugin framework.

### 28/04/2026 - 30/04/2026
**Shifting Focus: Investigating the Core Domain**
*   Moved away from the framework launcher to analyze the core business logic in the `freeplane` main module.
*   Started scanning packages using grep and IDE search tools to locate recognizable pattern names (`*Strategy`, `*Builder`, `*Proxy`) and core architectural components.
*   Goal set: Find and document 4 major GoF patterns with significant impact on the application's runtime.

### 04/05/2026 - 06/05/2026
**Finding the Strategy Pattern in Filtering**
*   Explored the `org.freeplane.features.filter` package and discovered `StringMatchingStrategy.java`.
*   Analyzed how Freeplane handles searching nodes (Exact match, Regex, Levenshtein distance). 
*   Documented how the Strategy pattern prevents massive `switch/if-else` blocks inside the `FilterController`, isolating matching algorithms.

### 07/05/2026 - 09/05/2026
**Deep Dive: The Composite Pattern and the Mind Map Tree**
*   Started analyzing `NodeModel.java` in `org.freeplane.features.map`. Since mind maps are trees, a Composite pattern was highly expected.
*   Realized Freeplane uses a collapsed, simplified version of the Composite: there is no abstract `Component` interface splitting into `Leaf` and `Branch`. 
*   Investigated *why*: treating every node as a potential branch (with an empty child list for leaves) heavily optimizes performance, avoiding constant re-instantiations when users add/remove child nodes dynamically.

### 11/05/2026 - 13/05/2026
**The Scripting API and the Proxy Pattern**
*   Shifted to the `freeplane_plugin_script` module to see how external Groovy scripts interact with the map.
*   Discovered `NodeProxy.java`. This was a perfect example of a Protection/Simplification Proxy.
*   Analyzed the routing: scripts talk to `NodeProxy`, which forwards safe, controller-mediated calls (e.g., via `MTextController`) to the real `NodeModel`, guaranteeing that Undo/Redo mechanisms and UI refresh events are triggered properly.

### 14/05/2026 - 15/05/2026
**Dependency Tracking and the Builder Pattern**
*   While looking at script executions, I investigated how Freeplane knows *when* to recalculate formulas. 
*   Found `DependenciesBuilder.java`. Traced its usage in `DependencyLookupProxy`.
*   Documented the execution flow: as the script engine parses a formula, it incrementally calls `addAttribute()` on the builder. Only at the end, it calls `build()` to freeze the state into an immutable `Dependencies` object. A great example of preventing telescoping constructors while building state dynamically.

### 16/05/2026 - 17/05/2026 (Today)
**Drafting Diagrams and Finalizing the Report**
*   Compiled all the findings for the 4 selected patterns (Composite, Proxy, Builder, Strategy).
*   Created PlantUML class diagrams to map the relationships between classes (`NodeModel`, `NodeProxy`, `DependenciesBuilder`, etc.).
*   Also sketched PlantUML diagrams of *alternative architectures* (like Telescoping Constructors or Enums/Switch statements) to highlight the specific architectural problems these GoF patterns solved.
*   Finalized the `design_pattern_analysis.md` report, integrating practical contextual examples of how these patterns operate during standard user interactions.
