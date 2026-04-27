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
