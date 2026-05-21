# Bug Report — Commit rilevanti

**Modulo:** `freeplane_plugin_bugreport`  
**Commit rilevanti (feature / fix / api_change):** 41 su 136 totali

> Strumento interno per la **segnalazione bug**: raccoglie informazioni di sistema, log e contesto della mappa per facilitare il reporting agli sviluppatori.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2024](#2024) — 1 commit
- [2022](#2022) — 4 commit
- [2020](#2020) — 1 commit
- [2019](#2019) — 1 commit
- [2018](#2018) — 3 commit
- [2017](#2017) — 2 commit
- [2016](#2016) — 4 commit
- [2015](#2015) — 4 commit
- [2014](#2014) — 3 commit
- [2013](#2013) — 1 commit
- [2012](#2012) — 5 commit
- [2011](#2011) — 3 commit
- [2010](#2010) — 3 commit
- [2009](#2009) — 6 commit

---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-03-05 | `fix` | Generate bug reports only for Freeplane own errors | `ReportGenerator.java` | [d7534fad](https://github.com/freeplane/freeplane/commit/d7534fad09ca3d0fcfad6ffb2e49a6424b1730b3) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-02-27 | `feature` | add null check | `ReportGenerator.java` | [bc1ce11b](https://github.com/freeplane/freeplane/commit/bc1ce11b449a9531c81d8580d414fde218452454) |
| 2022-02-27 | `fix` | Don't submit bug reports related to groovy runtime errors | `ReportGenerator.java` | [510b9eb9](https://github.com/freeplane/freeplane/commit/510b9eb92fe9d2fb79be9e94dc0fd3f6c5f54b47) |
| 2022-02-27 | `fix` | remove file paths from submitted bug reports | `BugFormatter.java` | [a16efaf5](https://github.com/freeplane/freeplane/commit/a16efaf53193e58e122a7cb0d37b971c7507c3a0) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-01-30 | `fix` | fix bug report url | `ReportGenerator.java` | [3150b7fb](https://github.com/freeplane/freeplane/commit/3150b7fb847195fafdd42d11c1b56445f48e6978) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-11-24 | `fix` | Do not show bug report dialog in headless mode | `ReportGenerator.java` | [132c472a](https://github.com/freeplane/freeplane/commit/132c472a487468148b51da2525dc7a949e8b6d5a) |
| 2018-08-21 | `feature` | Add "deny" button to quick filter | `build.gradle`, `Resources_af.properties` +46 | [a8a1253f](https://github.com/freeplane/freeplane/commit/a8a1253f5b0fbab1a0ecac9f3456a508ca351f8c) |
| 2018-01-27 | `api_change` | Use Icon (interface) instead of SVGIcon or ImageIcon | `ResourceController.java`, `AFreeplaneAction.java` +16 | [9f50b315](https://github.com/freeplane/freeplane/commit/9f50b31569e5724e9929feab8eb2f66610ac7a5e) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-04-02 | `fix` | Fix error bitton icon and size | `freeplane.properties`, `ReportGenerator.java` | [98e2422e](https://github.com/freeplane/freeplane/commit/98e2422e4ae4c29534bb02cabc0ba6006a50f560) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-06-18 | `fix` | Show bug report dialog even in final version if property org.freeplane.plugin.bugreport.di | `freeplane.properties`, `ReportGenerator.java` | [040b42c3](https://github.com/freeplane/freeplane/commit/040b42c31b1f2e56eef081391219a75327b5a4a4) |
| 2016-04-10 | `fix` | execute bug report submission as privileged action | `ReportGenerator.java` | [11bc0b2e](https://github.com/freeplane/freeplane/commit/11bc0b2e44cfb0b807c96c874dd25d9f5c994fe7) |
| 2016-04-10 | `fix` | Fix some bugs related to security checks | `build.gradle`, `ReportGenerator.java` +2 | [0ee6aef1](https://github.com/freeplane/freeplane/commit/0ee6aef160140dd19c6c2e71588de8a221751604) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-11-28 | `fix` | Fix git revision information | `git.gradle`, `build.xml` +1 | [44e35149](https://github.com/freeplane/freeplane/commit/44e351491102142447dc4d6c2a8b5e70b1d383a5) |
| 2015-11-28 | `fix` | Fix git revision information | `build.xml`, `ReportGenerator.java` | [820e67e6](https://github.com/freeplane/freeplane/commit/820e67e6b7fadcdbefbe12fa86bf77f43a530102) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a maven repo, a | `MANIFEST.MF`, `build.gradle` +24 | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-04-13 | `feature` | Changing bugreport plugin to the new file layout | `Activator.java`, `BugFormatter.java` +5 | [37775a6d](https://github.com/freeplane/freeplane/commit/37775a6d0aa2328ede1e55704b60306458f21a6d) |

---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-04-21 | `fix` | fix NPE in case of logging from the SingleInstanceManager when 'single instance' mode is o | `ReportGenerator.java` | [6a0eaed5](https://github.com/freeplane/freeplane/commit/6a0eaed5a96c4479e80627303810367974568d1a) |

---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-25 | `feature` | Create headless package. The headless worker thread and executor are maintained in Headles | `UndoHandler.java`, `FrameController.java` +8 | [597493e7](https://github.com/freeplane/freeplane/commit/597493e7db05ac58556af9e67070f90bd7a3b97d) |
| 2012-08-12 | `fix` | do not ask to submit bug reports for final versions, assume denied | `FreeplaneVersion.java`, `freeplane.properties` +1 | [40a488bc](https://github.com/freeplane/freeplane/commit/40a488bca434a355638451e7b07bdfd84266ec62) |
| 2012-04-20 | `feature` | allow to add user identification to automatic bug reports, display "previous report" heade | `preferences.xml`, `freeplane.properties` +3 | [467eb5cc](https://github.com/freeplane/freeplane/commit/467eb5cca37ad795d68baf010425bd7be91bfb6e) |
| 2012-04-17 | `fix` | format month as number in bug reports | `ReportGenerator.java` | [aef140ba](https://github.com/freeplane/freeplane/commit/aef140babcaddfeb91f76c78c4d35aba75806553) |
| 2012-04-15 | `fix` | include a reference to the prevous report in automatic bug reports | `ReportGenerator.java` | [e9cca8a0](https://github.com/freeplane/freeplane/commit/e9cca8a022e7546c5f676c04668f9382e9a5c14f) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-10-08 | `fix` | Fix auto bugs | `browsemodemenu.xml`, `mindmapmodemenu.xml` +13 | [ed1f1694](https://github.com/freeplane/freeplane/commit/ed1f16943afffb138b24a37265d534cd52aa9c69) |
| 2011-09-25 | `fix` | Transmit bzr revision info in bug reports | `build.xml`, `Activator.java` +1 | [43639fb5](https://github.com/freeplane/freeplane/commit/43639fb53e9fda31011e678eb3f9f8e3860c9e6c) |
| 2011-08-07 | `feature` | Implicitly remove mnemonic symbol "&" from all language properties.  To keep it new method | `SetBooleanPropertyAction.java`, `OptionPanel.java` +37 | [58c24897](https://github.com/freeplane/freeplane/commit/58c248971b98a22c06a0cc262e2989d02573be5c) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-08-18 | `fix` | do not send bug reports from bugreport plugin to avoid infinite loops | `XmlRpcHandler.java` | [ef514caa](https://github.com/freeplane/freeplane/commit/ef514caa9c5dcbadae044322ccb5dccadc67139b) |
| 2010-03-30 | `fix` | rename FpStringUtils to TextUtil, move it into core.util package and move all static metho | `MANIFEST.MF`, `ColorTracker.java` +163 | [06ed5406](https://github.com/freeplane/freeplane/commit/06ed54068f045191f8031fd9399021fd060c58ad) |
| 2010-03-21 | `fix` | Remove wanted bug reports from auto.properties | `ManualBugReporter.java`, `ReportRegistry.java` +1 | [f0c738ce](https://github.com/freeplane/freeplane/commit/f0c738ce27f93a8a491fc797ba080efc25121e5e) |

---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-12-24 | `fix` | 356]: Encryption violation triggers Automatic bug report | `NodeModel.java`, `XmlRpcHandler.java` | [d50325de](https://github.com/freeplane/freeplane/commit/d50325de9aded537e806bd1438102399b7a443e9) |
| 2009-12-15 | `fix` | build patch from ewl: separate properties | `ant.properties`, `build.xml` +12 | [db2ac954](https://github.com/freeplane/freeplane/commit/db2ac9547e843ffe9123d133e7e6cb30292727f9) |
| 2009-07-23 | `feature` | bug fix: do not start new timer on blinking in reminder | `ReminderExtension.java`, `ReminderHook.java` +1 | [fcb759d7](https://github.com/freeplane/freeplane/commit/fcb759d7d8056f55f752148b4620f57df144b4e5) |
| 2009-07-22 | `feature` | add thread with stack trace output to bug report plug-in | `Activator.java` | [ba88361b](https://github.com/freeplane/freeplane/commit/ba88361b284f733157392c0ee937d241bdce66ae) |
| 2009-07-20 | `fix` | automatic bug report can be initiated by user by pressing "ALT+SHIFT+CONTROL b" if Freepla | `Activator.java` | [b064f530](https://github.com/freeplane/freeplane/commit/b064f530589f0f6d79a88b3d28cb40d1da575bab) |
| 2009-06-14 | `fix` | bug report dialog and bug report policy option in preferences | `preferences.xml`, `freeplane.properties` +2 | [9631078d](https://github.com/freeplane/freeplane/commit/9631078d9682493f964a7e855bdd3192807cf8d0) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
