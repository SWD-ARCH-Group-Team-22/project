# Software Design and Architecture Project Repository
This repository contains the whole project for the Software Design and Architecture Polito course in the academic year 2025-2026.  
The final goal is to produce a complete and understandable analysis of both design and architecture of the Freeplane software, an open-source tool for students and teachers  

## Repository Structure
A strict structure has been defined to make everyone's life easier; please comply with that while working in the project.
- `journals`: here put your weekly journal, following the guidelines (if you wish)
- `doc/reports`: here we will store the final reports
- `doc/charts/puml`: here put all charts, in their respective subdirectory. If you put PlantUML charts here, an automatic pipeline will convert them in .pdf and .svg
- `doc/charts/C4`: here put all charts, in their respective subdirectory. If you put C4 charts and models here, an automatic pipeline will convert them in .pdf and .svg
- `doc/analysis/md`: here put all analysis notes in Markdown. If you put the .md files here, an automatic pipeline will convert them in .pdf and .svg
- `img`: in the respective subdirectory, you could find all file that have been subsequentely automatically converted

## Automatic journal update and commit messages requirements
Keeping track of our work can be difficult. To help everyone, a small commit-msg hook was developed to fill journals automatically. All you have to do is writing a long, self-explaining commit messages, that complies with Git standards; it should start with either one of the following 
- feat:      (New feature)"
- fix:       (Bug fix)"
- hotfix:    (Urgent production fix)"
- chore:     (Routine tasks, dependencies)"
- docs:      (Documentation changes)"
- refactor:  (Code rewrite, no new features/fixes)"
- test:      (Adding/updating tests)"
- ci/build:  (Pipeline or build system changes)"
- style:     (Formatting, white-space)"
- perf:      (Performance improvements)"

To enable the hook, you must run locally the following script once:  
`chmod +x .githooks/commit-msg`

---

## Automatic Diagram Conversion Pipeline (CI/CD)

To abstract away the complexity of rendering architectural diagrams and ensure a unified graphic standard for our documentation, we have implemented a dedicated GitHub Action pipeline. You do not need to manually export your diagrams to images or PDFs before pushing your code. 

### How the Converter Works
Whenever you push changes to the `doc/charts/puml/**` or `doc/charts/C4/**` directories, the automated pipeline triggers in the background. The workflow executes the following steps:

1. **LikeC4 Translation:** It parses all the `.c4` source files in the C4 directory and strictly translates the architectural model into standard PlantUML syntax.
2. **Vector Rendering (SVG):** It utilizes the official Java-based PlantUML compiler to generate scalable, high-resolution SVG files for both standard UML diagrams and the translated C4 models.
3. **Print-Ready Conversion (PDF):** It utilizes `librsvg` to losslessly convert every generated SVG into a high-quality PDF, perfect for inclusion in our LaTeX/Markdown final reports.
4. **Cleanup & Auto-Commit:** It completely removes all intermediate and temporary files (preventing repository bloat) and automatically commits the `.svg` and `.pdf` files back into the corresponding `doc/deliverables/` directories.

### Crucial Developer Workflow Step: `git pull`
Because the GitHub Action creates the final SVGs and PDFs directly on the GitHub server *after* your push, your local machine will not immediately have these new files. 

**Always run `git pull` after the GitHub Action finishes executing successfully.** If you skip this step, your local repository will fall out of sync with the remote, and subsequent pushes will likely result in merge conflicts.


### Modeling Architecture with LikeC4

For our C4 Model diagrams, we strictly utilize **LikeC4**, a domain-specific language designed to describe software architecture at various levels of abstraction. Instead of manually drawing boxes and lines, LikeC4 allows us to define the *model* of Freeplane's architecture as code and automatically generate multiple views.

To learn how to use LikeC4, write the syntax, define models, and generate views, **please carefully follow the official tutorial:**

🔗 **[LikeC4 Official Tutorial](https://likec4.dev/tutorial/)**

#### Recommended Local Setup
While the GitHub Action handles the final rendering, working blindly is inefficient. To get real-time syntax highlighting, error checking, and live diagram previews locally:
1. Install **Visual Studio Code**.
2. Install the official **LikeC4 extension** from the VS Code marketplace.
3. This will allow you to see exactly how your diagrams will look as you type, before you push them to the repository.
