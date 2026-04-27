# Freeplane Plugins Architecture summary
## Introduction

This document aims at summarizing and clarifying key information about plugins. All information inside this summary has been
extracted and verified from one (or more) .txt file, whereas the single text files have been AI generated. They are based on the
mined commit history from the original Freeplane repository. However, some information in these documents can be imprecise or wrong. This document aims at pinpointing these faults and at offering a comprehensive and understandable overall presentation of the Architecture

## Freeplane Debug Helper
The Debug Helper plugin is an advanced tool for developers: it brings debugging features that help speeding up the overall developing time for delivering a new feature for a plugin.  
The debug helper basically introduces helper features for anyone who is in charge of developing a new feature. 
It introduces features such as direct import inside Java IDEs, or logging features to control length and detail for log messages. Moreover, it includes settings to disable mouse movement that can interfere with debugging features, strict authentication features (such as mouse movement tracking for debugging) and advanced UI features support (for better testing).  
### Communication
It depends on both the Freeplane API and the Freeplane core code. It has a direct dependency on the AI plugin as well. It has a direct connection on the Formula plugin as well, to load user-defined scripts and report bugs that come from there. 
It is basically just a bridge: it opens the all dependencies listed in the build-gradle (Core, Formula, AI) in a debug state to make it possible to attach an external debugger.

## Freeplane Bug Report
It is a diagnosing tool to provide developers with comprehensive information about bug and crashes that users may suffer from. It has a complex policy structure to ensure that all meaningful data is sent to the developers, provided that the user gives its approval

Since the beginning of the life-cycle of the Software, the ReportGenerator class was included. Its task is to send the report of the bug to the developers. It has included featurs to send reports even if there are not exceptions, but some strange behavior. It has strict control over Encryption and its violation automatically return an exception.
It supports privacy features: for instance, since 2022 reports do not include local paths from user's machine. However, an user can declare itself to be contacted by developers, and chains of reports can be created to provide maintainers with greater bug history. 
It reports Freeplane bugs only: bugs from user-written scripts are not considered. The bugreporter plugin is excluded and its exceptions do not trigger a new report (avoid infinite loops). Bugs are not signaled in headless mode; sending reports is a priviledged action.
### Communication
The bugreport plugin is connected to the core Freeplane code directly.

## Freeplane JSyntaxPane
It is in charge of creating highlightead and readable text in the Freeplane mind map interface. It implements readability and formatting settings depending on what the user is writing (comments, script code, LaTex formulas).
It was born basically as a fork of the pre-existing LaTex plugin, and initially it supported the JSyntaxPane library. In its early stages, it was a sort of evolution and maintenance of the library. In the 2020s, a new syntax library was adopted, and it required many fix actions. Nowadays, the SyntaxPane supports the dark theme and tags within mindmaps in Freeplane.  
It is crucial for productivity of all script editors in the Freeplane software. 
### Communication
Freeplane JSyntaxPane depends on the Freeplane Core only. However, many classes must be aware of its presence; these classes are:  
- formula
- markdown
- latex
- script

Its Activator file suggests that the plugin works as a bridge between the Freeplane core GUI package and the external library in charge of formatting the code to enhance readability.
## Freeplane Latex
This plugin implements the LaTex formatting engine. It makes it possible from people working in scientific fields to use the software to render their documentation.  
It is one of the main features of the software since its creation, and it was maintaned and evolved during time. Its first implementations were based on the HotEqn library, but from 2012 onwards, the JLaTeXMath Java libray was introduced. Nowadays, it supports advanced formatting features, as well as math fonts. It has always been embedded in the Freeplane mindmap visualizer.  
The plugin UX was evolved starting from its very beginning: if in 2009 it was just a plain editor, nowadays LaTex support has been extended to details, notes, as well as its nodes are automatically deleted if there is no text. Graphical support for MacOS themes and for dark visualization was introudced in 2021, as well as minor GUI fixes.  
Special features include:
- Global Macro within the map
- Support for Asiatic languages
- Unparsed LaTeX formatting
- Support for clones within the map

### Communication
This plugin depends on both the Freeplane Core Plugin and the JSyntaxPane one. 
It communicates with the Freeplane core to become aware of some information, such as if the software has some command-line enabled features that impacts the graphical render of text, and, more importantly, to handle the Controller to format latex text when inserted in the map.  
It is connected to `org.freeplane.features*`:
- `.features.mode.*`: to control the MindMapper mode and to render LaTex text
- `.features.text`: to access actual text and render it if required
- `.feature.format`: to register the LaTex formatting as an accepted Freeplane render setting

## Freeplane Markdown
If enabled, it allows users to write nodes in Markdown syntax, instead of raw text or html tags.  
 It has a rather young history, dating back to 2021.
It exploits the Java porting of the Javascript `marked` library, that has excellent rendering speed and efficience.
As the LaTeX module, it was enabled to be supported everywhere in Freeplane from January, 2021. It supports explicit tables from May 2021 onwards. 
It is fully supported by the core rendering engine, and its syntax is therefore clearly fisible within a mindmap in Freeplane. 
From 2025 onwards, the Markdown plugin offers PlantUML support embedded in Freeplane. As it was done for the LaTeX plugin, it was enabled to read commandline inputs and to support `input method events` from asiatic languages. 
### Communication
Freeplane Markdown depends on both the Freeplane core and the JSyntaxPane. It is also directly imported by the AI plugin as well.

