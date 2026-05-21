# Script / Groovy — Commit rilevanti

**Modulo:** `freeplane_plugin_script`  
**Commit rilevanti (feature / fix / api_change):** 550 su 1290 totali

> Permette di eseguire script **Groovy** (e altri linguaggi JVM) direttamente sulle mappe. È il cuore dell'automazione in Freeplane: si usa per generare nodi, trasformare testo, interrogare API esterne o costruire workflow personalizzati.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 2 commit
- [2025](#2025) — 17 commit
- [2024](#2024) — 9 commit
- [2023](#2023) — 12 commit
- [2022](#2022) — 25 commit
- [2021](#2021) — 26 commit
- [2020](#2020) — 19 commit
- [2019](#2019) — 22 commit
- [2018](#2018) — 65 commit
- [2017](#2017) — 24 commit
- [2016](#2016) — 37 commit
- [2015](#2015) — 27 commit
- [2014](#2014) — 28 commit
- [2013](#2013) — 36 commit
- [2012](#2012) — 38 commit
- [2011](#2011) — 105 commit
- [2010](#2010) — 50 commit
- [2009](#2009) — 8 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, script, and AI | `expose-node-tags-to-ai-tools.md`, `TagCategoryAccess.java` +44 | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |
| 2026-02-20 | `api_change` | 2026-02-20-expose-styles-ai-tools Expose styles in AI tools and unify list API | `expose-node-styles-to-ai-tools.md`, `expose-node-tags-to-ai-tools.md` +30 | [5432e96f](https://github.com/freeplane/freeplane/commit/5432e96f9c9492b88242fcbaec14455da46f731b) |

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-09-01 | `feature` | Issue #2641 New script action is difficult to find in script editor | `ScriptEditorPanel.java` | [4410f359](https://github.com/freeplane/freeplane/commit/4410f359d08e95059a2b8315fa45579689dbbcca) |
| 2025-08-03 | `feature` | Fix UI component references for UI-follows-focus architecture | `GrabKeyDialog.java`, `ShowPreferencesAction.java` +45 | [44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf) |
| 2025-07-12 | `feature` | Scripting API: deprecate StrikedThrough, add Strikethrough | `Font.java`, `FontRO.java` +1 | [ee27a149](https://github.com/freeplane/freeplane/commit/ee27a14956ce8172aa22bd3bfcb9e8ad19085a76) |
| 2025-07-12 | `fix` | Scripting API: rename underlined to underline | `Font.java`, `FontRO.java` +1 | [67ea65c1](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2) |
| 2025-07-05 | `feature` | Issue #2560 add underline | `Resources_ar.properties`, `Resources_ca.properties` +28 | [b48e383d](https://github.com/freeplane/freeplane/commit/b48e383db28b2952d37152d5e667c4c2c53d996b) |
| 2025-06-20 | `api_change` | Improve Bookmark API | `Node.java`, `NodeBookmark.java` +3 | [c7cf203a](https://github.com/freeplane/freeplane/commit/c7cf203af1717dfd3a21c45b6b716f6f1e5b3e00) |
| 2025-06-20 | `feature` | Add open methods to NodeBookmark API and implement in NodeBookmarkProxy class | `NodeBookmark.java`, `NodeBookmarkProxy.java` | [5ac0a772](https://github.com/freeplane/freeplane/commit/5ac0a7720f05a438e951c1f3a3dc8a950a13bee9) |
| 2025-06-19 | `fix` | fix GroovyStaticImports in javadoc | `build.gradle` | [e29da9c1](https://github.com/freeplane/freeplane/commit/e29da9c16216188cd6f64c17569c2e22e9a1e8a2) |
| 2025-06-19 | `feature` | do not add values to API mind map, they mostly have no meaning | `apiGenerator.groovy` | [89dbe0e5](https://github.com/freeplane/freeplane/commit/89dbe0e573aefecdc4bfbc9825351a228761a412) |
| 2025-06-19 | `feature` | add GroovyStaticImports to javadoc | `build.gradle` | [9cb7d12e](https://github.com/freeplane/freeplane/commit/9cb7d12e2888112424acfd208a40f158b370986c) |
| 2025-06-19 | `api_change` | include GroovyStaticImports in API generation | `apiGenerator.groovy` | [7bb11c94](https://github.com/freeplane/freeplane/commit/7bb11c94294edbfe485bfa080a2911b0b57b2b0e) |
| 2025-06-19 | `feature` | Add utility methods and documentation to Enhance and document GroovyStaticImports class | `GroovyStaticImports.java` | [7d354270](https://github.com/freeplane/freeplane/commit/7d3542700f3fcc94449e95d436c37f794fde382d) |
| 2025-06-15 | `feature` | Implement bookmark functionality in Freeplane node api | `BookmarkNodeAction.java`, `BookmarksController.java` +13 | [0b3743d5](https://github.com/freeplane/freeplane/commit/0b3743d5fd6f27f70eb7c8fd20ba67879b89bfa9) |
| 2025-06-15 | `api_change` | Improve internal scrolling API | `NodeBookmark.java`, `IMapSelection.java` +4 | [4dfbb7be](https://github.com/freeplane/freeplane/commit/4dfbb7be38f7adf3b6ee1110aed8a3384ac5873e) |
| 2025-06-15 | `api_change` | align Numbering API with API for other formatting properties | `NodeStyle.java`, `NodeStyleRO.java` +1 | [54bf4ef7](https://github.com/freeplane/freeplane/commit/54bf4ef747fe37ec18bfcf9b4a3230a54d3b79fa) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts | `OptionPanel.java`, `PathProperty.java` +29 | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-01-04 | `fix` | Issue #2190 Fix script exception handling | `ExecuteScriptAction.java`, `GroovyScript.java` +1 | [c5c1ff61](https://github.com/freeplane/freeplane/commit/c5c1ff6100cc43d5fdad1d9631ef90700e475cbc) |

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

**[ee27a149](https://github.com/freeplane/freeplane/commit/ee27a14956ce8172aa22bd3bfcb9e8ad19085a76)** (2025-07-12) — Scripting API: deprecate StrikedThrough, add Strikethrough

> According to Copilot:
> The term "strikethrough" is used as a noun to describe the formatting style itself — a visual effect where text is crossed out with a horizontal line. In contrast, "strike through" is a verb phrase that refers to the action of applying that effect.
> In UI design and programming contexts, property names tend to favor noun forms because they represent states or attributes. So strikethrough fits naturally alongside other formatting properties like bold, italic, or underline.
> 
> `strikethrough` is used to align with naming conventions in the Groovy Scripting API for other formatting settings. For example, the `bold` property uses method names like `isBold()`, `setBold(isBold)``, and `isBoldSet()``, which integrate naturally into Groovy code such as `node.style.font.bold = true`. This is in contrast with `bolded` or `emboldened`, which are the corresponding adjectives for `bold`.
> 
> Formatting to adjective
> -----------------------
> - Bold: bolded, emboldened
> - Italic: italicized
> - Underline: underlined
> - Strikethrough: struck-through, crossed-out

**[67ea65c1](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2)** (2025-07-12) — Scripting API: rename underlined to underline

> Although `underlined` is grammatically correct, `underline` is used to align with naming conventions in the Groovy Scripting API for other formatting settings. For example, the `bold` property uses method names like `isBold()`, `setBold(isBold)``, and `isBoldSet()``, which integrate naturally into Groovy code such as `node.style.font.bold = true`. This is in contrast with `bolded` or `emboldened`, which are the corresponding adjectives for `bold`.
> 
> Formatting to adjective
> -----------------------
> - Bold: bolded, emboldened
> - Italic: italicized
> - Underline: underlined
> - Strikethrough: struck-through, crossed-out

**[7d354270](https://github.com/freeplane/freeplane/commit/7d3542700f3fcc94449e95d436c37f794fde382d)** (2025-06-19) — Add utility methods and documentation to Enhance and document GroovyStaticImports class

> Enhanced the GroovyStaticImports class with additional utility methods for null checking, number rounding, and text parsing. Updated Javadoc to provide comprehensive usage instructions and descriptions for each utility, facilitating easier access to common functionalities when compiling Groovy scripts outside of Freeplane's environment.

**[54bf4ef7](https://github.com/freeplane/freeplane/commit/54bf4ef747fe37ec18bfcf9b4a3230a54d3b79fa)** (2025-06-15) — align Numbering API with API for other formatting properties

> deprecate isNumberingEnabled(), which doubles as isNumbering() and isNumberingSet(), throwing NPL if not set

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
| 2024-08-24 | `feature` | Rework tag categories, add option to show tag categories | `mindmapmodemenu.xml`, `JFilterableComboBox.java` +20 | [ccea2b9d](https://github.com/freeplane/freeplane/commit/ccea2b9dcc98113f3707c893144e7f9fef7f6a92) |
| 2024-06-21 | `fix` | fix formula result refresh for nodes accessing clones | `AccessedNodes.java`, `MultipleNodeList.java` +5 | [66effa94](https://github.com/freeplane/freeplane/commit/66effa9440f7d0f5e1666d5b94c48bf45be0232f) |
| 2024-05-09 | `feature` | Implement map and node tag categories when showing, in filters and API | `mindmapmodemenu.xml`, `preferences.xml` +18 | [0469cdfd](https://github.com/freeplane/freeplane/commit/0469cdfd525609755cf7567e1fc41dab33583209) |
| 2024-05-09 | `feature` | add API methods and filters for tag categories | `preferences.xml`, `CategorizedTag.java` +13 | [b1ee9533](https://github.com/freeplane/freeplane/commit/b1ee9533bb8073270a365b1883c77e472e96f5f1) |
| 2024-05-09 | `feature` | rename methods and parameters in Tags scripting API | `Tags.java`, `TagsRO.java` +1 | [0f8d2842](https://github.com/freeplane/freeplane/commit/0f8d2842aa2bb432ea07d390cb9f8c0730e93dd7) |
| 2024-04-06 | `feature` | implement iconController.getTags() | `IconController.java`, `TagContainedCondition.java` +4 | [707afcf1](https://github.com/freeplane/freeplane/commit/707afcf1bd862a17bfc6e9ef15c85223ed96fee8) |
| 2024-04-04 | `feature` | Add methods supporting tags to Freeplane API | `Node.java`, `NodeRO.java` +5 | [53ca172d](https://github.com/freeplane/freeplane/commit/53ca172d140794625a4d3b4fa2c5ac01a94738fb) |
| 2024-02-18 | `feature` | extend API: add get/set for followed map and associated template | `MindMap.java`, `MindMapRO.java` +1 | [574a4f2e](https://github.com/freeplane/freeplane/commit/574a4f2edbb06a5b8b78a873dc58feb8cf028e57) |
| 2024-01-30 | `feature` | Add scriptUtils to static properties for consistency | `ScriptingConfiguration.java` | [8ef43227](https://github.com/freeplane/freeplane/commit/8ef4322798d012fefaea575ebab423f3c6f9fea5) |

### Dettagli commit con note

**[0f8d2842](https://github.com/freeplane/freeplane/commit/0f8d2842aa2bb432ea07d390cb9f8c0730e93dd7)** (2024-05-09) — rename methods and parameters in Tags scripting API

> - change parameter names from `string` and `tag` to `keyword` -- for the string representation of a Tag -- to make it uniform across get and set, as well as to make it clear that only `keyword` is affected, not `Tag` consisting of `keyword` and `color`
> - use bare `add` and `remove` for any argument types to make it easier to type the code when creating scripts in Groovy
> - optimize `containsAll` for performance


---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-11-24 | `feature` | Update scripting api generator (#1544) | `apiGenerator.groovy` | [31a03915](https://github.com/freeplane/freeplane/commit/31a03915c5cded8e981c6b7d7aba57fbd236282b) |
| 2023-11-24 | `feature` | new api method: mindMap.copyUserStylesFrom(...) (#1541) | `MindMap.java`, `MapProxy.java` | [8d8c71a0](https://github.com/freeplane/freeplane/commit/8d8c71a04e1ad0b141f1e8e87ecebd2aeb49d6ef) |
| 2023-10-29 | `feature` | API changes (node's border and edge) (#1355) | `ComboProperty.java`, `DashIconFactory.java` +39 | [2a803599](https://github.com/freeplane/freeplane/commit/2a80359962a8ea7b3aa98caa760dd781e7ffd5c3) |
| 2023-10-02 | `feature` | Add horizontal text alignment to API | `NodeStyleBuilder.java`, `NodeStyleController.java` +12 | [c54d215e](https://github.com/freeplane/freeplane/commit/c54d215e9760368c013203dd3232124c95dd7863) |
| 2023-09-22 | `feature` | fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when `Opt | `ExternalObjectProxy.java` | [ca0c9524](https://github.com/freeplane/freeplane/commit/ca0c95243801593441f6492ef03e995f0782caf7) |
| 2023-09-22 | `feature` | Revert "fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` w | `ViewerController.java`, `ExternalObjectProxy.java` | [d79e2179](https://github.com/freeplane/freeplane/commit/d79e21797976fc877a1ba9c28a3f6dd0f26ea916) |
| 2023-09-16 | `feature` | fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mind | `ViewerController.java`, `ExternalObjectProxy.java` | [02f32e28](https://github.com/freeplane/freeplane/commit/02f32e2872554313c0cfe66ea1918c103600983d) |
| 2023-09-05 | `fix` | fix and extend uri-to-file conversion | `LinkProxy.java` | [f3f801be](https://github.com/freeplane/freeplane/commit/f3f801be4be4ce07a6d367c73a00306941944fad) |
| 2023-06-19 | `api_change` | allow non html content in note / detail API proxy | `NoteManager.java`, `TextController.java` +1 | [e1f2ab4d](https://github.com/freeplane/freeplane/commit/e1f2ab4d63a807008dd746af9c24491f718f11d5) |
| 2023-05-26 | `feature` | support setting of double properties | `ResourceController.java`, `FreeplaneScriptBaseClass.java` | [f554850b](https://github.com/freeplane/freeplane/commit/f554850bf7d852ca848a98f7dd0e14f53506b6e8) |
| 2023-05-13 | `feature` | Add node API methods getBranchAsTextOutline and appendTextOutlineAsBranch | `MapClipboardController.java`, `MindMapPlainTextWriter.java` +4 | [023d7d9d](https://github.com/freeplane/freeplane/commit/023d7d9de5adcccd492e2f2b3c0f1c14b29d9f95) |
| 2023-03-03 | `feature` | Add function getChildNodesLayout to API | `Node.java`, `NodeRO.java` +1 | [93337e97](https://github.com/freeplane/freeplane/commit/93337e97902d12af2b9cb9c7f9a102abaecc37f2) |

### Dettagli commit con note

**[31a03915](https://github.com/freeplane/freeplane/commit/31a03915c5cded8e981c6b7d7aba57fbd236282b)** (2023-11-24) — Update scripting api generator (#1544)

> * add icons to icons branch
> 
> * better Strings for node texts
> 
> * noDuplicatedMapName
> 
> to avoid the same name for two open maps
> 
> * adds missing classes
> 
> Update apiGenerator.groovy
> 
> * sort classes in proxy and utils nodes
> 
> * adding enums and constants
> 
> adding enums and constants
> 
> * deleting useless comments

**[8d8c71a0](https://github.com/freeplane/freeplane/commit/8d8c71a04e1ad0b141f1e8e87ecebd2aeb49d6ef)** (2023-11-24) — new api method: mindMap.copyUserStylesFrom(...) (#1541)

> * Adds copyUserStylesFrom() method to mindMap API

**[2a803599](https://github.com/freeplane/freeplane/commit/2a80359962a8ea7b3aa98caa760dd781e7ffd5c3)** (2023-10-29) — API changes (node's border and edge) (#1355)

> * API changes
> 
> 1. expose Border object and its color methods
> 2. expose isColorSet for Edge object
> 
> * simplifying expressions
> 
> * Adding width methods to Border api
> 
> * Move RenderedContentSupplier methods from enums so that the enums can be used in freeplane api
> 
> * Decouple DashVariant from icons and UITools
> 
> * Apply font scale factor to dashed curves
> 
> * Move DashVariant to freeplane api and improve naming
> 
> * implement new API methods
> 
> * Use the old name to ensure backward compatibility with old maps
> 
> * corrects border.isWithSet
> 
> * implements "border Matches Edge ..." methods
> 
> * implements "isSet" for "border Matches Edge..." in Border API
> 
> implements:
> - border.isUsesEdgeColorSet()
> - border.isUsesEdgeWidthSet()
> - border.isUsesEdgeDashSet()
> 
> * implements additional border.setWidth() methods
> 
> * Adds some explanation for API's java doc
> 
> ---------
> 
> Co-authored-by: Dimitry Polivaev <dpolivaev@gmx.de>

**[ca0c9524](https://github.com/freeplane/freeplane/commit/ca0c95243801593441f6492ef03e995f0782caf7)** (2023-09-22) — fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when `OptionPanel.links == "relative"`

> by bypassing URI checks via the simple paste() method

**[d79e2179](https://github.com/freeplane/freeplane/commit/d79e21797976fc877a1ba9c28a3f6dd0f26ea916)** (2023-09-22) — Revert "fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mindMap isn't saved and `OptionPanel.links == "relative"`"

> This reverts commit 02f32e2872554313c0cfe66ea1918c103600983d.

**[02f32e28](https://github.com/freeplane/freeplane/commit/02f32e2872554313c0cfe66ea1918c103600983d)** (2023-09-16) — fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mindMap isn't saved and `OptionPanel.links == "relative"`

> by bypassing URI checks via the extracted setExternalResource; the fix is needed for the PackAndGoGo add-on


---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-12-11 | `feature` | fix: add missing getDelegate() to call method of MLogicalStyleController instead of Logica | `MapConditionalStylesProxy.java` | [7f950e47](https://github.com/freeplane/freeplane/commit/7f950e47315486205f1f2e6aba2edb9ce9d46340) |
| 2022-12-11 | `feature` | implement callDelayedRefresh | `MapController.java`, `LogicalStyleController.java` +4 | [497a49bd](https://github.com/freeplane/freeplane/commit/497a49bd27813ea9bcab5f005115b6d217fe506d) |
| 2022-12-06 | `feature` | implement base distance to child nodes | `LocationBuilder.java`, `LocationController.java` +15 | [06614fd5](https://github.com/freeplane/freeplane/commit/06614fd5dfa0721230b09c7fa1f49c63a0ea4c36) |
| 2022-11-24 | `feature` | Refactor creation of new nodes | `NodeProxy.java` | [d8a0c368](https://github.com/freeplane/freeplane/commit/d8a0c368b9200759d8e01874a68cbf6a2c657480) |
| 2022-11-24 | `feature` | Issue  #843 conditional formating script filter rules are not applied to the new node. | `ComparableByPriority.java`, `IMapChangeListener.java` +5 | [8f17ede4](https://github.com/freeplane/freeplane/commit/8f17ede4e786720796ad7c4feafb8d5dd97072c1) |
| 2022-11-04 | `feature` | wip replace old three enums by the new one | `LayoutBuilder.java`, `LayoutController.java` +16 | [598bd606](https://github.com/freeplane/freeplane/commit/598bd606c85e6d1488e499dcc3bc86c622479b66) |
| 2022-10-30 | `feature` | add more Java-doc and bump @since; refactor | `ConditionalStyle.java`, `ConditionalStyleRO.java` +12 | [219f8aeb](https://github.com/freeplane/freeplane/commit/219f8aeb0cbb60f708e8bc32d005bbe75de4e246) |
| 2022-10-30 | `feature` | add ConditionalStyles-related api | `ConditionalStyleModel.java`, `LogicalStyleController.java` +21 | [61f92526](https://github.com/freeplane/freeplane/commit/61f9252654b98faee1433e98a562c3b43392d016) |
| 2022-10-09 | `feature` | Implement layout model and controllers | `LayoutBuilder.java`, `LayoutController.java` +23 | [4f2aef94](https://github.com/freeplane/freeplane/commit/4f2aef9423a4ae60c225b7609bfb56f99a4ad69a) |
| 2022-10-09 | `api_change` | Change API to reflect both possible layout directions | `ConnectorProperties.java`, `NodeModel.java` +31 | [60010ce9](https://github.com/freeplane/freeplane/commit/60010ce96cc296de07b7740decf83887066cd901) |
| 2022-10-03 | `feature` | Issue #703 The setting "Place new branches" (being set to "First") should affect more than | `MMapController.java`, `MMapClipboardController.java` +4 | [f104a4a7](https://github.com/freeplane/freeplane/commit/f104a4a72ff76252bebb1d71a725e74fbcfd707a) |
| 2022-09-14 | `fix` | fix Side, change links | `apiGenerator.groovy` | [58d0b59c](https://github.com/freeplane/freeplane/commit/58d0b59c33c94a40deae6a17322cd9c24d0e645f) |
| 2022-09-09 | `feature` | Add style/node property VerticalNodeLayout | `LocationBuilder.java`, `LocationController.java` +14 | [6c99f1a8](https://github.com/freeplane/freeplane/commit/6c99f1a8a7363abca2b03aa9597ab241d16bc47c) |
| 2022-09-02 | `api_change` | rename API method to get/setSideAtRoot | `Node.java`, `NodeRO.java` +1 | [a1423157](https://github.com/freeplane/freeplane/commit/a142315768fffc5c21ddbceac6781eea226dbcef) |
| 2022-08-28 | `api_change` | Change API metod names as discussed in https://github.com/freeplane/freeplane/discussions/ | `Node.java`, `NodeRO.java` +3 | [ea10a8c1](https://github.com/freeplane/freeplane/commit/ea10a8c1673e25819a57d08e170f68552e6ff4cd) |
| 2022-08-20 | `fix` | Fix script menu entry titles and change menu item title for Api Generator | `Resources_en.properties`, `ScriptingMenuEntryVisitor.java` | [b76798ae](https://github.com/freeplane/freeplane/commit/b76798aef3a47fd1a3f766391e111035e0041199) |
| 2022-08-20 | `feature` | add ViewSide to api map | `apiGenerator.groovy` | [4ee2c4c6](https://github.com/freeplane/freeplane/commit/4ee2c4c686423547ee069a9434c3c4be2bcdb3d6) |
| 2022-08-20 | `feature` | Add new methods handling node sides to freeplane API | `ControllerRO.java`, `Node.java` +5 | [37de591a](https://github.com/freeplane/freeplane/commit/37de591abc660d793d6ac2bf384b00ee5b20f78b) |
| 2022-08-16 | `feature` | add missing classes, include enum constants | `apiGenerator.groovy` | [90f6b7bd](https://github.com/freeplane/freeplane/commit/90f6b7bd34c10a29d6314ac3e756ea61b0085814) |
| 2022-08-12 | `fix` | fix node side after drag and drop | `MapController.java`, `NodeModel.java` +14 | [70323ae4](https://github.com/freeplane/freeplane/commit/70323ae4ec246458d432dd412347fb938f3b008a) |
| 2022-08-02 | `feature` | extend API: add MindMap getListeners | `MindMap.java`, `MapProxy.java` +2 | [ec5687d9](https://github.com/freeplane/freeplane/commit/ec5687d96a0321ebbc2b342fab0400cf79ffc802) |
| 2022-05-21 | `fix` | fix script editor | `ScriptEditorPanel.java` | [d5145322](https://github.com/freeplane/freeplane/commit/d514532215edded8e4670e2334a456f364c3861e) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-03-26 | `feature` | make script editor non modal and add node short text to dialog title | `ScriptEditor.java`, `ScriptEditorPanel.java` +1 | [8e346c8e](https://github.com/freeplane/freeplane/commit/8e346c8e7e18a4def935e88930631d0780e58253) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-12-12 | `feature` | Add methods to NodeStyleRO: isBackgroundColorSet(), isTextColorSet(), isMinNodeWidthSet(), | `NodeStyleRO.java`, `NodeStyleProxy.java` | [48bf9a24](https://github.com/freeplane/freeplane/commit/48bf9a2417f13a989bcb98dfc4f7f978bbcc4229) |
| 2021-12-11 | `feature` | add method NodeStyleRO.isCssSet() to API | `NodeStyleRO.java`, `NodeStyleProxy.java` | [7e489e04](https://github.com/freeplane/freeplane/commit/7e489e04858b6cfff8dacfd519ba4034ab62fab6) |
| 2021-12-03 | `feature` | Add CSS getter and setter to script API | `NodeStyle.java`, `NodeStyleRO.java` +1 | [09801db2](https://github.com/freeplane/freeplane/commit/09801db27f0f86babc04417a598de27466d18605) |
| 2021-11-13 | `api_change` | #3068 API show descendants fails to work on fp-1.9.11 | `MapProxy.java` | [0b6ca365](https://github.com/freeplane/freeplane/commit/0b6ca36556b6b07dac5ba45ad78590d257e2e92b) |
| 2021-10-08 | `fix` | Fix reuse of old filter conditions | `Filter.java`, `FilterController.java` +5 | [37b87f7f](https://github.com/freeplane/freeplane/commit/37b87f7f4ce2339766f262a8ba7e79b74f4f3ff2) |
| 2021-10-07 | `feature` | Support complex conditional styles and script conditions in conditional styles | `ASelectableCondition.java`, `ConditionalStyleModel.java` +1 | [2b5ed1f2](https://github.com/freeplane/freeplane/commit/2b5ed1f29cf015ec14a8550aa8d8b79e3c207d05) |
| 2021-09-05 | `feature` | rename new api method | `MindMap.java`, `MapProxy.java` | [927a6fe2](https://github.com/freeplane/freeplane/commit/927a6fe255f37c7c635ce0d28b2273cc8d920ddc) |
| 2021-09-04 | `api_change` | script API MindMap.copyStyleFrom, MindMap.copyStyleConditionsFrom | `ConditionalStyleModel.java`, `LogicalStyleController.java` +3 | [d3a3125e](https://github.com/freeplane/freeplane/commit/d3a3125e27693bc467d47698e39bdcfecaab9407) |
| 2021-09-04 | `api_change` | script api List<String> NodeStyle.getAllActiveStyles() | `NodeStyleRO.java`, `NodeStyleProxy.java` | [0564a012](https://github.com/freeplane/freeplane/commit/0564a0121f22c89a02136f2c9f96ceb00be6d072) |
| 2021-08-07 | `feature` | #2986 If new views of a map are created their name in groovy is wrong | `ControllerProxy.java`, `MapProxy.java` | [35a1976a](https://github.com/freeplane/freeplane/commit/35a1976af1b823a91162330303bc67217812b4f7) |
| 2021-08-07 | `fix` | #2988 fix apiGenerator.groovy (Cannot get property 'name' on null object) | `apiGenerator.groovy` | [8e0002b5](https://github.com/freeplane/freeplane/commit/8e0002b506853010d24f670d6d2c5bfe3cf1b021) |
| 2021-07-03 | `fix` | fix NPE | `LinkProxy.java` | [72ec8177](https://github.com/freeplane/freeplane/commit/72ec81776254d4d57a34f871d45116e4e7b7bd14) |
| 2021-06-29 | `api_change` | Use recursiveComparison for asserts instead of deprecated API | `CompiledFilesSpec.java` | [008c80ab](https://github.com/freeplane/freeplane/commit/008c80ab7c301f5305623ea908b6d5e49ecbfc23) |
| 2021-06-27 | `fix` | fix it and allow custom hyperlinks | `Hyperlink.java`, `TypeReference.java` +15 | [cccd2fc0](https://github.com/freeplane/freeplane/commit/cccd2fc06998c54fcdd8a74d23f73226f6838325) |
| 2021-06-19 | `fix` | fix copying nodes from other maps | `INodeDuplicator.java`, `MapModel.java` +3 | [bca22f6f](https://github.com/freeplane/freeplane/commit/bca22f6f6d0495292598cf396aa2d671e2a433d7) |
| 2021-06-03 | `fix` | fix editor background colors on VAqua | `NoteStyleAccessor.java`, `MNoteController.java` +9 | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-05-13 | `fix` | Fix jsyntaxpane package import | `build.gradle`, `build.gradle` +1 | [fd935f1f](https://github.com/freeplane/freeplane/commit/fd935f1f882564cecd9d3998e2f710e406daaa82) |
| 2021-05-07 | `fix` | #2919 Fix cleaning of compiled script file directory | `CompiledScriptCleaner.java` | [60bd75cc](https://github.com/freeplane/freeplane/commit/60bd75ccf447e1e3e659bb862435a6ff51b063a7) |
| 2021-04-04 | `feature` | add enum simple class name to property name in resources | `Resources_af.properties`, `Resources_ar.properties` +74 | [463128be](https://github.com/freeplane/freeplane/commit/463128bee5f9972e9307c656bae9529e9cb7e1e8) |
| 2021-03-13 | `feature` | Add content type getters and setters to API | `Node.java`, `NodeRO.java` +1 | [eee68e0a](https://github.com/freeplane/freeplane/commit/eee68e0a8108c9b8d257c93778d9cf48106dcf14) |
| 2021-03-07 | `fix` | fix NPE | `ConnectorProxy.java` | [85e93935](https://github.com/freeplane/freeplane/commit/85e93935f9e0d04b1beb12fe18a765696dd95aa9) |
| 2021-02-27 | `fix` | fix NPE | `ScriptCondition.java` | [f499d7c2](https://github.com/freeplane/freeplane/commit/f499d7c24a6df354af364b384e60359b98442fba) |
| 2021-02-13 | `feature` | implement equals and hashCode for ScriptCondition | `ScriptCondition.java` | [a27aad9a](https://github.com/freeplane/freeplane/commit/a27aad9a73b60475845ef0dea773e72dbc675dec) |
| 2021-01-07 | `fix` | fix concurrent modification exception | `EvaluationDependencies.java` | [94dc0886](https://github.com/freeplane/freeplane/commit/94dc08868b963653f0f17a5b4d6a19aef21e8aaa) |
| 2021-01-07 | `feature` | introduce interface INodeDuplicator and add operation duplicate on nodes | `XmlImporter.java`, `INodeDuplicator.java` +14 | [63fca871](https://github.com/freeplane/freeplane/commit/63fca871c8305e7418d15443033fced1f40dc2c8) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown support | `build.gradle`, `FormulaEditor.java` +14 | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |

### Dettagli commit con note

**[008c80ab](https://github.com/freeplane/freeplane/commit/008c80ab7c301f5305623ea908b6d5e49ecbfc23)** (2021-06-29) — Use recursiveComparison for asserts instead of deprecated API

> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>

**[60bd75cc](https://github.com/freeplane/freeplane/commit/60bd75ccf447e1e3e659bb862435a6ff51b063a7)** (2021-05-07) — #2919 Fix cleaning of compiled script file directory

> org.apache.commons.io.IOExceptionList: 1 exceptions:
> [java.io.IOException: Unable to delete file]
>     at org.apache.commons.io.FileUtils.cleanDirectory(FileUtils.java:345)
>     at org.apache.commons.io.FileUtils.deleteDirectory(FileUtils.java:1206)
>     at org.freeplane.plugin.script.CompiledScriptCleaner.removeOutdated(CompiledScriptCleaner.java:77)
>     at org.freeplane.plugin.script.CompiledScriptCleaner.lambda$removeOutdatedCompiledScripts$1(CompiledScriptCleaner.java:54)
>     at java.util.Spliterators$ArraySpliterator.forEachRemaining(Unknown
> Source)
>     at java.util.stream.ReferencePipeline$Head.forEach(Unknown Source)
>     at org.freeplane.plugin.script.CompiledScriptCleaner.removeOutdatedCompiledScripts(CompiledScriptCleaner.java:54)
>     at org.freeplane.plugin.script.ClasspathScriptCompiler.compileScriptsOnPath(ClasspathScriptCompiler.java:63)

**[a27aad9a](https://github.com/freeplane/freeplane/commit/a27aad9a73b60475845ef0dea773e72dbc675dec)** (2021-02-13) — implement equals and hashCode for ScriptCondition

> #2872 FP 1.9.0 alpha 03: Conditional rules get duplicated when using
> "Follow Styles"

**[94dc0886](https://github.com/freeplane/freeplane/commit/94dc08868b963653f0f17a5b4d6a19aef21e8aaa)** (2021-01-07) — fix concurrent modification exception

> java.util.ConcurrentModificationException
> 	at java.util.WeakHashMap$HashIterator.nextEntry(Unknown Source)
> 	at java.util.WeakHashMap$KeyIterator.next(Unknown Source)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:78)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:81)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:81)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:81)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:81)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getRecursively(EvaluationDependencies.java:81)
> 	at org.freeplane.plugin.script.dependencies.EvaluationDependencies.getChangedDependencies(EvaluationDependencies.java:62)
> 	at org.freeplane.plugin.script.FormulaDependencies.getAllChangedDependencies(FormulaDependencies.java:30)


---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-30 | `api_change` | improve API export function | `ControllerRO.java`, `ControllerProxy.java` | [91516b50](https://github.com/freeplane/freeplane/commit/91516b507a4f99980c8ca5c028b00641e55f2d5b) |
| 2020-12-30 | `feature` | can not create map inside transaction #181 | `AttributeManagerDialog.java`, `MModeController.java` +1 | [38e4e4c6](https://github.com/freeplane/freeplane/commit/38e4e4c6f0b235c0f82487b74a9dec74e455ad89) |
| 2020-12-30 | `api_change` | You can use a substring or an empty string instead of full description in API controller.e | `ControllerRO.java`, `ControllerProxy.java` | [d5867ee5](https://github.com/freeplane/freeplane/commit/d5867ee5fe606582922970c30b0a966e141ebd5e) |
| 2020-12-13 | `feature` | Add node geometry operations to node API | `Node.java`, `NodeGeometry.java` +6 | [8b7cbc71](https://github.com/freeplane/freeplane/commit/8b7cbc71cde47a85a643e67a48618665d1b3a2bf) |
| 2020-12-13 | `api_change` | Extend freeplane API to use Quantities and Length Units | `Node.java`, `NodeRO.java` +2 | [4047c97a](https://github.com/freeplane/freeplane/commit/4047c97ae1a987e6da27a3392e4136cf01cb4992) |
| 2020-11-28 | `feature` | Add freeplane.gdsl to sources | `freeplane.gdsl` | [2a0ef156](https://github.com/freeplane/freeplane/commit/2a0ef1560659c2a9abcce20be5c471766f9d3c86) |
| 2020-07-28 | `fix` | fix condition in CompiledScriptCleaner | `CompiledScriptCleaner.java`, `GroovyShell.java` | [72bcddd4](https://github.com/freeplane/freeplane/commit/72bcddd44075e7bc64e7c2a54bb92d923b22bd5b) |
| 2020-07-25 | `fix` | fix NPE | `CompiledScriptCleaner.java`, `GroovyShell.java` | [1fe6c4af](https://github.com/freeplane/freeplane/commit/1fe6c4afb60edac5085c328c01d9b8905d2bac97) |
| 2020-06-06 | `fix` | fix #2788 Can't remove or undo map filters created by script | `ApplyNoFilteringAction.java`, `FilterController.java` +4 | [cf0c8081](https://github.com/freeplane/freeplane/commit/cf0c80810882617efb79134c1b450b9b6cfd0c6f) |
| 2020-06-06 | `fix` | fix #2785 Filtering attributes not working | `ApplyNoFilteringAction.java`, `FilterController.java` +4 | [7078e26c](https://github.com/freeplane/freeplane/commit/7078e26c14c1bf5be13512da97235e34d6a6f331) |
| 2020-06-05 | `fix` | Fix slow JFileChooser for windows by not using Windows icons | `OptionPanel.java`, `PathProperty.java` +18 | [80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be) |
| 2020-05-11 | `fix` | fix filter applied to visible nodes | `Filter.java`, `FilterController.java` +4 | [666a6831](https://github.com/freeplane/freeplane/commit/666a683140325b36341570c2971c0317c79f67f6) |
| 2020-03-08 | `feature` | Add script API for hiding nodes by filter condition | `MindMap.java`, `MapProxy.java` | [f2ff5ae3](https://github.com/freeplane/freeplane/commit/f2ff5ae3559ee860c489f19c8c0d0b47f2478dda) |
| 2020-03-08 | `feature` | Add script for hiding nodes by filter condition | `MindMap.java`, `MapProxy.java` | [f0e609e9](https://github.com/freeplane/freeplane/commit/f0e609e943636140118909d72129049f10c44a2e) |
| 2020-03-06 | `feature` | Add specific RuntimeException ScriptEngineNotLoaded | `GenericScript.java`, `ScriptEngineNotLoadedException.java` | [2b0fa4fb](https://github.com/freeplane/freeplane/commit/2b0fa4fbe88365baf718d5c12b3736f7868397e7) |
| 2020-03-06 | `fix` | fix dialog icon | `ManageAddOnsDialog.java` | [df67c1fb](https://github.com/freeplane/freeplane/commit/df67c1fb597b504cee6dd68db29461c7809c8ced) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-02-11 | `feature` | rename methods, add method HtmlUtils.textToHTML | `HtmlUtils.java`, `AboutAction.java` +13 | [adcdd4ac](https://github.com/freeplane/freeplane/commit/adcdd4ac97e67df07fc788e4882efbd43fe7f9fc) |
| 2020-01-27 | `fix` | #2726 fix manage addons dialog icon | `ManageAddOnsDialog.java` | [66543b82](https://github.com/freeplane/freeplane/commit/66543b824c040b2c3e20b5ad6e9d12e2b9c0a5cd) |

### Dettagli commit con note

**[38e4e4c6](https://github.com/freeplane/freeplane/commit/38e4e4c6f0b235c0f82487b74a9dec74e455ad89)** (2020-12-30) — can not create map inside transaction #181

> https://github.com/freeplane/freeplane/issues/181

**[80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be)** (2020-06-05) — Fix slow JFileChooser for windows by not using Windows icons

> https://stackoverflow.com/a/59165208/1833472


---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-12-13 | `feature` | Update groovy to 2.5.8 to support Java 13 | `build.gradle` | [081277b0](https://github.com/freeplane/freeplane/commit/081277b0b0c7feabb908e2272b3c518385787beb) |
| 2019-10-25 | `fix` | Fix jsyntaxpane package import | `build.gradle` | [8e612af6](https://github.com/freeplane/freeplane/commit/8e612af6d898731abcc21056e5830ae5461ec2f8) |
| 2019-10-18 | `fix` | fix plugin bundle imports | `build.gradle`, `build.gradle` | [bf81ff64](https://github.com/freeplane/freeplane/commit/bf81ff641d0a30e86271969f16da235483aa7b2e) |
| 2019-10-12 | `fix` | fix NPE | `ScriptingMenuEntryVisitor.java` | [36761707](https://github.com/freeplane/freeplane/commit/3676170704df24b5bee1ebfe274ae88f923b07f5) |
| 2019-10-12 | `fix` | fix NPE | `ScriptingMenuEntryVisitor.java` | [d29e56fe](https://github.com/freeplane/freeplane/commit/d29e56fea13cb2da57126d16b7ff29426e4b7e88) |
| 2019-10-06 | `feature` | implement strikedThrough property of node.style.font | `Font.java`, `FontRO.java` +2 | [128a2695](https://github.com/freeplane/freeplane/commit/128a2695002680a0d4d5ae76af2027f5c2df5ee5) |
| 2019-09-28 | `fix` | Fix table row heights after font scaling | `UITools.java`, `AttributeRegistryTable.java` +4 | [15384981](https://github.com/freeplane/freeplane/commit/15384981d8172c23ee2004eb05d286ba07802dde) |
| 2019-09-28 | `feature` | Add new properties  to connector API : dashArray, opacity, width, labelFontFamily and labe | `ColorUtils.java`, `LinkBuilder.java` +10 | [f4c86c81](https://github.com/freeplane/freeplane/commit/f4c86c8129390c482d1823494186137497d77f63) |
| 2019-09-14 | `feature` | Support dark mode | `build.gradle`, `history_en.txt` +9 | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2019-09-08 | `api_change` | API change: replace interface Map by MindMap, deprecate Map | `Controller.java`, `ControllerRO.java` +14 | [04b99850](https://github.com/freeplane/freeplane/commit/04b9985053bac60f98a4bbf2404b4e818d26993a) |
| 2019-08-22 | `fix` | fix for headless environments | `ScriptConditionController.java` | [5a3edda3](https://github.com/freeplane/freeplane/commit/5a3edda3e9d283f20fa8a484ead82aa5c4ea6125) |
| 2019-08-18 | `api_change` | getMainThreadExecutorService from freeplane API | `Controller.java`, `EventQueueExecutorServiceAdapter.java` +7 | [8663a7e0](https://github.com/freeplane/freeplane/commit/8663a7e01e35cee472753500169f58d9a38b59bc) |
| 2019-08-10 | `feature` | Add NodeChangeListener to Freeplane API | `Map.java`, `NodeChangeListener.java` +5 | [746e83e0](https://github.com/freeplane/freeplane/commit/746e83e0565e3b37e24ea881802e16a2ed768b4b) |
| 2019-05-25 | `fix` | fix Grape for Java 12 | `GrapeMetaClass.java` | [c680962f](https://github.com/freeplane/freeplane/commit/c680962f20d66e47fcbfa21dd043105ad95c8e93) |
| 2019-02-22 | `fix` | fix NPE | `GroovyScript.java` | [9fc305cf](https://github.com/freeplane/freeplane/commit/9fc305cf8ef046c87593134aaeb527bb36e02625) |
| 2019-02-22 | `fix` | fix StackOverflowError | `ControllerProxy.java` | [afb3ae16](https://github.com/freeplane/freeplane/commit/afb3ae168bf72dc9659c6895fc675a541bc9b9bb) |
| 2019-01-27 | `api_change` | rename API method loader to mapLoader | `Controller.java`, `HeadlessMapCreator.java` +3 | [d0125d20](https://github.com/freeplane/freeplane/commit/d0125d208316f73aabdecc896b719ab2ec5403bd) |
| 2019-01-17 | `feature` | move ignoreCycles to ScriptUtils and add it as default static import | `FormulaUtils.java`, `FreeplaneScriptBaseClass.java` +2 | [087a37d6](https://github.com/freeplane/freeplane/commit/087a37d630e58cce411b270ae76d81ccee9f59ac) |
| 2019-01-17 | `feature` | support @grab for compiled groovy classes in the library | `GrapeMetaClass.java`, `ScriptClassLoader.java` | [89622f20](https://github.com/freeplane/freeplane/commit/89622f20408b1363f7a7bbd34260dee96e9542de) |
| 2019-01-08 | `api_change` | API for find operations including ancestors / descendants | `Filter.java`, `ControllerRO.java` +5 | [16e2a07c](https://github.com/freeplane/freeplane/commit/16e2a07cf07acf0ef1c54005c955dea44017d5f0) |
| 2019-01-06 | `fix` | fix API access | `ScriptClassLoader.java` | [1226fde2](https://github.com/freeplane/freeplane/commit/1226fde2cd1a2123fcd2d9d5d2ed7102d452d234) |
| 2019-01-02 | `feature` | fix lookup of menu titles for add-on sub-menus that got broken around version 1.4. Before  | `ScriptingMenuUtils.java` | [08ea029a](https://github.com/freeplane/freeplane/commit/08ea029a7867985b130f82d91b530ed092786273) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-31 | `fix` | Revert "fix changing script permissions" | `ScriptClassLoader.java`, `ScriptingPermissions.java` | [1c2bf60f](https://github.com/freeplane/freeplane/commit/1c2bf60fed975616a95224f4425d4d197f51c46f) |
| 2018-12-30 | `fix` | fix reminder script execution | `ReminderHook.java`, `NodeListWithReminders.java` +2 | [797d2096](https://github.com/freeplane/freeplane/commit/797d2096d75139a6f52c7b533ff8f403ad79d751) |
| 2018-12-29 | `fix` | fix formatting to use spaces only | `apiGenerator.groovy` | [1012c9f9](https://github.com/freeplane/freeplane/commit/1012c9f9f36393051de79a652cd500e6dc52ec50) |
| 2018-12-29 | `feature` | add 'closed' icon for deprecated methods and fix the Groovy API URL after closing of groov | `apiGenerator.groovy` | [ef5d0564](https://github.com/freeplane/freeplane/commit/ef5d0564b1d441d7c14b38a24607174a55e653df) |
| 2018-12-29 | `feature` | Add Freeplane API... action to open javadoc from help menu | `mindmapmodemenu.xml`, `OpenURLAction.java` +3 | [bd78c185](https://github.com/freeplane/freeplane/commit/bd78c1854667b4b536788cad217a26b28f46767f) |
| 2018-12-29 | `fix` | Fix generated API title and version | `build.gradle`, `dist.gradle` +1 | [5a22db0a](https://github.com/freeplane/freeplane/commit/5a22db0a544740b7db6f419de808b21fcd148eed) |
| 2018-12-27 | `fix` | fix changing script permissions | `GenericScript.java`, `GroovyScript.java` | [ab1346fe](https://github.com/freeplane/freeplane/commit/ab1346fe92360746ea351d7e4d871e9e9d3cd77e) |
| 2018-12-27 | `fix` | fix changing script permissions | `ScriptClassLoader.java`, `ScriptingPermissions.java` | [6a6e155b](https://github.com/freeplane/freeplane/commit/6a6e155b29cb434a9e97b45707800cc77ff1d4ee) |
| 2018-12-27 | `fix` | fix changing script permissions | `GenericScript.java`, `ScriptClassLoader.java` | [400a7413](https://github.com/freeplane/freeplane/commit/400a74136103d1a06e7c8ab64ade8c8215ba1fac) |
| 2018-12-11 | `feature` | Use raw object in Convertible.isEqual and add a getter to return it | `Convertible.java`, `Convertible.java` | [7f95541d](https://github.com/freeplane/freeplane/commit/7f95541d6ffa30779a41258e1b82437287fb3bf1) |
| 2018-11-24 | `fix` | fix NPE | `ScriptContext.java` | [71675782](https://github.com/freeplane/freeplane/commit/716757825eeafc732e36718608bcd86b338eeecc) |
| 2018-11-12 | `feature` | Fix: create map views in newMap and newMapFromTemplate | `ControllerProxy.java` | [8dfef80e](https://github.com/freeplane/freeplane/commit/8dfef80e93bcf65f5fe194ec9da1e0e2acec85d3) |
| 2018-11-10 | `api_change` | API scripts run with standard permissions | `StringScriptProxy.java` | [7ca12ca6](https://github.com/freeplane/freeplane/commit/7ca12ca6f842f1354f107698307cef6f595de13f) |
| 2018-11-04 | `api_change` | API scripts run with all permissions | `HeadlessMapCreator.java`, `FileScriptProxy.java` +1 | [9e6f7623](https://github.com/freeplane/freeplane/commit/9e6f76231b32fa120f7fa84611e5e6e835afa43a) |
| 2018-11-04 | `fix` | Test script execution using API and fix script execution permission | `TestApp.java`, `ScriptProxy.java` | [2beacb26](https://github.com/freeplane/freeplane/commit/2beacb26d61fd5dddcde1df67ad67302d26039a8) |
| 2018-11-04 | `feature` | add API method to execute embedded scripts | `HeadlessMapCreator.java`, `ExecuteScriptAction.java` +7 | [32a54497](https://github.com/freeplane/freeplane/commit/32a54497627291045e998cd3bbed1868bfe90446) |
| 2018-11-03 | `feature` | Add toString and refactor FreeplaneScriptBaseClass | `FreeplaneScriptBaseClass.java`, `GroovyScript.java` +1 | [7ef24363](https://github.com/freeplane/freeplane/commit/7ef24363b7ebf5793ab2ceab2eee820b5fd4961b) |
| 2018-11-03 | `feature` | Add toScrng and refactor FreeplaneScriptBaseClass | `FreeplaneScriptBaseClass.java`, `GroovyScript.java` +1 | [3d1e50d1](https://github.com/freeplane/freeplane/commit/3d1e50d1bef16627fe78315358e1dafe4316901f) |
| 2018-10-27 | `api_change` | API method evaluateOutdatedFormulas and small refactoring | `Map.java`, `FormulaUtils.java` +1 | [60ecf8bf](https://github.com/freeplane/freeplane/commit/60ecf8bf130ce09f02a734caa7c724c348f4ce98) |
| 2018-10-27 | `fix` | fix evaluateAllFormulas | `FormulaUtils.java` | [2602aa2b](https://github.com/freeplane/freeplane/commit/2602aa2bac81525841c03388e195f521427ed431) |
| 2018-10-21 | `fix` | Fix script editor dialog size for time management | `ScriptComboBoxEditor.java` | [5c340111](https://github.com/freeplane/freeplane/commit/5c3401110369e0c60ad462f91ef3296275daa5ec) |
| 2018-10-15 | `fix` | fix script plugin exported packages | `build.gradle` | [dc4b392d](https://github.com/freeplane/freeplane/commit/dc4b392d07c0ec287437b2dabab23686764c0d21) |
| 2018-10-15 | `fix` | Fix docu and names | `Dependencies.java`, `DependencyLookup.java` +8 | [82aecb58](https://github.com/freeplane/freeplane/commit/82aecb5843e6667536ba8ee0af2dba85eb060d46) |
| 2018-10-15 | `api_change` | getPrecendents() and getDependents() API | `NodeAttributeTableModel.java`, `Dependencies.java` +18 | [f273ade7](https://github.com/freeplane/freeplane/commit/f273ade7ab2c3a26633cf90e04af3c28c7093379) |
| 2018-10-15 | `fix` | fix it | `Activator.java`, `EvaluationDependencies.java` +1 | [1dbfc360](https://github.com/freeplane/freeplane/commit/1dbfc360b8d41c728b15f56078d78fa8a3816dde) |
| 2018-10-15 | `fix` | fix NPE | `RelatedElements.java` | [af24535b](https://github.com/freeplane/freeplane/commit/af24535bddd4b1cb983676a51399966cbae1e2ba) |
| 2018-10-07 | `fix` | Fix NPE for scripts executed without context | `AttributesProxy.java`, `ControllerProxy.java` +1 | [38c73a6a](https://github.com/freeplane/freeplane/commit/38c73a6a9f4d677f14463261341e8ca772d5b575) |
| 2018-10-06 | `fix` | bug fixes and improvements | `AttributeController.java`, `Connectors.java` +7 | [6afa6838](https://github.com/freeplane/freeplane/commit/6afa68387afa40da2e185e32d572a2e37225640e) |
| 2018-10-06 | `feature` | Add status message for cyclic dependencies | `CyclicScriptReferenceException.java`, `FormulaUtils.java` | [df4640e8](https://github.com/freeplane/freeplane/commit/df4640e80f935e072e33c5eeaf06ca7de92d4b78) |
| 2018-10-06 | `fix` | fix NPE | `EvaluateAllAction.java`, `FormulaCache.java` | [2cee80a0](https://github.com/freeplane/freeplane/commit/2cee80a0d196d041d43c8ad08ccdf32b806d5b5a) |
| 2018-10-05 | `fix` | fix NPE | `DependentsSearchStrategy.java`, `NodeScript.java` | [01e51f27](https://github.com/freeplane/freeplane/commit/01e51f27f41b3824a15d252df2dddfc28c3a4413) |
| 2018-10-03 | `fix` | fix eclipse compiler warning | `EvaluationDependencies.java` | [5b75d54e](https://github.com/freeplane/freeplane/commit/5b75d54edf0d3334106c7ce154051bf516fd718f) |
| 2018-09-04 | `api_change` | remove debug output from api genarator script | `apiGenerator.groovy` | [7614e8eb](https://github.com/freeplane/freeplane/commit/7614e8eb8beb2bb979afac7b1ba9669f8eec3d3f) |
| 2018-09-02 | `fix` | workaround for knopflerfish bug | `ScriptClassLoader.java` | [2188f6be](https://github.com/freeplane/freeplane/commit/2188f6bec50ae7575eaefdbfdaab976fbe223439) |
| 2018-08-31 | `feature` | add groovy-dateutil to runtime | `build.gradle` | [8aff5488](https://github.com/freeplane/freeplane/commit/8aff5488e01302d85243403bebd9f1db08d818c9) |
| 2018-08-30 | `api_change` | include Script to generated api mind map | `apiGenerator.groovy` | [fac2a2d0](https://github.com/freeplane/freeplane/commit/fac2a2d0046f727e3b20246317c40040aea19140) |
| 2018-08-21 | `feature` | Add "deny" button to quick filter | `build.gradle`, `Resources_af.properties` +46 | [a8a1253f](https://github.com/freeplane/freeplane/commit/a8a1253f5b0fbab1a0ecac9f3456a508ca351f8c) |
| 2018-08-19 | `api_change` | extend and document API | `HeadlessMapCreator.java`, `Script.java` +2 | [b322ea37](https://github.com/freeplane/freeplane/commit/b322ea37a0dad701ac72fdb3acac57ee85817977) |
| 2018-08-19 | `fix` | Fix scripting permissions and prepare scripts for multithreading | `ExecuteScriptAction.java`, `GenericScript.java` +10 | [f3e4c293](https://github.com/freeplane/freeplane/commit/f3e4c293074c8825a99ad8f30ad72f75b5724d3f) |
| 2018-07-31 | `api_change` | extend API | `Node.java`, `NodeRO.java` +1 | [e4bc8231](https://github.com/freeplane/freeplane/commit/e4bc82315c8d23f4500492dfa3113619c2b9ebd7) |
| 2018-07-21 | `feature` | support relative paths in maps loaded from scripts and formulas | `ScriptContext.java`, `ScriptCondition.java` +1 | [4cbc9e83](https://github.com/freeplane/freeplane/commit/4cbc9e8347ab9d8919ac56f7e0570d4df5372a1e) |
| 2018-07-19 | `fix` | Fix Proxy.Loader api | `apiGenerator.groovy`, `ControllerProxy.java` +2 | [1f809f2e](https://github.com/freeplane/freeplane/commit/1f809f2e2ac5fe48743778b9f8ced801312eb9be) |
| 2018-07-19 | `feature` | add new api to api mind map generation script | `EncryptedMap.java`, `MapController.java` +9 | [8a59e966](https://github.com/freeplane/freeplane/commit/8a59e96690a511eeeabc4a4ce6f52973c7eb73eb) |
| 2018-07-19 | `feature` | add new api to api mind map generation script | `EncryptedMap.java`, `MapController.java` +9 | [b5a9ac44](https://github.com/freeplane/freeplane/commit/b5a9ac442323435633992c52341446ecce2a3e0d) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [79de8564](https://github.com/freeplane/freeplane/commit/79de85641fe2c7d9cbb2ecc79238a18fa8b8ae18) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [bb1e7869](https://github.com/freeplane/freeplane/commit/bb1e78694778a47fff37f07484c283126847b8ed) |
| 2018-07-19 | `api_change` | MapLoader api and refactoring | `MapController.java`, `MapModel.java` +14 | [d2c45816](https://github.com/freeplane/freeplane/commit/d2c458160eb4a8a1bdb2004903315b5d7c20c444) |
| 2018-07-15 | `fix` | Fix repositories | `build.gradle`, `build.gradle` +1 | [3a488ae9](https://github.com/freeplane/freeplane/commit/3a488ae90e1bf614c2adcdbf5c9efebe4aab25ce) |
| 2018-07-15 | `fix` | Fix repositories | `build.gradle`, `build.gradle` | [28de04ff](https://github.com/freeplane/freeplane/commit/28de04ffc3d2747f50963b392289cf14dc922613) |
| 2018-07-11 | `api_change` | loader api | `Controller.java`, `HeadlessLoader.java` +5 | [b64c78d5](https://github.com/freeplane/freeplane/commit/b64c78d5c624e8a20c4c42aaac4063d42b7a6cc1) |
| 2018-07-08 | `api_change` | rename API methods newMap -> openMap, newMapFromTemplate -> openUntitledMap, hiddenMap ->  | `EncryptedMap.java`, `XmlImporter.java` +24 | [a76dc05a](https://github.com/freeplane/freeplane/commit/a76dc05a3fe1d4bb41c642401861949053f14b9e) |
| 2018-07-08 | `feature` | Add API method Controller.hiddenMap | `MMapController.java`, `MMapIO.java` +4 | [ba2c7706](https://github.com/freeplane/freeplane/commit/ba2c77064878fb9001a497a3467801cb7eb010f9) |
| 2018-07-03 | `feature` | create compiledScriptsDir on ScriptCompiler initialization | `ScriptCompiler.java` | [11a7e22c](https://github.com/freeplane/freeplane/commit/11a7e22c8b998916f358208d6445eb084e772358) |
| 2018-07-01 | `fix` | fix imports | `CompiledFiles.java` | [290284e9](https://github.com/freeplane/freeplane/commit/290284e90dd8ec7dbec53c2c78ccc8318a9a8a0e) |
| 2018-07-01 | `fix` | fix classpath | `ScriptingConfiguration.java` | [61bd5a19](https://github.com/freeplane/freeplane/commit/61bd5a190fd304bbafebdd1850d5e75b822ab382) |
| 2018-07-01 | `fix` | fix encoding | `CompiledFiles.java` | [12c8c313](https://github.com/freeplane/freeplane/commit/12c8c3136d974856acd2033e7f79bcd223f970f0) |
| 2018-07-01 | `fix` | fix tests | `CompiledFilesSpec.java` | [87c3ace5](https://github.com/freeplane/freeplane/commit/87c3ace53f81e9348b988bfb15faea3fb4fbe40d) |
| 2018-06-30 | `fix` | Fix compilation classpath for on start script compiler | `ScriptCompiler.java`, `ScriptingRegistration.java` | [e8a09958](https://github.com/freeplane/freeplane/commit/e8a099582375d82629f35fa493ead3c8f31d9fae) |
| 2018-06-30 | `fix` | Fix compilation classpath for on start script compiler | `ScriptCompiler.java`, `ScriptingRegistration.java` | [b53e5c71](https://github.com/freeplane/freeplane/commit/b53e5c71cbddb1158f6e88512377431c07141170) |
| 2018-06-19 | `api_change` | freeplane api package must not depend on any other freeplane packages | `build.gradle`, `Connector.java` +20 | [42e21482](https://github.com/freeplane/freeplane/commit/42e214828ff405b0a71adca6f169d13e290b58dd) |
| 2018-06-17 | `feature` | move api to core project and create api jar | `build.gradle`, `AttributeCondition.java` +33 | [4973e455](https://github.com/freeplane/freeplane/commit/4973e455f369a3f93bd3865c4bede8a274a28a71) |
| 2018-06-17 | `fix` | fix java7 compatibility | `NodeProxy.java` | [63750aa3](https://github.com/freeplane/freeplane/commit/63750aa39cfd945e9cd4cc09cf35b74e93d3be02) |
| 2018-05-30 | `feature` | Add docu for scripting Controller newHiddenMapFromTemplate | `Proxy.java` | [0ede2da5](https://github.com/freeplane/freeplane/commit/0ede2da5aca6938582f35c5163eb32f176491837) |
| 2018-05-30 | `feature` | add transformed attributes to the scripting api | `AttributesProxy.java`, `NodeProxy.java` +1 | [3e17ba14](https://github.com/freeplane/freeplane/commit/3e17ba142e9c4a1a8145449cb77d4a27b17ef26e) |
| 2018-05-30 | `feature` | add newHiddenMapFromTemplate method to controller scripting API | `MMapController.java`, `MMapIO.java` +2 | [257c29cc](https://github.com/freeplane/freeplane/commit/257c29cc40e4a33b4acf649af5b195c1bda0cd64) |

### Dettagli commit con note

**[1c2bf60f](https://github.com/freeplane/freeplane/commit/1c2bf60fed975616a95224f4425d4d197f51c46f)** (2018-12-31) — Revert "fix changing script permissions"

> This reverts commit 6a6e155b


---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-07-08 | `fix` | fix documentation of an API method | `Proxy.java` | [613e22ea](https://github.com/freeplane/freeplane/commit/613e22eaba3f5ee1ddea9c1b57adaf4efb40450a) |
| 2017-07-08 | `api_change` | Improve overloaded methods handling in API generator script | `build.gradle`, `apiGenerator.groovy` | [e94af1a7](https://github.com/freeplane/freeplane/commit/e94af1a74537ce8cfed967bc8690c11a273f7d1a) |
| 2017-07-08 | `feature` | Declare and document new attribute proxy methods in the interface | `Proxy.java` | [4571df77](https://github.com/freeplane/freeplane/commit/4571df77fd35d090c114235131b46cb717a09b01) |
| 2017-04-09 | `feature` | inline IconStoreFactory.create() | `FButtonBar.java`, `AttributeController.java` +14 | [16fcbdd5](https://github.com/freeplane/freeplane/commit/16fcbdd5b46e791b3a455ee577c2b05f0bd756f7) |
| 2017-04-08 | `api_change` | GroovyPatcher API changed | `GroovyScript.java` | [fff767c6](https://github.com/freeplane/freeplane/commit/fff767c62bf3169ec62374bdc7a1e4f45ad1d7be) |
| 2017-04-01 | `fix` | Use byte buddy to patch Groovy at run time | `build.gradle`, `CachedField.java` +7 | [da33365a](https://github.com/freeplane/freeplane/commit/da33365a40aeb685df6adecdf234d56b6fc8b71f) |
| 2017-04-01 | `fix` | Use byte buddy to patch Groovy at run time | `build.gradle`, `CachedField.java` +7 | [41b98fba](https://github.com/freeplane/freeplane/commit/41b98fbaf18d4324cf6f9c38f7a81eb6cd21b181) |
| 2017-03-19 | `feature` | Add checks for calls of class loader protected methods | `AccessPermissionChecker.java` | [738df903](https://github.com/freeplane/freeplane/commit/738df9037fb1df9f9a2c576f4ac0c0b8e2da0fda) |
| 2017-03-19 | `feature` | Add security checks | `CachedMethod.java` | [364b1b9c](https://github.com/freeplane/freeplane/commit/364b1b9c72f0b15070e32426e78c1f8297533bb8) |
| 2017-03-19 | `feature` | Add security checks | `CachedMethod.java` | [c5af25c9](https://github.com/freeplane/freeplane/commit/c5af25c91473e4920c5fb3e16e554743b461e48a) |
| 2017-03-04 | `fix` | Improve fix | `AccessPermissionChecker.java`, `CachedConstructor.java` +2 | [bc8140e9](https://github.com/freeplane/freeplane/commit/bc8140e9c11586b730d650799d37ce9740369eb1) |
| 2017-03-04 | `fix` | Improve fix | `AccessPermissionChecker.java`, `CachedConstructor.java` +2 | [5936013e](https://github.com/freeplane/freeplane/commit/5936013eb8a90290bd2ec194c886ae4b57a4e8da) |
| 2017-02-27 | `fix` | another attempt to fix security | `permissions.perm`, `GenericScript.java` +6 | [938043fa](https://github.com/freeplane/freeplane/commit/938043faef58905689a6a48fda0dc8b65a0ac246) |
| 2017-02-27 | `fix` | another attempt to fix security | `permissions.perm`, `GenericScript.java` +7 | [8155a6cc](https://github.com/freeplane/freeplane/commit/8155a6ccaf73db655db38450ca30c8b6b6a2b626) |
| 2017-02-26 | `fix` | Fix script security issue | `AFreeplaneAction.java`, `InternationalizedSecurityManager.java` +2 | [f74f473e](https://github.com/freeplane/freeplane/commit/f74f473e7300598a3338b78355e3468ccae5a024) |
| 2017-02-26 | `fix` | fix merge | `GroovyScript.java` | [532b4304](https://github.com/freeplane/freeplane/commit/532b430405cf6ab99c7fa8a659d85d6953e3840b) |
| 2017-02-26 | `fix` | Improve security fix: allow running scripts with restricted permissions | `GenericScript.java`, `GroovyScript.java` +3 | [0582930e](https://github.com/freeplane/freeplane/commit/0582930ee1ffda6b18d514ac7b24c0f6744a2bec) |
| 2017-02-25 | `fix` | Fix security issue # Conflicts: #	freeplane_plugin_script/src/main/java/org/freeplane/plug | `GroovyScript.java`, `ScriptSecurity.java` | [e2b31c70](https://github.com/freeplane/freeplane/commit/e2b31c704dac1162fbe731423e4e6c7d4a9cc983) |
| 2017-02-25 | `fix` | Fix security issue | `GroovyScript.java`, `ScriptSecurity.java` | [644cfb42](https://github.com/freeplane/freeplane/commit/644cfb42b38e84ec887e163381a3b5aa4342ba82) |
| 2017-02-21 | `fix` | Fix ContextClassLoader in GroovyScript | `GroovyScript.java` | [3992e887](https://github.com/freeplane/freeplane/commit/3992e88748719c026a9c21f754f8a8b7b1f29b77) |
| 2017-02-19 | `fix` | fix conditional style update for scripting conditions | `ASelectableCondition.java`, `ConditionalStyleModel.java` +1 | [634ca837](https://github.com/freeplane/freeplane/commit/634ca83721e890be6d5a8dfcca807a87e9ae3a48) |
| 2017-02-18 | `fix` | fix StringIndexOutOfBoundsException | `ScriptCondition.java` | [fd40a1c6](https://github.com/freeplane/freeplane/commit/fd40a1c67a752ba3af4955fc65cbcba3cfd1a8db) |
| 2017-02-18 | `fix` | fix StringIndexOutOfBoundsException | `ScriptCondition.java` | [8c9d42e7](https://github.com/freeplane/freeplane/commit/8c9d42e7db8686bca38d3ea3d6d9661a0954e752) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-16 | `fix` | Bug fix #2430 workaround for image URL redirects | `InternationalizedSecurityManager.java` | [051ba456](https://github.com/freeplane/freeplane/commit/051ba456ee29ca9df1f78d07a2072fdac2a59eb1) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [2e38286e](https://github.com/freeplane/freeplane/commit/2e38286e3b35f58e558c329073a1eba35640d9c7) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [096fbd1f](https://github.com/freeplane/freeplane/commit/096fbd1f116b38edc7648618cf2c5e45bcd7b536) |
| 2016-10-03 | `fix` | fix all javadoc errors and some of the warnings | `Proxy.java` | [df0f8af6](https://github.com/freeplane/freeplane/commit/df0f8af63ab78d8710c1301ce666192b75332d01) |
| 2016-10-03 | `fix` | fix all javadoc warnings and errors | `Convertible.java` | [7a866c96](https://github.com/freeplane/freeplane/commit/7a866c96a71a15e97083558f8cc28dcdfbdac80a) |
| 2016-08-18 | `feature` | fix missing parseFreeplaneVersion() | `installScriptAddOn.groovy` | [b89c27a9](https://github.com/freeplane/freeplane/commit/b89c27a9739565de6a256623afc6c2493aa4521d) |
| 2016-08-15 | `feature` | add and call onApplicationStopped method to ApplicationLifecycleListener | `Controller.java`, `ApplicationLifecycleListener.java` +3 | [50e37859](https://github.com/freeplane/freeplane/commit/50e37859cb3001c3468fa904b4b56370aceb8796) |
| 2016-07-24 | `feature` | add documentation for Connector.source and target | `Proxy.java` | [02a05a43](https://github.com/freeplane/freeplane/commit/02a05a43685cbe7034fa987a07c7881614bb3a05) |
| 2016-07-23 | `fix` | Fix java.security.AccessControlException for formulas | `GroovyScript.java` | [255c8dc9](https://github.com/freeplane/freeplane/commit/255c8dc97d3e9dcfabd3312a76245b34b99893e0) |
| 2016-07-23 | `feature` | add documentation for connector source and target | `Proxy.java` | [b7a6a4b8](https://github.com/freeplane/freeplane/commit/b7a6a4b8eaaf26c3d76f9579874cc1d9990dcf8b) |
| 2016-06-26 | `api_change` | Remove bad web link from API map | `apiGenerator.groovy` | [0ffeb125](https://github.com/freeplane/freeplane/commit/0ffeb12577b9b199ea07da48e1e99703dff3ef35) |
| 2016-06-26 | `api_change` | Use old template standard.mm for API generator | `apiGenerator.groovy` | [43771d35](https://github.com/freeplane/freeplane/commit/43771d35016eb28f858c43d75e75e097efeba661) |
| 2016-06-26 | `feature` | Add method newMapFromTemplate to controller proxy | `MMapIO.java`, `ControllerProxy.java` +1 | [84413751](https://github.com/freeplane/freeplane/commit/844137510fbd4c4a3fb7dfa45966b34716d3d28d) |
| 2016-05-29 | `feature` | Support look and feels installed by users | `OptionPanelBuilder.java`, `ClassLoaderFactory.java` +4 | [5804b7ad](https://github.com/freeplane/freeplane/commit/5804b7adaa1c28bfa5b5c75fbc3395cb082ec57d) |
| 2016-05-08 | `feature` | add permission to read protectionDomain for all scripts | `ScriptingPolicy.java` | [a1fe8a67](https://github.com/freeplane/freeplane/commit/a1fe8a6707460e5ddb02fd9813dca6239e09b096) |
| 2016-04-25 | `feature` | Add RuntimePermission("exitVM.0") for all scripts | `ScriptingPolicy.java` | [608a9fef](https://github.com/freeplane/freeplane/commit/608a9fefbd8a5d4fef14abf8bc1d0b4790fea924) |
| 2016-04-24 | `feature` | revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations) | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943) |
| 2016-04-24 | `feature` | avoid all translation warnings for add-ons | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c) |
| 2016-04-23 | `feature` | Add RuntimePermission("setIO") for all scripts | `ScriptingPolicy.java` | [c1e10d97](https://github.com/freeplane/freeplane/commit/c1e10d977a1176d08139d312b3eab9699913b1bd) |
| 2016-04-16 | `feature` | permissions.add(new PropertyPermission("*", "read,write")); if (pWithoutWriteRestriction)  | `ScriptingPolicy.java`, `ScriptingSecurityManager.java` | [1d1c1561](https://github.com/freeplane/freeplane/commit/1d1c15618a1574d64b48702e87c837b91ee45a24) |
| 2016-04-12 | `feature` | Add some permissions to scripts | `ScriptingPolicy.java` | [25dc0abb](https://github.com/freeplane/freeplane/commit/25dc0abba03fa81b24a7091653ab8b7d5f948b4a) |
| 2016-04-10 | `fix` | Fix some bugs related to security checks | `build.gradle`, `ReportGenerator.java` +2 | [0ee6aef1](https://github.com/freeplane/freeplane/commit/0ee6aef160140dd19c6c2e71588de8a221751604) |
| 2016-04-10 | `feature` | added init script facility | `Controller.java`, `ApplicationLifecycleListener.java` +4 | [7d88585d](https://github.com/freeplane/freeplane/commit/7d88585dfd029e48fe3e62ee8f0aa89e1f0b6271) |
| 2016-04-09 | `fix` | fix ambiguity with operators in groovy (thanks to Gergely Papp) | `installScriptAddOn.groovy` | [1762d5b8](https://github.com/freeplane/freeplane/commit/1762d5b8a90cf900ed954d4444087e50efa06c07) |
| 2016-03-30 | `fix` | Fix security exceptions in java script engine | `InternationalizedSecurityManager.java`, `PrivilegedURLClassLoader.java` | [ffd1b697](https://github.com/freeplane/freeplane/commit/ffd1b6973b3a4f38b4ab40472dc5a3108fc92d2d) |
| 2016-03-30 | `fix` | Fix security exceptions in java script engine | `GenericScript.java`, `InternationalizedSecurityManager.java` +1 | [2a95745a](https://github.com/freeplane/freeplane/commit/2a95745a9e1bef2ceea0c98541b1bdbdb9fd5a88) |
| 2016-03-28 | `fix` | Fix URLPermission | `SecureRunner.java`, `ScriptingSecurityManager.java` | [46a4c4d6](https://github.com/freeplane/freeplane/commit/46a4c4d680dbfcccb9c4e79c80d4c1553aa5f4df) |
| 2016-03-28 | `api_change` | Remove warnings: do not use internal API constants | `ScriptingSecurityManager.java` | [399d21b6](https://github.com/freeplane/freeplane/commit/399d21b6ad6f5479928298e7973d5145ebf2d86c) |
| 2016-03-27 | `fix` | Fix scripting security issues | `FreeplaneGUIStarter.java`, `FreeplaneSecurityManager.java` +6 | [1490c603](https://github.com/freeplane/freeplane/commit/1490c603c9c143273ca31f118a63cec049c24a3c) |
| 2016-03-26 | `fix` | fix javadoc internal links | `Proxy.java` | [339c1704](https://github.com/freeplane/freeplane/commit/339c17046d8fe98ac7124dcc9e741154eaca192c) |
| 2016-02-20 | `feature` | Fix new node size calculation for nodes moved in scripts | `NodeProxy.java` | [9d24fcdd](https://github.com/freeplane/freeplane/commit/9d24fcdd3eb97775a6615fbbbcbefacfe32a39fa) |
| 2016-02-19 | `fix` | Fix MapProxy | `MapProxy.java` | [d59902aa](https://github.com/freeplane/freeplane/commit/d59902aa65d1b132afe21afdae87896811f6f89d) |
| 2016-01-24 | `feature` | add quantity setter methods to NodeProxy | `NodeProxy.java`, `Proxy.java` | [ad2ad315](https://github.com/freeplane/freeplane/commit/ad2ad315063778611637ddc82b2c0f66f03dda1e) |
| 2016-01-23 | `fix` | Fix class cast exception | `ProxyUtils.java` | [66860a95](https://github.com/freeplane/freeplane/commit/66860a95e4e5d900a4ff1be51e1a09eed6523501) |
| 2016-01-20 | `fix` | correct appendAsCloneWith(out)Subtree(): with and without were mixed up | `NodeProxy.java` | [50edb372](https://github.com/freeplane/freeplane/commit/50edb3726347e537e14662e06d1fff32b5ea737e) |
| 2016-01-03 | `api_change` | make counts of clones and the clones itself accessible via the scripting API | `NodeProxy.java`, `Proxy.java` | [4869f3cd](https://github.com/freeplane/freeplane/commit/4869f3cd0335481739c52728e0c8cea9ab9df770) |

### Dettagli commit con note

**[b89c27a9](https://github.com/freeplane/freeplane/commit/b89c27a9739565de6a256623afc6c2493aa4521d)** (2016-08-18) — fix missing parseFreeplaneVersion()

> for allowing the install of add-ons in 1.5.15+.  Discussed in https://sourceforge.net/p/freeplane/discussion/758437/thread/12897ed2/

**[7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943)** (2016-04-24) — revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations)

> will use a different approach

**[ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c)** (2016-04-24) — avoid all translation warnings for add-ons

> Translations of add-ons are often missing. To make them look nicer
> in the GUI we'll cut all warnings about missing keys for add-ons
> and erase the [translate me] suffix

**[7d88585d](https://github.com/freeplane/freeplane/commit/7d88585dfd029e48fe3e62ee8f0aa89e1f0b6271)** (2016-04-10) — added init script facility

> Scripts in <freeplaneuserdir>/scripts/init are executed after application startup
> i.e. after initialization of the gui (including opening of last maps etc.)
> 
> New ApplicationLifecycleListener are registered in the Controller to be
> executed after startup.

**[66860a95](https://github.com/freeplane/freeplane/commit/66860a95e4e5d900a4ff1be51e1a09eed6523501)** (2016-01-23) — Fix class cast exception

> java.lang.ClassCastException:
> org.freeplane.plugin.script.proxy.ProxyUtils$2 cannot be cast to
> org.freeplane.features.filter.condition.ASelectableCondition
> 	at
> org.freeplane.features.filter.FilterController.getSelectedCondition(FilterController.java:441)


---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-31 | `api_change` | extend scripting API for clones: Node appendAsClone(NodeRO toBeCloned) Node appendAsCloneW | `history_en.txt`, `NodeProxy.java` +1 | [a17d677c](https://github.com/freeplane/freeplane/commit/a17d677c368f7c040613c332be16a0f776cb79d7) |
| 2015-12-23 | `feature` | Display add-on menu item locations | `build.gradle`, `EntryAccessor.java` +4 | [1abc7f18](https://github.com/freeplane/freeplane/commit/1abc7f18f501de5541aa2cb904d7429fbe68ea17) |
| 2015-12-23 | `feature` | Build formatted menu location for add-on details | `EntryAccessor.java`, `EntryAccessorTest.java` +1 | [a4f21706](https://github.com/freeplane/freeplane/commit/a4f217063d067d2c3afeb6cc0146beb748616444) |
| 2015-11-29 | `fix` | fix exception on updateMenus occuring if no scripts are available | `ExecutionModeSelector.java`, `ScriptingMenuEntryVisitor.java` | [677b4d53](https://github.com/freeplane/freeplane/commit/677b4d53db38337ab10701b5092ec7459fdb2afd) |
| 2015-11-29 | `feature` | ensure that for each script exactly one menu entry is shown | `mindmapmode.generic.xml`, `ExecuteScriptAction.java` +3 | [0d61af06](https://github.com/freeplane/freeplane/commit/0d61af06534d34c7a5f840b529bc7fa85297be57) |
| 2015-11-29 | `api_change` | Delete unused interface with only one implementation class | `PhaseProcessor.java`, `Processor.java` +3 | [a000f382](https://github.com/freeplane/freeplane/commit/a000f38230d8f4126079453e6b9745c548e40be3) |
| 2015-11-29 | `feature` | add an alias for node_popup_scripting that may be in use by add-ons | `ScriptingMenuEntryVisitor.java` | [ae553faf](https://github.com/freeplane/freeplane/commit/ae553faf775310d9f355e2f6b012b8a9e8b9bea8) |
| 2015-11-29 | `feature` | capitalize submenu names created for add-ons and scripts | `ScriptingMenuUtils.java` | [1a4e253d](https://github.com/freeplane/freeplane/commit/1a4e253d07fee7d933ce95e1ca448cfc3d04c397) |
| 2015-11-29 | `feature` | implement scripting and add-on menus | `ScriptingConfiguration.java`, `ScriptingMenuEntryVisitor.java` +2 | [38e3e0d5](https://github.com/freeplane/freeplane/commit/38e3e0d5321bd4b5b3d031ece6522505e24d384a) |
| 2015-11-09 | `feature` | add tooltips | `ScriptingMenuEntryVisitor.java` | [f3cf0a5b](https://github.com/freeplane/freeplane/commit/f3cf0a5b4c98ae6f426c572e93efac8efbf638ac) |
| 2015-11-09 | `feature` | add tooltips | `ScriptingMenuContributor.java`, `ScriptingRibbonsContributorFactory.java` | [b4aa1071](https://github.com/freeplane/freeplane/commit/b4aa1071ef22555c2b4570f4594a99e6716a54e8) |
| 2015-11-09 | `feature` | add static import | `ScriptingMenuEntryVisitor.java` | [db924e71](https://github.com/freeplane/freeplane/commit/db924e7140076fbaaafd0f32e8bd8e4dbd2631d0) |
| 2015-11-08 | `feature` | Script Actions Builder for new UI | `mindmapmode.generic.xml`, `ExecutionModeSelector.java` +2 | [91b92cfb](https://github.com/freeplane/freeplane/commit/91b92cfb4e3d5ade5a140a49305aba09b62cd0c5) |
| 2015-11-08 | `api_change` | deprecate old menu/ribbon builders | `ScriptingMenuContributor.java`, `ScriptingRibbonsContributor.java` | [7c4dab94](https://github.com/freeplane/freeplane/commit/7c4dab9405bc634e818eab9392261c9acba91eb6) |
| 2015-11-08 | `fix` | fix parse error | `Proxy.java` | [a06c8d25](https://github.com/freeplane/freeplane/commit/a06c8d2546e3e437df0b64ead4a1eea6434dbf15) |
| 2015-11-08 | `fix` | fix first part of the depth-/breath-first confusion | `Proxy.java` | [f0430c38](https://github.com/freeplane/freeplane/commit/f0430c383dbf87e02f0e603c17cdec024d02ee2e) |
| 2015-11-08 | `feature` | scripting API: add Node.sortChildrenBy(Closure) | `NodeProxy.java`, `Proxy.java` | [77c0690d](https://github.com/freeplane/freeplane/commit/77c0690d7f3a07480ec9dd539a155df3670dcb97) |
| 2015-11-08 | `feature` | scripting API: add Icons.addAll(names) and Icons.addAll(Icons) | `IconsProxy.java`, `Proxy.java` | [c4b146d4](https://github.com/freeplane/freeplane/commit/c4b146d49042d52979a40e35248940f2ce733402) |
| 2015-11-08 | `feature` | scripting API: add Controller.getOpenMaps() | `ControllerProxy.java`, `Proxy.java` | [460b4cd6](https://github.com/freeplane/freeplane/commit/460b4cd6d2ccc07d19e0a08743e4059cc90b2df8) |
| 2015-09-05 | `api_change` | removed more old ribbon api calls | `RibbonActionComponentProvider.java`, `FreeplaneGUIStarter.java` +4 | [7f82b617](https://github.com/freeplane/freeplane/commit/7f82b6170eca0e86f447f21f02241d106532a546) |
| 2015-06-07 | `api_change` | Scripting API: - Added NodeRO.getHtmlText() - improved documentation of many node core rel | `NodeProxy.java`, `Proxy.java` | [e87a89a0](https://github.com/freeplane/freeplane/commit/e87a89a003184e2992337c18851e1a92f1864804) |
| 2015-05-14 | `feature` | implement node.attributes.optimizeWidths() | `AttributesProxy.java`, `Proxy.java` | [7a4c78b1](https://github.com/freeplane/freeplane/commit/7a4c78b1a6708bb3a5110da7154276d3f5339536) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-03 | `api_change` | generate javadoc only for scripting interface | `build.gradle`, `build.gradle` | [9bac0e72](https://github.com/freeplane/freeplane/commit/9bac0e72bea288cf024df6aa573e83d42d5b5bee) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a maven repo, a | `MANIFEST.MF`, `build.gradle` +24 | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |
| 2015-01-01 | `feature` | add jgoodies-forms/commons, move some java files from src/ to src/main/java | `build.gradle`, `ConditionSnapshotFactory.java` +15 | [bc062b52](https://github.com/freeplane/freeplane/commit/bc062b5210d694fba72d6ad405bdb0ed04a736ed) |
| 2015-01-01 | `feature` | new plugin 'freeplane_plugin_jsp' for jsyntaxpane including LaTeX enhancements (used by sc | `build.gradle`, `jsyntaxpane.jar` +12 | [27d69c29](https://github.com/freeplane/freeplane/commit/27d69c296ad8d456419913697dff5d0e598c01da) |

### Dettagli commit con note

**[0d61af06](https://github.com/freeplane/freeplane/commit/0d61af06534d34c7a5f840b529bc7fa85297be57)** (2015-11-29) — ensure that for each script exactly one menu entry is shown

> Each script is registered for one or more execution modes but no
> matter if a matching execution mode is selected/active or not a
> menu entry must represent the script. To implement that the following
> measures are taken:
> 
> * For each available execution mode a menu entry is added to the menu
> * Initially and on every execution mode selection change all script
>   entries are made invisible that are not selected. If this would make
>   the script completely invisible, one of the invisible entries are
>   made a) visible and b) disabled
> 
> Having entries for all execution modes is also important to enable
> keyboard shortcuts even for the invisible scripts

**[38e3e0d5](https://github.com/freeplane/freeplane/commit/38e3e0d5321bd4b5b3d031ece6522505e24d384a)** (2015-11-29) — implement scripting and add-on menus

> Some problems remains. At least the scripting API is not placed right


---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-12-26 | `feature` | add zipJavadoc task to scripting plugin | `build.gradle` | [80cf5f1b](https://github.com/freeplane/freeplane/commit/80cf5f1b56d8fff435fe55c58ed2f2ec9fbe9079) |
| 2014-12-14 | `api_change` | Scripting API extensions: - Controller.select(Collection<Node>) - Link.remove() . Attribut | `history_en.txt`, `AttributesProxy.java` +3 | [b2b204b4](https://github.com/freeplane/freeplane/commit/b2b204b408978c327a139ac1538f8d1f5cb1084a) |
| 2014-09-08 | `fix` | fix bug #2186: use fixed locale for toUpperCase to cope with the http://mattryall.net/blog | `ScriptAddOnProperties.java` | [0441e4fc](https://github.com/freeplane/freeplane/commit/0441e4fcf17bcc5a91c4964ae990b65307b61895) |
| 2014-09-08 | `fix` | fix bug #2186: use fixed locale for toUpperCase to cope with the http://mattryall.net/blog | `ScriptAddOnProperties.java` | [6a216022](https://github.com/freeplane/freeplane/commit/6a21602245d33c29f95ce41a43289bf75122eb3d) |
| 2014-07-26 | `fix` | JSyntaxPane: Fix a javascript problem with java8 (error popup when starting the formula ed | `jsyntaxpane.jar` | [8a019f3c](https://github.com/freeplane/freeplane/commit/8a019f3c49631ed122e9e2028bbae5c302d80d13) |
| 2014-06-04 | `feature` | new Date().getTime() -> System.currentTimeMillis() | `TimeConditionController.java`, `ReminderConditionController.java` +1 | [c604f332](https://github.com/freeplane/freeplane/commit/c604f332fcec752038d5b36a9d0755e698f1e0b2) |
| 2014-05-06 | `feature` | fix abt build for freeplane_plugin_script : add insubstantial.jars to classpath | `build.xml` | [725ebde5](https://github.com/freeplane/freeplane/commit/725ebde5df1c14e70fc751096d87a5ddc3a18be1) |
| 2014-04-24 | `fix` | #2140: fix file filter for .groovy files to compile | `ScriptCompiler.java` | [cd689adb](https://github.com/freeplane/freeplane/commit/cd689adb61a3db117ba08d52fa45464133657fe2) |
| 2014-04-24 | `fix` | #2140: fix file filter for .groovy files to compile | `ScriptCompiler.java` | [ad027978](https://github.com/freeplane/freeplane/commit/ad0279789532a42ba5e09250791fbb52c2eeb856) |
| 2014-04-09 | `fix` | fix NPE | `ConvertibleTest.java` | [9a376942](https://github.com/freeplane/freeplane/commit/9a376942554eb27f4071563b492ac25930108f5f) |
| 2014-04-09 | `feature` | #2126:  - ensure that no exception occurs on node.details and node.note  - implement both, | `FormulaUtils.java`, `ConvertibleHtmlText.java` +4 | [39c16277](https://github.com/freeplane/freeplane/commit/39c1627709760189f6f63f6df8b4f8fd5d660036) |
| 2014-04-09 | `feature` | #2126:  - ensure that no exception occurs on node.details and node.note  - implement both, | `FormulaUtils.java`, `ConvertibleHtmlText.java` +4 | [58a6ae86](https://github.com/freeplane/freeplane/commit/58a6ae8689a94a8eaf7ec4385d43ac886a1dc546) |
| 2014-03-21 | `feature` | add property node.style.numberingEnabled | `NodeStyleProxy.java`, `Proxy.java` | [01f835d4](https://github.com/freeplane/freeplane/commit/01f835d4b60521c3991267fba969544f7367e9dd) |
| 2014-03-21 | `feature` | add property node.style.numberingEnabled | `NodeStyleProxy.java`, `Proxy.java` | [d51820b6](https://github.com/freeplane/freeplane/commit/d51820b6e24677b8dc81f769ba741cf760b148a0) |
| 2014-03-18 | `fix` | fix #2109: script assert error does not show stack | `ExecuteScriptAction.java` | [b655cf98](https://github.com/freeplane/freeplane/commit/b655cf98305643fa228e7fd61e6af72f66e365c2) |
| 2014-03-11 | `fix` | Fix: Two writers for the same stream. | `GenericScript.java` | [9f8030bb](https://github.com/freeplane/freeplane/commit/9f8030bbe42bbc0a24e6d5105263ffd23a6bb22e) |
| 2014-03-11 | `fix` | Fix: stdout not set in generic scripts. | `GenericScript.java`, `GroovyScript.java` | [b88f2212](https://github.com/freeplane/freeplane/commit/b88f221256708b6fdd3114ec82b33fe6909da1be) |
| 2014-03-11 | `fix` | Fix: stdout not set in generic scripts. | `GenericScript.java`, `GroovyScript.java` | [7d81a17b](https://github.com/freeplane/freeplane/commit/7d81a17bc9f2cab33048e902ef8798391aabfa0d) |
| 2014-03-11 | `fix` | Fix code-indent. | `GenericScript.java` | [ae37e7cc](https://github.com/freeplane/freeplane/commit/ae37e7cc76641998f20a42262ce14cf3505b754d) |
| 2014-03-11 | `fix` | Fix code-indent. | `GenericScript.java` | [fbde5769](https://github.com/freeplane/freeplane/commit/fbde5769c462053733cd6c95426752b56810102b) |
| 2014-03-11 | `fix` | Fix: Once a groovy script has a compiletime error, it's never compiled again. | `CompileTimeStrategy.java`, `GenericScript.java` +1 | [80c55a44](https://github.com/freeplane/freeplane/commit/80c55a44a324e120f2690249f2d44bc89018ad6e) |
| 2014-03-11 | `fix` | Fix: Once a groovy script has a compiletime error, it's never compiled again. | `CompileTimeStrategy.java`, `GenericScript.java` +1 | [ea2b89bb](https://github.com/freeplane/freeplane/commit/ea2b89bb84e0b0301725846be2acb254074aefce) |
| 2014-03-09 | `fix` | #2109: partial fix: log groovy execution exception when running from script editor panel | `ScriptEditorPanel.java` | [ae6a9680](https://github.com/freeplane/freeplane/commit/ae6a96807657476e2c071ee4e88d423268754f83) |
| 2014-03-01 | `feature` | implement node proxy properties horizontalShift, verticalShift and minimalDistanceBetweenC | `LocationController.java`, `ChangeShiftXActor.java` +5 | [d36a6822](https://github.com/freeplane/freeplane/commit/d36a68223bcefa725299da48b5da1430f05255f6) |
| 2014-02-25 | `feature` | #2110: let add-on paths take a higher precedence than userlibs | `ScriptingConfiguration.java` | [2b8e68cb](https://github.com/freeplane/freeplane/commit/2b8e68cbbfc88e33ee47f1903420a64f3237096c) |
| 2014-02-25 | `feature` | #2110: let add-on paths take a higher precedence than userlibs | `ScriptingConfiguration.java` | [257ec6dd](https://github.com/freeplane/freeplane/commit/257ec6dd5250a9b79d665b2e31e3d9ae4290c8cc) |

### Dettagli commit con note

**[b88f2212](https://github.com/freeplane/freeplane/commit/b88f221256708b6fdd3114ec82b33fe6909da1be)** (2014-03-11) — Fix: stdout not set in generic scripts.

> Thus `print` was not working in e.g Python scripts.
> 
> Conflicts:
> 	freeplane_plugin_script/src/org/freeplane/plugin/script/GenericScript.java

**[7d81a17b](https://github.com/freeplane/freeplane/commit/7d81a17bc9f2cab33048e902ef8798391aabfa0d)** (2014-03-11) — Fix: stdout not set in generic scripts.

> Thus `print` was not working in e.g Python scripts.

**[ae37e7cc](https://github.com/freeplane/freeplane/commit/ae37e7cc76641998f20a42262ce14cf3505b754d)** (2014-03-11) — Fix code-indent.

> I did not put this into the last commit to reduce number of changes.
> 
> Conflicts:
> 	freeplane_plugin_script/src/org/freeplane/plugin/script/GenericScript.java

**[fbde5769](https://github.com/freeplane/freeplane/commit/fbde5769c462053733cd6c95426752b56810102b)** (2014-03-11) — Fix code-indent.

> I did not put this into the last commit to reduce number of changes.

**[80c55a44](https://github.com/freeplane/freeplane/commit/80c55a44a324e120f2690249f2d44bc89018ad6e)** (2014-03-11) — Fix: Once a groovy script has a compiletime error, it's never compiled again.

> This includes changes:
> - In execute(), re-raise existing errors only if the scrips has not
>   changed.
> - For this to work: reset ``compileTime`` prior to compiling the script.
>   (Otherwise canUseOldCompiledScript() could not be run in execute() due
>   to it integrated check-delay.)
> - Clear ``errorsInScript`` prior to compiling. (Instead of not compiling,
>   at all if ``errorsInScript are set.)
> - Same changes for GenericScript.
> 
> Conflicts:
> 	freeplane_plugin_script/src/org/freeplane/plugin/script/GenericScript.java

**[ea2b89bb](https://github.com/freeplane/freeplane/commit/ea2b89bb84e0b0301725846be2acb254074aefce)** (2014-03-11) — Fix: Once a groovy script has a compiletime error, it's never compiled again.

> This includes changes:
> - In execute(), re-raise existing errors only if the scrips has not
>   changed.
> - For this to work: reset ``compileTime`` prior to compiling the script.
>   (Otherwise canUseOldCompiledScript() could not be run in execute() due
>   to it integrated check-delay.)
> - Clear ``errorsInScript`` prior to compiling. (Instead of not compiling,
>   at all if ``errorsInScript are set.)
> - Same changes for GenericScript.


---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [62e125b3](https://github.com/freeplane/freeplane/commit/62e125b331c29ae0c3962a3b0d27e0342bcc18ee) |
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [2c986d3a](https://github.com/freeplane/freeplane/commit/2c986d3abd50356b5bf63f28fb97347deb0cf4e3) |
| 2013-11-16 | `api_change` | upgrade groovy to 2.1.9 | `groovy-all.jar` | [9e1861f4](https://github.com/freeplane/freeplane/commit/9e1861f4a64adbe3c38358479cc335ab6d9ad19f) |
| 2013-10-30 | `feature` | Add a comment about some code never reached. | `GenericScript.java` | [e17f8c37](https://github.com/freeplane/freeplane/commit/e17f8c379104aa1f5383e905df559481ec407fcb) |
| 2013-10-29 | `fix` | Fix: Nullpointer-Exceptions in script filters are not reported properly. | `ScriptCondition.java` | [c464435e](https://github.com/freeplane/freeplane/commit/c464435e27d089e286a6c1d058dcc095095b8064) |
| 2013-09-29 | `fix` | fix ant build files | `build.xml`, `build.xml` +1 | [2c367ac7](https://github.com/freeplane/freeplane/commit/2c367ac7b92941a6841c7f3055a9262fb63b8f21) |
| 2013-07-28 | `feature` | Scripting/other languages: * new configuration options:   - script_compilation_disabled_ex | `Resources_de.properties`, `Resources_en.properties` +10 | [2e24f90d](https://github.com/freeplane/freeplane/commit/2e24f90d20f9f3025c4910a675c48fce88cb644f) |
| 2013-07-25 | `fix` | fix incorrect use of IScript.CACHE_COMPILED_SCRIPTS | `GenericScript.java` | [d45612de](https://github.com/freeplane/freeplane/commit/d45612de74b5e881b0601b8b4feed030e76995dd) |
| 2013-07-23 | `feature` | - refactoring: renamings - implement registration of non-groovy scripts | `GenericFreeplaneScript.java`, `GenericScript.java` +8 | [a341f93e](https://github.com/freeplane/freeplane/commit/a341f93e5e85e89c44bc411b4065a2a3e3d6bdc1) |
| 2013-07-01 | `api_change` | scripting API for map specific storage | `history_en.txt`, `MapStyle.java` +3 | [8085eff2](https://github.com/freeplane/freeplane/commit/8085eff229490b889722ed5f47071bee8affd8be) |
| 2013-06-30 | `feature` | new method Convertible.getBool() adds explicit conversion to boolean | `Convertible.java`, `ConvertibleTest.java` | [5808bd4f](https://github.com/freeplane/freeplane/commit/5808bd4f9cbc0991e94ddab97bf81debbe66d327) |
| 2013-06-30 | `api_change` | scripting API for encrypted nodes refactored EncryptionController to remove direct Swing r | `history_en.txt`, `EncryptionController.java` +7 | [324ee6f1](https://github.com/freeplane/freeplane/commit/324ee6f16aee4c25806e3fbca2255029e19154cb) |
| 2013-06-12 | `api_change` | preliminary scripting api for exports | `ControllerProxy.java`, `Proxy.java` | [0f493ee7](https://github.com/freeplane/freeplane/commit/0f493ee7bae0c3e8934e4500c746e2c43f2808be) |
| 2013-06-04 | `feature` | Add .gitignore for the `preferences.xml` files which are now built. | `.gitignore`, `.gitignore` | [8203c0a0](https://github.com/freeplane/freeplane/commit/8203c0a029ff7a2eebd17317a9badeb2715ccde3) |
| 2013-05-10 | `feature` | scripting api: add node.icons.clear() like node.attributes.clear() | `IconsProxy.java`, `Proxy.java` | [ce7d7593](https://github.com/freeplane/freeplane/commit/ce7d759343bda70a0d6397203d0b5a347c561760) |
| 2013-04-21 | `fix` | fix NPE in case of formulas that have scripting proxy lists as an result. In this case Nod | `FormulaUtils.java`, `ScriptContext.java` | [354c49f3](https://github.com/freeplane/freeplane/commit/354c49f3e3364a3a16991613f280c9094acc6313) |
| 2013-04-13 | `feature` | merge workspace into freeplane/master | `.project`, `.project` +206 | [d91f421e](https://github.com/freeplane/freeplane/commit/d91f421e91cb3746577290e87e8a016462783cdd) |
| 2013-04-12 | `feature` | Scripting API: add Node.getPathToRoot() | `NodeProxy.java`, `Proxy.java` | [d1de0404](https://github.com/freeplane/freeplane/commit/d1de040422850654fce0098fd371abd44b72e76c) |
| 2013-04-07 | `feature` | new utility class ScriptUtils | `build.xml`, `apiGenerator.groovy` +1 | [447f41fa](https://github.com/freeplane/freeplane/commit/447f41fad33a68c3c9060c8d4624209cc682a7fe) |
| 2013-04-02 | `fix` | fix array out of bounds problem | `ConnectorProxy.java` | [ecd3023c](https://github.com/freeplane/freeplane/commit/ecd3023c565aa541ddc0f03b7748bbed727f4955) |
| 2013-04-02 | `feature` | new: Proxy.Connector.get{Start,End}Inclination, setInclination(start, end) | `ConnectorProxy.java`, `Proxy.java` | [7c8cd7ea](https://github.com/freeplane/freeplane/commit/7c8cd7ea7887d95b81c871d876ca5f36863b4984) |
| 2013-03-31 | `feature` | fix compilation of scripts in the script's classpath: - find .groovy files recursively - c | `.classpath`, `build.xml` +1 | [adc7a601](https://github.com/freeplane/freeplane/commit/adc7a601fff695c86d3c2f0ba8667b30d6854cef) |
| 2013-03-12 | `fix` | fix html syntax error | `overview.html` | [2bb8de26](https://github.com/freeplane/freeplane/commit/2bb8de2614079d76a888af2b3f785465b5d80b48) |
| 2013-03-11 | `api_change` | merged from master: scripting API documentation improvements | `MenuUtils.java`, `build.xml` +2 | [72ee848d](https://github.com/freeplane/freeplane/commit/72ee848d04da65d52cd2137a6600a09e2929ffa2) |
| 2013-03-11 | `api_change` | scripting API documentation improvements | `MenuUtils.java`, `build.xml` +2 | [25ee5ed4](https://github.com/freeplane/freeplane/commit/25ee5ed4dbc4fe1eada624606dcab1c6fd042007) |
| 2013-02-24 | `feature` | add node.externalObject.file = <file> | `ExternalObjectProxy.java`, `Proxy.java` | [75e1eb58](https://github.com/freeplane/freeplane/commit/75e1eb58220a8fd9ce0882c229f0299249cfc227) |
| 2013-02-24 | `feature` | #1909: make setting of node.externalObject.uri work even for new nodes | `ExternalObjectProxy.java` | [c15d0b3f](https://github.com/freeplane/freeplane/commit/c15d0b3f5d0e3592bd774592d67d5a6abc642aeb) |
| 2013-02-24 | `feature` | #1909: make setting of node.externalObject.uri work even for new nodes | `ExternalObjectProxy.java` | [245cbb62](https://github.com/freeplane/freeplane/commit/245cbb625c3ba53f72a525af47ebe43e5dce9b82) |
| 2013-02-24 | `fix` | fix: execute script without asking option not saved properly | `ScriptingEngine.java` | [ff276866](https://github.com/freeplane/freeplane/commit/ff2768666f552422ab594ee07ef3b9de19914bb0) |
| 2013-02-22 | `feature` | #1907: cloud support in the scripting API | `history_en.txt`, `apiGenerator.groovy` +3 | [ecf389d4](https://github.com/freeplane/freeplane/commit/ecf389d4833628f86ce0079a35bc5b1be2f8aa7b) |
| 2013-02-21 | `feature` | - add top button to add-on installer - move malware warning to top and make red - adjust t | `Resources_de.properties`, `Resources_el.properties` +14 | [c802f03f](https://github.com/freeplane/freeplane/commit/c802f03f2456cc0031d7740e6033c99f6f0d7ca4) |
| 2013-02-12 | `feature` | - add hyperlinks for non-Freeplane classes too - add hyperlinks for more parameters - meth | `apiGenerator.groovy` | [97e332b9](https://github.com/freeplane/freeplane/commit/97e332b9fb331ddcf5491aef5d4b647d000f47fb) |
| 2013-02-12 | `fix` | fix typo showAnchestors -> showAncestors (thanks to kunkel321) | `Filter.java`, `MapView.java` +2 | [6d921264](https://github.com/freeplane/freeplane/commit/6d9212640cc1ff3a54be9bafe10518a1dbd9d89c) |
| 2013-02-03 | `fix` | fix compiler warnings | `LaTeXLexer.java`, `LaTeXSyntaxKit.java` | [70ca3706](https://github.com/freeplane/freeplane/commit/70ca370647bbf7a65b80e463474be893828c2fc5) |
| 2013-01-26 | `feature` | add to the last commit | `ExecuteScriptAction.java` | [da387260](https://github.com/freeplane/freeplane/commit/da387260f3b0970e9c5ce938106560fe69a4b3e1) |
| 2013-01-11 | `feature` | include delta files for JSyntaxPane LaTeX support (uses svn jsyntaxpane r095 from 2013-01- | `.classpath`, `build.xml` +7 | [943f14de](https://github.com/freeplane/freeplane/commit/943f14de4b091cce571522a4db2999e55bf9e5e1) |

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

**[c464435e](https://github.com/freeplane/freeplane/commit/c464435e27d089e286a6c1d058dcc095095b8064)** (2013-10-29) — Fix: Nullpointer-Exceptions in script filters are not reported properly.

> Solution is to print the exception message instead if stdout.

**[d91f421e](https://github.com/freeplane/freeplane/commit/d91f421e91cb3746577290e87e8a016462783cdd)** (2013-04-13) — merge workspace into freeplane/master

> -initial version of the new workspace as used for docear


---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-28 | `feature` | new method formatDate(date) applies default date format (instead of standard date-time) fo | `FreeplaneScriptBaseClass.java` | [01c0e2ef](https://github.com/freeplane/freeplane/commit/01c0e2ef1779b4be0d95ec82812083b1a06bb913) |
| 2012-12-28 | `feature` | allow Object valued attribute values in add-on maps | `installScriptAddOn.groovy` | [bb45d56d](https://github.com/freeplane/freeplane/commit/bb45d56d44061a29b03852638f65ec53c84159a4) |
| 2012-12-25 | `feature` | Refactor: add method ModeController.isHeadless | `FoldingController.java`, `ModeController.java` +2 | [5b8837de](https://github.com/freeplane/freeplane/commit/5b8837de42ea91c44979a3e50fd68d82f309355b) |
| 2012-12-25 | `fix` | Run tests and fix issues | `MANIFEST.MF`, `FoldingController.java` +10 | [8dd6a47f](https://github.com/freeplane/freeplane/commit/8dd6a47ff18ac70ef6936863c724b616f2192d5c) |
| 2012-12-24 | `api_change` | convert FreeplaneStarter to interface | `Controller.java`, `ApplicationResourceController.java` +8 | [55ce224b](https://github.com/freeplane/freeplane/commit/55ce224b3fe41539b712ff29c7de9c8d92b51cbd) |
| 2012-12-22 | `feature` | Integrate JSyntaxPane 0.9.6pre with support for LaTeX syntax highlighting | `LatexRenderer.java`, `MANIFEST.MF` +4 | [ee13aa28](https://github.com/freeplane/freeplane/commit/ee13aa2858e22a740cda10c0c637446668d5e51d) |
| 2012-12-16 | `fix` | Fix rendering of script based conditions on the button / in the list | `ScriptComboBoxEditor.java`, `ScriptRenderer.java` | [b0d51ac2](https://github.com/freeplane/freeplane/commit/b0d51ac2620038cf059725c8ed6c8fa3183b9471) |
| 2012-10-15 | `feature` | add properties - node.style.minNodeWidth - node.style.maxNodeWidth | `history_en.txt`, `NodeStyleProxy.java` +1 | [82417327](https://github.com/freeplane/freeplane/commit/82417327eccbadd1b785662aff988ddcca65f961) |
| 2012-10-15 | `feature` | add properties - node.style.minNodeWidth - node.style.maxNodeWidth | `history_en.txt`, `NodeStyleProxy.java` +1 | [48af94a4](https://github.com/freeplane/freeplane/commit/48af94a4bc7956ee64efab0c1f1549bb16326e0b) |
| 2012-10-15 | `fix` | fix potential NPE | `ConnectorInListProxy.java` | [eb3b11b4](https://github.com/freeplane/freeplane/commit/eb3b11b48cd70ec7c342272fae13a670a49e47cd) |
| 2012-10-15 | `fix` | fix potential NPE | `ConnectorInListProxy.java` | [91c01af2](https://github.com/freeplane/freeplane/commit/91c01af29a250b833b02cf9916cafa244ef33c28) |
| 2012-10-01 | `fix` | fix npe | `ScriptingConfiguration.java` | [9551404c](https://github.com/freeplane/freeplane/commit/9551404cb0f213f375c0e4bb5034bbf98cd586dd) |
| 2012-08-01 | `fix` | fix java 5 | `ScriptConditionController.java`, `ConnectorProxy.java` | [2eff4bf9](https://github.com/freeplane/freeplane/commit/2eff4bf990efb7a56c8f1bcdab459bb379edf96e) |
| 2012-07-30 | `fix` | Continue bug fix 1754]: Execute [Selected] Node scripts fails | `ExecuteScriptAction.java`, `ExecuteScriptForAllNodes.java` +3 | [08fa2b68](https://github.com/freeplane/freeplane/commit/08fa2b6801dafbcee4a46e804cf6ce65fd43e565) |
| 2012-07-13 | `fix` | fix handling of signed scripts | `ScriptingEngine.java` | [d78d111e](https://github.com/freeplane/freeplane/commit/d78d111eb6daa966d68193cf1074ac2a65e65734) |
| 2012-07-12 | `api_change` | upgrade Groovy to 1.8.6 | `.classpath`, `MANIFEST.MF` +3 | [7be3127e](https://github.com/freeplane/freeplane/commit/7be3127ea880797385281b1a14b0cf0c31da2233) |
| 2012-07-11 | `feature` | #1490: fix keyboard shortcut assignment on add-on installation | `installScriptAddOn.groovy` | [8d3983c6](https://github.com/freeplane/freeplane/commit/8d3983c6afe16b112b86ef2f5be038a9236b5f0d) |
| 2012-07-09 | `fix` | #: fix NPE in Convertible.equals() | `Convertible.java`, `ConvertibleTest.java` | [17abea95](https://github.com/freeplane/freeplane/commit/17abea951e2bd21b1ee194380ebab57df2f836b2) |
| 2012-07-09 | `feature` | scripting API: support for floating nodes | `history_en.txt`, `NodeStyleProxy.java` +1 | [43fb3260](https://github.com/freeplane/freeplane/commit/43fb3260999f2a35fd71de5911ffbc8a5c712005) |
| 2012-05-29 | `feature` | Scripting:  - make menuUtils easily accessible via the variable 'menuUtils'  - support con | `build.xml`, `FreeplaneScriptBaseClass.java` | [7a1af12b](https://github.com/freeplane/freeplane/commit/7a1af12b14461cde4b1756f8681ffcf70af9535b) |
| 2012-05-20 | `feature` | add loadUri() | `freeplane.dsld` | [dd21facb](https://github.com/freeplane/freeplane/commit/dd21facb1e040493724f94739d4dbb899f79ccc8) |
| 2012-05-13 | `feature` | add loadUri() to scripting API | `FreeplaneScriptBaseClass.java`, `Proxy.java` | [372bec8d](https://github.com/freeplane/freeplane/commit/372bec8d06165dbe44c786712858c031b5013b1a) |
| 2012-05-11 | `feature` | add Reminder.remove() | `Proxy.java`, `ReminderProxy.java` | [e82f0e27](https://github.com/freeplane/freeplane/commit/e82f0e275548429d8a93557e4c4f420adec8ce0c) |
| 2012-05-11 | `feature` | add creation of reminders to the scripting API | `ReminderExtension.java`, `ReminderHook.java` +3 | [94bc7aaf](https://github.com/freeplane/freeplane/commit/94bc7aafd3fab34aa55ce04b732ba27ce103f71c) |
| 2012-05-11 | `feature` | implement asBoolean() methods for node properties like if(node.link) ... | `AttributesProxy.java`, `ExternalObjectProxy.java` +2 | [89c1b717](https://github.com/freeplane/freeplane/commit/89c1b7170a298b8eef59fa419daaf1d11e244c2d) |
| 2012-04-21 | `feature` | enable automatic link recognition in attributes by handling URIs instead of URLs special | `Proxy.java`, `ProxyUtils.java` | [70df01f7](https://github.com/freeplane/freeplane/commit/70df01f7ec784162eb1a2dbf48d207822806adaa) |
| 2012-04-20 | `feature` | Fixes and extensions of the scripting API: | `FilterController.java`, `MapNavigationUtils.java` +5 | [f29a260e](https://github.com/freeplane/freeplane/commit/f29a260e41f44b11fac062b37628821870ef5e73) |
| 2012-04-20 | `feature` | - make Convertible support URLs - extend and fix unit test | `TextUtils.java`, `Convertible.java` +1 | [16f81087](https://github.com/freeplane/freeplane/commit/16f81087856e659448a3e8875146e71fea983649) |
| 2012-04-01 | `feature` | add debugging statements | `FormulaUtils.java` | [7f18b3e3](https://github.com/freeplane/freeplane/commit/7f18b3e3824d59a1c291f97d0b21019a41216301) |
| 2012-03-07 | `fix` | #1488: fix startup problem with Turkish locale | `ScriptingConfiguration.java` | [4a6eb43c](https://github.com/freeplane/freeplane/commit/4a6eb43c14edce02358c8e7615179e5ed3fa7b13) |
| 2012-02-22 | `feature` | new method node.icons.getUrls() | `IconsProxy.java`, `Proxy.java` | [261e1fc0](https://github.com/freeplane/freeplane/commit/261e1fc06d4e5c47f910ed379abb1b4e93ae0ecb) |
| 2012-02-17 | `feature` | Add special FilterCancelledException to replace RuntimeException if ScriptCondition cancel | `Filter.java`, `FilterCancelledException.java` +1 | [afbf331b](https://github.com/freeplane/freeplane/commit/afbf331b5adae52b31161687403cdafa1be493ca) |
| 2012-02-17 | `fix` | fix NPE | `ScriptEditorPanel.java` | [edd35b10](https://github.com/freeplane/freeplane/commit/edd35b10223f99055991b8e50d848194f9d3b3ae) |
| 2012-01-27 | `feature` | new FormatController.formatUsingDefault() | `FormatController.java`, `FreeplaneScriptBaseClass.java` | [7d13a123](https://github.com/freeplane/freeplane/commit/7d13a1234258dc2f05c8ed38bff1065b51c9fb0a) |
| 2012-01-14 | `feature` | Create a new API for map loading and mark an old API as deprecated | `MANIFEST.MF`, `EncryptedMap.java` +17 | [cbcfb2b7](https://github.com/freeplane/freeplane/commit/cbcfb2b73e3c66041a5ebb58252b659384a70a0e) |
| 2012-01-12 | `feature` | Added the following command line arguments:  -X<menukey>: execute menu item with key <menu | `history_en.txt`, `MenuUtils.java` +9 | [347dc196](https://github.com/freeplane/freeplane/commit/347dc196f65a70af6b16f5db6dfe7b32b16ed50a) |
| 2012-01-06 | `feature` | updated for new methods in FreeplaneScriptBaseClass | `freeplane.dsld` | [4c0be87e](https://github.com/freeplane/freeplane/commit/4c0be87e4ce6ddd257c46b47c9df3aea930f2a3d) |
| 2012-01-06 | `feature` | add format(object) with default format | `FreeplaneScriptBaseClass.java` | [8ab33519](https://github.com/freeplane/freeplane/commit/8ab3351938b69148ffd9e7f2e14c7fc3b164b484) |

### Dettagli commit con note

**[f29a260e](https://github.com/freeplane/freeplane/commit/f29a260e41f44b11fac062b37628821870ef5e73)** (2012-04-20) — Fixes and extensions of the scripting API:

> - properties Node.next and Node.previous (extracted functionality from FilterController to util)
> 
>  - completed API documentations to resolve the FIXMEs
> 
>  - added special support for URL attribute values
> 
>  - removed the necessity to use the ArrowType enum in the scripting API for Connectors


---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-12-30 | `feature` | Rework creation of new maps: refactoring because of bug 1417]: Show node icons heirarchica | `AttributeController.java`, `AttributeRegistry.java` +21 | [d39a5fef](https://github.com/freeplane/freeplane/commit/d39a5fefef1b69a9e5663e7ffc9caca1532ec468) |
| 2011-12-28 | `fix` | fix NPE | `ScriptComboBoxEditor.java` | [0f0a159a](https://github.com/freeplane/freeplane/commit/0f0a159a9fb4ab4c743a5bcd1ecb83e7e962b085) |
| 2011-12-28 | `feature` | new 'global' methods format(object, formatString) and parse(object) | `FreeplaneScriptBaseClass.java` | [f3e9bcb5](https://github.com/freeplane/freeplane/commit/f3e9bcb555e39c3043e51b5c4b3ebc1c25e14eee) |
| 2011-12-23 | `feature` | #1409: create <userdir>/resources/images folder first before installing images Improve pla | `installScriptAddOn.groovy` | [e6e72bf1](https://github.com/freeplane/freeplane/commit/e6e72bf171f3de51c475dad304f85ffe7dcbf335) |
| 2011-12-15 | `feature` | care for display of keyboard shortcuts in the add-on details | `MenuUtils.java`, `installScriptAddOn.groovy` +1 | [9bcec98d](https://github.com/freeplane/freeplane/commit/9bcec98d71946dd18a29afefe6967df2015f1ad8) |
| 2011-12-14 | `feature` | new icons from Predrag Cuklin | `install_addons.png`, `manage_addons.png` +2 | [ed09f6eb](https://github.com/freeplane/freeplane/commit/ed09f6eb118be38b920a0e53cd5cbb8d66c3d297) |
| 2011-12-14 | `feature` | manage add-ons: make deactivate/deinstall buttons work again | `ManageAddOnsPanel.java` | [b42811c1](https://github.com/freeplane/freeplane/commit/b42811c18c66fe73390db90295fe2ebd4305cd92) |
| 2011-12-10 | `fix` | fix method call | `ControllerProxy.java` | [55ba6705](https://github.com/freeplane/freeplane/commit/55ba67050198e2476e381f797a2fc0b6ffcf4768) |
| 2011-12-09 | `fix` | fix NullPointerExceptions on getNoteText() | `NodeProxy.java` | [6c837883](https://github.com/freeplane/freeplane/commit/6c83788371d097652468a3f5d8ea4a2108636720) |
| 2011-12-09 | `feature` | add Map.backgroundColor(Code) | `MapProxy.java`, `Proxy.java` | [9a5ef9e4](https://github.com/freeplane/freeplane/commit/9a5ef9e49b13a5bcd316abacc847424fde7b799e) |
| 2011-12-09 | `fix` | fix getFile() method to properly handle relative file URLs | `LinkProxy.java` | [4b6c9900](https://github.com/freeplane/freeplane/commit/4b6c9900d9bdc7aa3ad3279236852991c64191ee) |
| 2011-12-09 | `fix` | fix (unused) confirm dialog | `installScriptAddOn.groovy` | [76b88e2b](https://github.com/freeplane/freeplane/commit/76b88e2ba2bc506ad44f0ca379681e36c2ef2207) |
| 2011-12-04 | `feature` | add images to the add-on dialogs | `IconNotFound.java`, `UrlManager.java` +5 | [cb52b0f2](https://github.com/freeplane/freeplane/commit/cb52b0f2bd9c14daf8076783052772e6cd1bdfbb) |
| 2011-11-30 | `feature` | re-create round() method to make maps from the gallery work again | `FreeplaneScriptBaseClass.java` | [6fad32e5](https://github.com/freeplane/freeplane/commit/6fad32e52fff20f9e5c20d57867e879e1a470f85) |
| 2011-11-30 | `feature` | Add-ons dialog: - new 'Themes' tab for add-ons with names ending on 'theme' or 'Theme' - a | `Resources_de.properties`, `Resources_nl.properties` +7 | [8f9fa402](https://github.com/freeplane/freeplane/commit/8f9fa4028740de2e5c86c8cfde265add68764d46) |
| 2011-11-26 | `fix` | fix cast class exception | `ScriptingEngine.java` | [b069a404](https://github.com/freeplane/freeplane/commit/b069a404e6b1ed22b38a0b01ddf423c45e2979cb) |
| 2011-11-25 | `feature` | Add methods to Proxy.Node | `NodeProxy.java`, `Proxy.java` | [bdb5f733](https://github.com/freeplane/freeplane/commit/bdb5f7330669cda0e6e1d9fc6cc03a72a8fc3ea8) |
| 2011-11-22 | `feature` | add addon buttons from Predrag Cuklin | `addons.png`, `install_addons.png` +3 | [6ef92f90](https://github.com/freeplane/freeplane/commit/6ef92f9016c940529be8b47554b59983b42c3b63) |
| 2011-11-22 | `feature` | add a name to the search button | `Resources_de.properties`, `Resources_en.properties` +1 | [c8b508a1](https://github.com/freeplane/freeplane/commit/c8b508a11142a56bd5610e0b28267d6cd0edd4e3) |
| 2011-11-19 | `feature` | add close button to ManageAddOnsDialog | `Resources_en.properties`, `ManageAddOnsDialog.java` | [12b7834e](https://github.com/freeplane/freeplane/commit/12b7834e114bf9d58a8e941721b7a05a7fe4cd1d) |
| 2011-11-19 | `feature` | fix naming of new menu item | `ScriptingRegistration.java` | [ce05064b](https://github.com/freeplane/freeplane/commit/ce05064b4db50703f79af06b445bb36ce03e08aa) |
| 2011-11-19 | `feature` | Add-ons: Differentiate between a fresh install and an update deinstall the old version bef | `Resources_de.properties`, `AddOnsController.java` +2 | [b6bc609a](https://github.com/freeplane/freeplane/commit/b6bc609a0c48dea0e3669d2cc35a129a71845c26) |
| 2011-11-18 | `fix` | fix Groovy error | `installScriptAddOn.groovy` | [bb368635](https://github.com/freeplane/freeplane/commit/bb36863552b6a464c6e9a59c0e0449b1fbe345a6) |
| 2011-11-17 | `feature` | Display add-on details on installation | `Resources_de.properties`, `UITools.java` +6 | [8e7b87de](https://github.com/freeplane/freeplane/commit/8e7b87dea5bbb4b557ee2043c9255287e530cd0e) |
| 2011-11-08 | `fix` | fix ScriptingRegistration.install | `ScriptingRegistration.java`, `ManageAddOnsAction.java` +1 | [5b2622d8](https://github.com/freeplane/freeplane/commit/5b2622d81529e50ee8a1359521c1320183fe94da) |
| 2011-11-08 | `feature` | Create rename api.zip in dirstibution to script-api.zip. Create it only for dist but nore  | `build.xml`, `build.xml` | [57864d64](https://github.com/freeplane/freeplane/commit/57864d64addef5ae5719feb0b8f8d0cc6694ef05) |
| 2011-11-08 | `feature` | add-ons: 'Really install?'... | `Resources_en.properties`, `installScriptAddOn.groovy` | [9a721533](https://github.com/freeplane/freeplane/commit/9a721533f3fb15f3e35f6ecac9587735000520d7) |
| 2011-11-06 | `feature` | tabbed manage/install add-on dialog | `Resources_en.properties`, `AddOnInstallerPanel.java` +2 | [2a29ca74](https://github.com/freeplane/freeplane/commit/2a29ca749711d69e23c3ce0d78725dcd895d5446) |
| 2011-11-01 | `fix` | bug fixes in ManageAddOnsDialog | `ButtonsInCellRenderer.java`, `ManageAddOnsDialog.java` | [6a0b607b](https://github.com/freeplane/freeplane/commit/6a0b607b96a6cdf97c6b70db028cfe84dfbfb1d6) |
| 2011-10-31 | `feature` | on install only create a MapModel from the given URL, don't open it as a view | `ManageAddOnsDialog.java` | [4b36b85e](https://github.com/freeplane/freeplane/commit/4b36b85ecbf4dee0334b0ee3c2165d4374ef0069) |
| 2011-10-31 | `feature` | add new properties author and license and make them optional in the installer | `AddOnProperties.java`, `Resources_en.properties` +1 | [a1212a08](https://github.com/freeplane/freeplane/commit/a1212a08b7504cc0a0adaff7450ad61d27bf83b9) |
| 2011-10-30 | `feature` | Scripting API: new method Attributes.isEmpty() | `AttributesProxy.java`, `Proxy.java` | [50eef519](https://github.com/freeplane/freeplane/commit/50eef519ad275dae56e9bad647dba87c53b53039) |
| 2011-10-26 | `feature` | ManageAddOnsDialog: - cope with HTML descriptions - update add-ons table after deinstall o | `AddOnsController.java`, `Resources_en.properties` +1 | [51ab52f2](https://github.com/freeplane/freeplane/commit/51ab52f2ee5c725945068cd2d8a1b1d6fbc20b55) |
| 2011-10-24 | `fix` | #1339: avoid bug reports on installation errors | `installScriptAddOn.groovy` | [7d624e84](https://github.com/freeplane/freeplane/commit/7d624e84347298c1734c0ca804d3fb4851c180b3) |
| 2011-10-24 | `feature` | add-on fixes | `ScriptingConfiguration.java`, `ManageAddOnsDialog.java` | [2e7a6b6f](https://github.com/freeplane/freeplane/commit/2e7a6b6f9c3fdf4885e2db1393ffb9d884625987) |
| 2011-10-23 | `feature` | final fixes & implement deactivate and deinstall | `AddOnProperties.java`, `AddOnsController.java` +3 | [17e44ef1](https://github.com/freeplane/freeplane/commit/17e44ef1b2814a60ba462f89c01acc232ec7f2c3) |
| 2011-10-19 | `feature` | new scripting API method: Node.setLeft() | `NodeProxy.java`, `Proxy.java` | [2b4dd55a](https://github.com/freeplane/freeplane/commit/2b4dd55a39b58c3571a488782f8fc8b9382f20f8) |
| 2011-10-19 | `fix` | fix script installation and menu building | `Resources_en.properties`, `installScriptAddOn.groovy` +4 | [a4e93369](https://github.com/freeplane/freeplane/commit/a4e93369c96d914a1f6089ec5f4ef75fef7bb99a) |
| 2011-10-15 | `feature` | Freeplane script API support for the Groovy Eclipse plugin | `freeplane.dsld` | [8b542f7c](https://github.com/freeplane/freeplane/commit/8b542f7cf06a7f0f5a408f536285f6cc4b4a22a5) |
| 2011-10-15 | `feature` | Add-ons can contain Zips | `installScriptAddOn.groovy`, `ScriptAddOnProperties.java` | [733e6efe](https://github.com/freeplane/freeplane/commit/733e6efe5cf345ddb6db78e328b6cdb7531cab18) |
| 2011-10-15 | `feature` | remove add-on type from the add-ons dialog | `Resources_de.properties`, `Resources_en.properties` +1 | [7688a97f](https://github.com/freeplane/freeplane/commit/7688a97f1f9d8826b67bc0d0300602e4161b9600) |
| 2011-10-15 | `feature` | Scripting API: new methods Node.setBinary(byte[]) and Node.getBinary() | `NodeProxy.java`, `Proxy.java` | [048019bd](https://github.com/freeplane/freeplane/commit/048019bd36578ff8e374736778d15d647c9f465a) |
| 2011-10-10 | `feature` | add-ons support shortcut setting | `Resources_en.properties`, `installScriptAddOn.groovy` +3 | [89a63bc4](https://github.com/freeplane/freeplane/commit/89a63bc44877b2bb648595099f3704f22d1e2ded) |
| 2011-10-03 | `api_change` | upgrade groovy to 1.8.2 | `.classpath`, `MANIFEST.MF` +3 | [dd9f37ef](https://github.com/freeplane/freeplane/commit/dd9f37efa962eeeef1340a298858e094349fa78b) |
| 2011-10-02 | `feature` | enable null check for details text | `NodeProxy.java` | [5cbebb5e](https://github.com/freeplane/freeplane/commit/5cbebb5efeff716435a4673af7eaeb491e9fcc83) |
| 2011-10-02 | `fix` | fix restrictive permissions in case the user has set the classpath | `ScriptingEngine.java`, `ScriptingPermissions.java` | [5f789b03](https://github.com/freeplane/freeplane/commit/5f789b03549ada7bfb9a585c75676460fbf2d126) |
| 2011-09-28 | `feature` | fix permission handling of scripts: - can be set for a script individually - add-on permis | `installScriptAddOn.groovy`, `ScriptEditor.java` +4 | [c3e60a49](https://github.com/freeplane/freeplane/commit/c3e60a4966b181e19116210e39f11cde0da9735a) |
| 2011-09-26 | `feature` | add-on configuration, i18n, permissions | `Resources_en.properties`, `installScriptAddOn.groovy` +10 | [ef7a5b93](https://github.com/freeplane/freeplane/commit/ef7a5b93a20a8e8cb6a7c12da8c0245fbb6d7235) |
| 2011-09-24 | `feature` | 1270: add an extra key for <menu_category name=scripting> to the node context menu too | `mindmapmodemenu.xml`, `ScriptingConfiguration.java` +2 | [403ac5d6](https://github.com/freeplane/freeplane/commit/403ac5d6ca007f624beedbbc7144429155acca2a) |
| 2011-09-24 | `feature` | Add-on-Installer | `Resources_de.properties`, `AddOnProperties.java` +4 | [e28b1575](https://github.com/freeplane/freeplane/commit/e28b1575f500b619059c69350efbe04d2aaa7c5f) |
| 2011-09-23 | `fix` | fix JDK 1.5/1.6 ncompatibilities | `ScriptingRegistration.java`, `ButtonsInCellRenderer.java` +1 | [52300f21](https://github.com/freeplane/freeplane/commit/52300f2155a8eb5bfb175ed62037710140b8e647) |
| 2011-09-15 | `feature` | Prototype of add-on management | `MANIFEST.MF`, `Resources_de.properties` +21 | [39e3ac81](https://github.com/freeplane/freeplane/commit/39e3ac81a46c0768b16729fc56901ba8462e1d33) |
| 2011-09-01 | `feature` | new property 'config' available in all scripts | `FreeplaneScriptBaseClass.java` | [e6f4751c](https://github.com/freeplane/freeplane/commit/e6f4751ccbeea64d0e3bd425481a449682cdbe0d) |
| 2011-08-09 | `feature` | Scripting support math with nodes: node.text = 2; assert 3 * node * 2 == 12 | `history_en.txt`, `FreeplaneScriptBaseClass.java` +2 | [386ce91c](https://github.com/freeplane/freeplane/commit/386ce91c06020864519cce4fa6202499982bfdb1) |
| 2011-08-07 | `feature` | Scripting API: add Attributes.getMap() | `AttributesProxy.java`, `Proxy.java` | [3c7bb18b](https://github.com/freeplane/freeplane/commit/3c7bb18b7bba7505ef3b33e5488562c317a5e8dc) |
| 2011-08-07 | `feature` | add combocompletions in script editor | `build.xml`, `jsyntaxpane.jar` +1 | [21fd58f1](https://github.com/freeplane/freeplane/commit/21fd58f1064900427774f18d07fbd7bf8182fe4d) |
| 2011-08-07 | `feature` | Implicitly remove mnemonic symbol "&" from all language properties.  To keep it new method | `SetBooleanPropertyAction.java`, `OptionPanel.java` +37 | [58c24897](https://github.com/freeplane/freeplane/commit/58c248971b98a22c06a0cc262e2989d02573be5c) |
| 2011-07-27 | `fix` | fix compilation errors due to wrong Closure type parameter | `AttributesProxy.java`, `ControllerProxy.java` +2 | [9c274023](https://github.com/freeplane/freeplane/commit/9c274023275cf2dc79a67b4d2906be44986987b0) |
| 2011-07-26 | `fix` | fix closure type parameter | `ProxyUtils.java` | [d9bf7f48](https://github.com/freeplane/freeplane/commit/d9bf7f48f97872d379b42386ccfb32a86a79a9e6) |
| 2011-07-25 | `fix` | Closure is a generic type now - fix compiler warnings | `AttributesProxy.java`, `ControllerProxy.java` +3 | [778b8a0a](https://github.com/freeplane/freeplane/commit/778b8a0a0f0db5fcb548f7d95d388a983ea4b54d) |
| 2011-07-25 | `fix` | Bug #1155: - set class loader in the designed way - override the right method - otherwise  | `ScriptingEngine.java` | [820e3cae](https://github.com/freeplane/freeplane/commit/820e3cae943632e8f5c6dc149749c9b7af38d4df) |
| 2011-07-13 | `feature` | new methods and properties for filtering | `history_en.txt`, `MapProxy.java` +1 | [cc59bef1](https://github.com/freeplane/freeplane/commit/cc59bef19b33de3b4fe2c7f47b0c03471b0de2ff) |
| 2011-07-13 | `feature` | improved documentation and new scripting methods to adjust to the format handling via form | `NodeProxy.java`, `Proxy.java` | [8bd760ff](https://github.com/freeplane/freeplane/commit/8bd760ff559b416fac9496817ffd436415701e03) |
| 2011-06-20 | `feature` | new scripting API methods/properties:  - node.icons[<index>]  - node.icons.first  - node.i | `IconsProxy.java`, `NodeProxy.java` +2 | [5db3eb78](https://github.com/freeplane/freeplane/commit/5db3eb782c49c65d3f6bb2022fc1c984333d313d) |
| 2011-06-12 | `fix` | fix /freeplane_plugin_script/src-jsyntaxpane/org/freeplane/plugin/script/NodeIdHighLighter | `NodeIdHighLighter.java` | [7a21627c](https://github.com/freeplane/freeplane/commit/7a21627c8e83dd90cac0de002c1746fd14dbcf4e) |
| 2011-06-12 | `fix` | fix java.util.ConcurrentModificationException 	at org.freeplane.plugin.script.ScriptingEng | `ScriptingEngine.java` | [2035bb80](https://github.com/freeplane/freeplane/commit/2035bb802d06b3d85c1a9288b729c780321a150a) |
| 2011-06-12 | `fix` | Attempt to fix java.util.NoSuchElementException 	at java.util.LinkedList.remove(LinkedList | `IUndoHandler.java`, `UndoHandler.java` +1 | [4e3f6b0c](https://github.com/freeplane/freeplane/commit/4e3f6b0cc37e32d3d6e91429f99244c57d7e1565) |
| 2011-06-03 | `feature` | new methods Node.appendChild(Node) and Node.appendBranch(Node) | `NodeProxy.java`, `Proxy.java` | [79873c06](https://github.com/freeplane/freeplane/commit/79873c065a3f6231944398354fa19d3dfcaeba2b) |
| 2011-06-02 | `fix` | bug fix for changing side (left/right) when nodes are moved by script | `NodeProxy.java` | [355b544b](https://github.com/freeplane/freeplane/commit/355b544b23a427cf55e9d890f094351b1bfd722d) |
| 2011-05-19 | `fix` | fix the documentation of Node.findAll() | `Proxy.java` | [245fd995](https://github.com/freeplane/freeplane/commit/245fd99550bf57334ba5f72d3c25915dbef81f30) |
| 2011-05-11 | `feature` | - improved support for FormattedNumber in formulas - changed attribute value type from Str | `AttributesProxy.java`, `ConvertibleNumber.java` +4 | [f49c1440](https://github.com/freeplane/freeplane/commit/f49c144059051613c28e93a3f453906d03b780f4) |
| 2011-05-09 | `feature` | implemented input scanner for date and number recognition: - replace options parse_dates a | `Resources_de.properties`, `Resources_fr.properties` +33 | [35d089f0](https://github.com/freeplane/freeplane/commit/35d089f0ac335957e07c5b4df9ac3914cd7934b7) |
| 2011-04-29 | `feature` | add test suites | `MANIFEST.MF`, `AllFreeplanePluginScriptUnitTests.java` +2 | [0d7402d6](https://github.com/freeplane/freeplane/commit/0d7402d612a246c90bd5ecf5cc954a92ff067cde) |
| 2011-04-28 | `feature` | fixed documentation of add/move/removeConnector methods | `Proxy.java` | [670a9a07](https://github.com/freeplane/freeplane/commit/670a9a0777782533b056fdf56526503952b84d2a) |
| 2011-04-18 | `fix` | many improvements and fixes: - fix package of FreeplaneScriptBaseClass (Bug #1050) - remov | `apiGenerator.groovy` | [1c122263](https://github.com/freeplane/freeplane/commit/1c122263b754d8a15fe70c9f12d81c065827724c) |
| 2011-04-18 | `feature` | add TextUtils | `build.xml` | [f374af4b](https://github.com/freeplane/freeplane/commit/f374af4baade9a53cff6161bc9f587e22e994f5b) |
| 2011-03-29 | `api_change` | package and distribute scripting api.zip | `build.xml`, `build.xml` | [79be0970](https://github.com/freeplane/freeplane/commit/79be09706508252bd475327452e14d9511834f73) |
| 2011-03-27 | `fix` | fix compiler warnings | `ResourceController.java`, `TypedListCellRenderer.java` +8 | [d7d93930](https://github.com/freeplane/freeplane/commit/d7d93930265e1fc8747c2a8af35a4a182da75d98) |
| 2011-03-25 | `fix` | fix wrong circular reference errors | `UniqueStack.java` | [ed14e1e9](https://github.com/freeplane/freeplane/commit/ed14e1e901a46d899d1068fd6886deac5f04c674) |
| 2011-03-20 | `fix` | Rename KeyTypeAction to FirstAction, fix freeplane_script_plugin | `AccelerateableAction.java`, `IEditHandler.java` +6 | [e88b92a2](https://github.com/freeplane/freeplane/commit/e88b92a232a9c6b2e1d949eae289524abc44331b) |
| 2011-03-12 | `api_change` | Scripting API: Extended AttributeProxy: | `AttributesProxy.java`, `NodeProxy.java` +1 | [7c9d467b](https://github.com/freeplane/freeplane/commit/7c9d467b448d0d233ab2cd495849cbdb3b1b3da0) |
| 2011-03-07 | `feature` | Scripting API: add support for FreeplaneDate and URIs | `FreeplaneDate.java`, `Convertible.java` +3 | [ae7c454d](https://github.com/freeplane/freeplane/commit/ae7c454d6d176cae169ad4d4d0015c35e7b7d1af) |
| 2011-03-04 | `fix` | Bug fix: remove buggy method MapController.refreshMap, use fireMapChanged instead Remove o | `Resources_ar.properties`, `Resources_ca.properties` +45 | [801ccd7e](https://github.com/freeplane/freeplane/commit/801ccd7e650207b368968997cd25f9e5c8315d68) |
| 2011-02-21 | `feature` | new "global" methods: - toString(Object) - Long round(Double) - Double round(Double, preci | `FreeplaneScriptBaseClass.java` | [1daf2634](https://github.com/freeplane/freeplane/commit/1daf2634eb9e1f0ba3c761a9ccdf2097ecad0ae9) |
| 2011-02-17 | `fix` | fix java.lang.NoSuchMethodException: jsyntaxpane.actions.ActionUtils.setCaretPosition(java | `JSyntaxPaneProxy.java` | [8275b952](https://github.com/freeplane/freeplane/commit/8275b952c8869e8932583b9caee2016ae74395ad) |
| 2011-02-09 | `fix` | fix illegal use of keyword (why did it work before??) | `apiGenerator.groovy` | [35981365](https://github.com/freeplane/freeplane/commit/359813656589f1cd21bd1fc4686cd64195685241) |
| 2011-02-09 | `feature` | use new API method Node.createChild(text) | `ScriptApiTest.java` | [bfaaa926](https://github.com/freeplane/freeplane/commit/bfaaa926b41b4b89416eae97c238967e9d68079e) |
| 2011-02-02 | `feature` | Scripting API extensions + changes: | `ControllerProxy.java`, `MapProxy.java` +1 | [b42d7478](https://github.com/freeplane/freeplane/commit/b42d7478bfd9080a44da10b839567b5cb9a7ffa9) |
| 2011-02-02 | `feature` | add new binding 'textUtils' as an alias for TextUtils | `TextUtils.java`, `FreeplaneScriptBaseClass.java` | [2b9cfdac](https://github.com/freeplane/freeplane/commit/2b9cfdacadaaa36445a57915da963657309cd46e) |
| 2011-01-30 | `feature` | add check for toNum("") | `ConvertibleTest.java` | [50a3a729](https://github.com/freeplane/freeplane/commit/50a3a729a991d407615554205aee6ac4a1285d8f) |
| 2011-01-20 | `feature` | create the user scripts directory if it doesn't exist | `ScriptingConfiguration.java`, `ScriptingRegistration.java` | [13b1151b](https://github.com/freeplane/freeplane/commit/13b1151b05f6fbf23829707b2aa855470d580944) |
| 2011-01-14 | `api_change` | - make HtmlUtil available in scripts as "global variable" htmlUtils - added HtmlUtils to t | `HtmlUtils.java`, `build.xml` +1 | [ac609888](https://github.com/freeplane/freeplane/commit/ac609888f04a1533158d8869dfa35639a7645dbe) |
| 2011-01-14 | `feature` | add FreeplaneVersion to the API documentation | `FreeplaneVersion.java`, `build.xml` | [f23d0442](https://github.com/freeplane/freeplane/commit/f23d0442f784dc1e71ff69842bd00ce6b61cbac7) |
| 2011-01-14 | `api_change` | added API generation to the distribution | `build.xml`, `build.xml` | [b946317c](https://github.com/freeplane/freeplane/commit/b946317c567a48bf8c54074558ec24a8780fc84b) |
| 2011-01-13 | `fix` | fix NPE | `ConnectorInListProxy.java` | [6e88d30b](https://github.com/freeplane/freeplane/commit/6e88d30bc002b91b6ca2c34b2df49d8d43040adf) |
| 2011-01-13 | `fix` | documentation fix | `Convertible.java`, `ConvertibleNodeText.java` | [542242b9](https://github.com/freeplane/freeplane/commit/542242b918b945edc76b32f4f57d29cbada91168) |
| 2011-01-13 | `api_change` | complete documentation of scripting api | `UITools.java`, `LogUtils.java` +1 | [54a669cd](https://github.com/freeplane/freeplane/commit/54a669cdd25f327648690b72d1660316912b76db) |
| 2011-01-13 | `fix` | ExternalObject: - fix NPEs - allow removal of external objects - rename property: external | `ExternalObjectProxy.java`, `Proxy.java` | [e679c94d](https://github.com/freeplane/freeplane/commit/e679c94dd5f79002e4b231a533becc5c5cb8ac2a) |
| 2011-01-11 | `feature` | new methods Controller.edit(node) and  Controller.editInPopup(node) | `ControllerProxy.java`, `Proxy.java` | [49c1339b](https://github.com/freeplane/freeplane/commit/49c1339bf09c04d78c08e7d83eb394a00cf12244) |
| 2011-01-10 | `feature` | added two new bindings: | `FreeplaneScriptBaseClass.java` | [7a2fbbf2](https://github.com/freeplane/freeplane/commit/7a2fbbf29c8874738ee994ca7be8fe4c8b2a9fd7) |
| 2011-01-10 | `feature` | new convenience method: Node.createChild(nodeText) | `NodeProxy.java`, `Proxy.java` | [ee4bd062](https://github.com/freeplane/freeplane/commit/ee4bd06219d8559b7b2924d8958bd61bc03b2fcc) |
| 2011-01-10 | `feature` | Scripting API/Controller+Node: new methods findAll() and findAllDepthFirst() | `ControllerProxy.java`, `Proxy.java` +1 | [dbfb2b82](https://github.com/freeplane/freeplane/commit/dbfb2b82ee6058a37a3b6623fa565d13ef04f5d6) |
| 2011-01-10 | `api_change` | Scripting API/Link: added convenience methods and properties for dealing with link targets | `history_en.txt`, `LinkProxy.java` +1 | [8868a6b2](https://github.com/freeplane/freeplane/commit/8868a6b288850c0f3f1c6de55be1201fcc9ce7cd) |
| 2011-01-02 | `feature` | Add new connector options to preferences for setting the standard values | `preferences.xml`, `OptionPanelBuilder.java` +4 | [04f20b6a](https://github.com/freeplane/freeplane/commit/04f20b6a49b135e79071c9a4febc3cd3c94d8c85) |
| 2011-01-02 | `feature` | New link formatting options : width, transparency | `ColorUtils.java`, `ConnectorModel.java` +12 | [4fa46c76](https://github.com/freeplane/freeplane/commit/4fa46c761a0c16be36b447322bc9545411c25317) |

### Dettagli commit con note

**[8bd760ff](https://github.com/freeplane/freeplane/commit/8bd760ff559b416fac9496817ffd436415701e03)** (2011-07-13) — improved documentation and new scripting methods to adjust to the format handling via formatted typed content:

> - Node.getObject()
> - Node.getFormat()
> - Node.setObject(Object object)
> - Node.setDateTime(Date date)
> - Node.setFormat(String format)

**[7c9d467b](https://github.com/freeplane/freeplane/commit/7c9d467b448d0d233ab2cd495849cbdb3b1b3da0)** (2011-03-12) — Scripting API: Extended AttributeProxy:

> - added getValues()
>  - added findValues(Closure closure)
>  - replaced getAttributeNames() by getNames()

**[b42d7478](https://github.com/freeplane/freeplane/commit/b42d7478bfd9080a44da10b839567b5cb9a7ffa9)** (2011-02-02) — Scripting API extensions + changes:

> - new: ControllerRO.getUserDirectory()
> 
> - fix: Controller.newMap() ensures that undo is handled correctly
>   (avoids NullPointerExceptions and more)
> 
> - new: MapRO.isSaved() + Map.setSaved(boolean) to set/check the saved/changed flag
> 
> - new: Map.setName()

**[7a2fbbf2](https://github.com/freeplane/freeplane/commit/7a2fbbf29c8874738ee994ca7be8fe4c8b2a9fd7)** (2011-01-10) — added two new bindings:

> - logger -> org.freeplane.core.util.LogUtils
> - ui -> org.freeplane.core.ui.components.UiTools
> 
> This allows code like this:
> 
>   logger.info("Hello World")
>   ui.informationMessage("Hello World")
> 
> or more elaborate:
>   ui.informationMessage(ui.frame, "Hello World")


---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-12-28 | `fix` | fix typo | `AttributeCompareCondition.java`, `AttributeExistsCondition.java` +34 | [0288b2d1](https://github.com/freeplane/freeplane/commit/0288b2d1d6066022ca3620f4b05cb2656ac5e438) |
| 2010-12-26 | `feature` | add Node.get/setHideDetails() | `NodeProxy.java`, `Proxy.java` | [a050d6dc](https://github.com/freeplane/freeplane/commit/a050d6dcbadb94660c361159dbea7e4c0419b2a3) |
| 2010-12-24 | `feature` | new alternative API methods for setting and getting colors dealing with RGB strings:  - St | `ConnectorProxy.java`, `EdgeProxy.java` +2 | [84a4472c](https://github.com/freeplane/freeplane/commit/84a4472c0ce271100021ab8cdc8e55c9a894d115) |
| 2010-12-19 | `fix` | Move NodeIdHighLighter in its own jar file, fix JSyntaxPaneProxy, revert FormulaTextTransf | `.bzrignore`, `FormulaTextTransformer.java` +4 | [b030e51e](https://github.com/freeplane/freeplane/commit/b030e51e7be597310535cf999e183011ac0e569a) |
| 2010-12-18 | `feature` | add NodeIdHighlighter | `MapController.java`, `FormulaTextTransformer.java` +5 | [7b52a2fd](https://github.com/freeplane/freeplane/commit/7b52a2fd70ce82ac966121e1b27b428c7677f5b9) |
| 2010-12-07 | `feature` | new methods: . Convertible Proxy.NodeRO.getDetails() . String Proxy.NodeRO.getDetailsText( | `ConvertibleText.java`, `NodeProxy.java` +2 | [ccd0514c](https://github.com/freeplane/freeplane/commit/ccd0514cce18b174c407b8650825bfaef638e604) |
| 2010-11-25 | `feature` | Scripting API: - add Icons.add(iconId) and Icons.remove(iconId) - deprecate Icons.addIcon( | `IconsProxy.java`, `Proxy.java` | [d7f46ae2](https://github.com/freeplane/freeplane/commit/d7f46ae22c8e38c9222f3b97a4775b2223e0db12) |
| 2010-11-14 | `fix` | bug fix: updating of formula results in AttributeTable | `AttributeTable.java`, `AttributeTableModelDecoratorAdapter.java` +3 | [0c6585ac](https://github.com/freeplane/freeplane/commit/0c6585acbaedf08efd71739ade958506d7be94c8) |
| 2010-11-13 | `feature` | Fix #804: Scripting errors due to missing read permissions: | `IValidator.java`, `OptionPanel.java` +10 | [13a5bddc](https://github.com/freeplane/freeplane/commit/13a5bddc10aa653f528995994a6ce478a6b1e9ba) |
| 2010-11-07 | `fix` | patch jsyntaxpane : use dialogs as parent of further dialogs | `jsyntaxpane-jdk5.jar`, `jsyntaxpane-r095-jdk5-patch.txt` +2 | [c0595759](https://github.com/freeplane/freeplane/commit/c05957594241cf32808bb983f7a8fc489787e151) |
| 2010-11-06 | `feature` | add JSyntaxPane to script plugin | `.classpath`, `MANIFEST.MF` +5 | [4055012c](https://github.com/freeplane/freeplane/commit/4055012c3a2f966c89345ae110470be580f146ac) |
| 2010-11-05 | `feature` | Formulas: enable access between formulas in attributs notes and node texts of the same nod | `FormulaUtils.java`, `ScriptContext.java` | [af2ec041](https://github.com/freeplane/freeplane/commit/af2ec041f9345aa260230634d111066e9c0df290) |
| 2010-10-23 | `feature` | Refactor condittions Add equals and hashCode methods using org.apache.commons.lang.builder | `AttributeCompareCondition.java`, `AttributeConditionController.java` +70 | [dab47919](https://github.com/freeplane/freeplane/commit/dab479199e537868bcb48e7623ec58eeb212afe0) |
| 2010-10-21 | `feature` | new method ifNull(value, valueIfNull) | `FreeplaneScriptBaseClass.java` | [83a7901e](https://github.com/freeplane/freeplane/commit/83a7901eda71b64c125402a9e3c5d758f9e8192d) |
| 2010-10-17 | `feature` | add defaults.properties to plugin jar files: fix build.xml | `build.xml`, `build.xml` | [25e674e1](https://github.com/freeplane/freeplane/commit/25e674e10803fa5b5cf8e6763b1a66dc842ddc86) |
| 2010-10-13 | `feature` | new 'safe' variant of Convertible.getNum() returns (long) 0 on conversion errors | `Convertible.java`, `ConvertibleTest.java` | [a6305ea7](https://github.com/freeplane/freeplane/commit/a6305ea73431ad3cebc55d378d07d308467eb9f9) |
| 2010-10-12 | `fix` | Bug fix : FormulaTextTransformer removed HTML formatting even if no script | `MainView.java`, `FormulaTextTransformer.java` +1 | [833005e6](https://github.com/freeplane/freeplane/commit/833005e60e6e8531b73311d27b3b0e7683e87a2a) |
| 2010-10-12 | `feature` | new filter condition ScriptCondition | `Resources_en.properties`, `ScriptCondition.java` | [b4852229](https://github.com/freeplane/freeplane/commit/b4852229591c2bb1e5b30ef7e34c0019f9e79d39) |
| 2010-10-12 | `feature` | - read plugin default from file defaults.properties to avoid hardcoded defaults. Used in s | `ResourceController.java`, `AppletResourceController.java` +8 | [1309850d](https://github.com/freeplane/freeplane/commit/1309850ddbc06d0a413751be29bb975264bbb548) |
| 2010-10-09 | `fix` | move constants FILTER_NODE, FILTER_DETAILS and FILTER_PARENT to TextController fix complie | `IgnoreCaseNodeContainsCondition.java`, `NodeContainsCondition.java` +6 | [a4051418](https://github.com/freeplane/freeplane/commit/a4051418841190480a4a1b6e78dd77ef711cf405) |
| 2010-10-03 | `feature` | - handle circular references - new option 'don't mark formula nodes' | `MainView.java`, `Resources_en.properties` +8 | [35e29691](https://github.com/freeplane/freeplane/commit/35e296913e602a3c3e037b49aebb9eefaad990f8) |
| 2010-09-15 | `feature` | Refactor: let all styles implement IStyle | `CloudController.java`, `EdgeController.java` +20 | [637e7f05](https://github.com/freeplane/freeplane/commit/637e7f05ba39b32bc862f2a581cd5f899fa279c3) |
| 2010-08-26 | `feature` | large script API overhaul mostly for formula use: * Script API / Attribute   - deprecated: | `ViewController.java`, `FreeplaneIconUtils.java` +22 | [40c1e149](https://github.com/freeplane/freeplane/commit/40c1e14960af350fc09e1936e4a113717e37629a) |
| 2010-08-18 | `feature` | - differentiate between pure Convertibles and ConvertibleNodeText (for caching) - renamed  | `Convertible.java`, `ConvertibleNodeText.java` +4 | [7824f192](https://github.com/freeplane/freeplane/commit/7824f19237444acf6c97a3a118ddc065a5dea326) |
| 2010-08-18 | `api_change` | extended anew, updated for API changes | `ScriptApiTest.java` | [30b55267](https://github.com/freeplane/freeplane/commit/30b55267ef8f6c5c172fe8c89669201960315b6b) |
| 2010-08-18 | `api_change` | scripting api extensions (and some deprecations:  + Controller.getFreeplaneVersion()  + No | `ControllerProxy.java`, `ConversionException.java` +7 | [6acb8e64](https://github.com/freeplane/freeplane/commit/6acb8e6441717c68bcfb4c59998d3e50f70e731b) |
| 2010-08-18 | `feature` | - allow for node ids used as variables: ID_1234567.text returns the text   of the node wit | `FreeplaneSecurityManager.java`, `FreeplaneScriptBaseClass.java` +1 | [6fefd4d7](https://github.com/freeplane/freeplane/commit/6fefd4d732b57c9b75537cdee07d4e0b0611e2df) |
| 2010-08-18 | `fix` | fix some compiler warnings with Eclipse 3.6 | `ResourceBundles.java`, `BitmapImagePreview.java` +7 | [32e5b086](https://github.com/freeplane/freeplane/commit/32e5b086a8d68f5b15b7b5e9c67ce89f9c750c2d) |
| 2010-08-04 | `api_change` | more tests - no 52 tests of 131 for all API methods are implemented and pass | `ScriptApiTest.java` | [e1711048](https://github.com/freeplane/freeplane/commit/e171104875998ec8798560543c607570a515ff0f) |
| 2010-08-04 | `api_change` | Scripting API bugfix: Node.isDescendant(Node p) entered an infinite loop if called with si | `NodeProxy.java` | [d40c0c4b](https://github.com/freeplane/freeplane/commit/d40c0c4b09f161a9a5ba0ef3e5770b50d834fac0) |
| 2010-08-01 | `fix` | Preparations for spreadsheet/formula plugin: | `Resources_es.properties`, `Resources_fr.properties` +13 | [2da72e95](https://github.com/freeplane/freeplane/commit/2da72e95375cec64654569b0fdd0af6ad81cc24c) |
| 2010-08-01 | `api_change` | started a test for every Scripting API method - 34 of 131 are tested Usage: Run the follow | `ScriptApiTest.java` | [26a648a2](https://github.com/freeplane/freeplane/commit/26a648a2fb0978ab62c02ee4262e3f501a5bca25) |
| 2010-06-25 | `feature` | - move scripting option panel configuration to new tab 'Plugins' - add scripting configura | `preferences.xml`, `ConfigurationUtils.java` +5 | [aad11d2f](https://github.com/freeplane/freeplane/commit/aad11d2fee37e0696598df89513d40de363ca1b3) |
| 2010-06-22 | `api_change` | - #517: getNotePlainText() and setNotePlainText() methods for    scripting interface. - ad | `NodeProxy.java`, `Proxy.java` | [3d9a26a1](https://github.com/freeplane/freeplane/commit/3d9a26a1ff829ad121c4b30a0cc31e9122d712e1) |
| 2010-04-26 | `feature` | new Proxy.Map.getFile() | `MapProxy.java`, `Proxy.java` | [24f4e29b](https://github.com/freeplane/freeplane/commit/24f4e29be4be6d9a209e81f1571b9c4a64d26abf) |
| 2010-04-05 | `api_change` | 551]: deleting nodes via scripting interface using each iterator throws exception | `NodeProxy.java` | [c3f12e8b](https://github.com/freeplane/freeplane/commit/c3f12e8bdb17fb2631d9ebac953cdcb85b351185) |
| 2010-03-30 | `fix` | rename FpStringUtils to TextUtil, move it into core.util package and move all static metho | `MANIFEST.MF`, `ColorTracker.java` +163 | [06ed5406](https://github.com/freeplane/freeplane/commit/06ed54068f045191f8031fd9399021fd060c58ad) |
| 2010-03-17 | `api_change` | #485: adjustments of the attribute API after review | `AttributesProxy.java`, `Proxy.java` | [deb4c6f5](https://github.com/freeplane/freeplane/commit/deb4c6f5d5432ef0b0f8cb7a7cab093e943db031) |
| 2010-03-12 | `api_change` | #485: several attributes with same name are not taken into account - first sketch of an in | `AttributesProxy.java`, `Proxy.java` | [062a0d6b](https://github.com/freeplane/freeplane/commit/062a0d6b238e5ceb75d043ae6c22643f0324e721) |
| 2010-02-27 | `feature` | 425]: Drag and drop from file explorer under Linux does not create a node with relative li | `MClipboardController.java`, `ExportBranchAction.java` +11 | [3abd79ef](https://github.com/freeplane/freeplane/commit/3abd79effb49ad0cd6d478759533f4f539d94343) |
| 2010-02-19 | `feature` | enable undo for setLastModifiedAt() and setCreatedAt() | `HistoryInformationModel.java`, `NodeProxy.java` | [b72ff2b6](https://github.com/freeplane/freeplane/commit/b72ff2b62680f7ebf87165a04c935545a5f45344) |
| 2010-02-19 | `feature` | extracted checkNode() from ICondition to a new interface - renamed ICondition to ISelectab | `Filter.java`, `FilterComposerDialog.java` +39 | [1d33574b](https://github.com/freeplane/freeplane/commit/1d33574b0e4134a56917f55be8a09b747d89c8d3) |
| 2010-02-16 | `feature` | new methods ControllerProxy.find(ICondition) and ControllerProxy.findByRegexp(String) | `ControllerProxy.java`, `Proxy.java` | [5a4464d4](https://github.com/freeplane/freeplane/commit/5a4464d432f8efdfba1a0ccac16d2f91058b94e3) |
| 2010-02-12 | `feature` | Add methods for output to status line in scripting API to Controller | `ControllerProxy.java`, `Proxy.java` | [c9cfc6a5](https://github.com/freeplane/freeplane/commit/c9cfc6a53a9561cdf8add1480c8045f8f061daf6) |
| 2010-02-06 | `fix` | bug fix in ExecuteScriptAction undo handling | `ExecuteScriptAction.java` | [8db1a2f6](https://github.com/freeplane/freeplane/commit/8db1a2f6466b1ee98d226afe85008169a0f2aa2e) |
| 2010-01-30 | `feature` | add MapProxy with method node(id) to scripting api use generics in AbstractProxy | `AbstractProxy.java`, `AttributesProxy.java` +11 | [5063a192](https://github.com/freeplane/freeplane/commit/5063a192405a582a08da1a8b72be36b5fe298282) |
| 2010-01-23 | `feature` | extract a new interface method AttributesProxy.getAttributeNames() | `AttributesProxy.java` | [6d0b7f0f](https://github.com/freeplane/freeplane/commit/6d0b7f0f742393384ce3f1c16466130a9e87aa9c) |
| 2010-01-18 | `fix` | bug fixes for link target management | `MapController.java`, `MapModel.java` +13 | [43acb8b1](https://github.com/freeplane/freeplane/commit/43acb8b17cd9ccab343d3dfb6a400dddec1e2e07) |
| 2010-01-14 | `feature` | added scripts configuration to the OptionPanel, ohne group per script | `Resources_de.properties`, `ResourceBundles.java` +5 | [f91a4165](https://github.com/freeplane/freeplane/commit/f91a4165a628cb54efe938fd336bff6b0afc9793) |
| 2010-01-11 | `fix` | fix resource leak | `ExecuteScriptAction.java` | [df50b0dd](https://github.com/freeplane/freeplane/commit/df50b0dd10130325b4e925ae5383d83eb0650ebb) |

### Dettagli commit con note

**[84a4472c](https://github.com/freeplane/freeplane/commit/84a4472c0ce271100021ab8cdc8e55c9a894d115)** (2010-12-24) — new alternative API methods for setting and getting colors dealing with RGB strings:  - String Edge.getColorCode()  - Edge.setColorCode(rgbString)  - String Connector.getColorCode()  - Connector.setColorCode(rgbString)  - String Edge.getTextColorCode()  - Edge.setTextColorCode(rgbString)  - String Edge.getBackgroundColorCode()  - Edge.setBackgroundColorCode(rgbString)

> Use:
>   node.style.textColorCode = "#9f00fF"
>   node.text = node.style.textColorCode"

**[13a5bddc](https://github.com/freeplane/freeplane/commit/13a5bddc10aa653f528995994a6ce478a6b1e9ba)** (2010-11-13) — Fix #804: Scripting errors due to missing read permissions:

> - Reduced permission of execute_scripts_without_file_restriction to
>   pure file/read access
> 
> - Added new file/write access permission
> 
> - Implemented a validation facility for the OptionPanel for use by
>   plugins.
> 
> - Validate classpath/read permission dependency on OptionPanel submit.
> 
> - Allow use of single path.separator chars (instead of two) as
>   separator of script directories and of classpath entries.
> 
> - Improved labels and tooltips of scripting configuration items.

**[dab47919](https://github.com/freeplane/freeplane/commit/dab479199e537868bcb48e7623ec58eeb212afe0)** (2010-10-23) — Refactor condittions Add equals and hashCode methods using org.apache.commons.lang.builder.EqualsBuilder.reflectionEquals(Object, Object) and org.apache.commons.lang.builder.HashCodeBuilder.reflectionHashCode(Object) to ASelectableCondition

> Add splitting of combined conditions to conditions editor

**[1309850d](https://github.com/freeplane/freeplane/commit/1309850ddbc06d0a413751be29bb975264bbb548)** (2010-10-12) — - read plugin default from file defaults.properties to avoid hardcoded defaults. Used in scripting and formula plugin.

> - remove deprecation of ResourceController.getIntProperty(String, int) and add
>   an appropriate comment instead
> 
> - remove unused ResourceController.loadProperties(FromXML)
> 
> - formulas: changed preferences variables: enable[plugin|caching] -> disable...

**[40c1e149](https://github.com/freeplane/freeplane/commit/40c1e14960af350fc09e1936e4a113717e37629a)** (2010-08-26) — large script API overhaul mostly for formula use: * Script API / Attribute   - deprecated: Attribute.findAttribute(String) - replaced by findFirst(name)   - new: Attribute.findFirst(name) - replaces findAttribute()   - new: Attribute.clear()

> * Script API / Controller
>   - deprecated: Controller.find(ICondition) - use find(Closure) instead
>   - deprecated: Controller.setStatusInfo(infoPanelKey, icon)
>   - new: Controller.setStatusInfo(infoPanelKey, info, String iconKey)
>   - new: Controller.undo()
>   - new: Controller.newMap()
>   - new: Controller.newMap(URL)
> 
> * Script API / Map
>   - deprecated: Map.getRootNode() - use getRoot() instead
>   - new: Map.getRoot() - replaces getRootNode()
>   - new: close()
>   - new: save()
> 
> * Script API / Node
>   - new: Convertible Node.getAt(attributeName) - simple attribute access
>   - new: Convertible Node.putAt(attributeName, Object) - simple attribute access
>   - changed Node.getValue() to return Convertible
>   - new: Node.setAttributes(Map<String, Object>)
>   - removed: Node.getPlainNoteText() that was introduced after 1.1 -
>     use getNote().getPlain() instead.
>   - deprecated: Node.getPlainTextContent() - replaced by getPlainText()
>   - new: Node.getPlainText() - replaces getPlainTextContent()
>   - new: Convertible Node.getNote()
>   - deprecated: Node.find(ICondition) - use find(Closure) instead
>   - new: Node.setNote(Object) - renders setPlainNote() unnecessary
>   - deprecated: Node.setNoteText(String) - use setNote(Object) instead
>   - extended Node.setText(String) to setText(Object)
> 
> * Convertible:
>   - added isNum(), isDate()
>   - overwrite getProperty() and invokeMethod() to "extend" class String
> 
> * FreeplaneScriptBaseClass:
>   - "imports" node's methods into the script's namespace
> 
> * ScriptApiTest: extended and adjusted to API changes
> 
> * ViewController:
>   - merged addStatusInfo and addStatusImage into one addStatusInfo
>     method
>   - registered the standard status info under the name
>     STANDARD_STATUS_INFO_KEY = 'standard' in statusInfos
> * FreeplaneIconUtils (new)
>   - utility methods to access Freeplane's (builtin and user) icons.
> 
> * StringMetaClass (new)
>   - make Convertible known to class String and let String handle
>     Convertibles as if they were Strings
> 
> * ScriptingSecurityManager
>   - enabled again but only log on packageAccess errors

**[2da72e95](https://github.com/freeplane/freeplane/commit/2da72e95375cec64654569b0fdd0af6ad81cc24c)** (2010-08-01) — Preparations for spreadsheet/formula plugin:

> - Proxy: separate read-only methods from the other methods by
>   introducing 'RO' interfaces as super interface of the full
>   interfaces: Example: Proxy.Node inherits Proxy.NodeRO and is
>   implemented by NodeProxy
> 
> - added the following methods to the Scripting API:
>   Proxy.Controller: void undo();    -- mainly for testing purposes
>   Proxy.Controller: void redo();    -- mainly for testing purposes
>   Proxy.Controller: Map newMap();
>   Proxy.Controller: Map newMap(URL url);
> 
>   Proxy.Map: String getName();
>   Proxy.Map: boolean close(boolean force, boolean allowInteraction);
>   Proxy.Map: boolean save(boolean allowInteraction);
> 
> - Fix: ControllerProxy does not keep a copy of the Selection which lead to a bug when a script accesses multiple maps.
> 
> - Changed logging of script invocation errors

**[f91a4165](https://github.com/freeplane/freeplane/commit/f91a4165a628cb54efe938fd336bff6b0afc9793)** (2010-01-14) — added scripts configuration to the OptionPanel, ohne group per script

> - OptionPanel settings have a higher priority than the in-script-settings
> 
>  - this change required to add language resources dynamically and to
>    expose the method PropertyAdapter uses for key building.
> 
> TODO:
>  - improve handling of language resources (for esthetical reasons, mainly)
> 
>  - caching is not disableable via the OptionPanel (although it is
>    enableable)


---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-12-19 | `fix` | bug fixes in scripting | `MapView.java`, `ScriptingEngine.java` +1 | [09d2a805](https://github.com/freeplane/freeplane/commit/09d2a8058ae74d77f8b1aa01555594191bd241d6) |
| 2009-12-15 | `api_change` | 341]: Scripting API bugs | `Resources_ar.properties`, `Resources_ca.properties` +46 | [ed3927bf](https://github.com/freeplane/freeplane/commit/ed3927bfeb39dad3e77c1b515b89c91defcb78b0) |
| 2009-12-15 | `fix` | build patch from ewl: separate properties | `ant.properties`, `build.xml` +12 | [db2ac954](https://github.com/freeplane/freeplane/commit/db2ac9547e843ffe9123d133e7e6cb30292727f9) |
| 2009-12-06 | `feature` | 330]: New scripting API bug in proxy.Connector (?), general problem with scripting engine | `ConnectorIterator.java` | [c381c3af](https://github.com/freeplane/freeplane/commit/c381c3af68b6bfb1cce1c6c2a22bfe972be70b58) |
| 2009-11-22 | `api_change` | proxy API | `PersistentNodeHook.java`, `ExternalResource.java` +19 | [3bd96b9f](https://github.com/freeplane/freeplane/commit/3bd96b9fd523572488ef80bf3c16a885f7495509) |
| 2009-11-21 | `api_change` | script API part 1 | `ArrowType.java`, `ConnectorModel.java` +27 | [9c1dac83](https://github.com/freeplane/freeplane/commit/9c1dac834afe0125cbb200fee4645199f7dcfbe7) |
| 2009-05-18 | `fix` | bug request, feature request and help request actions | `browsemodemenu.xml`, `filemodemenu.xml` +14 | [b181724e](https://github.com/freeplane/freeplane/commit/b181724e5affeb58b2678c78e741e40c337774c4) |
| 2009-05-11 | `fix` | bug fix: disable reading of local files when running groovy scripts | `MANIFEST.MF`, `UpdateCheckAction.java` +3 | [0aff8c4b](https://github.com/freeplane/freeplane/commit/0aff8c4b6d7b9d90fc1dd0ea09aa9c8e89e90775) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
