# Framework OSGi — Commit rilevanti

**Modulo:** `freeplane_framework`  
**Commit rilevanti (feature / fix / api_change):** 146 su 669 totali

> Il **framework OSGi** che gestisce il ciclo di vita dei plugin: caricamento, dipendenze, isolamento dei moduli. È la spina dorsale dell'architettura modulare di Freeplane.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 1 commit
- [2025](#2025) — 4 commit
- [2024](#2024) — 10 commit
- [2023](#2023) — 1 commit
- [2022](#2022) — 8 commit
- [2021](#2021) — 4 commit
- [2020](#2020) — 7 commit
- [2019](#2019) — 5 commit
- [2018](#2018) — 9 commit
- [2017](#2017) — 3 commit
- [2016](#2016) — 15 commit
- [2015](#2015) — 11 commit
- [2014](#2014) — 5 commit
- [2013](#2013) — 13 commit
- [2012](#2012) — 7 commit
- [2011](#2011) — 8 commit
- [2010](#2010) — 22 commit
- [2009](#2009) — 13 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-02-09 | `fix` | fix windows installer script | `Freeplane.iss` | [b6ce1731](https://github.com/freeplane/freeplane/commit/b6ce1731e2e8536dfcefd36c5162bb176b834cbf) |

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-08-10 | `feature` | Fix Gradle 9.0 test discovery strictness | `build.gradle`, `build.gradle` | [7098c15e](https://github.com/freeplane/freeplane/commit/7098c15e87743baf55f6b44f419b5695a74bfebd) |
| 2025-08-10 | `fix` | Fix Gradle 9.0.0 compatibility issues | `bin.dist.gradle`, `build.gradle` +3 | [bad0e0cd](https://github.com/freeplane/freeplane/commit/bad0e0cddbfc0fae7824d19acc61687d4294aebf) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts | `OptionPanel.java`, `PathProperty.java` +29 | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-02-28 | `fix` | fix package name | `freeplane.sh` | [bd746d1f](https://github.com/freeplane/freeplane/commit/bd746d1faaa25bf13d591a4a17f2712f5c7b5a07) |

### Dettagli commit con note

**[7098c15e](https://github.com/freeplane/freeplane/commit/7098c15e87743baf55f6b44f419b5695a74bfebd)** (2025-08-10) — Fix Gradle 9.0 test discovery strictness

> - Add failOnNoDiscoveredTests = false for projects with non-JUnit test files
> - Many subprojects have debugging/demo apps in test directories, not actual tests
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[bad0e0cd](https://github.com/freeplane/freeplane/commit/bad0e0cddbfc0fae7824d19acc61687d4294aebf)** (2025-08-10) — Fix Gradle 9.0.0 compatibility issues

> - Replace deprecated fileMode with filePermissions syntax
> - Remove PartialJar class incompatible with Gradle 9.0, use shared pattern variables instead
> - Fix XmlNodePrinter deprecation in emoji.gradle with XmlUtil.serialize
> - Maintain DRY principle by defining editorJarIncludes/osgiJarIncludes variables
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3)** (2025-05-24) — Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts

> - Implement org.freeplane.api.swing.JFileChooser that wraps setUI() in doPrivileged()
> - Resolves AccessControlException when FlatLaf tries to use reflection in restricted environments
> - Export new package in OSGi system packages for script accessibility
> - Include JFileChooser in API generator documentation
> 
> Fixes FlatLaf styling errors in Groovy scripts that use file choosers.


---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-11-30 | `feature` | create 2 windows distributions | `.gitignore`, `dist.gradle` +2 | [9ca50c55](https://github.com/freeplane/freeplane/commit/9ca50c55feb5deba9d4e0fe7ca8c708d8ce32898) |
| 2024-11-24 | `fix` | fix encoding | `Freeplane.iss` | [0ed3dcad](https://github.com/freeplane/freeplane/commit/0ed3dcad056e057d253a4374380171da19780bca) |
| 2024-11-24 | `feature` | Add new options to freeplane.bat | `freeplane.bat` | [1db8e0c5](https://github.com/freeplane/freeplane/commit/1db8e0c56229b04246b600060f738726fba5358c) |
| 2024-08-24 | `fix` | Fix exclusion pattern for l4j.ini files in windown installer | `Freeplane.iss` | [4e9a5abf](https://github.com/freeplane/freeplane/commit/4e9a5abf528b7ced092782bc8ed7f1fd7e73c5e3) |
| 2024-08-17 | `fix` | fix version number | `Freeplane.iss` | [64602f40](https://github.com/freeplane/freeplane/commit/64602f406af00c3893d1dd7529022dd61aa5f88b) |
| 2024-02-02 | `fix` | fix eclipse configuration in gradle | `build.gradle`, `build.gradle` | [ce7cf789](https://github.com/freeplane/freeplane/commit/ce7cf789de677eb858829b58f74785fbd7421936) |
| 2024-01-22 | `fix` | fix launcher (revert) | `freeplane.bat`, `mac.dist.gradle` | [fb719bb4](https://github.com/freeplane/freeplane/commit/fb719bb4dc30eef6eac669941192b8c660b209e3) |
| 2024-01-22 | `fix` | fix launcher configuration | `build.gradle`, `freeplane.xml` +3 | [e653bc1e](https://github.com/freeplane/freeplane/commit/e653bc1ee2309ccff82334d44cabddf798e20f99) |
| 2024-01-19 | `fix` | fix java 8 version number | `freeplaneConsole.lj4.xml`, `freeplaneGui.lj4.xml` | [0604b4ec](https://github.com/freeplane/freeplane/commit/0604b4ec408426d0a1bbc59a150add1a77f98e5e) |
| 2024-01-17 | `feature` | Support running Freeplane under Java 8 and Java 11 on Windows | `build.gradle`, `freeplaneConsole.lj4.xml` +3 | [8fe2aa54](https://github.com/freeplane/freeplane/commit/8fe2aa54115a5805935fec5f47c06141b84e7f29) |

---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-10-15 | `feature` | update launch4j config files to support the latest launch4j version 3.50 | `freeplaneConsole.lj4.xml`, `freeplaneGui.lj4.xml` | [676e7b6d](https://github.com/freeplane/freeplane/commit/676e7b6d63d76b3562071fedee26210b69fba6bb) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-10-29 | `feature` | add permission java.awt.AWTPermission "watchMousePointer" | `freeplane.policy`, `freeplane.policy` | [c725f317](https://github.com/freeplane/freeplane/commit/c725f31740618b65c9ebd4bf7a5f191a64cae726) |
| 2022-09-11 | `feature` | add url parameter architecture=x86-64-bit | `freeplaneConsole.lj4.xml`, `freeplaneGui.lj4.xml` | [b7d1a428](https://github.com/freeplane/freeplane/commit/b7d1a428b290d0819a67d512b43c708a49232d8d) |
| 2022-03-27 | `feature` | add missing bracket | `freeplane.sh` | [46551618](https://github.com/freeplane/freeplane/commit/465516188f4de4789cf3f0626f6f4971d0f46fd6) |
| 2022-03-27 | `feature` | create windows distribution containing java-runtime | `.gitignore`, `createJavaRuntimeImage.sh` +5 | [07b76b95](https://github.com/freeplane/freeplane/commit/07b76b95b6711a5467fcf13bebd270b175e9475f) |
| 2022-03-25 | `fix` | fix windows launcher | `freeplaneConsole.lj4.xml`, `freeplaneGui.lj4.xml` +2 | [b1cccb15](https://github.com/freeplane/freeplane/commit/b1cccb155ce2d09dae022c30203ca2013659bdcb) |
| 2022-03-25 | `feature` | Support java 15, 16 and 17 | `build.gradle`, `freeplaneConsole.lj4.xml` +5 | [64bd241e](https://github.com/freeplane/freeplane/commit/64bd241ed2e99fd98ee2b5cebcf1ebe96423f0bb) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-01-21 | `fix` | fix the issue that freeplane.exe cannot launch | `freeplaneGui.lj4.xml` | [fdca7d4e](https://github.com/freeplane/freeplane/commit/fdca7d4ee52ef43d5aa640ad86e8ebd3f90b7546) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-05-09 | `feature` | configure add-exports and add-opens for linux | `freeplane.sh` | [6b420ee6](https://github.com/freeplane/freeplane/commit/6b420ee61fa125a6f4d805b7ae6935eb24df8e7d) |
| 2021-04-24 | `feature` | Update portable launcher to use new icons and OpenJDK JRE Portable 64-bit Java | `FreeplanePortable.ini`, `appicon.ico` +6 | [2922b3fa](https://github.com/freeplane/freeplane/commit/2922b3fa641b074986f64fa7c047598a8009bfac) |
| 2021-03-20 | `fix` | deploy with Java15 to fix default MacOS look and feel (non vaqua) | `Compat.java`, `FrameController.java` +2 | [bd677400](https://github.com/freeplane/freeplane/commit/bd677400946069d063841d33b455843b4cb780ad) |
| 2021-01-11 | `feature` | replace freeplane app icons by new artwork  by Stuart Robertson | `Freeplane_app_menu_128.png`, `Freeplane_frame_icon.png` +12 | [1965cfa0](https://github.com/freeplane/freeplane/commit/1965cfa0f26a11df397b02455909a95911ac144a) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-24 | `feature` | add dependency and options for vaquaorg.violetlib:vaqua:9  with mac os look and feel | `build.gradle`, `mac_info_plist.xslt` +2 | [063077bd](https://github.com/freeplane/freeplane/commit/063077bd4ebfce0903a83203e810f37d9e0d62d7) |
| 2020-03-12 | `fix` | fix copyright | `Freeplane_without_Java.iss` | [67b65054](https://github.com/freeplane/freeplane/commit/67b65054b9767d36c386328f8a622e964efe0530) |
| 2020-02-28 | `feature` | remove directory fwdir from BIN not required with the new knopflerfish | `build.gradle` | [8329cb04](https://github.com/freeplane/freeplane/commit/8329cb048ee2b72a7e417923bc5932d09c52d31e) |
| 2020-02-23 | `fix` | fix Info.plist white space | `mac_info_plist.xslt` | [6b01d7d6](https://github.com/freeplane/freeplane/commit/6b01d7d6b92f2e55d8cc12337519282376c0649f) |
| 2020-02-23 | `fix` | fix file associations using old plist keys | `file-associations.config`, `mac_info_plist.xslt` +1 | [08082101](https://github.com/freeplane/freeplane/commit/0808210118b898c46e4e5f66c3c87c7813073dbe) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-02-08 | `feature` | Add uninstaller parameters /DELETE_CONFIGURATION_FILES and /KEEP_CONFIGURATION_FILES | `Freeplane_without_Java.iss` | [8d434e42](https://github.com/freeplane/freeplane/commit/8d434e42fa77507efcaca11c06597a8cdb86f903) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-10-05 | `fix` | fix start sequence | `CommandLineParser.java`, `ActivatorImpl.java` +1 | [9b84c570](https://github.com/freeplane/freeplane/commit/9b84c5708dee049e65aea0af589b8022621b8113) |
| 2019-09-22 | `feature` | Improve windows installer translations, add spanish and portuguese | `Croatian.isl`, `Freeplane_without_Java.iss` +5 | [da9cff08](https://github.com/freeplane/freeplane/commit/da9cff0836e7e67e69dd78d82e0fd143027f60bf) |
| 2019-09-08 | `api_change` | API change: replace interface Map by MindMap, deprecate Map | `Controller.java`, `ControllerRO.java` +14 | [04b99850](https://github.com/freeplane/freeplane/commit/04b9985053bac60f98a4bbf2404b4e818d26993a) |
| 2019-01-27 | `api_change` | rename API method loader to mapLoader | `Controller.java`, `HeadlessMapCreator.java` +3 | [d0125d20](https://github.com/freeplane/freeplane/commit/d0125d208316f73aabdecc896b719ab2ec5403bd) |
| 2019-01-16 | `feature` | consider new location of java-atk-wrapper under linux in policy files | `freeplane.policy`, `freeplane.policy` | [6759ef7e](https://github.com/freeplane/freeplane/commit/6759ef7e473c9bbbf2fac408c6123db4dfb0a063) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-28 | `fix` | fix build on Linux | `build.gradle` | [c8ac5a89](https://github.com/freeplane/freeplane/commit/c8ac5a897324f8d7a4c088fc74ed0ce8fbd551da) |
| 2018-11-04 | `fix` | Test script execution using API and fix script execution permission | `TestApp.java`, `ScriptProxy.java` | [2beacb26](https://github.com/freeplane/freeplane/commit/2beacb26d61fd5dddcde1df67ad67302d26039a8) |
| 2018-11-01 | `feature` | Revert "Add property -Dorg.knopflerfish.osgi.registerserviceurlhandler=false to run under  | `props.xargs` | [21e56ffe](https://github.com/freeplane/freeplane/commit/21e56ffe24d235b0d2a3cf9cf518b1fe30f60201) |
| 2018-10-20 | `feature` | Add property -Dorg.knopflerfish.osgi.registerserviceurlhandler=false to run under tomcat | `props.xargs` | [68959b75](https://github.com/freeplane/freeplane/commit/68959b7555098ac77891e1899cd2d3a71a03ae70) |
| 2018-07-19 | `api_change` | MapLoader api and refactoring | `MapController.java`, `MapModel.java` +14 | [d2c45816](https://github.com/freeplane/freeplane/commit/d2c458160eb4a8a1bdb2004903315b5d7c20c444) |
| 2018-07-11 | `api_change` | loader api | `Controller.java`, `HeadlessLoader.java` +5 | [b64c78d5](https://github.com/freeplane/freeplane/commit/b64c78d5c624e8a20c4c42aaac4063d42b7a6cc1) |
| 2018-07-08 | `api_change` | rename API methods newMap -> openMap, newMapFromTemplate -> openUntitledMap, hiddenMap ->  | `EncryptedMap.java`, `XmlImporter.java` +24 | [a76dc05a](https://github.com/freeplane/freeplane/commit/a76dc05a3fe1d4bb41c642401861949053f14b9e) |
| 2018-06-19 | `api_change` | freeplane api package must not depend on any other freeplane packages | `build.gradle`, `Connector.java` +20 | [42e21482](https://github.com/freeplane/freeplane/commit/42e214828ff405b0a71adca6f169d13e290b58dd) |
| 2018-05-13 | `feature` | add all permissions for /usr/lib64/java-atk-wrapper/java-atk-wrapper.jar | `freeplane.policy` | [fe0b3d3c](https://github.com/freeplane/freeplane/commit/fe0b3d3c7f05668d40ca1433346f5bec92e26743) |

### Dettagli commit con note

**[21e56ffe](https://github.com/freeplane/freeplane/commit/21e56ffe24d235b0d2a3cf9cf518b1fe30f60201)** (2018-11-01) — Revert "Add property -Dorg.knopflerfish.osgi.registerserviceurlhandler=false to run under tomcat"

> This reverts commit 68959b7555098ac77891e1899cd2d3a71a03ae70.


---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-09 | `feature` | fix OpenJDK detection, enable some font rendering workaround with OpenJDK | `freeplane.sh` | [01417594](https://github.com/freeplane/freeplane/commit/014175941f8cf5019559bc80c3ce59d9374d9863) |
| 2017-08-22 | `fix` | correct build directory in installer configuration and launchers | `freeplane knopflerfish mac.launch`, `freeplane knopflerfish.launch` +1 | [8378a30a](https://github.com/freeplane/freeplane/commit/8378a30a055086b551599d3c1e0089ed9bcae7c9) |
| 2017-04-08 | `feature` | Add read file permissions | `freeplane.policy`, `freeplane.policy` | [442b0a49](https://github.com/freeplane/freeplane/commit/442b0a49265d7008b0bff25c4dfabd073186d066) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-19 | `fix` | Bug fix workaround for Knopflerfish bug | `ActivatorImpl.java`, `Launcher.java` | [c54e57da](https://github.com/freeplane/freeplane/commit/c54e57dadccffe0168f73feb5c6f58c4c45a8f95) |
| 2016-11-16 | `fix` | Bug fix #2430 also in Launcher in case script plug-in is not installed | `Launcher.java` | [3e355b79](https://github.com/freeplane/freeplane/commit/3e355b7911b83d9c93b2354b312f3a337fedefc4) |
| 2016-11-13 | `fix` | grant all permissions to shared java extension libs: fix syntax error | `freeplane.sh` | [7bfc9048](https://github.com/freeplane/freeplane/commit/7bfc904897996addfbb7070c093384e046dcbdd2) |
| 2016-09-18 | `fix` | Revert "Fix for debugging Freeplane in intelliJ" | `Launcher.java` | [538320d0](https://github.com/freeplane/freeplane/commit/538320d0a7a9914d7e310cc68ecc6bb9bae4a36a) |
| 2016-09-17 | `fix` | Fix for debugging Freeplane in intelliJ | `Launcher.java` | [9f3db8fb](https://github.com/freeplane/freeplane/commit/9f3db8fb0e02dc1c77fd0c042d7b3539d1ab640b) |
| 2016-06-26 | `fix` | Fix eclipse launchers for eclipse 4.6 neon | `freeplane-osgi-mac.launch`, `freeplane-osgi.launch` | [f85b4775](https://github.com/freeplane/freeplane/commit/f85b47752ac9c0cfccc709820d60b252fcb2fef1) |
| 2016-06-25 | `fix` | Fix translation and iss file encoding | `build.gradle`, `build.gradle` +1 | [222a0df7](https://github.com/freeplane/freeplane/commit/222a0df7df56b194768405f64714116fd000e9f2) |
| 2016-05-22 | `fix` | GNOME3 app name fix: run only on X11 | `Launcher.java` | [7f591566](https://github.com/freeplane/freeplane/commit/7f5915669a13a953b41b515500401c6a0b07775e) |
| 2016-05-21 | `fix` | Fix Task bar name for GNOME3 | `Launcher.java` | [1d49d962](https://github.com/freeplane/freeplane/commit/1d49d962b0a77074b580d259010df18dae908e40) |
| 2016-04-10 | `fix` | Fix typo | `Freeplane_without_Java.iss` | [eda678a6](https://github.com/freeplane/freeplane/commit/eda678a62e366f13582144c0917183a55f347980) |
| 2016-04-10 | `fix` | Fix fwdir location | `Launcher.java` | [dbcfe3c2](https://github.com/freeplane/freeplane/commit/dbcfe3c20e7c3f428c39891d386b60d348ef9025) |
| 2016-04-10 | `fix` | Fix windows installer script | `Freeplane_without_Java.iss` | [1b74000b](https://github.com/freeplane/freeplane/commit/1b74000ba1996319d935449cf60d5fcd82eb5a88) |
| 2016-04-10 | `fix` | Fix some bugs related to security checks | `build.gradle`, `ReportGenerator.java` +2 | [0ee6aef1](https://github.com/freeplane/freeplane/commit/0ee6aef160140dd19c6c2e71588de8a221751604) |
| 2016-04-04 | `fix` | Fix Launcher | `Launcher.java` | [cc8bbe94](https://github.com/freeplane/freeplane/commit/cc8bbe94707ce627373d60817293afed9766b622) |
| 2016-02-01 | `fix` | Refactor dependency handling in gradle, small fix | `build.gradle` | [e844ef6d](https://github.com/freeplane/freeplane/commit/e844ef6db92bcde3d27f1b29f7d651e93ce9dccf) |

### Dettagli commit con note

**[c54e57da](https://github.com/freeplane/freeplane/commit/c54e57dadccffe0168f73feb5c6f58c4c45a8f95)** (2016-11-19) — Bug fix workaround for Knopflerfish bug

> "Knopflerfish fails to start if arbitraty working directory contains
> files with special names"
> https://github.com/knopflerfish/knopflerfish.org/issues/11

**[538320d0](https://github.com/freeplane/freeplane/commit/538320d0a7a9914d7e310cc68ecc6bb9bae4a36a)** (2016-09-18) — Revert "Fix for debugging Freeplane in intelliJ"

> This reverts commit 9f3db8fb0e02dc1c77fd0c042d7b3539d1ab640b.


---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-23 | `fix` | Fix installer file encoding | `Freeplane_without_Java.iss` | [74a174fd](https://github.com/freeplane/freeplane/commit/74a174fda98e4dc7c1d000121c864c42873aaa39) |
| 2015-12-04 | `fix` | Fix exe file names produced by build | `dist.gradle`, `Freeplane_without_Java.iss` +1 | [e646e9b0](https://github.com/freeplane/freeplane/commit/e646e9b0ed76a68f11deb8810757e8cb5fad1a7d) |
| 2015-11-28 | `fix` | Fix git revision information | `git.gradle`, `build.xml` +1 | [44e35149](https://github.com/freeplane/freeplane/commit/44e351491102142447dc4d6c2a8b5e70b1d383a5) |
| 2015-11-28 | `fix` | Fix git revision information | `build.xml`, `ReportGenerator.java` | [820e67e6](https://github.com/freeplane/freeplane/commit/820e67e6b7fadcdbefbe12fa86bf77f43a530102) |
| 2015-03-29 | `fix` | freeplane.sh: fix mind map paths with spaces | `freeplane.sh` | [762a0710](https://github.com/freeplane/freeplane/commit/762a0710eef7b7fe4fb7fc0b7584cdc01ba92da9) |
| 2015-03-29 | `fix` | Fix freeplane.bat : forward command line arguments to the launcher | `freeplane.bat` | [7371bed6](https://github.com/freeplane/freeplane/commit/7371bed65cd00563ba7ca568c6424c50a52afc3c) |
| 2015-03-20 | `feature` | create setup.exe in DIST | `Freeplane_without_Java.iss` | [33ae76be](https://github.com/freeplane/freeplane/commit/33ae76be9aae04c116d38395ad3c591466d4c680) |
| 2015-02-25 | `fix` | fix freeplane.bat to work with the latest knopflerfish | `freeplane.bat` | [fd85dcde](https://github.com/freeplane/freeplane/commit/fd85dcde89139997ee379d872ac811182e54c23d) |
| 2015-02-16 | `feature` | fix installer script to use the new build directory | `Freeplane_without_Java.iss` | [ce4c45e9](https://github.com/freeplane/freeplane/commit/ce4c45e9d257344f0de849c3fd6c746c17af77c2) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-01 | `fix` | fix freeplanelauncher.jar (without version number) | `build.gradle` | [96ec6305](https://github.com/freeplane/freeplane/commit/96ec6305d608ea2cf865dbd55057d9da9efa0c9f) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-23 | `fix` | fix syntax error in freeplane_framework/ant/build.xml | `build.xml` | [b9d45c05](https://github.com/freeplane/freeplane/commit/b9d45c0598eaa2e979708347ad30d15ce6794808) |
| 2014-11-22 | `fix` | fix freeplane.sh | `freeplane.sh` | [d99a4f73](https://github.com/freeplane/freeplane/commit/d99a4f73a679f107c5f03ff12aa2070e967f4845) |
| 2014-04-27 | `feature` | fix build to add minor release information to generated exe files | `build.xml`, `Freeplane_without_Java.iss` | [a998f4f9](https://github.com/freeplane/freeplane/commit/a998f4f92517bdc6621272bf42e587d1dbfe9a40) |
| 2014-04-13 | `feature` | add line to freeplane.l4j.ini which is to be enabled to turn off splash | `freeplane.l4j.ini` | [0870b8b6](https://github.com/freeplane/freeplane/commit/0870b8b67708b30d2f325c3e53e962920b00afc0) |
| 2014-04-13 | `feature` | freeplane.sh: add a line which is to be commented out to turn off splash | `freeplane.sh` | [544a6963](https://github.com/freeplane/freeplane/commit/544a69639cedb31dd8c4422a9545f78f0ef9fe67) |

---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-11-16 | `fix` | fix param<i>, i>=5 in freeplane.bat | `freeplane.bat` | [03f5e8c6](https://github.com/freeplane/freeplane/commit/03f5e8c6b44493f2d980f0e86c467cfd449476b3) |
| 2013-09-17 | `feature` | add "pre" to preview distribution names | `build.xml` | [baa773a1](https://github.com/freeplane/freeplane/commit/baa773a19815116a65afb8e285b4ac0fe95837f0) |
| 2013-09-17 | `feature` | add release status to dist file names | `build.xml` | [ffa82cae](https://github.com/freeplane/freeplane/commit/ffa82cae5a115787f77e688e9a0b701d8c303ac1) |
| 2013-08-11 | `fix` | fix quoting in freeplane.sh | `freeplane.sh` | [91037f07](https://github.com/freeplane/freeplane/commit/91037f07075c04a6e67b87cf59da5de450b340e4) |
| 2013-08-03 | `feature` | Add prefs option for common/global LaTeX macros | `Resources_de.properties`, `OptionPanelBuilder.java` +9 | [59bad5cd](https://github.com/freeplane/freeplane/commit/59bad5cd722f50340e02287e949c281fb554b472) |
| 2013-06-11 | `fix` | Fix: Fix entries in auto.properties only once (when moving the dir). | `freeplane.sh` | [f0e1d484](https://github.com/freeplane/freeplane/commit/f0e1d484c0ad8528b5df4a710cfd2e06c941e53c) |
| 2013-06-11 | `feature` | Fix: Some entries in auto.properties still point to old config dir. | `freeplane.sh` | [0e8089fd](https://github.com/freeplane/freeplane/commit/0e8089fd1a62fe45e992372ecb989879eda4e7d4) |
| 2013-06-09 | `feature` | Add support for $XDG_CONFIG_HOME (incl. moving config to new place). | `freeplane.sh` | [2a191af8](https://github.com/freeplane/freeplane/commit/2a191af8dc9189238362bbe3521983243befeb12) |
| 2013-03-16 | `feature` | add minor version to all dist file names | `build.xml` | [b6280eb0](https://github.com/freeplane/freeplane/commit/b6280eb0272ab59421e958102bf15322301f123f) |
| 2013-02-22 | `feature` | new app icons | `Freeplane_frame_icon.png`, `ApplicationViewController.java` +2 | [42ca2bea](https://github.com/freeplane/freeplane/commit/42ca2bea70bb0e2d225cafecad79ab917fbc0704) |
| 2013-02-21 | `feature` | restore new icon for compiled freeplane.exe | `freeplane.exe` | [8dcd2075](https://github.com/freeplane/freeplane/commit/8dcd20751dbc91e41b65183c3f2b943c7e8c9b2d) |
| 2013-01-13 | `feature` | manually merged trunk version of freeplane.sh to enable overwriting the userdir | `freeplane.sh` | [4f98f5cc](https://github.com/freeplane/freeplane/commit/4f98f5cc3f1503025094313c4006f697a0db25a0) |
| 2013-01-01 | `feature` | new launcher binaries | `freeplane.exe`, `freeplaneConsole.exe` | [da5c606c](https://github.com/freeplane/freeplane/commit/da5c606c753a424b6664a8fc5db3c178a61c7e66) |

### Dettagli commit con note

**[0e8089fd](https://github.com/freeplane/freeplane/commit/0e8089fd1a62fe45e992372ecb989879eda4e7d4)** (2013-06-11) — Fix: Some entries in auto.properties still point to old config dir.

> But they should point to the new config-dir in $XDG_CONFIG_HOME.

**[2a191af8](https://github.com/freeplane/freeplane/commit/2a191af8dc9189238362bbe3521983243befeb12)** (2013-06-09) — Add support for $XDG_CONFIG_HOME (incl. moving config to new place).

> To keep the implementation simple, this is done in the Unix start-script.


---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-11-17 | `feature` | new icons | `Freeplane_app.ico`, `Freeplane_doc.ico` +4 | [fdad9c13](https://github.com/freeplane/freeplane/commit/fdad9c131bf7017f873ed60ca7050f356cde5277) |
| 2012-09-02 | `feature` | declare support for retina displays | `mac_info_plist.xslt` | [91fbe61a](https://github.com/freeplane/freeplane/commit/91fbe61a403817a9c8327565830bd0995739fc1e) |
| 2012-08-29 | `feature` | Create installer for portableApps test version (use their splash screen) | `build.xml`, `Splash.png` | [63456fbc](https://github.com/freeplane/freeplane/commit/63456fbcb5f7b597eba6113076f594609d655d7d) |
| 2012-08-12 | `fix` | bug fix version 1.2.19 beta | `version.properties`, `Freeplane_without_Java.iss` +1 | [db5ba40c](https://github.com/freeplane/freeplane/commit/db5ba40c6f06738b699277dcb42dfa47346b44b3) |
| 2012-02-26 | `feature` | Add license and fix copyright message in about box and windows installer | `Resources_ar.properties`, `Resources_ca.properties` +40 | [d50ffbf3](https://github.com/freeplane/freeplane/commit/d50ffbf3e583018681a20a5aeeec628b70962f0e) |
| 2012-01-22 | `fix` | fix launcher for windows 7 64bit | `freeplane.dev`, `freeplane.exe` +4 | [b29f4594](https://github.com/freeplane/freeplane/commit/b29f4594840ff32f3cfe10bfbef55e06555efe06) |
| 2012-01-12 | `feature` | Added the following command line arguments:  -X<menukey>: execute menu item with key <menu | `history_en.txt`, `MenuUtils.java` +9 | [347dc196](https://github.com/freeplane/freeplane/commit/347dc196f65a70af6b16f5db6dfe7b32b16ed50a) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-11-08 | `feature` | Create rename api.zip in dirstibution to script-api.zip. Create it only for dist but nore  | `build.xml`, `build.xml` | [57864d64](https://github.com/freeplane/freeplane/commit/57864d64addef5ae5719feb0b8f8d0cc6694ef05) |
| 2011-09-25 | `fix` | Transmit bzr revision info in bug reports | `build.xml`, `Activator.java` +1 | [43639fb5](https://github.com/freeplane/freeplane/commit/43639fb53e9fda31011e678eb3f9f8e3860c9e6c) |
| 2011-08-20 | `fix` | fix batch file freeplanePortable.bat | `freeplanePortable.bat` | [f4e27a0e](https://github.com/freeplane/freeplane/commit/f4e27a0e108aa808a5cabecaca7bd2625ad98ef9) |
| 2011-07-05 | `feature` | new icons | `freeplane_app_128x128.png`, `freeplane.icns` +7 | [052a2501](https://github.com/freeplane/freeplane/commit/052a25011011763a937169889e369c072a7e98b9) |
| 2011-06-13 | `feature` | add devresources to src dist | `build.xml` | [e20aad15](https://github.com/freeplane/freeplane/commit/e20aad15b2de7a93f84806321bfc6d9b7797a385) |
| 2011-06-11 | `feature` | new artwork | `Freeplane_frame_icon.png`, `Freeplane_frame_icon_32x32.png` +16 | [198bd07a](https://github.com/freeplane/freeplane/commit/198bd07a7019abf015879433f10cee8ce1457142) |
| 2011-03-29 | `api_change` | package and distribute scripting api.zip | `build.xml`, `build.xml` | [79be0970](https://github.com/freeplane/freeplane/commit/79be09706508252bd475327452e14d9511834f73) |
| 2011-01-14 | `api_change` | added API generation to the distribution | `build.xml`, `build.xml` | [b946317c](https://github.com/freeplane/freeplane/commit/b946317c567a48bf8c54074558ec24a8780fc84b) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-07-30 | `feature` | take application data location from environment variable for windows os + use new user fol | `ApplicationResourceController.java`, `FreeplaneStarter.java` +7 | [c2918488](https://github.com/freeplane/freeplane/commit/c291848869ff446ce6e282a0227c3357ad5e6b05) |
| 2010-07-11 | `feature` | let jortho and freeplaneant be compiled from freeplane/ant/build.xml add freeplane/.extern | `.bzrignore`, `build.xml` +6 | [257c5f19](https://github.com/freeplane/freeplane/commit/257c5f19d1a5bbdf6bf1586d40a6d7e9abd1ad7e) |
| 2010-06-06 | `fix` | fix CreatePlugin | `build.xml`, `freeplaneant.jar` | [d6573be9](https://github.com/freeplane/freeplane/commit/d6573be91e96f9e085197a66304773d773b17fe4) |
| 2010-06-05 | `feature` | - updated to freeplaneant.jar boercher-20100605001746-sic2r1wu9cv28x28 (2010-06-05 02:17:4 | `build.xml`, `freeplaneant.jar` | [b8476950](https://github.com/freeplane/freeplane/commit/b84769501dc9ec2b0bc28f9314ee79d815376d29) |
| 2010-05-13 | `feature` | after update to the new freeplane_ant wrong eol style is detected by check-translation. So | `build.xml`, `build.xml` | [6805506b](https://github.com/freeplane/freeplane/commit/6805506ba7850e0c1a62f96e43d8690ec9cdde52) |
| 2010-05-02 | `api_change` | remove dependencies from google-translate-api | `build.xml`, `Resources_ar.properties` +33 | [9a799adb](https://github.com/freeplane/freeplane/commit/9a799adb94852d6ced8c94b1f4f9c02f5e92d8f4) |
| 2010-04-29 | `feature` | format-translation: make writeIfUnchanged default create target format-translation-no-forc | `build.xml`, `build.xml` | [7e763975](https://github.com/freeplane/freeplane/commit/7e7639759be10e7c9e8839ecac51f9ff856d2340) |
| 2010-04-12 | `feature` | added new target format-translation-force, necessary if only the eol style has to be fixed | `build.xml`, `build.xml` | [ab0bfcef](https://github.com/freeplane/freeplane/commit/ab0bfcef2d43923272efc16d1d4828aadc327523) |
| 2010-04-11 | `feature` | update freeplane_ant to revision boercher-20100411021753-zn3fz8hkojpmlxim (2010-04-11 04:1 | `build.xml`, `build.xml` +2 | [cd637e0e](https://github.com/freeplane/freeplane/commit/cd637e0e3e2489f860cb731026a221ea8af2cf7b) |
| 2010-03-24 | `feature` | - added new targets check-translation and format-translation to   freeplane_framework/ant  | `build.xml`, `build.xml` +1 | [6978f913](https://github.com/freeplane/freeplane/commit/6978f9133bde9091422397e18c248c9151eaf928) |
| 2010-03-03 | `feature` | add bzr info to distributions | `build.xml` | [841b05a3](https://github.com/freeplane/freeplane/commit/841b05a35b4d63114a636a695e511fe1dc9ee232) |
| 2010-03-03 | `fix` | fix build target dmg4mac | `build.xml` | [0d5c0cce](https://github.com/freeplane/freeplane/commit/0d5c0cce31441d2058f6a6110d841b703e49b22f) |
| 2010-02-26 | `fix` | fix batch files | `freeplane.bat`, `freeplanePortable.bat` +1 | [c3b8d595](https://github.com/freeplane/freeplane/commit/c3b8d595d60e4f2fa3c5ea337182ee74314fcbc3) |
| 2010-02-16 | `feature` | Add freeplanedoc.icns to mac-jarbundler | `freeplanedoc.icns` | [a0330195](https://github.com/freeplane/freeplane/commit/a0330195c09459cd4cbe5b530c674bf2f614d3be) |
| 2010-02-13 | `feature` | simplify freeplane_framework/ant/build.xml, new target makePlugin | `build.xml` | [b47d3d6f](https://github.com/freeplane/freeplane/commit/b47d3d6f3fe565dd77f494fadc9dc2c8199f4a89) |
| 2010-02-13 | `feature` | 430]: Freeplane Mac applications doesn't start: add file permissions Simplify freeplane_fr | `build.xml` | [eaea0067](https://github.com/freeplane/freeplane/commit/eaea0067cf0257340060ce60a1ea0001caecb702) |
| 2010-02-11 | `feature` | create dmg | `build.xml` | [ff2fd424](https://github.com/freeplane/freeplane/commit/ff2fd42443457ba3eeb24c30ecf66e612fa7dafa) |
| 2010-02-09 | `feature` | Implement Mac file associations | `build.xml` | [57bcd52e](https://github.com/freeplane/freeplane/commit/57bcd52eeed61f326e27ccef877cb65dc25eaa1f) |
| 2010-02-05 | `feature` | Add new subdirectory freeplane_framework/mac-jarbundler | `bazaarBranchCreation.txt`, `build.xml` +3 | [a94035d2](https://github.com/freeplane/freeplane/commit/a94035d2e89d493c08b97ad037521b7c1d6cf368) |
| 2010-01-31 | `feature` | Freeplane.c update portable app to the new version | `Freeplane.c`, `freeplane.exe` +3 | [87aeb002](https://github.com/freeplane/freeplane/commit/87aeb002c24b5bae971e95c7ef8e095dfa696b72) |
| 2010-01-30 | `feature` | Add OK and Cancel buttons to Latex Editor | `Resources_ar.properties`, `Resources_ca.properties` +29 | [5610d61c](https://github.com/freeplane/freeplane/commit/5610d61c3fc7f734efb92a475559d887760a829e) |
| 2010-01-14 | `api_change` | set status back to beta because of the expected changes in script user api | `version.properties`, `Freeplane_without_Java.iss` +1 | [a7a2afeb](https://github.com/freeplane/freeplane/commit/a7a2afeb4ec77055c918698787a81407c7f9a737) |

### Dettagli commit con note

**[6978f913](https://github.com/freeplane/freeplane/commit/6978f9133bde9091422397e18c248c9151eaf928)** (2010-03-24) — - added new targets check-translation and format-translation to   freeplane_framework/ant and freeplane/ant

> - make target build fail unless the Resource files are formatted
> 
> - added current freeplaneant.jar from project misc/freeplane_ant
>   (revision-id: boercher-20100324014058-0rh66dsrkqbqv7en)


---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-12-15 | `fix` | build patch from ewl: separate properties | `ant.properties`, `build.xml` +12 | [db2ac954](https://github.com/freeplane/freeplane/commit/db2ac9547e843ffe9123d133e7e6cb30292727f9) |
| 2009-12-13 | `fix` | freeplane.sh patch for MAC OS | `freeplane.sh` | [e5fd8742](https://github.com/freeplane/freeplane/commit/e5fd87424c82b724cf833038971761a2dc96dada) |
| 2009-11-16 | `feature` | new art | `Freeplane_application_icon_blue.png`, `Freeplane_frame_icon.png` +19 | [808081fb](https://github.com/freeplane/freeplane/commit/808081fbf8a750afcc7cfb31b8754a204fbc1f8b) |
| 2009-11-01 | `feature` | patch 295 Create source file pure i.e. without any compiled part like libraries | `build.xml` | [e1224b1a](https://github.com/freeplane/freeplane/commit/e1224b1ab86151c50ac7cbd2f857623b7bc3c6de) |
| 2009-10-25 | `feature` | add jortho to source distribution | `build.xml` | [b464f0f1](https://github.com/freeplane/freeplane/commit/b464f0f13d22543059068b7a360a7e23037aad3a) |
| 2009-08-11 | `fix` | installer bug fixes | `Freeplane_without_Java.iss` | [126a90cc](https://github.com/freeplane/freeplane/commit/126a90cc6b110525b4d64d31e192e637a8d0bd65) |
| 2009-07-07 | `fix` | fix in batch file | `freeplane.bat` | [155f794c](https://github.com/freeplane/freeplane/commit/155f794c46fd3a671bd3feb50d64c08614c26bc0) |
| 2009-07-06 | `fix` | fix in batch file | `freeplane.bat` | [d38b4ef1](https://github.com/freeplane/freeplane/commit/d38b4ef150f4042ecc969cf09a3079b8c8b2b849) |
| 2009-06-19 | `fix` | fix from ewl | `freeplane.sh` | [2a62562d](https://github.com/freeplane/freeplane/commit/2a62562db01ad3232af733343b84cd7e027738ed) |
| 2009-05-05 | `fix` | bug fix: drag and drop oh html links from firefox bug fix: encrypted nodes bug fix: Java e | `preferences.xml`, `ShowFilterToolbarAction.java` +11 | [5556c20e](https://github.com/freeplane/freeplane/commit/5556c20eae1dededc74091921415519334bb6eaa) |
| 2009-04-19 | `fix` | Bug fix [Bugs 0000037]: Filter toolbar does not turn off via toolbar icon | `FreeplaneVersion.java`, `ShowFilterToolbarAction.java` +1 | [f6b3c028](https://github.com/freeplane/freeplane/commit/f6b3c0282ac8e31ae19875d5e995ab56f8b9a154) |
| 2009-03-01 | `fix` | Bug fix 0000008: using CTRL + arrow key left moves node to next parent freeplane.sh improv | `MMapController.java`, `NodeUpAction.java` +7 | [4888373c](https://github.com/freeplane/freeplane/commit/4888373c7c5f2312378b9e14726befa649964342) |
| 2009-02-26 | `feature` | Bug fix: scrolling for icon tool bar New icons for windows and linux | `ViewController.java`, `JAutoScrollBarPane.java` +5 | [38a87988](https://github.com/freeplane/freeplane/commit/38a879887a706a387fc1bf7640fd123a9e39cb3c) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