The plugin imports many classes from the core Freeplane package. The most important ones are:
- `Controller, MModeController, SModeController`: it reveals that the plugin works with the core in both the MindMap visualization and in the styles
- `TextEditor, NodeController, MNodeController`: coupling with this class crucial to define text modification and alternative rendering.
- `ResourceController, CommandLineOptions`

## Freeplane API
The Freeplane API is an important plugin that define stable APIs to work with the core without directly touching it. It is crucial for anybody who wants to work with scripts, since all methods from scripts come from the Freeplane API. 
Its MapLoader API for instance allows maps to be opened without direct support from the GUI. Moreover, it offers a structured hierarchy for supporting authorization. It offers conditional styling settings, that are based on some booleans derived from user-written conditions. It supports the tags, with both getter and setter methods. It offers APIs to set and navigate bookmarks, as well as a broader tag definition, embedded with AI support.
### Communication
The Freeplane API, as an Architectural choice, does not depend on anything. It is loaded by the core Freeplane code to be called by scripts when needed. 

## Freeplane Forumla
This plugin is in charge of rendering and evaluating Groovy scripts inside the Freeplane MindMaps: it works as a common spreadsheet application, where the = followed by some text is substituted by the result of the corresponding Groovy expression (Groovy is a sort of simplified Java Language). It support Cyclic Graphs detection and avoidance: if a circular dependency is found, the script is blocked.  
It supports APIs to define formula traceability, and it allows update of forumlas that are cloned from another node (up to 2024 this was not possible). It supports global condition formatting, and newly created nodes are immediately under the rules. Moreover, it supports independent formatting engine: it means that the user is not forced to have LaTeX, formulas and data format active at the same time.
### Communication
The Formula plugin communicates with the core Freeplane, to manage computation within the map and to gather information upon user-defined data. Particularly, it communicates with:
- `Controller, ModeController, MModeController`: to compute formulas within the core mindmap visualizer
- `ResourceController`: to gather knowledge about user-defined settings
- `MapController`: to adapt to nodes within the map to trace information about formulas, from where do they come from and which nodes do they reference  

It communicates with `org.freeplane.plugin.scripts` to:
- send the intercepted formula as a script to be interpreted
- receive information about possible exceptions  

It communicates with the `JSyntaxPane` to adopt formatting settings to its text.

## Freeplane OpenMaps
Freeplane OpenMaps plugin allows mindmaps to show geographical locations. It requires a set of coordinates (lat, long) to be assigned to a node, and it will automatically embed the location within the file.  
The plugin registers to a NodeHook within the core to work and add its visualization data to the map. It implements persistence in terms of zomming of the geograhical location. It implements a listener that let the user add a new geographical location with a double click. Opening the OpenStreetMap viewer requires a click only. It supports undo and a special User-Agent that authenticates the client to OpenStreetMap servers to gather geographical information.
It implements the JMapViewer Java library.
### Communication
It communicates with the Freeplane core to subscribe to the mindmap workstation (`ModeController, MModeController`), to be compliant with the overall icon style within the whole application (`freeplane.org.icon`), to save data (`PersistentNodeHook`) and finally to get command-line instruction defined by users (`CommandLineOptions`)

## Freeplane Framework
It is the backbone of the software. It manages the application life-cycle following the OSGi pattern (Knopflerfish implementation). During the development, many major changes were implemented, such as API changes (to better clarify methods), new startup pipeline to succesfully load components, and the definition of the Freeplane API, that from 2018 onwards was defined as an independent plugin with its own lifecycle and, more importantly, without any dependency.  
It is responsible of managing security permissions, to avoid dangerous scripts and to block the software from reading from forbidden paths.  
It distributes the API doc file during the building process. 
### Communication
The Freeplane Framework does not depend on anything but the API. 

## Freeplane Scripts Plugin
This plugin is in charge of dealing with scripting in Freeplane. It supports Groovy as main scripting language, and it can modify nodes, change styles, automate workflow. It is based on three pillars:
1. It relies on a stable and public API
2. It is based on an engine that compiles scripts based on permissions
3. Scripts are written inside a graphic interface within the mindmap workstation

Internal Freeplane Objects and Data Structures are wrapped in Groovy Proxy items, and they are then exposed to the API. It supports a control panel that makes it possibile to define settings with higher priority than what the actual script will then try to do.
A script can perform get and set operations to understand edges values (between nodes in the mindmap), and it supports tags.  
It offers LLM and AI support, through unified tag access among all crucial parts of the software, and frontend uniformity is guaranteed as well.  
Freeplane Scripts plugin distinguish between embedded scripts (that are saved in a dedicated .mm file) and "script file" type of scripts, that are .groovy items that are saved on disk. It supports -R command-line option to execute Groovy script when the application is first launched.  
Security measures were stricter in the past, whereas today the software executes script files with all permissions granted, whereas API scripts have higher (but way more relaxed than in the 2010s) security standard they must meet.  

### Communications
It depends on the Freeplane JSyntaxPane plugin (for readability and UI features). It also relies on the Freeplane core.
It depends on:
- `ModeController, MModeController`: since scripting tools must be enabled by the user in the UI, the workstation must add support for them
- `CommandLineOptions`: it refers to the headless excution
- Indirectly, the API `Controller` is imported; this is done to create a bridge between the scripts and the API calls they are designed to do.