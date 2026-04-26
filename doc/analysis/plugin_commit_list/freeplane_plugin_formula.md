# Formula — Commit rilevanti

**Modulo:** `freeplane_plugin_formula`  
**Commit rilevanti (feature / fix / api_change):** 51 su 187 totali

> Aggiunge il supporto alle **formule** nei nodi (sintassi simile a spreadsheet). Consente calcoli automatici, riferimenti ad altri nodi e aggregazioni, trasformando Freeplane in uno strumento di analisi dati visuale.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2025](#2025) — 2 commit
- [2024](#2024) — 2 commit
- [2022](#2022) — 2 commit
- [2021](#2021) — 5 commit
- [2020](#2020) — 2 commit
- [2019](#2019) — 3 commit
- [2018](#2018) — 10 commit
- [2017](#2017) — 1 commit
- [2016](#2016) — 1 commit
- [2015](#2015) — 4 commit
- [2014](#2014) — 2 commit
- [2013](#2013) — 2 commit
- [2012](#2012) — 1 commit
- [2011](#2011) — 5 commit
- [2010](#2010) — 9 commit

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-05-18 | `feature` | Better support input method events | `IEditHandler.java`, `IUserInputListenerFactory.java` +18 | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2025-04-04 | `fix` | fix NPE | `FormulaDependencyTracer.java` | [5b8d5f72](https://github.com/freeplane/freeplane/commit/5b8d5f72f48eb6ee5fda233615eb2a44cd56b485) |

---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-08-14 | `fix` | Simplify and fix ClassCastException | `NoteDialogStarter.java`, `EditNodeBase.java` +8 | [4a01a75a](https://github.com/freeplane/freeplane/commit/4a01a75a2e75b4ca44f1efbad0a5c90264ac8de1) |
| 2024-06-21 | `fix` | fix formula result refresh for nodes accessing clones | `AccessedNodes.java`, `MultipleNodeList.java` +5 | [66effa94](https://github.com/freeplane/freeplane/commit/66effa9440f7d0f5e1666d5b94c48bf45be0232f) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-11-24 | `feature` | Issue  #843 conditional formating script filter rules are not applied to the new node. | `ComparableByPriority.java`, `IMapChangeListener.java` +5 | [8f17ede4](https://github.com/freeplane/freeplane/commit/8f17ede4e786720796ad7c4feafb8d5dd97072c1) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-06-03 | `fix` | fix editor background colors on VAqua | `NoteStyleAccessor.java`, `MNoteController.java` +9 | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-03-07 | `feature` | Option to enforce modal editor dialogs | `preferences.xml`, `EditNodeDialog.java` +4 | [e30072b5](https://github.com/freeplane/freeplane/commit/e30072b59691a0cfe8393094c8e09bf0d3c976a5) |
| 2021-01-17 | `fix` | fix rendering | `FormatContentTransformer.java`, `MainView.java` +4 | [0c305a86](https://github.com/freeplane/freeplane/commit/0c305a867024a10fc23a8d8d07572fd669f419e8) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | `NoteDialogStarter.java`, `RichTextModel.java` +9 | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown support | `build.gradle`, `FormulaEditor.java` +14 | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |

### Dettagli commit con note

**[e30072b5](https://github.com/freeplane/freeplane/commit/e30072b59691a0cfe8393094c8e09bf0d3c976a5)** (2021-03-07) — Option to enforce modal editor dialogs

> #2888 Problem with the new feature (Non blocking editing of node core,
> details and notes in dialogs) added in (1.8.11)


---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-24 | `fix` | make latex editor non modal and fix blocking editor treatment | `NoteDialogStarter.java`, `EditNodeBase.java` +7 | [a6f20816](https://github.com/freeplane/freeplane/commit/a6f208166ce4b6dfe06327c0191a725bf6cc2048) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-09-28 | `feature` | Add new properties  to connector API : dashArray, opacity, width, labelFontFamily and labe | `ColorUtils.java`, `LinkBuilder.java` +10 | [f4c86c81](https://github.com/freeplane/freeplane/commit/f4c86c8129390c482d1823494186137497d77f63) |
| 2019-09-14 | `feature` | Support dark mode | `build.gradle`, `history_en.txt` +9 | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2019-08-10 | `feature` | Add NodeChangeListener to Freeplane API | `Map.java`, `NodeChangeListener.java` +5 | [746e83e0](https://github.com/freeplane/freeplane/commit/746e83e0565e3b37e24ea881802e16a2ed768b4b) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-11 | `fix` | fix exception trace pane width in formula editor | `FormulaEditor.java` | [66415885](https://github.com/freeplane/freeplane/commit/6641588575f68e94533431515e9a81ddb2003df8) |
| 2018-11-25 | `feature` | Support selection of multiple cells in attribute tables | `HighlightedElements.java`, `AttributeController.java` +5 | [3a90c16b](https://github.com/freeplane/freeplane/commit/3a90c16bdb0bc7269676dc6897d76a04f5d87cc8) |
| 2018-10-16 | `fix` | fix #2616 Reference from other maps v. 1.7.2_04 | `IMapLifeCycleListener.java`, `MapController.java` +2 | [27e3de61](https://github.com/freeplane/freeplane/commit/27e3de6156813702aa5bccc6e5b6835be86f0982) |
| 2018-10-15 | `fix` | Fix docu and names | `Dependencies.java`, `DependencyLookup.java` +8 | [82aecb58](https://github.com/freeplane/freeplane/commit/82aecb5843e6667536ba8ee0af2dba85eb060d46) |
| 2018-10-15 | `api_change` | getPrecendents() and getDependents() API | `NodeAttributeTableModel.java`, `Dependencies.java` +18 | [f273ade7](https://github.com/freeplane/freeplane/commit/f273ade7ab2c3a26633cf90e04af3c28c7093379) |
| 2018-10-15 | `fix` | fix it | `Activator.java`, `EvaluationDependencies.java` +1 | [1dbfc360](https://github.com/freeplane/freeplane/commit/1dbfc360b8d41c728b15f56078d78fa8a3816dde) |
| 2018-10-06 | `fix` | fix NPE | `EvaluateAllAction.java`, `FormulaCache.java` | [2cee80a0](https://github.com/freeplane/freeplane/commit/2cee80a0d196d041d43c8ad08ccdf32b806d5b5a) |
| 2018-10-05 | `fix` | fix NPE | `DependentsSearchStrategy.java`, `NodeScript.java` | [01e51f27](https://github.com/freeplane/freeplane/commit/01e51f27f41b3824a15d252df2dddfc28c3a4413) |
| 2018-10-05 | `fix` | fix recursive call | `DependentsSearchStrategy.java`, `FormulaDependencyTracer.java` | [938f149f](https://github.com/freeplane/freeplane/commit/938f149f38bca60aa2511cab404f5577f5e0fbd0) |
| 2018-10-03 | `fix` | fix saving of traced values | `FormulaDependencyTracer.java` | [e8ffd6cb](https://github.com/freeplane/freeplane/commit/e8ffd6cb3cbdcb763372aa543eebcfc523fbd615) |

### Dettagli commit con note

**[27e3de61](https://github.com/freeplane/freeplane/commit/27e3de6156813702aa5bccc6e5b6835be86f0982)** (2018-10-16) — fix #2616 Reference from other maps v. 1.7.2_04

> chandle how accessed closed maps are handled


---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-31 | `fix` | Fix latex and formula editors | `ConditionalContentTransformer.java`, `Activator.java` +1 | [3d92c063](https://github.com/freeplane/freeplane/commit/3d92c063dd0a69ff6ec6065577406d75f84f8e68) |
| 2015-07-17 | `feature` | 2195: Make data formatting, formula processing and LaTeX rendering independently configura | `preferences.mm`, `ConditionalContentTransformer.java` +7 | [925ec4ed](https://github.com/freeplane/freeplane/commit/925ec4ed74b24ed116c000393f0ad22e7d7ebe01) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a maven repo, a | `MANIFEST.MF`, `build.gradle` +24 | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |

---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-09-29 | `fix` | fix ant build files | `build.xml`, `build.xml` +1 | [2c367ac7](https://github.com/freeplane/freeplane/commit/2c367ac7b92941a6841c7f3055a9262fb63b8f21) |
| 2013-06-04 | `feature` | Add .gitignore for the `preferences.xml` files which are now built. | `.gitignore`, `.gitignore` | [8203c0a0](https://github.com/freeplane/freeplane/commit/8203c0a029ff7a2eebd17317a9badeb2715ccde3) |

---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-01-22 | `fix` | fix NPEs | `LinkTransformer.java`, `FormulaTextTransformer.java` | [c9bf3de8](https://github.com/freeplane/freeplane/commit/c9bf3de8fbb437fa4823fb8441dc1860bb002427) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-10-02 | `fix` | bug fix: restore no-formula check | `FormulaTextTransformer.java` | [df713a9a](https://github.com/freeplane/freeplane/commit/df713a9afae801ceae4ce45180fd80653d5855fd) |
| 2011-04-02 | `feature` | create plugin dependent submenus only if plugin is loaded | `mindmapmodemenu.xml`, `MenuBuilder.java` +1 | [bbbf5690](https://github.com/freeplane/freeplane/commit/bbbf5690ee4f4efe67c67942a37b3e3e82c43505) |
| 2011-03-07 | `fix` | fix compiler warnings | `CompareConditionAdapter.java`, `FormulaUpdateChangeListener.java` | [939c9fff](https://github.com/freeplane/freeplane/commit/939c9fff2e301cb126e254906e749312407587b7) |
| 2011-02-27 | `fix` | bug fix for opening formula editor | `AbstractTextTransformer.java`, `FormulaTextTransformer.java` | [eb1c2432](https://github.com/freeplane/freeplane/commit/eb1c243288cd05138059f95b89a3662047cbb51e) |
| 2011-01-02 | `feature` | initial implementation of new style options node numbering and text templates | `NodeStyleController.java`, `NodeStyleModel.java` +10 | [431f2103](https://github.com/freeplane/freeplane/commit/431f21038e18f0bdaacc9afd1c2fad050f0652d8) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-12-19 | `fix` | Move NodeIdHighLighter in its own jar file, fix JSyntaxPaneProxy, revert FormulaTextTransf | `.bzrignore`, `FormulaTextTransformer.java` +4 | [b030e51e](https://github.com/freeplane/freeplane/commit/b030e51e7be597310535cf999e183011ac0e569a) |
| 2010-12-18 | `feature` | add NodeIdHighlighter | `MapController.java`, `FormulaTextTransformer.java` +5 | [7b52a2fd](https://github.com/freeplane/freeplane/commit/7b52a2fd70ce82ac966121e1b27b428c7677f5b9) |
| 2010-11-14 | `fix` | bug fix: updating of formula results in AttributeTable | `AttributeTable.java`, `AttributeTableModelDecoratorAdapter.java` +3 | [0c6585ac](https://github.com/freeplane/freeplane/commit/0c6585acbaedf08efd71739ade958506d7be94c8) |
| 2010-10-31 | `feature` | Formula plugin: Display evaluated formulas...  - in attribute table  - in attribute toolti | `NodeAttributeTableModel.java`, `ITextTransformer.java` +5 | [3677d7a3](https://github.com/freeplane/freeplane/commit/3677d7a3048dd03dfb049168d1f417657d6740ff) |
| 2010-10-28 | `feature` | added new formula icon by Predrag Cuklin installed it as an icon for EvaluateAllAction | `formula.png`, `defaults.properties` | [519d314f](https://github.com/freeplane/freeplane/commit/519d314faf6f684e1eeb21a2ade4027c1652d488) |
| 2010-10-17 | `feature` | add defaults.properties to plugin jar files: fix build.xml | `build.xml`, `build.xml` | [25e674e1](https://github.com/freeplane/freeplane/commit/25e674e10803fa5b5cf8e6763b1a66dc842ddc86) |
| 2010-10-12 | `fix` | Bug fix : FormulaTextTransformer removed HTML formatting even if no script | `MainView.java`, `FormulaTextTransformer.java` +1 | [833005e6](https://github.com/freeplane/freeplane/commit/833005e60e6e8531b73311d27b3b0e7683e87a2a) |
| 2010-10-12 | `feature` | - read plugin default from file defaults.properties to avoid hardcoded defaults. Used in s | `ResourceController.java`, `AppletResourceController.java` +8 | [1309850d](https://github.com/freeplane/freeplane/commit/1309850ddbc06d0a413751be29bb975264bbb548) |
| 2010-10-03 | `feature` | - handle circular references - new option 'don't mark formula nodes' | `MainView.java`, `Resources_en.properties` +8 | [35e29691](https://github.com/freeplane/freeplane/commit/35e296913e602a3c3e037b49aebb9eefaad990f8) |

### Dettagli commit con note

**[3677d7a3](https://github.com/freeplane/freeplane/commit/3677d7a3048dd03dfb049168d1f417657d6740ff)** (2010-10-31) — Formula plugin: Display evaluated formulas...  - in attribute table  - in attribute tooltip  - in note tooltip  - when 'Show Notes in Map' is enabled

> Refactored TextController:
>  - getText() renamed to getTransformedText()
>  - new getText() returns untransformed text
>  - avoid direct model access in MainView

**[1309850d](https://github.com/freeplane/freeplane/commit/1309850ddbc06d0a413751be29bb975264bbb548)** (2010-10-12) — - read plugin default from file defaults.properties to avoid hardcoded defaults. Used in scripting and formula plugin.

> - remove deprecation of ResourceController.getIntProperty(String, int) and add
>   an appropriate comment instead
> 
> - remove unused ResourceController.loadProperties(FromXML)
> 
> - formulas: changed preferences variables: enable[plugin|caching] -> disable...


---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
