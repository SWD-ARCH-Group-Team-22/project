# Journal
## Author: Gaia Martignone

### 18/04/2026
**Initial understanding of the project requirements and Freeplane documentation**

*   Started reviewing the general requirements of the Software Design and Architecture project.
*   Focused on understanding the expected deliverables: overview report, design report, software architecture report, and individual journal.
*   Read the available Freeplane documentation to get a first understanding of the system, its purpose, and its general structure.
*   Identified Freeplane as a large open-source Java desktop application for mind mapping, organized around a core application and several plugin-based extensions.
*   Took initial notes on the distinction between the two main parts of the project:
    *   **Design analysis**, focused on dependencies between modules/components and design patterns.
    *   **Software architecture analysis**, focused on reconstructing the architecture using the C4 model.

### 30/04/2026
**Planning the dependency analysis**

*   Started defining the scope of my part of the design report, focused on the analysis of dependencies between modules and software components.
*   Organized the work into three main steps:
    *   first, analyse **knowledge dependencies**, using the Git history and the co-change data;
    *   then, analyse **code dependencies**, looking at the static structure of the project;
    *   finally, compare the two results to understand where static dependencies and historical co-changes match or differ.
*   Started analysing the material already created by teammates in our `project` repository.
*   Checked the branch `feat/design_import_dependencies`, which is dedicated to this part of the project.
*   Analysed the content of the folder `doc/analysis/mutual_commit_changes`, where the outputs of the automated dependency analysis were collected.
*   The co-change analysis tool analysed the Git commit history and identified files that are often modified together.
*   The generated reports were divided into three different time windows:
    *   full repository history;
    *   last 10 years;
    *   last 5 years.
*   Defined the next step: analyse the different report files, starting from the most recent ones. The goal is to extract the most relevant file pairs and group them by functional area, so that they can later be compared with the static code dependencies.

### 02/05/2026
**Analysis of the last-5-years co-change report**

*   Started analysing the last-5-years co-change report, using the file `report_last_5_years/top_pairs.csv`.
*   Chose this report as a starting point because it gives a more recent view of the files that currently tend to evolve together.
*   Checked the structure of the CSV file, focusing on the file pairs, the class names, the number of co-changes, and the total number of changes for each file.
*   Began grouping the most frequent pairs by area of the application, instead of treating them as isolated file pairs.
*   The first groups that emerged are:
    *   the Swing map view, with classes such as `MapView`, `NodeView`, and `MainView`;
    *   the outline subsystem, with classes such as `ScrollableTreePanel`, `BreadcrumbPanel`, and `OutlinePane`;
    *   tag and icon management, with classes such as `TagCategories`, `TagCategoryEditor`, and `TagEditor`;
    *   the relation between API and scripting, with classes such as `Node`, `NodeRO`, and `NodeProxy`;
    *   text rendering plugins, with classes such as `FormulaTextTransformer`, `LatexRenderer`, and `MarkdownRenderer`.
*   This first inspection helped me identify which parts of the code are worth analysing in more detail.
*   The next step will be to open the corresponding Freeplane classes and check whether the historical co-changes are also reflected in the static code structure.