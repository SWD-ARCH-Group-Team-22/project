# OpenMaps — Commit rilevanti

**Modulo:** `freeplane_plugin_openmaps`  
**Commit rilevanti (feature / fix / api_change):** 20 su 82 totali

> Integrazione con **OpenStreetMap**: permette di visualizzare e agganciare coordinate geografiche ai nodi, utile per mappe concettuali con componente spaziale.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2022](#2022) — 2 commit
- [2020](#2020) — 1 commit
- [2019](#2019) — 1 commit
- [2017](#2017) — 1 commit
- [2016](#2016) — 2 commit
- [2015](#2015) — 2 commit
- [2014](#2014) — 4 commit
- [2012](#2012) — 7 commit

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-12-13 | `fix` | Fix OpenMapsViewer by setting Freeplane specific user agent | `OpenMapsViewer.java` | [5d541e27](https://github.com/freeplane/freeplane/commit/5d541e27673112557fcb9dd0f68a52749fea496b) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-04-09 | `feature` | inline IconStoreFactory.create() | `FButtonBar.java`, `AttributeController.java` +14 | [16fcbdd5](https://github.com/freeplane/freeplane/commit/16fcbdd5b46e791b3a455ee577c2b05f0bd756f7) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-01-23 | `fix` | bug #2305 clicking in icon-area does not select node | `IconController.java`, `IconMouseListener.java` +2 | [ddb73bd9](https://github.com/freeplane/freeplane/commit/ddb73bd9db306cc5078b57a1ad783720db81a590) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a maven repo, a | `MANIFEST.MF`, `build.gradle` +24 | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-08-31 | `feature` | add IconMouseListener concept for clicks on icons and use it to call openmaps viewer when  | `MultipleImage.java`, `IconClickedEvent.java` +6 | [83e5bd24](https://github.com/freeplane/freeplane/commit/83e5bd24bfe85be7247b05042907554850433527) |
| 2014-07-08 | `feature` | Moved OpenMaps plugin to the new directory structure, couldn't find a maven repo for openm | `build.gradle`, `Activator.java` +12 | [7c7bdca9](https://github.com/freeplane/freeplane/commit/7c7bdca9ab49dc012dd5c00ca732131aea0eee99) |

---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-10-12 | `feature` | Undo now removes the openMaps data if the last command was a creation. Still need to imple | `OpenMapsExtension.java`, `OpenMapsNodeHook.java` | [8898b0b9](https://github.com/freeplane/freeplane/commit/8898b0b9e19bf47f192dd68f13fba149cd9f1a38) |
| 2012-09-28 | `fix` | fixed bug in storing the zoom | `OpenMapsNodeHook.java` | [40afbeb6](https://github.com/freeplane/freeplane/commit/40afbeb642bb4817efcc80c588c987b6f625d780) |
| 2012-09-23 | `fix` | Fixed bug with multiple NodeHooks being created | `OpenMapsNodeHook.java`, `OpenMapsRegistration.java` +3 | [c2288b9a](https://github.com/freeplane/freeplane/commit/c2288b9a3a110abad26d495cf6df7e3168b018b1) |
| 2012-09-23 | `fix` | Various Bug fixes | `OpenMapsNodeHook.java` | [c6f9d625](https://github.com/freeplane/freeplane/commit/c6f9d62586c8749d4a762aae2b6ef4e4d27698a5) |
| 2012-09-09 | `feature` | Added new listener for selecting locations (over a loop) | `LocationChoosenListener.java`, `OpenMapsNodeHook.java` +1 | [5b1416d3](https://github.com/freeplane/freeplane/commit/5b1416d3a7e72db9639fecd734ca6ed50e9302f3) |
| 2012-09-08 | `feature` | Added a new controller to allow double click location adding. Switched to Coordinate (JMap | `OpenMapsExtension.java`, `OpenMapsNodeHook.java` +3 | [004ee3f7](https://github.com/freeplane/freeplane/commit/004ee3f752d4b9e025c9abe67befdd373c37d133) |
| 2012-08-26 | `fix` | Fixed missing OpenMapsNodeHookAction.text bug and overided serveral persistant node method | `OpenMapsLocation.java`, `OpenMapsNodeHook.java` +2 | [8d89b703](https://github.com/freeplane/freeplane/commit/8d89b7031513fbdf9332fe494b7edf2868960b03) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
