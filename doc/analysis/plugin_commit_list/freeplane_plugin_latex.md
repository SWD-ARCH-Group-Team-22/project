# LaTeX — Commit rilevanti

**Modulo:** `freeplane_plugin_latex`  
**Commit rilevanti (feature / fix / api_change):** 54 su 210 totali

> Integra il rendering **LaTeX/MathJax** nei nodi. Indispensabile per chi usa Freeplane in ambito scientifico, matematico o accademico per inserire equazioni e notazione formale nelle mappe.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 1 commit
- [2025](#2025) — 3 commit
- [2022](#2022) — 1 commit
- [2021](#2021) — 7 commit
- [2020](#2020) — 2 commit
- [2019](#2019) — 2 commit
- [2017](#2017) — 2 commit
- [2016](#2016) — 1 commit
- [2015](#2015) — 5 commit
- [2014](#2014) — 7 commit
- [2013](#2013) — 4 commit
- [2012](#2012) — 9 commit
- [2011](#2011) — 3 commit
- [2010](#2010) — 5 commit
- [2009](#2009) — 2 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-04-04 | `fix` | Issue #2867 fix NPE | `LatexRenderer.java` | [b27609a2](https://github.com/freeplane/freeplane/commit/b27609a277783114a3b12cbe51385075c54d2023) |

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-09-24 | `fix` | Issue #2682 Fix class cast exception | `ViewerController.java`, `LatexNodeHook.java` | [3de9d1e2](https://github.com/freeplane/freeplane/commit/3de9d1e2cedcb46254e6999d3ee8ad32a67e491c) |
| 2025-07-23 | `fix` | Fix latex rendered width, font and colors | `NoteStyleAccessor.java`, `NoteManager.java` +4 | [c9e842a5](https://github.com/freeplane/freeplane/commit/c9e842a5781f3b9389fb68f48f3a4ca157848b46) |
| 2025-05-18 | `feature` | Better support input method events | `IEditHandler.java`, `IUserInputListenerFactory.java` +18 | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-06-03 | `fix` | fix editor background colors on VAqua | `NoteStyleAccessor.java`, `MNoteController.java` +9 | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-05-13 | `fix` | Fix jsyntaxpane package import | `build.gradle`, `build.gradle` +1 | [fd935f1f](https://github.com/freeplane/freeplane/commit/fd935f1f882564cecd9d3998e2f710e406daaa82) |
| 2021-02-05 | `fix` | fix latex note editor | `LatexRenderer.java` | [aaac8d35](https://github.com/freeplane/freeplane/commit/aaac8d35f171aa6eeba7d4a80dbde7e20cca4f08) |
| 2021-01-18 | `fix` | fix LatexRenderer | `LatexRenderer.java` | [7bb3b7d5](https://github.com/freeplane/freeplane/commit/7bb3b7d56515eca9781bdf3a563c62c27a1d0622) |
| 2021-01-16 | `fix` | fix note views in maps | `MainView.java`, `NodeViewFactory.java` +4 | [b72ceda3](https://github.com/freeplane/freeplane/commit/b72ceda36165440f7e142cc9ea89b11cf4eb8c39) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | `NoteDialogStarter.java`, `RichTextModel.java` +9 | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown support | `build.gradle`, `FormulaEditor.java` +14 | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |

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
| 2019-10-18 | `fix` | fix plugin bundle imports | `build.gradle`, `build.gradle` | [bf81ff64](https://github.com/freeplane/freeplane/commit/bf81ff641d0a30e86271969f16da235483aa7b2e) |
| 2019-09-14 | `feature` | Support dark mode | `build.gradle`, `history_en.txt` +9 | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-09-17 | `feature` | add dependencies on jlatex-math fonts | `build.gradle` | [820920af](https://github.com/freeplane/freeplane/commit/820920afa2c1556250ef8fbcb6990d7ab5703c57) |

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
| 2015-01-01 | `feature` | new plugin 'freeplane_plugin_jsp' for jsyntaxpane including LaTeX enhancements (used by sc | `build.gradle`, `jsyntaxpane.jar` +12 | [27d69c29](https://github.com/freeplane/freeplane/commit/27d69c296ad8d456419913697dff5d0e598c01da) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-12-20 | `feature` | add more instructions to latex plugin | `build.gradle`, `build.gradle` | [b9ffacd3](https://github.com/freeplane/freeplane/commit/b9ffacd343e98a0af1ae9e76831cafd44c2d5966) |
| 2014-07-08 | `fix` | fix creation of latex viewers for node clones | `LatexNodeHook.java` | [3d725cc6](https://github.com/freeplane/freeplane/commit/3d725cc6a3604343041251ffdaf383fc87673a53) |
| 2014-07-05 | `feature` | Moving the latex plugin to the new build struture | `build.gradle`, `Activator.java` +15 | [e506597a](https://github.com/freeplane/freeplane/commit/e506597aa9e94fd5dbe3589b23d7af5ef040f313) |
| 2014-03-22 | `feature` | Add Format=Unparsed LaTeX and \unparsedlatex node prefix to allow LaTeX content that is so | `mm2latexinput.xsl`, `Resources_de.properties` +4 | [fa8385f0](https://github.com/freeplane/freeplane/commit/fa8385f0fd12f48c206507583caf6a4e7ae30da8) |
| 2014-02-10 | `feature` | Add option to disable LaTeX Syntax Highlighting Editor | `Resources_de.properties`, `freeplane.properties` +3 | [4ff1f94f](https://github.com/freeplane/freeplane/commit/4ff1f94fb95854b2d7c3981e7b93b18b3398cd79) |

---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-11-27 | `feature` | fix freeplane_ant create-plugin | `build.xml`, `.classpath` +6 | [05585087](https://github.com/freeplane/freeplane/commit/05585087c4b7798b25ccfb0ff2f4fcd11fec8c72) |
| 2013-09-29 | `fix` | fix ant build files | `build.xml`, `build.xml` +1 | [2c367ac7](https://github.com/freeplane/freeplane/commit/2c367ac7b92941a6841c7f3055a9262fb63b8f21) |
| 2013-08-03 | `feature` | Add prefs option for common/global LaTeX macros | `Resources_de.properties`, `OptionPanelBuilder.java` +9 | [59bad5cd](https://github.com/freeplane/freeplane/commit/59bad5cd722f50340e02287e949c281fb554b472) |
| 2013-01-12 | `fix` | Fix missing math mode decl in Freeplane_LaTeX.mm | `Freeplane_LaTeX.mm` | [7a474aab](https://github.com/freeplane/freeplane/commit/7a474aab0469ef0734676a47170d10735a64a52c) |

---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-22 | `fix` | LatexRegistration: fix string compare with == | `LatexRegistration.java` | [c12400a7](https://github.com/freeplane/freeplane/commit/c12400a7b2b7b15363456502526bcb1f49d49c04) |
| 2012-12-22 | `feature` | Add dependency on freeplane_plugin_script to freeplane_plugin_latex | `MANIFEST.MF` | [67b1f3da](https://github.com/freeplane/freeplane/commit/67b1f3da70a1b34acceaafe5ee91a0fd5a343784) |
| 2012-12-22 | `feature` | Integrate JSyntaxPane 0.9.6pre with support for LaTeX syntax highlighting | `LatexRenderer.java`, `MANIFEST.MF` +4 | [ee13aa28](https://github.com/freeplane/freeplane/commit/ee13aa2858e22a740cda10c0c637446668d5e51d) |
| 2012-11-23 | `feature` | "Add LaTeX formula...": replace by msgbox telling about deprecation of old LaTeX feature + | `Resources_de.properties`, `freeplane.properties` +5 | [73108439](https://github.com/freeplane/freeplane/commit/731084392c29d4dc42921e2094c32f1a2f49b5ee) |
| 2012-11-23 | `api_change` | TeXText: do not wrap input text in array-env (which would break automatic line breaking, a | `TeXText.java` | [b27f7335](https://github.com/freeplane/freeplane/commit/b27f7335feabdfb52c9633ba14cf78e68f2e2c0e) |
| 2012-11-11 | `feature` | add JLaTeXMath 1.0.1 prerelease, automatic line breaking in latex formulas in core now wor | `.classpath`, `MANIFEST.MF` +3 | [f14b8867](https://github.com/freeplane/freeplane/commit/f14b88672c0ee64e69228f04cb766b74b46dec8f) |
| 2012-10-18 | `fix` | bug fix for undo/ redo of adding a latex equation | `LatexNodeHook.java` | [4b28962f](https://github.com/freeplane/freeplane/commit/4b28962f98d9d58a10a30f01e7e25ab479d59f05) |
| 2012-05-18 | `fix` | fix tex | `LatexRenderer.java` | [cb2f3677](https://github.com/freeplane/freeplane/commit/cb2f36770f73b911cfa16ca8d233f5654833208e) |
| 2012-03-17 | `feature` | fix build files, include new jars | `ant.properties`, `build.xml` +1 | [63cf4f66](https://github.com/freeplane/freeplane/commit/63cf4f66a144cec92857aa0e7a8391bab18c0cb6) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-02-06 | `feature` | 957]: Can not add or edit LaTeX formula in Freeplane rev 1526 | `LatexEditor.java` | [018d9fac](https://github.com/freeplane/freeplane/commit/018d9face4cb73518c06d141816ec6c2a9dacd79) |
| 2011-01-28 | `fix` | Bug fix | `LatexViewer.java` | [ed920bac](https://github.com/freeplane/freeplane/commit/ed920bac4924d8cbe297dd9637e5e8661cbbcbfd) |
| 2011-01-22 | `feature` | remove the LatexExtension if user removes text from the new editor, LatexExtension is not  | `EditLatexAction.java`, `LatexEditor.java` +3 | [13674ed9](https://github.com/freeplane/freeplane/commit/13674ed93320e9405d2e83a403f16b7d2b0e6e57) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-07-29 | `feature` | 714]: Exception on saving which truncates the file : do not create latex extension without | `PersistentNodeHook.java`, `LatexNodeHook.java` | [bb606d13](https://github.com/freeplane/freeplane/commit/bb606d137b3bc01bb0a5c0c5e902fd28d8c4eb81) |
| 2010-07-17 | `fix` | use fix order of content viewers | `ExternalResource.java`, `ViewerController.java` +4 | [29ff1989](https://github.com/freeplane/freeplane/commit/29ff198914b7f15b19fbc32594de1b693242fc4b) |
| 2010-07-05 | `feature` | - remove redundant test resources from freeplane_ant - adjust test target create-plugin-ba | `.bzrignore`, `ant-1.7.1.jar` +16 | [761fe31d](https://github.com/freeplane/freeplane/commit/761fe31dc032b0bc4d560cd2d0d58612b47ccc69) |
| 2010-03-30 | `fix` | rename FpStringUtils to TextUtil, move it into core.util package and move all static metho | `MANIFEST.MF`, `ColorTracker.java` +163 | [06ed5406](https://github.com/freeplane/freeplane/commit/06ed54068f045191f8031fd9399021fd060c58ad) |
| 2010-01-30 | `feature` | Add OK and Cancel buttons to Latex Editor | `Resources_ar.properties`, `Resources_ca.properties` +29 | [5610d61c](https://github.com/freeplane/freeplane/commit/5610d61c3fc7f734efb92a475559d887760a829e) |

---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-12-15 | `fix` | build patch from ewl: separate properties | `ant.properties`, `build.xml` +12 | [db2ac954](https://github.com/freeplane/freeplane/commit/db2ac9547e843ffe9123d133e7e6cb30292727f9) |
| 2009-08-11 | `feature` | add some zoom support to latex plugin | `JZoomedHotEqn.java` | [88554c50](https://github.com/freeplane/freeplane/commit/88554c502d1dd9c9a5a9374ffa5caabd5b78e0b5) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
