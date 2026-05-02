# System Overview Report – Freeplane

## System Purpose 
Freeplane is an open-source desktop application designed to support the creation and organization of ideas through mind maps. Its main purpose is to help users structure information visually, making it easier to understand relationships between concepts, plan activities, and manage knowledge. The system is flexible enough to be used in different contexts, such as studying, brainstorming, or project planning.

## Main Stakeholders:      
**End users:** They seperating in two groups first, users that create and manage mind maps for their daily tasks. Second, advenced users that using complex features such as scripting and plugins to customize the system and automate repetitive actions.    
**Plugin developers:** Contributing to the ecosystem by extending the functionality of the application.    
**Core maintainers of the project:** They are responsible for evolving the system, reviewing contributions, and ensuring its overall quality and stability.


## System Description

Freeplane is a cross-platform desktop application designed for creating and managing mind maps, allowing users to visually organize ideas and information in a structured way. It is implemented primarily in Java and provides a rich graphical interface built on top of the Swing toolkit, enabling users to construct hierarchical diagrams composed of interconnected nodes.

By offering an interactive and flexible editing environment, the system supports a wide range of use cases, from simple note-taking to complex knowledge management and project planning. Users can manipulate the structure of their maps, apply formatting, and enrich content with links, images, and metadata, all within a unified interface that abstracts the underlying complexity of the system.

From architectural perspective, Freeplane follows a modular monolithic architecture in which different concerns are separated into packages and components, while still being delivered as a single application. The core logic is implemented in Java, while additional functionality is supported through a combination of technologies including JavaScript, TypeScript, and scripting languages such as Groovy. The system stores mind maps using an XML-based `.mm` format, allowing structured data representation and eliminating the need for a database layer.

The application also incorporates a plugin system that enables dynamic extension of features without modifying the core codebase. Plugins are typically written in Java and interact with the application through well-defined extension points. In addition, a scripting engine allows advanced users to automate workflows and customize behavior, providing a high degree of flexibility. Supporting technologies such as JSON, YAML, and XML are used for configuration and data exchange, while auxiliary scripts in languages like Python or Shell are used for tooling and build processes.

Freeplane interacts directly with the operating system for file management, rendering, and resource access, and it supports exporting mind maps into formats such as PDF, HTML, and images. This combination of technologies allows the system to remain both portable and extensible, while maintaining performance and usability expected from a desktop application.

Overall, Freeplane combines a Java-based architecture with a diverse supporting technology stack, enabling both ease of use for end users and extensibility for developers.


## Basic Code Statics

**Number of files:** 3260   
**Line of Code (LOC):** 384077   
**Number of packages:** ~2300 (including both core and auxiliary components)   
**Number of Developers:** 275 contributers in GitHub repository

![Code Analysis](../../images/code-analysis.png)