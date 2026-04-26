# Add-ons — Commit rilevanti

**Modulo:** `addons`  
**Commit rilevanti (feature / fix / api_change):** 77 su 157 totali

> **Add-on di terze parti** distribuiti tramite il repository ufficiale. Pacchetti installabili dall'utente che estendono Freeplane senza modificare il core.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2025](#2025) — 2 commit
- [2021](#2021) — 1 commit
- [2020](#2020) — 6 commit
- [2019](#2019) — 2 commit
- [2018](#2018) — 2 commit
- [2016](#2016) — 10 commit
- [2015](#2015) — 2 commit
- [2014](#2014) — 5 commit
- [2013](#2013) — 10 commit
- [2012](#2012) — 3 commit
- [2011](#2011) — 34 commit

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-08-03 | `feature` | Fix UI component references for UI-follows-focus architecture | `GrabKeyDialog.java`, `ShowPreferencesAction.java` +45 | [44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts | `OptionPanel.java`, `PathProperty.java` +29 | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |

### Dettagli commit con note

**[44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf)** (2025-08-03) — Fix UI component references for UI-follows-focus architecture

> Replace getMenuComponent() with getCurrentRootComponent() throughout codebase
> to support UI components moving between frames. Key changes:
> 
> - Remove getMenuComponent() method from ViewController implementations
> - Consolidate UITools to use getCurrentRootComponent() consistently
> - Update all dialog parent references to use current frame
> - Simplify full screen handling to auto-detect current frame
> - Fix frame references in AccelerateableAction, dialogs, and utilities
> 
> This ensures all UI operations work correctly when menus and components
> move between frames based on focus, resolving assumptions that UI
> components are fixed to the main frame.
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

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-01-07 | `feature` | introduce interface INodeDuplicator and add operation duplicate on nodes | `XmlImporter.java`, `INodeDuplicator.java` +14 | [63fca871](https://github.com/freeplane/freeplane/commit/63fca871c8305e7418d15443033fced1f40dc2c8) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-10-24 | `feature` | #2837 Add-on's jar file removed when upgrading | `AddOnsController.java` | [3a0e0f2f](https://github.com/freeplane/freeplane/commit/3a0e0f2fe14d29eae423c61745cc705e64c0918a) |
| 2020-07-04 | `feature` | #2796 Add-on deinstallation fails to delete jar | `AddOnsController.java` | [de3c82e8](https://github.com/freeplane/freeplane/commit/de3c82e86d75d5c545a1fdf3e5ebf5d88fdfcf3d) |
| 2020-06-05 | `fix` | Fix slow JFileChooser for windows by not using Windows icons | `OptionPanel.java`, `PathProperty.java` +18 | [80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be) |
| 2020-03-06 | `fix` | fix dialog icon | `ManageAddOnsDialog.java` | [df67c1fb](https://github.com/freeplane/freeplane/commit/df67c1fb597b504cee6dd68db29461c7809c8ced) |
| 2020-02-11 | `feature` | rename methods, add method HtmlUtils.textToHTML | `HtmlUtils.java`, `AboutAction.java` +13 | [adcdd4ac](https://github.com/freeplane/freeplane/commit/adcdd4ac97e67df07fc788e4882efbd43fe7f9fc) |
| 2020-01-27 | `fix` | #2726 fix manage addons dialog icon | `ManageAddOnsDialog.java` | [66543b82](https://github.com/freeplane/freeplane/commit/66543b824c040b2c3e20b5ad6e9d12e2b9c0a5cd) |

### Dettagli commit con note

**[80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be)** (2020-06-05) — Fix slow JFileChooser for windows by not using Windows icons

> https://stackoverflow.com/a/59165208/1833472


---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-09-28 | `fix` | Fix table row heights after font scaling | `UITools.java`, `AttributeRegistryTable.java` +4 | [15384981](https://github.com/freeplane/freeplane/commit/15384981d8172c23ee2004eb05d286ba07802dde) |
| 2019-02-15 | `fix` | fix NPE | `AddOnsController.java` | [c45e067c](https://github.com/freeplane/freeplane/commit/c45e067c39210331320e852ddd628dbd4d84903b) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-31 | `feature` | Fix #2386 Special characters in add-on translations wrongly displayed | `TextUtils.java`, `AddOnProperties.java` | [d3fa8d97](https://github.com/freeplane/freeplane/commit/d3fa8d97c65f75ca8c09e548622989a09ee52730) |
| 2018-12-19 | `feature` | Fix for #2386 Special characters in add-on translations wrongly displayed | `AddOnProperties.java` | [c9b7a8a2](https://github.com/freeplane/freeplane/commit/c9b7a8a2b4899e3a2d79bcf71a9bf12c4a1cbdb5) |

### Dettagli commit con note

**[d3fa8d97](https://github.com/freeplane/freeplane/commit/d3fa8d97c65f75ca8c09e548622989a09ee52730)** (2018-12-31) — Fix #2386 Special characters in add-on translations wrongly displayed

> Added method escapeUtf8 to org.freeplane.core.util.TextUtils. Method
> escapeUtf8 is a stripped down version StringEscapeUtils.escapeJava. It
> only escapes UTF-8 non-ASCII characters. It escapes them to \uXXXX where
> XXXX is the hex code of the escaped character. It solves this bug
> because it does not escape backslashes and double quotes.
> 
> Replaced method "StringEscapeUtils.escapeJava" with
> "TextUtils.escapeUtf8" on line 456 of
> org.freeplane.main.addons.AddOnProperties.
> 
> As part of the fix of this bug the add-on devtools is also changed to
> use TextUtils.escapeUtf8.

**[c9b7a8a2](https://github.com/freeplane/freeplane/commit/c9b7a8a2b4899e3a2d79bcf71a9bf12c4a1cbdb5)** (2018-12-19) — Fix for #2386 Special characters in add-on translations wrongly displayed

> Removed method "StringEscapeUtils.escapeJava" from line 456 of
> AddOnProperties.java. This method is already applied by devtools,
> aplying it twice leads to double backslashes for every escaped UTF-8,
> non-ascii characters: \\uXXXX.


---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-12-29 | `feature` | add tools svgs | `ExecuteScriptForAllNodes.svg`, `ExecuteScriptForSelectionAction.svg` +15 | [0a27a7fd](https://github.com/freeplane/freeplane/commit/0a27a7fd6ae92ebef92adae77b0e37a508f33949) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [2e38286e](https://github.com/freeplane/freeplane/commit/2e38286e3b35f58e558c329073a1eba35640d9c7) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [096fbd1f](https://github.com/freeplane/freeplane/commit/096fbd1f116b38edc7648618cf2c5e45bcd7b536) |
| 2016-08-18 | `feature` | fix missing parseFreeplaneVersion() | `installScriptAddOn.groovy` | [b89c27a9](https://github.com/freeplane/freeplane/commit/b89c27a9739565de6a256623afc6c2493aa4521d) |
| 2016-04-25 | `feature` | avoid all translation warnings for add-ons | `AddOnsController.java` | [6a3f1dd0](https://github.com/freeplane/freeplane/commit/6a3f1dd09b19dcbd1a69bcb21ccfead70e276e0f) |
| 2016-04-24 | `feature` | revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations) | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943) |
| 2016-04-24 | `feature` | avoid all translation warnings for add-ons | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c) |
| 2016-04-09 | `fix` | fix ambiguity with operators in groovy (thanks to Gergely Papp) | `installScriptAddOn.groovy` | [1762d5b8](https://github.com/freeplane/freeplane/commit/1762d5b8a90cf900ed954d4444087e50efa06c07) |
| 2016-03-19 | `feature` | #2214 Adding updateUrl to add-on leads to installation error fix NPE | `AddOnProperties.java` | [cf444355](https://github.com/freeplane/freeplane/commit/cf444355726206deb29fac26d3afdddcaef03de2) |
| 2016-03-18 | `feature` | #2214 Adding updateUrl to add-on leads to installation error convert updateUrl from URI va | `AddOnProperties.java` | [93bd9880](https://github.com/freeplane/freeplane/commit/93bd9880cb186d343563421b6eb69315bbb8d205) |

### Dettagli commit con note

**[b89c27a9](https://github.com/freeplane/freeplane/commit/b89c27a9739565de6a256623afc6c2493aa4521d)** (2016-08-18) — fix missing parseFreeplaneVersion()

> for allowing the install of add-ons in 1.5.15+.  Discussed in https://sourceforge.net/p/freeplane/discussion/758437/thread/12897ed2/

**[6a3f1dd0](https://github.com/freeplane/freeplane/commit/6a3f1dd09b19dcbd1a69bcb21ccfead70e276e0f)** (2016-04-25) — avoid all translation warnings for add-ons

> Translations of add-ons are often missing. To make them look nicer
> in the GUI we'll cut all warnings about missing keys for add-ons
> and erase the [translate me] suffix

**[7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943)** (2016-04-24) — revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations)

> will use a different approach

**[ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c)** (2016-04-24) — avoid all translation warnings for add-ons

> Translations of add-ons are often missing. To make them look nicer
> in the GUI we'll cut all warnings about missing keys for add-ons
> and erase the [translate me] suffix


---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-23 | `feature` | Display add-on menu item locations | `build.gradle`, `EntryAccessor.java` +4 | [1abc7f18](https://github.com/freeplane/freeplane/commit/1abc7f18f501de5541aa2cb904d7429fbe68ea17) |
| 2015-12-23 | `feature` | Build formatted menu location for add-on details | `EntryAccessor.java`, `EntryAccessorTest.java` +1 | [a4f21706](https://github.com/freeplane/freeplane/commit/a4f217063d067d2c3afeb6cc0146beb748616444) |

---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-09-08 | `fix` | fix bug #2186: use fixed locale for toUpperCase to cope with the http://mattryall.net/blog | `ScriptAddOnProperties.java` | [0441e4fc](https://github.com/freeplane/freeplane/commit/0441e4fcf17bcc5a91c4964ae990b65307b61895) |
| 2014-09-08 | `fix` | fix bug #2186: use fixed locale for toUpperCase to cope with the http://mattryall.net/blog | `ScriptAddOnProperties.java` | [6a216022](https://github.com/freeplane/freeplane/commit/6a21602245d33c29f95ce41a43289bf75122eb3d) |
| 2014-04-12 | `feature` | Moved freeplane files to the new structure | `AsyncScalr.java`, `Scalr.java` +924 | [cbde615a](https://github.com/freeplane/freeplane/commit/cbde615a1b35e12ab19be1ed77c5c1d151db6e59) |
| 2014-03-16 | `feature` | avoid ConcurrentModificationExceptions on add-on update check | `AddOnsController.java` | [40bb8a47](https://github.com/freeplane/freeplane/commit/40bb8a478d49e592919ef7ff6a5b9a63711404e0) |
| 2014-03-16 | `feature` | avoid ConcurrentModificationExceptions on add-on update check | `AddOnsController.java` | [eece7ca2](https://github.com/freeplane/freeplane/commit/eece7ca245d5c9671ff30b1ede28f2381ea27628) |

---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [62e125b3](https://github.com/freeplane/freeplane/commit/62e125b331c29ae0c3962a3b0d27e0342bcc18ee) |
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [2c986d3a](https://github.com/freeplane/freeplane/commit/2c986d3abd50356b5bf63f28fb97347deb0cf4e3) |
| 2013-09-09 | `feature` | - make version.properties the default add-on version file - refactorings | `FreeplaneVersion.java`, `AddOnProperties.java` +3 | [6325b562](https://github.com/freeplane/freeplane/commit/6325b56206f90704695f01a27e362b21d8edb5e3) |
| 2013-08-13 | `feature` | support for new properties : downloadUrl and changelogUrl | `AddOnProperties.java`, `HttpVersionClient.java` +1 | [21d6b2d6](https://github.com/freeplane/freeplane/commit/21d6b2d669c6a40a8a00ec328a64bbbf191dbbe6) |
| 2013-08-13 | `feature` | handling undefined 'homepage' for add-ons | `AddOnProperties.java`, `UpdateCheckAction.java` +1 | [27d5a422](https://github.com/freeplane/freeplane/commit/27d5a422e3ba53e8ffc01a64762f6f13d571b434) |
| 2013-07-28 | `feature` | Scripting/other languages: * new configuration options:   - script_compilation_disabled_ex | `Resources_de.properties`, `Resources_en.properties` +10 | [2e24f90d](https://github.com/freeplane/freeplane/commit/2e24f90d20f9f3025c4910a675c48fce88cb644f) |
| 2013-07-28 | `feature` | store the last version of an add-on | `AddOnProperties.java` | [ca2858d9](https://github.com/freeplane/freeplane/commit/ca2858d98e86f4f414e91c670eb70a4a76abf7f5) |
| 2013-07-27 | `feature` | added updateUrl property to be abble to check for newer add-ons versions | `AddOnProperties.java` | [794432e1](https://github.com/freeplane/freeplane/commit/794432e16d9c30c7097f700e22148341f3d22221) |
| 2013-02-21 | `feature` | - add top button to add-on installer - move malware warning to top and make red - adjust t | `Resources_de.properties`, `Resources_el.properties` +14 | [c802f03f](https://github.com/freeplane/freeplane/commit/c802f03f2456cc0031d7740e6033c99f6f0d7ca4) |
| 2013-01-13 | `feature` | #1859: allow using \uFFFF escape sequences in add-ons to circumvent all encoding issues | `AddOnsController.java` | [fa73d64d](https://github.com/freeplane/freeplane/commit/fa73d64d71402bd04a10c8d5d16f8e3c938b1b24) |

### Dettagli commit con note

**[62e125b3](https://github.com/freeplane/freeplane/commit/62e125b331c29ae0c3962a3b0d27e0342bcc18ee)** (2013-12-26) — 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane/pull/20):

> - Always add <freeplaneuserdir>/lib and all jars therein to all
>    script's classpath.
> 
>  - Add-ons have a new 'lib' node which may contain jars or class
>    files (not nested).
> 
>  - Lib files are installed with the add-on.
> 
> 2. Additions and changes compared to the initial pull request:
> 
>  - Install add-on scripts to a new "private add-on directory"
>    <freeplaneuserdir>/addons/<addonname>/scripts
> 
>  - Install add-on libs to <freeplaneuserdir>/addons/<addonname>/lib
> 
>  - Omitted other non-related changes, especially the fix for the
>    'deinstall' spelling error
> 
>  - Enhanced the add-on related 'devtools' scripts, especially to
>    support the new add-on lib: Better checks, more automation.
> 
> Possible enhancement: The add-on libs are added to the global
> script classpath, not only to the classpath of the scripts to
> which the libs belong to.

**[2c986d3a](https://github.com/freeplane/freeplane/commit/2c986d3abd50356b5bf63f28fb97347deb0cf4e3)** (2013-12-26) — 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane/pull/20):

> - Always add <freeplaneuserdir>/lib and all jars therein to all
>    script's classpath.
> 
>  - Add-ons have a new 'lib' node which may contain jars or class
>    files (not nested).
> 
>  - Lib files are installed with the add-on.
> 
> 2. Additions and changes compared to the initial pull request:
> 
>  - Install add-on scripts to a new "private add-on directory"
>    <freeplaneuserdir>/addons/<addonname>/scripts
> 
>  - Install add-on libs to <freeplaneuserdir>/addons/<addonname>/lib
> 
>  - Omitted other non-related changes, especially the fix for the
>    'deinstall' spelling error
> 
>  - Enhanced the add-on related 'devtools' scripts, especially to
>    support the new add-on lib: Better checks, more automation.
> 
> Possible enhancement: The add-on libs are added to the global
> script classpath, not only to the classpath of the scripts to
> which the libs belong to.


---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-28 | `feature` | allow Object valued attribute values in add-on maps | `installScriptAddOn.groovy` | [bb45d56d](https://github.com/freeplane/freeplane/commit/bb45d56d44061a29b03852638f65ec53c84159a4) |
| 2012-07-11 | `feature` | #1490: fix keyboard shortcut assignment on add-on installation | `installScriptAddOn.groovy` | [8d3983c6](https://github.com/freeplane/freeplane/commit/8d3983c6afe16b112b86ef2f5be038a9236b5f0d) |
| 2012-01-14 | `feature` | Create a new API for map loading and mark an old API as deprecated | `MANIFEST.MF`, `EncryptedMap.java` +17 | [cbcfb2b7](https://github.com/freeplane/freeplane/commit/cbcfb2b73e3c66041a5ebb58252b659384a70a0e) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-12-30 | `feature` | Rework creation of new maps: refactoring because of bug 1417]: Show node icons heirarchica | `AttributeController.java`, `AttributeRegistry.java` +21 | [d39a5fef](https://github.com/freeplane/freeplane/commit/d39a5fefef1b69a9e5663e7ffc9caca1532ec468) |
| 2011-12-23 | `feature` | #1409: create <userdir>/resources/images folder first before installing images Improve pla | `installScriptAddOn.groovy` | [e6e72bf1](https://github.com/freeplane/freeplane/commit/e6e72bf171f3de51c475dad304f85ffe7dcbf335) |
| 2011-12-15 | `feature` | care for display of keyboard shortcuts in the add-on details | `MenuUtils.java`, `installScriptAddOn.groovy` +1 | [9bcec98d](https://github.com/freeplane/freeplane/commit/9bcec98d71946dd18a29afefe6967df2015f1ad8) |
| 2011-12-14 | `feature` | new icons from Predrag Cuklin | `install_addons.png`, `manage_addons.png` +2 | [ed09f6eb](https://github.com/freeplane/freeplane/commit/ed09f6eb118be38b920a0e53cd5cbb8d66c3d297) |
| 2011-12-14 | `feature` | manage add-ons: make deactivate/deinstall buttons work again | `ManageAddOnsPanel.java` | [b42811c1](https://github.com/freeplane/freeplane/commit/b42811c18c66fe73390db90295fe2ebd4305cd92) |
| 2011-12-09 | `fix` | fix (unused) confirm dialog | `installScriptAddOn.groovy` | [76b88e2b](https://github.com/freeplane/freeplane/commit/76b88e2ba2bc506ad44f0ca379681e36c2ef2207) |
| 2011-12-04 | `feature` | add images to the add-on dialogs | `IconNotFound.java`, `UrlManager.java` +5 | [cb52b0f2](https://github.com/freeplane/freeplane/commit/cb52b0f2bd9c14daf8076783052772e6cd1bdfbb) |
| 2011-11-30 | `feature` | Add-ons dialog: - new 'Themes' tab for add-ons with names ending on 'theme' or 'Theme' - a | `Resources_de.properties`, `Resources_nl.properties` +7 | [8f9fa402](https://github.com/freeplane/freeplane/commit/8f9fa4028740de2e5c86c8cfde265add68764d46) |
| 2011-11-22 | `feature` | add addon buttons from Predrag Cuklin | `addons.png`, `install_addons.png` +3 | [6ef92f90](https://github.com/freeplane/freeplane/commit/6ef92f9016c940529be8b47554b59983b42c3b63) |
| 2011-11-22 | `feature` | add a name to the search button | `Resources_de.properties`, `Resources_en.properties` +1 | [c8b508a1](https://github.com/freeplane/freeplane/commit/c8b508a11142a56bd5610e0b28267d6cd0edd4e3) |
| 2011-11-19 | `feature` | add close button to ManageAddOnsDialog | `Resources_en.properties`, `ManageAddOnsDialog.java` | [12b7834e](https://github.com/freeplane/freeplane/commit/12b7834e114bf9d58a8e941721b7a05a7fe4cd1d) |
| 2011-11-19 | `feature` | Add-ons: Differentiate between a fresh install and an update deinstall the old version bef | `Resources_de.properties`, `AddOnsController.java` +2 | [b6bc609a](https://github.com/freeplane/freeplane/commit/b6bc609a0c48dea0e3669d2cc35a129a71845c26) |
| 2011-11-18 | `fix` | fix Groovy error | `installScriptAddOn.groovy` | [bb368635](https://github.com/freeplane/freeplane/commit/bb36863552b6a464c6e9a59c0e0449b1fbe345a6) |
| 2011-11-17 | `feature` | Display add-on details on installation | `Resources_de.properties`, `UITools.java` +6 | [8e7b87de](https://github.com/freeplane/freeplane/commit/8e7b87dea5bbb4b557ee2043c9255287e530cd0e) |
| 2011-11-08 | `fix` | fix ScriptingRegistration.install | `ScriptingRegistration.java`, `ManageAddOnsAction.java` +1 | [5b2622d8](https://github.com/freeplane/freeplane/commit/5b2622d81529e50ee8a1359521c1320183fe94da) |
| 2011-11-08 | `feature` | add-ons: 'Really install?'... | `Resources_en.properties`, `installScriptAddOn.groovy` | [9a721533](https://github.com/freeplane/freeplane/commit/9a721533f3fb15f3e35f6ecac9587735000520d7) |
| 2011-11-06 | `feature` | tabbed manage/install add-on dialog | `Resources_en.properties`, `AddOnInstallerPanel.java` +2 | [2a29ca74](https://github.com/freeplane/freeplane/commit/2a29ca749711d69e23c3ce0d78725dcd895d5446) |
| 2011-11-01 | `fix` | bug fixes in ManageAddOnsDialog | `ButtonsInCellRenderer.java`, `ManageAddOnsDialog.java` | [6a0b607b](https://github.com/freeplane/freeplane/commit/6a0b607b96a6cdf97c6b70db028cfe84dfbfb1d6) |
| 2011-10-31 | `feature` | on install only create a MapModel from the given URL, don't open it as a view | `ManageAddOnsDialog.java` | [4b36b85e](https://github.com/freeplane/freeplane/commit/4b36b85ecbf4dee0334b0ee3c2165d4374ef0069) |
| 2011-10-31 | `feature` | add new properties author and license and make them optional in the installer | `AddOnProperties.java` | [04d51d49](https://github.com/freeplane/freeplane/commit/04d51d4970e386059af935b5b858807e866eed77) |
| 2011-10-31 | `feature` | add new properties author and license and make them optional in the installer | `AddOnProperties.java`, `Resources_en.properties` +1 | [a1212a08](https://github.com/freeplane/freeplane/commit/a1212a08b7504cc0a0adaff7450ad61d27bf83b9) |
| 2011-10-26 | `feature` | ManageAddOnsDialog: - cope with HTML descriptions - update add-ons table after deinstall o | `AddOnsController.java`, `Resources_en.properties` +1 | [51ab52f2](https://github.com/freeplane/freeplane/commit/51ab52f2ee5c725945068cd2d8a1b1d6fbc20b55) |
| 2011-10-24 | `fix` | #1339: avoid bug reports on installation errors | `installScriptAddOn.groovy` | [7d624e84](https://github.com/freeplane/freeplane/commit/7d624e84347298c1734c0ca804d3fb4851c180b3) |
| 2011-10-24 | `feature` | add-on fixes | `ScriptingConfiguration.java`, `ManageAddOnsDialog.java` | [2e7a6b6f](https://github.com/freeplane/freeplane/commit/2e7a6b6f9c3fdf4885e2db1393ffb9d884625987) |
| 2011-10-23 | `feature` | final fixes & implement deactivate and deinstall | `AddOnProperties.java`, `AddOnsController.java` +3 | [17e44ef1](https://github.com/freeplane/freeplane/commit/17e44ef1b2814a60ba462f89c01acc232ec7f2c3) |
| 2011-10-19 | `fix` | fix script installation and menu building | `Resources_en.properties`, `installScriptAddOn.groovy` +4 | [a4e93369](https://github.com/freeplane/freeplane/commit/a4e93369c96d914a1f6089ec5f4ef75fef7bb99a) |
| 2011-10-15 | `feature` | Add-ons can contain Zips | `installScriptAddOn.groovy`, `ScriptAddOnProperties.java` | [733e6efe](https://github.com/freeplane/freeplane/commit/733e6efe5cf345ddb6db78e328b6cdb7531cab18) |
| 2011-10-15 | `feature` | remove add-on type from the add-ons dialog | `Resources_de.properties`, `Resources_en.properties` +1 | [7688a97f](https://github.com/freeplane/freeplane/commit/7688a97f1f9d8826b67bc0d0300602e4161b9600) |
| 2011-10-10 | `feature` | add-ons support shortcut setting | `Resources_en.properties`, `installScriptAddOn.groovy` +3 | [89a63bc4](https://github.com/freeplane/freeplane/commit/89a63bc44877b2bb648595099f3704f22d1e2ded) |
| 2011-09-28 | `feature` | fix permission handling of scripts: - can be set for a script individually - add-on permis | `installScriptAddOn.groovy`, `ScriptEditor.java` +4 | [c3e60a49](https://github.com/freeplane/freeplane/commit/c3e60a4966b181e19116210e39f11cde0da9735a) |
| 2011-09-26 | `feature` | add-on configuration, i18n, permissions | `Resources_en.properties`, `installScriptAddOn.groovy` +10 | [ef7a5b93](https://github.com/freeplane/freeplane/commit/ef7a5b93a20a8e8cb6a7c12da8c0245fbb6d7235) |
| 2011-09-24 | `feature` | Add-on-Installer | `Resources_de.properties`, `AddOnProperties.java` +4 | [e28b1575](https://github.com/freeplane/freeplane/commit/e28b1575f500b619059c69350efbe04d2aaa7c5f) |
| 2011-09-23 | `fix` | fix JDK 1.5/1.6 ncompatibilities | `ScriptingRegistration.java`, `ButtonsInCellRenderer.java` +1 | [52300f21](https://github.com/freeplane/freeplane/commit/52300f2155a8eb5bfb175ed62037710140b8e647) |
| 2011-09-15 | `feature` | Prototype of add-on management | `MANIFEST.MF`, `Resources_de.properties` +21 | [39e3ac81](https://github.com/freeplane/freeplane/commit/39e3ac81a46c0768b16729fc56901ba8462e1d33) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
