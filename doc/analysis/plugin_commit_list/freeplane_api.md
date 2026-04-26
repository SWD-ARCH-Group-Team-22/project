# API pubblica — Commit rilevanti

**Modulo:** `freeplane_api`  
**Commit rilevanti (feature / fix / api_change):** 97 su 173 totali

> L'**API pubblica** di Freeplane: le interfacce e le classi esposte agli sviluppatori di plugin e script. Definisce il contratto stabile tra il core e le estensioni esterne.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 2 commit
- [2025](#2025) — 10 commit
- [2024](#2024) — 4 commit
- [2023](#2023) — 14 commit
- [2022](#2022) — 19 commit
- [2021](#2021) — 14 commit
- [2020](#2020) — 8 commit
- [2019](#2019) — 7 commit
- [2018](#2018) — 19 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-03-16 | `feature` | Add javadoc for tag category API | `MapTagCategories.java`, `MapTagCategoriesRO.java` +9 | [3ae0781b](https://github.com/freeplane/freeplane/commit/3ae0781b8af6f779b772eaf65236e773149e7432) |
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, script, and AI | `expose-node-tags-to-ai-tools.md`, `TagCategoryAccess.java` +44 | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-07-12 | `feature` | Scripting API: deprecate StrikedThrough, add Strikethrough | `Font.java`, `FontRO.java` +1 | [ee27a149](https://github.com/freeplane/freeplane/commit/ee27a14956ce8172aa22bd3bfcb9e8ad19085a76) |
| 2025-07-12 | `fix` | Scripting API: rename underlined to underline | `Font.java`, `FontRO.java` +1 | [67ea65c1](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2) |
| 2025-07-05 | `feature` | Issue #2560 add underline | `Resources_ar.properties`, `Resources_ca.properties` +28 | [b48e383d](https://github.com/freeplane/freeplane/commit/b48e383db28b2952d37152d5e667c4c2c53d996b) |
| 2025-06-22 | `fix` | Issue #2423 Fix paths containing RTL letters in folder and file names. | `LastOpenedList.java`, `MapViewDockingWindows.java` +2 | [708df2e1](https://github.com/freeplane/freeplane/commit/708df2e12c3e7971ffa9e9d1128edb78e8b85be7) |
| 2025-06-20 | `api_change` | Improve Bookmark API | `Node.java`, `NodeBookmark.java` +3 | [c7cf203a](https://github.com/freeplane/freeplane/commit/c7cf203af1717dfd3a21c45b6b716f6f1e5b3e00) |
| 2025-06-20 | `feature` | Add open methods to NodeBookmark API and implement in NodeBookmarkProxy class | `NodeBookmark.java`, `NodeBookmarkProxy.java` | [5ac0a772](https://github.com/freeplane/freeplane/commit/5ac0a7720f05a438e951c1f3a3dc8a950a13bee9) |
| 2025-06-15 | `feature` | Implement bookmark functionality in Freeplane node api | `BookmarkNodeAction.java`, `BookmarksController.java` +13 | [0b3743d5](https://github.com/freeplane/freeplane/commit/0b3743d5fd6f27f70eb7c8fd20ba67879b89bfa9) |
| 2025-06-15 | `api_change` | align Numbering API with API for other formatting properties | `NodeStyle.java`, `NodeStyleRO.java` +1 | [54bf4ef7](https://github.com/freeplane/freeplane/commit/54bf4ef747fe37ec18bfcf9b4a3230a54d3b79fa) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts | `OptionPanel.java`, `PathProperty.java` +29 | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-05-09 | `fix` | fix layout | `VerticalNodeViewLayoutStrategy.java`, `ChildNodesAlignment.java` | [36a31464](https://github.com/freeplane/freeplane/commit/36a31464e13ec59d108452aeec3e45e1aae8c714) |

### Dettagli commit con note

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
| 2024-05-09 | `feature` | add API methods and filters for tag categories | `preferences.xml`, `CategorizedTag.java` +13 | [b1ee9533](https://github.com/freeplane/freeplane/commit/b1ee9533bb8073270a365b1883c77e472e96f5f1) |
| 2024-05-09 | `feature` | rename methods and parameters in Tags scripting API | `Tags.java`, `TagsRO.java` +1 | [0f8d2842](https://github.com/freeplane/freeplane/commit/0f8d2842aa2bb432ea07d390cb9f8c0730e93dd7) |
| 2024-04-04 | `feature` | Add methods supporting tags to Freeplane API | `Node.java`, `NodeRO.java` +5 | [53ca172d](https://github.com/freeplane/freeplane/commit/53ca172d140794625a4d3b4fa2c5ac01a94738fb) |
| 2024-02-18 | `feature` | extend API: add get/set for followed map and associated template | `MindMap.java`, `MindMapRO.java` +1 | [574a4f2e](https://github.com/freeplane/freeplane/commit/574a4f2edbb06a5b8b78a873dc58feb8cf028e57) |

### Dettagli commit con note

**[0f8d2842](https://github.com/freeplane/freeplane/commit/0f8d2842aa2bb432ea07d390cb9f8c0730e93dd7)** (2024-05-09) — rename methods and parameters in Tags scripting API

> - change parameter names from `string` and `tag` to `keyword` -- for the string representation of a Tag -- to make it uniform across get and set, as well as to make it clear that only `keyword` is affected, not `Tag` consisting of `keyword` and `color`
> - use bare `add` and `remove` for any argument types to make it easier to type the code when creating scripts in Groovy
> - optimize `containsAll` for performance


---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-11-24 | `feature` | new api method: mindMap.copyUserStylesFrom(...) (#1541) | `MindMap.java`, `MapProxy.java` | [8d8c71a0](https://github.com/freeplane/freeplane/commit/8d8c71a04e1ad0b141f1e8e87ecebd2aeb49d6ef) |
| 2023-10-29 | `feature` | API changes (node's border and edge) (#1355) | `ComboProperty.java`, `DashIconFactory.java` +39 | [2a803599](https://github.com/freeplane/freeplane/commit/2a80359962a8ea7b3aa98caa760dd781e7ffd5c3) |
| 2023-10-03 | `feature` | wip right-to-left text writing direction support | `leftToRight.svg`, `rightToLeft.svg` +23 | [42f9c353](https://github.com/freeplane/freeplane/commit/42f9c35356f5dd6f9550bcf08b5654775ad5d659) |
| 2023-10-02 | `feature` | Add horizontal text alignment to API | `NodeStyleBuilder.java`, `NodeStyleController.java` +12 | [c54d215e](https://github.com/freeplane/freeplane/commit/c54d215e9760368c013203dd3232124c95dd7863) |
| 2023-09-10 | `fix` | combine java-doc from ConditionalStylesRO and improve docs; extend Iterable<ConditionalSty | `ConditionalStyles.java` | [e4477655](https://github.com/freeplane/freeplane/commit/e447765513c017535c3834f40ff81e0142ad48f6) |
| 2023-09-10 | `feature` | add java-doc; extend ConditionalStyleRO | `ConditionalStyle.java` | [9d3a5b8c](https://github.com/freeplane/freeplane/commit/9d3a5b8cd31b799aaf37d1cf14592326139f772f) |
| 2023-08-04 | `fix` | fix gradle deprecation warning, use java extension instead of convention | `build.gradle`, `build.gradle` +4 | [f0e70967](https://github.com/freeplane/freeplane/commit/f0e7096783a7edd362f5eb8d1055e257f906f524) |
| 2023-06-10 | `fix` | fix applet | `NodeCenter.svg`, `SetLinkByFileChooserAction.svg` +4 | [07a59724](https://github.com/freeplane/freeplane/commit/07a59724a75ef2e99130d3d3343c24a9d4ee7849) |
| 2023-05-13 | `feature` | Add node API methods getBranchAsTextOutline and appendTextOutlineAsBranch | `MapClipboardController.java`, `MindMapPlainTextWriter.java` +4 | [023d7d9d](https://github.com/freeplane/freeplane/commit/023d7d9de5adcccd492e2f2b3c0f1c14b29d9f95) |
| 2023-04-21 | `feature` | add "flow" layouts | `auto_flow.svg`, `lefttoright_bothsides_flow.svg` +10 | [13d6b37e](https://github.com/freeplane/freeplane/commit/13d6b37effc63fb2bb413f1f7458338e279fec81) |
| 2023-04-10 | `api_change` | rename flag (API!) to isStacked | `MainView.java`, `MapView.java` +5 | [996d934d](https://github.com/freeplane/freeplane/commit/996d934d65e2fe718c087885589af965403fe7d7) |
| 2023-03-03 | `feature` | Add function getChildNodesLayout to API | `Node.java`, `NodeRO.java` +1 | [93337e97](https://github.com/freeplane/freeplane/commit/93337e97902d12af2b9cb9c7f9a102abaecc37f2) |
| 2023-01-24 | `feature` | Add layouts aligning parent with first or last child | `auto_first.svg`, `auto_last.svg` +25 | [c5a40916](https://github.com/freeplane/freeplane/commit/c5a409164a27926bc13f02e4c68b347a4f62ff8a) |
| 2023-01-03 | `fix` | fix TBC version in since tag in API | `ConditionalStyle.java`, `ConditionalStyleRO.java` +3 | [46f8b646](https://github.com/freeplane/freeplane/commit/46f8b6465325c4767964f7bf3a4dea16deac3492) |

### Dettagli commit con note

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

**[e4477655](https://github.com/freeplane/freeplane/commit/e447765513c017535c3834f40ff81e0142ad48f6)** (2023-09-10) — combine java-doc from ConditionalStylesRO and improve docs; extend Iterable<ConditionalStyle>

> to fix the issue of the object not coming up as iterable in IDE
> and also so that ConditionalStylesRO can be removed

**[f0e70967](https://github.com/freeplane/freeplane/commit/f0e7096783a7edd362f5eb8d1055e257f906f524)** (2023-08-04) — fix gradle deprecation warning, use java extension instead of convention

> See https://docs.gradle.org/8.2/userguide/upgrading_version_8.html#java_convention_deprecation


---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-12-06 | `feature` | implement base distance to child nodes | `LocationBuilder.java`, `LocationController.java` +15 | [06614fd5](https://github.com/freeplane/freeplane/commit/06614fd5dfa0721230b09c7fa1f49c63a0ea4c36) |
| 2022-11-19 | `feature` | add new parent node alignments and consider them in layout for Y axis | `VerticalNodeViewLayoutStrategy.java`, `ParentNodeAlignment.java` | [552ee58c](https://github.com/freeplane/freeplane/commit/552ee58cc20dc1441c367fba73fe8cce915a0b85) |
| 2022-11-11 | `feature` | Add tool tips to node layouts | `ButtonPanelProperty.java`, `ChildNodesLayoutControlGroup.java` +2 | [f8c5d6ce](https://github.com/freeplane/freeplane/commit/f8c5d6ce28cb138ebdac48975a0c8d9c4f69e10d) |
| 2022-11-11 | `feature` | Add layouts AUTO_BYFIRST, AUTO_CENTERED and AUTO_BYLAST | `auto_byfirst.svg`, `auto_bylast.svg` +3 | [9b094340](https://github.com/freeplane/freeplane/commit/9b094340611ef8ece977808789803ea351738155) |
| 2022-11-05 | `feature` | rename some layout enum elements and add gear symbol to some SVGs | `lefttoright_bothsides_auto.svg`, `lefttoright_bottom_auto.svg` +10 | [495d08fb](https://github.com/freeplane/freeplane/commit/495d08fba7c82d490f9a066c803dfcdf8b1c0027) |
| 2022-11-04 | `feature` | wip replace old three enums by the new one | `LayoutBuilder.java`, `LayoutController.java` +16 | [598bd606](https://github.com/freeplane/freeplane/commit/598bd606c85e6d1488e499dcc3bc86c622479b66) |
| 2022-11-04 | `feature` | Add ChildNodesLayout enum and svg files | `auto.svg`, `lefttoright_bothsides_byownside.svg` +25 | [5dbc7713](https://github.com/freeplane/freeplane/commit/5dbc7713d5bfaf58c0b494b57753186f299c0718) |
| 2022-10-30 | `feature` | add more Java-doc and bump @since; refactor | `ConditionalStyle.java`, `ConditionalStyleRO.java` +12 | [219f8aeb](https://github.com/freeplane/freeplane/commit/219f8aeb0cbb60f708e8bc32d005bbe75de4e246) |
| 2022-10-30 | `feature` | add ConditionalStyles-related api | `ConditionalStyleModel.java`, `LogicalStyleController.java` +21 | [61f92526](https://github.com/freeplane/freeplane/commit/61f9252654b98faee1433e98a562c3b43392d016) |
| 2022-10-09 | `feature` | Implement layout model and controllers | `LayoutBuilder.java`, `LayoutController.java` +23 | [4f2aef94](https://github.com/freeplane/freeplane/commit/4f2aef9423a4ae60c225b7609bfb56f99a4ad69a) |
| 2022-10-09 | `api_change` | Change API to reflect both possible layout directions | `ConnectorProperties.java`, `NodeModel.java` +31 | [60010ce9](https://github.com/freeplane/freeplane/commit/60010ce96cc296de07b7740decf83887066cd901) |
| 2022-09-09 | `feature` | Add style/node property VerticalNodeLayout | `LocationBuilder.java`, `LocationController.java` +14 | [6c99f1a8](https://github.com/freeplane/freeplane/commit/6c99f1a8a7363abca2b03aa9597ab241d16bc47c) |
| 2022-09-02 | `api_change` | rename API method to get/setSideAtRoot | `Node.java`, `NodeRO.java` +1 | [a1423157](https://github.com/freeplane/freeplane/commit/a142315768fffc5c21ddbceac6781eea226dbcef) |
| 2022-08-28 | `api_change` | Change API metod names as discussed in https://github.com/freeplane/freeplane/discussions/ | `Node.java`, `NodeRO.java` +3 | [ea10a8c1](https://github.com/freeplane/freeplane/commit/ea10a8c1673e25819a57d08e170f68552e6ff4cd) |
| 2022-08-20 | `feature` | Add new methods handling node sides to freeplane API | `ControllerRO.java`, `Node.java` +5 | [37de591a](https://github.com/freeplane/freeplane/commit/37de591abc660d793d6ac2bf384b00ee5b20f78b) |
| 2022-08-19 | `fix` | fix Java doc as discussed in docs-76 | `NodeStyle.java` | [93b2216e](https://github.com/freeplane/freeplane/commit/93b2216e69249c02f2f8c197419181bd7867af49) |
| 2022-08-02 | `feature` | extend API: add MindMap getListeners | `MindMap.java`, `MapProxy.java` +2 | [ec5687d9](https://github.com/freeplane/freeplane/commit/ec5687d96a0321ebbc2b342fab0400cf79ffc802) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-01-08 | `feature` | add invisible node shape | `NodeStyleShape.java`, `BubblePainter.java` +5 | [585a63e9](https://github.com/freeplane/freeplane/commit/585a63e95e7f36111b331200cfbd5a4466931889) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-12-12 | `feature` | Add methods to NodeStyleRO: isBackgroundColorSet(), isTextColorSet(), isMinNodeWidthSet(), | `NodeStyleRO.java`, `NodeStyleProxy.java` | [48bf9a24](https://github.com/freeplane/freeplane/commit/48bf9a2417f13a989bcb98dfc4f7f978bbcc4229) |
| 2021-12-11 | `feature` | add method NodeStyleRO.isCssSet() to API | `NodeStyleRO.java`, `NodeStyleProxy.java` | [7e489e04](https://github.com/freeplane/freeplane/commit/7e489e04858b6cfff8dacfd519ba4034ab62fab6) |
| 2021-12-03 | `feature` | Add CSS getter and setter to script API | `NodeStyle.java`, `NodeStyleRO.java` +1 | [09801db2](https://github.com/freeplane/freeplane/commit/09801db27f0f86babc04417a598de27466d18605) |
| 2021-09-05 | `feature` | rename new api method | `MindMap.java`, `MapProxy.java` | [927a6fe2](https://github.com/freeplane/freeplane/commit/927a6fe255f37c7c635ce0d28b2273cc8d920ddc) |
| 2021-09-04 | `api_change` | script API MindMap.copyStyleFrom, MindMap.copyStyleConditionsFrom | `ConditionalStyleModel.java`, `LogicalStyleController.java` +3 | [d3a3125e](https://github.com/freeplane/freeplane/commit/d3a3125e27693bc467d47698e39bdcfecaab9407) |
| 2021-09-04 | `api_change` | script api List<String> NodeStyle.getAllActiveStyles() | `NodeStyleRO.java`, `NodeStyleProxy.java` | [0564a012](https://github.com/freeplane/freeplane/commit/0564a0121f22c89a02136f2c9f96ceb00be6d072) |
| 2021-06-29 | `api_change` | Remove deprecates API calls in tests | `EventTest.java`, `MemoryTest.java` +28 | [0b00408b](https://github.com/freeplane/freeplane/commit/0b00408b78fd6e687387ee661011a1cff7b27d93) |
| 2021-06-11 | `fix` | fix java applet | `kitfox-svg-salamander-1.1.1-p1.jar`, `TextUtils.java` +11 | [e18c46d5](https://github.com/freeplane/freeplane/commit/e18c46d5feec5d79d44d22e8eff6c1824d6dc59c) |
| 2021-03-13 | `feature` | Add content type getters and setters to API | `Node.java`, `NodeRO.java` +1 | [eee68e0a](https://github.com/freeplane/freeplane/commit/eee68e0a8108c9b8d257c93778d9cf48106dcf14) |
| 2021-02-07 | `fix` | fix NodeRO.getHorizontalShiftInScreenPixels | `NodeRO.java` | [ac89cc77](https://github.com/freeplane/freeplane/commit/ac89cc7762c236542c6fcda60359fd17e3d92c65) |
| 2021-02-07 | `fix` | fix NodeRO.getHorizontalShiftInScreenPixels | `NodeRO.java` | [f837b20b](https://github.com/freeplane/freeplane/commit/f837b20b8a611759173457b0eb5273a634496698) |
| 2021-01-07 | `fix` | fix test | `QuantityShould.java`, `QuantityTest.java` | [1731c019](https://github.com/freeplane/freeplane/commit/1731c019388fac43832716259b37a03b6a586518) |
| 2021-01-07 | `fix` | fix test | `QuantityShould.java`, `QuantityTest.java` | [02c8422b](https://github.com/freeplane/freeplane/commit/02c8422b30b325880aa169c8281851807b1bcc06) |
| 2021-01-06 | `feature` | add test | `build.gradle`, `QuantityTest.java` | [3967b5c9](https://github.com/freeplane/freeplane/commit/3967b5c96c912bcb1b6e9078d0599d1b4b68dcda) |

### Dettagli commit con note

**[0b00408b](https://github.com/freeplane/freeplane/commit/0b00408b78fd6e687387ee661011a1cff7b27d93)** (2021-06-29) — Remove deprecates API calls in tests

> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>


---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-30 | `api_change` | improve API export function | `ControllerRO.java`, `ControllerProxy.java` | [91516b50](https://github.com/freeplane/freeplane/commit/91516b507a4f99980c8ca5c028b00641e55f2d5b) |
| 2020-12-30 | `api_change` | You can use a substring or an empty string instead of full description in API controller.e | `ControllerRO.java`, `ControllerProxy.java` | [d5867ee5](https://github.com/freeplane/freeplane/commit/d5867ee5fe606582922970c30b0a966e141ebd5e) |
| 2020-12-13 | `feature` | Add node geometry operations to node API | `Node.java`, `NodeGeometry.java` +6 | [8b7cbc71](https://github.com/freeplane/freeplane/commit/8b7cbc71cde47a85a643e67a48618665d1b3a2bf) |
| 2020-12-13 | `api_change` | Extend freeplane API to use Quantities and Length Units | `Node.java`, `NodeRO.java` +2 | [4047c97a](https://github.com/freeplane/freeplane/commit/4047c97ae1a987e6da27a3392e4136cf01cb4992) |
| 2020-05-22 | `fix` | fix failing gradle build (#160) | `build.gradle`, `MenuBuildProcessFactoryTest.java` +3 | [e1d6707f](https://github.com/freeplane/freeplane/commit/e1d6707ffd56e705fd68a2c24caf5f4cc44e5dcf) |
| 2020-03-08 | `feature` | Add script API for hiding nodes by filter condition | `MindMap.java`, `MapProxy.java` | [f2ff5ae3](https://github.com/freeplane/freeplane/commit/f2ff5ae3559ee860c489f19c8c0d0b47f2478dda) |
| 2020-03-08 | `feature` | Add script for hiding nodes by filter condition | `MindMap.java`, `MapProxy.java` | [f0e609e9](https://github.com/freeplane/freeplane/commit/f0e609e943636140118909d72129049f10c44a2e) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-10-06 | `feature` | implement strikedThrough property of node.style.font | `Font.java`, `FontRO.java` +2 | [128a2695](https://github.com/freeplane/freeplane/commit/128a2695002680a0d4d5ae76af2027f5c2df5ee5) |
| 2019-09-28 | `feature` | Add new properties  to connector API : dashArray, opacity, width, labelFontFamily and labe | `ColorUtils.java`, `LinkBuilder.java` +10 | [f4c86c81](https://github.com/freeplane/freeplane/commit/f4c86c8129390c482d1823494186137497d77f63) |
| 2019-09-08 | `api_change` | API change: replace interface Map by MindMap, deprecate Map | `Controller.java`, `ControllerRO.java` +14 | [04b99850](https://github.com/freeplane/freeplane/commit/04b9985053bac60f98a4bbf2404b4e818d26993a) |
| 2019-08-18 | `api_change` | getMainThreadExecutorService from freeplane API | `Controller.java`, `EventQueueExecutorServiceAdapter.java` +7 | [8663a7e0](https://github.com/freeplane/freeplane/commit/8663a7e01e35cee472753500169f58d9a38b59bc) |
| 2019-08-10 | `feature` | Add NodeChangeListener to Freeplane API | `Map.java`, `NodeChangeListener.java` +5 | [746e83e0](https://github.com/freeplane/freeplane/commit/746e83e0565e3b37e24ea881802e16a2ed768b4b) |
| 2019-01-27 | `api_change` | rename API method loader to mapLoader | `Controller.java`, `HeadlessMapCreator.java` +3 | [d0125d20](https://github.com/freeplane/freeplane/commit/d0125d208316f73aabdecc896b719ab2ec5403bd) |
| 2019-01-08 | `api_change` | API for find operations including ancestors / descendants | `Filter.java`, `ControllerRO.java` +5 | [16e2a07c](https://github.com/freeplane/freeplane/commit/16e2a07cf07acf0ef1c54005c955dea44017d5f0) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-11 | `feature` | Use raw object in Convertible.isEqual and add a getter to return it | `Convertible.java`, `Convertible.java` | [7f95541d](https://github.com/freeplane/freeplane/commit/7f95541d6ffa30779a41258e1b82437287fb3bf1) |
| 2018-11-04 | `api_change` | API scripts run with all permissions | `HeadlessMapCreator.java`, `FileScriptProxy.java` +1 | [9e6f7623](https://github.com/freeplane/freeplane/commit/9e6f76231b32fa120f7fa84611e5e6e835afa43a) |
| 2018-11-04 | `feature` | add API method to execute embedded scripts | `HeadlessMapCreator.java`, `ExecuteScriptAction.java` +7 | [32a54497](https://github.com/freeplane/freeplane/commit/32a54497627291045e998cd3bbed1868bfe90446) |
| 2018-10-27 | `api_change` | API method evaluateOutdatedFormulas and small refactoring | `Map.java`, `FormulaUtils.java` +1 | [60ecf8bf](https://github.com/freeplane/freeplane/commit/60ecf8bf130ce09f02a734caa7c724c348f4ce98) |
| 2018-10-15 | `fix` | Fix docu and names | `Dependencies.java`, `DependencyLookup.java` +8 | [82aecb58](https://github.com/freeplane/freeplane/commit/82aecb5843e6667536ba8ee0af2dba85eb060d46) |
| 2018-10-15 | `api_change` | getPrecendents() and getDependents() API | `NodeAttributeTableModel.java`, `Dependencies.java` +18 | [f273ade7](https://github.com/freeplane/freeplane/commit/f273ade7ab2c3a26633cf90e04af3c28c7093379) |
| 2018-08-19 | `fix` | fix docu | `NodeRO.java` | [9840a72a](https://github.com/freeplane/freeplane/commit/9840a72acdf21fc47e1b6fa3933d14c1090eb37e) |
| 2018-08-19 | `api_change` | extend and document API | `HeadlessMapCreator.java`, `Script.java` +2 | [b322ea37](https://github.com/freeplane/freeplane/commit/b322ea37a0dad701ac72fdb3acac57ee85817977) |
| 2018-08-15 | `feature` | new syntax for map explorer | `Command.java`, `ExploringStep.java` +6 | [cfbf1914](https://github.com/freeplane/freeplane/commit/cfbf191415358b590fec8900f68b2f35d3042b65) |
| 2018-08-05 | `fix` | fix docu | `NodeRO.java` | [91551f7c](https://github.com/freeplane/freeplane/commit/91551f7c1cd1c0f0ad6da548c1b3e0bd6c14273c) |
| 2018-08-05 | `fix` | fix docu | `NodeRO.java` | [d9604ff5](https://github.com/freeplane/freeplane/commit/d9604ff583eac1cbb0f818c01f6ff22d6add6820) |
| 2018-07-31 | `feature` | Let new API be valid from version 1.7.1 | `AttributesRO.java`, `Controller.java` +4 | [5c217046](https://github.com/freeplane/freeplane/commit/5c217046bea6b9305a4b622521040818d229cc86) |
| 2018-07-31 | `api_change` | extend API | `Node.java`, `NodeRO.java` +1 | [e4bc8231](https://github.com/freeplane/freeplane/commit/e4bc82315c8d23f4500492dfa3113619c2b9ebd7) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [79de8564](https://github.com/freeplane/freeplane/commit/79de85641fe2c7d9cbb2ecc79238a18fa8b8ae18) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [bb1e7869](https://github.com/freeplane/freeplane/commit/bb1e78694778a47fff37f07484c283126847b8ed) |
| 2018-07-19 | `api_change` | MapLoader api and refactoring | `MapController.java`, `MapModel.java` +14 | [d2c45816](https://github.com/freeplane/freeplane/commit/d2c458160eb4a8a1bdb2004903315b5d7c20c444) |
| 2018-07-11 | `api_change` | loader api | `Controller.java`, `HeadlessLoader.java` +5 | [b64c78d5](https://github.com/freeplane/freeplane/commit/b64c78d5c624e8a20c4c42aaac4063d42b7a6cc1) |
| 2018-07-08 | `api_change` | rename API methods newMap -> openMap, newMapFromTemplate -> openUntitledMap, hiddenMap ->  | `EncryptedMap.java`, `XmlImporter.java` +24 | [a76dc05a](https://github.com/freeplane/freeplane/commit/a76dc05a3fe1d4bb41c642401861949053f14b9e) |
| 2018-07-08 | `feature` | Add API method Controller.hiddenMap | `MMapController.java`, `MMapIO.java` +4 | [ba2c7706](https://github.com/freeplane/freeplane/commit/ba2c77064878fb9001a497a3467801cb7eb010f9) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
