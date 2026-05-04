# System Overview Report – Freeplane

## System Purpose

Freeplane is an open-source desktop application used to create and manage mind maps. Its main purpose is to help users organize information visually, making ideas, tasks, concepts, and relationships easier to understand and manage.

The system can be used in different contexts, such as studying, brainstorming, taking notes, organizing personal activities, managing knowledge, and planning projects. Freeplane was publicly launched in July 2009 as a fork of FreeMind and evolved from a mind map viewer into a more complete working tool. Today, it includes advanced features such as LaTeX and Markdown support, integration with AI tools, and the Code Explorer.

We selected Freeplane because it is a real-world open-source project with a large codebase, a long development history, several contributors, and an internal organization based on multiple modules and plugins. For this reason, it represents a good case study for analyzing both design choices and the overall architecture of the system.

## Main Stakeholders

**End users:**  
End users create, edit, and manage mind maps for personal, academic, or professional purposes. Two main groups can be identified:
- Basic users mainly use Freeplane for visual organization, note-taking, studying, brainstorming, or planning daily activities.
- Advanced users, generally more familiar with technical features, use more powerful functionalities such as formatting, formulas, scripting, add-ons, export options, and customization mechanisms.

**Plugin, script, and add-on developers:**  
These stakeholders extend the system by developing plugins, scripts, or add-ons. Freeplane explicitly supports extensibility: plugin development follows specific conventions, plugin modules are included in the Gradle configuration, and individual plugins can declare their own dependencies and OSGi imports. This makes extensibility an important part of the system structure.

**Core maintainers and contributors:**  
Core maintainers are responsible for evolving the system, reviewing contributions, fixing bugs, and preserving the quality and stability of the project. External contributors can also support the project by reporting bugs, proposing improvements, improving documentation, translating content, or contributing code.

## System Description

### General functioning and data management

Freeplane is a cross-platform desktop application mainly implemented in Java. It provides a graphical user interface based on Java Swing and uses OSGi to organize the system into modular parts. It runs on different operating systems, as long as a current version of Java is available. It can be installed normally, but it can also be run from removable storage, which increases its portability.

The application allows users to build hierarchical mind maps composed of interconnected nodes. Through the user interface, users can structure ideas, format nodes, add links and images, manage attributes, use formulas, and organize information in a flexible way, all within a unified interface that hides the underlying complexity of the system.

Mind maps are stored as `.mm` files, which are XML-based files. As a result, Freeplane does not require a traditional database layer for its main data model, because map content is saved directly in structured files.

### Internal organization and extensibility

From a general point of view, Freeplane can be described as a single desktop application with an internal modular organization. The system has a main core, responsible for the essential functionalities, while more specific, advanced, or graphical features are added through plugins. These plugins are not independent external resources, but components intended by the project structure: they are generally written in Java and interact with the application through defined extension points.

The repository reflects this organization: besides the main modules, it contains several plugin subprojects, for example for scripting, formulas, LaTeX, Markdown, SVG, OpenMaps, AI, code exploration, syntax support, and bug reporting. The official plugin development documentation also shows that new plugins follow the `freeplane_plugin_*` naming convention, must be included in `settings.gradle`, and can declare their own dependencies and OSGi imports. This aspect will also be useful in the following analyses, because it helps observe how the system separates the core from extensible functionalities.

Freeplane also provides scripting support for advanced customization and automation. This allows users to extend the behavior of the application without directly modifying the core code. The documentation refers to scripting with Groovy and JavaScript, while also mentioning support for other scripting languages in specific versions. This mechanism is useful for advanced users and add-on developers, because it allows them to automate operations and adapt the system to specific needs.

The application interacts directly with the operating system for file management, rendering, access to local resources, and export operations. It supports exporting maps to several formats, such as PDF, images, XML, XHTML/HTML, and office-related formats. These features show that Freeplane is not only a simple editor, but a complete desktop tool for creating, extending, and sharing structured information.

## Basic Code Statistics

The following statistics provide a general overview of the selected repository snapshot used for the analysis.

**Repository branch/snapshot:** `1.13.x`  
**Number of files:** 3260  
**Lines of Code (LOC):** 384077  
**Number of Gradle subprojects/modules:** 17  
**Number of directories:** ~2300, including source, test, plugin, resource, build, and auxiliary folders  
**Main language:** Java  
**Other relevant languages/technologies:** XSLT, Groovy, Shell, HTML, XML, JSON, YAML, and build/configuration files  
**Number of developers/contributors:** 275 contributors in the GitHub repository  

![Code Analysis](../../images/code-analysis.png)

## Summary

Freeplane is a mature open-source desktop application with a large Java codebase and an internal modular organization. Its Java/Swing core, OSGi-based structure, plugins, scripting support, `.mm` file format, and export features make it a suitable system for studying dependencies, extensibility mechanisms, recurring design solutions, and architectural characteristics.