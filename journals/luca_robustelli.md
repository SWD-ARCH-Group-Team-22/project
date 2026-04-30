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
