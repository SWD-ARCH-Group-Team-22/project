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

## Automatic journal update
The repository is provided with some githooks to enhance automatization of processes.  
Since it may be easy to forget journal compilation, developers are given:
- A post-commit hook: this script automatically updates the journal with information about the commit, date, and username. A TODO placeholder is placed in the description field.  
- A pre-push hook that avoid pushing to remote repository if the TODO placeholders haven't been replaced with a proper descripiton. 

These hooks are downloaded when the repository is cloned. However, Github security measures require the developer to independently activate them. You can do iy by running:
`chmod +x .githooks/post-commit`
`chmod +x .githooks/pre-push`