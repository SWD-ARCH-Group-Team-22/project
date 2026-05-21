# Core — Commit rilevanti

**Modulo:** `freeplane_core`  
**Commit rilevanti (feature / fix / api_change):** 3130 su 13039 totali

> Il **nucleo** dell'applicazione: gestione delle mappe `.mm`, rendering del canvas, sistema di nodi/edge, filtri, export, UI principale e tutto ciò che non è un plugin separato.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 40 commit
- [2025](#2025) — 324 commit
- [2024](#2024) — 166 commit
- [2023](#2023) — 182 commit
- [2022](#2022) — 180 commit
- [2021](#2021) — 227 commit
- [2020](#2020) — 117 commit
- [2019](#2019) — 56 commit
- [2018](#2018) — 83 commit
- [2017](#2017) — 129 commit
- [2016](#2016) — 247 commit
- [2015](#2015) — 270 commit
- [2014](#2014) — 89 commit
- [2013](#2013) — 92 commit
- [2012](#2012) — 164 commit
- [2011](#2011) — 284 commit
- [2010](#2010) — 241 commit
- [2009](#2009) — 239 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-03-29 | `feature` | 2026-03-29-copy-markdown Add chat markdown copy action | `020-copy-selected-visible-chat-blocks-as-markdown.md`, `Resources_de.properties` +6 | [235726bb](https://github.com/freeplane/freeplane/commit/235726bb73c0097f6b7d451e8cf2f7c0e9ea11e6) |
| 2026-03-16 | `feature` | add methods that determine childNodesLayout origin | `LayoutController.java` | [94b7deb4](https://github.com/freeplane/freeplane/commit/94b7deb42a4a962a65d89d8c9a0e0d869856599a) |
| 2026-03-16 | `feature` | make it clear that getStyles returns List (ordered); add JavaDoc | `LogicalStyleController.java` | [3fabbea3](https://github.com/freeplane/freeplane/commit/3fabbea32825e20adb663fa17f98b68c7449c572) |
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, script, and AI | `expose-node-tags-to-ai-tools.md`, `TagCategoryAccess.java` +44 | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |
| 2026-03-15 | `fix` | Issue #2845 fix locking view root node with password | `NodeView.java` | [cf1d28d6](https://github.com/freeplane/freeplane/commit/cf1d28d6bc2cdd0b500f112ba209554955d40da8) |
| 2026-02-20 | `feature` | Add tag category characterization baseline tests (2026-02-20-expose-tags-ai-tools) | `expose-node-tags-to-ai-tools.md`, `TagCategoriesTest.java` +1 | [290c2cff](https://github.com/freeplane/freeplane/commit/290c2cff344058fb8ce9da0eb8a360dfb3c678e7) |
| 2026-02-20 | `api_change` | 2026-02-20-expose-styles-ai-tools Expose styles in AI tools and unify list API | `expose-node-styles-to-ai-tools.md`, `expose-node-tags-to-ai-tools.md` +30 | [5432e96f](https://github.com/freeplane/freeplane/commit/5432e96f9c9492b88242fcbaec14455da46f731b) |
| 2026-02-20 | `feature` | 2026-02-20-mcp-bearer: support MCP bearer auth with legacy fallback | `012-extend-mcp-authentication-with-bearer-token-support.md`, `Resources_en.properties` +5 | [011b24a2](https://github.com/freeplane/freeplane/commit/011b24a255e75801e93a2d6b8cfe02038613d5db) |
| 2026-02-20 | `feature` | 2026-02-20-ollama-token-auth: add Ollama token auth and cache invalidation | `extend-mcp-authentication-with-bearer-token-support.md`, `011-enable-remote-ollama-endpoint-authentication.md` +13 | [a7d66d2c](https://github.com/freeplane/freeplane/commit/a7d66d2c18f8d25c59be07d8f223ddca8242e8df) |
| 2026-02-15 | `fix` | Fix svg icons using accent colors | `FixedSizeUIIcon.java` | [0b006673](https://github.com/freeplane/freeplane/commit/0b006673bd50dcd9161833d629e2b5496535dca9) |
| 2026-02-15 | `fix` | 2026-02-15-secret-property-reads: extract ApplicationPropertyStore and fix secret property | `006-fix-application-resource-controller-secret-property-reads.md`, `ResourceController.java` +4 | [899ffda0](https://github.com/freeplane/freeplane/commit/899ffda0eee42b40c4d9132e19709d2222e73ec7) |
| 2026-02-14 | `feature` | 2026-02-14-ai-panel-font-size: scale AI panel styles and add configurable font size | `ai-panel-scaled-style-and-configurable-font-size.md`, `Resources_en.properties` +7 | [dae8d16b](https://github.com/freeplane/freeplane/commit/dae8d16bc1556f2b36bca9ee15e89d0de7f99306) |
| 2026-02-14 | `feature` | 2026-02-14-bootstrap-activator: add Java 8 bootstrap activator with Java 17 runtime gating | `java-eight-bootstrap-activator-for-ai-plugin.md`, `build.gradle` +4 | [92367151](https://github.com/freeplane/freeplane/commit/923671512a2b2658c7a8496da3f6085461b301c0) |
| 2026-02-09 | `feature` | 2026-02-05-mcp-authentication: Add MCP API key auth with generated key flow | `add-mcp-server-api-key-authentication.md`, `051-add-mcp-server-api-key-authentication.md` +7 | [a1b8d59c](https://github.com/freeplane/freeplane/commit/a1b8d59c8fa1c04f1b413efcf371322b386855b9) |
| 2026-02-08 | `feature` | 2026-02-05-secret-settings: add secret settings field with show/hide icons | `add-secret-field-type-for-settings.md`, `046-add-secret-field-type-for-settings.md` +8 | [76ee422b](https://github.com/freeplane/freeplane/commit/76ee422b2abeacfc8a68b3d1f4f708e37aa60408) |
| 2026-02-08 | `feature` | 2026-02-08-profile-menu: add AI profile manager menu entry | `045-add-ai-profile-manager-menu-item-in-chat-panel.md`, `Resources_en.properties` +2 | [46b78cf5](https://github.com/freeplane/freeplane/commit/46b78cf5d1e14486c09b2213340c80797529893a) |
| 2026-02-06 | `fix` | fix profile icon | `EggheadCB.svg` | [76f609e8](https://github.com/freeplane/freeplane/commit/76f609e80afd92112a267d5cd4cc4bf2a5070ddc) |
| 2026-02-06 | `feature` | 2026-02-03-assistant-profiles: add profile management UI, structured profile transcript en | `AGENTS.md`, `chat-memory-system-messages.md` +32 | [63c83935](https://github.com/freeplane/freeplane/commit/63c83935626315cf774bb8bd355c9f5573cb89d6) |
| 2026-02-02 | `feature` | Add user readme about configuration location. | `freeplane-1-13-configuration-directory-handling.md`, `userReadme_1.13.txt` +3 | [f5e3b154](https://github.com/freeplane/freeplane/commit/f5e3b154e06c20bc2c0ee1b5062cc8a378d9638d) |
| 2026-02-01 | `fix` | fix NPE | `TimeDelayedOutlineSelection.java` | [085bd1c8](https://github.com/freeplane/freeplane/commit/085bd1c801fb60b3e4311c7c3284d0222aeb9733) |
| 2026-02-01 | `feature` | 2026-01-31-ai-chat: Add cancel shortcut and tooltips | `Resources_en.properties`, `038-ai-chat-cancel-shortcut-tooltips.md` +1 | [d36450d3](https://github.com/freeplane/freeplane/commit/d36450d3287be6d4e789eb7e87195252b9819212) |
| 2026-01-31 | `feature` | Add send shortcut tooltip | `Resources_en.properties`, `AIChatPanel.java` | [94ddcb98](https://github.com/freeplane/freeplane/commit/94ddcb98298172198c244194a91adbbacbe8ac16) |
| 2026-01-31 | `feature` | 2026-01-31-stop-chat-non-streaming: implement stop control and split tasks | `Resources_es.properties`, `Resources_uk_UA.properties` +14 | [51a67ce2](https://github.com/freeplane/freeplane/commit/51a67ce2f0f52e3bfdac0b67815c01accbe511e2) |
| 2026-01-31 | `feature` | 2026-01-24-chat-history-transcripts: add icons, map count merge, and tests | `Resources_es.properties`, `Resources_uk_UA.properties` +14 | [6d9263a7](https://github.com/freeplane/freeplane/commit/6d9263a7b329ac9d62a71bf893caa4c9ab8ece6b) |
| 2026-01-31 | `feature` | 2026-01-24-chat-history-transcripts: add transcript chat restore and list UX | `Resources_es.properties`, `Resources_en.properties` +23 | [9b5fc38f](https://github.com/freeplane/freeplane/commit/9b5fc38f7b6b288a926f90b2554f7400c1fdd7fd) |
| 2026-01-30 | `fix` | fix Class Cast Exception | `MapViewDockingWindows.java` | [a82af670](https://github.com/freeplane/freeplane/commit/a82af67062bf566c36a932c2fc3990c12d55efda) |
| 2026-01-30 | `fix` | fix NPE | `NodeSelector.java` | [21f68398](https://github.com/freeplane/freeplane/commit/21f683984785f38be4d5b14c6d1dc94688e9ead8) |
| 2026-01-30 | `fix` | fix NPE | `NodeView.java` | [b8ae03e1](https://github.com/freeplane/freeplane/commit/b8ae03e14060f2f847209f0eab38be4e134a40dd) |
| 2026-01-30 | `fix` | fix NPE | `UndoHandler.java` | [39663fa8](https://github.com/freeplane/freeplane/commit/39663fa8d098877ce220c9360245920dd9e24dee) |
| 2026-01-30 | `fix` | fix NPE | `MapAwareOutlinePane.java` | [d7e59624](https://github.com/freeplane/freeplane/commit/d7e596247761ff03ec3e264cb1d6578afc5dcc05) |
| 2026-01-25 | `feature` | 2026-01-25-tool-set-refinement: refine tool descriptions and create folding options | `MapController.java`, `Resources_en.properties` +34 | [e7ba9cee](https://github.com/freeplane/freeplane/commit/e7ba9cee6203b19dad4217cda8316eb77ecc56e8) |
| 2026-01-19 | `feature` | 2026-01-17-ai-edits: add AI edits persistence and preferences | `AGENTS.md`, `Resources_en.properties` +8 | [ea719fdc](https://github.com/freeplane/freeplane/commit/ea719fdc2ff99d8df7aeafa3de4333f31e08de71) |
| 2026-01-18 | `fix` | fix NPE for bookmarks opened as view roots and having no parent node view | `NodeView.java` | [74c3603f](https://github.com/freeplane/freeplane/commit/74c3603f88ae303b3a4ceb7970a40b1580f25d08) |
| 2026-01-17 | `feature` | Implement AI edit markers and document design proposal | `freeplane.properties`, `ai.svg` +17 | [3accecf0](https://github.com/freeplane/freeplane/commit/3accecf0a4d59d274872c20d0e2e66d98ee7b366) |
| 2026-01-14 | `feature` | Add ai use ollama label | `Resources_en.properties` | [b5bd5a2a](https://github.com/freeplane/freeplane/commit/b5bd5a2a0f5b428309f4984349216afb5e2477e2) |
| 2026-01-14 | `feature` | Add ai model allowlist translations | `Resources_en.properties` | [b2f825c3](https://github.com/freeplane/freeplane/commit/b2f825c33acbc83e09b9722ee24e9b0dd36e9873) |
| 2026-01-10 | `feature` | Implement tool to create summary nodes using error handler | `MMapController.java`, `add-node-create-and-move-tools-with-anchor-and-summary-rules.md` +8 | [ac09ee3d](https://github.com/freeplane/freeplane/commit/ac09ee3d20a28c08a28573609eeb007912b96cf1) |
| 2026-01-09 | `feature` | Add tools to create and move nodes | `HtmlProcessor.java`, `Tags.java` +31 | [0dc8972e](https://github.com/freeplane/freeplane/commit/0dc8972ea7b95ec349d1125f565d8cd2a5eb6276) |
| 2026-01-06 | `feature` | Add "toggle map outline" action to file mode | `filemodemenu.xml` | [0d2b7b52](https://github.com/freeplane/freeplane/commit/0d2b7b525ddb02b236180ffc282bf9c7002d6907) |
| 2026-01-03 | `feature` | Add MCP server to freeplane | `Resources_en.properties`, `build.gradle` +12 | [747ada3e](https://github.com/freeplane/freeplane/commit/747ada3e271e27a183c08a2845d9892011fb09f2) |

### Dettagli commit con note

**[235726bb](https://github.com/freeplane/freeplane/commit/235726bb73c0097f6b7d451e8cf2f7c0e9ea11e6)** (2026-03-29) — 2026-03-29-copy-markdown Add chat markdown copy action

> Add an explicit Copy Markdown action that exports whole chat blocks intersected by the current selection or caret-containing block, wire it into the chat popup and context menu, add translations and focused tests, and move the task spec to done.


---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-12-28 | `feature` | add preferences | `Resources_en.properties`, `build.gradle` +9 | [5f52d246](https://github.com/freeplane/freeplane/commit/5f52d2468bb32f3e39b9be41d7a76833a9fe76fa) |
| 2025-12-26 | `fix` | Fix Out Of Memory on reloading huge code maps in code explorer | `SelectionActor.java`, `CodeMapController.java` | [0e84baf5](https://github.com/freeplane/freeplane/commit/0e84baf5221c7a08001a94413c5a6105fa72838a) |
| 2025-12-26 | `fix` | fix NavigationButtonHider: allow only one navigationButtons instance and hide others | `NavigationButtonHider.java` | [a87b6501](https://github.com/freeplane/freeplane/commit/a87b6501d78718564471a05aeeec19c84bc84fc8) |
| 2025-12-26 | `fix` | fix NavigationButtonHider:  reset hovered node only on event | `NavigationButtonHider.java` | [805b2c4c](https://github.com/freeplane/freeplane/commit/805b2c4c1be38d970fbb0c5231628944a1710a0b) |
| 2025-12-26 | `fix` | fix NavigationButtonHider:  avoid multiple instances of mouseMovementDetector | `NavigationButtonHider.java`, `VisibleOutlineNodes.java` | [726bc5ed](https://github.com/freeplane/freeplane/commit/726bc5edf6076ec665f1f7247e8c573df1668932) |
| 2025-12-26 | `fix` | fix NPE | `MapAwareOutlinePane.java` | [7b4efb3e](https://github.com/freeplane/freeplane/commit/7b4efb3e90b7cf57e1178fed5789f840e0b7fd13) |
| 2025-12-26 | `fix` | fix NPE | `MapAwareOutlinePane.java` | [29526e2d](https://github.com/freeplane/freeplane/commit/29526e2d0a72894f4142123a443de4d8a7f80b15) |
| 2025-12-21 | `fix` | Issue #2782 Bug: error when moving node | `OutlinePane.java`, `ScrollableTreePanel.java` +1 | [5a6afbb9](https://github.com/freeplane/freeplane/commit/5a6afbb94b2ea49fe15fe145987b48775e726e32) |
| 2025-12-15 | `fix` | Fix automatic layout side calculation for first level nodes | `LayoutController.java` | [6bd15ca8](https://github.com/freeplane/freeplane/commit/6bd15ca8c71dbd5f693b6bdef5f0689d0eea7bc2) |
| 2025-12-15 | `fix` | revert some old changes and finish layout fix | `VerticalNodeViewLayoutStrategy.java` | [1d76004d](https://github.com/freeplane/freeplane/commit/1d76004d656fa66678c44bde5483dbbf9678274d) |
| 2025-12-10 | `fix` | inline methods, fix layout calculation considering handles | `VerticalNodeViewLayoutStrategy.java` | [c98f9227](https://github.com/freeplane/freeplane/commit/c98f9227fd4c2187db118d99c72b4292a476d273) |
| 2025-12-01 | `fix` | Fix collapsing breadcrumb nodes | `ScrollableTreePanel.java` | [d8ce76d4](https://github.com/freeplane/freeplane/commit/d8ce76d43ddfac16b38c2b0a8d432487fbee5266) |
| 2025-11-30 | `fix` | Fix horizontal outline view scrolling | `OutlinePane.java`, `OutlineViewport.java` +1 | [5f71270f](https://github.com/freeplane/freeplane/commit/5f71270f10dc3265b1c9ba17a95370a0d3d0804b) |
| 2025-11-30 | `fix` | Fix horizontal outline view scrolling | `OutlineViewport.java` | [9f2072bb](https://github.com/freeplane/freeplane/commit/9f2072bbf1ff4851b884cfc2fdbd6a771933012c) |
| 2025-11-30 | `feature` | Support RTL languages in outline | `Resources_af.properties`, `Resources_cs.properties` +29 | [886c10b6](https://github.com/freeplane/freeplane/commit/886c10b697acd9161c5c1d9ff6ac4363547d7142) |
| 2025-11-23 | `feature` | Upgrade AES encryption from CBC to GCM mode | `Aes256Encrypter.java`, `Aes256EncrypterTest.java` | [214baa9b](https://github.com/freeplane/freeplane/commit/214baa9ba91823c6c50e33e090769984a8fe338c) |
| 2025-11-23 | `feature` | Feature/aes 256 encryption (#2726) | `.gitignore`, `Aes256Encrypter.java` +12 | [73858dd9](https://github.com/freeplane/freeplane/commit/73858dd970b75061e1b1396a3f2a9efd710d1e2c) |
| 2025-11-17 | `fix` | Fix outline node scrolling | `ScrollableTreePanel.java` | [a1b61bfc](https://github.com/freeplane/freeplane/commit/a1b61bfc143c4081ca1dcae3d4ac490dbd114947) |
| 2025-11-16 | `feature` | Add predefined filters to outline filter menu | `TextIcon.java`, `FilterController.java` +2 | [6882eb56](https://github.com/freeplane/freeplane/commit/6882eb56ea76c23b7e063829a79c2a1fcd08ff77) |
| 2025-11-16 | `fix` | Fix block panel scrolling | `OutlineViewport.java`, `ScrollableTreePanel.java` | [90c03e44](https://github.com/freeplane/freeplane/commit/90c03e4414e6bd5804dadfbedb9f56135e096715) |
| 2025-11-15 | `fix` | Fix editor background color for node details | `MMapViewController.java` | [ab7fd3a5](https://github.com/freeplane/freeplane/commit/ab7fd3a554599f65addad48950acdd526ba60570) |
| 2025-11-15 | `fix` | Fix editor background color | `EditNodeWYSIWYG.java` | [42bdde12](https://github.com/freeplane/freeplane/commit/42bdde12fe522cb827b11fd0634b1564ba363ba2) |
| 2025-11-11 | `feature` | Add outline toggle to code exporer menus | `codeexplorermodemenu.xml` | [7cbf62e4](https://github.com/freeplane/freeplane/commit/7cbf62e49c85eb93097ddc73a8e92204f5ebe49b) |
| 2025-11-07 | `fix` | Issue #2730 Consider outline filter when nodes are deleted, inserted or moved. Fix outline | `MapController.java`, `MapModel.java` +3 | [4c105fb8](https://github.com/freeplane/freeplane/commit/4c105fb86278d2a514a7e7f7cd83a10c5b56cb56) |
| 2025-11-07 | `fix` | fix outline block panel positioning | `ScrollableTreePanel.java` | [a0771692](https://github.com/freeplane/freeplane/commit/a0771692274fd2f6fb9d199dd1c7488170cf2e52) |
| 2025-11-07 | `fix` | fix NPE | `BreadcrumbPanel.java` | [29610d8b](https://github.com/freeplane/freeplane/commit/29610d8b82f263162cf239e9258ba0d3fb9d4cdb) |
| 2025-11-06 | `fix` | Fix underline for non colored outline items | `TextIcon.java`, `MapTreeNode.java` +1 | [37adf0c7](https://github.com/freeplane/freeplane/commit/37adf0c7765e171966ec933d58333463e314b754) |
| 2025-11-03 | `fix` | Fix navigation buttons: they were hidden on attachNode | `NavigationButtonHider.java`, `NavigationButtons.java` | [cf80c5ad](https://github.com/freeplane/freeplane/commit/cf80c5ad5a5e073e57bdc8029787c28f39708ca7) |
| 2025-11-03 | `fix` | Fix concurrent modification exception | `MapModel.java` | [5b1ffdfe](https://github.com/freeplane/freeplane/commit/5b1ffdfed756193baf4a7d9fc1268fd2c9c1a76a) |
| 2025-11-01 | `fix` | Fix breadcrumb node selection in the outline | `OutlineFocusManager.java` | [d0aa9143](https://github.com/freeplane/freeplane/commit/d0aa9143055354fbd269445da26a80271afca4a6) |
| 2025-11-01 | `fix` | Fix NPE / selection error after multiple node deletion | `MapView.java` | [7c810c0a](https://github.com/freeplane/freeplane/commit/7c810c0a6ac564472269c82b0c1c43a168fdbdb0) |
| 2025-11-01 | `api_change` | Introduce functional interface FilterUpdateListener | `Filter.java`, `FilterUpdateListener.java` | [d13bf1f3](https://github.com/freeplane/freeplane/commit/d13bf1f3e43bd10dbcde3a9ffb1578ae8f84f608) |
| 2025-10-26 | `fix` | Fix tests | `MapBookmarksTest.java` | [46207009](https://github.com/freeplane/freeplane/commit/46207009555b22bafd1e8aacc909784caa8ff34e) |
| 2025-10-26 | `feature` | Do not bookmark the root node on new maps | `MapBookmarks.java` | [aa3c180d](https://github.com/freeplane/freeplane/commit/aa3c180d3794b40a9a6372110a6a2e3f4b46c482) |
| 2025-10-23 | `feature` | Add quick filter to outline | `FilterCache.java`, `MapAwareOutlinePane.java` +2 | [de8c0da5](https://github.com/freeplane/freeplane/commit/de8c0da5d28c037c130783b6e798983f488f5fad) |
| 2025-10-23 | `feature` | Issue #2710 Constant full CPU core load of bookmark opened as root in new view | `NodeView.java` | [5abb6c26](https://github.com/freeplane/freeplane/commit/5abb6c264a02d5d15a129674410bffae437a58f4) |
| 2025-10-10 | `fix` | fix outline node reduce/expand operations | `ExpansionControls.java`, `TreeNode.java` | [afc15a51](https://github.com/freeplane/freeplane/commit/afc15a514994dd768b07a8d8bf8da48175074a6f) |
| 2025-10-10 | `fix` | Fix class cast exception | `DefaultMapMouseListener.java` | [1da5a64f](https://github.com/freeplane/freeplane/commit/1da5a64f1eab7c37cb55ad8f9a06e192052093f0) |
| 2025-10-06 | `fix` | Fix regression | `DefaultMapMouseListener.java`, `DefaultNodeMouseMotionListener.java` | [b663ad05](https://github.com/freeplane/freeplane/commit/b663ad05458d314468278fd13a2723f1f9afb5e5) |
| 2025-10-05 | `feature` | Issue #2694 Add option to disable status message after automatic save | `preferences.xml`, `DoAutomaticSave.java` +2 | [bcd66cce](https://github.com/freeplane/freeplane/commit/bcd66cce3785537f8ad9c605a1110016f511ba6e) |
| 2025-10-05 | `fix` | fix resize | `AuxillaryEditorSplitPane.java` | [b57d420a](https://github.com/freeplane/freeplane/commit/b57d420a8a1248b908275e9e82a75c39c609f127) |
| 2025-10-04 | `fix` | Fix focus after selection | `OutlineSelectionBridge.java` | [e6d55d38](https://github.com/freeplane/freeplane/commit/e6d55d38adfa3061bf85a2251d177bafd5d04daa) |
| 2025-10-04 | `fix` | refactor and fix layout | `BlockPanel.java`, `BreadcrumbPanel.java` +7 | [85db286b](https://github.com/freeplane/freeplane/commit/85db286bfb7f9ebc1dea9cd10d8dedb002cbc289) |
| 2025-10-03 | `fix` | fix breadcrumb selection update | `ScrollableTreePanel.java` | [bcf3eb82](https://github.com/freeplane/freeplane/commit/bcf3eb823858cc86c68481f6108c336828fde792) |
| 2025-10-02 | `fix` | Fix outline item button size | `BlockPanel.java`, `BreadcrumbPanel.java` +4 | [bedb085e](https://github.com/freeplane/freeplane/commit/bedb085ec749f15b7fb9134c66d21b878849f356) |
| 2025-09-26 | `fix` | Issue #2627 Fix selection after moving nodes between different views of the same mind map | `MNodeDropListener.java` | [e3d2f1f4](https://github.com/freeplane/freeplane/commit/e3d2f1f47716c0ecfa3bd0754aa71593239646fb) |
| 2025-09-26 | `fix` | fix field initialization | `ScrollableTreePanel.java` | [96d7466d](https://github.com/freeplane/freeplane/commit/96d7466dd60dd85fa44bcb42943135305fb36c13) |
| 2025-09-24 | `feature` | Add padding to text on colored outline items | `TextIcon.java`, `MapTreeNode.java` | [d0098be8](https://github.com/freeplane/freeplane/commit/d0098be8ee509ad0cdd6af489669f02075183c82) |
| 2025-09-24 | `fix` | Issue #2682 Fix class cast exception | `ViewerController.java`, `LatexNodeHook.java` | [3de9d1e2](https://github.com/freeplane/freeplane/commit/3de9d1e2cedcb46254e6999d3ee8ad32a67e491c) |
| 2025-09-23 | `fix` | Fix node visibility check | `MapAwareOutlinePane.java`, `ScrollableTreePanel.java` | [447472b7](https://github.com/freeplane/freeplane/commit/447472b7c5969bea713a8fb25fd3ed4dbfe7bc42) |
| 2025-09-22 | `feature` | Add outline preferences action | `OutlineActions.java` | [84ec9322](https://github.com/freeplane/freeplane/commit/84ec9322822efac9e749f133eeba6984d0602290) |
| 2025-09-22 | `feature` | refactor highlighting properties in option panel and support separated groups | `HighlightablePropertyControl.java`, `OptionPanel.java` +5 | [efe1388d](https://github.com/freeplane/freeplane/commit/efe1388d763e6c15eea3db534900f316173828a1) |
| 2025-09-20 | `fix` | Fix font scaling | `BlockPanel.java`, `BreadcrumbPanel.java` +2 | [54ef2ae2](https://github.com/freeplane/freeplane/commit/54ef2ae2e9e68c3f8975df813424b04f5eb267c9) |
| 2025-09-20 | `fix` | Fix NPE | `OutlineFocusManager.java` | [1f926b5a](https://github.com/freeplane/freeplane/commit/1f926b5a93b6dcd3860b17d9361def9735bc50d6) |
| 2025-09-20 | `fix` | fix class cast exception | `MapViewDockingWindows.java` | [6e0b048d](https://github.com/freeplane/freeplane/commit/6e0b048d3766b86cd37e2441d8e31eaed1491085) |
| 2025-09-20 | `feature` | Enable outline node drag and clipboard integration | `BookmarkDragGestureListener.java`, `NodeButton.java` +2 | [e2456a34](https://github.com/freeplane/freeplane/commit/e2456a34809e21a29820befaf1e2608c0b75aa18) |
| 2025-09-20 | `feature` | Add navigation actions to outline nodes | `NodeBookmark.java`, `NodeNavigator.java` +5 | [253cac48](https://github.com/freeplane/freeplane/commit/253cac48d3736ee4b623a21cac202c175b546f2c) |
| 2025-09-20 | `feature` | Add bookmark outline mode infrastructure | `MapBookmarks.java`, `BookmarkModeFilterCache.java` +5 | [6b07b34e](https://github.com/freeplane/freeplane/commit/6b07b34e3e57fabbb71c101d102ac85ee9b5aae6) |
| 2025-09-20 | `feature` | Open selection as root in a new view (alt+shift+ESCAPE) | `history_en.txt`, `mindmapmodemenu.xml` +4 | [63953bf0](https://github.com/freeplane/freeplane/commit/63953bf0d446c6ef1263b252a0a42da9a384f725) |
| 2025-09-16 | `feature` | Issue #2668 Open as Root in New View - misses the context-selected bookmark | `NodeBookmark.java` | [c66a0c77](https://github.com/freeplane/freeplane/commit/c66a0c77d4963c5f08694c20a7cbf51f1632cce0) |
| 2025-09-14 | `feature` | Issue #2667: Highlight ascendant edges using selection rectangle color | `mindmapmodemenu.xml`, `preferences.xml` +6 | [a8bcb1c3](https://github.com/freeplane/freeplane/commit/a8bcb1c3ad1ddf7f4885ee0c43a763726a7fe1ea) |
| 2025-09-14 | `fix` | fix update after insertion/deletion | `NodeTreeBuilder.java`, `OutlineBlockLayout.java` +3 | [0845038a](https://github.com/freeplane/freeplane/commit/0845038a4c9a82dfe4d09f984a4089ec1fd7713e) |
| 2025-09-13 | `api_change` | Outline: align breadcrumb panel with viewport inner area and clarify API | `BreadcrumbPanel.java`, `OutlinePane.java` | [2f589672](https://github.com/freeplane/freeplane/commit/2f589672b13c08b403bc59776124ab7f0f21e5fd) |
| 2025-09-13 | `fix` | Fix outline layout | `BlockPanel.java`, `NodePositioning.java` +4 | [ef50a2e7](https://github.com/freeplane/freeplane/commit/ef50a2e7f95007bae183f7f941cc8a7528e3d0eb) |
| 2025-09-13 | `feature` | Outline: add "Select in Map" action to burger menu (Enter)\n\n- OutlineActions: add select | `OutlineActionTarget.java`, `OutlineActions.java` +4 | [256728e5](https://github.com/freeplane/freeplane/commit/256728e5dc2a3f733d28f4975f7a9a5af5bea477) |
| 2025-09-13 | `feature` | Outline: add top toolbar with right‑aligned burger button and actions menu\n\n- OutlinePan | `TranslatedElementFactory.java`, `BreadcrumbPanel.java` +7 | [a79da5e7](https://github.com/freeplane/freeplane/commit/a79da5e77f4e733a17678f576b238289f34d9aad) |
| 2025-09-12 | `feature` | outline: cleanup and visibility fixes | `BlockPanel.java`, `BreadcrumbPanel.java` +10 | [8fd28351](https://github.com/freeplane/freeplane/commit/8fd28351dec4e78c0fb7b56728a1f4c23fb25e83) |
| 2025-09-12 | `feature` | outline: fix selection visibility check using viewport indices; add isNodeActuallyVisible  | `OutlineSelectionManager.java`, `ScrollableTreePanel.java` | [59486beb](https://github.com/freeplane/freeplane/commit/59486bebf14e01a98e651f244b263e0a473b4c2d) |
| 2025-09-12 | `feature` | outline: restore scroll debounce pattern and add bounded selection visibility stabilizatio | `BlockPanel.java`, `BreadcrumbPanel.java` +5 | [efc2b776](https://github.com/freeplane/freeplane/commit/efc2b776fbcba2f94db993390e69feccbade2281) |
| 2025-09-12 | `fix` | fix(outline): do not force root.applyExpansionLevel(1) in ScrollableTreePanel; rely on Nod | `MapAwareOutlinePane.java`, `ScrollableTreePanel.java` | [2edb8d3b](https://github.com/freeplane/freeplane/commit/2edb8d3ba2d2d73dc86ded539cd59f980e4eda54) |
| 2025-09-12 | `feature` | test(outline/phase7): add AssertJ tests for BreadcrumbPath and OutlineSelectionManager | `UITools.java`, `REFACTORING.md` +2 | [5ebe3500](https://github.com/freeplane/freeplane/commit/5ebe35001df44f8ac5d75de9f7becd770cd613ac) |
| 2025-09-12 | `feature` | test(outline/phase7): add AssertJ-based tests for NodePositioning and OutlineViewport/Visi | `REFACTORING.md`, `NodePositioningTest.java` +1 | [5661e275](https://github.com/freeplane/freeplane/commit/5661e2754a2ce6975ba9903eca4ebad01df992f2) |
| 2025-09-12 | `feature` | refactor(outline/phase6): delegate setSelectedNode orchestration to OutlineSelectionManage | `OutlineSelectionManager.java`, `REFACTORING.md` +1 | [589d09ef](https://github.com/freeplane/freeplane/commit/589d09ef41a9add470303a30da12e6e4154838d7) |
| 2025-09-12 | `fix` | fix NPE | `MapTreeNode.java` | [0dccf298](https://github.com/freeplane/freeplane/commit/0dccf298eb8950b64df3231a5bab835a8a0685f7) |
| 2025-09-12 | `feature` | refactor(outline/phase2): centralize key bindings via OutlineActions and OutlineActionTarg | `BreadcrumbPanel.java`, `OutlineActionTarget.java` +3 | [3b3677f5](https://github.com/freeplane/freeplane/commit/3b3677f55f7dc01feec91ed51db589758e2f931d) |
| 2025-09-12 | `feature` | Outline: debounce scroll and streamline breadcrumb updates | `BreadcrumbPath.java`, `NodePositioning.java` +3 | [95324067](https://github.com/freeplane/freeplane/commit/95324067725cec52a341a74a811cc0bdc3c6a1bc) |
| 2025-09-11 | `feature` | UI: add RadioButtonProperty and OptionPanelBuilder support for <radiobuttons> | `preferences.xml`, `OptionPanelBuilder.java` +2 | [4744f1f2](https://github.com/freeplane/freeplane/commit/4744f1f2892173f74ea30453725c2a6d6f38f24c) |
| 2025-09-07 | `fix` | outline: correct breadcrumb membership logic and refine selection scrolling | `BlockPanel.java`, `BreadcrumbPanel.java` +4 | [0899a23e](https://github.com/freeplane/freeplane/commit/0899a23e7129e6c32e950637e5f04cfcf834e3fa) |
| 2025-09-07 | `api_change` | outline: refine scrolling and focus behavior | `BlockPanel.java`, `BreadcrumbPanel.java` +9 | [f56812c9](https://github.com/freeplane/freeplane/commit/f56812c933d46021b66613cf38ee9e01ff57098f) |
| 2025-09-07 | `feature` | outline: extract OutlineBlockLayout and delegate block management | `BreadcrumbState.java`, `ExpansionHandler.java` +3 | [29d59b88](https://github.com/freeplane/freeplane/commit/29d59b88196ff896bc78369b492b942faa6b8e0b) |
| 2025-09-07 | `feature` | outline: adopt 'level' terminology and remove FlatNode | `BlockPanel.java`, `BreadcrumbPanel.java` +15 | [623ecbbf](https://github.com/freeplane/freeplane/commit/623ecbbf755f0e132a10f5c2d819b38093874a47) |
| 2025-09-07 | `fix` | outline: fix incorrect content-level indentation by using computed parent-chain depth | `BlockPanel.java`, `NodePositioning.java` +1 | [c3338a39](https://github.com/freeplane/freeplane/commit/c3338a39ba88f9127febc463ae66923cc506fd96) |
| 2025-09-07 | `feature` | outline: Phase 3 — introduce NodeButton and remove clientProperty usage | `BlockPanel.java`, `BreadcrumbPanel.java` +2 | [dd34a602](https://github.com/freeplane/freeplane/commit/dd34a602a703e5ca9fe9c7b67b23beee64e54f73) |
| 2025-09-06 | `feature` | outline: decouple view state from UI and adopt tell-don't-ask | `BreadcrumbPanel.java`, `BreadcrumbPath.java` +9 | [9850e425](https://github.com/freeplane/freeplane/commit/9850e425a225331f0d2f9542ce044f584885b463) |
| 2025-09-06 | `feature` | Outline: refactor selection bridge, rename selection APIs, improve key bindings, and remov | `BlockPanel.java`, `BreadcrumbPanel.java` +7 | [331aea3a](https://github.com/freeplane/freeplane/commit/331aea3a6d680cf94d6d1ca3aca6efc24e57bc30) |
| 2025-09-05 | `feature` | Outline keyboard navigation: bind keys at focus-owning components\n\n- Move Up/Down/PageUp | `BlockPanel.java`, `BreadcrumbPanel.java` +4 | [029cdc79](https://github.com/freeplane/freeplane/commit/029cdc7989457f809dfc81a0bbd21d75666c4f9d) |
| 2025-09-05 | `feature` | Add FocusOutlineAction and focus handling in outline\n\n- New FocusOutlineAction sets clie | `mindmapmodemenu.xml`, `FocusOutlineAction.java` +4 | [5fe05b15](https://github.com/freeplane/freeplane/commit/5fe05b15afb7900a41a915aa2fe26c649781526d) |
| 2025-09-05 | `feature` | Add outline visibility toggle via split-pane binding and action\n\n- Introduce ToggleOutli | `mindmapmodemenu.xml`, `FrameController.java` +8 | [e26f1c6f](https://github.com/freeplane/freeplane/commit/e26f1c6f7ab0437d3e2aaf137099cd5e443847ea) |
| 2025-09-05 | `fix` | Make zooming smoother (easy fix) | `MapView.java` | [a7c3760e](https://github.com/freeplane/freeplane/commit/a7c3760e7bc9546da9d6b579765c44c34bafe6b3) |
| 2025-08-31 | `feature` | Outline: forward outline selection to Freeplane selection via bridge | `MapAwareOutlinePane.java`, `OutlineSelectionBridge.java` +1 | [fe290858](https://github.com/freeplane/freeplane/commit/fe290858a79720448df4c7520398ee73f434d54c) |
| 2025-08-31 | `feature` | Outline: implement MapAwareOutlinePane.SelectedNodeUpdater.onSelect | `MapAwareOutlinePane.java` | [0137a0e1](https://github.com/freeplane/freeplane/commit/0137a0e117da696377cdcf9a057653386481d579) |
| 2025-08-31 | `fix` | Fix overridden method | `MapAwareOutlinePane.java` | [ab3d9f63](https://github.com/freeplane/freeplane/commit/ab3d9f631e144af1ff7f492a737dd01b1a15ec18) |
| 2025-08-31 | `feature` | outline/bookmarks/window events: centralize per-window MapView selection changes in Dockin | `IMapViewChangeListener.java`, `MapViewDockingWindows.java` +6 | [4cabd635](https://github.com/freeplane/freeplane/commit/4cabd63558982d22dce9dcf0586191ee4435fcfa) |
| 2025-08-31 | `feature` | outline: persist expansion state per MapView and simplify rebuild | `Filter.java`, `MapAwareOutlinePane.java` +6 | [9d571286](https://github.com/freeplane/freeplane/commit/9d571286c41a2344cf81df4e43a8f33b1460c705) |
| 2025-08-30 | `feature` | aux: move only note pane between frames; keep outline per-frame | `AuxiliarySplitPanes.java`, `FrameComponentMover.java` +1 | [0d76cdbd](https://github.com/freeplane/freeplane/commit/0d76cdbd2dac7d541607c4f3d0b13bf592c15f35) |
| 2025-08-30 | `feature` | ui: track per-window last selected MapView and expose getLastSelectedMapViewContainedIn | `IMapViewManager.java`, `FrameComponentMover.java` +4 | [12d27803](https://github.com/freeplane/freeplane/commit/12d27803e75ba4f723b38e6e7b0068cc926e7fb8) |
| 2025-08-29 | `feature` | Outline: incremental updates + safety fixes for node changes | `MapTreeNode.java`, `NodePositioning.java` +3 | [39a8f08a](https://github.com/freeplane/freeplane/commit/39a8f08a010103dee1edbc5487e8a3e03d2a4245) |
| 2025-08-29 | `feature` | Reduce visibility, add and remove listeners when added to / removed from component hierarc | `DemoTreeFactory.java`, `MapAwareOutlinePane.java` +4 | [89028ea2](https://github.com/freeplane/freeplane/commit/89028ea271830dd186ce33c85ea9059038be92f1) |
| 2025-08-24 | `fix` | Fix navigation buttons disappearing after expand/collapse in breadcrumb | `ScrollableTreePanel.java` | [66eb78e9](https://github.com/freeplane/freeplane/commit/66eb78e993b1ddbfb4559a73f720996200c27f2a) |
| 2025-08-24 | `feature` | Fix button overlap issue in outline virtual scrolling | `BlockPanel.java`, `OutlineGeometry.java` +1 | [440fa55e](https://github.com/freeplane/freeplane/commit/440fa55edd6683ffed0390a6ba4767dd526d1dad) |
| 2025-08-24 | `feature` | Implement live updates for outline with real map data | `BlockPanel.java`, `MapTreeNode.java` +4 | [80edda63](https://github.com/freeplane/freeplane/commit/80edda632e665d81813b91b900bc6ca938f69c39) |
| 2025-08-24 | `feature` | Replace demo data with live map integration in OutlinePane | `AuxiliarySplitPanes.java`, `BlockPanel.java` +6 | [811a0b4a](https://github.com/freeplane/freeplane/commit/811a0b4a273df5c603a67f836811fc9bf780568c) |
| 2025-08-23 | `feature` | Add OutlinePane to level 1 pane with demo tree data | `AuxiliarySplitPanes.java`, `BlockVirtualTreeDemo.java` +2 | [cd8be7a7](https://github.com/freeplane/freeplane/commit/cd8be7a70000e974ab056ec07de03ecb84e39e22) |
| 2025-08-23 | `feature` | Implement N-level nested auxiliary split pane system | `ApplicationViewController.java`, `AuxiliarySplitPaneController.java` +3 | [8223c6e8](https://github.com/freeplane/freeplane/commit/8223c6e8e54a2b0b4f2ee8cc0fce5b9817e69621) |
| 2025-08-23 | `feature` | Fix blue dot selection indicator positioning and reliability in outline view | `BlockPanel.java`, `NodePositioning.java` +1 | [97b2243f](https://github.com/freeplane/freeplane/commit/97b2243fff8641442eb231126a665a19d2efbd94) |
| 2025-08-17 | `fix` | fix auxillary split pane initialization | `AuxillaryEditorSplitPane.java` | [c5637e8f](https://github.com/freeplane/freeplane/commit/c5637e8fb7c9f9fc8842c301d1d2f3bc60f71474) |
| 2025-08-17 | `fix` | fix auxillary split pane divider position | `AuxillaryEditorSplitPane.java` | [5871a9bb](https://github.com/freeplane/freeplane/commit/5871a9bb254c0eb39cc3fedd2643189d3be4ef57) |
| 2025-08-17 | `feature` | Add user option "Selected map follows active window" | `history_en.txt`, `preferences.xml` +3 | [b00284bf](https://github.com/freeplane/freeplane/commit/b00284bf19a149a55503565acff739568e33da84) |
| 2025-08-17 | `fix` | Multiple bug fixes for auxillary component and for startup | `AuxillaryEditorSplitPane.java`, `FrameComponentMover.java` +1 | [d18cef3d](https://github.com/freeplane/freeplane/commit/d18cef3d0e5e657c131f2b08cf8a9f5fe77baa3c) |
| 2025-08-16 | `feature` | Add same map option to mouse over selection scope | `preferences.xml`, `NodeSelector.java` +1 | [d9f8bfe5](https://github.com/freeplane/freeplane/commit/d9f8bfe5749b7ba83638ebecdbecaadb4558cfad) |
| 2025-08-16 | `feature` | Add mouse over selection scope configuration | `preferences.xml`, `MouseTimerDelegate.java` +4 | [26d7812a](https://github.com/freeplane/freeplane/commit/26d7812a2eb6526dc5f51c0d1259c79a96eb3fc6) |
| 2025-08-15 | `fix` | fix menubar assignment to frame | `UITools.java` | [04fd659b](https://github.com/freeplane/freeplane/commit/04fd659bfacebb1618e6237b215835ba1028a1da) |
| 2025-08-14 | `feature` | Add option "UI elements follow selected map" true by default | `preferences.xml`, `ApplicationViewController.java` +7 | [aefa5f32](https://github.com/freeplane/freeplane/commit/aefa5f3249e0b95449cbc0350e70b892de3586df) |
| 2025-08-12 | `fix` | Issue #2616 Fix node selection rectangle | `DefaultMapMouseListener.java`, `MMapMouseListener.java` | [8cdef29a](https://github.com/freeplane/freeplane/commit/8cdef29a7788ddc9f0f34f3fb9401bf9d6a1c269) |
| 2025-08-10 | `fix` | fix NPE | `MapScroller.java` | [69320da3](https://github.com/freeplane/freeplane/commit/69320da30070122cc011d1c73f6d0704e135c990) |
| 2025-08-09 | `fix` | fix handling on component removal | `AuxillaryEditorSplitPane.java` | [330a783b](https://github.com/freeplane/freeplane/commit/330a783bc8b0ccd39c065d6bc519834d39ab058e) |
| 2025-08-09 | `fix` | fix note split pane divider location position | `AuxillaryEditorSplitPane.java` | [70825a62](https://github.com/freeplane/freeplane/commit/70825a624470e2acfe8df8a4bd941fd7738f91ff) |
| 2025-08-09 | `fix` | fix split pane divisor position | `ApplicationViewController.java`, `AuxillaryEditorSplitPane.java` | [0c39e034](https://github.com/freeplane/freeplane/commit/0c39e034966ab00f5cd159b85b2d08b7e196313f) |
| 2025-08-09 | `fix` | Fix mav view scrolling after change of the focused frame | `MNoteController.java`, `AuxillaryEditorSplitPane.java` +3 | [50b72a92](https://github.com/freeplane/freeplane/commit/50b72a92243e295460618130a01a6cfcfee13127) |
| 2025-08-09 | `fix` | Fix divider location positioning | `AuxillaryEditorSplitPane.java` | [da4e12e5](https://github.com/freeplane/freeplane/commit/da4e12e50ac874ea4cb464c25bd972d1f3fd8bf9) |
| 2025-08-03 | `feature` | Improve FrameComponentMover initialization and getCurrentRootComponent logic | `ApplicationViewController.java`, `AuxillaryEditorSplitPane.java` +1 | [07371e95](https://github.com/freeplane/freeplane/commit/07371e95e0dcda9b208d67376e39ddf43069d238) |
| 2025-08-03 | `feature` | Refactor auxiliary component management for dynamic split pane handling | `MNoteController.java`, `FrameController.java` +7 | [a0ae2b91](https://github.com/freeplane/freeplane/commit/a0ae2b91a12ca0c7027fee44200ea0b265cf9440) |
| 2025-08-03 | `feature` | Improve floating window handling and tab area management | `ApplicationViewController.java`, `MapViewDockingWindows.java` | [29541671](https://github.com/freeplane/freeplane/commit/2954167121c24ac442e312ff32c8c629a6b89d10) |
| 2025-08-03 | `feature` | Refactor setFullScreen methods for better frame-specific handling | `FrameController.java`, `ApplicationViewController.java` | [10b03bcb](https://github.com/freeplane/freeplane/commit/10b03bcb3263353f6275906b8e906050200c7c11) |
| 2025-08-03 | `feature` | Fix macOS full screen detection for multi-monitor setups | `Compat.java`, `FrameController.java` +4 | [6c347bbd](https://github.com/freeplane/freeplane/commit/6c347bbd3a9c3486e72fb734ee91a932a31db1ea) |
| 2025-08-03 | `feature` | Fix UI component references for UI-follows-focus architecture | `GrabKeyDialog.java`, `ShowPreferencesAction.java` +45 | [44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf) |
| 2025-08-03 | `feature` | Implement single note panel that moves between frames | `MNoteController.java`, `ApplicationViewController.java` +2 | [35ee57d0](https://github.com/freeplane/freeplane/commit/35ee57d0fb72eda827157d251fc49c96d82c2369) |
| 2025-08-03 | `feature` | Experimental: Implement UI follows focus with FrameComponentMover | `ApplicationViewController.java`, `FrameComponentMover.java` +1 | [2ea52fb1](https://github.com/freeplane/freeplane/commit/2ea52fb1cf6fb7da5f90a8353310c94493cd8a3b) |
| 2025-08-03 | `feature` | Fix InfoNode floating window sizing by capturing CENTER component size | `MapViewDockingWindows.java` | [2b53ab84](https://github.com/freeplane/freeplane/commit/2b53ab84e9ecee0d6db076b3853ce952e2558905) |
| 2025-08-02 | `feature` | Improve split pane position management with proportional values | `ApplicationViewController.java`, `AuxillaryEditorSplitPane.java` +1 | [6b94e1b8](https://github.com/freeplane/freeplane/commit/6b94e1b88977b25bec52c76980a6415a6e18753f) |
| 2025-08-02 | `feature` | Store component factory in ApplicationViewController for automatic floating window compone | `ApplicationViewController.java`, `MapViewDockingWindows.java` | [cb4c82c5](https://github.com/freeplane/freeplane/commit/cb4c82c5571748c509207808bc79a583eb226a42) |
| 2025-08-02 | `feature` | Implement factory pattern for note panels across all windows | `MNoteController.java`, `ViewController.java` +5 | [39a2b362](https://github.com/freeplane/freeplane/commit/39a2b36222f6b6b60a08b0f054bbedb560071b5f) |
| 2025-07-29 | `feature` | Remove accidentally committed backup files and ignore them | `.gitignore`, `.!52030!Resources_cs.properties` +12 | [8019e6dc](https://github.com/freeplane/freeplane/commit/8019e6dcd9015f41b0262a5b95aadcbaf5900901) |
| 2025-07-29 | `fix` | Fix Unicode corruption in all translation files | `.!52030!Resources_cs.properties`, `Resources_af.properties.backup` +12 | [d50a48ca](https://github.com/freeplane/freeplane/commit/d50a48ca010a2d4711d6dc7a6295aae81fadc5da) |
| 2025-07-28 | `feature` | Add mouse-over preferences translations for all supported languages | `Resources_af.properties`, `Resources_ar.properties` +16 | [28da344b](https://github.com/freeplane/freeplane/commit/28da344b747b3fa75405d61d2da7948caf1723a2) |
| 2025-07-28 | `feature` | Restructure mouse-over preferences and improve code quality | `CLAUDE.md`, `Resources_af.properties` +13 | [6dd1a024](https://github.com/freeplane/freeplane/commit/6dd1a0247e895633c388ff5f8ecea6173b9fccb9) |
| 2025-07-28 | `feature` | Change selection mouse over terminology from "enabled" to "immediate" | `Resources_cs.properties`, `Resources_eu.properties` +5 | [809a2b6d](https://github.com/freeplane/freeplane/commit/809a2b6d1bf4ef79b101b9c09f1f9b081b281b51) |
| 2025-07-28 | `feature` | Remove deprecated selection_method configuration system | `Resources_af.properties`, `Resources_ar.properties` +40 | [298663f1](https://github.com/freeplane/freeplane/commit/298663f1701e8c794f09edcc58e76d1f1762008a) |
| 2025-07-28 | `fix` | Fix mouse over selection timing bug | `NodeSelector.java` | [60ef0b8d](https://github.com/freeplane/freeplane/commit/60ef0b8df9e232eb4c2337b3bd21fabbe2b3dd49) |
| 2025-07-28 | `fix` | Fix additional encoding issue in Croatian translation | `Resources_hr.properties` | [eaa2fc0b](https://github.com/freeplane/freeplane/commit/eaa2fc0bf8343789c58d0040a467726daa9859d4) |
| 2025-07-28 | `fix` | Fix encoding issue in Croatian translation | `Resources_hr.properties` | [3e139827](https://github.com/freeplane/freeplane/commit/3e1398271b2e31c65458d1d4e666147fcb6f2de4) |
| 2025-07-28 | `feature` | Add 71 missing translations to French (Resources_fr.properties) | `Resources_fr.properties` | [fe679c9c](https://github.com/freeplane/freeplane/commit/fe679c9c1613867a09765554079c724441257b88) |
| 2025-07-28 | `feature` | Add 22 missing translations to Croatian (Resources_hr.properties) | `Resources_hr.properties` | [bc623588](https://github.com/freeplane/freeplane/commit/bc6235883a87090e8d2760ae620f72982a3c8f11) |
| 2025-07-28 | `feature` | Add 20 missing translations to Spanish (Resources_es.properties) | `Resources_es.properties` | [3a18523b](https://github.com/freeplane/freeplane/commit/3a18523b96ff574e187e11503814d1af48a6208c) |
| 2025-07-28 | `feature` | Add 50 missing translations to Portuguese Brazilian (Resources_pt_BR.properties) | `Resources_pt_BR.properties` | [dfc15921](https://github.com/freeplane/freeplane/commit/dfc159213663f66b4faa2d69716aefce38488711) |
| 2025-07-28 | `feature` | Add 47 missing translations to Chinese Simplified (Resources_zh_CN.properties) | `Resources_zh_CN.properties` | [85aebcf7](https://github.com/freeplane/freeplane/commit/85aebcf725f840115af4bebff538003a93cdbedd) |
| 2025-07-28 | `feature` | Add all 41 missing Japanese translations | `Resources_ja.properties` | [1776e6df](https://github.com/freeplane/freeplane/commit/1776e6dff80b5268df7c2e8a95750c66fa9bf1f9) |
| 2025-07-28 | `feature` | Add all 40 missing Russian translations | `Resources_ru.properties` | [76f4c66d](https://github.com/freeplane/freeplane/commit/76f4c66d241a5fdf67f7fbe8c4dc011156616f81) |
| 2025-07-28 | `feature` | Add missing German translations for mouse-over behavior settings | `Resources_de.properties` | [1646ca51](https://github.com/freeplane/freeplane/commit/1646ca512bd95f56dd3fa4d89673dd30d13da189) |
| 2025-07-28 | `feature` | Add missing Ukrainian translations for mouse-over behavior settings | `Resources_uk_UA.properties` | [60c0eed5](https://github.com/freeplane/freeplane/commit/60c0eed5cd71667e855af121e2e65cf90700b2fe) |
| 2025-07-28 | `feature` | Add missing Dutch translations for mouse-over behavior settings | `Resources_nl.properties` | [1cee4e9a](https://github.com/freeplane/freeplane/commit/1cee4e9a62d0ef07ac7ac4ba15dad8f202189d98) |
| 2025-07-28 | `feature` | Add missing Portuguese (PT) translations for mouse-over behavior settings | `Resources_pt_PT.properties` | [554d9c05](https://github.com/freeplane/freeplane/commit/554d9c05c731b2843fe53f26db1136b408247c6e) |
| 2025-07-27 | `feature` | Issue 2603: Restore wasFired protection for rapid folding prevention | `NodeFolder.java`, `NodeSelector.java` | [6f11a181](https://github.com/freeplane/freeplane/commit/6f11a181ef50fef9fa382964f190bff02a9a6b81) |
| 2025-07-27 | `feature` | Issue 2603: Refactor timing logic using composition over inheritance | `CLAUDE.md`, `MouseTimerDelegate.java` +2 | [cb8e2f77](https://github.com/freeplane/freeplane/commit/cb8e2f77bb7bd17c4e0e582d381bfbbb79dc3b21) |
| 2025-07-27 | `fix` | Issue #2603: Complete preview mode fix and improve architecture | `preferences.xml`, `DefaultNodeMouseMotionListener.java` +1 | [3ae994fd](https://github.com/freeplane/freeplane/commit/3ae994fd4007b05921a9e587f06dbd7257900089) |
| 2025-07-27 | `feature` | Issue #2603: Fix preview mode to persist unfolding after user clicks | `DefaultNodeMouseMotionListener.java`, `NodeFolder.java` | [9f829fe5](https://github.com/freeplane/freeplane/commit/9f829fe5a8c1505a222acb3a3a1498f2c9d67af2) |
| 2025-07-27 | `feature` | Issue #2603: Fix translation keys for mouse over behavior preferences | `CLAUDE.md`, `Resources_en.properties` | [4e8be515](https://github.com/freeplane/freeplane/commit/4e8be515138787d2556657720e042baff6114f0d) |
| 2025-07-27 | `feature` | Issue #2603: Add independent folding behavior configuration | `preferences.xml`, `ResourceController.java` +7 | [663e1aff](https://github.com/freeplane/freeplane/commit/663e1affd8f7b21ee07e2930082f07804256bfc6) |
| 2025-07-23 | `feature` | Issue #2594 Include node ID in backlink when moving a branch into a new map | `ExportBranchAction.java` | [095dd404](https://github.com/freeplane/freeplane/commit/095dd404779101b2064a2480956dfa5cbf8bbc30) |
| 2025-07-23 | `fix` | fix NPE | `NoteManager.java` | [04827133](https://github.com/freeplane/freeplane/commit/0482713355ce23aa2b4166f1901ac38ed582b1b9) |
| 2025-07-23 | `fix` | Fix latex rendered width, font and colors | `NoteStyleAccessor.java`, `NoteManager.java` +4 | [c9e842a5](https://github.com/freeplane/freeplane/commit/c9e842a5781f3b9389fb68f48f3a4ca157848b46) |
| 2025-07-19 | `fix` | Fix note pane | `ApplicationViewController.java`, `MapViewDockingWindows.java` | [0a8f7842](https://github.com/freeplane/freeplane/commit/0a8f784212bef22a68d7ad86bd728b2bd515f82c) |
| 2025-07-18 | `fix` | fix NPE | `BookmarkToolbarPane.java` | [784c08a4](https://github.com/freeplane/freeplane/commit/784c08a42a7ab3910a9f726da34afc7c3ef04a71) |
| 2025-07-18 | `feature` | Issue #2589 Fix URI space encoding issue throughout Freeplane | `FileOpener.java`, `URIUtils.java` +10 | [5d2843db](https://github.com/freeplane/freeplane/commit/5d2843db659f316c657eaea3527063701adeb2f3) |
| 2025-07-18 | `fix` | Revert "Fix resolving URIs containing # character" | `UrlManager.java` | [142ae601](https://github.com/freeplane/freeplane/commit/142ae601ab4ac13ee6bb8dc1f269192840a25f13) |
| 2025-07-15 | `feature` | Update Resources_en.properties | `Resources_en.properties` | [f6ade734](https://github.com/freeplane/freeplane/commit/f6ade7341671c1de72b5e25f3df836357028a140) |
| 2025-07-13 | `fix` | fix: disabling save_last_position_in_map has no effect | `Resources_af.properties`, `Resources_cs.properties` +29 | [6ade10e8](https://github.com/freeplane/freeplane/commit/6ade10e81a3900ecb3de7bac10652e88c8f12152) |
| 2025-07-12 | `feature` | Issue #2578 Fix jump out from node not present with the new root | `MapView.java` | [7254b65c](https://github.com/freeplane/freeplane/commit/7254b65cf2751b6aa893bff8b7f425a393f76427) |
| 2025-07-12 | `fix` | fix edit start position after editing by mouse click | `EditNodeTextField.java` | [3600a959](https://github.com/freeplane/freeplane/commit/3600a95920acb4d7300f37001b344ebf5e19f1ad) |
| 2025-07-12 | `feature` | enable underline checkbox for styles: Details, Note, Attributes, Tags | `StylePropertyAdjuster.java` | [cf66cebc](https://github.com/freeplane/freeplane/commit/cf66cebc2f482c1164c0890ca6bbf7e71663cfa1) |
| 2025-07-12 | `fix` | fix Tool-panel-underline-checkbox activation and label; fix typos | `FontUnderlineControlGroup.java`, `Resources_en.properties` | [0db9d807](https://github.com/freeplane/freeplane/commit/0db9d80783ea3861be76933cebb61b745656ac9c) |
| 2025-07-11 | `feature` | Step 3: Extract VisibleOutlineState class | `BlockPanel.java`, `BreadcrumbPanel.java` +3 | [76beccac](https://github.com/freeplane/freeplane/commit/76beccacbaadd1be846c960ff388008462e22151) |
| 2025-07-11 | `feature` | Step 2: Extract OutlineSelection class | `BlockPanel.java`, `BreadcrumbPanel.java` +2 | [08d4b701](https://github.com/freeplane/freeplane/commit/08d4b7010143b45b049aa56b6a73736c3f8aeec8) |
| 2025-07-11 | `feature` | Step 1: Extract OutlineGeometry class | `BlockPanel.java`, `BreadcrumbPanel.java` +3 | [97b1ba55](https://github.com/freeplane/freeplane/commit/97b1ba55d16abcf188af92f4588caece502db6fa) |
| 2025-07-11 | `feature` | Fix map positioning for new maps on start | `MapScroller.java`, `MapView.java` | [24620caa](https://github.com/freeplane/freeplane/commit/24620caa159acfc0a77152a2eb99c90b0f0cae8f) |
| 2025-07-10 | `fix` | fix layout for filtered map views | `VerticalNodeViewLayoutStrategy.java` | [76b0767b](https://github.com/freeplane/freeplane/commit/76b0767bedcfc4c727d898f87cca2c879e78233a) |
| 2025-07-06 | `feature` | add tooltip for display_inline_editor_for_all_new_nodes | `Resources_en.properties` | [3e22cfee](https://github.com/freeplane/freeplane/commit/3e22cfeed5ec194e876f1c0cc6cf825c03fe80a8) |
| 2025-07-05 | `fix` | Fix resolving URIs containing # character | `UrlManager.java` | [fc70fb9d](https://github.com/freeplane/freeplane/commit/fc70fb9d0e31cdae964c48f05c25a201dad49d07) |
| 2025-07-05 | `feature` | Support different content types for drag and drop to bookmarks | `BookmarkDropTargetListener.java`, `NodeDropUtils.java` | [275dea2b](https://github.com/freeplane/freeplane/commit/275dea2bcd139f3243331e3fe67b833195d4e65d) |
| 2025-07-05 | `feature` | Issue #2560 add underline | `Resources_ar.properties`, `Resources_ca.properties` +28 | [b48e383d](https://github.com/freeplane/freeplane/commit/b48e383db28b2952d37152d5e667c4c2c53d996b) |
| 2025-07-03 | `feature` | Make Add Root Branch button focusable and activate it on enter | `BookmarkButtonConfigurator.java`, `BookmarkClipboardHandler.java` +1 | [6728c3c4](https://github.com/freeplane/freeplane/commit/6728c3c4cc9a7720e675c511262f263eac3d6bf9) |
| 2025-07-02 | `feature` | Allow to create root branches and delete nodes directly from the toolbar | `FreeplaneToolBar.java`, `ToolbarLayout.java` +10 | [14efdedd](https://github.com/freeplane/freeplane/commit/14efdedd4b9b95850a7a995fe5d52cf32a75e3c5) |
| 2025-07-02 | `feature` | Implement hybrid bookmark drop: edges create bookmarks, center adds children | `BookmarkDropTargetListener.java` | [bf6b08c3](https://github.com/freeplane/freeplane/commit/bf6b08c3bb8ec3d25eacad7dbaaeddada29da32b) |
| 2025-07-01 | `feature` | Fix bookmark drops to add nodes as children to the map, not creating new bookmarks | `BookmarkClipboardHandler.java`, `BookmarkDropTargetListener.java` +2 | [c1f7b3fe](https://github.com/freeplane/freeplane/commit/c1f7b3fecef175a8752971d4a22e1c46ebb42aa2) |
| 2025-07-01 | `fix` | refactor and fix jump into invisible root | `MapView.java` | [4fa89822](https://github.com/freeplane/freeplane/commit/4fa89822178e71ffce0324ff18ca68f2fc506073) |
| 2025-06-30 | `fix` | Fix initial enabled state for map view navigation actions | `NavigationMapNextViewAction.java`, `NavigationMapPreviousViewAction.java` +2 | [36a9d219](https://github.com/freeplane/freeplane/commit/36a9d2190d13ef9f1df3b6855bce292a77f76ed7) |
| 2025-06-30 | `feature` | Add next/previous view navigation for same map with Ctrl+Shift+N shortcut | `mindmapmodemenu.xml`, `ViewController.java` +8 | [efa70b6a](https://github.com/freeplane/freeplane/commit/efa70b6ac31d94f2fa7d55b94a317f038a922ebe) |
| 2025-06-30 | `feature` | Issue #2526 add synchronizeSelectionOnlyOnBranchChange option | `history_en.txt`, `preferences.xml` +3 | [1dbcfd06](https://github.com/freeplane/freeplane/commit/1dbcfd0650742e17c828bf0c6d590334f57c7496) |
| 2025-06-29 | `fix` | fix NPE on open asRoot when lastSelectedNode is newly created | `MapBookmarks.java` | [e38ad4d7](https://github.com/freeplane/freeplane/commit/e38ad4d7e62d6767fc329b00df4b33548ee226d5) |
| 2025-06-29 | `fix` | fix NPE | `BookmarksController.java` | [f7dd9459](https://github.com/freeplane/freeplane/commit/f7dd945914a5b6acee5532c7e4c56fa2632f5215) |
| 2025-06-29 | `feature` | Improve scrolling for new maps | `MapScroller.java` | [795b2589](https://github.com/freeplane/freeplane/commit/795b2589c3f2c5d087be83b5c8a4e86e3f8fd814) |
| 2025-06-29 | `feature` | bookmark action: Open as root in new &view | `NodeBookmark.java`, `BookmarkPopupMenu.java` +1 | [ce0dd45d](https://github.com/freeplane/freeplane/commit/ce0dd45d5db87d4f3a4c7b7bf2cfa9756fdafea5) |
| 2025-06-28 | `feature` | Add action to switch to and from bookmarks tool bar | `mindmapmodemenu.xml`, `BookmarksController.java` +4 | [77fcce98](https://github.com/freeplane/freeplane/commit/77fcce98993f10bd78a95d57135664e903f2421c) |
| 2025-06-28 | `feature` | Support operations by keyboard | `BookmarkButton.java`, `BookmarkButtonConfigurator.java` +2 | [42c7a4b8](https://github.com/freeplane/freeplane/commit/42c7a4b86e32118d1da2203c56122d463a25621e) |
| 2025-06-28 | `fix` | fix repaint after select | `MapViewPane.java` | [4da1a5db](https://github.com/freeplane/freeplane/commit/4da1a5db8bb3114a0cb4900322880ce4fc491390) |
| 2025-06-28 | `feature` | Support drag and drop on the toolbar | `BookmarkButton.java`, `BookmarkDropTargetListener.java` +6 | [0ea8c13f](https://github.com/freeplane/freeplane/commit/0ea8c13fb8b87cf3de3a6d8572ff7b3d3c70b0bb) |
| 2025-06-28 | `feature` | Support gaps between components in ToolbarLayout | `ToolbarLayout.java` | [afbb646b](https://github.com/freeplane/freeplane/commit/afbb646b6fd48684f7832add194b947e8dd87e4b) |
| 2025-06-27 | `fix` | fix NPE | `BookmarkButton.java` | [56f6b9e1](https://github.com/freeplane/freeplane/commit/56f6b9e1b5810db95d6cff3be68c89f4dea000f4) |
| 2025-06-25 | `fix` | fix for scripting: setBookmark fails silently on newly created nodes | `BookmarksController.java` | [d87b619f](https://github.com/freeplane/freeplane/commit/d87b619fc549d52f64d89ba2b1a38a0282d18b2d) |
| 2025-06-23 | `fix` | fix translation | `Resources_de.properties` | [513e5b2c](https://github.com/freeplane/freeplane/commit/513e5b2c52cd04ced0fe5ce5130f01611464456f) |
| 2025-06-23 | `feature` | Add missing German translations | `Resources_de.properties` | [54ea1068](https://github.com/freeplane/freeplane/commit/54ea10687e9f371d32742c82b0675ab33bc5caec) |
| 2025-06-23 | `fix` | Fix note tooltips and refactor | `NoteController.java`, `TextController.java` | [01a6701f](https://github.com/freeplane/freeplane/commit/01a6701fa0f80820cb175246ef58a5921f11cbdb) |
| 2025-06-22 | `fix` | fix licenses info | `licenses.txt` | [2be75107](https://github.com/freeplane/freeplane/commit/2be75107b9a0f4c66ea176b0c3719062fae77628) |
| 2025-06-22 | `fix` | Issue #2423 Fix paths containing RTL letters in folder and file names. | `LastOpenedList.java`, `MapViewDockingWindows.java` +2 | [708df2e1](https://github.com/freeplane/freeplane/commit/708df2e12c3e7971ffa9e9d1128edb78e8b85be7) |
| 2025-06-22 | `feature` | Issue #2491 Fix autoscroll after new nodes were added | `MapScroller.java` | [31b20a20](https://github.com/freeplane/freeplane/commit/31b20a204a2c817625d8283aae1f47a878a19c6d) |
| 2025-06-22 | `fix` | Issue #2528 fix NPE | `BookmarkNodeAction.java` | [6aa4aa7d](https://github.com/freeplane/freeplane/commit/6aa4aa7d4c0d895352bccb3a895e6da91600583f) |
| 2025-06-21 | `fix` | Fix bookmarks persistence implementation | `BookmarksBuilder.java`, `BookmarksBuilderTest.java` | [6793c9f4](https://github.com/freeplane/freeplane/commit/6793c9f43ca61d2d025776ceb46e255693b79dfe) |
| 2025-06-21 | `fix` | Fix autoscroll and smooth autoscroll | `MapController.java`, `MapScroller.java` +2 | [f83a2c1d](https://github.com/freeplane/freeplane/commit/f83a2c1d545b1d6bc6571050a20f64a0fee1d34e) |
| 2025-06-20 | `feature` | Add user option for general display scaling | `preferences.xml`, `UITools.java` +2 | [d3527446](https://github.com/freeplane/freeplane/commit/d35274466ade16d6e34a075c3f5fd5597fc8aeb3) |
| 2025-06-17 | `fix` | fix opening nodes hidden by filter | `BookmarksToolbarBuilder.java`, `NodeBookmark.java` +1 | [ae0f397b](https://github.com/freeplane/freeplane/commit/ae0f397b6da3818bf6e1d313256ceb9a6289ac46) |
| 2025-06-17 | `feature` | Add actions to select the bookmarked node or open it as root | `TranslatedElementFactory.java`, `BookmarksToolbarBuilder.java` +2 | [804ecd28](https://github.com/freeplane/freeplane/commit/804ecd28b68f844711c90cfa1768763dbdf72825) |
| 2025-06-16 | `fix` | fix file creation from URI | `Browser.java` | [d02c21e0](https://github.com/freeplane/freeplane/commit/d02c21e0bc97b6dd54f70e003db2d77361892fb5) |
| 2025-06-16 | `fix` | Issue #2408 Fix link opening | `preferences.xml`, `FileUtils.java` +5 | [1df1536f](https://github.com/freeplane/freeplane/commit/1df1536fbbf27c961781d62b8e0c403eb1d305bd) |
| 2025-06-15 | `feature` | Implement bookmark functionality in Freeplane node api | `BookmarkNodeAction.java`, `BookmarksController.java` +13 | [0b3743d5](https://github.com/freeplane/freeplane/commit/0b3743d5fd6f27f70eb7c8fd20ba67879b89bfa9) |
| 2025-06-15 | `feature` | Enhance BookmarkNodeAction to support bookmark deletion | `BookmarkNodeAction.java` | [9f339659](https://github.com/freeplane/freeplane/commit/9f33965975b4fb39145cb26e2ecb965eadbbe3e2) |
| 2025-06-15 | `feature` | Enhance bookmarks functionality with drag-and-drop support in toolbar | `BookmarksBuilder.java`, `BookmarksToolbarBuilder.java` | [48b25b46](https://github.com/freeplane/freeplane/commit/48b25b46680a84d250d06b4c0a4995fac01d6e11) |
| 2025-06-15 | `feature` | Add popup menu to bookmark toolbar buttons | `BookmarksController.java`, `BookmarksToolbarBuilder.java` +2 | [f9b8b8eb](https://github.com/freeplane/freeplane/commit/f9b8b8eb26a31b5c8e29c213201a8f1ea205af30) |
| 2025-06-15 | `api_change` | Improve internal scrolling API | `NodeBookmark.java`, `IMapSelection.java` +4 | [4dfbb7be](https://github.com/freeplane/freeplane/commit/4dfbb7be38f7adf3b6ee1110aed8a3384ac5873e) |
| 2025-06-15 | `feature` | Add BookmarkNodeAction and integrate into bookmarks functionality | `mindmapmodemenu.xml`, `BookmarkNodeAction.java` +4 | [de8f8af7](https://github.com/freeplane/freeplane/commit/de8f8af7ac1c265605439790a5fecd6877f52726) |
| 2025-06-15 | `feature` | Add bookmarks feature with toolbar integration | `mindmapmodemenu.xml`, `FreeplaneToolBar.java` +15 | [a8c33b98](https://github.com/freeplane/freeplane/commit/a8c33b989165cb0d05510fb2c703b89f24115b1b) |
| 2025-06-14 | `feature` | Issues #2508 icons not visible in new nodes when preserve format with icons is enabled | `MMapController.java` | [21da8637](https://github.com/freeplane/freeplane/commit/21da863702a4b8468e586d0bc04ed543d6fa199e) |
| 2025-06-14 | `feature` | MapViewPane should not implement ViewportReservedAreaSupplier for flexibility | `MapViewSerializer.java`, `MapViewScrollPane.java` +1 | [1d4a896a](https://github.com/freeplane/freeplane/commit/1d4a896a3c1273b4e8897ff354f6eae583f30dea) |
| 2025-06-13 | `fix` | Fix autoscroll | `MapController.java` | [2dea8afa](https://github.com/freeplane/freeplane/commit/2dea8afa458f3a702e058dab7075caa192a72c23) |
| 2025-06-13 | `fix` | Fix rounding error in zoomed html nodes | `ZoomableLabelUI.java` | [911522e4](https://github.com/freeplane/freeplane/commit/911522e4c1096941898ea1b28f3c74f58db94a5d) |
| 2025-06-13 | `feature` | Issue #2505 New Nodes Sometimes Don't Accept The First Character Typed | `EventBuffer.java` | [7db4dbe3](https://github.com/freeplane/freeplane/commit/7db4dbe30466a112118a3676337406b0f72a614c) |
| 2025-06-08 | `feature` | Issue #2498 Enable smooth scrolling for auto-scroll | `ViewController.java`, `MapScroller.java` +1 | [269561d6](https://github.com/freeplane/freeplane/commit/269561d63c19483452e2c53e242b6c5d47a40156) |
| 2025-06-08 | `fix` | Fix node tool tip removal | `MainView.java`, `NodeTooltipManager.java` | [7cffe5f7](https://github.com/freeplane/freeplane/commit/7cffe5f720433767bc85375c57466d1c340c0e02) |
| 2025-06-07 | `feature` | Issue #2496 add extra gap between subtrees | `VerticalNodeViewLayoutStrategy.java` | [c449307a](https://github.com/freeplane/freeplane/commit/c449307a50a9dc71f0269a853a0f979256a8192a) |
| 2025-06-01 | `fix` | fix NPE | `EditNodeTextField.java` | [9b23666a](https://github.com/freeplane/freeplane/commit/9b23666a4b9a89b207e3880db74ee80161d23954) |
| 2025-05-29 | `fix` | fix and log NPE for backup files | `MFileManager.java` | [c7d77d55](https://github.com/freeplane/freeplane/commit/c7d77d5572f8152943617076ad1698703c8ba36b) |
| 2025-05-29 | `fix` | fix node tooltip priorities | `MainView.java` | [d613c642](https://github.com/freeplane/freeplane/commit/d613c64240bf07303172f15cd1bf30d21f64fc46) |
| 2025-05-25 | `fix` | Fix default show/hide note accelerator for mac | `default_accelerators_mac.properties` | [7adb9285](https://github.com/freeplane/freeplane/commit/7adb928598ee0d1298518d6ae13fa8a1ce3b0b68) |
| 2025-05-25 | `fix` | fix null check | `DefaultMouseWheelListener.java` | [1206f9eb](https://github.com/freeplane/freeplane/commit/1206f9eb00d6095b677d32d8147a4743ed0dc782) |
| 2025-05-25 | `feature` | Issue #2474 Add "shift [arrow-key]" action to the menu | `mindmapmodemenu.xml`, `FreeSelectNodeAction.java` +1 | [7d4f3be6](https://github.com/freeplane/freeplane/commit/7d4f3be61012114c621a50b1c2f3637484ca479b) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts | `OptionPanel.java`, `PathProperty.java` +29 | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-05-22 | `fix` | fix NPE | `MapView.java` | [737f08a8](https://github.com/freeplane/freeplane/commit/737f08a8f09d0d8c4b92514ea8a4446915946924) |
| 2025-05-22 | `fix` | fix exceptions for non local transfers: | `TagSelection.java`, `MindMapNodesSelection.java` +1 | [df8f8315](https://github.com/freeplane/freeplane/commit/df8f83158802aa80ff10f529c2c6bba8cd17f634) |
| 2025-05-22 | `fix` | fix NPE | `EditNodeTextField.java` | [cb60c69e](https://github.com/freeplane/freeplane/commit/cb60c69e79f7fac44ea59ac8f819989f82503a72) |
| 2025-05-22 | `fix` | fix NPE | `TextualTooltipRendererFactory.java` | [512534be](https://github.com/freeplane/freeplane/commit/512534beb19e9be3a5b41df17a46f164256de954) |
| 2025-05-22 | `fix` | fix NPE | `TextualTooltipRendererFactory.java` | [8a0e9c12](https://github.com/freeplane/freeplane/commit/8a0e9c1226ecade28c13d32bbc392752f6494753) |
| 2025-05-18 | `feature` | Better support input method events | `IEditHandler.java`, `IUserInputListenerFactory.java` +18 | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2025-05-16 | `feature` | Issue #2462 Support hyperlinks in markdown notes | `NotePanel.java`, `FreeplaneTooltip.java` +2 | [b87876eb](https://github.com/freeplane/freeplane/commit/b87876eb72688214d61a998332fb1c37c772c3c8) |
| 2025-05-16 | `fix` | Issue #2460 Fix edge start points for horizontal layouts | `EdgeView.java` | [4e70d2b0](https://github.com/freeplane/freeplane/commit/4e70d2b0778223739e3796762a6b1f601e098a18) |
| 2025-05-14 | `fix` | fix formatting | `NodeViewLayoutHelper.java` | [62dee64c](https://github.com/freeplane/freeplane/commit/62dee64c35123c87aa307cb36ff57153962434f4) |
| 2025-05-13 | `fix` | Issue #2447 fix for empty attribute values | `MAttributeController.java` | [e1f07a54](https://github.com/freeplane/freeplane/commit/e1f07a548488633a90cc571d1e3a7153e978beb0) |
| 2025-05-11 | `fix` | Issue #2449 fix compact layout for stacked nodes | `NodeViewLayout.java`, `NodeViewLayoutHelper.java` +1 | [f324fb79](https://github.com/freeplane/freeplane/commit/f324fb793dacfefc1ff22c800482dd3f310a5846) |
| 2025-05-11 | `fix` | fix layout | `VerticalNodeViewLayoutStrategy.java` | [d937cf23](https://github.com/freeplane/freeplane/commit/d937cf2317720b2aa5caf1eafac2b8c38c30c444) |
| 2025-05-10 | `feature` | Use auto compact layout as the new default in all Freeplane templates | `BigMap.mm`, `BuzanMap.mm` +18 | [f57ed6a1](https://github.com/freeplane/freeplane/commit/f57ed6a1317d9f7c9cb1b4062b3a4bc20669ec03) |
| 2025-05-09 | `fix` | Issue #2439 Fix printing in landscape mode | `ContentPane.java`, `MainView.java` | [50af5baa](https://github.com/freeplane/freeplane/commit/50af5baaec8bc79c2e6f8210ee6387ae068d9304) |
| 2025-05-09 | `fix` | fix layout | `VerticalNodeViewLayoutStrategy.java`, `ChildNodesAlignment.java` | [36a31464](https://github.com/freeplane/freeplane/commit/36a31464e13ec59d108452aeec3e45e1aae8c714) |
| 2025-05-05 | `fix` | Issue #2435 Filter related compact layout bug | `VerticalNodeViewLayoutStrategy.java` | [c68b2908](https://github.com/freeplane/freeplane/commit/c68b29084c87bab9056fbc9d66bf8d26763a8832) |
| 2025-05-04 | `feature` | Add distance to children to child content boundary size so that edges and folding marks do | `NodeView.java`, `NodeViewLayoutHelper.java` +1 | [dbcb4bc3](https://github.com/freeplane/freeplane/commit/dbcb4bc3ff7e5bd0429560b48de9e2751478b9e4) |
| 2025-05-04 | `fix` | fix compact layout for zoomed map | `NodeView.java` | [31778edd](https://github.com/freeplane/freeplane/commit/31778edd45b85fc227fde0cddbc9fbb3135d5350) |
| 2025-05-03 | `feature` | Use new folding mark width for non compacted maps too | `FoldingMark.java`, `MainViewPainter.java` +1 | [6244cd83](https://github.com/freeplane/freeplane/commit/6244cd83c6876314d1bd35ad1a7e48337133ef91) |
| 2025-05-03 | `feature` | Issue #2430 New bug related to the summary node | `VerticalNodeViewLayoutStrategy.java` | [45e801d6](https://github.com/freeplane/freeplane/commit/45e801d6f95a3f8841e3f7dbd956319626bb45e6) |
| 2025-05-01 | `fix` | fix cloud handling in compact lsyouts | `VerticalNodeViewLayoutStrategy.java` | [1f26cce5](https://github.com/freeplane/freeplane/commit/1f26cce57240d480cbe91b3d2102a2af039e1203) |
| 2025-04-29 | `fix` | refactor and fix | `VerticalNodeViewLayoutStrategy.java` | [3bae638e](https://github.com/freeplane/freeplane/commit/3bae638ef7c63537815b5637131d3cc7344c5759) |
| 2025-04-28 | `feature` | Refactor VerticalNodeViewLayoutStrategy | `VerticalNodeViewLayoutStrategy.java` | [a1001046](https://github.com/freeplane/freeplane/commit/a1001046c0d17a83511c3cfdf6e6e80bdc288b4e) |
| 2025-04-28 | `fix` | fix typo | `ResourceController.java`, `IconSelectionPopupDialog.java` +17 | [a9451631](https://github.com/freeplane/freeplane/commit/a945163128013a1f7889b007ed17b7da8f1fcecd) |
| 2025-04-27 | `feature` | Add compact layout switch to the toolbar | `mindmapmodemenu.xml`, `SetBooleanMapPropertyAction.java` +2 | [5e52d053](https://github.com/freeplane/freeplane/commit/5e52d053e6e641a1bd540bc60a48033dffff069a) |
| 2025-04-25 | `fix` | fix layout | `VerticalNodeViewLayoutStrategy.java` | [0e1a5854](https://github.com/freeplane/freeplane/commit/0e1a58549a760af3b82e5265e35af53928a6bffe) |
| 2025-04-22 | `feature` | Enhance CombinedFunction to support FALLBACK operation and improve evaluation logic | `StepFunction.java`, `StepFunctionTest.java` | [7e9d7ccf](https://github.com/freeplane/freeplane/commit/7e9d7ccf5ab1b6ab1e7d930a78d3ad4714b0378a) |
| 2025-04-21 | `feature` | Implement nested translation flattening in StepFunction and add corresponding unit tests | `StepFunction.java`, `StepFunctionTest.java` | [dbc258aa](https://github.com/freeplane/freeplane/commit/dbc258aafc17040c3597c4b94e6911825d6cbf18) |
| 2025-04-21 | `feature` | Add map option "force compact layout" | `mindmapmodemenu.xml`, `MapStyle.java` +5 | [2780b28c](https://github.com/freeplane/freeplane/commit/2780b28c5612ff5ce85707b709175c25f20ca2a4) |
| 2025-04-21 | `feature` | Enhance CombinedFunction to handle gaps between segments and improve constructor argument  | `StepFunction.java`, `StepFunctionTest.java` | [b5887977](https://github.com/freeplane/freeplane/commit/b5887977e9b17100dda5aaf761e777f0d57d3e8f) |
| 2025-04-20 | `feature` | Refactor StepFunction interface and implementations to unify samplePoints method and adjus | `StepFunction.java`, `StepFunctionTest.java` | [79bb4fe4](https://github.com/freeplane/freeplane/commit/79bb4fe4d2745c017386fd601d346937143c4941) |
| 2025-04-18 | `feature` | Add StepFunction class and corresponding tests | `StepFunction.java`, `StepFunctionTest.java` | [f6708d8f](https://github.com/freeplane/freeplane/commit/f6708d8f4a2a26b616a51df386e3bd8225a97d9f) |
| 2025-04-18 | `fix` | fix NPE | `AFilterComposerDialog.java` | [8587134e](https://github.com/freeplane/freeplane/commit/8587134e00fb32634e9b0fdc27873d8c55828ccb) |
| 2025-04-18 | `fix` | fix NPE | `NodeView.java` | [3ce589c4](https://github.com/freeplane/freeplane/commit/3ce589c454857cf5491892b43f6097d1b3c5b591) |
| 2025-04-13 | `fix` | make more robust fix for windows UI scroolbars | `AttributeViewScrollPane.java` | [c32fb200](https://github.com/freeplane/freeplane/commit/c32fb200e5f8b62adeaf16318b29e22cd8ce9505) |
| 2025-04-12 | `fix` | Fix unfold on drop for tags and for siblings | `MNodeDropListener.java` | [e9ac4aa7](https://github.com/freeplane/freeplane/commit/e9ac4aa7b5a66f42fa4d558eaae46b02ade0c302) |
| 2025-04-07 | `feature` | always delayed unfold and enable scroll on unfold | `NodeSelector.java` | [c4d7df3f](https://github.com/freeplane/freeplane/commit/c4d7df3fa7d8980ad6fabf61bed755b911972f90) |
| 2025-04-06 | `feature` | Add F2 key binding for editing in editable components' input maps | `OSKeyBindingManager.java` | [d8b47763](https://github.com/freeplane/freeplane/commit/d8b4776324f4d3f539400d7df2c7dd369169de17) |
| 2025-04-06 | `fix` | Fix adding missing hot keys to  input map by motif | `FrameController.java` | [bcf3a0dc](https://github.com/freeplane/freeplane/commit/bcf3a0dcf9d2f1755270ed8031c4ec84976dd433) |
| 2025-04-05 | `fix` | fix painting for large maps | `MapView.java` | [a1eff250](https://github.com/freeplane/freeplane/commit/a1eff250cb09b190fc760f89aadad8d1ecbfe262) |
| 2025-04-05 | `feature` | add method IMapViewManager.containsView | `IMapViewManager.java`, `HeadlessMapViewController.java` +1 | [7e9c723e](https://github.com/freeplane/freeplane/commit/7e9c723eb2362df0b6fec8e4610ecea6324a79ec) |
| 2025-04-05 | `fix` | fix updating reminder state icon after | `ReminderHook.java` | [1a5c193d](https://github.com/freeplane/freeplane/commit/1a5c193df523d4193c0f6fd118191ce3681b8b18) |
| 2025-04-05 | `feature` | add different listeners for map view created and map view displayed | `MapController.java`, `IMapViewChangeListener.java` +5 | [61401ab7](https://github.com/freeplane/freeplane/commit/61401ab7afc05c8cd433b636ddfe999197bcd227) |
| 2025-03-19 | `fix` | Fix NPE | `MapView.java` | [28071ba1](https://github.com/freeplane/freeplane/commit/28071ba1ff70e17a88fb9e0880012b2a2fe66b87) |
| 2025-03-18 | `fix` | Issue #2345 Fix connector collision detector | `CollisionDetector.java` | [92f3b403](https://github.com/freeplane/freeplane/commit/92f3b403dfa36a8c9c603cf5e1a7708d3af73866) |
| 2025-03-01 | `fix` | Fix drag and drop text as siblings after target node | `MMapClipboardController.java` | [58114caf](https://github.com/freeplane/freeplane/commit/58114caf5d8117323ee8913a5c22a2ea077afead) |
| 2025-03-01 | `fix` | Fix non local drag and drop as a sibling after the drop target node | `MNodeDropListener.java` | [6a922bed](https://github.com/freeplane/freeplane/commit/6a922beda68308eace2215c750ccf1d01d37990e) |
| 2025-03-01 | `fix` | Fix editor field bounds | `ZoomableLabelUI.java`, `EditNodeTextField.java` | [cc937009](https://github.com/freeplane/freeplane/commit/cc937009715625f78158e7989ba587aace74012f) |
| 2025-02-28 | `fix` | Fix editor background colors for transparent nodes | `ColorUtils.java`, `NodeView.java` | [b9878de1](https://github.com/freeplane/freeplane/commit/b9878de1be9245be7eedb2e01b7d9bba3da23baa) |
| 2025-02-27 | `fix` | fix reserved areas | `MapViewScrollPane.java` | [d40221ad](https://github.com/freeplane/freeplane/commit/d40221ad148155bf45a4f5a50980bc9fdb03786d) |
| 2025-02-27 | `fix` | fix reserved areas | `MapViewScrollPane.java` | [57cd8147](https://github.com/freeplane/freeplane/commit/57cd8147e205c363b044e0932b6d4511bf55e871) |
| 2025-02-24 | `fix` | fix method name | `MapViewSerializer.java` | [04271ac6](https://github.com/freeplane/freeplane/commit/04271ac61a20a5e3d05c0a7f82bd09999c034482) |
| 2025-02-24 | `fix` | Fix hidden areas | `MapViewScrollPane.java` | [39410616](https://github.com/freeplane/freeplane/commit/3941061690db5dfa094a4400dfbf744a622c1a6e) |
| 2025-02-23 | `feature` | Add strike-through formatting action to shtml editor | `build.gradle`, `Resources_cs.properties` +28 | [f3b2f654](https://github.com/freeplane/freeplane/commit/f3b2f65406287367e063f2a9ea8b8806b49f604f) |
| 2025-02-23 | `feature` | Add strike-through formatting action  to inline editor | `EditNodeTextField.java` | [87bb70d4](https://github.com/freeplane/freeplane/commit/87bb70d4e7f46c78c8ae8dfae6d34045bbcdba83) |
| 2025-02-23 | `feature` | Issue #141 Add support for horizontal mouse scroll | `DefaultMouseWheelListener.java` | [7e0184f4](https://github.com/freeplane/freeplane/commit/7e0184f4a099ccf9889141ad0383956562270e90) |
| 2025-02-18 | `fix` | Fix icon and text placament for uniform nodes and variable inset painters | `VariableInsetsPainter.java`, `ZoomableLabelUI.java` +1 | [7d11b236](https://github.com/freeplane/freeplane/commit/7d11b236f4326d5faeafbc619da9b3136fdb8419) |
| 2025-02-18 | `fix` | Bug fix: Invalidate image viewers on zoom change | `ExternalResource.java`, `ViewerController.java` +3 | [38be47d8](https://github.com/freeplane/freeplane/commit/38be47d84a883b5f396f8cb5bf4a4a926cc2ff7e) |
| 2025-02-15 | `feature` | Add separator between attributes and tags | `MModeControllerFactory.java` | [e2a048e6](https://github.com/freeplane/freeplane/commit/e2a048e6e368742b38fa5aa7af617eafe8ebab64) |
| 2025-02-15 | `feature` | Add filter to tag tree in panel | `IconReplacer.java`, `GraphicIconFactory.java` +7 | [76d97c6d](https://github.com/freeplane/freeplane/commit/76d97c6dec781eb34c1bdded3eaadb1a093992c0) |
| 2025-02-15 | `feature` | Add new tab name to translated resources | `MModeControllerFactory.java`, `Resources_en.properties` | [c4474406](https://github.com/freeplane/freeplane/commit/c447440600c4f4160963202e356448a425b73773) |
| 2025-02-14 | `feature` | Add tag tree to panel containing attributes | `TagIcon.java`, `JTagTree.java` +5 | [1acbc263](https://github.com/freeplane/freeplane/commit/1acbc26358809e1d329b665f4cdc36ba36c2f334) |
| 2025-02-10 | `fix` | Issue #2281 fix: finish startup when map view and node are selected | `ApplicationViewController.java`, `FreeplaneGUIStarter.java` +1 | [59eb5c40](https://github.com/freeplane/freeplane/commit/59eb5c40a5b4b01ca8d49d3185692ec830307cc1) |
| 2025-02-09 | `feature` | reorder conditions also if new conditions are not saved | `FilterController.java` | [e2a62934](https://github.com/freeplane/freeplane/commit/e2a62934cf320c012834632e9c861a2a786fc581) |
| 2025-01-31 | `fix` | Option "Overwrite mind map files automatically", fix auto-save file removal | `preferences.xml`, `DoAutomaticSave.java` +3 | [1290dbc3](https://github.com/freeplane/freeplane/commit/1290dbc38be795e231ffbcfe3c4193c7aa47b0aa) |
| 2025-01-25 | `feature` | Add option to save applied quick filters | `history_en.txt`, `preferences.xml` +3 | [36658a75](https://github.com/freeplane/freeplane/commit/36658a75be482fe7e18a899aa02b28ec6e39b5f2) |
| 2025-01-24 | `fix` | fix NPE | `UITools.java` | [9503e09f](https://github.com/freeplane/freeplane/commit/9503e09f1c526a01b1c60fb6fa71b05a108e1e71) |
| 2025-01-24 | `fix` | fix NPE | `MapView.java` | [fa294a6b](https://github.com/freeplane/freeplane/commit/fa294a6b7f37bcac8d17f5fec0a687384b2c0fd0) |
| 2025-01-24 | `feature` | Issue #2239 Saved filters / New filters get magically added | `FilterController.java` | [3d12ca2d](https://github.com/freeplane/freeplane/commit/3d12ca2d8cd1d92c00017180e00d61005a352586) |
| 2025-01-19 | `fix` | fix node with editing field layout | `EditNodeTextField.java` | [61cf2737](https://github.com/freeplane/freeplane/commit/61cf27379f960f8ff53c07134c17082c0e6f53df) |
| 2025-01-19 | `fix` | fix getUIIconAt point | `MultipleImageIcon.java` | [503c2248](https://github.com/freeplane/freeplane/commit/503c22489b66b4a7ad719f49877457ec1309ff55) |
| 2025-01-18 | `feature` | Add option "antialias_during_scrolling" | `history_en.txt`, `preferences.xml` +3 | [30c1a564](https://github.com/freeplane/freeplane/commit/30c1a56410d2094c84f28f543fe1aae513ddf27a) |
| 2025-01-18 | `fix` | fix antialiasing | `AntiAliasingConfigurator.java` | [7e01a7ac](https://github.com/freeplane/freeplane/commit/7e01a7acaf32e4b436e7e9d4ef294a2bb6e7c6ed) |
| 2025-01-18 | `fix` | fix antialiasing | `AntiAliasingConfigurator.java` | [82b043e8](https://github.com/freeplane/freeplane/commit/82b043e8bcb967b66fa496fa91b38bbe92946d2a) |
| 2025-01-17 | `fix` | fix style panel layout | `StyleControlGroup.java` | [195ec114](https://github.com/freeplane/freeplane/commit/195ec1147b059e85d916e429a1fcdf2308f54787) |
| 2025-01-14 | `fix` | fix antialiasing configurator | `AntiAliasingConfigurator.java` | [be034227](https://github.com/freeplane/freeplane/commit/be0342273b1321c523c04ea368b113c39b62bde6) |
| 2025-01-12 | `fix` | fix antialias options for tagicon | `AntiAliasingConfigurator.java`, `TagIcon.java` +1 | [58d83598](https://github.com/freeplane/freeplane/commit/58d835985561cfaa00b3c9b0d80448904c67916b) |
| 2025-01-12 | `fix` | fix tag colors for categorized tags | `IconController.java` | [7f5ebef2](https://github.com/freeplane/freeplane/commit/7f5ebef26129264bc0722eddc08aada5a55f80bd) |
| 2025-01-12 | `fix` | fix tag component width calculation | `NodeView.java` | [d3fef87e](https://github.com/freeplane/freeplane/commit/d3fef87e6ebababa5e3be908d381f05b0bb84005) |
| 2025-01-12 | `fix` | fix tag icon component size | `NodeView.java` | [20ce4f21](https://github.com/freeplane/freeplane/commit/20ce4f2150a2d54b92b662857ca034a37d6233a5) |
| 2025-01-11 | `feature` | Add alignment style option to attributes | `StylePropertyAdjuster.java`, `AttributeView.java` | [1382816e](https://github.com/freeplane/freeplane/commit/1382816ea654606fac3ad3580fdd8f26c07ea6c1) |
| 2025-01-11 | `feature` | Add color and alignment style options to tags | `TagIcon.java`, `IconController.java` +2 | [a44da912](https://github.com/freeplane/freeplane/commit/a44da9120b1a358273ea382e382d93a8391551fd) |
| 2025-01-11 | `fix` | fix AntiAliasingConfigurator | `AntiAliasingConfigurator.java`, `MapView.java` | [6cc15978](https://github.com/freeplane/freeplane/commit/6cc15978a469c0c037da15eee9214efb7df8f95d) |
| 2025-01-08 | `fix` | Fix bugs | `FileOpener.java`, `IconListComponent.java` +5 | [e74bf9f4](https://github.com/freeplane/freeplane/commit/e74bf9f487f1fdd27d184b501023f2411a39d662) |
| 2025-01-08 | `feature` | Improve MNodeDropListener to better support tags | `NodeView.java`, `MNodeDropListener.java` | [e5e5ad68](https://github.com/freeplane/freeplane/commit/e5e5ad681cd082212a41f8da8a1fa9f44d5b33e1) |
| 2025-01-08 | `fix` | fix node tooltip location | `MainView.java` | [22520ebe](https://github.com/freeplane/freeplane/commit/22520ebe6dc8131f2272461db05e1605041b8627) |
| 2025-01-07 | `fix` | fix layout when icons are painted above text | `ZoomableLabelUI.java`, `EditNodeTextField.java` | [70be7221](https://github.com/freeplane/freeplane/commit/70be7221a0bc6d1dd9d51ac5b59f44c1817b28ad) |
| 2025-01-06 | `fix` | Issue #2199 "OS-Command links with spaces are misinterpreted on Linux" | `LinkController.java` | [175ecee5](https://github.com/freeplane/freeplane/commit/175ecee54f61d0229817d58dcddcd58040eab1be) |
| 2025-01-04 | `fix` | fix rendering | `TagIcon.java` | [c4825d64](https://github.com/freeplane/freeplane/commit/c4825d649fa36da05d7e23eea101e669c280897e) |

### Dettagli commit con note

**[214baa9b](https://github.com/freeplane/freeplane/commit/214baa9ba91823c6c50e33e090769984a8fe338c)** (2025-11-23) — Upgrade AES encryption from CBC to GCM mode

> - Switch from AES/CBC/PKCS5Padding to AES/GCM/NoPadding for authenticated encryption
> - Reduce IV length from 16 to 12 bytes (GCM standard)
> - Replace IvParameterSpec with GCMParameterSpec (128-bit authentication tag)
> - Add handling for AEADBadTagException in decryption
> - Modernize test assertions from Hamcrest to AssertJ
> - Update test expectations for new IV length
> 
> GCM mode provides authenticated encryption, protecting against tampering
> and eliminating padding oracle vulnerabilities present in CBC mode.

**[73858dd9](https://github.com/freeplane/freeplane/commit/73858dd970b75061e1b1396a3f2a9efd710d1e2c)** (2025-11-23) — Feature/aes 256 encryption (#2726)

> * initial commit
> 
> * fix salt parameters
> 
> * Fix encoding inconsistency - use StandardCharsets.UTF_8
> 
> Replace string literals 'UTF-8' and 'UTF8' with StandardCharsets.UTF_8
> throughout Aes256Encrypter and DesEncrypter for consistency and to
> avoid potential UnsupportedEncodingException (which should never occur
> with UTF-8 but requires handling when using string literals).
> 
> This change:
> - Adds StandardCharsets import to both encrypter classes
> - Replaces all getBytes("UTF-8") with getBytes(StandardCharsets.UTF_8)
> - Replaces all new String(bytes, "UTF8") with new String(bytes, StandardCharsets.UTF_8)
> - Ensures consistent encoding across all encryption implementations
> 
> Addresses issue #3 from SECURITY_ISSUES.md
> 
> * Fix version marker collision risk
> 
> Change AES-256 version marker from 'AES256:' to 'FP-AES256-V1:' to reduce
> the risk of collision with base64-encoded legacy DES data.
> 
> The new marker:
> - Uses 'FP' prefix to identify Freeplane
> - Includes algorithm identifier 'AES256'
> - Adds version 'V1' for future compatibility
> - Contains hyphens which are not part of base64 alphabet, making
>   false detection extremely unlikely
> 
> Addresses issue #4 from SECURITY_ISSUES.md
> 
> * Add logging to silent exception handling in DesEncrypter
> 
> Replace empty catch blocks with appropriate logging in DesEncrypter
> to aid debugging and troubleshooting.
> 
> Changes:
> - decrypt(): Use debug-level logging for crypto exceptions since
>   we expect failures when trying wrong algorithms during fallback.
>   This prevents log spam while still capturing information when
>   debug logging is enabled.
> - decrypt(): Use warn level for UnsupportedEncodingException as
>   this should never happen with StandardCharsets.UTF_8
> - encrypt(): Use severe level for all exceptions as encryption
>   failures are unexpected and critical
> 
> Addresses issue #5 from SECURITY_ISSUES.md
> 
> * Improve validation in EncryptionHelper.isValidDecryption()
> 
> Enhance the decryption validation to reduce false positives when trying
> multiple algorithms during fallback.
> 
> Improvements:
> - Add check for closing tag (</node>) or self-closing tag (/>)
> - Add balanced angle bracket validation to catch obvious garbage
> - Keep validation lightweight (no full XML parsing) for performance
> - Add detailed documentation about validation strategy
> 
> The enhanced validation prevents accepting corrupted data that happens
> to start with '<node ' but isn't actually valid XML.
> 
> Addresses issue #6 from SECURITY_ISSUES.md
> 
> * Add destroy() method to IEncrypter interface
> 
> Add destroy() method to IEncrypter interface for proper cleanup of
> sensitive data (passwords, keys, salts) from memory.
> 
> This is a critical security improvement that prevents passwords from
> remaining in memory longer than necessary. The destroy() method must
> be implemented by all IEncrypter implementations and called when the
> encrypter is no longer needed.
> 
> Part of addressing issue #2 (Password Not Cleared from Memory) from
> SECURITY_ISSUES.md
> 
> * Implement destroy() in Aes256Encrypter with memory cleanup
> 
> Implement the destroy() method in Aes256Encrypter to properly clean up
> sensitive data from memory:
> 
> Security measures:
> - Zero out password character array with Arrays.fill()
> - Zero out salt byte array
> - Clear cipher and parameter references for garbage collection
> 
> This prevents passwords from remaining in memory in heap dumps or
> during debugging sessions, reducing the attack surface.
> 
> Part of addressing issue #2 (Password Not Cleared from Memory) from
> SECURITY_ISSUES.md
> 
> * Implement destroy() in DesEncrypter with memory cleanup
> 
> Implement the destroy() method in DesEncrypter to properly clean up
> sensitive data from memory. This implementation applies to all DES
> variants (SingleDesEncrypter and TripleDesEncrypter) since they
> inherit from DesEncrypter.
> 
> Security measures:
> - Zero out password character array with Arrays.fill()
> - Zero out salt byte array
> - Clear cipher references for garbage collection
> 
> This completes the password cleanup implementation across all
> encryption algorithms.
> 
> Completes addressing issue #2 (Password Not Cleared from Memory) from
> SECURITY_ISSUES.md - implementations are done, next step is to ensure
> destroy() is called appropriately.
> 
> * Call destroy() on encrypters to clean up passwords from memory
> 
> Update all code paths to properly clean up encrypters when they are no
> longer needed, ensuring passwords are cleared from memory.
> 
> Changes:
> 1. EncryptionModel.unlock(): Destroy the stored encrypter when unlocking
> 2. EncryptionController.decrypt(): Use try-finally to destroy temporary
>    encrypter after password verification
> 3. EncryptionHelper.tryDecryptWithAllAlgorithms(): Destroy each encrypter
>    after attempting decryption during algorithm fallback
> 
> This completes the implementation of issue #2 (Password Not Cleared
> from Memory) from SECURITY_ISSUES.md. Passwords are now properly
> zeroed from memory as soon as they are no longer needed.
> 
> * Implement complete algorithm fallback in EncryptionModel
> 
> Add proper fallback logic to try all available encryption algorithms
> when the initially detected algorithm fails to decrypt content. This
> is critical for backward compatibility with legacy DES/TripleDES
> encrypted content.
> 
> Implementation:
> 1. Simplify checkAndSetEncrypter() to just validate and set
> 2. Add new decryptWithFallback() method that:
>    - Tries all available algorithms using EncryptionHelper
>    - Validates decrypted content
>    - Parses and loads the decrypted nodes
>    - Creates new AES-256 encrypter for future operations (auto-upgrade)
> 3. Update EncryptionController.decrypt() to:
>    - First try with detected algorithm
>    - Fall back to trying all algorithms if that fails
>    - Properly clean up temporary encrypters
> 
> This ensures users with legacy encrypted content can always decrypt
> their data, and the content will be automatically upgraded to AES-256
> on the next save.
> 
> Addresses issue #1 (Incomplete Algorithm Fallback Implementation) from
> SECURITY_ISSUES.md
> 
> * Fix linter errors - remove unused imports and invalid exception handlers
> 
> Remove UnsupportedEncodingException catch blocks that are no longer
> needed after switching to StandardCharsets.UTF_8. This encoding is
> guaranteed to be available and never throws UnsupportedEncodingException.
> 
> Also update exception handling in DesEncrypter to use comments instead
> of non-existent debug logging methods, explaining that these exceptions
> are expected during algorithm fallback attempts.
> 
> * Fix PBEKeySpec to explicitly include salt and iteration count
> 
> Pass salt and iteration count directly to PBEKeySpec constructor for
> explicit key derivation, rather than relying on PBEParameterSpec alone.
> This makes the key derivation process more maintainable and less reliant
> on implementation-specific behavior.
> 
> Addresses review feedback from Copilot AI.
> 
> * Add encrypter cleanup on EncryptionModel creation failure
> 
> Wrap EncryptionModel creation in try-catch blocks to ensure encrypters
> are properly cleaned up if initialization fails. This prevents passwords
> and keys from remaining in memory when errors occur.
> 
> The encrypter ownership is transferred to EncryptionModel on successful
> creation, and EncryptionModel.unlock() handles cleanup in normal cases.
> 
> Addresses review feedback from Copilot AI.
> 
> * Correct documentation: CBC mode, not GCM (no authenticated encryption)
> 
> Fix critical documentation error: The implementation uses CBC mode, not
> GCM mode, and therefore does NOT provide authenticated encryption or
> tamper detection as initially claimed.
> 
> Update javadoc to clearly state:
> - AES-256 in CBC mode (not GCM)
> - No authenticated encryption
> - No cryptographic tamper detection
> - Primary improvement is 256-bit key size and PBKDF2-HMAC-SHA256
> 
> This addresses the discrepancy between the PR description claiming
> 'AES-256-GCM with authenticated encryption' and the actual implementation
> using PBEWithHmacSHA256AndAES_256 which is CBC-based.
> 
> Addresses critical review feedback from Copilot AI and maintainer.
> 
> * Restore Gradle test discovery settings
> 
> The initial commit accidentally removed test configuration settings that were
> added in commit 7098c15e87 to handle Gradle 9.0's stricter test discovery.
> 
> These settings allow subprojects with non-JUnit test files (like TestApp in
> freeplane_framework) to build successfully without failing on test discovery.
> 
> This change is unrelated to the AES-256 encryption feature and restores the
> intended build configuration.
> 
> * Fix encrypter lifecycle to prevent null pointer on re-lock
> 
> The encrypter was being destroyed prematurely in the decrypt() method,
> causing mEncrypter to be null when attempting to re-lock a node. This
> resulted in an IllegalStateException when toggling encryption state.
> 
> Changes:
> - Remove try-finally block that destroyed encrypter after decryption
> - Only destroy encrypter if decryption fails with detected algorithm
> - Preserve encrypter in EncryptionModel for re-encryption on lock()
> - Add destroy() method for proper cleanup when encryption is removed
> - Add diagnostic logging to track encrypter lifecycle
> - Add null check in encryptXml() with clear error message
> 
> The encrypter is now properly preserved after successful decryption and
> reused when the node is locked again, preventing the null pointer issue.
> 
> * Add comprehensive automated tests for AES-256 encryption
> 
> - Add 135+ test methods across 4 test classes
> - Test AES-256 encryption and backward compatibility with DES/TripleDES
> - Cover edge cases, error handling, and real-world XML scenarios
> - Include README documenting test suite
> 
> Tests can be run with:
>   gradle test --tests 'org.freeplane.features.encrypt.*'
> 
> * Fix AES-256 encryption to support Unicode passwords
> 
> Replace PBE algorithm with PBKDF2WithHmacSHA256 for key derivation
> combined with standard AES/CBC/PKCS5Padding. This change enables
> full Unicode password support (Chinese, Japanese, Cyrillic, emojis, etc.)
> while maintaining AES-256 security with 100,000 PBKDF2 iterations.
> 
> The previous PBEWithHmacSHA256AndAES_256 implementation had ASCII-only
> password restrictions that caused encryption failures with non-ASCII
> characters. The new approach uses:
> - PBKDF2WithHmacSHA256 for key derivation (supports Unicode)
> - AES-256 in CBC mode with explicit IV management
> - Encrypted format: VERSION_MARKER + salt + IV + ciphertext
> 
> All 107 encryption tests now pass, including Unicode password tests.
> 
> * Add binary header format for encrypted content
> 
> Implement 8-byte binary header format for encrypted map data:
> - Bytes 0-3: Magic number 'FPM\x01' (Freeplane Map encryption v1)
> - Bytes 4-7: Algorithm ID ('AES2', 'DES\x00', '3DES')
> 
> Benefits:
> - Trivial algorithm detection (read first 8 bytes)
> - Extensible for future algorithms (AESG, C20P, etc.)
> - Space efficient (8 bytes vs 13+ chars text marker)
> - Self-documenting with magic number
> 
> Changes:
> - Add EncryptionHeader class for header management
> - Update Aes256Encrypter to use binary headers
> - Update EncryptionHelper for header-based detection
> - Add comprehensive test suite (25+ tests)
> - Full backward compatibility with old text marker format
> 
> All existing encrypted maps continue to work. New encryptions
> automatically use binary header format. Maps are upgraded on save.
> 
> Technical docs: freeplane/src/main/java/org/freeplane/features/encrypt/IMPLEMENTATION.md
> 
> * Update encryption tests to cover new binary header format
> 
> * Enhance AES-256 to DES fallback mechanism documentation and testing
> 
> - Add explicit documentation that fallback occurs even when AES-256 magic numbers are present
> - Add logging when fallback from AES-256 to legacy algorithms is triggered
> - Add test cases to verify fallback behavior works correctly
> - Update IMPLEMENTATION.md with detailed fallback mechanism explanation
> 
> The fallback mechanism was already working correctly - these changes make it
> more explicit, maintainable, and debuggable. Addresses maintainer feedback about
> ensuring fallback to old algorithms when magic number decryption fails.
> 
> * Refactor encryption code to minimize comments
> 
> Remove redundant inline comments and condense JavaDoc across encryption
> classes, following clean code principles. Changes preserve all
> functionality with zero logic modifications.
> 
> Changes:
> - Aes256Encrypter: Condense class JavaDoc, remove 15+ inline comments
> - EncryptionHelper: Streamline method documentation
> - EncryptionHeader: Remove obvious implementation comments
> - EncryptionController: Simplify resource ownership notes
> 
> Kept essential documentation:
> - Security warnings (CBC mode limitations)
> - Resource lifecycle management notes
> - Backward compatibility references
> - Minimal class-level purpose statements
> 
> All 124 encryption tests pass. Net reduction: 262 lines.
> 
> * add support for textual header format in encryption
> 
> * Work on AES-256 encryption implementation
> 
> * Remove AI clutter: simplify comments and remove redundant documentation
> 
> - Remove excessive comments from destroy() methods that explain what the code does
> - Simplify IEncrypter.destroy() javadoc to be concise
> - Remove verbose ownership comments in EncryptedMap
> - Keep code self-documenting per coding guidelines
> 
> * Remove empty else block and verbose javadoc from EncryptionHelper
> 
> - Remove empty else block in EncryptionModel.lock()
> - Remove redundant javadoc that explains what code does
> - Method names are self-documenting
> 
> * Remove AI clutter: section dividers and redundant comments
> 
> - Remove decorated section dividers (// ========== ... ==========) from tests
> - Remove redundant comments explaining what code does
> - Remove excessive javadoc in test methods
> - Test method names are self-documenting
> 
> * Remove redundant javadoc from EncryptionModel.destroy()
> 
> - Method purpose is clear from interface definition
> 
> * Remove IMPLEMENTATION.md from production source tree
> 
> Documentation files should not be in production source code.
> Code should be self-documenting.
> 
> * Simplify class javadoc to match existing codebase style
> 
> Replace verbose javadoc with minimal @author style consistent with
> DesEncrypter and other original classes. Remove method javadoc.
> 
> * Remove test documentation README
> 
> Project does not use test documentation files. Tests should be
> self-documenting through descriptive method names.
> 
> * Remove inconsistent @author tags from new classes
> 
> Codebase pattern uses actual author names (Dimitry Polivaev, foltin, etc.)
> or no javadoc at all. 'Freeplane team' is not consistent with existing code.
> 
> * Remove verbose AI-style error messages to match codebase
> 
> Match DesEncrypter error handling pattern:
> - decrypt(): silent failures (empty catch blocks)
> - encrypt(): minimal log messages with algorithm prefix
> - init(): log exception only without explanatory text
> 
> Remove verbose descriptions like 'Strong', 'Weak', 'will be upgraded'
> to match minimal codebase style.
> 
> * Remove AI accidental complexity from EncryptionHeader
> 
> Removed unnecessary abstraction layers:
> - Removed Algorithm enum with unused description field
> - Removed unused methods: fromEncryptedString(), hasHeader(), getDescription()
> - Removed unnecessary object creation (new EncryptionHeader())
> - Simplified to direct string prefix checks
> - Updated all tests to test actual behavior instead of abstraction
> 
> EncryptionHeader now contains only:
> - Three PREFIX constants
> - One stripPrefix() method
> 
> Reduced from 117 lines to 19 lines (-84%).
> 
> * Remove unnecessary complexity: tryDecryptWithAllAlgorithms and isAes256Encrypted
> 
> Per maintainer feedback:
> - AES-256 is NEW, no legacy AES format exists
> - Removed tryDecryptWithAllAlgorithms fallback mechanism (unnecessary)
> - Removed isAes256Encrypted helper (use startsWith directly)
> - Simplified: if has prefix → trust it, if no prefix → legacy DES
> 
> Tests updated to use direct createDecrypter().decrypt() calls.
> 
> * Remove empty javadoc comment (AI clutter)
> 
> * remove redundant tests
> 
> * Refactor encryption tests to simplify assertions and remove redundant comments
> 
> * fix imports
> 
> * Remove unused PREFIX_3DES and PREFIX_DES constants from EncryptionHeader
> 
> These prefixes cannot be created by any production code path as neither
> SingleDesEncrypter nor TripleDesEncrypter add prefixes when encrypting.
> Only PREFIX_AES256 can be created and is actively used.
> 
> * Remove TripleDesEncrypter references from EncryptionHelper
> 
> Remove the check for PREFIX_3DES in createDecrypter() and
> getEncryptionAlgorithmDescription() as this prefix cannot be created
> by any code path. The system now only distinguishes between AES-256
> (with prefix) and legacy DES (without prefix).
> 
> * Delete unused TripleDesEncrypter class
> 
> TripleDesEncrypter was never used to create encrypted content. Only
> SingleDesEncrypter was used in the creation path before AES-256 was
> introduced. This class has existed since 2008 but remained unused.
> 
> * Remove PREFIX_3DES and PREFIX_DES tests from EncryptionHeaderTest
> 
> Remove tests for unused PREFIX_DES and PREFIX_3DES constants that
> cannot be created by any production code path.
> 
> * Remove TripleDesEncrypter tests from EncryptionTest
> 
> Remove all tests that use TripleDesEncrypter as this class was never
> used in production and has been deleted.
> 
> ---------
> 
> Co-authored-by: Dimitry Polivaev <dpolivaev@gmx.de>

**[1da5a64f](https://github.com/freeplane/freeplane/commit/1da5a64f1eab7c37cb55ad8f9a06e192052093f0)** (2025-10-10) — Fix class cast exception

> java.lang.ClassCastException: class org.freeplane.view.swing.map.DetailsView cannot be cast to class org.freeplane.view.swing.map.MapView (org.freeplane.view.swing.map.DetailsView and org.freeplane.view.swing.map.MapView are in unnamed module of loader 'app')
> 	at org.freeplane.view.swing.ui.NodeSelector.lambda$1(NodeSelector.java:55)
> 	at org.freeplane.view.swing.ui.NodeSelector.getSelectionBehavior(NodeSelector.java:269)
> 	at org.freeplane.view.swing.ui.NodeSelector.handleMouseEvent(NodeSelector.java:156)
> 	at org.freeplane.view.swing.ui.DefaultMapMouseListener.mouseMoved(DefaultMapMouseListener.java:134)

**[a8bcb1c3](https://github.com/freeplane/freeplane/commit/a8bcb1c3ad1ddf7f4885ee0c43a763726a7fe1ea)** (2025-09-14) — Issue #2667: Highlight ascendant edges using selection rectangle color

> - Add  preference and ResourceController constant.
> - Cache flag and color rule in MapView; expose package-private accessors; update cache on color/property changes; repaint on selection change while enabled.
> - NodeView: override edge color for selected node and ancestors using cached ConstantObject color.
> - Register preference in preferences.xml and default in freeplane.properties.
> - Add English OptionPanel strings (label + tooltip).
> - Menu: replace ShowSelectionAsRectangleAction with boolean toggle and add new toggle for ascendant edge highlight.
> - EdgeController: minor cleanup (whitespace; simplify getColor signature).

**[2f589672](https://github.com/freeplane/freeplane/commit/2f589672b13c08b403bc59776124ab7f0f21e5fd)** (2025-09-13) — Outline: align breadcrumb panel with viewport inner area and clarify API

> - Anchor breadcrumb to viewport border bounds + JViewport insets to remove top gap where content could peek through.
> - Replace BreadcrumbPanel.calculateBounds() with getPreferredBreadcrumbHeight() and rename internal field to preferredBreadcrumbHeight for clarity.
> - Update OutlinePane to use preferred height when setting bounds.
> 
> No behavior change to scrolling logic; fixes visual misalignment across L&Fs.

**[8fd28351](https://github.com/freeplane/freeplane/commit/8fd28351dec4e78c0fb7b56728a1f4c23fb25e83)** (2025-09-12) — outline: cleanup and visibility fixes

> - Restore required {/**/} empty blocks; strip comments/FQNs in touched files
> - Add early-exit breadcrumb check tied to first fully visible node
> - Ensure selection anchors to top with final stabilization pass
> - Refine viewport visibility (isNodeFullyVisibleInViewport)
> - Make visible index lookup O(1) via VisibleOutlineState index map
> - Remove unused code (delete ExpansionHandler, minor dead code)

**[95324067](https://github.com/freeplane/freeplane/commit/95324067725cec52a341a74a811cc0bdc3c6a1bc)** (2025-09-12) — Outline: debounce scroll and streamline breadcrumb updates

> - OutlinePane: always call updateVisibleBlocks on vertical scroll and debounce 200 ms to call updateVisibleBlocksAndBreadcrumb; add Timer and constant; set scrollbar increment via UITools for both initial and new scroll panes.
> - BreadcrumbPath: make calculateBreadcrumbState() self-contained (no param), remove redundant checks, compute from first fully visible node.
> - ScrollableTreePanel: remove getCurrentBreadcrumbNodes(), adapt to new calculateBreadcrumbState(); ensure breadcrumb updates after navigation button scrolls.
> - OutlineViewport: remove unused helper, add toString for VisibleBlockRange, tidy imports.
> - NodePositioning: clarify division precedence in first visible index calculation.

**[4744f1f2](https://github.com/freeplane/freeplane/commit/4744f1f2892173f74ea30453725c2a6d6f38f24c)** (2025-09-11) — UI: add RadioButtonProperty and OptionPanelBuilder support for <radiobuttons>

> - New RadioButtonProperty renders a vertical group of JRadioButtons and
>   mirrors ComboProperty API (string lists and enum helpers).
> - OptionPanelBuilder: add RadioButtonsOptionCreator and register
>   element handler name 'radiobuttons'; supports enum="..." and explicit
>   <option value text/icon> children with optional icons.
> - Layout/polish: label aligns with the first radio; subsequent radios are
>   stacked in a panel with no intra-block gap; ensure next property starts
>   on a fresh row (and append a row if needed) to avoid index errors;
>   handle wrapping when already at the second data column; propagate tooltips.
> - PropertyAdapter: make labelComponent protected to allow manual label
>   placement when building multi-row properties.
> - preferences.xml updated accordingly.
> 
> Build: verified with 'gradle :freeplane:compileJava'.

**[0899a23e](https://github.com/freeplane/freeplane/commit/0899a23e7129e6c32e950637e5f04cfcf834e3fa)** (2025-09-07) — outline: correct breadcrumb membership logic and refine selection scrolling

> - Replace index-based breadcrumb checks with actual path membership from BreadcrumbPanel.
> - Remove VisibleOutlineState.isNodeInBreadcrumbArea; all checks use panel’s breadcrumb list.
> - Update BlockPanel and ScrollableTreePanel to use isNodeInBreadcrumbArea(node).
> - Adjust scrollToSelectedNode to handle breadcrumb case by pinning selection to top and recalculating.
> 
> Additional: small API cleanups and consistency updates from prior step.

**[f56812c9](https://github.com/freeplane/freeplane/commit/f56812c933d46021b66613cf38ee9e01ff57098f)** (2025-09-07) — outline: refine scrolling and focus behavior

> - Skip content scrolling when selected node is in breadcrumb area.
> - NodePositioning: simplify selection icon API, remove root dependency.
> - ExpansionControls: preserve focus in outline on expand/collapse.
> - Guard toggle on leaf nodes.
> - Minor cleanups and FQCN tidy-ups.
> 
> Note: additional issues remain; committing incremental progress.

**[29d59b88](https://github.com/freeplane/freeplane/commit/29d59b88196ff896bc78369b492b942faa6b8e0b)** (2025-09-07) — outline: extract OutlineBlockLayout and delegate block management

> - Move block creation/clear/size/width into OutlineBlockLayout.
> - ScrollableTreePanel delegates to the new layout helper.
> - Preserve behavior; no UI changes intended.

**[623ecbbf](https://github.com/freeplane/freeplane/commit/623ecbbf755f0e132a10f5c2d819b38093874a47)** (2025-09-07) — outline: adopt 'level' terminology and remove FlatNode

> - Replace all remaining depth terminology with level for consistency with Freeplane.
> - TreeNode now carries authoritative level; setParent recomputes subtree levels.
> - VisibleOutlineState uses List<TreeNode> (FlatNode removed).
> - Update all consumers (layout, viewport, panels) to use node.getLevel().
> - Refresh REFACTORING.md to document the new invariants and removal of FlatNode.

**[c3338a39](https://github.com/freeplane/freeplane/commit/c3338a39ba88f9127febc463ae66923cc506fd96)** (2025-09-07) — outline: fix incorrect content-level indentation by using computed parent-chain depth

> - BlockPanel computes X from actual node depth instead of FlatNode.depth.
> - NodePositioning aligns navigation buttons using computed depth for content area.
> - Remove temporary stdout diagnostics.
> 
> This corrects cases where first-level nodes appeared at deeper levels under wrong parents in the outline.

**[dd34a602](https://github.com/freeplane/freeplane/commit/dd34a602a703e5ca9fe9c7b67b23beee64e54f73)** (2025-09-07) — outline: Phase 3 — introduce NodeButton and remove clientProperty usage

> - Add NodeButton (typed TreeNode binding) and replace JButton+clientProperty across BlockPanel,
>   BreadcrumbPanel, and ScrollableTreePanel.
> - Update visibility, focus, scrolling, and title-update paths to use NodeButton.getNode().
> - Keep visual/behavior identical; improves type safety and readability.

**[9850e425](https://github.com/freeplane/freeplane/commit/9850e425a225331f0d2f9542ce044f584885b463)** (2025-09-06) — outline: decouple view state from UI and adopt tell-don't-ask

> - VisibleOutlineState: remove BlockPanel storage; add behavior methods
>   (getVisibleNodeCount, getFlatNode, getFlatNodeAtIndex, getNodeIdAtVisibleIndex).
> - Introduce OutlineBlockViewCache owned by ScrollableTreePanel for block panels.
> - Adapt ScrollableTreePanel, BreadcrumbPath, MapAwareOutlinePane to new APIs.
> - Encapsulate DTOs: BreadcrumbState, OutlineViewport.VisibleBlockRange, OutlineViewState.
> - Add REFACTORING.md documenting plan, completed work, and next phases.
> 
> No functional changes intended; prepares for further SOLID refactors.

**[331aea3a](https://github.com/freeplane/freeplane/commit/331aea3a6d680cf94d6d1ca3aca6efc24e57bc30)** (2025-09-06) — Outline: refactor selection bridge, rename selection APIs, improve key bindings, and remove fully qualified class names

> - Replace fully qualified javax.swing usages with imports in BlockPanel and BreadcrumbPanel (InputMap, ActionMap, KeyStroke, AbstractAction); use ActionEvent import and explicit actionPerformed overrides.
> - Route selection through a concrete OutlineSelectionBridge: convert the previous interface to a class that targets MapView/Window, and wire it in MapAwareOutlinePane and BreadcrumbPanel.
> - Unify naming around outline selection:
>   - Rename selection field to outlineSelection in ScrollableTreePanel; update all references and accessors (getOutlineSelection).
>   - Rename selectNodeById to selectOutlineNodeById; update callers in OutlineController, MapAwareOutlinePane, and ScrollableTreePanel.
> - Improve keyboard interactions:
>   - Map ENTER to select and SPACE to toggle on outline and breadcrumb buttons.
>   - Use WHEN_ANCESTOR_OF_FOCUSED_COMPONENT consistently for panel-level bindings.
> - Simplify focus and refresh logic:
>   - Reduce restoreFocusIfNeeded to a single-parameter variant; adjust call sites.
>   - Remove the “force” path from refreshOutlineLater; streamline MapAwareOutlinePane refresh flow.
> - Cleanups and polish:
>   - Add serialVersionUID to Swing panels.
>   - Remove obsolete SelectionIndicator inner class from BreadcrumbPanel.
>   - Minor whitespace and import ordering fixes.
>   - In NodeTreeBuilder, replace org.freeplane.features.filter.Filter FQCN with imported Filter for clarity.

**[fe290858](https://github.com/freeplane/freeplane/commit/fe290858a79720448df4c7520398ee73f434d54c)** (2025-08-31) — Outline: forward outline selection to Freeplane selection via bridge

> - Add OutlineSelectionBridge interface and hook in ScrollableTreePanel
> - Bridge implemented in MapAwareOutlinePane with weak refs, no cycles
> - Forward only when owning MapView is selected and window matches
> - Suppress feedback by checking current core selection id first

**[0137a0e1](https://github.com/freeplane/freeplane/commit/0137a0e117da696377cdcf9a057653386481d579)** (2025-08-31) — Outline: implement MapAwareOutlinePane.SelectedNodeUpdater.onSelect

> - Resolve NodeModel to outline node or nearest visible ancestor
> - Do not change expansion levels; select ancestor if target hidden
> - Scroll to make target first visible when outside viewport/breadcrumb
> - Keep UI updates on EDT; small onSelect with extracted helpers

**[4cabd635](https://github.com/freeplane/freeplane/commit/4cabd63558982d22dce9dcf0586191ee4435fcfa)** (2025-08-31) — outline/bookmarks/window events: centralize per-window MapView selection changes in DockingWindows + controller gating

> - Emit afterWindowLastSelectedMapViewChanged/Removed only from DockingWindows property updates
> - Gate emission in MapViewController to focused window and value changes
> - Add robust fallback: resolve replacement MapView for window on focus/undock
> - Simplify panes (Outline/Bookmarks) to follow per-window callbacks only
> - Normalize types (MapView, Window) in IMapViewChangeListener; remove FQCNs
> - Remove redundant listeners and duplication; apply comment/import cleanup on changed files

**[9d571286](https://github.com/freeplane/freeplane/commit/9d571286c41a2344cf81df4e43a8f33b1460c705)** (2025-08-31) — outline: persist expansion state per MapView and simplify rebuild

> - Add OutlineViewState: firstVisibleNodeId + expansionLevels>0 + rootId + WeakReference<Filter>
> - Implement Filter.equals/hashCode and equalsIgnoringAncestors for reliable comparisons
> - Introduce NodeTreeBuilder: single-pass build + anchor calculation + state applicability
> - Remove OutlineTreeUpdater and NodeTreeFactory; move cleanup into OutlinePane
> - Update MapAwareOutlinePane to capture/save state per MapView, use builder, apply expansions when applicable, and scroll to computed anchor
> - Keep firstVisibleNodeId unconditional; gate expansion restore by root and filter equality
> - Preserve hidden-node flattening semantics during tree construction

**[0d76cdbd](https://github.com/freeplane/freeplane/commit/0d76cdbd2dac7d541607c4f3d0b13bf592c15f35)** (2025-08-30) — aux: move only note pane between frames; keep outline per-frame

> - Add AuxiliarySplitPanes.moveAuxiliaryNoteTo to encapsulate moving only level-0 auxiliary (notes)
> - Update FrameComponentMover to use the new method instead of moving all levels
> - Prevents unintended removal of the outline pane on focused window change

**[12d27803](https://github.com/freeplane/freeplane/commit/12d27803e75ba4f723b38e6e7b0068cc926e7fb8)** (2025-08-30) — ui: track per-window last selected MapView and expose getLastSelectedMapViewContainedIn

> - Rename IMapViewManager.findMapViewContainedIn to getLastSelectedMapViewContainedIn and allow null
> - Store per-Window last selected MapView on the Window RootPane client property
> - Update MapViewDockingWindows to set/clear property on docking focus/removal
> - Update FrameComponentMover and BookmarkToolbarPane to use the new method
> - Defer BookmarkToolbarPane refresh with SwingUtilities.invokeLater to avoid race during docking

**[39a8f08a](https://github.com/freeplane/freeplane/commit/39a8f08a010103dee1edbc5487e8a3e03d2a4245)** (2025-08-29) — Outline: incremental updates + safety fixes for node changes

> - Prevent NPE in NodePositioning.calculateNodeDepth when node is outside current tree; return -1 and guard callers.
> - Add incremental paths: updateNodeTitle(TreeNode) for rename-only, rebuildFromNode(TreeNode) for insert/delete starting from affected parent.
> - Breadcrumb-aware partial rebuild: when breadcrumb needs to change, compute state and call updateVisibleBlocks(state.firstVisibleNodeIndex) to keep content aligned.
> - Navigation buttons: hide before partial rebuilds and clear hovered node if it is no longer visible to avoid stale attachments.
> - Block cleanup: strengthen clearBlocks and partial removal to avoid lingering BlockPanels; skip re-creating blocks that already exist.
> - Wire OutlinePane + MapTreeNode to use the incremental paths for nodeChanged/insert/delete.

**[66eb78e9](https://github.com/freeplane/freeplane/commit/66eb78e993b1ddbfb4559a73f720996200c27f2a)** (2025-08-24) — Fix navigation buttons disappearing after expand/collapse in breadcrumb

> Change attachNavigationNode to always set hovered node instead of clearing it for breadcrumb nodes. This preserves the hovered state needed for navigation button restoration after breadcrumb rebuilds.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[440fa55e](https://github.com/freeplane/freeplane/commit/440fa55edd6683ffed0390a6ba4767dd526d1dad)** (2025-08-24) — Fix button overlap issue in outline virtual scrolling

> - Reorder operations in updateVisibleBlocksAndBreadcrumb: update visible nodes first, then calculate breadcrumbs, then create blocks
> - Remove duplicate updateVisibleNodes call from updateVisibleBlocks to prevent inconsistent state
> - Fix selection logic to use node IDs instead of text comparison
> - Remove debug logging
> 
> This fixes the issue where multiple buttons appeared at the same Y coordinate after node insertions, caused by breadcrumb height calculations and block positioning using different visible node lists.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[80edda63](https://github.com/freeplane/freeplane/commit/80edda632e665d81813b91b900bc6ca938f69c39)** (2025-08-24) — Implement live updates for outline with real map data

> - Complete MapTreeNode implementation with nodeChanged, onNodeInserted, onNodeDeleted
> - Fix selection logic to use node IDs instead of text comparison
> - Make TreeNode.title mutable for efficient text updates
> - Add recursive node creation for inserted subtrees
> - Implement proper listener cleanup to prevent memory leaks
> - Fix refreshTree to call updateVisibleBlocksAndBreadcrumb for full button updates
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[811a0b4a](https://github.com/freeplane/freeplane/commit/811a0b4a273df5c603a67f836811fc9bf780568c)** (2025-08-24) — Replace demo data with live map integration in OutlinePane

> - Replace static demo data with MapAwareOutlinePane that listens to map changes
> - Add NodeTreeFactory to convert NodeModel hierarchy to TreeNode structure
> - Add MapTreeNode with INodeView listeners for live updates
> - Fix virtual scrolling corruption by recreating components instead of updating state
> - Fix breadcrumb selection circle positioning after layout changes
> - Add proper getter methods and encapsulation to ScrollableTreePanel
> - Ensure OutlinePane works reliably with both scrollbar and mouse wheel scrolling
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[cd8be7a7](https://github.com/freeplane/freeplane/commit/cd8be7a70000e974ab056ec07de03ecb84e39e22)** (2025-08-23) — Add OutlinePane to level 1 pane with demo tree data

> - Initialize OutlinePane on left side of level 1 pane automatically
> - Extract DemoTreeFactory to separate public class for reusability
> - Make TreeNode class and constructor public for external access
> - Position OutlinePane on west (left) side by setting location before insertion
> - Provide hierarchical tree view alongside mind map for enhanced navigation
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[8223c6e8](https://github.com/freeplane/freeplane/commit/8223c6e8e54a2b0b4f2ee8cc0fce5b9817e69621)** (2025-08-23) — Implement N-level nested auxiliary split pane system

> - Replace static properties with configurable AuxiliarySplitPaneController
> - Add AuxiliarySplitPanes manager for N-level nested structure
> - Update ApplicationViewController to use manager with level-based operations
> - Fix FrameComponentMover to work with nested structure using manager API
> - Maintain backward compatibility with existing note functionality at level 0
> - Support dynamic property keys for multiple split pane instances
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[97b2243f](https://github.com/freeplane/freeplane/commit/97b2243fff8641442eb231126a665a19d2efbd94)** (2025-08-23) — Fix blue dot selection indicator positioning and reliability in outline view

> - Move selection dot from left side to right side of text labels
> - Replace unreliable mouseClicked with ActionListener for button selection
> - Add repaint() call to ensure selection changes are immediately visible
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[d9f8bfe5](https://github.com/freeplane/freeplane/commit/d9f8bfe5749b7ba83638ebecdbecaadb4558cfad)** (2025-08-16) — Add same map option to mouse over selection scope

> - Add selection_inside.same_map choice to preferences XML
> - Implement same_map logic in NodeSelector to only apply mouse over selection
>   within the currently selected map (matching the active selection)
> - Add English translation for selection_inside.same_map option
> - Update tooltip to include all four available scope options
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[26d7812a](https://github.com/freeplane/freeplane/commit/26d7812a2eb6526dc5f51c0d1259c79a96eb3fc6)** (2025-08-16) — Add mouse over selection scope configuration

> - Add mouse_over_selection_inside preference with three options:
>   - selected_map_view: Only apply mouse over selection to the currently selected map view
>   - selected_window: Only apply to maps in the focused window
>   - any_map: Apply to all map views (previous behavior)
> - Update NodeSelector to respect the new scope setting
> - Add English translations for the new preference combo
> - Set default to selected_map_view for more focused interaction
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[07371e95](https://github.com/freeplane/freeplane/commit/07371e95e0dcda9b208d67376e39ddf43069d238)** (2025-08-03) — Improve FrameComponentMover initialization and getCurrentRootComponent logic

> Enhance the frame component mover with proper initialization and improve
> root component detection with better error handling.
> 
> Changes:
> - Add parameterized constructor to FrameComponentMover taking initial JFrame
> - Initialize lastFocusedFrame with main application frame in constructor
> - Improve getCurrentRootComponent with explicit null checks and fallback logic
> - Fix full screen tab visibility logic (invert boolean for proper hiding)
> - Remove unused imports from AuxillaryEditorSplitPane after refactoring
> - Clean up FrameComponentMover imports
> 
> This ensures the component mover always starts with a valid frame reference
> and provides more robust root component detection for multi-window scenarios.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[a0ae2b91](https://github.com/freeplane/freeplane/commit/a0ae2b91a12ca0c7027fee44200ea0b265cf9440)** (2025-08-03) — Refactor auxiliary component management for dynamic split pane handling

> Simplify the auxiliary component system by removing complex factory patterns
> and field dependencies in favor of dynamic split pane lookup.
> 
> Changes:
> - Remove insertComponentIntoAllSplitPanes method from ViewController interface
> - Rename removeSplitPane to removeAuxiliaryComponent for better clarity
> - Replace mSplitPane field with getSplitPane() dynamic lookup methods
> - Remove activeComponentFactory and floating window insertion complexity
> - Update all ViewController implementations to match new interface
> - Simplify AuxillaryEditorSplitPane by removing complex removeSplitPane logic
> - Fix constant usage (WindowConstants.DO_NOTHING_ON_CLOSE, Frame.MAXIMIZED_BOTH)
> - Update MNoteController and CodeProjectController to use new method names
> 
> The new architecture works dynamically with the current focus context instead
> of maintaining stateful references, making it more reliable for multi-window
> scenarios and UI-follows-focus functionality.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[29541671](https://github.com/freeplane/freeplane/commit/2954167121c24ac442e312ff32c8c629a6b89d10)** (2025-08-03) — Improve floating window handling and tab area management

> Enhance the floating window system with better identification and
> consolidated tab area visibility control.
> 
> Changes:
> - Add FREEPLANE_FLOATING_WINDOW constant for client property storage
> - Store FloatingWindow reference in JFrame client property for reliable lookup
> - Consolidate setTabAreaVisiblePolicy methods into single boolean parameter method
> - Replace fragile component traversal with client property lookup for floating windows
> - Improve type safety by casting to JFrame explicitly
> - Simplify ApplicationViewController.setFullScreen to use consolidated API
> 
> This provides more reliable floating window identification and cleaner
> tab area management across all window types.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[10b03bcb](https://github.com/freeplane/freeplane/commit/10b03bcb3263353f6275906b8e906050200c7c11)** (2025-08-03) — Refactor setFullScreen methods for better frame-specific handling

> Improve full screen functionality by making frame parameter explicit and
> ensuring proper property updates and event handling.
> 
> Changes:
> - Split FrameController.setFullScreen into two overloads for better API clarity
> - Add setFullScreen(JFrame, boolean) to allow operating on specific frames
> - Move property change notification logic into setFullScreenOnMac method
> - Update ApplicationViewController to override new frame-specific method
> - Fix fullScreenToggled to call setFullScreen for proper event handling
> - Use explicit frame parameter instead of re-detecting current frame
> 
> This provides better control over which frame enters/exits full screen mode
> and ensures consistent property updates across all full screen transitions.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[6c347bbd](https://github.com/freeplane/freeplane/commit/6c347bbd3a9c3486e72fb734ee91a932a31db1ea)** (2025-08-03) — Fix macOS full screen detection for multi-monitor setups

> Replace unreliable position-based detection (window.getY() == 0) with proper
> macOS FullScreenListener API. The position check failed on multi-monitor
> configurations where windows could have Y coordinates other than 0.
> 
> Changes:
> - Add fullScreenToggled(JFrame, boolean) method to ViewController interface
> - Implement fullScreenToggled in FrameController to update FULLSCREEN_ENABLED_PROPERTY
> - Create FullScreenListener proxy in MacChanges constructor to detect actual state changes
> - Add Compat.registerFullScreenListener() to expose registration cross-platform
> - Register listener for main application frame in ApplicationViewController.initFrame()
> - Register listener for floating window frames in MapViewDockingWindows
> - Update MacChanges.setFullScreen() to use listener-tracked state instead of position
> - Fix floating window component access in MapViewDockingWindows tab policies
> 
> The listener-based approach provides reliable full screen detection across all
> monitor configurations by using native macOS events instead of window positioning.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

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

**[35ee57d0](https://github.com/freeplane/freeplane/commit/35ee57d0fb72eda827157d251fc49c96d82c2369)** (2025-08-03) — Implement single note panel that moves between frames

> - Revert MNoteController to 1.12.x singleton pattern with static notePanel
> - Enhance FrameComponentMover to move auxiliary components between split panes
> - Modify ApplicationViewController to not create new components for floating windows
> - Update AuxillaryEditorSplitPane to support auxiliary component removal/re-addition
> - Keep auxiliary panel infrastructure while ensuring only one note panel moves between frames
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[2ea52fb1](https://github.com/freeplane/freeplane/commit/2ea52fb1cf6fb7da5f90a8353310c94493cd8a3b)** (2025-08-03) — Experimental: Implement UI follows focus with FrameComponentMover

> Add experimental functionality to move UI components (toolbars, panels, menus) between frames when user focus changes. Components dynamically follow the user's attention from main window to floating windows and vice versa.
> 
> Features:
> - FrameComponentMover class using KeyboardFocusManager for global focus tracking
> - Moves menu bars, BorderLayout components (NORTH/SOUTH/EAST/WEST) between frames
> - Mac-specific menu handling with apple.laf.useScreenMenuBar property
> - Install/uninstall pattern for clean lifecycle management
> - Automatic detection of focus changes between any JFrame windows
> 
> Technical approach:
> - Uses PropertyChangeListener on KeyboardFocusManager's "focusedWindow" property
> - No manual frame registration needed - works globally for all JFrames
> - Preserves existing InfoNode floating window sizing functionality
> - Clean separation of concerns with dedicated component mover class
> 
> Platform behavior:
> - Windows/Linux: Physical menu/component movement between windows
> - Mac: Menu content changes in system menu bar (native Mac behavior)
> 
> This creates a unified "UI follows focus" experience across all platforms.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[2b53ab84](https://github.com/freeplane/freeplane/commit/2b53ab84e9ecee0d6db076b3853ce952e2558905)** (2025-08-03) — Fix InfoNode floating window sizing by capturing CENTER component size

> InfoNode's FloatingWindow.setInternalSize() only considers the main component size and ignores additional components that Freeplane adds (auxiliary panels, dividers). This causes floating windows to be undersized.
> 
> Solution: Capture the actual size of the CENTER component from the main frame's BorderLayout when a window is removed, then apply this size directly to floating windows using InfoNode's own setInternalSize() pattern.
> 
> - Add capturedCenterSize field to store measured size
> - Capture CENTER component size in windowRemoved()
> - Apply captured size in windowAdded() using InfoNode's setPreferredSize/pack/reset pattern
> - Simple and reliable approach without complex proportional mathematics
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[6b94e1b8](https://github.com/freeplane/freeplane/commit/6b94e1b88977b25bec52c76980a6415a6e18753f)** (2025-08-02) — Improve split pane position management with proportional values

> - Add getProportionalDividerLocation() method to AuxillaryEditorSplitPane
> - Change split pane position storage from integer to double proportional values (0.0-1.0)
> - Rename property keys to AUX_SPLIT_PANE_LAST_*_POSITION to avoid conflicts
> - Use Double.NaN as default value instead of magic numbers
> - Fix imports in ApplicationViewController and MapViewDockingWindows
> - Extract floating window component insertion logic into separate method
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[cb4c82c5](https://github.com/freeplane/freeplane/commit/cb4c82c5571748c509207808bc79a583eb226a42)** (2025-08-02) — Store component factory in ApplicationViewController for automatic floating window component insertion

> Move auxiliary pane creation logic to ApplicationViewController and store active component factory to ensure new floating windows automatically inherit currently active components (like note panels).
> 
> Key changes:
> - ApplicationViewController: Store activeComponentFactory field and apply to new floating windows
> - Clear factory on removeSplitPane() to handle component removal lifecycle
> - Move bookmarkToolbarPanes map ownership from MapViewDockingWindows
> - Delegate floating window creation/removal to ApplicationViewController
> - Automatic component insertion based on stored factory state
> 
> This ensures new floating windows get the same components as existing windows without requiring factory storage in MapViewDockingWindows or direct MNoteController access.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[39a2b362](https://github.com/freeplane/freeplane/commit/39a2b36222f6b6b60a08b0f054bbedb560071b5f)** (2025-08-02) — Implement factory pattern for note panels across all windows

> Add insertComponentIntoAllSplitPanes() method to ViewController interface that uses Function<JRootPane, JComponent> factory pattern for global component insertion. This enables note panels to appear in both main window and floating windows simultaneously when preferences are enabled.
> 
> Key changes:
> - ViewController: Add factory method for per-frame component creation
> - ApplicationViewController: Apply factory to main window and delegate to floating windows
> - MapViewDockingWindows: Add methods to iterate floating windows and apply factory
> - MNoteController: Use factory pattern leveraging existing per-frame NotePanel logic
> - Update all ViewController implementations for interface compliance
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[8019e6dc](https://github.com/freeplane/freeplane/commit/8019e6dcd9015f41b0262a5b95aadcbaf5900901)** (2025-07-29) — Remove accidentally committed backup files and ignore them

> - Remove *.backup files that were accidentally committed during Unicode repair
> - Remove temp files with special characters
> - Add patterns to .gitignore to prevent future accidents
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[d50a48ca](https://github.com/freeplane/freeplane/commit/d50a48ca010a2d4711d6dc7a6295aae81fadc5da)** (2025-07-29) — Fix Unicode corruption in all translation files

> Systematic repair of Unicode corruption introduced in commit 28da344b74:
> - Remove null bytes that broke file structure
> - Fix broken Unicode escapes (u0159 → \u0159, u00E1 → \u00E1, etc.)
> - Fix double UTF-8 encoding (\u00C3\u00A1 → \u00E1)
> - All 38 translation files repaired and validated
> - No content deleted, only technical corruption fixed
> - Weblate corruption alerts eliminated
> 
> Also update CLAUDE.md with correct directory structure documentation
> to prevent future path confusion.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[28da344b](https://github.com/freeplane/freeplane/commit/28da344b747b3fa75405d61d2da7948caf1723a2)** (2025-07-28) — Add mouse-over preferences translations for all supported languages

> Add translations for 6 new mouse-over preference keys to 18 languages:
> - OptionPanel.mouse_over_folding_action
> - OptionPanel.mouse_over_folding_action.tooltip
> - OptionPanel.mouse_over_folding_timing
> - OptionPanel.mouse_over_folding_timing.tooltip
> - OptionPanel.mouse_over_selection_timing
> - OptionPanel.mouse_over_selection_timing.tooltip
> 
> All translations use proper Unicode escaping for non-ASCII characters and
> maintain consistency with existing UI terminology patterns.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[6dd1a024](https://github.com/freeplane/freeplane/commit/6dd1a0247e895633c388ff5f8ecea6173b9fccb9)** (2025-07-28) — Restructure mouse-over preferences and improve code quality

> - Split mouse_over_timing into separate selection and folding timing
> - Add mouse_over_folding_action for granular folding behavior control
> - Update preferences.xml with 4-control structure for clarity
> - Fix timer management bug: stop folding timer on manual fold/unfold actions
> - Add English translations for new preference keys
> - Maintain backward compatibility through property migration
> 
> Code quality improvements:
> - Reduce class visibility to package-private for internal UI components
> - Organize static elements at top: blocks, constants, inner classes
> - Optimize inner classes: static when no outer access needed
> - Document Java code quality standards in project CLAUDE.md
> 
> This resolves UI confusion where overlapping controls made behavior unclear
> and fixes the critical bug where delayed folding timers would interfere
> with manual folding actions.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[809a2b6d](https://github.com/freeplane/freeplane/commit/809a2b6d1bf4ef79b101b9c09f1f9b081b281b51)** (2025-07-28) — Change selection mouse over terminology from "enabled" to "immediate"

> Replace the confusing "enabled" terminology with clearer "immediate" for the
> selection_on_mouse_over preference. This better describes the behavior where
> selection happens immediately upon mouse over, distinct from "delayed" timing.
> 
> Changes:
> - Update preferences.xml to use "immediate" instead of "enabled" as choice value
> - Update NodeSelector.java constants and logic to use SELECTION_IMMEDIATE
> - Add backward compatibility for users with "enabled" in their settings
> - Add "immediate" translations to 16 language files that had "enabled" translations
> - Update selection_method migration to use "immediate" terminology
> 
> The new terminology makes the distinction clearer:
> - "immediate" = select immediately on mouse over
> - "delayed" = use mouse_over_delay setting
> - "disabled" = no mouse over selection
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[298663f1](https://github.com/freeplane/freeplane/commit/298663f1701e8c794f09edcc58e76d1f1762008a)** (2025-07-28) — Remove deprecated selection_method configuration system

> Remove the deprecated "selection_method" preference option which has been
> replaced by the new granular mouse over behavior settings. This removes:
> 
> - selection_method combo from preferences.xml
> - selection_method property from freeplane.properties
> - All translation keys for selection_method from 40+ language files
> 
> The new mouse over behavior system provides better granular control with
> separate settings for selection, folding, timing, and delay.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[60ef0b8d](https://github.com/freeplane/freeplane/commit/60ef0b8df9e232eb4c2337b3bd21fabbe2b3dd49)** (2025-07-28) — Fix mouse over selection timing bug

> When "Selection on mouse over" is set to "Enabled", selection now happens
> immediately instead of waiting for the mouse over delay. This resolves the
> bug where users expected immediate selection but had to wait 3000ms.
> 
> The fix bypasses the timer delegate when selection behavior is "enabled"
> and directly executes the selection action.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[eaa2fc0b](https://github.com/freeplane/freeplane/commit/eaa2fc0bf8343789c58d0040a467726daa9859d4)** (2025-07-28) — Fix additional encoding issue in Croatian translation

> Remove control character (null byte) and fix malformed Unicode encoding
> in OptionPanel.mouse_over_timing.tooltip where \u00C5\u00A1 and u0161 were
> corrupted. Now properly uses \u0161 for Croatian letter 'š'.
> 
> This completes the fix for all encoding issues in Resources_hr.properties
> related to mouse interaction strings.
> 
> Also checked other recently changed translation files (Russian, Spanish,
> French, Portuguese, German, Japanese, Ukrainian, Chinese) - no similar
> encoding issues found.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[3e139827](https://github.com/freeplane/freeplane/commit/3e1398271b2e31c65458d1d4e666147fcb6f2de4)** (2025-07-28) — Fix encoding issue in Croatian translation

> Remove control character (null byte) and fix malformed Unicode encoding
> in OptionPanel.mouse_over_delay.tooltip where \u00C5\u00A1 and u0161 were
> corrupted. Now properly uses \u0161 for Croatian letter 'š'.
> 
> Fixes: "String contains control character: 'Vreme kašnjenja pri prelasku mišem'"
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[fe679c9c](https://github.com/freeplane/freeplane/commit/fe679c9c1613867a09765554079c724441257b88)** (2025-07-28) — Add 71 missing translations to French (Resources_fr.properties)

> Added missing translations for:
> - Continuous node selection actions (up/down/left/right)
> - Navigation actions (next/previous map view)
> - Tag management functionality (categories, colors, uncategorized)
> - Mouse-over behavior settings and timing options
> - Bookmark functionality (toolbar actions, node operations, management)
> - Option panel settings and tooltips
> - Display configuration options
> - Code exploration features (dependency tracking with recursion options)
> - ArchUnit server configuration
> - Structured text handling
> 
> All translations use proper Unicode escape sequences for Java compatibility.
> Some existing translations were preserved when duplicates were detected during formatting.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[bc623588](https://github.com/freeplane/freeplane/commit/bc6235883a87090e8d2760ae620f72982a3c8f11)** (2025-07-28) — Add 22 missing translations to Croatian (Resources_hr.properties)

> Added missing translations for:
> - Mouse-over behavior settings and timing options
> - Option panel settings and tooltips
> - Node functionality (folding, selection, inline editor)
> - UI state controls (enabled/disabled, toggle)
> - Display options (preview, underline)
> 
> All translations use proper Unicode escape sequences for Java compatibility.
> Some existing translations were preserved when duplicates were detected during formatting.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[3a18523b](https://github.com/freeplane/freeplane/commit/3a18523b96ff574e187e11503814d1af48a6208c)** (2025-07-28) — Add 20 missing translations to Spanish (Resources_es.properties)

> Added missing translations for:
> - Mouse-over behavior settings and timing options
> - Option panel settings and tooltips
> - Node functionality (folding, selection, timing)
> - UI state controls (enabled/disabled, toggle)
> - Display options (preview, underline)
> 
> All translations use proper Unicode escape sequences for Java compatibility.
> One existing translation was preserved when duplicate was detected during formatting.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[dfc15921](https://github.com/freeplane/freeplane/commit/dfc159213663f66b4faa2d69716aefce38488711)** (2025-07-28) — Add 50 missing translations to Portuguese Brazilian (Resources_pt_BR.properties)

> Added missing translations for:
> - Continuous node selection actions (up/down/left/right)
> - Navigation actions (next/previous map view)
> - Mouse-over behavior settings and timing options
> - Bookmark functionality (toolbar actions, node operations, management)
> - Option panel settings and tooltips
> - Display configuration options
> - Node layout and folding controls
> 
> All translations use proper Unicode escape sequences for Java compatibility.
> Some existing translations were preserved when duplicates were detected during formatting.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[85aebcf7](https://github.com/freeplane/freeplane/commit/85aebcf725f840115af4bebff538003a93cdbedd)** (2025-07-28) — Add 47 missing translations to Chinese Simplified (Resources_zh_CN.properties)

> Added missing translations for:
> - Navigation actions (next/previous view)
> - Mouse-over behavior settings and timing options
> - Bookmark functionality (toolbar actions, node operations)
> - Option panel settings and tooltips
> - Code exploration menu keys (hierarchy, usages, implementations)
> - Display and UI configuration options
> 
> All translations use proper Unicode escape sequences for Java compatibility.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[1776e6df](https://github.com/freeplane/freeplane/commit/1776e6dff80b5268df7c2e8a95750c66fa9bf1f9)** (2025-07-28) — Add all 41 missing Japanese translations

> Complete Japanese translation file with comprehensive UI elements:
> 
> **Mouse-over Behavior (17 items):**
> - Core settings: delayed, disabled, enabled, immediate, toggle, unfold_only
> - Mouse behavior: folding_on_mouse_over, mouse_over_behavior, mouse_over_delay, mouse_over_timing
> - Selection: selection_on_mouse_over, preview, separator.mouse_over_behavior
> - Comprehensive tooltips explaining functionality
> 
> **Code Explorer Features (22 items):**
> - Class filtering: FilterClassesByDependencies, FilterClassesBySelectedDependencies
> - Cycle detection: FilterCyclesAction, SelectCyclesAction
> - Dependency directions: INCOMING, OUTGOING, INCOMING_AND_OUTGOING
> - Class hierarchy: superclass/subclass, interface relationships
> - Visibility states: VISIBLE, SELECTED, with parameterized messages
> - Action feedback: no_cycles_found, no_dependencies_found, n_hidden_dependencies_revealed
> 
> **Additional Options (2 items):**
> - automaticSideDistribution.tooltip - detailed node placement behavior
> - code_showOutsideDependencies - external dependency display
> 
> All translations use proper Unicode escape sequences for Japanese characters
> and follow established Japanese UI terminology patterns from the existing codebase.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[76f4c66d](https://github.com/freeplane/freeplane/commit/76f4c66d241a5fdf67f7fbe8c4dc011156616f81)** (2025-07-28) — Add all 40 missing Russian translations

> Complete Russian translation file with all missing UI elements:
> 
> **Navigation & Actions (4 items):**
> - BookmarkNodeAction, FocusBookmarkToolbarAction
> - NavigationMapNextViewAction, NavigationMapPreviousViewAction
> 
> **Option Panel Settings (17 items):**
> - Mouse-over behavior: delayed, disabled, enabled, immediate, toggle, unfold_only
> - folding_on_mouse_over, mouse_over_behavior, mouse_over_delay, mouse_over_timing
> - preview, selection_on_mouse_over, separator.mouse_over_behavior
> - display_scale, show_bookmark_icons, synchronizeSelectionOnlyOnBranchChange
> - nodefontunderline, display_inline_editor_for_all_new_nodes.tooltip
> 
> **Bookmark Functionality (10 items):**
> - Complete bookmark management including add, delete, rename, goto
> - Root branch operations and view controls
> - Node content and name synchronization
> 
> **Layout & Children (1 item):**
> - SelectNodeChildrenLayoutAction for child node layout selection
> 
> All translations use proper Unicode escape sequences and follow
> established Russian UI terminology patterns from the existing codebase.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[1646ca51](https://github.com/freeplane/freeplane/commit/1646ca512bd95f56dd3fa4d89673dd30d13da189)** (2025-07-28) — Add missing German translations for mouse-over behavior settings

> Added 13 missing OptionPanel translation keys related to mouse-over behavior:
> - delayed, disabled, enabled
> - folding_on_mouse_over, immediate, mouse_over_behavior
> - mouse_over_delay, mouse_over_timing
> - preview, selection_on_mouse_over
> - separator.mouse_over_behavior
> - toggle, unfold_only
> 
> All translations use proper Unicode escape sequences for German characters
> and follow established German UI terminology patterns in the codebase.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[60c0eed5](https://github.com/freeplane/freeplane/commit/60c0eed5cd71667e855af121e2e65cf90700b2fe)** (2025-07-28) — Add missing Ukrainian translations for mouse-over behavior settings

> Added 13 missing OptionPanel translation keys related to mouse-over behavior:
> - delayed, disabled, enabled
> - folding_on_mouse_over, immediate, mouse_over_behavior
> - mouse_over_delay, mouse_over_timing
> - preview, selection_on_mouse_over
> - separator.mouse_over_behavior
> - toggle, unfold_only
> 
> All translations use proper Unicode escape sequences and follow
> established Ukrainian UI terminology patterns from the existing file.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[1cee4e9a](https://github.com/freeplane/freeplane/commit/1cee4e9a62d0ef07ac7ac4ba15dad8f202189d98)** (2025-07-28) — Add missing Dutch translations for mouse-over behavior settings

> Added 13 missing OptionPanel translation keys related to mouse-over behavior:
> - delayed, disabled, enabled
> - folding_on_mouse_over, immediate, mouse_over_behavior
> - mouse_over_delay, mouse_over_timing
> - preview, selection_on_mouse_over
> - separator.mouse_over_behavior
> - toggle, unfold_only
> 
> All translations follow established Dutch UI terminology patterns
> and maintain concise clarity appropriate for interface elements.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[554d9c05](https://github.com/freeplane/freeplane/commit/554d9c05c731b2843fe53f26db1136b408247c6e)** (2025-07-28) — Add missing Portuguese (PT) translations for mouse-over behavior settings

> Added 16 missing OptionPanel translation keys related to mouse-over behavior:
> - delayed, disabled, enabled
> - folding_on_mouse_over and tooltip
> - immediate, mouse_over_behavior
> - mouse_over_delay and tooltip
> - mouse_over_timing and tooltip
> - preview, selection_on_mouse_over and tooltip
> - separator.mouse_over_behavior
> - toggle, unfold_only
> 
> All translations use proper Unicode escape sequences for Portuguese (Portugal)
> variant and follow existing terminology patterns in the codebase.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[6f11a181](https://github.com/freeplane/freeplane/commit/6f11a181ef50fef9fa382964f190bff02a9a6b81)** (2025-07-27) — Issue 2603: Restore wasFired protection for rapid folding prevention

> The wasFired field was critical for preventing rapid successive folding actions
> when hovering over folding controls. Without this protection, quick mouse
> movements could trigger multiple fold/unfold operations causing flickering.
> 
> Original 1.12.x logic: if(isInFoldingRegion && delayedSelection.wasFired) return;
> 
> Restored functionality:
> - Added wasFired field back to TimeDelayedFolding class
> - Track delayedFolding instance in NodeFolder
> - Check wasFired before creating new timers
> - Clear delayedFolding reference when timer stops
> - Set wasFired = true when folding action executes
> 
> This prevents rapid fold/unfold cycles while preserving the new architecture.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[cb8e2f77](https://github.com/freeplane/freeplane/commit/cb8e2f77bb7bd17c4e0e582d381bfbbb79dc3b21)** (2025-07-27) — Issue 2603: Refactor timing logic using composition over inheritance

> - Extract MouseTimerDelegate class to handle shared timing behavior
> - Replace inheritance with composition in NodeSelector and NodeFolder
> - Implement ActionProvider interface for delegation pattern
> - Remove code duplication: getControlRegion, timer management, timing constants
> - Clean up unused wasFired field from NodeSelector
> - Update CLAUDE.md with Freeplane logging system knowledge
> 
> ✅ Compilation successful
> ✅ All duplication removed between NodeFolder and NodeSelector
> ✅ Clean delegation pattern established
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[3ae994fd](https://github.com/freeplane/freeplane/commit/3ae994fd4007b05921a9e587f06dbd7257900089)** (2025-07-27) — Issue #2603: Complete preview mode fix and improve architecture

> - Fix preview mode to persist unfolding when user clicks on preview-unfolded node
> - Prevent toggle folding actions when clicking on preview-unfolded nodes
> - Clear preview state when user explicitly folds a node to prevent unwanted re-unfolding
> - Refactor previewUnfoldedNode from static to instance variable for better encapsulation
> - Make TimeDelayedFolding non-static inner class to access instance variables
> - Reorganize preferences.xml to group selection and folding behavior separately
> 
> Now preview mode works correctly:
> - Click on preview-unfolded node keeps it unfolded permanently
> - Explicitly folding a node prevents it from preview-unfolding again
> - Better separation of selection vs folding configuration
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[9f829fe5](https://github.com/freeplane/freeplane/commit/9f829fe5a8c1505a222acb3a3a1498f2c9d67af2)** (2025-07-27) — Issue #2603: Fix preview mode to persist unfolding after user clicks

> When using "preview" folding mode, nodes temporarily unfold on mouse-over.
> This fix ensures that clicking on a preview-unfolded node makes the unfolding
> permanent instead of toggling/folding the node.
> 
> Changes:
> - Add makePreviewUnfoldingPermanent() method to clear preview state
> - Add isPreviewUnfolded() method to check if node is in preview state
> - Prevent toggle folding action when clicking on preview-unfolded nodes
> - Call makePreviewUnfoldingPermanent() when user clicks to make unfolding permanent
> 
> Now clicking on a preview-unfolded node keeps it unfolded instead of folding it.
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[4e8be515](https://github.com/freeplane/freeplane/commit/4e8be515138787d2556657720e042baff6114f0d)** (2025-07-27) — Issue #2603: Fix translation keys for mouse over behavior preferences

> - Add missing OptionPanel.separator.mouse_over_behavior translation key
> - Update preference choice translations to use OptionPanel prefix:
>   - immediate → OptionPanel.immediate
>   - delayed → OptionPanel.delayed
>   - toggle → OptionPanel.toggle
>   - preview → OptionPanel.preview
>   - unfold_only → OptionPanel.unfold_only
> - Document translation key conventions in CLAUDE.md
> - Run format_translation to maintain alphabetical sorting
> 
> Crafted by [Claude Code](https://claude.ai/code) — the AI used with judgment.
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[663e1aff](https://github.com/freeplane/freeplane/commit/663e1affd8f7b21ee07e2930082f07804256bfc6)** (2025-07-27) — Issue #2603: Add independent folding behavior configuration

> Separates node folding behavior from selection behavior, allowing users
> independent control over mouse-over interactions. Adds new configuration
> options for folding method (disabled/toggle/unfold_only/preview) and
> shared mouse-over timing settings.
> 
> Key changes:
> - Added isPropertySetByUser() method to ResourceController classes
> - Created NodeFolder class with folding-specific logic extracted from NodeSelector
> - Updated NodeSelector to use new selection configuration
> - Added new preferences: mouse_over_timing, mouse_over_delay, selection_on_mouse_over, folding_on_mouse_over
> - Implemented property migration for backward compatibility
> - Added preview mode for temporary node unfolding
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[5d2843db](https://github.com/freeplane/freeplane/commit/5d2843db659f316c657eaea3527063701adeb2f3)** (2025-07-18) — Issue #2589 Fix URI space encoding issue throughout Freeplane

> - Replace direct URI creation with URIUtils.createURIFromString() in all user-facing code
> - Fix space handling in file paths and URLs across the application
> - Update MLinkController.setLink() to handle spaces in link strings
> - Update SetLinkByTextFieldAction to validate clipboard URIs with spaces
> - Update MMapClipboardController to handle links with spaces from clipboard
> - Update FileOpener to handle dropped files with spaces in names
> - Update OpenURLMapAction to handle URLs with spaces from user input
> - Add URIUtils import statements to all affected files
> 
> This comprehensive fix ensures that users can work with files and URLs containing spaces without encountering URI encoding errors. The solution maintains backward compatibility while providing robust space handling throughout the entire application.

**[142ae601](https://github.com/freeplane/freeplane/commit/142ae601ab4ac13ee6bb8dc1f269192840a25f13)** (2025-07-18) — Revert "Fix resolving URIs containing # character"

> This reverts commit fc70fb9d0e31cdae964c48f05c25a201dad49d07.

**[f6ade734](https://github.com/freeplane/freeplane/commit/f6ade7341671c1de72b5e25f3df836357028a140)** (2025-07-15) — Update Resources_en.properties

> Minor corrections for Preferences dialog text
> 
> Fixed spelling of "Scrollling" section in Behaviour tab - it had 3 L's instead of 2.
> 
> Fixed spelling/grammar for first Connectors option on Defaults tab. New description says "Assign node-dependent styles to new connectors".

**[6ade10e8](https://github.com/freeplane/freeplane/commit/6ade10e81a3900ecb3de7bac10652e88c8f12152)** (2025-07-13) — fix: disabling save_last_position_in_map has no effect

> rename save_last_visited_node (which is used in preferences / resources) to save_last_position_in_map (which is used in LastOpenedList.java)

**[76beccac](https://github.com/freeplane/freeplane/commit/76beccacbaadd1be846c960ff388008462e22151)** (2025-07-11) — Step 3: Extract VisibleOutlineState class

> - Create VisibleOutlineState to centralize visible node state management
> - Move visibleNodes, blockPanels, breadcrumbAreaHeight, and hoveredNode to VisibleOutlineState
> - Add helper methods like isNodeInBreadcrumbArea, getFlatNode, getMaxDepth
> - Update ScrollableTreePanel to use VisibleOutlineState instead of direct state management
> - Update BreadcrumbPanel and BlockPanel to use VisibleOutlineState methods
> - Update NavigationButtons to use VisibleOutlineState methods
> - All compilation successful, ready for next step

**[08d4b701](https://github.com/freeplane/freeplane/commit/08d4b7010143b45b049aa56b6a73736c3f8aeec8)** (2025-07-11) — Step 2: Extract OutlineSelection class

> - Create OutlineSelection class to replace TreeSelection with cleaner API
> - Add selectNode(TreeNode) overload for convenience
> - Update ScrollableTreePanel, BreadcrumbPanel, and BlockPanel to use OutlineSelection
> - Delete old TreeSelection.java file
> - All compilation successful, ready for next step

**[97b1ba55](https://github.com/freeplane/freeplane/commit/97b1ba55d16abcf188af92f4588caece502db6fa)** (2025-07-11) — Step 1: Extract OutlineGeometry class

> - Create OutlineGeometry class with all geometric calculations
> - Update NavigationButtons to use OutlineGeometry instead of duplicate calculations
> - Update ScrollableTreePanel, BreadcrumbPanel, and BlockPanel to use geometry object
> - All compilation successful, ready for next step

**[3e22cfee](https://github.com/freeplane/freeplane/commit/3e22cfeed5ec194e876f1c0cc6cf825c03fe80a8)** (2025-07-06) — add tooltip for display_inline_editor_for_all_new_nodes

> to give more information about the functionality toggled by the setting, as discussed in #2563

**[1dbcfd06](https://github.com/freeplane/freeplane/commit/1dbcfd0650742e17c828bf0c6d590334f57c7496)** (2025-06-30) — Issue #2526 add synchronizeSelectionOnlyOnBranchChange option

> - Introduce new boolean option `synchronizeSelectionOnlyOnBranchChange`
> - Expose under Preferences…->Behaviour->Selection->Sync only on branch change
> - Tooltip: “Only synchronize selection when switching between branches.”
> - When enabled, ignore drill-down/up within the same branch and re-sync only on branch switches
> - Default behavior changes to full-depth synchronization

**[e38ad4d7](https://github.com/freeplane/freeplane/commit/e38ad4d7e62d6767fc329b00df4b33548ee226d5)** (2025-06-29) — fix NPE on open asRoot when lastSelectedNode is newly created

> NullPointerException: Cannot invoke "String.equals(Object)" because "selectedNodeId" is null

**[d87b619f](https://github.com/freeplane/freeplane/commit/d87b619fc549d52f64d89ba2b1a38a0282d18b2d)** (2025-06-25) — fix for scripting: setBookmark fails silently on newly created nodes

> e.g. node.createChild('B').setBookmark('B', 'ROOT')

**[de8f8af7](https://github.com/freeplane/freeplane/commit/de8f8af7ac1c265605439790a5fecd6877f52726)** (2025-06-15) — Add BookmarkNodeAction and integrate into bookmarks functionality

> - Added BookmarkNodeAction class to enable bookmarking of nodes.
> - Updated BookmarksController to register the new action.
> - Modified mindmapmodemenu.xml to include BookmarkNodeAction in the menu.
> - Added necessary translations for bookmark-related UI elements.

**[a8c33b98](https://github.com/freeplane/freeplane/commit/a8c33b989165cb0d05510fb2c703b89f24115b1b)** (2025-06-15) — Add bookmarks feature with toolbar integration

> - Introduced BookmarksBuilder, BookmarksController, and MapBookmarks classes to manage bookmarks functionality.
> - Implemented BookmarkNodeAction for adding bookmarks to nodes.
> - Added ToggleBookmarksToolbarAction to toggle the visibility of the bookmarks toolbar.
> - Updated UI components to integrate bookmarks toolbar and ensure proper display.
> - Enhanced MapViewPane to support bookmarks management and display.
> - Added tests for bookmarks functionality to ensure reliability and correctness.

**[05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3)** (2025-05-24) — Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy scripts

> - Implement org.freeplane.api.swing.JFileChooser that wraps setUI() in doPrivileged()
> - Resolves AccessControlException when FlatLaf tries to use reflection in restricted environments
> - Export new package in OSGi system packages for script accessibility
> - Include JFileChooser in API generator documentation
> 
> Fixes FlatLaf styling errors in Groovy scripts that use file choosers.

**[df8f8315](https://github.com/freeplane/freeplane/commit/df8f83158802aa80ff10f529c2c6bba8cd17f634)** (2025-05-22) — fix exceptions for non local transfers:

> Drop exception:
> java.awt.dnd.InvalidDnDOperationException: No drop current
> 	at java.desktop/sun.awt.dnd.SunDropTargetContextPeer.getTransferData(Unknown Source)
> 	at java.desktop/sun.awt.datatransfer.TransferableProxy.getTransferData(Unknown Source)
> 	at java.desktop/java.awt.dnd.DropTargetContext$TransferableProxy.getTransferData(Unknown Source)
> 	at org.freeplane.view.swing.ui.mindmapmode.MNodeDropListener.getDropAction(MNodeDropListener.java:396)
> 	at org.freeplane.view.swing.ui.mindmapmode.MNodeDropListener.drop(MNodeDropListener.java:290)

**[a1001046](https://github.com/freeplane/freeplane/commit/a1001046c0d17a83511c3cfdf6e6e80bdc288b4e)** (2025-04-28) — Refactor VerticalNodeViewLayoutStrategy

> Simplified updateSummaryGroupBounds method and added new helper methods for better readability and maintainability. Adjusted calculations for child positioning and alignment in auto-compact layouts.

**[7e9d7ccf](https://github.com/freeplane/freeplane/commit/7e9d7ccf5ab1b6ab1e7d930a78d3ad4714b0378a)** (2025-04-22) — Enhance CombinedFunction to support FALLBACK operation and improve evaluation logic

> Updated the CombinedFunction class to include a new CombineOperation called FALLBACK, allowing for fallback evaluations when the primary function is undefined. Adjusted the evaluate method to handle cases where the input falls outside the defined ranges, and added unit tests to validate the new behavior, ensuring correct evaluations in various scenarios including gaps between segments.

**[dbc258aa](https://github.com/freeplane/freeplane/commit/dbc258aafc17040c3597c4b94e6911825d6cbf18)** (2025-04-21) — Implement nested translation flattening in StepFunction and add corresponding unit tests

> Enhanced the TranslatedFunction class to flatten nested translations by delegating to the inner StepFunction. Added unit tests to verify the behavior of flattened nested translations in both evaluation and sample points, ensuring correct calculations for translated segments.

**[b5887977](https://github.com/freeplane/freeplane/commit/b5887977e9b17100dda5aaf761e777f0d57d3e8f)** (2025-04-21) — Enhance CombinedFunction to handle gaps between segments and improve constructor argument handling

> Updated the CombinedFunction constructor to sort input segments based on their minX values. Added logic to evaluate gaps between segments, ensuring correct behavior for both MAX and MIN operations. Introduced new unit tests to validate gap handling and constructor argument swapping for combined functions.

**[79bb4fe4](https://github.com/freeplane/freeplane/commit/79bb4fe4d2745c017386fd601d346937143c4941)** (2025-04-20) — Refactor StepFunction interface and implementations to unify samplePoints method and adjust segment boundaries

> Updated the StepFunction interface to change the samplePoints method to return all sample points without min/max parameters. Adjusted segment boundaries in the evaluate method to include the right edge. Enhanced the CombinedFunction to cache computed sample points for efficiency. Added unit tests to validate new samplePoints behavior and ensure correct evaluation at segment boundaries.

**[f6708d8f](https://github.com/freeplane/freeplane/commit/f6708d8f4a2a26b616a51df386e3bd8225a97d9f)** (2025-04-18) — Add StepFunction class and corresponding tests

> Introduced the StepFunction class to represent a step function with methods for evaluation, combination, and translation. Added comprehensive unit tests to validate the functionality, including constructor validation, evaluation, combination of functions, distance calculation, and translation methods.

**[3ce589c4](https://github.com/freeplane/freeplane/commit/3ce589c454857cf5491892b43f6097d1b3c5b591)** (2025-04-18) — fix NPE

> java.lang.NullPointerException: Cannot invoke "org.freeplane.view.swing.map.NodeView.layoutOrientation()" because "parentView" is null
> 	at org.freeplane.view.swing.map.NodeView.getNextVisibleSibling(NodeView.java:580)
> 	at org.freeplane.view.swing.map.MapView.getNextVisibleSiblingAtAnyLevel(MapView.java:2121)
> 	at org.freeplane.view.swing.map.MapView.getNextVisibleSibling(MapView.java:1980)
> 	at org.freeplane.view.swing.map.MapView.suggestNewSelectedSibling(MapView.java:1973)
> 	at org.freeplane.view.swing.map.MapView.selectPreferredVisibleAncestorSibling(MapView.java:1928)
> 	at org.freeplane.view.swing.map.MapView.selectRelatedNode(MapView.java:1745)
> 	at org.freeplane.view.swing.map.MapView.selectRight(MapView.java:1735)

**[175ecee5](https://github.com/freeplane/freeplane/commit/175ecee54f61d0229817d58dcddcd58040eab1be)** (2025-01-06) — Issue #2199 "OS-Command links with spaces are misinterpreted on Linux"

> fix execution of execute-links with spaces on Linux;
> show error in status line


---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-12-30 | `fix` | Fix tooltip provider for styles | `LogicalStyleController.java` | [811bb14b](https://github.com/freeplane/freeplane/commit/811bb14beb8db576fefe8e914d66d933c23ad898) |
| 2024-12-30 | `fix` | fix spelling | `LogicalStyleController.java` | [d144948f](https://github.com/freeplane/freeplane/commit/d144948fa23f5d6c4b57f70c4c479e4d82230b58) |
| 2024-12-29 | `feature` | Issue #2171 Add nodes inside selection rectangle to selection if shift is pressed | `MapView.java`, `DefaultMapMouseListener.java` +1 | [a558d637](https://github.com/freeplane/freeplane/commit/a558d63720e38336ea50e36204f3c9a8cc58cae6) |
| 2024-12-27 | `fix` | fix show icon property value taken from user properties | `MapStyle.java` | [d2130e7d](https://github.com/freeplane/freeplane/commit/d2130e7d435d54cc88912834e2544efa53f9f696) |
| 2024-12-26 | `fix` | fix tag rendering for zoomed maps | `IconListComponent.java` | [5332933b](https://github.com/freeplane/freeplane/commit/5332933bd590d273051f4d8d2e27a4c77951cceb) |
| 2024-12-22 | `feature` | Add "Close map" action to tab popup menu | `MapViewDockingWindows.java`, `Resources_en.properties` | [52349d1c](https://github.com/freeplane/freeplane/commit/52349d1c795a438bb72d90a3b783f18f48dc838c) |
| 2024-11-23 | `feature` | fix adding new elements | `FilterController.java` | [ce65eb26](https://github.com/freeplane/freeplane/commit/ce65eb2605e011cd913f611e0fbafcd14f9f45b4) |
| 2024-11-23 | `fix` | Fix accessibility objects | `IconListComponent.java`, `FilterController.java` +3 | [b388f317](https://github.com/freeplane/freeplane/commit/b388f317c3bf2e07738d949efdb20f13e63b55e5) |
| 2024-11-19 | `feature` | Issue #2115: not possible to insert text in new nodes | `EventBuffer.java` | [4ea4ca71](https://github.com/freeplane/freeplane/commit/4ea4ca7152ed5fd663aba9d7822543e25f01eb2b) |
| 2024-11-16 | `fix` | fix NPE | `TextIcon.java` | [d1a25997](https://github.com/freeplane/freeplane/commit/d1a259979584f2f8b40ae1179e55e2c168334245) |
| 2024-11-12 | `feature` | Add "no ancestors", "no sescendants" and "no child" conditions | `DecoratedConditionFactory.java`, `NoAncestorConditionDecorator.java` +3 | [2810e22e](https://github.com/freeplane/freeplane/commit/2810e22e5f16de73bc6e10e6d2baf8ac031bba99) |
| 2024-11-02 | `fix` | fix NPE | `MTextController.java` | [c3b98f31](https://github.com/freeplane/freeplane/commit/c3b98f31cf271c349082b7c3f1cd29d9638efa3e) |
| 2024-11-02 | `fix` | fix NPE | `TextUtils.java` | [10ed1858](https://github.com/freeplane/freeplane/commit/10ed185862f438569e64b12367b480c5ef4b22d6) |
| 2024-11-02 | `feature` | Issue #2088 Support more date and number formats in formulas | `FormatController.java`, `PatternFormat.java` | [64cc2a0f](https://github.com/freeplane/freeplane/commit/64cc2a0fe343b2abda503c1861cdafa14e15fa24) |
| 2024-10-20 | `feature` | Issue #2054 Add to find dialog an option to search in subtree | `history_en.txt`, `FindAction.java` +1 | [2e85020c](https://github.com/freeplane/freeplane/commit/2e85020c38a05df5ee70db8de9b4d16e15b38556) |
| 2024-10-06 | `feature` | Issue #2038 New node editor interferes with command "Add hyperlink (file)" | `MTextController.java` | [83ed6009](https://github.com/freeplane/freeplane/commit/83ed6009f0b7ae245c9c8f36224374c61d8ffe7c) |
| 2024-10-05 | `fix` | bug fixes | `IconListComponent.java`, `FilterController.java` +3 | [4f66134c](https://github.com/freeplane/freeplane/commit/4f66134c92e10610c8d8508d60b741d9e5e0011a) |
| 2024-10-04 | `feature` | Implement fast way to remove filter conditions | `IconListComponent.java`, `IconRow.java` +9 | [7f2a0b7e](https://github.com/freeplane/freeplane/commit/7f2a0b7ec8c2d8f95e34a4a31f3db499197e230b) |
| 2024-10-04 | `fix` | fix filter condition box and tooltip | `IconListComponent.java`, `FilterController.java` +2 | [d66a55d1](https://github.com/freeplane/freeplane/commit/d66a55d1f5481ea5bd20f50ef70a3a471357bfec) |
| 2024-10-03 | `feature` | add quick filter conditions to the filter condition list | `FilterController.java` | [86dbd4de](https://github.com/freeplane/freeplane/commit/86dbd4dee67a8fdfff0a8d1a54a0672edf8cc8aa) |
| 2024-10-03 | `fix` | Fix rendered icon | `IconContainedCondition.java` | [6497067b](https://github.com/freeplane/freeplane/commit/6497067b546e8da51ef68374758c87253ac4d261) |
| 2024-09-29 | `fix` | fix condition descriptions and show them as tooltips | `ASelectableCondition.java`, `CombinedConditions.java` +5 | [fc80a37c](https://github.com/freeplane/freeplane/commit/fc80a37cdd645f32b596f6ef5234f9f38b6dd007) |
| 2024-09-28 | `feature` | move class GraphicHints to new package | `build.gradle`, `GraphicsHints.java` +3 | [15149ebd](https://github.com/freeplane/freeplane/commit/15149ebdc5186b30f0475c9ddd063604b8648336) |
| 2024-09-27 | `feature` | implement TextIcon | `TextIcon.java` | [584a22de](https://github.com/freeplane/freeplane/commit/584a22de6e1ae2e07d23edb2a6b9e026aa20adc8) |
| 2024-09-13 | `feature` | Add test helper | `TagCategories.java`, `TagAssertions.java` +1 | [431e7b8b](https://github.com/freeplane/freeplane/commit/431e7b8b2b48208c8638f07cfcece8ff14a8aa1c) |
| 2024-09-12 | `fix` | Fix endless recursion | `TagCategories.java`, `TagCategoryEditor.java` | [4da7ec4f](https://github.com/freeplane/freeplane/commit/4da7ec4f0af70a3549a28e2972a034b3349b0bee) |
| 2024-09-12 | `fix` | fix: setColor not needed here | `TagCategories.java` | [e65b0e82](https://github.com/freeplane/freeplane/commit/e65b0e82eb143914fc8f44401e795d61ef6597e3) |
| 2024-09-12 | `feature` | Add test to check the color of the renamed tag node | `TagCategoryEditorTest.java` | [d0e1954b](https://github.com/freeplane/freeplane/commit/d0e1954bee4eb5441c007e1a7f0bfc23961122b0) |
| 2024-09-12 | `fix` | Fix renaming uncategorized tags | `TagCategories.java` | [b0bb9294](https://github.com/freeplane/freeplane/commit/b0bb929492846f0effd482fb0c985266a577a6ec) |
| 2024-09-12 | `feature` | Add test for renaming categorized tag | `TagCategories.java`, `TagCategoryEditorTest.java` | [a8c4c84d](https://github.com/freeplane/freeplane/commit/a8c4c84d2ec02044bfe3c9fe92db701898d2ff02) |
| 2024-09-12 | `fix` | Issue #2033 Correct color is not assigned after merging tags | `TagCategoryEditor.java` | [25afb2a8](https://github.com/freeplane/freeplane/commit/25afb2a85629ef82f94353fa76c42bb9e8365701) |
| 2024-09-11 | `feature` | Issue #2030 FP 1.12.6_03: not possible to create new tags in the tag category editor TCE | `TagCategories.java` | [368d960b](https://github.com/freeplane/freeplane/commit/368d960bb5a1ce1cdc59c3b2480c5fbb9e5676f5) |
| 2024-09-11 | `feature` | implement Icon IconListComponent.getIcon(Point) | `IconListComponent.java` | [a59e05ab](https://github.com/freeplane/freeplane/commit/a59e05abb744ba58a6b879706cab24a6bd6252b7) |
| 2024-09-06 | `feature` | Add test for color change | `TagCategories.java`, `TagCategoryEditor.java` +1 | [147adc67](https://github.com/freeplane/freeplane/commit/147adc6715be2f2bde213a6f92a5e46e5dba4277) |
| 2024-09-06 | `feature` | add TagCategoryEditorTest | `TagCategoryEditor.java`, `TagCategoriesTest.java` +1 | [77bfa284](https://github.com/freeplane/freeplane/commit/77bfa284e31b78b26e50d89a09b91735492c429d) |
| 2024-09-06 | `fix` | fix test | `TagCategoriesTest.java` | [26bbf629](https://github.com/freeplane/freeplane/commit/26bbf6298060b8df7aa440144eb1f4b325657928) |
| 2024-09-05 | `fix` | Fix removing tags and editing uncategorized tags | `TagCategories.java`, `TagCategoryEditor.java` | [273b7436](https://github.com/freeplane/freeplane/commit/273b7436e6fc8dab1536af30672c22fd70e2b5fb) |
| 2024-09-05 | `fix` | fix changing tag colors | `Tag.java`, `TagCategories.java` +4 | [6f0703ca](https://github.com/freeplane/freeplane/commit/6f0703cae67f712ab0a9b91cfe4efc7ee0abb113) |
| 2024-08-31 | `fix` | Fix painting combobox button as table editor component on macos laf | `TypedListCellRenderer.java`, `TagEditor.java` +1 | [98999625](https://github.com/freeplane/freeplane/commit/98999625a4581a80906301dd56d1159f96521721) |
| 2024-08-31 | `fix` | Fix class cast exception for com.apple.laf.AquaComboBoxButton | `TagEditor.java` | [79eac0c6](https://github.com/freeplane/freeplane/commit/79eac0c64b2a1db94686d7ca05374fc98624e68f) |
| 2024-08-31 | `fix` | fix endless loop | `TagCategories.java` | [cf9ab22f](https://github.com/freeplane/freeplane/commit/cf9ab22fbb98153e0e9a274d0212c41d0ecf4767) |
| 2024-08-31 | `feature` | Add no siblings below uncategorized node | `TagCategoryEditor.java` | [02b340b1](https://github.com/freeplane/freeplane/commit/02b340b157a5d1d3a8fcc4180610c24bc1a43e8e) |
| 2024-08-31 | `fix` | Fix NPE | `TagCategoryEditor.java` | [d79b6794](https://github.com/freeplane/freeplane/commit/d79b6794281ed389ed6b8cd68e8d10cd3261a420) |
| 2024-08-30 | `fix` | fix compile error | `TagCategories.java` | [859b35f2](https://github.com/freeplane/freeplane/commit/859b35f24b4f0ade6fc0d51c9280007d3d3c1c7e) |
| 2024-08-25 | `fix` | Fix removing tags and tag categories | `TagCategories.java`, `TagCategoryEditor.java` | [517f23fe](https://github.com/freeplane/freeplane/commit/517f23fe442c012a9def681daef0a3533d016fc6) |
| 2024-08-25 | `fix` | Fix renaming and merging tags | `Tags.java`, `TagCategoryEditor.java` | [735a9577](https://github.com/freeplane/freeplane/commit/735a9577286de1e4a4471468d063f68d1a8dc82f) |
| 2024-08-24 | `fix` | fix moving tags to uncategorized | `TagCategories.java` | [ad7eea1b](https://github.com/freeplane/freeplane/commit/ad7eea1b7e99ddfa970eb93782ae51b6171fad5d) |
| 2024-08-24 | `fix` | fix test | `TagCategoriesTest.java` | [4fae51ba](https://github.com/freeplane/freeplane/commit/4fae51baa9b056bb270a6e54ec2f7b1f4c452f40) |
| 2024-08-24 | `feature` | Rework tag categories, add option to show tag categories | `mindmapmodemenu.xml`, `JFilterableComboBox.java` +20 | [ccea2b9d](https://github.com/freeplane/freeplane/commit/ccea2b9dcc98113f3707c893144e7f9fef7f6a92) |
| 2024-08-17 | `fix` | Fix moving tags in Tag Category Editor | `TagCategoryEditor.java` | [9b31cfed](https://github.com/freeplane/freeplane/commit/9b31cfede84bd0c7d6275c3e025aa8c185947f0b) |
| 2024-08-16 | `fix` | Fix category merge | `TagCategoryEditor.java` | [2c556941](https://github.com/freeplane/freeplane/commit/2c55694155a0692f77e3059bbdd266b05771a1d0) |
| 2024-08-16 | `fix` | Fix moving tags to uncategorized | `TagCategoryEditor.java` | [a268bee4](https://github.com/freeplane/freeplane/commit/a268bee4b91c1613b280dc47824d2525651b490e) |
| 2024-08-16 | `fix` | Bug fix: tags were deleted twice | `TagCategoryEditor.java` | [87e2ba3c](https://github.com/freeplane/freeplane/commit/87e2ba3ca5703e13c4111ac0e56e30a229232324) |
| 2024-08-14 | `fix` | Fix java.lang.ArrayIndexOutOfBoundsException: | `NodeList.java` | [6fdc8e4f](https://github.com/freeplane/freeplane/commit/6fdc8e4fd70988479fdff72770831c5e09bf48a8) |
| 2024-08-14 | `fix` | Fix java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0 | `NodeViewLayoutHelper.java`, `VerticalNodeViewLayoutStrategy.java` | [acd58076](https://github.com/freeplane/freeplane/commit/acd58076fcee0a4b1dd961cd54f8e25ad76d7f7e) |
| 2024-08-14 | `fix` | Use correct mapController instance | `MFileManager.java`, `HeadlessMModeControllerFactory.java` +2 | [43d90cab](https://github.com/freeplane/freeplane/commit/43d90cab6f954fb232f24c789f212c14848e13f6) |
| 2024-08-14 | `fix` | Simplify and fix ClassCastException | `NoteDialogStarter.java`, `EditNodeBase.java` +8 | [4a01a75a](https://github.com/freeplane/freeplane/commit/4a01a75a2e75b4ca44f1efbad0a5c90264ac8de1) |
| 2024-08-14 | `fix` | Use correct mode controller instance | `EditNodeTextField.java` | [ee8c1a13](https://github.com/freeplane/freeplane/commit/ee8c1a1357e23eb3fb15bbf09b67e098697d5c33) |
| 2024-08-14 | `fix` | fix class cast exception | `CommandSearchDialog.java` | [6cb403c7](https://github.com/freeplane/freeplane/commit/6cb403c7c9e4ac97914e92e04ead972a9fb08cf1) |
| 2024-08-11 | `feature` | Add unicode right to left characters to short text | `TextController.java` | [327fccf7](https://github.com/freeplane/freeplane/commit/327fccf758988f74ecae4a3df72ad8d33e9d810b) |
| 2024-08-11 | `fix` | fix popup menu text | `EditNodeBase.java` | [9a4e0edf](https://github.com/freeplane/freeplane/commit/9a4e0edf10d5f421db907d0be6bb69b2c2ca9a65) |
| 2024-08-10 | `fix` | Issue #1958 Fix editor component orientation | `EditNodeTextField.java` | [477301e5](https://github.com/freeplane/freeplane/commit/477301e533599e0ff4d84ad21961865f78e4df6b) |
| 2024-08-10 | `fix` | Revert "The character was visible in arial, fix it." | `ZoomableLabel.java` | [86fffd0e](https://github.com/freeplane/freeplane/commit/86fffd0ef32ebe8ffe0a8c0166475fea5360e20c) |
| 2024-08-10 | `fix` | fix layout | `VariableInsetsPainter.java` | [88412bd9](https://github.com/freeplane/freeplane/commit/88412bd9c702f888e9eb38abbc033eedd2486a74) |
| 2024-08-09 | `fix` | The character was visible in arial, fix it. | `ZoomableLabel.java` | [ec8f4870](https://github.com/freeplane/freeplane/commit/ec8f4870e4cd443510ac4719fce947783ff93ce2) |
| 2024-08-02 | `feature` | Issue #1077 Support transparent backgrounds for printing and exports | `MapStyle.java`, `MapView.java` +3 | [61845e20](https://github.com/freeplane/freeplane/commit/61845e206840000cc7e1b0345d8ce5bc5a19cee8) |
| 2024-07-30 | `fix` | Fix auto-expand selected nodes | `MapView.java` | [1245d0e6](https://github.com/freeplane/freeplane/commit/1245d0e64df433747531ff2520a2759620e2e544) |
| 2024-07-28 | `fix` | fix division by zero | `MapScroller.java` | [948eb6d2](https://github.com/freeplane/freeplane/commit/948eb6d2988158fad66c8899982c4da1c8268957) |
| 2024-07-27 | `fix` | fix input field borders | `TagCategoryEditor.java` | [5c9d4ab7](https://github.com/freeplane/freeplane/commit/5c9d4ab7d498f80e02f595aa26a39a8cdc9804e2) |
| 2024-07-27 | `feature` | support copy action in tag category editor drag and drop | `TagCategoryEditor.java` | [87d9c93d](https://github.com/freeplane/freeplane/commit/87d9c93d87292fef8e46f553b7c43e9298a1ddc7) |
| 2024-07-27 | `fix` | bug fix: remove renamed tags from the map | `TagCategories.java`, `TagCategoryEditor.java` | [92cfa433](https://github.com/freeplane/freeplane/commit/92cfa4334e31df5a6b0015dca136ae18b0d50d2d) |
| 2024-07-12 | `fix` | Fix merging of same tags | `TagCategories.java`, `TagCategoryEditor.java` | [4a92738e](https://github.com/freeplane/freeplane/commit/4a92738ec1f34cab61903dd691fdbe952415ddcc) |
| 2024-07-07 | `feature` | do not create new nodes under uncategorized nodes | `TagCategoryEditor.java` | [8a4f2cd2](https://github.com/freeplane/freeplane/commit/8a4f2cd2b317bf9ce5749d2c994077ce1fe83a55) |
| 2024-06-30 | `feature` | add new tags above uncategorized tags | `TagCategories.java` | [5d3ed505](https://github.com/freeplane/freeplane/commit/5d3ed5050eec9092f0aca56cd1f19c551eb53e07) |
| 2024-06-30 | `fix` | Issue #1898 Fix copy/paste tags on Windows | `TagEditor.java` | [27284ec4](https://github.com/freeplane/freeplane/commit/27284ec4d20a183524373a5a1c2e89d7b199da12) |
| 2024-06-29 | `fix` | fix NPE | `TagCategories.java` | [93d8ef67](https://github.com/freeplane/freeplane/commit/93d8ef67cfdf6ea731cc33882896be071f2c3f02) |
| 2024-06-28 | `fix` | fix tag editor actions executed by menu click | `TagEditor.java` | [9d234ad1](https://github.com/freeplane/freeplane/commit/9d234ad185ff3051a37e4ef0e0972c538f11a42e) |
| 2024-06-28 | `fix` | try to fix scroll on unfold | `MapView.java` | [38b05300](https://github.com/freeplane/freeplane/commit/38b053009620e73785a8dd381dc2e5dfde823b6f) |
| 2024-06-23 | `fix` | fix failing test | `TagCategories.java` | [0ca706ee](https://github.com/freeplane/freeplane/commit/0ca706eedb490f99139bdbe1afce767874d6d221) |
| 2024-06-23 | `feature` | Create tag references for qualified category tags | `TagCategories.java` | [61126b25](https://github.com/freeplane/freeplane/commit/61126b2596c90aa21e119f393e27a8116eda705c) |
| 2024-06-22 | `fix` | Fix: show node tree should consider map overview | `MapScroller.java` | [58c55673](https://github.com/freeplane/freeplane/commit/58c55673573d0f475ef2eee168410caba8b0c407) |
| 2024-06-21 | `fix` | fix formula result refresh for nodes accessing clones | `AccessedNodes.java`, `MultipleNodeList.java` +5 | [66effa94](https://github.com/freeplane/freeplane/commit/66effa9440f7d0f5e1666d5b94c48bf45be0232f) |
| 2024-06-17 | `fix` | fix renaming leaf tags | `TagCategories.java` | [721ff53c](https://github.com/freeplane/freeplane/commit/721ff53c0f74a1983f68d0747f0263b6297c58a4) |
| 2024-06-16 | `fix` | fix to no longer indicate childless clone-tree-root nodes as single-clone nodes | `MainViewPainter.java` | [979371c6](https://github.com/freeplane/freeplane/commit/979371c6cb2dbaf400a6587a46b357509d1259ec) |
| 2024-06-16 | `fix` | bug fixes | `TagCategories.java`, `TagCategoryEditor.java` | [84e31f52](https://github.com/freeplane/freeplane/commit/84e31f52ce1c710d95c50369ddb09223afa73a2e) |
| 2024-06-16 | `fix` | fix insertSelectedTagsIntoSelectedNodes | `TagCategoryEditor.java` | [a8c8db88](https://github.com/freeplane/freeplane/commit/a8c8db88933c158021f949477bc86a0ef85b524e) |
| 2024-06-15 | `fix` | fix test on Windows | `TagCategoriesTest.java` | [955582bc](https://github.com/freeplane/freeplane/commit/955582bc5ceeb674e1b562a33cac2308ea47e95e) |
| 2024-06-15 | `fix` | fix NPE | `MapStyle.java` | [0e367cc6](https://github.com/freeplane/freeplane/commit/0e367cc68749498c771246baa10077007aa6b11f) |
| 2024-06-14 | `fix` | fix intermediate node tag color | `TagCategories.java` | [8595c1f8](https://github.com/freeplane/freeplane/commit/8595c1f8e04fd13cf28d49f875b55bf876608d24) |
| 2024-06-14 | `feature` | add convenience method shortTag | `Tag.java` | [f982b5d0](https://github.com/freeplane/freeplane/commit/f982b5d02710a1838150ceee30a9154334118813) |
| 2024-05-30 | `fix` | fix text property name | `TagEditor.java` | [636e21d3](https://github.com/freeplane/freeplane/commit/636e21d3b70b9ea6801b03f77c57a9756c070492) |
| 2024-05-26 | `feature` | add option to prefer node-border color for state-symbol background | `Resources_pl.properties`, `preferences.xml` +3 | [9e7613ba](https://github.com/freeplane/freeplane/commit/9e7613ba63618ae1b5f94d25af71312f64ed5052) |
| 2024-05-26 | `feature` | fix state symbol to no longer be invisible when node border and background are invisible | `Resources_pl.properties`, `FoldingMark.java` +1 | [e7a72cfa](https://github.com/freeplane/freeplane/commit/e7a72cfa141d769a69a17166bd8c79bc7a200dbe) |
| 2024-05-25 | `feature` | Issue #1649 Option to turn off automatic left/right distribution of new nodes | `Resources_pl.properties`, `preferences.xml` +3 | [094ca3b4](https://github.com/freeplane/freeplane/commit/094ca3b471f35c890305be4f8f2a25f773e6f7a7) |
| 2024-05-19 | `fix` | Fix IconListComponent preferred width calculation | `IconListComponent.java` | [b7c7cbfe](https://github.com/freeplane/freeplane/commit/b7c7cbfe26878d01fc8e9add45d0e4579dc4956f) |
| 2024-05-19 | `fix` | Fix icon and tag position check on zoomed maps | `MainView.java` | [dfc5303b](https://github.com/freeplane/freeplane/commit/dfc5303bac37b40a10f9706d76872d7992873897) |
| 2024-05-19 | `feature` | Add ad-hoc category tags to categorized tags list | `TagCategories.java`, `TagEditor.java` | [77253a88](https://github.com/freeplane/freeplane/commit/77253a883cf5cc6744eee146e23bfb5a325d7d54) |
| 2024-05-18 | `fix` | fix code explorer node popup menu | `codeexplorermodemenu.xml` | [2b0591ab](https://github.com/freeplane/freeplane/commit/2b0591ab1fd5690a3d7fe9cb5837adfaece2d6d8) |
| 2024-05-18 | `feature` | Add mouse listeners to start tag editing on double click | `MultipleImageIcon.java`, `TagIcon.java` +3 | [dcb052f3](https://github.com/freeplane/freeplane/commit/dcb052f3efb7239f078a34545d68ba3760da32ac) |
| 2024-05-18 | `feature` | Add option to show tags under nodes | `mindmapmodemenu.xml`, `ActionFinder.java` +10 | [49b64e59](https://github.com/freeplane/freeplane/commit/49b64e5916da97a007f5545123a28da11937c7ba) |
| 2024-05-18 | `fix` | fix drag and drop of categorized tags | `TagCategories.java`, `TagEditor.java` +1 | [1b1721ae](https://github.com/freeplane/freeplane/commit/1b1721aecf2d2337fef72864a33f73539ecb1482) |
| 2024-05-17 | `feature` | Create configuration management menu "project" | `Resources_de.properties`, `Resources_es.properties` +24 | [3d48a50f](https://github.com/freeplane/freeplane/commit/3d48a50f21c48e00706db2a23980d565965775b4) |
| 2024-05-12 | `fix` | fix check for changed tag values | `TagEditor.java` | [1d6a4431](https://github.com/freeplane/freeplane/commit/1d6a44315a7b805336f48f30ffb4e76c5c1ba1ca) |
| 2024-05-12 | `fix` | fix submit and submit on close | `IconRegistry.java`, `TagCategories.java` +2 | [c0b20baa](https://github.com/freeplane/freeplane/commit/c0b20baae29ee3de0ab140db7c5ebbcc93c622ab) |
| 2024-05-12 | `fix` | fix component focus transition | `TagEditor.java` | [acf8f470](https://github.com/freeplane/freeplane/commit/acf8f4701c20a1dc84a84852817864b332f30abb) |
| 2024-05-12 | `feature` | fix new child tag action | `TagEditor.java` | [ff61d70b](https://github.com/freeplane/freeplane/commit/ff61d70bb83d86580e2e60aa82c83ead8129451c) |
| 2024-05-12 | `fix` | Fix tag category editor bugs | `MIconController.java`, `TagCategoryEditor.java` +2 | [15dfb478](https://github.com/freeplane/freeplane/commit/15dfb4783ba386f150e166479c7aa0e17b741191) |
| 2024-05-12 | `fix` | bug fixes | `IconRegistry.java`, `TagCategories.java` +5 | [8de13f41](https://github.com/freeplane/freeplane/commit/8de13f4184c3f1797d87990b3873952035982cd5) |
| 2024-05-11 | `fix` | fix editor field width | `TagCategoryEditor.java` | [2e8ca79d](https://github.com/freeplane/freeplane/commit/2e8ca79d8a70a85b5d8f526bfbad621653d0bc6d) |
| 2024-05-11 | `fix` | Fix tag heights in editors | `TagIcon.java`, `TagCategoryEditor.java` +1 | [136d9253](https://github.com/freeplane/freeplane/commit/136d9253578bcbc59e46514d27f63feeba1b3932) |
| 2024-05-11 | `fix` | Fix menu item accelerator | `TagCategoryEditor.java` | [37476a13](https://github.com/freeplane/freeplane/commit/37476a13a82c0ee51ff40be19a033f34d4d501f7) |
| 2024-05-11 | `fix` | Fix editor focus on Windows | `TagEditor.java` | [aea5d76d](https://github.com/freeplane/freeplane/commit/aea5d76d80d430c52dc5807526b31ec2f2c66537) |
| 2024-05-10 | `feature` | Add tags to search and replace dialog | `ListComparator.java`, `IconController.java` +4 | [fe654666](https://github.com/freeplane/freeplane/commit/fe6546669939b9644163bc1e82fd0b85075f03a6) |
| 2024-05-09 | `feature` | Implement map and node tag categories when showing, in filters and API | `mindmapmodemenu.xml`, `preferences.xml` +18 | [0469cdfd](https://github.com/freeplane/freeplane/commit/0469cdfd525609755cf7567e1fc41dab33583209) |
| 2024-05-09 | `feature` | add API methods and filters for tag categories | `preferences.xml`, `CategorizedTag.java` +13 | [b1ee9533](https://github.com/freeplane/freeplane/commit/b1ee9533bb8073270a365b1883c77e472e96f5f1) |
| 2024-05-09 | `fix` | save tag categories in the map and fix tag category editor | `mindmapmodemenu.xml`, `CategorizedTagForCategoryNode.java` +11 | [3a72e274](https://github.com/freeplane/freeplane/commit/3a72e2748dc5edca8c08d73a85d8edf6baa727da) |
| 2024-05-06 | `fix` | fix text field y position | `EditNodeTextField.java` | [b8449de1](https://github.com/freeplane/freeplane/commit/b8449de158ed3e0fe39980df3894800d0ccf33f3) |
| 2024-05-06 | `fix` | fix tag categories | `CategorizedTagForCategoryNode.java`, `MIconController.java` +2 | [ce5956d8](https://github.com/freeplane/freeplane/commit/ce5956d8b7f264486278600258642dd1e9892061) |
| 2024-05-05 | `fix` | fix edited text field height | `EditNodeTextField.java` | [77169cec](https://github.com/freeplane/freeplane/commit/77169cecc6e56d1f3c8bbdb6a659e25a12428561) |
| 2024-05-05 | `feature` | Add filter for tag categories | `CategorizedTag.java`, `IconConditionController.java` +11 | [3a58f49c](https://github.com/freeplane/freeplane/commit/3a58f49c53160c9ad1c3e2d9667c0d24709b047d) |
| 2024-05-05 | `fix` | fix compile error | `TagCategories.java` | [0353f9da](https://github.com/freeplane/freeplane/commit/0353f9dad54b16517ae85dedae1e8f12f971f8d9) |
| 2024-05-05 | `fix` | fix tag cache | `JFilterableComboBox.java`, `CategorizedTagForCategoryNode.java` +2 | [bc857b38](https://github.com/freeplane/freeplane/commit/bc857b38ed3b8ed8faf571dde7c4dad4314eda1c) |
| 2024-05-05 | `fix` | fix compile error | `TagCategories.java` | [3656b4d7](https://github.com/freeplane/freeplane/commit/3656b4d78c76488e1f826621013eb2e3b44c6345) |
| 2024-05-05 | `feature` | register new tag categories | `TagCategories.java` | [62c2a8e7](https://github.com/freeplane/freeplane/commit/62c2a8e7528472c28d72c72c7c2dda27f2f213e2) |
| 2024-04-28 | `feature` | Add Edit menus to TagCategoryEditor and TagEditor | `TranslatedElementFactory.java`, `TagCategoryEditor.java` +2 | [3b424388](https://github.com/freeplane/freeplane/commit/3b424388a537d1542ba69636e3dca613dc3018e8) |
| 2024-04-27 | `feature` | Add node short text to dialogs for editing details, note and tags | `TagCategories.java`, `TagEditor.java` +3 | [2e1a5c4c](https://github.com/freeplane/freeplane/commit/2e1a5c4c171f78a373fa08b5c96f14bc2944aabc) |
| 2024-04-27 | `feature` | Implement Tag Editor Menu based on tag categories | `TranslatedElementFactory.java`, `IconRegistry.java` +5 | [45f5f1f3](https://github.com/freeplane/freeplane/commit/45f5f1f35d01604476bc3bca53deb6b018febfa6) |
| 2024-04-09 | `fix` | Fix node painting when the node is edited | `MapView.java`, `VariableInsetsPainter.java` +1 | [9828ec26](https://github.com/freeplane/freeplane/commit/9828ec2669aa483538005e22985943b2a9cbe3d8) |
| 2024-04-09 | `fix` | Issue #1776 Bug if tag exceeds node max width | `EditNodeTextField.java` | [cd468925](https://github.com/freeplane/freeplane/commit/cd4689259d668fe7e2ca7569d7a06588c6e5e1a6) |
| 2024-04-07 | `feature` | add node style to configure the tag font | `IconController.java`, `TagEditor.java` +3 | [909bdcf1](https://github.com/freeplane/freeplane/commit/909bdcf16a9de3832b4380fc2385cc3e74d9d979) |
| 2024-04-06 | `feature` | Add filter conditions for tags | `CompareConditionAdapter.java`, `IconConditionController.java` +5 | [d7e0ec86](https://github.com/freeplane/freeplane/commit/d7e0ec864ff83225ac5d483a48d695b0a099b990) |
| 2024-04-06 | `feature` | implement iconController.getTags() | `IconController.java`, `TagContainedCondition.java` +4 | [707afcf1](https://github.com/freeplane/freeplane/commit/707afcf1bd862a17bfc6e9ef15c85223ed96fee8) |
| 2024-04-05 | `feature` | Support sorting tags in tag editor | `TagEditor.java`, `Resources_en.properties` +3 | [fd067897](https://github.com/freeplane/freeplane/commit/fd067897212b829876fe93f4848d789ea51a3372) |
| 2024-04-05 | `fix` | bug fixes in tag editor | `TagEditor.java` | [f4268be7](https://github.com/freeplane/freeplane/commit/f4268be79a32b71d7530ac26a02d2c8e156678e3) |
| 2024-04-03 | `feature` | implement tags | `build.gradle`, `mindmapmodemenu.xml` +19 | [10ac51da](https://github.com/freeplane/freeplane/commit/10ac51da9104bde5fe2a8516f86babf38fb90a20) |
| 2024-03-31 | `fix` | Fix: always paint connectors of selected nodes | `MapView.java` | [c6a59a04](https://github.com/freeplane/freeplane/commit/c6a59a0435fae541c3aae4fa745878aef9ce8be4) |
| 2024-03-29 | `feature` | implement quickly adding project folders to configuration | `freeplane.properties`, `Resources_en.properties` +3 | [37b2e81b](https://github.com/freeplane/freeplane/commit/37b2e81bf2b2b2a20722d40d74518514d52a2ae3) |
| 2024-03-22 | `fix` | Fix menu bar disabled after assigning a hot key on MacOS | `GrabKeyDialog.java`, `UITools.java` | [d459b3a9](https://github.com/freeplane/freeplane/commit/d459b3a9c7877e7090bfe980965a1088d8d097ce) |
| 2024-03-17 | `feature` | Add links to code explorer online documentation | `codeexplorermodemenu.xml`, `freeplane.properties` +2 | [0d0a48cc](https://github.com/freeplane/freeplane/commit/0d0a48ccedd037217eb2d29c9f8dca651b7b7e31) |
| 2024-03-16 | `fix` | fix stack overflow error | `ViewerController.java` | [41e9a691](https://github.com/freeplane/freeplane/commit/41e9a69169af961c78ddf41b9e0f1102d511b532) |
| 2024-03-16 | `fix` | fix NPE | `MMapController.java` | [1f2822df](https://github.com/freeplane/freeplane/commit/1f2822df4e33257a12c6dd7a95e487427e77be4d) |
| 2024-03-16 | `fix` | Fix selection after filtering | `MapView.java` | [e5b1949f](https://github.com/freeplane/freeplane/commit/e5b1949f06f8afefe609997510e18c142cc982b6) |
| 2024-03-16 | `fix` | fix class cast exception | `DoAutomaticSave.java` | [f85cf653](https://github.com/freeplane/freeplane/commit/f85cf6537df2fa5b7b296ee6162b2868609544b1) |
| 2024-03-16 | `fix` | Try to fix NPE when parent node is not defined (I have no clue why it happens) | `MNodeMotionListener.java` | [c96338c0](https://github.com/freeplane/freeplane/commit/c96338c0b464eb1166042ffa1584b7c7cffcb428) |
| 2024-03-14 | `fix` | Fix explore menu icons | `AFreeplaneAction.java`, `freeplane.properties` +1 | [b206e79a](https://github.com/freeplane/freeplane/commit/b206e79a35cbf69775c53b0228874ed307806f32) |
| 2024-02-26 | `fix` | Apply fix to docking library | `ComponentCache.java` | [d956154e](https://github.com/freeplane/freeplane/commit/d956154eab0515c2484106bafc15b8ed3f43083d) |
| 2024-02-20 | `feature` | Add "show selected attributes" option to code explorer | `codeexplorermodemenu.xml` | [34c2a6a7](https://github.com/freeplane/freeplane/commit/34c2a6a79129cb11cf34280bfabaf1df9dff5da9) |
| 2024-02-17 | `feature` | add Javadoc for normalizeTemplateLocation | `TemplateManager.java` | [f4a1badc](https://github.com/freeplane/freeplane/commit/f4a1badc786cf6a76002f55419320d235dd96dfb) |
| 2024-02-12 | `fix` | Fix race condition when registering attributes: delay registration | `AttributeRegistry.java`, `NodeAttributeTableModel.java` +5 | [229369f0](https://github.com/freeplane/freeplane/commit/229369f0839c76c790cf7a1f4c59f8adbd519b59) |
| 2024-02-12 | `feature` | Add map property "Optimize attribute width" (Menu View->Node attributes) | `mindmapmodemenu.xml`, `AttributeController.java` +5 | [1bf59d2f](https://github.com/freeplane/freeplane/commit/1bf59d2f4fc15e19d60f91224562e69b82e0c9ed) |
| 2024-02-06 | `fix` | fix attribute table cell tooltip colors | `FreeplaneTooltip.java`, `MainView.java` +2 | [7c90f7b0](https://github.com/freeplane/freeplane/commit/7c90f7b06f486dc1db189351ddb3e68839a29cd7) |
| 2024-02-05 | `fix` | Fix option panel | `HeadlessMModeControllerFactory.java`, `SModeControllerFactory.java` | [eb052bac](https://github.com/freeplane/freeplane/commit/eb052bac6afabbd9f57d4d6c890094d0ff2d12e4) |
| 2024-02-05 | `feature` | Add copy and paste attributes actions to code explorer | `codeexplorermodemenu.xml`, `CopyAttributes.java` +1 | [1796d228](https://github.com/freeplane/freeplane/commit/1796d2288aee0536660bfb027034d24066eaeb16) |
| 2024-02-02 | `feature` | Add and save user content | `codeexplorermodemenu.xml`, `ResourceController.java` +33 | [2a91840e](https://github.com/freeplane/freeplane/commit/2a91840e2f073fd49622c50e3d3b0e71d7904242) |
| 2024-02-01 | `fix` | fix eclipse java environment name | `RemoveAllAttributesAction.java` | [ce7a2caf](https://github.com/freeplane/freeplane/commit/ce7a2caf7487c2905cc3a7083aa1f8d17fc55ead) |
| 2024-02-01 | `feature` | Support editing of details and attributes on code explorer maps | `codeexplorermodemenu.xml`, `MapController.java` +15 | [8bf8f032](https://github.com/freeplane/freeplane/commit/8bf8f032f074f037bd47614c211d1be7f4990769) |
| 2024-02-01 | `fix` | Fix reloading map if only remaining map is CodeExplorer | `LastOpenedList.java` | [0f43ff7a](https://github.com/freeplane/freeplane/commit/0f43ff7a1c201e4d8cfa256e3b444eec46c10982) |
| 2024-01-20 | `fix` | Fix NPE | `AConnectorView.java` | [c6ed3d2a](https://github.com/freeplane/freeplane/commit/c6ed3d2a4375d964fbf4314f60773226a9289663) |
| 2024-01-13 | `feature` | Issue #1628 Bug when searching with Jump In activated: | `NodeView.java` | [97131289](https://github.com/freeplane/freeplane/commit/9713128922e730688012a51437cfb6a9f74499f7) |
| 2024-01-13 | `fix` | Revert "Issue #1628 Bug when searching with Jump In activated" | `FoundNodes.java` | [c128f0a4](https://github.com/freeplane/freeplane/commit/c128f0a4f902db4e29fd41bdad3fa17b4df9b533) |
| 2024-01-13 | `fix` | Fix password protection | `NodeModel.java` | [af6385bb](https://github.com/freeplane/freeplane/commit/af6385bb16dd53e4d48584c93bc635018270db4a) |
| 2024-01-13 | `fix` | Revert "Fix password protection" | `NodeModel.java`, `NodeView.java` | [ab136eea](https://github.com/freeplane/freeplane/commit/ab136eeace57bd33adc8f2ec5d128b67d555f2dc) |
| 2024-01-11 | `fix` | Fix password protection | `NodeModel.java`, `NodeView.java` | [9aeb0729](https://github.com/freeplane/freeplane/commit/9aeb07299e3e93dfa4c16d8724fe248e1c55449f) |
| 2024-01-08 | `fix` | Issue #1628 Bug when searching with Jump In activated | `FoundNodes.java` | [50e7ab60](https://github.com/freeplane/freeplane/commit/50e7ab6073f0e2c6ab9364af0424a5fc7abc3db0) |
| 2024-01-06 | `feature` | Add link to code explorer introduction video to the help menu | `latestFreeplaneFeatures.mm`, `codeexplorermodemenu.xml` +3 | [22d97d60](https://github.com/freeplane/freeplane/commit/22d97d604f881cbfc412ee7d58158b7aa5b1c057) |
| 2024-01-03 | `feature` | add map statistics to code explorer mode | `codeexplorermodemenu.xml`, `FilePropertiesAction.java` | [351e505d](https://github.com/freeplane/freeplane/commit/351e505dc3cd5e538a4d958c2da39ce4ae01296b) |

### Dettagli commit con note

**[6fdc8e4f](https://github.com/freeplane/freeplane/commit/6fdc8e4fd70988479fdff72770831c5e09bf48a8)** (2024-08-14) — Fix java.lang.ArrayIndexOutOfBoundsException:

> at java.base/java.util.Vector.elementAt(Vector.java:466)
> 	at java.desktop/javax.swing.table.DefaultTableColumnModel.getColumn(DefaultTableColumnModel.java:298)
> 	at org.freeplane.view.swing.features.time.mindmapmode.nodelist.NodeList.initializeUI(NodeList.java:712)
> 	at org.freeplane.view.swing.features.time.mindmapmode.nodelist.NodeList.startup(NodeList.java:500)
> 	at org.freeplane.view.swing.features.time.mindmapmode.nodelist.AllMapsNodeListAction.actionPerformed(AllMapsNodeListAction.java:48)
> 	at java.desktop/javax.swing.SwingUtilities.notifyAction(SwingUtilities.java:1810)

**[acd58076](https://github.com/freeplane/freeplane/commit/acd58076fcee0a4b1dd961cd54f8e25ad76d7f7e)** (2024-08-14) — Fix java.lang.ArrayIndexOutOfBoundsException: Index 0 out of bounds for length 0

> at org.freeplane.view.swing.map.VerticalNodeViewLayoutStrategy.calculateLayoutY(VerticalNodeViewLayoutStrategy.java:143)
> 	at org.freeplane.view.swing.map.VerticalNodeViewLayoutStrategy.calculateLayoutData(VerticalNodeViewLayoutStrategy.java:109)
> 	at org.freeplane.view.swing.map.VerticalNodeViewLayoutStrategy.calculateLayoutData(VerticalNodeViewLayoutStrategy.java:103)
> 	at org.freeplane.view.swing.map.NodeViewLayout.layoutContainer(NodeViewLayout.java:44)

**[86fffd0e](https://github.com/freeplane/freeplane/commit/86fffd0ef32ebe8ffe0a8c0166475fea5360e20c)** (2024-08-10) — Revert "The character was visible in arial, fix it."

> This reverts commit ec8f4870e4cd443510ac4719fce947783ff93ce2.

**[9e7613ba](https://github.com/freeplane/freeplane/commit/9e7613ba63618ae1b5f94d25af71312f64ed5052)** (2024-05-26) — add option to prefer node-border color for state-symbol background

> so that clone and "minimized" marks are prominent, thus easily noticeable

**[e7a72cfa](https://github.com/freeplane/freeplane/commit/e7a72cfa141d769a69a17166bd8c79bc7a200dbe)** (2024-05-26) — fix state symbol to no longer be invisible when node border and background are invisible

> Up till now, state-symbol has had border color of node-border color and background color of node-background color. This was causing the issue of invisible clone and/or "minimized" marks if node border and background were invisible. The new logic looks for a non-obviously-invisible property for border and falls back to using "standard selected node color (fallback)" for background. This assumes people want to see state symbols, i.e. clone and "minimized" marks. Showing clone marks can be disabled in preferences. To also hide "minimized" marks, "standard selected node and state-symbol color (fallback)" can be set to an invisible color.

**[d956154e](https://github.com/freeplane/freeplane/commit/d956154eab0515c2484106bafc15b8ed3f43083d)** (2024-02-26) — Apply fix to docking library

> https://github.com/ebourg/infonode/commit/e14d433c1c2d467913bf5f069904fbb292be0e04

**[97131289](https://github.com/freeplane/freeplane/commit/9713128922e730688012a51437cfb6a9f74499f7)** (2024-01-13) — Issue #1628 Bug when searching with Jump In activated:

> create "fake" parent node view if needed for layout

**[c128f0a4](https://github.com/freeplane/freeplane/commit/c128f0a4f902db4e29fd41bdad3fa17b4df9b533)** (2024-01-13) — Revert "Issue #1628 Bug when searching with Jump In activated"

> This reverts commit 50e7ab6073f0e2c6ab9364af0424a5fc7abc3db0.

**[ab136eea](https://github.com/freeplane/freeplane/commit/ab136eeace57bd33adc8f2ec5d128b67d555f2dc)** (2024-01-13) — Revert "Fix password protection"

> This reverts commit 9aeb07299e3e93dfa4c16d8724fe248e1c55449f.

**[50e7ab60](https://github.com/freeplane/freeplane/commit/50e7ab6073f0e2c6ab9364af0424a5fc7abc3db0)** (2024-01-08) — Issue #1628 Bug when searching with Jump In activated

> don't fold any nodes outside current selection root


---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-12-31 | `fix` | fix logic when connector lines and arrows are shown | `MapView.java` | [3d524abd](https://github.com/freeplane/freeplane/commit/3d524abdde7b772932d4d58f22a07df070af5f5d) |
| 2023-12-27 | `feature` | Add visual indication of successful / failed search | `FilterConditionEditor.java`, `QuickFindAction.java` | [2c5ead20](https://github.com/freeplane/freeplane/commit/2c5ead20ba7d7b3e31c9fbf8ade584d6ffad6e51) |
| 2023-12-26 | `fix` | fix NPE | `MMapClipboardController.java` | [f623130e](https://github.com/freeplane/freeplane/commit/f623130e7a1d8133ac37d4326bbb432d63f2720f) |
| 2023-12-23 | `fix` | fix handling selected nodes | `MapView.java` | [483ac36d](https://github.com/freeplane/freeplane/commit/483ac36ddcff5667366af67f7aee6dfbd8c30f2b) |
| 2023-12-19 | `feature` | add "copy single node" to menu | `codeexplorermodemenu.xml` | [cd9a3620](https://github.com/freeplane/freeplane/commit/cd9a36203061c6b6ba8d7cb457c97bd9949c931c) |
| 2023-12-19 | `feature` | Add copying code map as usual map | `codeexplorermodemenu.xml` | [70846253](https://github.com/freeplane/freeplane/commit/7084625325683ae6231fe9cdadca5f53ea1f3cdf) |
| 2023-12-19 | `feature` | Add exports to code mode | `codeexplorermodemenu.xml`, `CodeModeControllerFactory.java` | [ee210bf4](https://github.com/freeplane/freeplane/commit/ee210bf4ed92da7212923593f27503cf0b0de61b) |
| 2023-12-17 | `fix` | it looks like wrong var was used, fix it | `IconReplacer.java` | [5ad78e18](https://github.com/freeplane/freeplane/commit/5ad78e18a1338000f9c899332846015d9f6c511b) |
| 2023-12-15 | `fix` | fix menu name | `codeexplorermodemenu.xml`, `Resources_en.properties` | [adeb0f89](https://github.com/freeplane/freeplane/commit/adeb0f89caf70cba0c82d37dcba2de2c5d81acac) |
| 2023-12-10 | `fix` | Fix NPE when nodes are deleted | `MapModel.java`, `CodeMap.java` | [9dd9d958](https://github.com/freeplane/freeplane/commit/9dd9d958f345dca6a331f4e62c2f984d276cadcf) |
| 2023-12-10 | `feature` | add translations | `Resources_en.properties`, `CodeExplorerConfigurator.java` | [ed875661](https://github.com/freeplane/freeplane/commit/ed875661b46e3432f10c1e2f077a53100d14dcf5) |
| 2023-12-09 | `feature` | add icons for analysis panel actions | `freeplane.properties`, `Resources_en.properties` +11 | [dc1315e6](https://github.com/freeplane/freeplane/commit/dc1315e6ec393fce7a670b692e5da28c047f7083) |
| 2023-12-09 | `feature` | Enable some general user actions for code explorer mode | `codeexplorermodemenu.xml`, `MModeController.java` +4 | [fa84fc24](https://github.com/freeplane/freeplane/commit/fa84fc24083e4f3ca61562fffc3e09f5ccec9b9e) |
| 2023-12-04 | `fix` | fix translations | `codeexplorermodemenu.xml`, `Resources_en.properties` | [5e97e628](https://github.com/freeplane/freeplane/commit/5e97e628a8d3338b4b5b2d2041ccbc9e570cdfdb) |
| 2023-12-04 | `feature` | Add actions to show connected nodes regardless dependency directions | `codeexplorermodemenu.xml`, `freeplane.properties` +6 | [fd6eacd7](https://github.com/freeplane/freeplane/commit/fd6eacd78d161adec385815409be11a04149c7fd) |
| 2023-12-04 | `fix` | FP fix svg | `jumpOut.svg` | [8d970adb](https://github.com/freeplane/freeplane/commit/8d970adb5a8eea7dc79738145b6f7d8ed7d92db6) |
| 2023-12-04 | `feature` | FP support use of OSGi plug-in class loaders for loading resources | `ApplicationResourceController.java` | [a18379db](https://github.com/freeplane/freeplane/commit/a18379db996d3e366b04d3621f1c0928db0e2af9) |
| 2023-12-03 | `fix` | fix adding map view as map change listener to the map model | `MapView.java`, `MapViewController.java` | [aedce605](https://github.com/freeplane/freeplane/commit/aedce6051f4b24639e12fc0a3e470d1a05c95149) |
| 2023-12-03 | `feature` | add new actions to the menu | `codeexplorermodemenu.xml` | [9531fae3](https://github.com/freeplane/freeplane/commit/9531fae35074c18bd3348bd00ae73e5baf13fc09) |
| 2023-12-02 | `feature` | implement subprojects | `MapModel.java`, `MapView.java` +13 | [0da43737](https://github.com/freeplane/freeplane/commit/0da437370a6ce943797dd161de3415113c88d873) |
| 2023-12-01 | `feature` | prepare for multiple locations: add subproject index to node IDs | `NodeLinkModel.java`, `CodeConnectorModel.java` +10 | [129d7911](https://github.com/freeplane/freeplane/commit/129d791129c87c7277ad563cd957d49e9cc470f4) |
| 2023-11-28 | `feature` | Add command search action and hotkey reference action | `codeexplorermodemenu.xml` | [9f92015d](https://github.com/freeplane/freeplane/commit/9f92015dfca49d3fdbc1fea21bddd14bb9b36a3a) |
| 2023-11-27 | `feature` | implement RunAnalysisAction | `update-arrows.svg`, `codeexplorermodemenu.xml` +5 | [16cc8616](https://github.com/freeplane/freeplane/commit/16cc861616872c4847f08a80951abbad1219b8e1) |
| 2023-11-26 | `feature` | Adding new nodes linked to menu commands (#1543) | `Resources_af.properties`, `Resources_cs.properties` +39 | [d2e34dff](https://github.com/freeplane/freeplane/commit/d2e34dffa77228141d2fb1992fd1af66c20dfaf4) |
| 2023-11-25 | `fix` | FP fix navigation to siblings: root can't be a sibling | `NodeView.java` | [5af17d1e](https://github.com/freeplane/freeplane/commit/5af17d1eb31b8bfcf32388392f4008ed19148c5b) |
| 2023-11-23 | `feature` | add translations | `CodeDependenciesPanel.java`, `CodeExplorerConfigurator.java` +1 | [12f22feb](https://github.com/freeplane/freeplane/commit/12f22feb3f5484ae4d77d426260127b483959a61) |
| 2023-11-23 | `feature` | FP add method to be notified after map root node changes | `FilterController.java` | [528c8932](https://github.com/freeplane/freeplane/commit/528c8932487803140b6485eba6a0f0cf01e8b86a) |
| 2023-11-21 | `fix` | fix translations | `Resources_en.properties` | [fd1addd3](https://github.com/freeplane/freeplane/commit/fd1addd3a6b1a700b500fd9981d8803ab916aae6) |
| 2023-11-21 | `feature` | implement depth first graph explorer | `GraphExplorer.java` | [50009015](https://github.com/freeplane/freeplane/commit/5000901529a85296cfcbfc80ebf1eaa0f833e687) |
| 2023-11-21 | `feature` | Add subgroup indices to identify connected subgraphs for sibling nodes | `ClassNodeModel.java`, `ClassesNodeModel.java` +6 | [640a4cf4](https://github.com/freeplane/freeplane/commit/640a4cf42dfca76a87ecaa4323f5e1236fff16f8) |
| 2023-11-21 | `fix` | fix search stop criteria: we need2 edges to have a cycle here | `GraphCycleFinder.java` | [ad6f232b](https://github.com/freeplane/freeplane/commit/ad6f232ba5f0a0c065cc88d1a411171c0d045c0b) |
| 2023-11-20 | `feature` | add code node icons | `LICENSE.txt`, `NOTICE.txt` +17 | [adf50f14](https://github.com/freeplane/freeplane/commit/adf50f14a1719d56dd6b256c453ed3a99e6ec396) |
| 2023-11-19 | `feature` | Add actions to select nodes in cycles | `code_select_selected_cycles.svg`, `code_select_visible_cycles.svg` +5 | [a973665c](https://github.com/freeplane/freeplane/commit/a973665c0ee1403938a705c15a037c5ce69691cb) |
| 2023-11-19 | `feature` | add class counters to nodes | `ClassesNodeModel.java`, `CodeNodeModel.java` +1 | [8e1f353f](https://github.com/freeplane/freeplane/commit/8e1f353f5cc4f18b909a88667bf173b4f349dbf8) |
| 2023-11-16 | `feature` | add translation string | `Resources_en.properties` | [0536a6cb](https://github.com/freeplane/freeplane/commit/0536a6cb4e7918cab099fe1530f46455c0d68f44) |
| 2023-11-16 | `feature` | FP implement AncestorRemover | `AncestorRemover.java` | [0a62df1b](https://github.com/freeplane/freeplane/commit/0a62df1bdd3d4a12cc19cd016dbc0c6a6c89aaf2) |
| 2023-11-16 | `feature` | FP implement AncestorRemover | `AncestorRemover.java` | [fb21833a](https://github.com/freeplane/freeplane/commit/fb21833a98b593a27128f00f948522b32d8b9b0a) |
| 2023-11-14 | `feature` | refactor ClassNodeModel and add methods getOutgoingDependencies and getIncomingDependencie | `ClassNodeModel.java`, `ClassesNodeModel.java` +3 | [02c1ffc1](https://github.com/freeplane/freeplane/commit/02c1ffc12e9118a38bdb07659cbdaa3e59c2e12b) |
| 2023-11-14 | `feature` | FP add methods to IMapSelection and INodeSelectionListener | `IMapSelection.java`, `INodeSelectionListener.java` +2 | [45a6acfd](https://github.com/freeplane/freeplane/commit/45a6acfd1769798e44a530cba6f334ce90352660) |
| 2023-11-14 | `feature` | FP add methods to IMapSelection and INodeSelectionListener | `IMapSelection.java`, `INodeSelectionListener.java` +2 | [1abf8f67](https://github.com/freeplane/freeplane/commit/1abf8f67f18b6d8cd485a4be2f21a6c1cc4d74cc) |
| 2023-11-14 | `feature` | FP add and call method INodeSelectionListener.onSelectionSetChange | `INodeSelectionListener.java`, `SelectionController.java` +1 | [dfa11454](https://github.com/freeplane/freeplane/commit/dfa114548d6e2496a85e2d07ae5ac14de51e2051) |
| 2023-11-14 | `feature` | FP add and call method INodeSelectionListener.onSelectionSetChange | `INodeSelectionListener.java`, `SelectionController.java` +1 | [a46372ae](https://github.com/freeplane/freeplane/commit/a46372ae21b87a05a452d0fdd8cceabe4cf9c043) |
| 2023-11-14 | `feature` | extract methods to remove duplication and and implement getIncomingLinks | `ClassNodeModel.java`, `ClassesNodeModel.java` +2 | [65bbf096](https://github.com/freeplane/freeplane/commit/65bbf096e9edb086d20400b8bd83485161252f8d) |
| 2023-11-13 | `feature` | add goto dependency node actions | `codeexplorermodemenu.xml` | [3b947f78](https://github.com/freeplane/freeplane/commit/3b947f784394a2021a27016cf091893e02930bea) |
| 2023-11-13 | `feature` | add navigation actions | `codeexplorermodemenu.xml`, `JumpInAction.java` +4 | [4b309f62](https://github.com/freeplane/freeplane/commit/4b309f6296e74f897f24600e3192f424acb803fe) |
| 2023-11-10 | `feature` | FP fix: do not modify returned point, create a new one | `InclinationRecommender.java` | [272801cd](https://github.com/freeplane/freeplane/commit/272801cda9c48d7b4736228afb50be5b75cedccf) |
| 2023-11-10 | `feature` | FP fix: do not modify returned point, create a new one | `InclinationRecommender.java` | [32dcd97a](https://github.com/freeplane/freeplane/commit/32dcd97a8ada0e411f034591278bcd2426b92217) |
| 2023-11-09 | `fix` | fix: iterate over connected subgraph, not the complete graph | `PreferenceOrdering.java` | [7a92f189](https://github.com/freeplane/freeplane/commit/7a92f1893a6ab6ae84a74d0087a93ba01ce3dff9) |
| 2023-11-09 | `fix` | Fix node order | `PreferenceOrdering.java` | [301e6c11](https://github.com/freeplane/freeplane/commit/301e6c119fcf861db3c92fae4d2e258d57297efe) |
| 2023-11-09 | `fix` | fix translations | `Resources_en.properties` | [5f2aad7d](https://github.com/freeplane/freeplane/commit/5f2aad7db1d9c3c39cd10e3013ea553773c454be) |
| 2023-11-09 | `fix` | fix connectors for unfolded source packages and folded target packages | `CodeLinkController.java`, `JavaPackageNodeModel.java` | [74726e3b](https://github.com/freeplane/freeplane/commit/74726e3b30f06dbac5090c7a0d6c3fb1438e255d) |
| 2023-11-09 | `feature` | Add option on MapView to always repaing connectors after selection change | `MapView.java` | [9cf6e972](https://github.com/freeplane/freeplane/commit/9cf6e9721c037be314b44c0c965ce0f77356cb68) |
| 2023-11-09 | `feature` | Add option on MapView to always repaing connectors after selection change | `MapView.java` | [791305ca](https://github.com/freeplane/freeplane/commit/791305ca805cc2b5ddd196d09f6bfcde586071eb) |
| 2023-11-09 | `feature` | refactor: let only MMapController implement method newNode(final Object userObject, final  | `MapController.java`, `FMapController.java` +2 | [3ec0f854](https://github.com/freeplane/freeplane/commit/3ec0f854b769e3edde226f7a45d6440eecf83fa4) |
| 2023-11-09 | `feature` | refactor: let only MMapController implement method newNode(final Object userObject, final  | `MapController.java`, `FMapController.java` +2 | [42bd6c06](https://github.com/freeplane/freeplane/commit/42bd6c063f87cfdd58626fe6b7969a58f99551f2) |
| 2023-11-08 | `feature` | Implement node ordering based on weakly connected components | `PreferenceOrdering.java` | [3012c623](https://github.com/freeplane/freeplane/commit/3012c623bb547f227903c5bcefc8008aaa51c831) |
| 2023-11-06 | `fix` | fix some translation keys | `Resources_oc.properties`, `Resources_ru.properties` | [442287dc](https://github.com/freeplane/freeplane/commit/442287dc9f3119e7c23b30f8e241791a3f3ad445) |
| 2023-11-05 | `feature` | add style "Flower" also to BigMap template | `BigMap.mm` | [f496b9aa](https://github.com/freeplane/freeplane/commit/f496b9aa4ec1125a05329db2fecb4ff2ee7abbd3) |
| 2023-11-05 | `feature` | Add style "Flower" to all standard templates | `history_en.txt`, `latestFreeplaneFeatures.mm` +57 | [783da622](https://github.com/freeplane/freeplane/commit/783da622f6e690bb2c87b419ecab8f3554309c28) |
| 2023-11-02 | `fix` | fix painting fork nodes | `ForkPainter.java` | [ccfa550c](https://github.com/freeplane/freeplane/commit/ccfa550cf2209d5ca6e7bcae69d6fd4b1f239be2) |
| 2023-11-02 | `fix` | fix color | `ForkPainter.java` | [23a836a7](https://github.com/freeplane/freeplane/commit/23a836a728ed275e166496672cffb47b1cb3ae06) |
| 2023-11-02 | `fix` | fix ci compile error | `PreferencesIndexer.java` | [f70771b7](https://github.com/freeplane/freeplane/commit/f70771b77f54e7bf87bc76349a177ff7a05ce625) |
| 2023-11-02 | `fix` | remove unnecessary type casts (auto fix) | `Scalr.java`, `NumberSliderProperty.java` +8 | [b017a10d](https://github.com/freeplane/freeplane/commit/b017a10d7c7282c7507a87cac0938c9293139720) |
| 2023-10-31 | `feature` | Issue #1439 Sometimes "Save all maps" doesnt work on all maps: consider new maps | `SaveAll.java` | [9521bf34](https://github.com/freeplane/freeplane/commit/9521bf3417b552ed91f760776e855b18d892e62e) |
| 2023-10-29 | `feature` | API changes (node's border and edge) (#1355) | `ComboProperty.java`, `DashIconFactory.java` +39 | [2a803599](https://github.com/freeplane/freeplane/commit/2a80359962a8ea7b3aa98caa760dd781e7ffd5c3) |
| 2023-10-28 | `fix` | fix undo for connectors defined on default style | `MMapMouseListener.java` | [587cc386](https://github.com/freeplane/freeplane/commit/587cc3861d82a6200267595ac18f50e408f51b6c) |
| 2023-10-22 | `feature` | New BigMap template version | `BigMap.mm`, `BigMap.svg` | [5d1019a3](https://github.com/freeplane/freeplane/commit/5d1019a334e4aa2339711c82dc6bf9027fbd0532) |
| 2023-10-15 | `fix` | Rename tabs (#1353) | `MapViewDockingWindows.java`, `Resources_en.properties` | [d96fb632](https://github.com/freeplane/freeplane/commit/d96fb632d4b15830887b05ec40184c7c03e8cc3f) |
| 2023-10-09 | `fix` | Fix NPE | `NoteManager.java` | [793a72d1](https://github.com/freeplane/freeplane/commit/793a72d1ed8834b9a6a3cf76e3e31a7669df3995) |
| 2023-10-03 | `fix` | Fix logic of toggle button selection on the toolbar | `JAutoToggleButton.java`, `HorizontalTextAlignmentAction.java` +1 | [c7efc256](https://github.com/freeplane/freeplane/commit/c7efc256aead12e6fe8c936397386104bb67cb06) |
| 2023-10-03 | `fix` | fix icon | `closed.svg` | [1f0b2436](https://github.com/freeplane/freeplane/commit/1f0b243697e0a541df17a8b1f520683b23b5e094) |
| 2023-10-03 | `fix` | fix thumbnails on mac | `leftToRight.svg`, `rightToLeft.svg` +1 | [31257230](https://github.com/freeplane/freeplane/commit/312572304a73d6da0da382aaf4d32f410fb332d5) |
| 2023-10-03 | `feature` | wip right-to-left text writing direction support | `leftToRight.svg`, `rightToLeft.svg` +23 | [42f9c353](https://github.com/freeplane/freeplane/commit/42f9c35356f5dd6f9550bcf08b5654775ad5d659) |
| 2023-10-02 | `feature` | Add horizontal text alignment to API | `NodeStyleBuilder.java`, `NodeStyleController.java` +12 | [c54d215e](https://github.com/freeplane/freeplane/commit/c54d215e9760368c013203dd3232124c95dd7863) |
| 2023-09-23 | `feature` | Issue #1422 Add / Remove cloud on multiple nodes | `CloudAction.java` | [4ba63c31](https://github.com/freeplane/freeplane/commit/4ba63c31bb03d71cea479a80e2ee0af97512eaeb) |
| 2023-09-22 | `feature` | Revert "fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` w | `ViewerController.java`, `ExternalObjectProxy.java` | [d79e2179](https://github.com/freeplane/freeplane/commit/d79e21797976fc877a1ba9c28a3f6dd0f26ea916) |
| 2023-09-16 | `fix` | Revert "fix to no longer throw exception when relative image uri is set via script" | `ViewerController.java` | [9c073a9d](https://github.com/freeplane/freeplane/commit/9c073a9d0a584b0150ecb4ebc61f02b2026a1004) |
| 2023-09-16 | `feature` | fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mind | `ViewerController.java`, `ExternalObjectProxy.java` | [02f32e28](https://github.com/freeplane/freeplane/commit/02f32e2872554313c0cfe66ea1918c103600983d) |
| 2023-09-15 | `api_change` | use java 8 api | `MapExplorerController.java` | [a2b97c07](https://github.com/freeplane/freeplane/commit/a2b97c07fc74cfeab5dbfc633f18557afc3fcf92) |
| 2023-09-06 | `fix` | fix to no longer throw exception when relative image uri is set via script | `ViewerController.java` | [09285f57](https://github.com/freeplane/freeplane/commit/09285f57644326bb8c1be54ce2823b87e67d9318) |
| 2023-09-06 | `fix` | fix to no longer throw exception when relative image uri is set via script | `ViewerController.java` | [7be6fa4f](https://github.com/freeplane/freeplane/commit/7be6fa4fa4f7958d8d3c42fd29742784282fea1e) |
| 2023-09-06 | `fix` | fix to no longer throw exception when relative image uri is set via script | `ViewerController.java` | [1896288f](https://github.com/freeplane/freeplane/commit/1896288f86d28e72eb7276dccae7f5cf4b6dc41d) |
| 2023-09-05 | `fix` | fix to no longer throw exception when relative image uri is set via script | `ViewerController.java` | [c5a790c2](https://github.com/freeplane/freeplane/commit/c5a790c2d38efffdee93921d6b253e160a0a1156) |
| 2023-08-19 | `fix` | Issue #1341 Fix index out of bounds exception | `NodeList.java` | [c689e923](https://github.com/freeplane/freeplane/commit/c689e923216007db87e2d5383027519d8cfbaa2a) |
| 2023-08-19 | `feature` | Add time stamps to generated image file names | `TargetFileCreator.java` | [95cc9ba8](https://github.com/freeplane/freeplane/commit/95cc9ba8e462f52327dfa90f8b6f16eab38cdd18) |
| 2023-08-15 | `fix` | fix NPE | `EditNodeTextField.java` | [de48cd25](https://github.com/freeplane/freeplane/commit/de48cd259a4c7fe501e0c1c028f45ce660c9ac86) |
| 2023-08-15 | `fix` | fix class cast exception | `CompareConditionAdapter.java` | [f8daf55e](https://github.com/freeplane/freeplane/commit/f8daf55e47ed7499481e1c3e03b5dbd889a3b211) |
| 2023-08-15 | `fix` | fix NPE | `Slide.java` | [c67a5eff](https://github.com/freeplane/freeplane/commit/c67a5eff8ed8c26ef355618525196428fe194865) |
| 2023-08-15 | `fix` | fix class cast exception | `FilterController.java` | [8eb18eb6](https://github.com/freeplane/freeplane/commit/8eb18eb64de72b9498a1241b1561468b4631d553) |
| 2023-08-12 | `feature` | Issue #1326 1.11.5 changed the behavior of Enter+Paste: For new child nodes paste should g | `MTextController.java` | [1884e10f](https://github.com/freeplane/freeplane/commit/1884e10fcbbb063f85fb1365c7d3579d60ff0b3e) |
| 2023-08-06 | `fix` | Fix NPE | `LayoutController.java` | [658e9854](https://github.com/freeplane/freeplane/commit/658e9854538a8c5f0e000fe6bf859125f6d8662f) |
| 2023-07-23 | `fix` | fix NPE when text is null | `HtmlUtils.java` | [e8748d55](https://github.com/freeplane/freeplane/commit/e8748d55ba50f41c40e1babfcc01908235558919) |
| 2023-07-21 | `feature` | fix htmlToPlain to retain trailing NBSPs; add tests | `HtmlUtils.java`, `HtmlUtilsTest.java` | [b781c08d](https://github.com/freeplane/freeplane/commit/b781c08d51b95d95e97b868e2249319259023183) |
| 2023-07-18 | `feature` | Issue #1303 New highlighters: hotkeys not working | `EditNodeTextField.java` | [d3e25079](https://github.com/freeplane/freeplane/commit/d3e2507952eec533fab9aa211cc3fa8f0428368f) |
| 2023-07-18 | `feature` | Issue #1302 New highlighters: Yellow missing from the Edit node core in dialog menu | `freeplane.properties` | [cf2396bd](https://github.com/freeplane/freeplane/commit/cf2396bd12776cbd2a773ce07f9e400b5b78400a) |
| 2023-07-16 | `feature` | Better support for unknown html tags | `HtmlProcessor.java`, `XHTMLWriter.java` +2 | [ba8061d3](https://github.com/freeplane/freeplane/commit/ba8061d3617ba43ad2f2dec34e38407df4959378) |
| 2023-07-01 | `fix` | Issue #1282 fix parser to accept bad xml created by previous Freeplane versions | `IElementContentHandler.java`, `TreeXmlReader.java` +5 | [38ee9490](https://github.com/freeplane/freeplane/commit/38ee94903441161c6c195492d65c87db5ce5c8f4) |
| 2023-07-01 | `feature` | Revert "Issue #1252 Hot Key Presets Load ends up with old and new action for hot key" | `ActionAcceleratorManager.java` | [510537ba](https://github.com/freeplane/freeplane/commit/510537ba2e392f71178b23b0a31f5166937c5ce9) |
| 2023-06-23 | `feature` | Issue #1252 Hot Key Presets Load ends up with old and new action for hot key | `ActionAcceleratorManager.java` | [65a50d5e](https://github.com/freeplane/freeplane/commit/65a50d5eac6400fba7282ff0b5148d0e03dcffe1) |
| 2023-06-23 | `feature` | support setting any, even not visible node as map root node at any time | `MapView.java`, `NodeViewFactory.java` | [2009cab0](https://github.com/freeplane/freeplane/commit/2009cab0feed369d8a2cbaefb1044b9238964e58) |
| 2023-06-21 | `fix` | fix slides having root nodes previously not visible on the view | `MapView.java` | [4d6d4a49](https://github.com/freeplane/freeplane/commit/4d6d4a49a676a3e6c14706d6c2febed63bea9afa) |
| 2023-06-19 | `fix` | fix ArrayIndexOutOfBoundsException: | `NodeView.java` | [d873d898](https://github.com/freeplane/freeplane/commit/d873d8985e297dd62262f587afe3f64588bd7244) |
| 2023-06-19 | `api_change` | allow non html content in note / detail API proxy | `NoteManager.java`, `TextController.java` +1 | [e1f2ab4d](https://github.com/freeplane/freeplane/commit/e1f2ab4d63a807008dd746af9c24491f718f11d5) |
| 2023-06-18 | `fix` | fix: make sure #at(...) is decoded | `MapExplorerController.java` | [816bbbf8](https://github.com/freeplane/freeplane/commit/816bbbf8ec52d205bc1a160d181f7876e381ceb8) |
| 2023-06-18 | `feature` | Create new map view if required when node is selected by shift + mouse click | `MapController.java` | [d213d3c5](https://github.com/freeplane/freeplane/commit/d213d3c5701fec14c303c738ba10f6c0b62f8a50) |
| 2023-06-18 | `fix` | fix selected nodes: replace selection only after the node views are available | `MapViewChangeObserverCompound.java`, `MapViewController.java` | [8aa4437b](https://github.com/freeplane/freeplane/commit/8aa4437b31807c923b516de8c750684b52bbfe01) |
| 2023-06-18 | `feature` | open new map view on shift + mouse-click on the link | `MapController.java` | [ba9e4937](https://github.com/freeplane/freeplane/commit/ba9e493761b1fcd73d7ec149ce36049072c01105) |
| 2023-06-18 | `feature` | move logic selecting nodes on new map views as on old views from LastOpenedList to MapView | `LastOpenedList.java`, `MapViewController.java` | [80b8f54d](https://github.com/freeplane/freeplane/commit/80b8f54d4635cf1cca19093df7bc5c4f48a73ea1) |
| 2023-06-18 | `feature` | Disable editing of table columns containing line breaks and enable copying | `AttributeSelection.java`, `AttributeClipboardController.java` +1 | [2781b8b5](https://github.com/freeplane/freeplane/commit/2781b8b5c6dadfcb0552dc946545edf97b14a6a8) |
| 2023-06-17 | `fix` | fix the property set to "ask" | `HtmlProcessor.java` | [545daeef](https://github.com/freeplane/freeplane/commit/545daeef64c8a03539484fbda0197b149bb8a957) |
| 2023-06-17 | `feature` | make undo and other menu actions accessible before editing starts when new node is created | `MTextController.java` | [ce3b9757](https://github.com/freeplane/freeplane/commit/ce3b975709072081502add0452ad0178cee99acd) |
| 2023-06-17 | `feature` | fix new attribute table colors | `AttributeTable.java` | [074d7e65](https://github.com/freeplane/freeplane/commit/074d7e65a06897c2c81f8818a46f928ebbfdb215) |
| 2023-06-16 | `fix` | fix keys | `Resources_fr.properties`, `Resources_hr.properties` +4 | [742341f1](https://github.com/freeplane/freeplane/commit/742341f1dc82907a9507cd5cce7fd19d97cb99d7) |
| 2023-06-16 | `feature` | support full html | `Resources_es.properties`, `Resources_pt_PT.properties` +9 | [37cef5ac](https://github.com/freeplane/freeplane/commit/37cef5ac501dbcf5e955f00ebde1cd5f52f60f24) |
| 2023-06-16 | `feature` | Change icons and support explanations in OptionalDontShowMeAgainDialog | `question_msg.svg`, `warning_msg.svg` +1 | [23c0fcbe](https://github.com/freeplane/freeplane/commit/23c0fcbee9704baf3b961f582b647792ca1ac8cd) |
| 2023-06-14 | `feature` | Add option "saveCompactHtml" to translations. | `preferences.xml`, `Resources_en.properties` | [e0951eb3](https://github.com/freeplane/freeplane/commit/e0951eb34c417da3f383ad5fbb96d5dd75ecb043) |
| 2023-06-13 | `fix` | fix slow scrolling | `MapViewScrollPane.java` | [e6855bd7](https://github.com/freeplane/freeplane/commit/e6855bd7928db2ff69b96211acbb38f1b088200f) |
| 2023-06-10 | `fix` | fix applet | `NodeCenter.svg`, `SetLinkByFileChooserAction.svg` +4 | [07a59724](https://github.com/freeplane/freeplane/commit/07a59724a75ef2e99130d3d3343c24a9d4ee7849) |
| 2023-06-10 | `feature` | Issue #1221 Freeplane crashes when executing a script that add new child to a existing lis | `INodeView.java`, `NodeModel.java` +1 | [736ef015](https://github.com/freeplane/freeplane/commit/736ef0151bda04086cd9cb5d042153826b79e4d3) |
| 2023-06-10 | `feature` | Revert "Issue #1221 Freeplane crashes when executing a script that add new child to a exis | `NodeView.java` | [d864a1a7](https://github.com/freeplane/freeplane/commit/d864a1a7dac73b367e17120b50483f6c0444f0bf) |
| 2023-06-10 | `fix` | fix css style update | `MNoteController.java`, `NoteManager.java` +1 | [005afca5](https://github.com/freeplane/freeplane/commit/005afca59e0b920d70cb7a3c827e261389e67cf1) |
| 2023-06-09 | `feature` | Issue #1221 Freeplane crashes when executing a script that add new child to a existing lis | `NodeView.java` | [faa3feeb](https://github.com/freeplane/freeplane/commit/faa3feebf308748291fee7f3399a170aa0129b30) |
| 2023-06-08 | `fix` | Issue #1205 fix saving of plain text content like markdown in details and notes | `IElementContentHandler.java`, `TreeXmlReader.java` +8 | [33475572](https://github.com/freeplane/freeplane/commit/33475572fb1164e480ba787a870119caa1aff9ec) |
| 2023-06-04 | `feature` | use new property key "keepSelectedNodeVisible" and remove old translations | `Resources_cs.properties`, `Resources_de.properties` +23 | [b49d8e81](https://github.com/freeplane/freeplane/commit/b49d8e81913296b722e73853880dde611e87d839) |
| 2023-06-03 | `feature` | Issue #1192 Add "Jump in" and "Jump out" to the toolbar | `mindmapmodemenu.xml` | [8ebcc8b8](https://github.com/freeplane/freeplane/commit/8ebcc8b8ef13bf64a5c376fca6ba022e523badb6) |
| 2023-06-03 | `fix` | fix grammar | `Resources_en.properties` | [0cf00b08](https://github.com/freeplane/freeplane/commit/0cf00b08337ec6a79437ec8425f58359cb29ece8) |
| 2023-06-01 | `fix` | Issue #1191 fix NPE if there are different map views of the same map with different roots  | `NodeView.java` | [dd840cd6](https://github.com/freeplane/freeplane/commit/dd840cd60bca5153d171c47804ea1bfe4e4594ae) |
| 2023-06-01 | `fix` | fix switch between outline view and map view | `MapViewController.java` | [9b80c492](https://github.com/freeplane/freeplane/commit/9b80c49243154f0575a018aeabc89676e6b3bfb3) |
| 2023-05-29 | `feature` | add but toolbar layout option "on every separator" | `ButtonSelectorPanel.java`, `ToolbarLayout.java` +1 | [8b24192d](https://github.com/freeplane/freeplane/commit/8b24192d0b9afa30122a4e5367e8a515d1171be6) |
| 2023-05-28 | `fix` | fix jump-in | `NodeView.java` | [bbbcdf92](https://github.com/freeplane/freeplane/commit/bbbcdf9225f968cfc8181d397b3eca9d31573faa) |
| 2023-05-28 | `fix` | fix NPE | `MLayoutController.java` | [20deea98](https://github.com/freeplane/freeplane/commit/20deea981badeb7f9bea0686572c45bfcbee0e6b) |
| 2023-05-27 | `fix` | fix NPE | `RichTextModel.java` | [49094ee2](https://github.com/freeplane/freeplane/commit/49094ee2d0ea1a909e9d292bfe83ec9c0afe8e7e) |
| 2023-05-26 | `feature` | support setting of double properties | `ResourceController.java`, `FreeplaneScriptBaseClass.java` | [f554850b](https://github.com/freeplane/freeplane/commit/f554850bf7d852ca848a98f7dd0e14f53506b6e8) |
| 2023-05-23 | `fix` | dialog was hidden just after it was shown, fix attempt. | `ButtonSelectorPanel.java` | [68a211ee](https://github.com/freeplane/freeplane/commit/68a211eea1ef1762c651146fc5581f22864d0339) |
| 2023-05-23 | `feature` | Add layout button to toolbars, fix style toolbar | `mindmapmodemenu.xml`, `stylemodemenu.xml` +9 | [4e33c4e9](https://github.com/freeplane/freeplane/commit/4e33c4e9f120583b46609f47f69da49f4307cf0d) |
| 2023-05-21 | `fix` | fix note change detection | `MNoteController.java`, `RichTextModel.java` | [721e0580](https://github.com/freeplane/freeplane/commit/721e0580bc6a93fec75c7a111e66b7a1f90d1122) |
| 2023-05-13 | `feature` | Add node API methods getBranchAsTextOutline and appendTextOutlineAsBranch | `MapClipboardController.java`, `MindMapPlainTextWriter.java` +4 | [023d7d9d](https://github.com/freeplane/freeplane/commit/023d7d9de5adcccd492e2f2b3c0f1c14b29d9f95) |
| 2023-05-12 | `feature` | Add latest features map to the help menu | `mindmapmodemenu.xml`, `HelpController.java` +1 | [a8a70a25](https://github.com/freeplane/freeplane/commit/a8a70a2500ce4fceb04ac0d9269891f244eb6e3a) |
| 2023-05-12 | `feature` | Add menu action to select children nodes layout | `mindmapmodemenu.xml`, `stylemodemenu.xml` +5 | [e3beb8b9](https://github.com/freeplane/freeplane/commit/e3beb8b939ca393157af76145c9a6a594290f5fb) |
| 2023-05-07 | `fix` | fix NPE | `MapView.java` | [391ff454](https://github.com/freeplane/freeplane/commit/391ff45436b85d2b1090c7ca9ab61340eff1e227) |
| 2023-05-06 | `fix` | fix NPE and folding if node outside jump-in is shown | `MapView.java`, `NodeView.java` | [c896fa91](https://github.com/freeplane/freeplane/commit/c896fa913a11374667d315a13eb85064b3422c76) |
| 2023-04-29 | `fix` | fix button panel preferred height | `ToolbarLayout.java` | [7386ea66](https://github.com/freeplane/freeplane/commit/7386ea661f1d556b8ee49b298f4eacf467c7c2e0) |
| 2023-04-28 | `fix` | fix regex in icon selection | `IconSelectionPopupDialog.java` | [1b011b96](https://github.com/freeplane/freeplane/commit/1b011b967a570aa5b127d69b00e06b8416fed487) |
| 2023-04-28 | `fix` | fix select all after jump in | `SelectAllAction.java` | [460693ce](https://github.com/freeplane/freeplane/commit/460693ce643ed7cde60bf6fd64d15f225880743d) |
| 2023-04-28 | `fix` | fix java.util.ConcurrentModificationException | `StyleSheetConfigurer.java` | [5956287a](https://github.com/freeplane/freeplane/commit/5956287aab60a40e09fe45eccadaf4f34075ac64) |
| 2023-04-28 | `fix` | fix NPE | `MFileManager.java` | [de606008](https://github.com/freeplane/freeplane/commit/de60600800778353ad6a36b4949f00153d12f1e0) |
| 2023-04-28 | `fix` | fix NPE | `NodeView.java` | [a043816a](https://github.com/freeplane/freeplane/commit/a043816a8477552e402f173af6d981478eba1c87) |
| 2023-04-28 | `fix` | fix NPE | `IconSelectionPopupDialog.java` | [d8ae0e71](https://github.com/freeplane/freeplane/commit/d8ae0e7198394e77760916f1c0e5f7355b92da45) |
| 2023-04-28 | `fix` | fix division by zero | `NodeView.java` | [160cde97](https://github.com/freeplane/freeplane/commit/160cde97035728a6a4a493559c925ffebad18e51) |
| 2023-04-28 | `fix` | fix NPE | `MapViewController.java` | [6245b78e](https://github.com/freeplane/freeplane/commit/6245b78ed5974ff4f2300d9375fc5e9d15a896f3) |
| 2023-04-28 | `fix` | fix java.lang.AssertionError: select invisible node | `NodeView.java` | [46edb882](https://github.com/freeplane/freeplane/commit/46edb88294352f409c7064b9d8790d462f47cec6) |
| 2023-04-28 | `fix` | fix NPE | `FilterController.java` | [07112708](https://github.com/freeplane/freeplane/commit/07112708fa5141f8e7588493651235ce540a133d) |
| 2023-04-28 | `fix` | fix priority list | `PriorityConditionController.java` | [e830666c](https://github.com/freeplane/freeplane/commit/e830666cbc6dbddaec1824dbde07c52ec72f3df0) |
| 2023-04-28 | `fix` | fix error reporting on mac | `LogUtils.java` | [531c2242](https://github.com/freeplane/freeplane/commit/531c22422400c531abf7e2529066c1fbbcdd1997) |
| 2023-04-22 | `fix` | fix AccessControlException (the node accessing external resource was folded or unfolded fr | `NodeModel.java` | [3e021e2f](https://github.com/freeplane/freeplane/commit/3e021e2f7a075351817ebc96e2a3b0655e11cb8c) |
| 2023-04-21 | `fix` | fix navigation to opposite side for nodes with hidden parents | `MapView.java` | [dedff18e](https://github.com/freeplane/freeplane/commit/dedff18e538cce3d0b4a033bef3f6fec71609335) |
| 2023-04-21 | `feature` | add "flow" layouts | `auto_flow.svg`, `lefttoright_bothsides_flow.svg` +10 | [13d6b37e](https://github.com/freeplane/freeplane/commit/13d6b37effc63fb2bb413f1f7458338e279fec81) |
| 2023-04-21 | `fix` | fix navigation | `MapView.java` | [8e93834a](https://github.com/freeplane/freeplane/commit/8e93834a5d44f53f9f92e2112456ce943769522c) |
| 2023-04-14 | `feature` | Add Latvian and fix Lithuanian language | `Resources_lv.properties`, `freeplane.properties` +1 | [effafc87](https://github.com/freeplane/freeplane/commit/effafc87386af49a8596fcdc4aac5664407d2b07) |
| 2023-04-10 | `api_change` | rename flag (API!) to isStacked | `MainView.java`, `MapView.java` +5 | [996d934d](https://github.com/freeplane/freeplane/commit/996d934d65e2fe718c087885589af965403fe7d7) |
| 2023-04-07 | `fix` | Issue #1075 Layouts Combinations Display Bug | `VerticalNodeViewLayoutStrategy.java` | [3686eaba](https://github.com/freeplane/freeplane/commit/3686eaba0bd754a52aef9d9c7b8cffabf3a6f2bc) |
| 2023-03-18 | `fix` | fix navigation to parent | `MapView.java` | [1c0bd6cf](https://github.com/freeplane/freeplane/commit/1c0bd6cf63871056c1539b2a646c75009c35043f) |
| 2023-03-17 | `fix` | wip fix navigation on filtered maps | `MapView.java`, `NodeView.java` | [b31da851](https://github.com/freeplane/freeplane/commit/b31da851c3b2de68cdcc1e58c3532f2665ca6863) |
| 2023-03-12 | `fix` | fix navigation to summary nodes | `NodeView.java` | [3dce25c0](https://github.com/freeplane/freeplane/commit/3dce25c056c595fbc796711649ff25b12d6e8fb4) |
| 2023-03-04 | `fix` | Fix save directory initialization on start | `MFileManager.java` | [142d1df3](https://github.com/freeplane/freeplane/commit/142d1df3b0e87b9c02d480802b2563eb89dc4eb7) |
| 2023-03-03 | `fix` | fix navigation to summary nodes | `MapView.java` | [a1df16df](https://github.com/freeplane/freeplane/commit/a1df16df89f31b0c5ffe94db24b5f77cc74f9814) |
| 2023-02-24 | `fix` | fix continuous selection | `MapView.java` | [f84e0e6d](https://github.com/freeplane/freeplane/commit/f84e0e6dc6332ed3632ca200a6df8e8a7cff9eb6) |
| 2023-02-18 | `fix` | fix horizontal layout | `VerticalNodeViewLayoutStrategy.java` | [fa0a4891](https://github.com/freeplane/freeplane/commit/fa0a48913c3925e4c6af3eb67f06ce327b60da48) |
| 2023-02-18 | `fix` | fix layout for nodes with hidden content and subtrees | `NodeViewLayoutHelper.java`, `VerticalNodeViewLayoutStrategy.java` | [d8cce824](https://github.com/freeplane/freeplane/commit/d8cce824b2b1c4e40b73a5adfb74ba892487d428) |
| 2023-02-10 | `fix` | Fix "as parent" formatting properties for jump in | `NodeView.java` | [96d5a66b](https://github.com/freeplane/freeplane/commit/96d5a66b208c928f3c8bae4d9866ee63820cb413) |
| 2023-02-04 | `fix` | fix filter | `Filter.java` | [182d8cd7](https://github.com/freeplane/freeplane/commit/182d8cd7ab615fc172966c75bb0b06c8dff0ce63) |
| 2023-02-02 | `feature` | update flatlaf and add macos specific flat laf | `build.gradle`, `MModeController.java` | [eef8db9f](https://github.com/freeplane/freeplane/commit/eef8db9f15c13dc2b72984168130e39b9859c8ee) |
| 2023-02-02 | `feature` | Issue #511 Tab inserts 4 spaces when editing node text inline and I think it should insert | `FreeplaneMenuBar.java`, `EditNodeTextField.java` | [8670445c](https://github.com/freeplane/freeplane/commit/8670445c300ae0c78462f695310c01e6b51e3c1c) |
| 2023-01-24 | `feature` | Add layouts aligning parent with first or last child | `auto_first.svg`, `auto_last.svg` +25 | [c5a40916](https://github.com/freeplane/freeplane/commit/c5a409164a27926bc13f02e4c68b347a4f62ff8a) |
| 2023-01-20 | `fix` | fix icons | `auto.svg`, `auto_centered.svg` +3 | [1faf1374](https://github.com/freeplane/freeplane/commit/1faf137430f04c361298b512da3d910b92669f9c) |
| 2023-01-20 | `feature` | Issue #918 Add toolbar icons for text alignment | `mindmapmodemenu.xml` | [5c03fa82](https://github.com/freeplane/freeplane/commit/5c03fa82b19a51c49522f367dc696d935ec6ff17) |
| 2023-01-15 | `fix` | fix children side calculation when explicitly set | `NodeView.java` | [79fb6224](https://github.com/freeplane/freeplane/commit/79fb622487655dbac7d0d95a3cc6c0921b3d67d7) |
| 2023-01-15 | `fix` | fix NPE | `MNodeMotionListener.java` | [b1ee99cd](https://github.com/freeplane/freeplane/commit/b1ee99cd4ace1c1e550b4ca2c8dabe6b5918d133) |
| 2023-01-14 | `fix` | Fix children sides for auto layout cases | `ExportBranchAction.java`, `MainView.java` +4 | [839ddcf8](https://github.com/freeplane/freeplane/commit/839ddcf8581f7c9271964c9c76afc6a784168bef) |
| 2023-01-08 | `fix` | fix copying of child nodes layout | `MLayoutController.java` | [2d89c5da](https://github.com/freeplane/freeplane/commit/2d89c5da51eac7994b4148ca7410f972cf5ec3fd) |
| 2023-01-06 | `fix` | fix border width when like edge | `MainView.java` | [44e7a68f](https://github.com/freeplane/freeplane/commit/44e7a68f04c76d841b5d2d15bcd38ef987e8d477) |
| 2023-01-03 | `fix` | Fix cloud position around free nodes | `VerticalNodeViewLayoutStrategy.java` | [1119e931](https://github.com/freeplane/freeplane/commit/1119e9312f83b1fede5206af58a6e9f03ba36d0a) |

### Dettagli commit con note

**[d2e34dff](https://github.com/freeplane/freeplane/commit/d2e34dffa77228141d2fb1992fd1af66c20dfaf4)** (2023-11-26) — Adding new nodes linked to menu commands (#1543)

> * NewNodeLinkedToMenuItemOnNextClickAction
> 
> * Menu stays open when using dialog
> 
> to insert multiple nodes
> 
> * Adds missing text resources (bug)
> 
> * make the new action more consistent with existing actions
> 
> * making Menu to stay open when adding new nodes
> 
> * revert unrelated change
> 
> * remove comment
> 
> * make button text on cancel dialog configurable
> 
> * Define text string "done" copied from simplyhtml.done
> 
> * show "done" instead of "cancel", improve action name and dialog message
> 
> * show new nodes
> 
> * FP fix navigation to siblings: root can't be a sibling
> 
> * Revert "revert unrelated change"
> 
> This reverts commit bee3ad687595c4cb45acc7112391b229f23c50d4.
> 
> * Clarify the purpose by creating a dedicated method
> 
> ---------
> 
> Co-authored-by: Dimitry Polivaev <dpolivaev@gmx.de>
> Co-authored-by: Dimitry Polivaev <dimitry.polivaev@unite.eu>

**[3012c623](https://github.com/freeplane/freeplane/commit/3012c623bb547f227903c5bcefc8008aaa51c831)** (2023-11-08) — Implement node ordering based on weakly connected components

> - Change node ordering logic to group by weakly connected components
> instead of strongly connected components.
> - Sort weakly connected components by size before cycle-breaking and
> ordering.
> - Update ordering algorithm to accommodate connectedness without
> considering directionality.

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

**[d96fb632](https://github.com/freeplane/freeplane/commit/d96fb632d4b15830887b05ec40184c7c03e8cc3f)** (2023-10-15) — Rename tabs (#1353)

> * added Rename Tab PopupMenu
> 
> * Update MapViewDockingWindows.java
> 
> added missing imports
> 
> * Added TextUtils.getText to Tabs PopupMenu
> 
> * Update MapViewDockingWindows.java
> 
> * popup to not appear for not visible windows
> 
> * Update MapViewDockingWindows.java
> 
> not tested yet. Changed directly in Github repository.
> 
> * Update MapViewDockingWindows.java
> 
> trying to solve an error
> 
> * Adding renaming PopupMenu to single windows
> 
> * simplify, remove duplication
> 
> * Corrects Typos
> 
> - Corrects typo "loadingLayoutFromObjectInputStream"
> 
> * Reorders lines to optimize code
> 
> Reorders lines to optimize code to method updateTitle:
> - it only creates a title if it can get the containing docked window
> 
> * Loads current Tab name as predefined string
> 
> Loads current  Tab name to inputDialog as predefined string
> 
> * Enables grouped windows tabs to be renamed
> 
> Tabs that have multiple childwindows can also be renamed (temporarily)
> 
> * Enables loading from Custom Tab Names
> 
> Enables loading from previous Custom Tab Names when (re)starting Freeplane
> 
> * corrects bug:  mapsMenuAction not working
> 
> * Corrects loading from tab names with asterik
> 
> When unsaved maps get saved when closing Freeplane, their names are saved with asterisk (dirty) in the properties file.
> 
> * Replace CustomWindowTitleProvider class by method reference
> 
> * remove word "temporary" from rename tab popup menu and dialog title
> 
> ---------
> 
> Co-authored-by: EdoFro <35700575+EdoFro@users.noreply.github.com>

**[793a72d1](https://github.com/freeplane/freeplane/commit/793a72d1ed8834b9a6a3cf76e3e31a7669df3995)** (2023-10-09) — Fix NPE

> Issue #1442 FP 1.11.8: Changing "Automatic Level Styles" or "Automatic edge Color" raises error if Note Panel has never been shown in current session

**[d79e2179](https://github.com/freeplane/freeplane/commit/d79e21797976fc877a1ba9c28a3f6dd0f26ea916)** (2023-09-22) — Revert "fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mindMap isn't saved and `OptionPanel.links == "relative"`"

> This reverts commit 02f32e2872554313c0cfe66ea1918c103600983d.

**[9c073a9d](https://github.com/freeplane/freeplane/commit/9c073a9d0a584b0150ecb4ebc61f02b2026a1004)** (2023-09-16) — Revert "fix to no longer throw exception when relative image uri is set via script"

> This reverts commit c5a790c2d38efffdee93921d6b253e160a0a1156, 1896288f86d28e72eb7276dccae7f5cf4b6dc41d, 7be6fa4fa4f7958d8d3c42fd29742784282fea1e, 09285f57644326bb8c1be54ce2823b87e67d9318.

**[02f32e28](https://github.com/freeplane/freeplane/commit/02f32e2872554313c0cfe66ea1918c103600983d)** (2023-09-16) — fix to no longer fail on `node.externalObject.uri = URI.create('relative/path')` when mindMap isn't saved and `OptionPanel.links == "relative"`

> by bypassing URI checks via the extracted setExternalResource; the fix is needed for the PackAndGoGo add-on

**[09285f57](https://github.com/freeplane/freeplane/commit/09285f57644326bb8c1be54ce2823b87e67d9318)** (2023-09-06) — fix to no longer throw exception when relative image uri is set via script

> go back to `uri` set by User, because getCanonicalFile not only removes `../` but also follows symbolic links, and that might be undesired by User

**[7be6fa4f](https://github.com/freeplane/freeplane/commit/7be6fa4fa4f7958d8d3c42fd29742784282fea1e)** (2023-09-06) — fix to no longer throw exception when relative image uri is set via script

> fix NPE when map not saved

**[1896288f](https://github.com/freeplane/freeplane/commit/1896288f86d28e72eb7276dccae7f5cf4b6dc41d)** (2023-09-06) — fix to no longer throw exception when relative image uri is set via script

> make sure to operate on an absolute file and use canonical file for LINK_ABSOLUTE

**[c5a790c2](https://github.com/freeplane/freeplane/commit/c5a790c2d38efffdee93921d6b253e160a0a1156)** (2023-09-05) — fix to no longer throw exception when relative image uri is set via script

> (relative image was introduced in #1142)

**[f8daf55e](https://github.com/freeplane/freeplane/commit/f8daf55e47ed7499481e1c3e03b5dbd889a3b211)** (2023-08-15) — fix class cast exception

> java.lang.ClassCastException: class java.lang.Double cannot be cast to class java.lang.Long (java.lang.Double and java.lang.Long are in module java.base of loader 'bootstrap')
> 	at org.freeplane.features.filter.condition.CompareConditionAdapter.compareTo(CompareConditionAdapter.java:167)
> 	at org.freeplane.features.filter.condition.CompareConditionAdapter.compareToData(CompareConditionAdapter.java:124)
> 	at org.freeplane.features.filter.condition.CompareConditionAdapter.compareTo(CompareConditionAdapter.java:110)

**[8eb18eb6](https://github.com/freeplane/freeplane/commit/8eb18eb64de72b9498a1241b1561468b4631d553)** (2023-08-15) — fix class cast exception

> Exception in thread "AWT-EventQueue-0"
> java.lang.ClassCastException: class org.freeplane.features.presentations.mindmapmode.Slide$$Lambda$729/0x000000010060d1b8 cannot be cast to class org.freeplane.features.filter.condition.ASelectableCondition (org.freeplane.features.presentations.mindmapmode.Slide$$Lambda$729/0x000000010060d1b8 and org.freeplane.features.filter.condition.ASelectableCondition are in unnamed module of loader org.knopflerfish.framework.BundleClassLoader @56f25f5d)
> 	at org.freeplane.features.filter.FilterController.getSelectedCondition(FilterController.java:713)
> 	at org.freeplane.features.filter.FilterController.isFilterActive(FilterController.java:949)
> 	at org.freeplane.features.filter.FilterController.updateSettingsFromFilter(FilterController.java:842)
> 	at org.freeplane.features.filter.FilterController.updateUI(FilterController.java:385)
> 	at org.freeplane.features.filter.FilterController.access$400(FilterController.java:110)
> 	at org.freeplane.features.filter.FilterController$3.run(FilterController.java:372)
> 	at java.desktop/java.awt.event.InvocationEvent.dispatch(InvocationEvent.java:318)

**[e8748d55](https://github.com/freeplane/freeplane/commit/e8748d55ba50f41c40e1babfcc01908235558919)** (2023-07-23) — fix NPE when text is null

> Exception in thread "AWT-EventQueue-0" java.lang.NullPointerException: Cannot invoke "String.equals(Object)" because "threadLocalCachedHtmlToPlain.input" is null
> 	at org.freeplane.core.util.HtmlUtils.htmlToPlain(HtmlUtils.java:116)

**[b781c08d](https://github.com/freeplane/freeplane/commit/b781c08d51b95d95e97b868e2249319259023183)** (2023-07-21) — fix htmlToPlain to retain trailing NBSPs; add tests

> so that trailing spaces (nbsp) are respected, which is one of the methods to indicate a hard line break in markdown

**[510537ba](https://github.com/freeplane/freeplane/commit/510537ba2e392f71178b23b0a31f5166937c5ce9)** (2023-07-01) — Revert "Issue #1252 Hot Key Presets Load ends up with old and new action for hot key"

> This reverts commit 65a50d5eac6400fba7282ff0b5148d0e03dcffe1.

**[816bbbf8](https://github.com/freeplane/freeplane/commit/816bbbf8ec52d205bc1a160d181f7876e381ceb8)** (2023-06-18) — fix: make sure #at(...) is decoded

> this fixes the issue that special characters like spaces make the at-path invalid

**[80b8f54d](https://github.com/freeplane/freeplane/commit/80b8f54d4635cf1cca19093df7bc5c4f48a73ea1)** (2023-06-18) — move logic selecting nodes on new map views as on old views from LastOpenedList to MapViewController

> it  helps the selection to happen earlier

**[d864a1a7](https://github.com/freeplane/freeplane/commit/d864a1a7dac73b367e17120b50483f6c0444f0bf)** (2023-06-10) — Revert "Issue #1221 Freeplane crashes when executing a script that add new child to a existing list of children, then delete it)"

> This reverts commit faa3feebf308748291fee7f3399a170aa0129b30.

**[5956287a](https://github.com/freeplane/freeplane/commit/5956287aab60a40e09fe45eccadaf4f34075ac64)** (2023-04-28) — fix java.util.ConcurrentModificationException

> at java.base/java.util.LinkedHashMap$LinkedHashIterator.nextNode(Unknown Source)
> 
> 	at java.base/java.util.LinkedHashMap$LinkedKeyIterator.next(Unknown Source)
> 
> 	at java.base/java.util.Collections$3.nextElement(Unknown Source)
> 
> 	at org.freeplane.core.ui.components.html.StyleSheetConfigurer.resetStyles(StyleSheetConfigurer.java:12)
> 
> 	at org.freeplane.features.note.mindmapmode.NotePanel.updateStyleSheet(NotePanel.java:321)
> 
> 	at org.freeplane.features.note.mindmapmode.MNoteController.setDefaultStyle(MNoteController.java:300)
> 
> 	at org.freeplane.features.note.mindmapmode.NoteManager.updateEditor(NoteManager.java:111)
> 
> 	at org.freeplane.features.note.mindmapmode.NoteManager.onSelect(NoteManager.java:63)
> 
> 	at org.freeplane.features.mode.SelectionController.onSelect(SelectionController.java:64)

**[46edb882](https://github.com/freeplane/freeplane/commit/46edb88294352f409c7064b9d8790d462f47cec6)** (2023-04-28) — fix java.lang.AssertionError: select invisible node

> at org.freeplane.view.swing.map.MapView.selectAsTheOnlyOneSelected(MapView.java:2081)
> 
> 	at org.freeplane.view.swing.map.MapView.selectIfSelectionIsEmpty(MapView.java:2350)
> 
> 	at org.freeplane.view.swing.map.NodeView.setFolded(NodeView.java:981)
> 
> 	at org.freeplane.view.swing.map.NodeView.nodeChanged(NodeView.java:933)

**[839ddcf8](https://github.com/freeplane/freeplane/commit/839ddcf8581f7c9271964c9c76afc6a784168bef)** (2023-01-14) — Fix children sides for auto layout cases

> Issue #940 Regression: Impossible to drop as child


---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-12-11 | `feature` | implement callDelayedRefresh | `MapController.java`, `LogicalStyleController.java` +4 | [497a49bd](https://github.com/freeplane/freeplane/commit/497a49bd27813ea9bcab5f005115b6d217fe506d) |
| 2022-12-08 | `fix` | fix node drag and drop | `MNodeMotionListener.java` | [bc00c8a6](https://github.com/freeplane/freeplane/commit/bc00c8a687b71fcfdac7c2f8d67a21fff33c11d9) |
| 2022-12-07 | `fix` | fix StringIndexOutOfBoundsException | `MMapClipboardController.java` | [3e6a1230](https://github.com/freeplane/freeplane/commit/3e6a1230ca958fab95cb83264fd638479f278426) |
| 2022-12-07 | `fix` | fix StringIndexOutOfBoundsException | `MMapClipboardController.java` | [6f93354a](https://github.com/freeplane/freeplane/commit/6f93354ab55ff3d52a26cfc9b2d2dd21ccb27c35) |
| 2022-12-06 | `feature` | implement base distance to child nodes | `LocationBuilder.java`, `LocationController.java` +15 | [06614fd5](https://github.com/freeplane/freeplane/commit/06614fd5dfa0721230b09c7fa1f49c63a0ea4c36) |
| 2022-12-02 | `fix` | fix continuous selection | `MapView.java` | [97631936](https://github.com/freeplane/freeplane/commit/976319364e950aa1ba16956eb43f9a716a24dc28) |
| 2022-11-27 | `feature` | simplify move logic; add set* with table.fire* | `ConditionalStyleModel.java` | [7d3e7909](https://github.com/freeplane/freeplane/commit/7d3e790934f8a4fc9244f5eabad360a0deadc74f) |
| 2022-11-26 | `fix` | fix NPE | `MapView.java` | [775909c7](https://github.com/freeplane/freeplane/commit/775909c7dc9553061f72a74256864f56d0256124) |
| 2022-11-26 | `feature` | Adjust icons to reflect new compact layouts and rename them | `lefttoright_bothsides_left.svg`, `lefttoright_bothsides_right.svg` +10 | [2c100add](https://github.com/freeplane/freeplane/commit/2c100add7db69998424d42a5d860df24fa263890) |
| 2022-11-26 | `fix` | fix layout with filters | `NodeViewLayoutHelper.java` | [34049a87](https://github.com/freeplane/freeplane/commit/34049a8785b052956bfb2f272c01c7b7a9949cde) |
| 2022-11-24 | `feature` | Issue  #843 conditional formating script filter rules are not applied to the new node. | `ComparableByPriority.java`, `IMapChangeListener.java` +5 | [8f17ede4](https://github.com/freeplane/freeplane/commit/8f17ede4e786720796ad7c4feafb8d5dd97072c1) |
| 2022-11-20 | `fix` | fix Y layout for ParentNodeAlignment BEFORE_FIRST_CHILD and AFTER_LAST_CHILD | `VerticalNodeViewLayoutStrategy.java` | [5cfd2ca6](https://github.com/freeplane/freeplane/commit/5cfd2ca6903a5a7ee815386cd2a92b0e8d790e36) |
| 2022-11-19 | `feature` | add new parent node alignments and consider them in layout for Y axis | `VerticalNodeViewLayoutStrategy.java`, `ParentNodeAlignment.java` | [552ee58c](https://github.com/freeplane/freeplane/commit/552ee58cc20dc1441c367fba73fe8cce915a0b85) |
| 2022-11-19 | `fix` | fix layout | `VerticalNodeViewLayoutStrategy.java` | [0a5765cf](https://github.com/freeplane/freeplane/commit/0a5765cfbff9d84976d3853f0ce76cdd451c5e7a) |
| 2022-11-14 | `fix` | fix NPE | `NodeModel.java` | [dddfd016](https://github.com/freeplane/freeplane/commit/dddfd016260c19f4ca21b9d6fc59147d24059911) |
| 2022-11-11 | `fix` | fix tests | `LayoutController.java`, `SummaryLevelsShould.java` +1 | [d4aa92eb](https://github.com/freeplane/freeplane/commit/d4aa92eb6193b214ac19e8bd64d2d323279924df) |
| 2022-11-11 | `fix` | fix layout | `NodeView.java` | [68cccb18](https://github.com/freeplane/freeplane/commit/68cccb18cd4819b283361da48d6493389bd9fcde) |
| 2022-11-11 | `feature` | Add tool tips to node layouts | `ButtonPanelProperty.java`, `ChildNodesLayoutControlGroup.java` +2 | [f8c5d6ce](https://github.com/freeplane/freeplane/commit/f8c5d6ce28cb138ebdac48975a0c8d9c4f69e10d) |
| 2022-11-11 | `feature` | Add layouts AUTO_BYFIRST, AUTO_CENTERED and AUTO_BYLAST | `auto_byfirst.svg`, `auto_bylast.svg` +3 | [9b094340](https://github.com/freeplane/freeplane/commit/9b094340611ef8ece977808789803ea351738155) |
| 2022-11-05 | `feature` | rename some layout enum elements and add gear symbol to some SVGs | `lefttoright_bothsides_auto.svg`, `lefttoright_bottom_auto.svg` +10 | [495d08fb](https://github.com/freeplane/freeplane/commit/495d08fba7c82d490f9a066c803dfcdf8b1c0027) |
| 2022-11-04 | `feature` | wip replace old three enums by the new one | `LayoutBuilder.java`, `LayoutController.java` +16 | [598bd606](https://github.com/freeplane/freeplane/commit/598bd606c85e6d1488e499dcc3bc86c622479b66) |
| 2022-11-04 | `feature` | Add ChildNodesLayout enum and svg files | `auto.svg`, `lefttoright_bothsides_byownside.svg` +25 | [5dbc7713](https://github.com/freeplane/freeplane/commit/5dbc7713d5bfaf58c0b494b57753186f299c0718) |
| 2022-11-04 | `fix` | rename method, fix typo | `NodeView.java` | [aecc17d8](https://github.com/freeplane/freeplane/commit/aecc17d819c3fc50ad661d70484bcf91ae865fad) |
| 2022-11-03 | `fix` | fix isInFoldingRegion | `MainView.java` | [d9838229](https://github.com/freeplane/freeplane/commit/d9838229a102d64a7ced0c4fac4e3a570ca8b136) |
| 2022-11-03 | `fix` | fix NodeViewLayoutHelper.getContentHeight | `NodeViewLayoutHelper.java` | [2073614a](https://github.com/freeplane/freeplane/commit/2073614a7df8c49aefb98c709362b2dfaf7cc2ed) |
| 2022-10-31 | `fix` | Fix node order when pasted as first child | `MMapController.java`, `MMapClipboardController.java` | [dc6083d6](https://github.com/freeplane/freeplane/commit/dc6083d6dbeaa3be58ca54c9f307665d8503eab4) |
| 2022-10-30 | `feature` | add ConditionalStyles-related api | `ConditionalStyleModel.java`, `LogicalStyleController.java` +21 | [61f92526](https://github.com/freeplane/freeplane/commit/61f9252654b98faee1433e98a562c3b43392d016) |
| 2022-10-29 | `fix` | fix NPE | `FindAction.java` | [31624ce6](https://github.com/freeplane/freeplane/commit/31624ce6a6c53008230f1b5df42f9ad46ca6c905) |
| 2022-10-29 | `fix` | fix NPE | `ReminderExtension.java` | [04932c4f](https://github.com/freeplane/freeplane/commit/04932c4fc1a3ed38426936afff86f0d1e8a4c7c9) |
| 2022-10-29 | `feature` | add space to error message | `TreeXmlReader.java` | [f3cce33f](https://github.com/freeplane/freeplane/commit/f3cce33f2844508873c66cfc81bc6829e2d7d1a5) |
| 2022-10-28 | `fix` | fix NPE | `FindAction.java` | [aec33c40](https://github.com/freeplane/freeplane/commit/aec33c405ae65de2f5a51c0f1753e6739feb76e0) |
| 2022-10-23 | `fix` | fix dragging rectangle and folding mark sides | `MainView.java`, `MainViewPainter.java` +1 | [2fb75216](https://github.com/freeplane/freeplane/commit/2fb75216845f49a7b055bad6d87a6c05047077c6) |
| 2022-10-23 | `fix` | fix summary painter | `NodeView.java` | [d4e6cee9](https://github.com/freeplane/freeplane/commit/d4e6cee9f2c5b6568d63c91552ba6efdeb984506) |
| 2022-10-21 | `fix` | fix summary edges for both side layouts | `NodeView.java` | [36896567](https://github.com/freeplane/freeplane/commit/36896567d93c10389eb0e426e03c3f3bf60462fc) |
| 2022-10-21 | `fix` | fix: allow both sides | `NodeModel.java` | [d50ee987](https://github.com/freeplane/freeplane/commit/d50ee9876af417441a72aa793ca343ded92a7f6e) |
| 2022-10-20 | `fix` | fix colors and base URL for note panel | `NoteManager.java` | [0f368d5b](https://github.com/freeplane/freeplane/commit/0f368d5b3d80c4ef99d451f6a61a29be4b0f984a) |
| 2022-10-20 | `feature` | fix autosave for new mind maps | `DoAutomaticSave.java` | [5ba4e299](https://github.com/freeplane/freeplane/commit/5ba4e2997cddba44dc7c74b79e783f0c8324d951) |
| 2022-10-16 | `fix` | fix navigation in outline view | `MapView.java` | [3d969962](https://github.com/freeplane/freeplane/commit/3d9699626355198e354a4c356ecec9ba498c4861) |
| 2022-10-15 | `fix` | fix writer | `LayoutBuilder.java` | [0679cc2c](https://github.com/freeplane/freeplane/commit/0679cc2ce526b4ebf1e11c385b4d3cc7c5b1d064) |
| 2022-10-15 | `feature` | Support both sides for non root nodes | `LayoutController.java`, `NodeModel.java` +2 | [b76ecc9a](https://github.com/freeplane/freeplane/commit/b76ecc9a19541baa2925d6ae6b4845eefc2c8ce0) |
| 2022-10-09 | `feature` | Implement layout model and controllers | `LayoutBuilder.java`, `LayoutController.java` +23 | [4f2aef94](https://github.com/freeplane/freeplane/commit/4f2aef9423a4ae60c225b7609bfb56f99a4ad69a) |
| 2022-10-09 | `fix` | fix node builder: interpret old side names | `NodeBuilder.java` | [96011955](https://github.com/freeplane/freeplane/commit/96011955c8acaefd5d3664c09c63e463b545c9f9) |
| 2022-10-09 | `api_change` | Change API to reflect both possible layout directions | `ConnectorProperties.java`, `NodeModel.java` +31 | [60010ce9](https://github.com/freeplane/freeplane/commit/60010ce96cc296de07b7740decf83887066cd901) |
| 2022-10-03 | `feature` | Issue #703 The setting "Place new branches" (being set to "First") should affect more than | `MMapController.java`, `MMapClipboardController.java` +4 | [f104a4a7](https://github.com/freeplane/freeplane/commit/f104a4a72ff76252bebb1d71a725e74fbcfd707a) |
| 2022-09-30 | `feature` | #700 add insertConditionalStyle | `MLogicalStyleController.java` | [d2fd7098](https://github.com/freeplane/freeplane/commit/d2fd709880e118484537cc24b28f141a42776b6b) |
| 2022-09-30 | `feature` | support horizontal layout in horizontal edge view | `HorizontalEdgeView.java` | [31663923](https://github.com/freeplane/freeplane/commit/31663923e87f3944b36b112a4d248bd40cce161a) |
| 2022-09-30 | `fix` | fix interface change after merge | `VerticalNodeViewLayoutStrategy.java` | [49072eb4](https://github.com/freeplane/freeplane/commit/49072eb427238a715f6a40f02cf095fbf626cfd5) |
| 2022-09-29 | `fix` | fix access permission | `LinkDecorationConfig.java` | [21fb77c6](https://github.com/freeplane/freeplane/commit/21fb77c6288d744569bfc7a2622d551aa61a38f2) |
| 2022-09-27 | `feature` | Issue  #694 "Assigns node dependant styles to new connectors" works only for menu actions  | `AddConnectorAction.java`, `MLinkController.java` | [47d01a99](https://github.com/freeplane/freeplane/commit/47d01a99b639351d16bd47e194ea30dafee1ef7d) |
| 2022-09-25 | `feature` | add delegate method | `NodeView.java`, `NodeViewLayoutHelper.java` | [849d671e](https://github.com/freeplane/freeplane/commit/849d671ea6623e1385b60e13ffaeb24818427c51) |
| 2022-09-21 | `fix` | Fix node side changing using drag and drop | `MNodeDropListener.java` | [a4836c39](https://github.com/freeplane/freeplane/commit/a4836c396b599197f9b9750c11e5e5c2c4ca7b94) |
| 2022-09-17 | `fix` | fix folding sensitive area size | `ForkPainter.java`, `MainView.java` +2 | [fa090e4e](https://github.com/freeplane/freeplane/commit/fa090e4e9ac8c66aa375602d761ce12dfece8e62) |
| 2022-09-11 | `feature` | Use "new user style from selection" logic also in style selector box for consistency | `Resources_cs.properties`, `Resources_da.properties` +30 | [6c5a2fcb](https://github.com/freeplane/freeplane/commit/6c5a2fcb6860b2fc8dc38345a35eb3217f903d20) |
| 2022-09-11 | `feature` | Issue #654 style assigned to new nodes: grayed out menu items | `MLogicalStyleController.java` | [ecd62dd2](https://github.com/freeplane/freeplane/commit/ecd62dd24a6dbb9ef77840d5ee6ef54869925de1) |
| 2022-09-10 | `feature` | Creating new user style from selection assigns it to all selected nodes and clears their f | `NewUserStyleFromSelectionAction.java` | [ff46339d](https://github.com/freeplane/freeplane/commit/ff46339dc7e8b60cdee66b7a4496420571f72bf7) |
| 2022-09-09 | `feature` | Add style/node property VerticalNodeLayout | `LocationBuilder.java`, `LocationController.java` +14 | [6c99f1a8](https://github.com/freeplane/freeplane/commit/6c99f1a8a7363abca2b03aa9597ab241d16bc47c) |
| 2022-09-04 | `feature` | add icons for jump-in and jump-out actions | `freeplane.properties`, `jumpIn.svg` +1 | [7ecaa867](https://github.com/freeplane/freeplane/commit/7ecaa86775a622fd6236ee5e39c5e3866f43a2df) |
| 2022-09-04 | `feature` | Preset style assigned to new nodes using Format->Set new node style->... | `history_en.txt`, `mindmapmodemenu.xml` +8 | [b6df01a0](https://github.com/freeplane/freeplane/commit/b6df01a0963518d5ffae3b7e5d152995f17d60af) |
| 2022-09-04 | `fix` | Fix dialog menu bars for non aqua look and feel under mac os | `FreeplaneMenuBar.java`, `ApplicationViewController.java` | [4c5217fd](https://github.com/freeplane/freeplane/commit/4c5217fdc061d8d2a395579add8e35e4c04f45c5) |
| 2022-09-03 | `fix` | fix static method calls | `UrlManager.java`, `ExternalResource.java` | [c92931ec](https://github.com/freeplane/freeplane/commit/c92931ec2bf316c9184f11daed1cd0199bcad062) |
| 2022-09-03 | `feature` | Show warning if new summary node encloses nodes on the other side | `MMapController.java`, `NewSummaryAction.java` +1 | [a9f087dd](https://github.com/freeplane/freeplane/commit/a9f087dd03f325350d83f3691b756e50fae8f3c2) |
| 2022-09-02 | `feature` | Issue #595 : add restrictions on placement of summary nodes | `MMapController.java`, `NewSummaryAction.java` | [0165cda9](https://github.com/freeplane/freeplane/commit/0165cda9d8b33992540f9dd749ce48e1dcee990e) |
| 2022-08-26 | `feature` | Always create first group node on the same side as its summary node. | `MMapController.java` | [3c8c56d8](https://github.com/freeplane/freeplane/commit/3c8c56d8c94118ca56b50286d110368e14d587d1) |
| 2022-08-22 | `fix` | fix test | `SummaryGroupEdgeListAdderShould.java` | [c29a60a6](https://github.com/freeplane/freeplane/commit/c29a60a6e787189ca6d2870a8a6b3a8bfd9727c3) |
| 2022-08-20 | `fix` | Fix script menu entry titles and change menu item title for Api Generator | `Resources_en.properties`, `ScriptingMenuEntryVisitor.java` | [b76798ae](https://github.com/freeplane/freeplane/commit/b76798aef3a47fd1a3f766391e111035e0041199) |
| 2022-08-20 | `fix` | fix moving selection root child nodes up and down | `MMapController.java` | [c61d5e45](https://github.com/freeplane/freeplane/commit/c61d5e45cadcfb320debb9e318e84e2ce2f9b9ce) |
| 2022-08-18 | `fix` | Issue #570 UI menu font is too big: fix menuItemFontSize=100 in auto.properties | `FrameController.java` | [40784b2b](https://github.com/freeplane/freeplane/commit/40784b2b6fe1b1d7f010ba6b829ba0f37452c619) |
| 2022-08-18 | `fix` | Fix file not found message pane | `LastOpenedList.java` | [a504a984](https://github.com/freeplane/freeplane/commit/a504a984524c8c27b175c9b7b4b34383d94f789c) |
| 2022-08-14 | `fix` | fix local hyperlink recognition and editing for URI attribute table values | `TextController.java`, `AttributeTable.java` | [bfd13c07](https://github.com/freeplane/freeplane/commit/bfd13c07ded17c8de6ae2bc9e66998ad299c8fe4) |
| 2022-08-13 | `fix` | restore font size fix for default look and feel | `FrameController.java` | [fc311f7d](https://github.com/freeplane/freeplane/commit/fc311f7de62f5c0aa242e6f4c37edf8cb22d8114) |
| 2022-08-12 | `fix` | fix node side after drag and drop | `MapController.java`, `NodeModel.java` +14 | [70323ae4](https://github.com/freeplane/freeplane/commit/70323ae4ec246458d432dd412347fb938f3b008a) |
| 2022-07-22 | `feature` | support inner-map links in attribute table | `LinkController.java`, `TextController.java` | [0a628efb](https://github.com/freeplane/freeplane/commit/0a628efb0e620d939a4da181cf2999e7abe95cf9) |
| 2022-07-16 | `feature` | Add tooltips for jump in and jump out actions | `Resources_en.properties` | [2dd99f90](https://github.com/freeplane/freeplane/commit/2dd99f90b25968fb1a1c721c9a5dbca8c2c98dd2) |
| 2022-07-04 | `fix` | fix selected node focus | `MapView.java` | [f8fc8e76](https://github.com/freeplane/freeplane/commit/f8fc8e768c6d25e05f9fd35df573e22a044308fa) |
| 2022-07-03 | `fix` | fix map navigation when jumped in | `MapView.java`, `NodeView.java` | [25a0f4b7](https://github.com/freeplane/freeplane/commit/25a0f4b7648c68070d542d67503b8897e889c664) |
| 2022-07-02 | `fix` | fix connector views if jumped in | `MapView.java` | [af9d348b](https://github.com/freeplane/freeplane/commit/af9d348b974cb2e237bbfd0124a619f037f3e209) |
| 2022-06-30 | `feature` | add style management action icons and add the actions to the style editor toolbar | `addConnectorStyle.svg`, `manageMapConditionalStyle.svg` +3 | [ba2b1f84](https://github.com/freeplane/freeplane/commit/ba2b1f841dc4e119ef98156c962a3563a040e7bd) |
| 2022-06-29 | `feature` | add style management action icons and add the actions to the style editor toolbar | `deleteLevelStyle.svg`, `deleteUserStyle.svg` +6 | [832ddc62](https://github.com/freeplane/freeplane/commit/832ddc62dad899839591ee32e446389f9be7f174) |
| 2022-06-21 | `fix` | Issue #463 : fix updating of documentation maps created with old Freeplane | `MapController.java` | [4dae7e85](https://github.com/freeplane/freeplane/commit/4dae7e85466c2c32bdaf81465d26b5264634f349) |
| 2022-06-19 | `fix` | Issue #461 fix tool tip as sugested | `Resources_ar.properties`, `Resources_ca.properties` +34 | [c47bdf34](https://github.com/freeplane/freeplane/commit/c47bdf34bfc046cf739cae3e08d51a9b698b41a3) |
| 2022-06-18 | `fix` | fix map scrolling after zooming from map overview | `MapScroller.java` | [a94f1dd9](https://github.com/freeplane/freeplane/commit/a94f1dd91aa0d6cde3a38234f3ad6e1b64d38251) |
| 2022-06-18 | `fix` | fix stack overflow | `MapScroller.java` | [a51629a1](https://github.com/freeplane/freeplane/commit/a51629a160d7123005665ae25283ea36535e6b79) |
| 2022-06-18 | `fix` | fix separators | `FilterController.java` | [8c9ecf58](https://github.com/freeplane/freeplane/commit/8c9ecf5836987cdbbbf4707b9c9b5277536c5e0b) |
| 2022-06-18 | `fix` | fix icon sizes on the toolbar buttons | `NewChild.svg`, `NewChild_XL.svg` +16 | [e77e69b9](https://github.com/freeplane/freeplane/commit/e77e69b9b36e5f535b63ddeeb0480274d428925f) |
| 2022-06-16 | `fix` | fix map scrolling | `MapScroller.java` | [480721dc](https://github.com/freeplane/freeplane/commit/480721dcfa9195534545f8afe500cd4d15bd597d) |
| 2022-06-16 | `fix` | fix map scrolling | `MapScroller.java`, `MapView.java` | [0dc68311](https://github.com/freeplane/freeplane/commit/0dc68311bb0c81baf7a731abd3447aabafbb2902) |
| 2022-06-16 | `fix` | fix map scrolling after window size change | `MapView.java` | [02834135](https://github.com/freeplane/freeplane/commit/028341350cdb7365d2c4520f7559020b9a371090) |
| 2022-06-16 | `fix` | MacOS colors seem to work fine when started with native OS launcher, revert fix | `FrameController.java` | [bec3d92d](https://github.com/freeplane/freeplane/commit/bec3d92de90622d695b22b35c8e4e15e3b69b232) |
| 2022-06-13 | `fix` | "Fix" selected item color for MacOS native Look and Feel | `FrameController.java` | [9417a639](https://github.com/freeplane/freeplane/commit/9417a639e6f659ce6e4f0b2464b4b5c6f805d5db) |
| 2022-06-12 | `feature` | add drop-down menu "edit" to toolbar | `Resources_af.properties`, `Resources_ca.properties` +36 | [9e2e8ec3](https://github.com/freeplane/freeplane/commit/9e2e8ec39f22575fa53eb3d2d6cf51ae6506e031) |
| 2022-06-12 | `fix` | fix type recognition for user styles | `FrameController.java`, `freeplane.properties` +2 | [9f3914f6](https://github.com/freeplane/freeplane/commit/9f3914f6ba68484aa15a7577a7e6f7b2a96aa409) |
| 2022-06-12 | `feature` | fix keyboard focus after new user style was created | `NewUserStyleAction.java` | [77675d42](https://github.com/freeplane/freeplane/commit/77675d42682e8108f665aa4aea392ed5612496d9) |
| 2022-06-11 | `feature` | implement drop-down menus for tool bars | `mindmapmodemenu.xml`, `JBigButton.java` +4 | [9d3b675c](https://github.com/freeplane/freeplane/commit/9d3b675cbf923a226a086a0e8b4c4547c6137fd8) |
| 2022-06-10 | `feature` | add copy/paste/cut/delete actions to the tool bar | `mindmapmodemenu.xml` | [1a08ffbf](https://github.com/freeplane/freeplane/commit/1a08ffbfb91c8cd78b8782ab04dad19d4aab8a07) |
| 2022-06-10 | `feature` | add find next/find previous actions to find dialog | `FindAction.java` | [36ac640f](https://github.com/freeplane/freeplane/commit/36ac640fdd75fa83c19c7a3a2d1f87bbf97637d7) |
| 2022-06-10 | `feature` | Issue #443 change default accelerator for new child from "insert" to "tab" | `default_accelerators_mac.properties`, `mindmapmodemenu.xml` | [fdf5ce11](https://github.com/freeplane/freeplane/commit/fdf5ce11f37547f8d074c89a355882b5f420f109) |
| 2022-06-05 | `fix` | fix zoom selection on the toolbar | `MapViewController.java` | [f90ff7ce](https://github.com/freeplane/freeplane/commit/f90ff7ce7f86801f307eaa5105efbe99a704cf87) |
| 2022-06-05 | `fix` | fix map overview on scaled graphics | `MapOverviewImage.java` | [d72ca5be](https://github.com/freeplane/freeplane/commit/d72ca5bec1a4de42fbad5813d91bc51e26f99d63) |
| 2022-06-05 | `fix` | fix map scrolling | `MapView.java` | [385b3ebf](https://github.com/freeplane/freeplane/commit/385b3ebff59bece823c898b4bf11980212322e1c) |
| 2022-06-05 | `fix` | fix find | `FindAction.java` | [0d33a0ce](https://github.com/freeplane/freeplane/commit/0d33a0ce54bc116a5570ab2d736fada386afd8ad) |
| 2022-06-05 | `fix` | fix mapview position after size change | `MapView.java` | [e043f745](https://github.com/freeplane/freeplane/commit/e043f745671961165e017d80008c42a1dd60cdba) |
| 2022-06-05 | `fix` | fix mapview position after size change | `MapView.java` | [f4f3823e](https://github.com/freeplane/freeplane/commit/f4f3823e10dfb52497b6d383724b93bf3c697761) |
| 2022-06-04 | `fix` | fix LaF issues under Windows | `UITools.java`, `FrameController.java` | [e80aa1a5](https://github.com/freeplane/freeplane/commit/e80aa1a58e65bf53dc76ebed6ddc4156b7bbba37) |
| 2022-06-04 | `fix` | fix LaF issues under Windows | `UITools.java`, `FrameController.java` | [6e409118](https://github.com/freeplane/freeplane/commit/6e409118c82b5183cfb0b5a763a34338d8c85cda) |
| 2022-06-04 | `fix` | fix toolbars for other modes | `filemodemenu.xml`, `FModeControllerFactory.java` +1 | [90fda006](https://github.com/freeplane/freeplane/commit/90fda00624cab5e19a56743f15d1a6b0d5a403d1) |
| 2022-06-04 | `fix` | fix layout | `FreeplaneToolBar.java`, `FilterConditionEditor.java` +1 | [2417c0e2](https://github.com/freeplane/freeplane/commit/2417c0e294d70f02cec53df441c49d1ef257664e) |
| 2022-06-03 | `fix` | Issue #412: fix regression occured when window size was changed | `MapView.java`, `MapViewScrollPane.java` | [8e7222f6](https://github.com/freeplane/freeplane/commit/8e7222f6b4a3175bcc8236e3854eb934f12276d5) |
| 2022-05-29 | `fix` | Issue #414: Regression: broken checkboxes | `CheckIconWithBorder.java` | [2979f2e3](https://github.com/freeplane/freeplane/commit/2979f2e354d947d4d5dedc60b401582f7719a4be) |
| 2022-05-29 | `fix` | Issue #412: Regression: Diagonal trajectory when zooming | `MapScroller.java`, `MapViewScrollPane.java` | [062e7046](https://github.com/freeplane/freeplane/commit/062e70460d3808de49c351f133b329461b711818) |
| 2022-05-28 | `fix` | fix note panel divider location after start | `ApplicationViewController.java` | [42d97358](https://github.com/freeplane/freeplane/commit/42d973588e221008afdaf7bee7920b883172325e) |
| 2022-05-28 | `fix` | fix note panel divider location after start | `ApplicationViewController.java` | [38e095a5](https://github.com/freeplane/freeplane/commit/38e095a54c7b443e413a73fa64dd0c30af43f48c) |
| 2022-05-28 | `fix` | fix map positioning after freeplane start and when viewport is resized | `Controller.java`, `FreeplaneGUIStarter.java` +1 | [9ecfc927](https://github.com/freeplane/freeplane/commit/9ecfc927fc082425540481516feef7dff7f9b414) |
| 2022-05-26 | `feature` | Issue #399 Doing a multiple word search in the icon table result in unintentional add of i | `IconSelectionPopupDialog.java` | [ff15b555](https://github.com/freeplane/freeplane/commit/ff15b5557588bb7d280762a9403eac67fd051431) |
| 2022-05-26 | `fix` | fix race conditions: run more initializers in swing event thread | `EventQueueExecutorServiceAdapter.java`, `FreeplaneGUIStarter.java` +1 | [17781f6e](https://github.com/freeplane/freeplane/commit/17781f6e73a355f37cfe191642f04d4ca0dabb5d) |
| 2022-05-22 | `fix` | Issue #395 Regression on 1.10.3_pre4: touchpad scrolling is dead on the map view | `MapViewScrollPane.java` | [32a41d9c](https://github.com/freeplane/freeplane/commit/32a41d9ceb896f313ca49c80e9f199a27f620d89) |
| 2022-05-21 | `fix` | fix alt gr handling for F Button Bar | `FButtonBar.java` | [4f749c0b](https://github.com/freeplane/freeplane/commit/4f749c0b2d8277202d83abb50e99565d86e14428) |
| 2022-05-21 | `feature` | fix alt gr hot key support for mac os | `KeyEventTranslator.java` | [b4fcd5ed](https://github.com/freeplane/freeplane/commit/b4fcd5ed0d99490c33a572d10f0c1b023401c53e) |
| 2022-05-21 | `feature` | add a preference to remove icons from node search dialog | `preferences.xml`, `IconsHolder.java` +3 | [92bb07b2](https://github.com/freeplane/freeplane/commit/92bb07b211fbc14cf1908fc651e28f1f83fb939d) |
| 2022-05-20 | `fix` | fix toolbar button size under mac os | `FreeplaneToolBar.java` | [3c330a2b](https://github.com/freeplane/freeplane/commit/3c330a2bfdcbf99944bff87eb00f8c1a902c616a) |
| 2022-05-20 | `fix` | fix toggle button painting under mac os | `FreeplaneToolBar.java` | [cd55f85c](https://github.com/freeplane/freeplane/commit/cd55f85c1cd77020ffa083ce09edeb9b6d42ec6e) |
| 2022-05-20 | `fix` | fix race condition in VAqua L&F on start | `FrameController.java` | [69a3dec1](https://github.com/freeplane/freeplane/commit/69a3dec1eb72fe020ee342af87fab5526003c6c3) |
| 2022-05-18 | `feature` | add iconActionRemovesIconIfExists option to preferences | `preferences.xml` | [bf94e6da](https://github.com/freeplane/freeplane/commit/bf94e6da4ff06a6036b2ac4ad8c51065bf3648ea) |
| 2022-05-18 | `feature` | Add option to remove icon if exists when icon action is triggered | `history_en.txt`, `remove_icon_if_exists.svg` +10 | [1084e4bb](https://github.com/freeplane/freeplane/commit/1084e4bbae87617fdb400219ea57624801bc0d35) |
| 2022-05-17 | `fix` | fix compact layout | `VerticalNodeViewLayoutStrategy.java` | [bb1aaf8d](https://github.com/freeplane/freeplane/commit/bb1aaf8d38ba198be67a0a591ad2e60fa10ab83b) |
| 2022-05-14 | `feature` | Add map layout option "allow node overlap" (View -> View settings) | `mindmapmodemenu.xml`, `MapStyle.java` +4 | [ef7e6ad3](https://github.com/freeplane/freeplane/commit/ef7e6ad3ef42252e0b2b63590ce7c258c439165d) |
| 2022-05-13 | `fix` | fix loading of system look and feels | `FrameController.java` | [ad0985ea](https://github.com/freeplane/freeplane/commit/ad0985eae220bfa46a11f23a26738d8ab76e67d9) |
| 2022-04-18 | `fix` | fix zoom change on mouse wheel | `MapStyle.java`, `MapViewController.java` | [38f28d7e](https://github.com/freeplane/freeplane/commit/38f28d7ee2c74674088ccbdb51a036f970ae3f05) |
| 2022-04-18 | `fix` | fix zoom change on mouse wheel | `MapStyle.java`, `MapViewController.java` | [c49ff0f5](https://github.com/freeplane/freeplane/commit/c49ff0f51e6ff69768a24ad73fdfe36ee8d5e5fa) |
| 2022-04-18 | `fix` | fix folding circle colors and border widths | `UITools.java`, `FoldingMark.java` +1 | [bb57750e](https://github.com/freeplane/freeplane/commit/bb57750e5bdbdffa801c12f227f2c81cc82a5368) |
| 2022-04-18 | `fix` | fix folding circle colors | `FoldingMark.java`, `MainView.java` | [d2ed07f3](https://github.com/freeplane/freeplane/commit/d2ed07f330cc97de79b92998b991ab0cb1025da1) |
| 2022-04-18 | `fix` | fix icons | `ShowPreferencesAction.svg`, `freeplane.properties` +4 | [026c3379](https://github.com/freeplane/freeplane/commit/026c3379b02c9e10b15cc6c7ef79f6bb306f2ebd) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-04-10 | `feature` | Work around for Garbage on LineNumbersRuler under Java 11+ on Windows with HiDPI monitor s | `JRestrictedSizeScrollPane.java` | [b215be19](https://github.com/freeplane/freeplane/commit/b215be198b6a3ce52645648086a01101ddb43b5f) |
| 2022-04-10 | `feature` | Work around for Garbage on LineNumbersRuler under Java 11+ on Windows with HiDPI monitor s | `JRestrictedSizeScrollPane.java` | [5176f43e](https://github.com/freeplane/freeplane/commit/5176f43eb4925f3a304dfe895124d51e9e0dd1fd) |
| 2022-04-02 | `fix` | fix use of url query in icons for bundle urls | `ResourceController.java`, `SVGIconCreator.java` +1 | [e808f924](https://github.com/freeplane/freeplane/commit/e808f9248db185ec05b38a19445456ce1757d33b) |
| 2022-04-02 | `fix` | fix use of url query in icons for bundle urls | `ResourceController.java`, `SVGIconCreator.java` +1 | [7f5038f6](https://github.com/freeplane/freeplane/commit/7f5038f682521c1f5edfc7a7c643bc9fee5d3135) |
| 2022-04-01 | `fix` | fix accent color replacements | `freeplane.properties` | [29e2349d](https://github.com/freeplane/freeplane/commit/29e2349d70f6c9dbc54b19a45a4be97fd571b5d8) |
| 2022-04-01 | `feature` | Support accent colors in state icons | `ResourceController.java`, `IconStore.java` +2 | [f0afd4c5](https://github.com/freeplane/freeplane/commit/f0afd4c53bcc97b4b7c059a6afda3dfdc1f64638) |
| 2022-04-01 | `feature` | Support accent colors in state icons | `ResourceController.java`, `IconStore.java` +2 | [41215f99](https://github.com/freeplane/freeplane/commit/41215f999ede091720a7d69ecd0bfe44997ba87a) |
| 2022-03-25 | `fix` | fix NPE | `UserPropertiesUpdater.java` | [37f1abf6](https://github.com/freeplane/freeplane/commit/37f1abf62c56865e11137f2439b80b484ac89bed) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-03-11 | `fix` | Fix setting followed map for the case the template itself has no map styles | `MapLoader.java` | [a5d76fbc](https://github.com/freeplane/freeplane/commit/a5d76fbc38f6874d4bd7cf2fead4110284c8caf6) |
| 2022-03-11 | `fix` | fix NPE | `NodeHistory.java` | [061f2db6](https://github.com/freeplane/freeplane/commit/061f2db6255a8ecbf3650ae23e126a7e8560c38a) |
| 2022-02-27 | `feature` | add null check | `LogUtils.java` | [9cb4c856](https://github.com/freeplane/freeplane/commit/9cb4c8568cf1e940819040ecab86e9db86c2a107) |
| 2022-02-27 | `fix` | fix NPE | `EditNodeTextField.java` | [7badab22](https://github.com/freeplane/freeplane/commit/7badab223c62ae53e2484836d89fb70f67958b92) |
| 2022-02-21 | `feature` | Support invisible node text | `NodeColorControlGroup.java` | [6bd56cf3](https://github.com/freeplane/freeplane/commit/6bd56cf36ea3fd2b44b4c3b9184c49c3296079b6) |
| 2022-02-19 | `feature` | Support LaF specific colors | `SVGIconCreator.java` | [9d891239](https://github.com/freeplane/freeplane/commit/9d891239e341fbfa99021b2c10c4ada662d3e03a) |
| 2022-02-19 | `feature` | Add buttons "make transparent", "copy" and "paste" to color properties | `icons.ttf`, `preferences.xml` +10 | [52451464](https://github.com/freeplane/freeplane/commit/5245146474bab734a326daef3a5de01df8586a45) |
| 2022-02-14 | `fix` | fix #3119 Adjusted width of icons toolbar always returns to default width if close and ope | `OneTouchCollapseResizer.java` | [34593564](https://github.com/freeplane/freeplane/commit/3459356454ffe307c935f81c634373f7523c31f7) |
| 2022-02-13 | `fix` | fix LookAndFeelDockingTheme change | `MapViewDockingWindows.java` | [c7104f59](https://github.com/freeplane/freeplane/commit/c7104f592422742a0dab2139e10bf4cb3c5b51c0) |
| 2022-02-13 | `fix` | fix class cast exception in VAqua | `ApplicationViewController.java`, `SplitPaneLayoutManager2Decorator.java` +1 | [2d762afc](https://github.com/freeplane/freeplane/commit/2d762afc071178f83679aa290d22a954c52f76df) |
| 2022-02-12 | `fix` | Fix setOptimalColumnWidths for attribute tables | `AttributeTable.java` | [e8b01b7c](https://github.com/freeplane/freeplane/commit/e8b01b7c55f5fdfba0eb088e3477b6f0e2b024fb) |
| 2022-02-12 | `fix` | fix attribute table background color | `AttributeTable.java` | [b7c7c4c5](https://github.com/freeplane/freeplane/commit/b7c7c4c5df9ad2ee06490f9b0a835ba30114a01c) |
| 2022-02-10 | `fix` | fix NPE | `SVGIconCreator.java` | [d7072b8b](https://github.com/freeplane/freeplane/commit/d7072b8be4b536173e1166837408d1cd9d23e2b3) |
| 2022-02-09 | `fix` | Fix loading icons for special URLs with queries | `SVGIconCreator.java` | [f96c7f32](https://github.com/freeplane/freeplane/commit/f96c7f326ffcd14895b2f9cedfa5fd6b3ca21cee) |
| 2022-02-04 | `feature` | implement special treatment for Auqa L&F | `MapViewDockingWindows.java` | [abffb2b9](https://github.com/freeplane/freeplane/commit/abffb2b9d56fb07c427ed7a6ddf37dd53b9e7296) |
| 2022-02-04 | `feature` | Introduce even smaller formatting panel font size and use MIDDLE as the new default | `StyleEditorPanel.java`, `freeplane.properties` +1 | [f427922e](https://github.com/freeplane/freeplane/commit/f427922e0df771cdac39c5140c9a0e0607de9622) |
| 2022-02-04 | `feature` | Add border to file revisions table | `FileRevisionsDialog.java` | [8302cc7b](https://github.com/freeplane/freeplane/commit/8302cc7b5bbe79480ef89f21ca2a8e6a7799f793) |
| 2022-02-04 | `fix` | fix race conditions | `ApplicationViewController.java` | [f9814881](https://github.com/freeplane/freeplane/commit/f98148810ab8f3a9d9332b1cad2e17f566f7baa3) |
| 2022-01-30 | `fix` | fix class loader for L&F update | `FrameController.java` | [60f5a455](https://github.com/freeplane/freeplane/commit/60f5a455d57a52bb857e601b96ed55b8790c7827) |
| 2022-01-29 | `fix` | fix updateComponentTreeUI | `FreeplaneGUIStarter.java` | [527785e6](https://github.com/freeplane/freeplane/commit/527785e666542563ede31ba5ad1f2e4c9f21a478) |
| 2022-01-29 | `fix` | fix and simplify resizer | `CollapseableBoxBuilder.java`, `OneTouchCollapseResizer.java` | [1ff172be](https://github.com/freeplane/freeplane/commit/1ff172be781e4497599a5d162efe208ae18adf18) |
| 2022-01-29 | `fix` | fix resizer painting | `JResizer.java`, `OneTouchCollapseResizer.java` | [ca0b62de](https://github.com/freeplane/freeplane/commit/ca0b62de0c91be1d61a046d2c0573948c750c6b9) |
| 2022-01-22 | `fix` | fix version number | `version.properties` | [ad3c2bb9](https://github.com/freeplane/freeplane/commit/ad3c2bb9b3e577c6b88338bd93ce2e86bffa9ebe) |
| 2022-01-21 | `fix` | fix generics | `JComboBoxFactory.java` | [1a73d24c](https://github.com/freeplane/freeplane/commit/1a73d24cb1f0b9ad7210d30a5fb54e1e932e8b77) |
| 2022-01-21 | `fix` | Fix attribute table colors and header size | `FrameController.java`, `AttributeTable.java` | [59e75f57](https://github.com/freeplane/freeplane/commit/59e75f5793ca7eef40d39d608316580daa23269b) |
| 2022-01-21 | `feature` | Add UI laf themes "Flat Solarized Light" and "Atom One Dark Contrast (Material)" | `Atom One Dark Contrast.LICENSE.txt`, `Atom One Dark Contrast.theme.json` +6 | [9a14501b](https://github.com/freeplane/freeplane/commit/9a14501b220a8a2db8ea92616b341151a6ccad9d) |
| 2022-01-21 | `feature` | Add some space at the top of the tabbed pane | `UITools.java` | [03ec0e83](https://github.com/freeplane/freeplane/commit/03ec0e83a206e6766c1abbbf0ec6f9f4fc473f1c) |
| 2022-01-21 | `fix` | fix typo | `FreeSelectNodeAction.java` | [a5cee9b8](https://github.com/freeplane/freeplane/commit/a5cee9b81fb8089c3e9c5cf7d281f9c8a748f501) |
| 2022-01-16 | `feature` | refactor and add option | `preferences.xml`, `AddConnectorAction.java` +4 | [4e5e13f8](https://github.com/freeplane/freeplane/commit/4e5e13f88918ebc6875e07aa658165d1bdc11600) |
| 2022-01-14 | `feature` | support dark themes in syntax editor | `build.gradle`, `SourceTextEditorUIConfigurator.java` +3 | [eb4166a7](https://github.com/freeplane/freeplane/commit/eb4166a7612d80849365d13cff940940fab72e09) |
| 2022-01-14 | `api_change` | make empty implementation an interface default method | `MCloudController.java`, `MIconController.java` +4 | [a6bb8b0d](https://github.com/freeplane/freeplane/commit/a6bb8b0d0831a8d1097ffe6e5896d77c7ee370d2) |
| 2022-01-13 | `fix` | fix color property for mac os | `ColorIcon.java`, `ColorProperty.java` | [f7f2f747](https://github.com/freeplane/freeplane/commit/f7f2f747cc45f09d2f4ab255dababf5b984da6c6) |
| 2022-01-09 | `fix` | #3094 Apply icon size from format panel to style has a bug | `MIconController.java`, `MapStyle.java` | [23ab149d](https://github.com/freeplane/freeplane/commit/23ab149d319c11b9fc606e05d714ab2c26b7b82b) |
| 2022-01-09 | `fix` | fix color icon | `ColorIcon.java` | [6a564bdd](https://github.com/freeplane/freeplane/commit/6a564bddd5e6394278b962d04ba02d8dab9da0bd) |
| 2022-01-08 | `fix` | fix background color for map html exports using xslt | `treestyles.css`, `toxhtml.xsl` +2 | [bb751b18](https://github.com/freeplane/freeplane/commit/bb751b184294e1ac7509fc18f47728dd5a6b0e1a) |
| 2022-01-08 | `feature` | use new xml version 1.9.13 | `mapVersions.xml`, `FreeplaneVersion.java` | [ae2079d2](https://github.com/freeplane/freeplane/commit/ae2079d2f91c5481ca663b2a9640824a3e1e5259) |
| 2022-01-08 | `feature` | add invisible node shape | `NodeStyleShape.java`, `BubblePainter.java` +5 | [585a63e9](https://github.com/freeplane/freeplane/commit/585a63e95e7f36111b331200cfbd5a4466931889) |
| 2022-01-07 | `feature` | Add other flat LAFs | `MModeController.java` | [22418641](https://github.com/freeplane/freeplane/commit/2241864110d2a38e4ff45708d4e192a270631970) |
| 2022-01-07 | `feature` | Replace darcula LAF by supported Flat Darcula LAF and add Flat Light LAF | `build.gradle`, `FixDarculaToggleButtonUI.java` +4 | [40eb7bdf](https://github.com/freeplane/freeplane/commit/40eb7bdfd07db8ecfd5424ba4f765be268a7428e) |

### Dettagli commit con note

**[b215be19](https://github.com/freeplane/freeplane/commit/b215be198b6a3ce52645648086a01101ddb43b5f)** (2022-04-10) — Work around for Garbage on LineNumbersRuler under Java 11+ on Windows with HiDPI monitor support

> see https://github.com/Sciss/SyntaxPane/issues/36

**[5176f43e](https://github.com/freeplane/freeplane/commit/5176f43eb4925f3a304dfe895124d51e9e0dd1fd)** (2022-04-10) — Work around for Garbage on LineNumbersRuler under Java 11+ on Windows with HiDPI monitor support

> see https://github.com/Sciss/SyntaxPane/issues/36

**[9d891239](https://github.com/freeplane/freeplane/commit/9d891239e341fbfa99021b2c10c4ada662d3e03a)** (2022-02-19) — Support LaF specific colors

> UnfoldAllAction.icon=/images/unfold_all.svg?useAccentColor=true
> accentColorReplacementsForLightLookAndFeels=/#0071bc/#bc0071
> accentColorReplacementsForDarkLookAndFeels=/#0071bc/#bcff71
> accentColorReplacementsForFlatLafDarcula=/#0071bc/@accentColor
> accentColorReplacementsForFlatLafDark=/#0071bc/@accentColor
> accentColorReplacementsForFlatLafIntelliJ=/#0071bc/@accentColor
> accentColorReplacementsForFlatLafLight=/#0071bc/@accentColor
> accentColorReplacementsForAtomOneDarkContrastMaterial=/#0071bc/@accentColor
> accentColorReplacementsForSolarizedLight=/#0071bc/@accentColor


---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-12-15 | `fix` | bug fix: automatic edge color has priority over default style edge color | `EdgeController.java` | [7de867d4](https://github.com/freeplane/freeplane/commit/7de867d43c4292d91cf1e6454481753bfd5233f2) |
| 2021-12-11 | `fix` | fix NPE | `MapView.java` | [fb0a30c0](https://github.com/freeplane/freeplane/commit/fb0a30c057f38e5c12d3a7d6dab40731ed3a3933) |
| 2021-12-11 | `fix` | Fix: copy border dash when node format is copied | `NodeBorderModel.java` | [577115ef](https://github.com/freeplane/freeplane/commit/577115eff67681870867e720b917eb8d95a6d6a5) |
| 2021-12-10 | `fix` | fix: color chooser forgets recently used colors. | `ShowPreferencesAction.java`, `ColorTracker.java` +3 | [387357f8](https://github.com/freeplane/freeplane/commit/387357f8bc24e13f9d148cd3b2d6d2fe63e24be1) |
| 2021-11-28 | `feature` | add undo-redo to css editor | `UndoEnabler.java`, `CssEditor.java` +1 | [a3cf280d](https://github.com/freeplane/freeplane/commit/a3cf280d8a94c01a69ed866655ebffe53d6cc8ff) |
| 2021-11-28 | `feature` | add css editor, make it work | `cssPreview.html`, `ButtonProperty.java` +7 | [d572a4d7](https://github.com/freeplane/freeplane/commit/d572a4d719db8a824c035d87cd01e7db19fc9168) |
| 2021-11-28 | `feature` | enable paragraph tag selector in editor and improve note dialog css | `EditNodeWYSIWYG.java`, `freeplane.properties` | [d5c7b221](https://github.com/freeplane/freeplane/commit/d5c7b221c393594a06c611571ec1af44b284f082) |
| 2021-11-28 | `feature` | Add table cell border to default css | `StyleSheetConfigurer.java`, `AttributeController.java` +3 | [aac89019](https://github.com/freeplane/freeplane/commit/aac89019010ff46680bb098235c290934de016f1) |
| 2021-11-21 | `fix` | [fix 232] put filename before folder in Most Recent Maps submenu | `LastOpenedList.java` | [6780f6d5](https://github.com/freeplane/freeplane/commit/6780f6d51476045b4b95b569321f7118827e74c8) |
| 2021-11-21 | `feature` | fix #3073 Open new maps in a tab next to selected map and open previous map when it is clo | `MapViewController.java` | [778e4bd9](https://github.com/freeplane/freeplane/commit/778e4bd9ab73d86b94c86dbe067eadfb7261f5fa) |
| 2021-11-20 | `fix` | fix NPE | `MapStyle.java`, `MapStyleModel.java` +1 | [3d26f483](https://github.com/freeplane/freeplane/commit/3d26f4834690190a98313daa52ec781f89b37589) |
| 2021-11-14 | `fix` | Fix NPE | `MapStyle.java`, `MapStyleModel.java` | [1bc18512](https://github.com/freeplane/freeplane/commit/1bc18512c3beaccf8f722c210fead5d6060aa658) |
| 2021-10-26 | `fix` | #3057 Bug when trying to modify a text directly in node | `MainView.java` | [8bbb40ea](https://github.com/freeplane/freeplane/commit/8bbb40ea2e0d80c6e3f691839b4b40b204eeefb8) |
| 2021-10-24 | `fix` | fix rendering of <br> elements | `SynchronousScaledEditorKit.java` | [3763a4af](https://github.com/freeplane/freeplane/commit/3763a4af5c9a7262241d9030e20dd9f11afc121e) |
| 2021-10-22 | `feature` | revert "Support complex conditional styles and script conditions in conditional styles" | `ConditionalStyleModel.java` | [571a0263](https://github.com/freeplane/freeplane/commit/571a026305f184845e0d175b733041f9eb7e164b) |
| 2021-10-16 | `feature` | Outline view should always create new child node as the first child | `history_en.txt`, `MMapController.java` | [be752ffc](https://github.com/freeplane/freeplane/commit/be752ffc2a029089b267d8a63636d3014ec93d00) |
| 2021-10-15 | `feature` | add text saying "Presets are saved in [folder path]" | `InfoArea.java`, `SaveAcceleratorPresetsAction.java` +2 | [7dacf6ac](https://github.com/freeplane/freeplane/commit/7dacf6acd6434c680c6b90969a11e92d2d6c503d) |
| 2021-10-15 | `fix` | fix no actions available menu entries | `mindmapmodemenu.xml`, `MenuBuildProcessFactory.java` +2 | [f394cc87](https://github.com/freeplane/freeplane/commit/f394cc870b77a99acd5ce4317a910f4c4e8d9c05) |
| 2021-10-10 | `fix` | fix removing of user properties | `ResourceBundles.java` | [bf0bd642](https://github.com/freeplane/freeplane/commit/bf0bd6420685b99ba170ce046d463c9a4b39d025) |
| 2021-10-09 | `feature` | fix latex export: adapt XSLT script to new raw xml | `mm2latexinput.xsl` | [b405f214](https://github.com/freeplane/freeplane/commit/b405f21401276247f6966a7ad2ab3a39e4400a19) |
| 2021-10-08 | `feature` | add undo / redo to inline editor | `EditNodeTextField.java` | [9a9eed3e](https://github.com/freeplane/freeplane/commit/9a9eed3e4876f6aaa082a754d35f4e367d53f17d) |
| 2021-10-08 | `fix` | Fix reuse of old filter conditions | `Filter.java`, `FilterController.java` +5 | [37b87f7f](https://github.com/freeplane/freeplane/commit/37b87f7f4ce2339766f262a8ba7e79b74f4f3ff2) |
| 2021-10-07 | `feature` | Support complex conditional styles and script conditions in conditional styles | `ASelectableCondition.java`, `ConditionalStyleModel.java` +1 | [2b5ed1f2](https://github.com/freeplane/freeplane/commit/2b5ed1f29cf015ec14a8550aa8d8b79e3c207d05) |
| 2021-10-02 | `fix` | improve fix | `MNodeMotionListener.java` | [94adb208](https://github.com/freeplane/freeplane/commit/94adb2081ad8dcdaece30a028a95bc03af641b72) |
| 2021-10-02 | `fix` | fix NPE | `CommandSearchDialog.java`, `IconItem.java` +4 | [0995b569](https://github.com/freeplane/freeplane/commit/0995b569a784149af7d67d26cd2809557f996aac) |
| 2021-10-02 | `fix` | fix NPE | `MapStyle.java` | [43d717ad](https://github.com/freeplane/freeplane/commit/43d717ade78d8ac139a12efe73511434d45c2041) |
| 2021-10-02 | `fix` | fix dialog | `ManageAssociatedMindMapsDialog.java` | [23300974](https://github.com/freeplane/freeplane/commit/23300974f83db98d111da30ef060b8d82c4c3d4d) |
| 2021-10-01 | `fix` | fix NPE | `ConditionalStyleModel.java` | [1f29757a](https://github.com/freeplane/freeplane/commit/1f29757a547438b64e95b7ac5c5c474cf811a677) |
| 2021-09-25 | `fix` | #3014 fix reminder handling when map is closed | `ReminderExtension.java` | [f81d1f35](https://github.com/freeplane/freeplane/commit/f81d1f35be4e692a19fa6aa9d2811722b855d240) |
| 2021-09-25 | `fix` | fix enabling style editor panel after moving multiple nodes | `StyleEditorPanel.java` | [4655a584](https://github.com/freeplane/freeplane/commit/4655a584d2987dc05d6b311eacbb368c1da94455) |
| 2021-09-25 | `fix` | fix selected node update | `MapView.java` | [94db52d2](https://github.com/freeplane/freeplane/commit/94db52d2251578438b1c28abb7da3537a5f48337) |
| 2021-09-24 | `fix` | fix it | `MLogicalStyleController.java` | [2f4acfaa](https://github.com/freeplane/freeplane/commit/2f4acfaa9d40b439cc10b5b209877121d9da930f) |
| 2021-09-23 | `feature` | Add AnyDescendant to conditions targets (fix typo) | `Resources_es.properties`, `Resources_fr.properties` +9 | [a54423d6](https://github.com/freeplane/freeplane/commit/a54423d661056313fdd23c067403399da649493b) |
| 2021-09-23 | `feature` | Add "has children" condition to AllChildren/ AllDescendants conditions | `AllChildrenConditionDecorator.java`, `AllDescendantsConditionDecorator.java` | [02d08c56](https://github.com/freeplane/freeplane/commit/02d08c56f50a099b629f0e4bf77a281903875273) |
| 2021-09-23 | `feature` | fix editing new details inline | `MTextController.java` | [e75da4d5](https://github.com/freeplane/freeplane/commit/e75da4d5e8f23193df0eef3c54ca9cbf9d1ee6eb) |
| 2021-09-23 | `fix` | fix IndexOutOfBoundsException | `Slide.java` | [532c2c6b](https://github.com/freeplane/freeplane/commit/532c2c6bd11221c01f55420d00a8a18657e0ce3b) |
| 2021-09-21 | `fix` | fix issue with multiple hashtables | `FrameController.java` | [03a5ceb9](https://github.com/freeplane/freeplane/commit/03a5ceb96cbac9e0fa8100946c3bac8b5c3fe003) |
| 2021-09-21 | `api_change` | Expose internal API to generate menu and preference descriptions markdown | `build.gradle`, `IconIndexer.java` +7 | [68ffb79c](https://github.com/freeplane/freeplane/commit/68ffb79c2c2ed385281569fbabce7c3868130298) |
| 2021-09-20 | `fix` | Fix attribute table tooltip and editor colors | `AttributeController.java`, `AttributeTable.java` | [53ae3f27](https://github.com/freeplane/freeplane/commit/53ae3f27896f8b63ef7b32e4cb419d945b34fcc4) |
| 2021-09-19 | `fix` | fix NPE | `MapStyle.java` | [50aa121a](https://github.com/freeplane/freeplane/commit/50aa121a2e22930abb2c5ab58ee1c9abaa473f28) |
| 2021-09-18 | `fix` | fix URISyntaxException | `MapLoader.java` | [d243eae1](https://github.com/freeplane/freeplane/commit/d243eae1ef1c5826e6bcd997289a12dde4db0bd8) |
| 2021-09-12 | `feature` | add tooltip "Note: top-level menu names (e.g. File, Edit) are not checked for match with t | `CommandSearchDialog.java`, `Resources_en.properties` | [07185f91](https://github.com/freeplane/freeplane/commit/07185f917ec263a7bc78557a57e595a1f770e485) |
| 2021-09-12 | `feature` | Add new user style action not copying selected node style | `Resources_cs.properties`, `Resources_da.properties` +25 | [3865a58f](https://github.com/freeplane/freeplane/commit/3865a58facf9c404067d34fa14175c8ba3f4a50a) |
| 2021-09-08 | `fix` | fix #3006 Bug in selected node formatting | `NodeViewFactory.java` | [6d4044b0](https://github.com/freeplane/freeplane/commit/6d4044b04202232f740ddf9b5b994cc48b90ac9c) |
| 2021-09-08 | `fix` | fix #3001 Selected node does not change color when rectangular selection is set. | `MapView.java` | [6f388967](https://github.com/freeplane/freeplane/commit/6f3889671b0fc577f44984c9a10b6f129c6451bb) |
| 2021-09-08 | `feature` | introduce new map version 1.9.8 (14) and remove node shape from selection style on older m | `mapVersions.xml`, `BigMap.mm` +21 | [b140b931](https://github.com/freeplane/freeplane/commit/b140b9312f44e332db97547f21efcace93e7f3a9) |
| 2021-09-08 | `fix` | Fix undo for delete style actions | `DeleteLevelStyleAction.java`, `DeleteUserStyleAction.java` | [3cd842c5](https://github.com/freeplane/freeplane/commit/3cd842c597dbf0938085ad2e4cd076c629e73a00) |
| 2021-09-08 | `fix` | use std err for severe log messages because it is required for bug reporting | `LogInitializer.java` | [a825a003](https://github.com/freeplane/freeplane/commit/a825a003ccda6857eb8e46a28b18cc88c60ca8a3) |
| 2021-09-04 | `api_change` | script API MindMap.copyStyleFrom, MindMap.copyStyleConditionsFrom | `ConditionalStyleModel.java`, `LogicalStyleController.java` +3 | [d3a3125e](https://github.com/freeplane/freeplane/commit/d3a3125e27693bc467d47698e39bdcfecaab9407) |
| 2021-08-30 | `feature` | add floating style to displayed user styles | `MapStyleModel.java` | [8153e6de](https://github.com/freeplane/freeplane/commit/8153e6de6180225291249cd4e13c57abcd5571d5) |
| 2021-08-29 | `fix` | fix https://github.com/freeplane/freeplane/issues/225 | `NoteManager.java` | [6c96fabf](https://github.com/freeplane/freeplane/commit/6c96fabf1031890027ae3d8b14bfde603939c920) |
| 2021-08-28 | `fix` | fix url host, use "" instead of null | `FileOpener.java`, `Hyperlink.java` +2 | [22a7fd4c](https://github.com/freeplane/freeplane/commit/22a7fd4c95f14bc6e7fc00ddf3e9db461872b66d) |
| 2021-08-21 | `fix` | fix NPE | `MapStyleModel.java` | [34455c73](https://github.com/freeplane/freeplane/commit/34455c73785b321ae82463e87a5ddfca34b7fd9b) |
| 2021-08-21 | `feature` | remove new style node from template on undo | `MapStyle.java` | [8a3aa8f5](https://github.com/freeplane/freeplane/commit/8a3aa8f5473741a9d73029536ff1e801cffe7d88) |
| 2021-08-21 | `fix` | fix NPE | `MapStyle.java` | [82b186aa](https://github.com/freeplane/freeplane/commit/82b186aa47da2fae1815c6e70d21cd67021cd093) |
| 2021-08-20 | `fix` | fix pdf export removing font search un user directory performed by fop | `Resources_de.properties`, `Resources_es.properties` +22 | [1cd87dfe](https://github.com/freeplane/freeplane/commit/1cd87dfef08fb030b4a3acf7dd8c0c74c0726d4c) |
| 2021-08-13 | `feature` | Add element to add new user style to style selection box | `MapStyleModel.java`, `MLogicalStyleController.java` +3 | [c3654bfe](https://github.com/freeplane/freeplane/commit/c3654bfebd4f50742b37a1a990f9b2407bfa6c55) |
| 2021-08-13 | `fix` | fix NPE | `TemplateManager.java` | [96958eb4](https://github.com/freeplane/freeplane/commit/96958eb4d15c36dd0e313b4b54b7873c1e65bc25) |
| 2021-08-07 | `fix` | Fix https://github.com/freeplane/freeplane/issues/223 | `MMapController.java` | [b0441d04](https://github.com/freeplane/freeplane/commit/b0441d04c8faf294f0f6e13bdafe7384253a6312) |
| 2021-08-07 | `feature` | fix creating of new user templates | `TemplateManager.java` | [54dd629e](https://github.com/freeplane/freeplane/commit/54dd629e2f3fb98c45875e9c6b8ba684e44dc15e) |
| 2021-08-06 | `fix` | fix ManageAssociatedMindMapsDialog | `ManageAssociatedMindMapsDialog.java` | [e5e5cca3](https://github.com/freeplane/freeplane/commit/e5e5cca3ab8760f50c1c1e394923d5f244cdbb19) |
| 2021-08-01 | `fix` | fix text | `ManageAssociatedMindMapsDialog.java` | [c16b41ac](https://github.com/freeplane/freeplane/commit/c16b41ac8e06b8681098be99a8994d9b77a108df) |
| 2021-08-01 | `fix` | fix translation | `MindMapPreviewWithOptions.java`, `Resources_en.properties` | [40ccbae3](https://github.com/freeplane/freeplane/commit/40ccbae3cbfd4edb539520bd49c716cf41138a50) |
| 2021-08-01 | `feature` | add checkbox for associated templates | `MFileManager.java`, `TemplateChooser.java` +2 | [e3ca92bc](https://github.com/freeplane/freeplane/commit/e3ca92bc27eb98559f42f3af1bc2c60fb5737180) |
| 2021-08-01 | `feature` | refactor, add methods | `TemplateManager.java` | [4158fd36](https://github.com/freeplane/freeplane/commit/4158fd3605a8fb44f362997d134a768b783739cc) |
| 2021-07-28 | `fix` | bug fix: center selected node was sometimes ignored | `MapView.java` | [df60e1c0](https://github.com/freeplane/freeplane/commit/df60e1c01dd97f108518d1125b38dc3a0fb9ddd3) |
| 2021-07-28 | `fix` | bug fix: center selected node was sometimes ignored | `MapView.java` | [7f0cfea2](https://github.com/freeplane/freeplane/commit/7f0cfea25e026b15d985e58bea7147acc3b0eb2e) |
| 2021-07-28 | `fix` | #2987 Link to local folder, file stopped working: fix handling of relative paths in hyperl | `UrlManager.java` | [b7ebb59a](https://github.com/freeplane/freeplane/commit/b7ebb59a730b3098da848680463c659525315353) |
| 2021-07-25 | `fix` | fix concurrent modification exception | `NodeModel.java` | [bb2e0abd](https://github.com/freeplane/freeplane/commit/bb2e0abde3ec4b8fe4f63e467e61c7b572e94e6a) |
| 2021-07-25 | `fix` | fix style selector placement on formatting panel | `StyleControlGroup.java` | [3d864007](https://github.com/freeplane/freeplane/commit/3d8640076aec470bc95677bb17edb5a69b0f2434) |
| 2021-07-25 | `fix` | bug fix: don't update deleted views | `MapView.java` | [afdf28dd](https://github.com/freeplane/freeplane/commit/afdf28ddeb0f46198ee5915423e5f00b86f410c2) |
| 2021-07-25 | `fix` | bug fix: don't update deleted views | `MapView.java` | [c0047564](https://github.com/freeplane/freeplane/commit/c004756450c6881ecebc396f05ba215ccbc5d712) |
| 2021-07-24 | `fix` | fix CloudColorShapeControlGroup layout | `CloudColorShapeControlGroup.java` | [4f758ae0](https://github.com/freeplane/freeplane/commit/4f758ae0245f18343ef395c29feae1d7a462ea25) |
| 2021-07-19 | `feature` | add "Preferences->" and "Icons->" to copied items | `CommandSearchDialog.java`, `IconItem.java` +4 | [c6cb2313](https://github.com/freeplane/freeplane/commit/c6cb23133a11ca31bb13567aa6bab13350dd8214) |
| 2021-07-19 | `feature` | add "Preferences->" and "Icons->" to copied items | `CommandSearchDialog.java`, `IconItem.java` +4 | [82ee585a](https://github.com/freeplane/freeplane/commit/82ee585a44286db90247802e449189f8f251a3ff) |
| 2021-07-18 | `feature` | add RedefineStyleUpdateTemplateAction to menu | `mindmapmodemenu.xml` | [c6574920](https://github.com/freeplane/freeplane/commit/c65749207e0c72197ad32e6174b617073742101c) |
| 2021-07-17 | `api_change` | #2976 Freeplane API documentation is not accesible | `ApplicationViewController.java` | [201fcf5d](https://github.com/freeplane/freeplane/commit/201fcf5dc717964e069e5cbc347a15a1f6a305e7) |
| 2021-07-17 | `fix` | fix creation of hyperlinks with arbitrary URIs by TypeReference | `TypeReference.java` | [a01bca2b](https://github.com/freeplane/freeplane/commit/a01bca2b97794782f50d30428ad45bbcb10cd86f) |
| 2021-07-11 | `fix` | bug fix for blinking nodes, keep html view size after foreground color change | `ScaledHTML.java`, `ZoomableLabelUI.java` | [236cd644](https://github.com/freeplane/freeplane/commit/236cd6441af815c4fc50b4411a621c16f451dc2f) |
| 2021-07-07 | `fix` | fix typo | `Resources_en.properties` | [7754079b](https://github.com/freeplane/freeplane/commit/7754079b38c4ff55d99ecdc78ee1f867ff139146) |
| 2021-06-29 | `api_change` | Remove deprecates API calls in tests | `EventTest.java`, `MemoryTest.java` +28 | [0b00408b](https://github.com/freeplane/freeplane/commit/0b00408b78fd6e687387ee661011a1cff7b27d93) |
| 2021-06-28 | `fix` | fix selection of last visited node if it is the root node | `LastOpenedList.java` | [b0ac11f1](https://github.com/freeplane/freeplane/commit/b0ac11f1b57b9606e7c6f4923a715da654b4f2da) |
| 2021-06-28 | `fix` | fix xml export | `mm2xml.xsl` | [38d8db4f](https://github.com/freeplane/freeplane/commit/38d8db4f64746983a0141571aa93289f4d8eebe6) |
| 2021-06-28 | `fix` | fix if # is contained in path | `MLinkController.java` | [d75238ef](https://github.com/freeplane/freeplane/commit/d75238ef5280af97e938ee9df38cbf927b98adb7) |
| 2021-06-28 | `fix` | Bug fix: filter applied only to visbile nodes should also consider visible ancestors and d | `Filter.java` | [de6e6eaa](https://github.com/freeplane/freeplane/commit/de6e6eaa8a9c4bd1974f06fa9110b6a0006e3234) |
| 2021-06-27 | `fix` | fix it and allow custom hyperlinks | `Hyperlink.java`, `TypeReference.java` +15 | [cccd2fc0](https://github.com/freeplane/freeplane/commit/cccd2fc06998c54fcdd8a74d23f73226f6838325) |
| 2021-06-27 | `fix` | fix compile error | `OpenCurrentMapDirAction.java` | [d87a23a9](https://github.com/freeplane/freeplane/commit/d87a23a977ef2cbae5dd8916d27146387e235cd1) |
| 2021-06-19 | `fix` | Fix GlobalNodes: ignore nodes deleted from the map | `FilterIterator.java`, `GlobalNodes.java` | [68f7cc2e](https://github.com/freeplane/freeplane/commit/68f7cc2e4529ef4dbc0889a8759052134c5edac0) |
| 2021-06-19 | `fix` | fix copying nodes from other maps | `INodeDuplicator.java`, `MapModel.java` +3 | [bca22f6f](https://github.com/freeplane/freeplane/commit/bca22f6f6d0495292598cf396aa2d671e2a433d7) |
| 2021-06-15 | `fix` | fix it | `MMapController.java`, `MTextController.java` | [bba6d140](https://github.com/freeplane/freeplane/commit/bba6d14046148a805b53cd073d2d77af1b5b3773) |
| 2021-06-15 | `feature` | try to simplify new node editing logic | `MMapController.java`, `MTextController.java` | [489e0153](https://github.com/freeplane/freeplane/commit/489e0153c7cfd6a40524bd52fd6664203ae65484) |
| 2021-06-13 | `fix` | fix for X11 / linux | `MMapController.java`, `MTextController.java` | [bd8220d0](https://github.com/freeplane/freeplane/commit/bd8220d024e02e9f8ae1f51224d61b1ecb1136f2) |
| 2021-06-13 | `feature` | #2727 First accented letter in a new node | `MTextController.java` | [ddc1e679](https://github.com/freeplane/freeplane/commit/ddc1e67903144f2c5ef3cb0797254117c81d42ab) |
| 2021-06-13 | `fix` | fix name | `FreeScrollAction.java` | [667a2f9a](https://github.com/freeplane/freeplane/commit/667a2f9aafd488d90bc9e60d41d2169496634516) |
| 2021-06-12 | `fix` | fix valid bounds calculation | `MapOverviewImageMouseHandler.java` | [50645a11](https://github.com/freeplane/freeplane/commit/50645a11538a65fcde925181489c83b4e3026332) |
| 2021-06-12 | `fix` | #2959 fix map zoom | `MapScroller.java` | [7c256e1d](https://github.com/freeplane/freeplane/commit/7c256e1d8c3b0c7267e3a0b6c630394386be3086) |
| 2021-06-11 | `fix` | fix java applet | `kitfox-svg-salamander-1.1.1-p1.jar`, `TextUtils.java` +11 | [e18c46d5](https://github.com/freeplane/freeplane/commit/e18c46d5feec5d79d44d22e8eff6c1824d6dc59c) |
| 2021-06-11 | `fix` | #2954 Fix scanner configuration for fr-CH | `ScannerController.java` | [d56b409e](https://github.com/freeplane/freeplane/commit/d56b409ef197e6e9a409adf303e2cce37e551aa3) |
| 2021-06-07 | `fix` | fix zooming center point above the overview map | `MapOverviewImageMouseHandler.java` | [b913c6dc](https://github.com/freeplane/freeplane/commit/b913c6dc61c41552ee228d418b8936a77c834334) |
| 2021-06-04 | `fix` | fix NPE: the color in the event can be null | `MapViewPane.java` | [ca0b3783](https://github.com/freeplane/freeplane/commit/ca0b378322f1e53c14972916a91db87efd03a997) |
| 2021-06-03 | `fix` | fix handling of links with empty paths | `UrlManager.java` | [b7b0a7eb](https://github.com/freeplane/freeplane/commit/b7b0a7ebb83cc7863ce2e68d99324b842814c1a9) |
| 2021-06-03 | `fix` | Fix selection of map parent directory as a link | `LinkController.java` | [56b2c5b3](https://github.com/freeplane/freeplane/commit/56b2c5b3f42bcb3824e39ff5f1933219a937fcf8) |
| 2021-06-03 | `fix` | bug fixes | `MapOverviewImage.java`, `MapViewPane.java` | [78a2db3a](https://github.com/freeplane/freeplane/commit/78a2db3a6a31a619af6b66c8ecab02509c57a94c) |
| 2021-06-03 | `fix` | fix editor background colors on VAqua | `NoteStyleAccessor.java`, `MNoteController.java` +9 | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-06-02 | `feature` | map overview: add popup menuitem for hide current instance | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +4 | [418452e3](https://github.com/freeplane/freeplane/commit/418452e3ab91ce1a3cd1b5e3d4a2379ae4b4d78f) |
| 2021-05-31 | `feature` | set action as map change listener | `OpenCurrentMapDirAction.java` | [e52e730e](https://github.com/freeplane/freeplane/commit/e52e730e44a0bc379cf1e8dfac4f351d5e8d54ad) |
| 2021-05-31 | `feature` | add open current map directory action | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +4 | [cfdfa780](https://github.com/freeplane/freeplane/commit/cfdfa78032fbc6d393b175018d5f89e5036eb2ca) |
| 2021-05-31 | `fix` | minor visual adjustment | `MapOverviewImage.java`, `MapViewPane.java` +1 | [b0a18027](https://github.com/freeplane/freeplane/commit/b0a180276eaac8d44aace140762060d9b4b3f23c) |
| 2021-05-28 | `fix` | fix compat issues on MacOsX | `MapViewPane.java` | [a8fb28c1](https://github.com/freeplane/freeplane/commit/a8fb28c1cf750ce4f47e1e944a3af7b8b74b36c6) |
| 2021-05-27 | `feature` | add map free scroll / node selection actions | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +7 | [59a8aff7](https://github.com/freeplane/freeplane/commit/59a8aff7154b85871bed21f66c08d0ab799186e6) |
| 2021-05-27 | `fix` | fix a few translations | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +2 | [bdcdf9dd](https://github.com/freeplane/freeplane/commit/bdcdf9ddfe46a64572ae2250b5952c4c02b19dd9) |
| 2021-05-27 | `feature` | add actions for overview resetting | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +4 | [ea792452](https://github.com/freeplane/freeplane/commit/ea7924529f06f590d1cee88c0c04f5ec65bbacd4) |
| 2021-05-27 | `feature` | support overview map move & resize | `MapViewPane.java`, `freeplane.properties` | [c81417ef](https://github.com/freeplane/freeplane/commit/c81417efcc1a49bf712396adae16dd7b0118d08a) |
| 2021-05-24 | `feature` | #2945 FP 193 02: cannot close FP & not open a map | `NamedIcon.java` | [89e09e42](https://github.com/freeplane/freeplane/commit/89e09e42540f36f61b8c2a98d8ebb6b2c9e0b34b) |
| 2021-05-24 | `fix` | #2943 fix bad property | `MapStyle.java`, `MFileManager.java` | [850a7edc](https://github.com/freeplane/freeplane/commit/850a7edc8b41595873929a05f790cde4c8feb2e9) |
| 2021-05-24 | `fix` | #2943 fix bad property | `MapStyle.java`, `MFileManager.java` | [56ccc526](https://github.com/freeplane/freeplane/commit/56ccc5261641a264e2caf9703233514e79a8f34d) |
| 2021-05-24 | `feature` | add missing parameter | `FixedSizeUIIcon.java` | [392d6582](https://github.com/freeplane/freeplane/commit/392d65828e22c3923bf47495bb49f6b4322a286c) |
| 2021-05-24 | `fix` | Simplify and fix MapOverview | `GraphicsHints.java`, `MapOverview.java` +1 | [9faad789](https://github.com/freeplane/freeplane/commit/9faad789fc35ddf59f9f202f87ebceec31e91c4a) |
| 2021-05-23 | `fix` | fix fullscreen under linux | `FrameController.java` | [518a6d5a](https://github.com/freeplane/freeplane/commit/518a6d5a743041627d9830e3ba1db0d90435543e) |
| 2021-05-22 | `fix` | Fix accelerators on IconSelection | `IconSelectionPopupDialog.java`, `freeplane.properties` | [72a8303a](https://github.com/freeplane/freeplane/commit/72a8303a1deca6fe83791efa3c36a96d69bfc2e6) |
| 2021-05-22 | `fix` | fix icons in docu maps | `freeplaneUserGuide.mm`, `freeplaneUserGuide_ja.mm` +5 | [99be0add](https://github.com/freeplane/freeplane/commit/99be0add3c14fb65e69b3e68ff47646e277a2947) |
| 2021-05-21 | `fix` | Fix isWindowTranslucencySupported check | `FreeplaneSplashModern.java` | [9c20226e](https://github.com/freeplane/freeplane/commit/9c20226e96bc67f6ca413facb49ada00fc3a821d) |
| 2021-05-21 | `fix` | fix NPE | `LinkController.java` | [cb5e1438](https://github.com/freeplane/freeplane/commit/cb5e1438a417beeea0f08d16a29cc7f817d95736) |
| 2021-05-21 | `fix` | Fix NPE if linkDecoration.ini was deleted by user | `LinkDecorationConfig.java`, `NodeViewDecorator.java` | [c33a756d](https://github.com/freeplane/freeplane/commit/c33a756d89fcd81325763b9d48236e19ac4563d2) |
| 2021-05-21 | `fix` | fix malformed translation in zh_CN | `Resources_zh_CN.properties` | [e2657e53](https://github.com/freeplane/freeplane/commit/e2657e53d8585f00c2f2497bb2bee0f0f6207b5e) |
| 2021-05-21 | `feature` | fix minimap MapChangeListener add/remove | `MiniMapView.java` | [7224347b](https://github.com/freeplane/freeplane/commit/7224347bf451a9db3d54b575cfea9e12a0fba539) |
| 2021-05-21 | `fix` | minor fix minimap position | `MiniMapView.java` | [5542dbc0](https://github.com/freeplane/freeplane/commit/5542dbc01e7445dabd5c510f41a799cd6d93bb17) |
| 2021-05-21 | `fix` | fix minimap wheel zoom bounding algorithm | `MiniMapView.java` | [cd3b6ee4](https://github.com/freeplane/freeplane/commit/cd3b6ee46346bb28685bf7104a1dbb83bdda6938) |
| 2021-05-20 | `fix` | fix minimap minor issues | `MiniMapView.java` | [5a0f180b](https://github.com/freeplane/freeplane/commit/5a0f180b91c5e7c6531b55fdbae2ab6e00232eb8) |
| 2021-05-20 | `feature` | optimize minimap painting further | `MiniMapView.java` | [7483bfba](https://github.com/freeplane/freeplane/commit/7483bfbaac8ea9f47318052d67f2e472f06dcea2) |
| 2021-05-19 | `feature` | add map changing listener for minimap update | `MiniMapView.java` | [60384cd9](https://github.com/freeplane/freeplane/commit/60384cd9e95b7ec1d972e0718d14ac6d4a9029bd) |
| 2021-05-18 | `fix` | fix image scaling algorithm & check against image out-of-bounds | `MiniMapView.java` | [a4ed9a79](https://github.com/freeplane/freeplane/commit/a4ed9a79e74f2e09444952d571941383fdaae991) |
| 2021-05-18 | `fix` | Fix minimap viewport calculation & mouse event processing | `MiniMapView.java` | [edfc0216](https://github.com/freeplane/freeplane/commit/edfc021663f32e44afd3ca3e6dc528236005d6a3) |
| 2021-05-18 | `fix` | fix minimap thumbnail algorithm | `MiniMapView.java` | [84484b87](https://github.com/freeplane/freeplane/commit/84484b87b3f3a5184fde957677847fd5e81f3916) |
| 2021-05-18 | `fix` | fix minimap thumbnail algorithm | `MiniMapView.java` | [acea3b8b](https://github.com/freeplane/freeplane/commit/acea3b8b08963be3d93113365934287225c30396) |
| 2021-05-17 | `feature` | mapview: add minimap for easy navigation | `Resources_zh_CN.properties`, `Resources_zh_TW.properties` +9 | [7ba634ae](https://github.com/freeplane/freeplane/commit/7ba634aed2ff8c5b34d430987e8c046e2b568b6a) |
| 2021-05-11 | `fix` | translation: [zh_CN] fix missing keys (translate me) | `Resources_zh_CN.properties` | [99bfa0ea](https://github.com/freeplane/freeplane/commit/99bfa0ea4acca9bb04979a240d7f381f851ea0b9) |
| 2021-05-09 | `feature` | Add menu options to move selected node to top/bottom/corner | `filemodemenu.xml`, `mindmapmodemenu.xml` +4 | [b9d9151b](https://github.com/freeplane/freeplane/commit/b9d9151b8f8fa6bd379fe63c2761917d8ba90c7d) |
| 2021-05-07 | `api_change` | use direct access to sun.awt.shell.ShellFolder  instead of reflection API | `build.gradle`, `JFreeplaneCustomizableFileChooser.java` | [1f31746b](https://github.com/freeplane/freeplane/commit/1f31746bb0e5a341897ddb7ead35e5204a6332d0) |
| 2021-05-07 | `fix` | #2923 fix generated HTML and visible subtree check for leaf nodes | `NodeModel.java` | [0b9a788f](https://github.com/freeplane/freeplane/commit/0b9a788f2b4a1ad583ae459eeb85c7124c072cdf) |
| 2021-05-07 | `fix` | #2923 fix generated HTML and visible subtree check for leaf nodes | `NodeModel.java` | [6846ec3c](https://github.com/freeplane/freeplane/commit/6846ec3c62a1e43c1ee7845ec53f4e848fa7c4f8) |
| 2021-05-01 | `feature` | #2920 add borders to Markdown table | `ModeController.java`, `MarkdownRenderer.java` | [5edf77c9](https://github.com/freeplane/freeplane/commit/5edf77c9523afab976e43cc825102e256be055f4) |
| 2021-05-01 | `feature` | Enable filtering on link decoration icons | `IconContainedCondition.java`, `LinkController.java` | [af84d730](https://github.com/freeplane/freeplane/commit/af84d73051bfa280b3703396d5e88f7436088288) |
| 2021-04-24 | `fix` | fix undo / redo transactions for node style editor | `EditStylesAction.java`, `SModeController.java` | [5f66e50f](https://github.com/freeplane/freeplane/commit/5f66e50f1b16f3d7f975216fab15ee69d3710a82) |
| 2021-04-23 | `fix` | fix setting full screen on non macs | `FrameController.java` | [2d46d2b0](https://github.com/freeplane/freeplane/commit/2d46d2b0de375383c2fca690ed716aa1cb790df8) |
| 2021-04-17 | `feature` | do not copy compiled add-ons from older version | `UserPropertiesUpdater.java` | [aab01134](https://github.com/freeplane/freeplane/commit/aab01134c63640188f60d399c31a9faa4fab3c5f) |
| 2021-04-16 | `fix` | fix menu bars in non aqua looks and feels for MacOS | `FreeplaneMenuBar.java`, `mac.dist.gradle` | [9342e939](https://github.com/freeplane/freeplane/commit/9342e9391fe4590048d1912e11685d882c683c9f) |
| 2021-04-16 | `fix` | fix vaqua look and feel for macos | `MapViewDockingWindows.java` | [4e803eac](https://github.com/freeplane/freeplane/commit/4e803eac38dd176b49d38694288827bd7b059e3c) |
| 2021-04-11 | `fix` | fix NPE | `MMapClipboardController.java` | [15d8e05b](https://github.com/freeplane/freeplane/commit/15d8e05b78edc60de0e784763846104f5b37e4ff) |
| 2021-04-05 | `fix` | Fix note panel CSS | `NoteManager.java` | [3d819baf](https://github.com/freeplane/freeplane/commit/3d819baff2118b9514185818bf88d42ababa4ed7) |
| 2021-04-04 | `feature` | Add zoom levels 80%, 90%, 110%, 120% | `MapViewController.java`, `freeplane.properties` | [f63cf3eb](https://github.com/freeplane/freeplane/commit/f63cf3eb5fef695e0dcb05f34a38d4d18e642c89) |
| 2021-04-04 | `feature` | Add option to configure which images referenced from html are copied on paste | `build.gradle`, `preferences.xml` +6 | [4bbbbfe8](https://github.com/freeplane/freeplane/commit/4bbbbfe807f3477c3aadd7b6120d6d08b985903f) |
| 2021-04-04 | `feature` | add enum simple class name to property name in resources | `Resources_af.properties`, `Resources_ar.properties` +74 | [463128be](https://github.com/freeplane/freeplane/commit/463128bee5f9972e9307c656bae9529e9cb7e1e8) |
| 2021-04-02 | `fix` | Fix saving and reading of content type | `ContentSyntax.java` | [648299c3](https://github.com/freeplane/freeplane/commit/648299c30cfc46bddbcd124d3ac3f5b8dcfed076) |
| 2021-03-27 | `feature` | Add options for zooming | `preferences.xml`, `MapScroller.java` +3 | [89d81039](https://github.com/freeplane/freeplane/commit/89d810396c26d6815acba5f7e65947f925c82d7f) |
| 2021-03-21 | `feature` | Add warning for first PDF export | `Resources_en.properties`, `ExportPdf.java` | [7a921d80](https://github.com/freeplane/freeplane/commit/7a921d80cd7a2f286968a9c1154a3b221f13c48a) |
| 2021-03-21 | `fix` | fix image scaling for MacOS  when transform.scale != 1 | `BitmapViewerComponent.java` | [fa530feb](https://github.com/freeplane/freeplane/commit/fa530feb149270f6223eb75467718aaf140a9604) |
| 2021-03-20 | `fix` | deploy with Java15 to fix default MacOS look and feel (non vaqua) | `Compat.java`, `FrameController.java` +2 | [bd677400](https://github.com/freeplane/freeplane/commit/bd677400946069d063841d33b455843b4cb780ad) |
| 2021-03-19 | `feature` | Add option to show link specific icons | `preferences.xml`, `NodeViewDecorator.java` +2 | [2e55a22e](https://github.com/freeplane/freeplane/commit/2e55a22e352bd2778bf20771a12090a27481a6c3) |
| 2021-03-19 | `fix` | fix default edge and node widths | `EdgeBuilder.java`, `EdgeController.java` +5 | [960f2308](https://github.com/freeplane/freeplane/commit/960f23080bafae69ed2380362045ce321f50f408) |
| 2021-03-15 | `fix` | fix java 8 compatibility | `MIconController.java` | [05f497c3](https://github.com/freeplane/freeplane/commit/05f497c30fb3604987876057e08753fb0d6d14c9) |
| 2021-03-14 | `feature` | Don't add undo actors when undo is already running | `MModeController.java` | [23ddf6de](https://github.com/freeplane/freeplane/commit/23ddf6dee8bab1b0e442ca60219d8645b99d3f06) |
| 2021-03-14 | `feature` | Add options to ManageFollowedMindMap dialog | `MapStyle.java`, `ManageFollowedMindMapAction.java` +2 | [12d35921](https://github.com/freeplane/freeplane/commit/12d35921abf8196cef1a948bd24119c64d7724ac) |
| 2021-03-14 | `feature` | add background colors to exported maps | `NodeModel.java`, `MindMapHTMLWriter.java` | [41cb9646](https://github.com/freeplane/freeplane/commit/41cb96465fbcc3a8bf13339b9bc5aaa073be27a7) |
| 2021-03-13 | `feature` | Add option to show special folders in file chooser | `preferences.xml`, `JFreeplaneCustomizableFileChooser.java` +2 | [42aba012](https://github.com/freeplane/freeplane/commit/42aba012e52eb8bd00d54b77c89ab1ea338f3729) |
| 2021-03-13 | `fix` | fix UI icon scaling for MacOS  when transform.scale != 1 | `FixedSizeUIIcon.java` | [13678026](https://github.com/freeplane/freeplane/commit/13678026dd9739b703bc4bb86bce6e166254e5eb) |
| 2021-03-07 | `feature` | #2551 Simple but useful feature, Format > Copy format to new child | `Resources_af.properties`, `Resources_cs.properties` +31 | [c42849a1](https://github.com/freeplane/freeplane/commit/c42849a1d720f275388fbefd1af6a456f1b6f0e7) |
| 2021-03-07 | `feature` | Option to enforce modal editor dialogs | `preferences.xml`, `EditNodeDialog.java` +4 | [e30072b5](https://github.com/freeplane/freeplane/commit/e30072b59691a0cfe8393094c8e09bf0d3c976a5) |
| 2021-03-07 | `fix` | fix bug in menu factory | `MenuBuildProcessFactory.java` | [453f41f1](https://github.com/freeplane/freeplane/commit/453f41f1f535ab0c8971918fcaa245f86e03c4ae) |
| 2021-03-07 | `fix` | fix build on non macs | `Compat.java`, `MacChanges.java` | [9ae94486](https://github.com/freeplane/freeplane/commit/9ae94486c9d26bd241d34936d5ce2b2090aec36c) |
| 2021-03-05 | `feature` | Implement full screen for macos | `UIComponentVisibilityDispatcher.java`, `Compat.java` +2 | [ac65f59e](https://github.com/freeplane/freeplane/commit/ac65f59e2bb388a54abf18715806e8763b0c81bb) |
| 2021-03-05 | `feature` | Implement full screen for macos | `Compat.java`, `FrameController.java` +1 | [dce3f671](https://github.com/freeplane/freeplane/commit/dce3f671eef0887be7f416445bf42cf097dd5b0e) |
| 2021-03-05 | `fix` | fix node popup builder | `MenuBuildProcessFactory.java` | [ef7a050d](https://github.com/freeplane/freeplane/commit/ef7a050deb8479cd47f66b5bce01348f61536fd0) |
| 2021-03-05 | `fix` | fix radio button ui builders | `JRadioButtonGroupComponentRemover.java`, `MenuBuildProcessFactory.java` | [b5c3136c](https://github.com/freeplane/freeplane/commit/b5c3136c686185dbaf01db68398c2271df5823bc) |
| 2021-03-04 | `fix` | Initialize all UI components in event queue to fix issues with VAqua L&F | `FreeplaneGUIStarter.java` | [be3a4dd7](https://github.com/freeplane/freeplane/commit/be3a4dd7414aca51af951ea1b1719671c8596672) |
| 2021-02-28 | `fix` | fix web and web_ssl linkDecoratin icons | `linkDecoration.ini` | [0691c97b](https://github.com/freeplane/freeplane/commit/0691c97bedbc855dacdebea6877d937a6001eeb6) |
| 2021-02-28 | `fix` | fix skip template selection | `MFileManager.java` | [be754a75](https://github.com/freeplane/freeplane/commit/be754a753d99a7dc72f8448ba63fbdaba0813f63) |
| 2021-02-28 | `fix` | fix xhtml generation | `HtmlUtils.java`, `NoteWriter.java` +1 | [c7077d2e](https://github.com/freeplane/freeplane/commit/c7077d2ed7b89a00267d1866f4dea68452d69838) |
| 2021-02-27 | `fix` | fix NPE | `ImagePreview.java` | [f054be0a](https://github.com/freeplane/freeplane/commit/f054be0aceca5a59576aed4b9fa44b2af1fb8c04) |
| 2021-02-27 | `fix` | fix NPE | `NodeTextBuilder.java` | [273f2aa9](https://github.com/freeplane/freeplane/commit/273f2aa9b4cda4102ac4716cf97d96060653f958) |
| 2021-02-27 | `fix` | fix opening of files under mac os | `Browser.java`, `freeplane.properties` | [ab46a602](https://github.com/freeplane/freeplane/commit/ab46a6022f985d4ae59fafd7c00b7991ba7f62da) |
| 2021-02-27 | `feature` | update single backup directory to new version and improve PathProperty to keep placeholder | `PathProperty.java`, `TextUtils.java` +4 | [0ee73f92](https://github.com/freeplane/freeplane/commit/0ee73f92683aa65840494575f823f6a5795108dc) |
| 2021-02-27 | `fix` | Change blocking editor implementation | `EditNodeBase.java`, `MTextController.java` +1 | [12d6b70b](https://github.com/freeplane/freeplane/commit/12d6b70bf03d9bcabcd5977f0a0769ff04238c0b) |
| 2021-02-27 | `feature` | add control to default alt+char accelerators on mac os | `ActionAcceleratorManager.java` | [cb744bf2](https://github.com/freeplane/freeplane/commit/cb744bf288e98377b63af9e3ede0060a4da741e4) |
| 2021-02-21 | `fix` | fix wrong note update on node change | `NoteManager.java`, `NotePanel.java` | [ad086c86](https://github.com/freeplane/freeplane/commit/ad086c86ec1df102e6afe80aac94b7566f94ca34) |
| 2021-02-21 | `feature` | #2878 FP 190 04: move branch to a new map - not working | `MapStyle.java` | [6eb72594](https://github.com/freeplane/freeplane/commit/6eb725941249f3dd06a4276640d145042d113ac3) |
| 2021-02-21 | `fix` | fix NPE | `MNoteController.java` | [3e5211ca](https://github.com/freeplane/freeplane/commit/3e5211ca15d083acaae340fa1c917f35c6eabfd1) |
| 2021-02-21 | `feature` | #2877 add translations for markdown preferences | `Resources_es.properties`, `Resources_fr.properties` +6 | [06fbf85f](https://github.com/freeplane/freeplane/commit/06fbf85f1d39cb57002c423d19f461baa0a63356) |
| 2021-02-13 | `fix` | fix note panel needsSaving condition | `NotePanel.java` | [fc967775](https://github.com/freeplane/freeplane/commit/fc9677752675551d941c6d186a76c29ce13aafb9) |
| 2021-02-13 | `feature` | Add markdown levels as lists as suggested in https://github.com/freeplane/freeplane/pull/1 | `mm2markdown.xsl` | [3e7b7a17](https://github.com/freeplane/freeplane/commit/3e7b7a1774cf939954d35fc414c7b65821226ed8) |
| 2021-02-13 | `fix` | Fix initial loading of maps following other map styles | `MFileManager.java`, `MapLoader.java` | [1eac3489](https://github.com/freeplane/freeplane/commit/1eac3489d2a0ce8bf076c7e1dd8ff97b47554864) |
| 2021-02-13 | `fix` | fix event handling on NotePanel editors | `NotePanel.java` | [d073c754](https://github.com/freeplane/freeplane/commit/d073c754cc70a332e915357ec4f359217064e2ff) |
| 2021-02-12 | `fix` | fix NotePanel | `NotePanel.java` | [55ccda15](https://github.com/freeplane/freeplane/commit/55ccda153a9c9639abd57b8ed38a361461657e85) |
| 2021-02-05 | `fix` | fix compile error | `MindMapHTMLWriter.java` | [fa80b3c8](https://github.com/freeplane/freeplane/commit/fa80b3c8540be90259e4bb5296e0ad278ed14d28) |
| 2021-02-05 | `fix` | fix export | `NoteWriter.java`, `NodeTextBuilder.java` | [2d51268d](https://github.com/freeplane/freeplane/commit/2d51268dbc33dbc7f4d1fce52a8c42a2795a7e97) |
| 2021-02-05 | `fix` | fix latex output in transformed core | `NodeTextBuilder.java` | [c6824e39](https://github.com/freeplane/freeplane/commit/c6824e39eac48b5870bf16c2f04b099f6661dfcc) |
| 2021-02-05 | `feature` | add VAqua to installed looks and feels if available | `FrameController.java` | [2888d2a6](https://github.com/freeplane/freeplane/commit/2888d2a66b73d80ffc961f7cd7433b0739eeabae) |
| 2021-02-05 | `feature` | add paragraph separators for node and details | `MindMapHTMLWriter.java` | [76cc3762](https://github.com/freeplane/freeplane/commit/76cc3762c18b73c6250823d741530f5df9fece95) |
| 2021-01-31 | `fix` | fix decorator icon size | `LinkController.java` | [d757dd9f](https://github.com/freeplane/freeplane/commit/d757dd9ff486eac925362336a99b5fe9c61975f9) |
| 2021-01-31 | `fix` | fix spelling | `MIconController.java` | [8b880a35](https://github.com/freeplane/freeplane/commit/8b880a35029731dad34ea2254000e56a076d3290) |
| 2021-01-31 | `fix` | fix freeplane.properties | `freeplane.properties` | [0a994998](https://github.com/freeplane/freeplane/commit/0a9949988f801fff20cbe8e6d736c62c96454760) |
| 2021-01-31 | `fix` | fix laf name | `FrameController.java` | [c6222d90](https://github.com/freeplane/freeplane/commit/c6222d90ce55bdfb7cba56e66c25377829be6fa3) |
| 2021-01-31 | `fix` | Fix visual glitch caused by using mask in generic file icon | `file_Java.svg`, `file_XML.svg` +18 | [54141674](https://github.com/freeplane/freeplane/commit/5414167437d81de57468789a1e804aa5a1aa69ef) |
| 2021-01-29 | `fix` | fix check for last link configuration file modification time | `LinkDecorationConfig.java` | [5f86916a](https://github.com/freeplane/freeplane/commit/5f86916a2d63e4ae0ebd205f8b7ecd6461c5483e) |
| 2021-01-24 | `feature` | change action description to "Add connector style" | `Resources_en.properties` | [a8c496e4](https://github.com/freeplane/freeplane/commit/a8c496e464d98af90f476098c12f3f3a1396c50c) |
| 2021-01-24 | `fix` | fix content type specific editor start for note panel | `NotePanel.java` | [bdb4fcc8](https://github.com/freeplane/freeplane/commit/bdb4fcc8fae57a93b5174781a532e518822848af) |
| 2021-01-24 | `fix` | try to fix case where standard icons are not available | `JFileChooserWithSystemFileIcons.java` | [855760ab](https://github.com/freeplane/freeplane/commit/855760ab451612a76e35f37674a4482501548140) |
| 2021-01-22 | `fix` | fix loading user icons | `IconStore.java`, `IconStoreFactory.java` | [64757b97](https://github.com/freeplane/freeplane/commit/64757b9703d063758ab745b0c75651b65f75d14c) |
| 2021-01-17 | `fix` | fix note and detail tooltips | `NoteController.java`, `TextController.java` | [6b4bc054](https://github.com/freeplane/freeplane/commit/6b4bc054d27ea079968062d712ece79982df8153) |
| 2021-01-17 | `fix` | fix rendering | `FormatContentTransformer.java`, `MainView.java` +4 | [0c305a86](https://github.com/freeplane/freeplane/commit/0c305a867024a10fc23a8d8d07572fd669f419e8) |
| 2021-01-16 | `fix` | fix note views in maps | `MainView.java`, `NodeViewFactory.java` +4 | [b72ceda3](https://github.com/freeplane/freeplane/commit/b72ceda36165440f7e142cc9ea89b11cf4eb8c39) |
| 2021-01-16 | `feature` | implement different editor/viewers in note panel | `NoteManager.java`, `NotePanel.java` | [e76e85cc](https://github.com/freeplane/freeplane/commit/e76e85cc605487e5e692fdbe018a7657f1f56ab5) |
| 2021-01-16 | `fix` | fix split panel divider location | `ApplicationViewController.java` | [ac5b962c](https://github.com/freeplane/freeplane/commit/ac5b962cdd2ead4a614f26a48449e7bd9a2f0d3e) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | `NoteDialogStarter.java`, `RichTextModel.java` +9 | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |
| 2021-01-11 | `feature` | add connector style examples | `BigMap.mm`, `BuzanMap.mm` +3 | [d3195db6](https://github.com/freeplane/freeplane/commit/d3195db6d9edd58fe93666eb81d2df532c60dd37) |
| 2021-01-11 | `feature` | improve new templates and create new previews | `BigMap.svg`, `BuzanMap.svg` +32 | [03413eb5](https://github.com/freeplane/freeplane/commit/03413eb5f3c2f5a718f7c37329ef90f1239311a9) |
| 2021-01-11 | `feature` | replace freeplane app icons by new artwork  by Stuart Robertson | `Freeplane_app_menu_128.png`, `Freeplane_frame_icon.png` +12 | [1965cfa0](https://github.com/freeplane/freeplane/commit/1965cfa0f26a11df397b02455909a95911ac144a) |
| 2021-01-09 | `feature` | refactor file chooser: add new ways of customization | `JFileChooserWithSystemFileIcons.java`, `JFreeplaneCustomizableFileChooser.java` +3 | [e7c247d5](https://github.com/freeplane/freeplane/commit/e7c247d598e2dfda3e9714e09ff93a5da2615aa8) |
| 2021-01-07 | `fix` | fix NPE | `ConnectorView.java`, `InclinationRecommender.java` | [39c0d02d](https://github.com/freeplane/freeplane/commit/39c0d02d0a6fdaae2cbad60d1dcf6b5019e3a3c4) |
| 2021-01-07 | `fix` | fix test | `QuantityShould.java`, `QuantityTest.java` | [1731c019](https://github.com/freeplane/freeplane/commit/1731c019388fac43832716259b37a03b6a586518) |
| 2021-01-07 | `fix` | fix test | `QuantityShould.java`, `QuantityTest.java` | [02c8422b](https://github.com/freeplane/freeplane/commit/02c8422b30b325880aa169c8281851807b1bcc06) |
| 2021-01-07 | `feature` | implement CopyMapStyles | `Resources_af.properties`, `Resources_cs.properties` +38 | [833086bf](https://github.com/freeplane/freeplane/commit/833086bf6e64ab4c04d05dd1a7d716aef8e1d54c) |
| 2021-01-07 | `feature` | introduce interface INodeDuplicator and add operation duplicate on nodes | `XmlImporter.java`, `INodeDuplicator.java` +14 | [63fca871](https://github.com/freeplane/freeplane/commit/63fca871c8305e7418d15443033fced1f40dc2c8) |
| 2021-01-04 | `feature` | add icon search to icon selection | `IconSelectionPopupDialog.java` | [7d2d3571](https://github.com/freeplane/freeplane/commit/7d2d3571f39ff0fc6f168ffb67db55974e9ee8d7) |
| 2021-01-03 | `fix` | fix NPE | `JCalendar.java` | [46b958fb](https://github.com/freeplane/freeplane/commit/46b958fb70ecbd605b0616e76eefb897bf994a2d) |
| 2021-01-01 | `feature` | add decoration icons contributed by Stuart Robertson (Copyrights to be clarified) | `linkDecoration.ini`, `DecoratedMail.svg` +87 | [06970056](https://github.com/freeplane/freeplane/commit/06970056fdfc9f4daca6523405aecf28ab1185d6) |
| 2021-01-01 | `feature` | Add filter based on connector styles | `ConnectorChecker.java`, `ConnectorCondition.java` +7 | [372bde33](https://github.com/freeplane/freeplane/commit/372bde33d9ebedde7030b25b0ebce6deeffe5e08) |

### Dettagli commit con note

**[1bc18512](https://github.com/freeplane/freeplane/commit/1bc18512c3beaccf8f722c210fead5d6060aa658)** (2021-11-14) — Fix NPE

> java.lang.NullPointerException
> 	at org.freeplane.features.styles.MapStyleModel.getStyleNodeGroup(MapStyleModel.java:484)
> 	at org.freeplane.features.styles.MapStyleModel.getNodeStyles(MapStyleModel.java:359)
> 	at org.freeplane.features.styles.mindmapmode.ConditionalStyleTable$1.getTableCellEditorComponent(ConditionalStyleTable.java:118)
> 	at javax.swing.JTable.prepareEditor(Unknown Source)
> 	at javax.swing.JTable.editCellAt(Unknown Source)
> 	at java.awt.WaitDispatchSupport.enter(Unknown Source)
> 	at java.awt.Dialog.show(Unknown Source)
> 	at javax.swing.JOptionPane.showOptionDialog(Unknown Source)
> 	at javax.swing.JOptionPane.showConfirmDialog(Unknown Source)
> 	at javax.swing.JOptionPane.showConfirmDialog(Unknown Source)
> 	at org.freeplane.features.styles.mindmapmode.ManageNodeConditionalStylesAction.actionPerformed(ManageNodeConditionalStylesAction.java:60)
> 	at org.freeplane.core.ui.AccelerateableAction.actionPerformed(AccelerateableAction.java:93)
> 	at java.awt.Component.setVisible(Unknown Source)
> 	at java.awt.Window.setVisible(Unknown Source)
> 	at java.awt.Dialog.setVisible(Unknown Source)
> 	at org.freeplane.main.mindmapmode.stylemode.EditStylesAction.actionPerformed(EditStylesAction.java:89)
> 	at javax.swing.SwingUtilities.notifyAction(Unknown Source)

**[3cd842c5](https://github.com/freeplane/freeplane/commit/3cd842c597dbf0938085ad2e4cd076c629e73a00)** (2021-09-08) — Fix undo for delete style actions

> STDERR: java.lang.NullPointerException
> STDERR: at org.freeplane.features.styles.MapStyleModel.isUserStyleNode(MapStyleModel.java:99)
> STDERR: at org.freeplane.features.styles.MapStyleModel.addStyleNode(MapStyleModel.java:293)
> STDERR: at org.freeplane.main.mindmapmode.stylemode.DeleteLevelStyleAction$1.undo(DeleteLevelStyleAction.java:68)

**[0b00408b](https://github.com/freeplane/freeplane/commit/0b00408b78fd6e687387ee661011a1cff7b27d93)** (2021-06-29) — Remove deprecates API calls in tests

> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>

**[e52e730e](https://github.com/freeplane/freeplane/commit/e52e730e44a0bc379cf1e8dfac4f351d5e8d54ad)** (2021-05-31) — set action as map change listener

> which captures new map saving event thus enabling the action

**[b0a18027](https://github.com/freeplane/freeplane/commit/b0a180276eaac8d44aace140762060d9b4b3f23c)** (2021-05-31) — minor visual adjustment

> 1. think border line drawing removed (less distractive), corner/center
>    points retained as minimum visual indicators (visibility)
> 2. border operational area expanded (easier interaction)
> 3. indicator text (anchor & zoom level) reduced color alpha and font size
>    (less distractive), indicator bounds recalculated in terms of font metrics
>    (visibility)
> 4. overview location (layout) fixed (bug)
> 5. border drawing minor fix (for visibility)

**[a8fb28c1](https://github.com/freeplane/freeplane/commit/a8fb28c1cf750ce4f47e1e944a3af7b8b74b36c6)** (2021-05-28) — fix compat issues on MacOsX

> 1. MOVE_CURSOR won't show, use HAND_CURSOR instead
> 2. Paint emoji char (anchor '⚓') won't work, use '+' instead
> 3. Overview border background fixed
> 4. Paint location minor adjustment

**[ea792452](https://github.com/freeplane/freeplane/commit/ea7924529f06f590d1cee88c0c04f5ec65bbacd4)** (2021-05-27) — add actions for overview resetting

> 1. Reset to corresponding attaching origin by menu action or mouse
>    right double click corresponding corner point
> 2. Set attach point by menu actions or mouse left double click
>    four corner points

**[c81417ef](https://github.com/freeplane/freeplane/commit/c81417efcc1a49bf712396adae16dd7b0118d08a)** (2021-05-27) — support overview map move & resize

> 1. default to 320x320 anchor to SW; bounds persisted
> 2. resizable (border center points / corner points);
> 3. movable (other places of the border);
> 4. switch anchor point (origin point) by double clicking corner points.

**[89e09e42](https://github.com/freeplane/freeplane/commit/89e09e42540f36f61b8c2a98d8ebb6b2c9e0b34b)** (2021-05-24) — #2945 FP 193 02: cannot close FP & not open a map

> java.lang.ClassCastException: org.freeplane.features.icon.UserIcon
> cannot be cast to java.lang.Comparable
> 	at java.util.TreeMap.compare(Unknown Source)
> 	at java.util.TreeMap.put(Unknown Source)
> 	at java.util.TreeSet.add(Unknown Source)
> 	at java.util.AbstractCollection.addAll(Unknown Source)
> 	at java.util.TreeSet.addAll(Unknown Source)
> 	at org.freeplane.features.icon.hierarchicalicons.AccumulatedIcons.addAccumulatedIconsToTreeSet(AccumulatedIcons.java:55)
> 	at org.freeplane.features.icon.hierarchicalicons.AccumulatedIcons.setStyleCheckForChange(AccumulatedIcons.java:69)
> 	at org.freeplane.features.icon.hierarchicalicons.HierarchicalIcons$1.lambda$getStateIcon$0(HierarchicalIcons.java:59)
> 	at java.util.Iterator.forEachRemaining(Unknown Source)
> 	at java.util.Spliterators$IteratorSpliterator.forEachRemaining(Unknown
> Source)
> 	at java.util.stream.ReferencePipeline$Head.forEach(Unknown Source)

**[5a0f180b](https://github.com/freeplane/freeplane/commit/5a0f180b91c5e7c6531b55fdbae2ab6e00232eb8)** (2021-05-20) — fix minimap minor issues

> 1. slow down wheel zoom a bit
> 2. display zoom level in fullscreen mode (SW corner)
> 3. update minimap border color value from event.NewValue
>    rather than from MapView.getBackground() since view
>    is not updated yet

**[7483bfba](https://github.com/freeplane/freeplane/commit/7483bfbaac8ea9f47318052d67f2e472f06dcea2)** (2021-05-20) — optimize minimap painting further

> 1. only update minimap if visible
> 2. create minimap ImageIcon only once, redraw on its graphics if
>    updating is needed

**[acea3b8b](https://github.com/freeplane/freeplane/commit/acea3b8b08963be3d93113365934287225c30396)** (2021-05-18) — fix minimap thumbnail algorithm

> 1. Translate and scale origianl map view into a square image;
> 2. Translate and scale the inner bounds, expand it to a square;
> 3. Then crop the image with the square;
> 4. Scale the square image to fixed size.

**[648299c3](https://github.com/freeplane/freeplane/commit/648299c30cfc46bddbcd124d3ac3f5b8dcfed076)** (2021-04-02) — Fix saving and reading of content type

> #2898 FP 1.9.0 alpha 12: Content Type formatting bug

**[e30072b5](https://github.com/freeplane/freeplane/commit/e30072b59691a0cfe8393094c8e09bf0d3c976a5)** (2021-03-07) — Option to enforce modal editor dialogs

> #2888 Problem with the new feature (Non blocking editing of node core,
> details and notes in dialogs) added in (1.8.11)

**[ac65f59e](https://github.com/freeplane/freeplane/commit/ac65f59e2bb388a54abf18715806e8763b0c81bb)** (2021-03-05) — Implement full screen for macos

> #2884 Keyboard shortcut for "Full screen mode" gives mac beach ball

**[dce3f671](https://github.com/freeplane/freeplane/commit/dce3f671eef0887be7f416445bf42cf097dd5b0e)** (2021-03-05) — Implement full screen for macos

> #2884 Keyboard shortcut for "Full screen mode" gives mac beach ball

**[12d6b70b](https://github.com/freeplane/freeplane/commit/12d6b70bf03d9bcabcd5977f0a0769ff04238c0b)** (2021-02-27) — Change blocking editor implementation

> try to fix #2870 Stops responding to keyboard input inside map itself


---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-30 | `fix` | fix svg colors | `Darcula-1.7.svg`, `conceptMap.svg` +12 | [0eb408ad](https://github.com/freeplane/freeplane/commit/0eb408ad1f27dd0b489aa66927331081df7843c7) |
| 2020-12-30 | `feature` | can not create map inside transaction #181 | `AttributeManagerDialog.java`, `MModeController.java` +1 | [38e4e4c6](https://github.com/freeplane/freeplane/commit/38e4e4c6f0b235c0f82487b74a9dec74e455ad89) |
| 2020-12-30 | `fix` | fix default connector views and map repaint on map style update | `MapView.java`, `ConnectorView.java` +2 | [a84395b1](https://github.com/freeplane/freeplane/commit/a84395b1979b7c1b877afbcda942e3e24f64f541) |
| 2020-12-30 | `feature` | support connectors saved in Freeplane 1.9.x | `TreeXmlReader.java` | [45956aa1](https://github.com/freeplane/freeplane/commit/45956aa14cc45d616ff182f8ed39eb2ee7f20f9d) |
| 2020-12-29 | `fix` | fix edge view | `preferences.xml`, `ConnectorModel.java` +4 | [b3885fa1](https://github.com/freeplane/freeplane/commit/b3885fa1e5cf336eb673313b01fc933a96474bf1) |
| 2020-12-28 | `fix` | refactor and fix | `ConnectorModel.java`, `ConnectorProperties.java` +7 | [4524cdf2](https://github.com/freeplane/freeplane/commit/4524cdf2ab86a562539a11bed302b6423cf6e95a) |
| 2020-12-27 | `fix` | Revert "fix for vaqua look and feel" | `UrlManager.java` | [b74e180f](https://github.com/freeplane/freeplane/commit/b74e180fc24b2117b5095a7f0ac6fbc2e5549d1e) |
| 2020-12-27 | `fix` | fix for vaqua look and feel | `UrlManager.java` | [e030c04e](https://github.com/freeplane/freeplane/commit/e030c04e957e826ac28811273bfffe90a1142d49) |
| 2020-12-26 | `fix` | Fix class-cast exception related to VAqua | `AttributeTable.java` | [c9b3bcfe](https://github.com/freeplane/freeplane/commit/c9b3bcfecf3fab3419d537716e45673d4110cd54) |
| 2020-12-26 | `feature` | fix MindMapPreview for new map creation | `MindMapPreview.java` | [5a84af56](https://github.com/freeplane/freeplane/commit/5a84af5696a9a80dda5e0b95731f98094a896fa9) |
| 2020-12-25 | `fix` | fix menu item search | `MenuItem.java` | [cd82043d](https://github.com/freeplane/freeplane/commit/cd82043d14c1aaeee65b22a44d7c5e7e579f306c) |
| 2020-12-25 | `feature` | add map templates and generated previews | `BigMap.svg`, `BuzanMap.svg` +34 | [a96cdcbc](https://github.com/freeplane/freeplane/commit/a96cdcbc182d56dc083a66052b87d77f36d8c7e2) |
| 2020-12-24 | `fix` | make latex editor non modal and fix blocking editor treatment | `NoteDialogStarter.java`, `EditNodeBase.java` +7 | [a6f20816](https://github.com/freeplane/freeplane/commit/a6f208166ce4b6dfe06327c0191a725bf6cc2048) |
| 2020-12-18 | `fix` | fix unfolding for hidden nodes | `FilterInfo.java`, `MapController.java` +1 | [eef3ddce](https://github.com/freeplane/freeplane/commit/eef3ddce404c0d5f0d44be5932830a3be0e25612) |
| 2020-12-13 | `fix` | fix length unit keys in translations | `Resources_af.properties`, `Resources_cs.properties` +28 | [0d60628f](https://github.com/freeplane/freeplane/commit/0d60628fb442bcc4810cc92eb2e51bf938086f47) |
| 2020-12-10 | `fix` | Fix default locale codes | `ApplicationResourceController.java` | [be7a6a1e](https://github.com/freeplane/freeplane/commit/be7a6a1ec85d5549b315dfa30a413fdfeb5d157f) |
| 2020-12-10 | `fix` | fix pt_BR translation | `Resources_pt_BR.properties` | [7b1969f7](https://github.com/freeplane/freeplane/commit/7b1969f7e35656d0afbeaa81dabed3503e475bc8) |
| 2020-12-07 | `fix` | fix cloud painting for hidden nodes | `NodeView.java` | [bcbc564e](https://github.com/freeplane/freeplane/commit/bcbc564e35b6f35924d6dc38f03ac8580f14c524) |
| 2020-12-06 | `fix` | fix cloud painting no hidden nodes | `NodeView.java` | [fbed9e57](https://github.com/freeplane/freeplane/commit/fbed9e579d519b2c0625ee312bb024442ff129eb) |
| 2020-12-06 | `feature` | New option to capitalize words on splitting | `preferences.xml`, `SplitToWordsAction.java` +2 | [b3198edc](https://github.com/freeplane/freeplane/commit/b3198edc15131f8f7f220a73f1c5cb973db66069) |
| 2020-12-06 | `feature` | Add some other shapes to menu | `mindmapmodemenu.xml`, `NodeShapeAction.java` | [95a28aa8](https://github.com/freeplane/freeplane/commit/95a28aa880c027c552dc6c7f74354d788e70d1fd) |
| 2020-11-06 | `fix` | fix compiler error | `CommandSearchDialog.java` | [5149cc6e](https://github.com/freeplane/freeplane/commit/5149cc6e087dc197305027dccb1122a3ca6a0aff) |
| 2020-11-06 | `fix` | Fix: close action could be disabled after mode change | `ActionStatusUpdater.java`, `CloseAction.java` +2 | [bd422808](https://github.com/freeplane/freeplane/commit/bd4228080bf2874f40cd2282748526fed378412e) |
| 2020-11-06 | `fix` | Fix change to mind map mode from file mode if no map is open | `MMapController.java`, `MModeController.java` +2 | [1d523649](https://github.com/freeplane/freeplane/commit/1d523649d5ea04fe9c6c0009f7388b3b4367ee7b) |
| 2020-11-06 | `feature` | Assign new accelerator from command search dialog if control is hold | `CommandSearchDialog.java`, `IconIndexer.java` +6 | [49fcd94e](https://github.com/freeplane/freeplane/commit/49fcd94e3680a4479b082929cbb48af87b9a5560) |
| 2020-11-04 | `fix` | fix toString and refactor | `IconItem.java`, `MenuItem.java` +2 | [12771882](https://github.com/freeplane/freeplane/commit/12771882810ea336e3bda310c5ed2fb1c6980372) |
| 2020-11-03 | `fix` | Fix word boundary search in Search Command dialog | `SearchItem.java` | [751f30e8](https://github.com/freeplane/freeplane/commit/751f30e81918b9251ebd036002a09eda2c8f27cd) |
| 2020-10-31 | `fix` | fix NPE | `NewMapViewAction.java` | [c0f8e0a8](https://github.com/freeplane/freeplane/commit/c0f8e0a807580c46dcdcc9c3482e80953c378952) |
| 2020-10-31 | `fix` | fix NPE | `FindAction.java` | [7e4dbdce](https://github.com/freeplane/freeplane/commit/7e4dbdce8230ce417d37ac5663be2fdb18377fd1) |
| 2020-10-31 | `fix` | fix NPE | `ApplicationResourceController.java` | [9edefd74](https://github.com/freeplane/freeplane/commit/9edefd74df29297dc4534e4f35ca2c50f533ce65) |
| 2020-10-24 | `feature` | #2837 Add-on's jar file removed when upgrading | `AddOnsController.java` | [3a0e0f2f](https://github.com/freeplane/freeplane/commit/3a0e0f2fe14d29eae423c61745cc705e64c0918a) |
| 2020-10-09 | `fix` | Revert "fix saving folding state for encrypted nodes" | `NodeWriter.java` | [1b3dc632](https://github.com/freeplane/freeplane/commit/1b3dc632f347d09b07c6d984622b268f34eaf8d8) |
| 2020-10-09 | `fix` | fix saving folding state for encrypted nodes | `NodeWriter.java` | [0518d1f0](https://github.com/freeplane/freeplane/commit/0518d1f07a72393a5f54eee259b266e3ba67c84e) |
| 2020-09-27 | `feature` | Add Finnish language | `freeplane.properties`, `Resources_en.properties` | [b47798a9](https://github.com/freeplane/freeplane/commit/b47798a991dc8119bab2861b8385c31c891f017c) |
| 2020-09-26 | `feature` | add file for Finnish translation | `Resources_fi.properties` | [d3827ba2](https://github.com/freeplane/freeplane/commit/d3827ba2e7f978484cb83e56e171a92048fd158c) |
| 2020-09-25 | `fix` | fix: call to repaint turned out to make scrolled map look not smooth | `MapScroller.java` | [06afa473](https://github.com/freeplane/freeplane/commit/06afa4731bca344692dd6a1650ffff3d719e98b2) |
| 2020-09-12 | `fix` | fix showing icon categories in selectMenuItemDialog | `MenuUtils.java`, `SelectMenuItemDialog.java` | [134da776](https://github.com/freeplane/freeplane/commit/134da77658f09bd8cabb5d20ac1047263aa448af) |
| 2020-09-05 | `fix` | typo fix | `Resources_en.properties` | [451329b0](https://github.com/freeplane/freeplane/commit/451329b0457edec27b31a28a1cdde36ce146c611) |
| 2020-08-24 | `fix` | bug fix: destroy accelerators for actions only if there are no more entries | `AcceleratorBuilder.java`, `AcceleratorDestroyer.java` +4 | [8fe35103](https://github.com/freeplane/freeplane/commit/8fe35103bd23fd0bafb070aab2eb069117e7b2a8) |
| 2020-08-21 | `feature` | command search: add option check boxes, fix small things | `Resources_de.properties`, `preferences.xml` +2 | [1c57e231](https://github.com/freeplane/freeplane/commit/1c57e231b97c1f2311369cc33787c85cd9b9e1e8) |
| 2020-08-15 | `fix` | bug fix | `IconItem.java` | [2061ed38](https://github.com/freeplane/freeplane/commit/2061ed3896bdbe114bc31ed8993fd2f4e38d91f2) |
| 2020-08-15 | `feature` | Implement IconItems | `CommandSearchDialog.java`, `IconIndexer.java` +8 | [c87b1c73](https://github.com/freeplane/freeplane/commit/c87b1c73df7e13bfdf5df2968969c02b44d5cc3e) |
| 2020-08-15 | `feature` | command search: start with icon support in command search | `Resources_de.properties`, `CommandSearchDialog.java` +2 | [d23cc061](https://github.com/freeplane/freeplane/commit/d23cc061270cfce04caee234794b4a65306c59aa) |
| 2020-08-12 | `feature` | command search: add mnemonics to scope radio buttons | `CommandSearchDialog.java` | [5519432b](https://github.com/freeplane/freeplane/commit/5519432b0f979c0e0d96fe5aa4f574af2f2c2ee0) |
| 2020-08-10 | `fix` | command search: fix German translation | `Resources_de.properties`, `Resources_en.properties` | [08f61b0f](https://github.com/freeplane/freeplane/commit/08f61b0f9efc77020edfe1e1e09fa1120719853b) |
| 2020-08-10 | `feature` | command search: add scope (backed by a preferences item), search for conjunction of search | `Resources_de.properties`, `preferences.xml` +2 | [393e4a70](https://github.com/freeplane/freeplane/commit/393e4a707cca151dcd02be7a9b602973d2faeb4a) |
| 2020-07-17 | `fix` | fix translation | `Resources_it.properties` | [6bc70632](https://github.com/freeplane/freeplane/commit/6bc70632a4580c434795ca910be3cefa0c47f902) |
| 2020-07-04 | `feature` | #2796 Add-on deinstallation fails to delete jar | `AddOnsController.java` | [de3c82e8](https://github.com/freeplane/freeplane/commit/de3c82e86d75d5c545a1fdf3e5ebf5d88fdfcf3d) |
| 2020-06-24 | `fix` | fix HTmlUtils, https://github.com/freeplane/freeplane/issues/164 | `HtmlUtils.java` | [0506f500](https://github.com/freeplane/freeplane/commit/0506f5006b45917f8b143ef3ed8f9b368385e8ba) |
| 2020-06-24 | `fix` | fix index out of bound exception | `FastAccessableIcons.java` | [69efae0a](https://github.com/freeplane/freeplane/commit/69efae0ae475691d650cac189d7247aae687c9f5) |
| 2020-06-19 | `fix` | fix npe | `UrlManager.java` | [22468288](https://github.com/freeplane/freeplane/commit/2246828850a9fc8618cfbcadc267fff2f27c5569) |
| 2020-06-18 | `feature` | command search: Remove html tags from prefs / menu item text, add Predrag's icon for menu  | `menu_items.svg`, `CommandSearchDialog.java` +2 | [dc5ae611](https://github.com/freeplane/freeplane/commit/dc5ae611a6c8a01f3c47a893b13e636de3508b36) |
| 2020-06-15 | `fix` | fix class casts exception | `CombinedConditions.java`, `ConjunctConditions.java` +1 | [81ca90f1](https://github.com/freeplane/freeplane/commit/81ca90f12c31ca9fdfd934753e77079f2e233197) |
| 2020-06-07 | `fix` | Continue to fix filter | `FilterController.java`, `Slide.java` | [724df4c9](https://github.com/freeplane/freeplane/commit/724df4c9ca5f2e7b2530bdd325f1b794bd4135c5) |
| 2020-06-06 | `fix` | fix menu definitions | `filemodemenu.xml`, `stylemodemenu.xml` +1 | [75a02699](https://github.com/freeplane/freeplane/commit/75a02699e63cd30455b493a8bc05c9f62edc893c) |
| 2020-06-06 | `fix` | fix menu definition | `mindmapmodemenu.xml` | [72ee6e6e](https://github.com/freeplane/freeplane/commit/72ee6e6e020d810240dd30f15ae1f04f52828e9f) |
| 2020-06-06 | `fix` | fix #2788 Can't remove or undo map filters created by script | `ApplyNoFilteringAction.java`, `FilterController.java` +4 | [cf0c8081](https://github.com/freeplane/freeplane/commit/cf0c80810882617efb79134c1b450b9b6cfd0c6f) |
| 2020-06-06 | `fix` | fix #2785 Filtering attributes not working | `ApplyNoFilteringAction.java`, `FilterController.java` +4 | [7078e26c](https://github.com/freeplane/freeplane/commit/7078e26c14c1bf5be13512da97235e34d6a6f331) |
| 2020-06-05 | `fix` | fix JFileChooserWithSystemFileIcons | `JFileChooserWithSystemFileIcons.java`, `FrameController.java` | [223e8cc5](https://github.com/freeplane/freeplane/commit/223e8cc5663f8ac30d36795400964aedc0bcf311) |
| 2020-06-05 | `fix` | Fix slow JFileChooser for windows by not using Windows icons | `OptionPanel.java`, `PathProperty.java` +18 | [80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be) |
| 2020-05-31 | `feature` | command search: rename from fpsearch, add license headers | `Resources_de.properties`, `mindmapmodemenu.xml` +15 | [610c5974](https://github.com/freeplane/freeplane/commit/610c59741d5636e9fcdf90356d01634cb74c5438) |
| 2020-05-23 | `feature` | fpsearch: add hot keys for menu items as tooltip, fix menu item component translation | `FPSearchDialog.java`, `MenuItem.java` +1 | [58a133ca](https://github.com/freeplane/freeplane/commit/58a133ca1e610c75cf613f1601393b4eb5059588) |
| 2020-05-22 | `fix` | fix failing gradle build (#160) | `build.gradle`, `MenuBuildProcessFactoryTest.java` +3 | [e1d6707f](https://github.com/freeplane/freeplane/commit/e1d6707ffd56e705fd68a2c24caf5f4cc44e5dcf) |
| 2020-05-22 | `fix` | bug fix https://sourceforge.net/p/freeplane/discussion/758437/thread/435909c14c/ | `CollapseableBoxBuilder.java`, `OneTouchCollapseResizer.java` | [4d68d684](https://github.com/freeplane/freeplane/commit/4d68d6840211c2018225a5654332f9fced60227b) |
| 2020-05-21 | `feature` | fpsearch: use icon for pref entries, add tooltips for pref items | `ShowPreferencesAction.java`, `FPSearchDialog.java` +2 | [e6f9a0e2](https://github.com/freeplane/freeplane/commit/e6f9a0e231cca1a3c3126874aeaebc486ce435bb) |
| 2020-05-20 | `fix` | fpsearch: fix scrolling via arrow keys | `FPSearchDialog.java` | [3bb41058](https://github.com/freeplane/freeplane/commit/3bb4105878fd3b5ddd8ae0de75a3b7966b37a560) |
| 2020-05-19 | `fix` | fpsearch: use DefaultListCellRenderer for default jlabel formatting, fix update of jlist a | `FPSearchDialog.java` | [574bee1c](https://github.com/freeplane/freeplane/commit/574bee1c46371efb54986107b7f9035044291613) |
| 2020-05-11 | `fix` | fpsearch: Fix double setVisible(), make dialog non-modal | `FPSearchAction.java`, `FPSearchDialog.java` | [d0770b63](https://github.com/freeplane/freeplane/commit/d0770b63f6249fd70cc75d04b2984683688c402f) |
| 2020-05-11 | `fix` | fpsearch: Fix menu indexer | `MenuStructureIndexer.java` | [2e219063](https://github.com/freeplane/freeplane/commit/2e21906328992622a5bd48691a2aa493d92cccbd) |
| 2020-05-11 | `fix` | fix menu item | `mindmapmodemenu.xml` | [e3103fa0](https://github.com/freeplane/freeplane/commit/e3103fa083617ac5e04769962714171fe4bb4469) |
| 2020-05-11 | `fix` | fix filter applied to visible nodes | `Filter.java`, `FilterController.java` +4 | [666a6831](https://github.com/freeplane/freeplane/commit/666a683140325b36341570c2971c0317c79f67f6) |
| 2020-05-11 | `fix` | fix filter operations | `Filter.java`, `FilterController.java` +1 | [0eb7a844](https://github.com/freeplane/freeplane/commit/0eb7a8448b50b95daecf31542347a6925130f772) |
| 2020-05-04 | `feature` | add Preference Items result table | `FPSearchDialog.java`, `MenuStructureIndexer.java` +1 | [3af009f5](https://github.com/freeplane/freeplane/commit/3af009f5e903175fc9959b27203c58cbbb7c3281) |
| 2020-05-03 | `feature` | add initial MenuStructureIndexer | `FPSearchDialog.java`, `MenuStructureIndexer.java` +1 | [92869fc2](https://github.com/freeplane/freeplane/commit/92869fc2ab14c0cb8116f38479d61b7c86c94d94) |
| 2020-05-01 | `fix` | fix test | `SummaryLevels.java` | [e3ce653b](https://github.com/freeplane/freeplane/commit/e3ce653bab1a4dbd9997b0f24e9817285fee194d) |
| 2020-05-01 | `fix` | fix menu name | `mindmapmodemenu.xml` | [08c94641](https://github.com/freeplane/freeplane/commit/08c946413e2c99182ec57e3f5dc97dffa213037c) |
| 2020-04-23 | `feature` | UI/UX project: add actions to tool bar | `mindmapmodemenu.xml`, `freeplane.properties` +1 | [4683f253](https://github.com/freeplane/freeplane/commit/4683f2530673e6a2f8ffec28a88b179d40482972) |
| 2020-04-23 | `api_change` | remove "advanced" and "beginner" user interface variants | `Resources_de.properties`, `Resources_es.properties` +23 | [7ae7d6a2](https://github.com/freeplane/freeplane/commit/7ae7d6a2bf3b5e1586ff3254d12d42f70c318332) |
| 2020-04-19 | `fix` | fix NPE | `AFilterComposerDialog.java` | [422441b3](https://github.com/freeplane/freeplane/commit/422441b3e2399e6636bb9acb2cbf689fc8859e54) |
| 2020-04-07 | `fix` | fix test | `JMenuItemBuilderTest.java` | [63ff444a](https://github.com/freeplane/freeplane/commit/63ff444a64f2934196202104c6271bece0085699) |
| 2020-04-04 | `fix` | fix approximate search | `PseudoDamerauLevenshtein.java` | [1a36c21d](https://github.com/freeplane/freeplane/commit/1a36c21d19796caf6a5a7ea773b5d5d861e9302c) |
| 2020-03-21 | `feature` | Do not create invisible (not allowed) menu items | `JMenuItemBuilder.java`, `JMenuRadioGroupBuilder.java` +1 | [e7385808](https://github.com/freeplane/freeplane/commit/e7385808403ecacc68e39231e4258cf3cb5ba661) |
| 2020-03-19 | `fix` | Fix popup listener call order (it is inverted) | `JMenuItemBuilder.java` | [59652835](https://github.com/freeplane/freeplane/commit/5965283546e90dfe85ac9304deb57bc37fb581b4) |
| 2020-03-19 | `fix` | fix tests | `RecursiveMenuStructureProcessorTest.java`, `MenuBuildProcessFactoryTest.java` | [2f6e24bb](https://github.com/freeplane/freeplane/commit/2f6e24bbb3dcde8e09cc5eeb0de4c7a705132302) |
| 2020-03-19 | `feature` | Create menu item components lazily (otherwise menu initialization on MacOS takes too long  | `EntryPopupListenerCollection.java`, `SubtreeProcessor.java` +7 | [88686eea](https://github.com/freeplane/freeplane/commit/88686eea1a3f1e0020fff2ff3659ce020adb063f) |
| 2020-03-19 | `fix` | fix SubtreeChildrenDefaultBuilder | `RecursiveMenuStructureProcessor.java` | [dea5e0e3](https://github.com/freeplane/freeplane/commit/dea5e0e3ae60c8af8c54fcc8fcaeee4c93f5e2d4) |
| 2020-03-19 | `fix` | Fix popup menus for MacOSx | `JMenuItemBuilder.java` | [fab1c8a9](https://github.com/freeplane/freeplane/commit/fab1c8a9595a4a96cccf86c68ed5486644248038) |
| 2020-03-14 | `feature` | #2497 "New Map View" should select the same nodes as current map view | `IMapViewChangeListener.java`, `MFileManager.java` +3 | [5189e3af](https://github.com/freeplane/freeplane/commit/5189e3afc6a299bfc18a4d0d7343bd3ffa971ce4) |
| 2020-03-12 | `feature` | #2496 If the style format is set to "Text", FP should not wait for formula when new node i | `MTextController.java` | [7daa8172](https://github.com/freeplane/freeplane/commit/7daa8172de063c483d5b034efa2babe594e9fa6f) |
| 2020-03-12 | `feature` | Add "ignore accents" to condition description | `AttributeContainsCondition.java`, `AttributeExistsCondition.java` +27 | [e1817286](https://github.com/freeplane/freeplane/commit/e181728634b7b8b07bdaff1ddcf857af757b3a2c) |
| 2020-03-12 | `fix` | bug fix | `NodeContainsCondition.java` | [36a0c3c9](https://github.com/freeplane/freeplane/commit/36a0c3c9ff046000ab3c483759606331e914adf0) |
| 2020-03-10 | `api_change` | wip remove caseInsensitive flag from StringMatchingStrategy API | `DamerauLevenshtein.java`, `EditDistanceStringMatchingStrategy.java` +3 | [a0c87a7c](https://github.com/freeplane/freeplane/commit/a0c87a7c94c08e8a3d78f6f8a6081cd2b5e78b6a) |
| 2020-03-08 | `feature` | improve filter to support continuous hiding | `Filter.java` | [68218718](https://github.com/freeplane/freeplane/commit/682187184a3d022dfc1b923444b730dd1f478149) |
| 2020-02-23 | `fix` | Fix hierarchical icon action icons | `HierarchicalIconsAction.svg`, `IconIntersectionHierarchy.svg` +2 | [80c2e93e](https://github.com/freeplane/freeplane/commit/80c2e93e9398228876e12682dbab37088b0e45d0) |
| 2020-02-22 | `api_change` | change text "simple interface" to "beginner interface" | `Resources_en.properties` | [6a45a4c2](https://github.com/freeplane/freeplane/commit/6a45a4c2ee0028322a90e7f166746e5bb2dbef5d) |
| 2020-02-22 | `feature` | Add summary nodes to beginner interface | `mindmapmodemenu.xml` | [64499255](https://github.com/freeplane/freeplane/commit/64499255a1e2394634dc34f087ff2ea373c3c3b9) |
| 2020-02-22 | `fix` | Fix SVG backgrounds | `BitmapViewerFactory.java`, `IViewerFactory.java` +3 | [02b5f924](https://github.com/freeplane/freeplane/commit/02b5f924779846aff5dd9bfcf7c126b84a55dbcb) |
| 2020-02-21 | `fix` | fix svg images | `BitmapViewerFactory.java`, `ExternalResource.java` +3 | [65d1fe0f](https://github.com/freeplane/freeplane/commit/65d1fe0f7cb233dc6d1baf30f394d606723ef8c0) |
| 2020-02-21 | `fix` | fix #2733 FP 180 4: reminder icons lost | `ImportAttributesDialog.java`, `freeplane.properties` | [80b08ea8](https://github.com/freeplane/freeplane/commit/80b08ea89737b0939695454627e2757f3b3700e1) |
| 2020-02-21 | `feature` | add file again | `Resources_oc.properties` | [c5d2ad69](https://github.com/freeplane/freeplane/commit/c5d2ad690be55f07acfab65da6e74f7557ff9a1a) |
| 2020-02-21 | `fix` | remove file to fix its mode | `Resources_oc.properties` | [226f086c](https://github.com/freeplane/freeplane/commit/226f086c523c0a1b2c0c7ca00e3fee9c1fdfaecc) |
| 2020-02-16 | `fix` | fix encoding | `Resources_oc.properties` | [c052dd57](https://github.com/freeplane/freeplane/commit/c052dd5783ecd710a33eabcc7ff6b61131481c45) |
| 2020-02-11 | `feature` | rename methods, add method HtmlUtils.textToHTML | `HtmlUtils.java`, `AboutAction.java` +13 | [adcdd4ac](https://github.com/freeplane/freeplane/commit/adcdd4ac97e67df07fc788e4882efbd43fe7f9fc) |
| 2020-01-26 | `fix` | #2725 fix user icon file URL | `UserIcon.java` | [3c932511](https://github.com/freeplane/freeplane/commit/3c932511f4f78a8d19b5894886c4431ec4b1dfc1) |
| 2020-01-20 | `fix` | fix java applet and java web start | `build.gradle`, `freeplane_applet.jnlp` +2 | [c61135a3](https://github.com/freeplane/freeplane/commit/c61135a3ef60639e3b10cc1c72447681fb10af62) |
| 2020-01-20 | `fix` | fix applet resources | `MoveToRootAction.png`, `fullscreen.png` +4 | [36c06225](https://github.com/freeplane/freeplane/commit/36c06225934e2ae0b6b8b403b9f90e99dc9d1665) |
| 2020-01-12 | `fix` | Fix it | `ToolbarLayout.java`, `FastAccessableIcons.java` | [66862e63](https://github.com/freeplane/freeplane/commit/66862e632dc84408370fea72886d2641b13c2140) |
| 2020-01-12 | `fix` | Fix: do not persist clone conditions | `FilterController.java`, `ASelectableCondition.java` +9 | [c42158cc](https://github.com/freeplane/freeplane/commit/c42158ccd8ea197387660806ea347444a04fc561) |
| 2020-01-12 | `fix` | Fix: do not persist clone conditions | `FilterController.java`, `ASelectableCondition.java` +9 | [ad02ef67](https://github.com/freeplane/freeplane/commit/ad02ef6763504a8eccb74affd19789f76b261d25) |
| 2020-01-11 | `fix` | Fix user icon rendering | `FixedSizeUIIcon.java`, `ConditionFactory.java` +2 | [e3b2b508](https://github.com/freeplane/freeplane/commit/e3b2b508f650e671f67715ee29029f1c87cda4a4) |
| 2020-01-11 | `feature` | Let IconSelectionPopupDialog support user icons | `IconSelectionPopupDialog.java`, `ToolbarLayout.java` +1 | [43c72a50](https://github.com/freeplane/freeplane/commit/43c72a5019dacfe3c11cf7222ef30376fe3bc6ee) |
| 2020-01-11 | `fix` | Fix: show user icons on the toolbar only once | `MIconController.java` | [68812ad0](https://github.com/freeplane/freeplane/commit/68812ad0933106f0e569f551a49e0cb39ce077e2) |
| 2020-01-10 | `fix` | fix map loading on mac app start | `FreeplaneGUIStarter.java`, `MacOptions.java` +1 | [0f6fb38f](https://github.com/freeplane/freeplane/commit/0f6fb38fa1f48db97b0c6706cd147f685822271b) |
| 2020-01-10 | `fix` | fix map loading on mac app start | `FreeplaneGUIStarter.java`, `MacOptions.java` +1 | [b1640a8b](https://github.com/freeplane/freeplane/commit/b1640a8b1637a96b6c3faa889e791ee6d61ad76a) |
| 2020-01-06 | `fix` | fix icon selection popup | `emoji.gradle`, `IconSelectionPopupDialog.java` +1 | [a9ffe9e9](https://github.com/freeplane/freeplane/commit/a9ffe9e99319c7e90e07d57ed6bc25fb8fb3f4a0) |
| 2020-01-06 | `fix` | bug fixes | `build.gradle`, `emoji.gradle` +11 | [67ad49a7](https://github.com/freeplane/freeplane/commit/67ad49a715d280fd4d27b9f6c9ae8e3c43e36f0b) |
| 2020-01-05 | `fix` | replace getPath by getFile and fix encoding | `Compat.java`, `IconBuilder.java` +4 | [58dd0d77](https://github.com/freeplane/freeplane/commit/58dd0d777161de768d670f935936c0f76038c609) |

### Dettagli commit con note

**[38e4e4c6](https://github.com/freeplane/freeplane/commit/38e4e4c6f0b235c0f82487b74a9dec74e455ad89)** (2020-12-30) — can not create map inside transaction #181

> https://github.com/freeplane/freeplane/issues/181

**[b74e180f](https://github.com/freeplane/freeplane/commit/b74e180fc24b2117b5095a7f0ac6fbc2e5549d1e)** (2020-12-27) — Revert "fix for vaqua look and feel"

> This reverts commit e030c04e957e826ac28811273bfffe90a1142d49.

**[1b3dc632](https://github.com/freeplane/freeplane/commit/1b3dc632f347d09b07c6d984622b268f34eaf8d8)** (2020-10-09) — Revert "fix saving folding state for encrypted nodes"

> This reverts commit 0518d1f07a72393a5f54eee259b266e3ba67c84e.

**[80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be)** (2020-06-05) — Fix slow JFileChooser for windows by not using Windows icons

> https://stackoverflow.com/a/59165208/1833472


---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-12-30 | `feature` | #2719 Combine Add image with change image | `Resources_af.properties`, `Resources_cs.properties` +32 | [c5c5512d](https://github.com/freeplane/freeplane/commit/c5c5512db1df9099e4bebf5ae2b9b912348089ea) |
| 2019-12-26 | `fix` | fix toolbar layout for hidden components | `ToolbarLayout.java` | [ceb6c006](https://github.com/freeplane/freeplane/commit/ceb6c00666bed59d30e5027b630d6856055d308c) |
| 2019-12-26 | `fix` | fix toolbar layout for hidden components | `ToolbarLayout.java` | [6f04d4aa](https://github.com/freeplane/freeplane/commit/6f04d4aac28c90cb0fa8dcf5595011c5518b41d9) |
| 2019-12-26 | `feature` | Add demo to play around | `LabelDemo.java` | [6d0bc26d](https://github.com/freeplane/freeplane/commit/6d0bc26d3b03e2e71f83565e26be6fa4903de6d9) |
| 2019-12-26 | `fix` | fix for bad or empty icons | `ZoomedIcon.java` | [947fc57e](https://github.com/freeplane/freeplane/commit/947fc57eb9b59551fa8d5256e823ada4c961855a) |
| 2019-12-25 | `fix` | fix test | `ActionStatusUpdater.java`, `ActionStatusUpdaterTest.java` | [07cd8a7a](https://github.com/freeplane/freeplane/commit/07cd8a7a4eaa6cf0a12e0b795fdf0b889840d9e9) |
| 2019-12-25 | `feature` | Add parent entry constraints to actions created by builder | `EntryAccessor.java` | [bf66c8fb](https://github.com/freeplane/freeplane/commit/bf66c8fb36c96a0d445d6ac32912c497c821bd4f) |
| 2019-12-25 | `feature` | force SIMPLE ui only for new users (if no preference file is available for current and for | `FreeplaneGUIStarter.java`, `freeplane.properties` | [9ec1767c](https://github.com/freeplane/freeplane/commit/9ec1767cd6d91569cffb0ca461d47d2589b1471e) |
| 2019-12-25 | `fix` | Fix icon size on icon action buttons | `IconSelectionPopupDialog.java`, `DefaultConditionRenderer.java` +3 | [ec4b6501](https://github.com/freeplane/freeplane/commit/ec4b650122f389b6fd63617186cd8def90598a2e) |
| 2019-12-25 | `feature` | Implement compare in NamedIcon | `NamedIcon.java`, `UIIcon.java` | [f7ebcb4f](https://github.com/freeplane/freeplane/commit/f7ebcb4fdfda1420a276ce795f883793f2dcb267) |
| 2019-12-25 | `fix` | fix broken Umlaut | `resource_de.properties` | [59f9f7ba](https://github.com/freeplane/freeplane/commit/59f9f7ba0e45a2d04dd6760324c3bfecffa43af1) |
| 2019-12-24 | `api_change` | finish user interface modes | `editmode.png`, `editmode.svg` +23 | [bc29a8d6](https://github.com/freeplane/freeplane/commit/bc29a8d683061cf38dd5c4a7e800cdfb464332a3) |
| 2019-12-24 | `fix` | Improve and fix SetStringPropertyAction and radio menu items | `SetStringPropertyAction.java`, `JAutoRadioButtonMenuItem.java` +2 | [ca95f458](https://github.com/freeplane/freeplane/commit/ca95f45875e6a95767f7346cc4c494f3cf765cc3) |
| 2019-12-24 | `fix` | fix it | `ModeController.java`, `MModeController.java` +31 | [76bc2508](https://github.com/freeplane/freeplane/commit/76bc2508a7174553300804c93e87c7a41aae50c7) |
| 2019-12-14 | `feature` | Add lock editing action item and add it to the tool bar | `lock_editing.png`, `lock_editing.svg` +3 | [0283cae8](https://github.com/freeplane/freeplane/commit/0283cae8e51fad7418994a54028281a489e935fa) |
| 2019-10-05 | `fix` | Fix named CloneOfSelectedView condition because it appears in filter compose editor | `CloneOfSelectedViewCondition.java` | [d14586ce](https://github.com/freeplane/freeplane/commit/d14586ced1d9fbb9facaa4b5401f26e0d56bfe1a) |
| 2019-10-05 | `fix` | fix start sequence | `CommandLineParser.java`, `ActivatorImpl.java` +1 | [9b84c570](https://github.com/freeplane/freeplane/commit/9b84c5708dee049e65aea0af589b8022621b8113) |
| 2019-10-04 | `fix` | Fix style map undo handler (NPE after editing styles) | `EditStylesAction.java` | [f5b42f5b](https://github.com/freeplane/freeplane/commit/f5b42f5bb27e4b7775eb69d8deb977689b825b06) |
| 2019-10-04 | `feature` | Add mnemonics to SelectedPasteAction | `SelectedPasteAction.java` | [aeb106e3](https://github.com/freeplane/freeplane/commit/aeb106e32ecc42d3fc5e4e27fabcd36f84ca00fc) |
| 2019-10-02 | `fix` | fix attribute table row heights for zoomed maps | `AttributeTable.java` | [6ffeaeb3](https://github.com/freeplane/freeplane/commit/6ffeaeb3ace3c59a8fe4d879d5fcac6bbb6ef420) |
| 2019-09-28 | `fix` | Fix table row heights after font scaling | `UITools.java`, `AttributeRegistryTable.java` +4 | [15384981](https://github.com/freeplane/freeplane/commit/15384981d8172c23ee2004eb05d286ba07802dde) |
| 2019-09-28 | `feature` | Add new properties  to connector API : dashArray, opacity, width, labelFontFamily and labe | `ColorUtils.java`, `LinkBuilder.java` +10 | [f4c86c81](https://github.com/freeplane/freeplane/commit/f4c86c8129390c482d1823494186137497d77f63) |
| 2019-09-25 | `feature` | fix isUndoAction: add map as parameter | `AutomaticEdgeColorHook.java`, `MapController.java` +7 | [23eb7e39](https://github.com/freeplane/freeplane/commit/23eb7e3971faf5066e8820129d72c47fcf220db6) |
| 2019-09-21 | `fix` | Fix Darcula ButtonUI | `FixDarculaToggleButtonUI.java`, `FrameController.java` | [289901c0](https://github.com/freeplane/freeplane/commit/289901c03a3debccaad47ccdc6953d76510dc808) |
| 2019-09-15 | `fix` | Fix darcula LAF loading | `ClassLoaderFactory.java`, `FrameController.java` | [b5e84b59](https://github.com/freeplane/freeplane/commit/b5e84b59b8b43fb235f27c504710cac879c2338b) |
| 2019-09-14 | `fix` | Fix dispatch thread logic for headless controller | `MModeController.java`, `FrameController.java` +2 | [931fd17f](https://github.com/freeplane/freeplane/commit/931fd17f0af8946862e6a51c4ec5e7a42af0fb8a) |
| 2019-09-14 | `feature` | Support dark mode | `build.gradle`, `history_en.txt` +9 | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2019-08-18 | `api_change` | getMainThreadExecutorService from freeplane API | `Controller.java`, `EventQueueExecutorServiceAdapter.java` +7 | [8663a7e0](https://github.com/freeplane/freeplane/commit/8663a7e01e35cee472753500169f58d9a38b59bc) |
| 2019-07-26 | `feature` | Support for data URLs as specified in RFC 2397 | `build.gradle`, `Handler.java` +5 | [d8ea124e](https://github.com/freeplane/freeplane/commit/d8ea124ed16b0409b63da98be7f067cd5cc49467) |
| 2019-05-26 | `fix` | #2682 Fix map statistics | `FilePropertiesAction.java` | [775558f6](https://github.com/freeplane/freeplane/commit/775558f63efc864cff8c22860690a91a9b1348b7) |
| 2019-05-25 | `feature` | add logging for case no lock for map writing file can be obtained | `MFileManager.java` | [503fadb9](https://github.com/freeplane/freeplane/commit/503fadb9bc2052b4ab3251b7effa05e678c87603) |
| 2019-05-11 | `fix` | Fix JOptionPane location  on startup | `FreeplaneGUIStarter.java` | [abc4c947](https://github.com/freeplane/freeplane/commit/abc4c947804a4b5966b3a54b6eb6be03294e9d4b) |
| 2019-05-01 | `fix` | fix file locking | `DummyLockManager.java`, `LockManager.java` | [9516b8de](https://github.com/freeplane/freeplane/commit/9516b8dea3f3a6a0e305ea9e1a90109d032bb5be) |
| 2019-04-07 | `fix` | Handle automatic bug reports | `MMapClipboardController.java`, `MapStyleModel.java` +5 | [8fba1ce3](https://github.com/freeplane/freeplane/commit/8fba1ce34fd74dc2e9dd66529891884f4d2b9467) |
| 2019-03-29 | `fix` | fix counting rows during attribute editing | `AttributeTable.java`, `ExtendedAttributeTableModelDecorator.java` | [a1ada31a](https://github.com/freeplane/freeplane/commit/a1ada31ae806c4aefd8490d00f73a55d0ab81264) |
| 2019-02-25 | `fix` | fix translation | `Resources_tr.properties` | [2546a6ad](https://github.com/freeplane/freeplane/commit/2546a6ada4538e3737d0e1571cd0e3231cbac624) |
| 2019-02-22 | `fix` | fix NPE | `UserInputListenerFactory.java` | [5df01dcd](https://github.com/freeplane/freeplane/commit/5df01dcdd811a814a5ca5daef4f9b16e0ca132e2) |
| 2019-02-22 | `fix` | fix NPE | `FilterConditionEditor.java` | [cb1c320c](https://github.com/freeplane/freeplane/commit/cb1c320c23d6c3852d9aab00747731f45a23f89d) |
| 2019-02-22 | `fix` | fix NPE | `MapViewDockingWindows.java` | [d4f2e6f6](https://github.com/freeplane/freeplane/commit/d4f2e6f615b67411b18cb073332af0c7c878db6e) |
| 2019-02-15 | `fix` | improve automatic bug report messages | `Resources_cs.properties`, `Resources_da.properties` +24 | [b6160e18](https://github.com/freeplane/freeplane/commit/b6160e18712100561c25a52db0918dce0a4d86ef) |
| 2019-02-15 | `fix` | fix NPE | `MNoteController.java` | [0d3b1230](https://github.com/freeplane/freeplane/commit/0d3b12307c072e41af3d23cd80a83ed378e546e8) |
| 2019-02-15 | `fix` | fix text key | `ExportDialog.java` | [d7da913f](https://github.com/freeplane/freeplane/commit/d7da913f27a7b634cc4c7363177c20856d75cc69) |
| 2019-02-15 | `fix` | fix NPE | `NodeView.java` | [583fbe80](https://github.com/freeplane/freeplane/commit/583fbe80ad56dc1715307cea26d8ceebb1cdf367) |
| 2019-02-15 | `fix` | fix NPE | `AddOnsController.java` | [c45e067c](https://github.com/freeplane/freeplane/commit/c45e067c39210331320e852ddd628dbd4d84903b) |
| 2019-02-15 | `fix` | Fix enabling / disabling of QuantityProperty editor components | `QuantityProperty.java` | [1e4ccf5e](https://github.com/freeplane/freeplane/commit/1e4ccf5eada985c9732974ed2f4b05aee27d9c7c) |
| 2019-02-09 | `fix` | try to fix NPE | `ColorTracker.java` | [dc6cfecd](https://github.com/freeplane/freeplane/commit/dc6cfecd8afd1189b080f34b4fdae2b040fa2aaf) |
| 2019-02-09 | `fix` | fix NPE | `ImageRendererFactory.java` | [c8e7a612](https://github.com/freeplane/freeplane/commit/c8e7a612dc7437a0a92495463e44f8be584261e3) |
| 2019-02-09 | `fix` | fix NPE | `AttributePanelManager.java` | [2c151008](https://github.com/freeplane/freeplane/commit/2c151008f8a585cc929a732ef05ab97236ac04f5) |
| 2019-01-27 | `fix` | Fix revision information | `FreeplaneVersion.java`, `AboutAction.java` +1 | [e9785084](https://github.com/freeplane/freeplane/commit/e9785084bbcbfa930bda682055bb42bcb5ba2e16) |
| 2019-01-27 | `feature` | add containsProperty method | `ResourceController.java` | [774e3e9b](https://github.com/freeplane/freeplane/commit/774e3e9bde7d9bdb482b226216cf63887da63dd7) |
| 2019-01-23 | `fix` | #2630 losing node after password | `EncryptionModel.java` | [e63839ed](https://github.com/freeplane/freeplane/commit/e63839edc3b6c9a0624214ccd510e70181ce497c) |
| 2019-01-20 | `fix` | fix javadoc | `TextUtils.java` | [6a12e609](https://github.com/freeplane/freeplane/commit/6a12e609d986e5876207ad199ca8f48df66be528) |
| 2019-01-08 | `api_change` | API for find operations including ancestors / descendants | `Filter.java`, `ControllerRO.java` +5 | [16e2a07c](https://github.com/freeplane/freeplane/commit/16e2a07cf07acf0ef1c54005c955dea44017d5f0) |
| 2019-01-08 | `feature` | #2645 FP174 (bf376d4) NullPointerException when installing add-on | `UITools.java` | [1e4809d1](https://github.com/freeplane/freeplane/commit/1e4809d10b1251c5bbeb461709c83362ba958b25) |
| 2019-01-04 | `fix` | fix tooltip maximum width | `TextualTooltipRendererFactory.java` | [82a2ab83](https://github.com/freeplane/freeplane/commit/82a2ab8303937655df50851042e1a8c3c04a7838) |
| 2019-01-04 | `fix` | fix row height calculation | `AttributeTable.java` | [b016a0a1](https://github.com/freeplane/freeplane/commit/b016a0a154fea9fab22af4290c90853ee4bf2b14) |

### Dettagli commit con note

**[e63839ed](https://github.com/freeplane/freeplane/commit/e63839edc3b6c9a0624214ccd510e70181ce497c)** (2019-01-23) — #2630 losing node after password

> fix calculation of encrypted content for locked nodes


---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-31 | `feature` | Fix #2386 Special characters in add-on translations wrongly displayed | `TextUtils.java` | [5dc15caa](https://github.com/freeplane/freeplane/commit/5dc15caa27bbb489f3498c129934055157dab4d5) |
| 2018-12-31 | `feature` | Fix #2386 Special characters in add-on translations wrongly displayed | `TextUtils.java`, `AddOnProperties.java` | [d3fa8d97](https://github.com/freeplane/freeplane/commit/d3fa8d97c65f75ca8c09e548622989a09ee52730) |
| 2018-12-30 | `fix` | fix reminder script execution | `ReminderHook.java`, `NodeListWithReminders.java` +2 | [797d2096](https://github.com/freeplane/freeplane/commit/797d2096d75139a6f52c7b533ff8f403ad79d751) |
| 2018-12-30 | `fix` | fix removing reminders | `ReminderHook.java`, `FlatNodeTableFilterModel.java` +1 | [aca4e6ef](https://github.com/freeplane/freeplane/commit/aca4e6ef4636951708356b85527bdd125d000245) |
| 2018-12-30 | `feature` | Add mnemonics to node list ui elements | `NodeList.java`, `NodeListWithReplacement.java` | [6c769594](https://github.com/freeplane/freeplane/commit/6c7695946314b15ac7450ad7d05f5f00c1c1274e) |
| 2018-12-30 | `feature` | new window title for past reminders | `NodeList.java`, `ShowPastRemindersOnce.java` +1 | [50ad5d69](https://github.com/freeplane/freeplane/commit/50ad5d699824b287950f3004f609eca99e148f9c) |
| 2018-12-30 | `fix` | bug fixes | `NodeList.java`, `ShowPastRemindersOnce.java` | [d23c1220](https://github.com/freeplane/freeplane/commit/d23c122074151ad2a73ccef4a8b63bb75dd2a423) |
| 2018-12-30 | `feature` | refactor: create NodeListWithReplacements as NodeList subclass | `ReminderHook.java`, `AllMapsNodeListAction.java` +4 | [6a46cfb2](https://github.com/freeplane/freeplane/commit/6a46cfb233c82c4ec5f6e32677136dcfecca16ce) |
| 2018-12-29 | `feature` | Add Freeplane API... action to open javadoc from help menu | `mindmapmodemenu.xml`, `OpenURLAction.java` +3 | [bd78c185](https://github.com/freeplane/freeplane/commit/bd78c1854667b4b536788cad217a26b28f46767f) |
| 2018-12-26 | `fix` | Fix parsing of attribute value | `MMapClipboardController.java` | [7282cd3c](https://github.com/freeplane/freeplane/commit/7282cd3cfe98de45390298e27a60cd15001bf19a) |
| 2018-12-26 | `feature` | support pasting of attributes from text in clipboard to existing node | `MMapClipboardController.java` | [91c07cb3](https://github.com/freeplane/freeplane/commit/91c07cb350d64adfea1b23c78984d917b99ac537) |
| 2018-12-25 | `fix` | Fix NPE in style editor due to missing components | `SModeControllerFactory.java`, `FreeplaneTooltip.java` +1 | [c64d6faa](https://github.com/freeplane/freeplane/commit/c64d6faaf0ae6094efd18dbdbcf64ddc994fb275) |
| 2018-12-24 | `fix` | fix svg in previews and tooltips | `ImageTooltipRendererFactory.java`, `SvgViewerFactory.java` | [971c4ae4](https://github.com/freeplane/freeplane/commit/971c4ae4df0bfab9cdbad63a398c8df55d6da26b) |
| 2018-12-19 | `feature` | Fix for #2386 Special characters in add-on translations wrongly displayed | `AddOnProperties.java` | [c9b7a8a2](https://github.com/freeplane/freeplane/commit/c9b7a8a2b4899e3a2d79bcf71a9bf12c4a1cbdb5) |
| 2018-12-12 | `fix` | Fix copying attributes if only subset is visible | `IAttributeTableModel.java`, `AttributeClipboardController.java` +3 | [3626838e](https://github.com/freeplane/freeplane/commit/3626838ef4b5c3b10dda353a49d3774785ff0d69) |
| 2018-11-25 | `feature` | Support selection of multiple cells in attribute tables | `HighlightedElements.java`, `AttributeController.java` +5 | [3a90c16b](https://github.com/freeplane/freeplane/commit/3a90c16bdb0bc7269676dc6897d76a04f5d87cc8) |
| 2018-11-24 | `fix` | Fix initialization of MMapExplorerController for headless mode | `HeadlessMModeControllerFactory.java` | [7df4f656](https://github.com/freeplane/freeplane/commit/7df4f656fa6e295a3bc3a3f843d82f2f81656061) |
| 2018-11-24 | `fix` | bug fix : save resizer state after expansion | `OneTouchCollapseResizer.java` | [1fd27afc](https://github.com/freeplane/freeplane/commit/1fd27afc69af638a5e61b9dfb17f5700ea171ef3) |
| 2018-11-07 | `feature` | Add template for mindmap to be exported to Beamer | `beamerMap.mm` | [bf93698c](https://github.com/freeplane/freeplane/commit/bf93698ce36130a6f8a54ec610f98391fc442cfb) |
| 2018-10-29 | `feature` | Enable listings env in beamer template + fix extraction of fragile att | `mm2latexbeamer_richcontent_1.3.x.xsl` | [c57a5f5b](https://github.com/freeplane/freeplane/commit/c57a5f5bdf2598f11fac326c5f06de485751ff5c) |
| 2018-10-28 | `feature` | Add synchronized blocks for loading maps in different threads | `MClipboardController.java`, `MapReader.java` +1 | [7d855786](https://github.com/freeplane/freeplane/commit/7d8557861c7e49ce64372713ceeae9c38d8f4bc2) |
| 2018-10-28 | `fix` | fix file lock release on map restore | `MapController.java`, `MapModel.java` +3 | [1f2aa14d](https://github.com/freeplane/freeplane/commit/1f2aa14d930c9316c176908b53c00ea9ded2ad90) |
| 2018-10-20 | `fix` | fix mind map file locking | `MMapModel.java`, `MMapIO.java` +3 | [3d5bf484](https://github.com/freeplane/freeplane/commit/3d5bf484ed3a3e643be8e83dc30e895cc11aa37d) |
| 2018-10-16 | `fix` | fix #2616 Reference from other maps v. 1.7.2_04 | `IMapLifeCycleListener.java`, `MapController.java` +2 | [27e3de61](https://github.com/freeplane/freeplane/commit/27e3de6156813702aa5bccc6e5b6835be86f0982) |
| 2018-10-15 | `api_change` | getPrecendents() and getDependents() API | `NodeAttributeTableModel.java`, `Dependencies.java` +18 | [f273ade7](https://github.com/freeplane/freeplane/commit/f273ade7ab2c3a26633cf90e04af3c28c7093379) |
| 2018-10-15 | `feature` | use default methods in listener interfaces and add onMapReloaded method | `AutomaticEdgeColorHook.java`, `AMapChangeListenerAdapter.java` +10 | [f02844c7](https://github.com/freeplane/freeplane/commit/f02844c71c49a6427e31d72c7053fed22a758afc) |
| 2018-10-06 | `fix` | bug fixes and improvements | `AttributeController.java`, `Connectors.java` +7 | [6afa6838](https://github.com/freeplane/freeplane/commit/6afa68387afa40da2e185e32d572a2e37225640e) |
| 2018-10-05 | `feature` | add accelerators to trace dependency actions | `mindmapmodemenu.xml` | [9e77184f](https://github.com/freeplane/freeplane/commit/9e77184f0ffbf3cfd7b299b8b9bf3172a2ae5dca) |
| 2018-09-29 | `feature` | Fix insertion of new nodes when children are infolded one by one | `MapController.java`, `MMapController.java` +4 | [cb033d49](https://github.com/freeplane/freeplane/commit/cb033d49721799f6bf696227ff72869a2f629c28) |
| 2018-09-22 | `feature` | add goto node action to node popup menu | `mindmapmodemenu.xml` | [7129604c](https://github.com/freeplane/freeplane/commit/7129604ced19b5ce9ed4aedbdeb6dd04f05fff83) |
| 2018-08-30 | `fix` | fix test threading | `SurveyStarter.java`, `SurveyStarterShould.java` | [897af9c3](https://github.com/freeplane/freeplane/commit/897af9c3d0d07601edf437fc84cae41139f37b69) |
| 2018-08-29 | `fix` | fix buffer clean | `BigBufferedImage.java` | [70b14e1c](https://github.com/freeplane/freeplane/commit/70b14e1c2e7a84affac0bf364878346e04c81689) |
| 2018-08-21 | `fix` | fix generics | `ExploringStep.java`, `NodeMatcher.java` +1 | [3cf29a2b](https://github.com/freeplane/freeplane/commit/3cf29a2b35fff022405f4d8d82f2ef920aed8f3f) |
| 2018-08-21 | `feature` | Add "deny" button to quick filter | `build.gradle`, `Resources_af.properties` +46 | [a8a1253f](https://github.com/freeplane/freeplane/commit/a8a1253f5b0fbab1a0ecac9f3456a508ca351f8c) |
| 2018-08-20 | `fix` | fix getNodeReferenceSuggestion | `MapExplorerController.java` | [49b6bea9](https://github.com/freeplane/freeplane/commit/49b6bea91aafd244ea0b15b25d88c5df6d64f90b) |
| 2018-08-19 | `fix` | fix attribute table constructor | `AttributeTableModel.java` | [9cca8d5d](https://github.com/freeplane/freeplane/commit/9cca8d5d611eba8c9bf9beed4e314c8ba40ed0cb) |
| 2018-08-15 | `feature` | add path syntax check | `ExploringStepBuilder.java`, `ExploringStepBuilderSpec.java` | [b2280a81](https://github.com/freeplane/freeplane/commit/b2280a81966f74ff74097e0246d8f6a99d82f587) |
| 2018-08-15 | `feature` | new syntax for map explorer | `Command.java`, `ExploringStep.java` +6 | [cfbf1914](https://github.com/freeplane/freeplane/commit/cfbf191415358b590fec8900f68b2f35d3042b65) |
| 2018-08-11 | `fix` | bug #2604 Right click on the 'fold minus' BOTH folds and shows the fold/unfold contextual  | `DefaultNodeMouseMotionListener.java` | [d05a8ea9](https://github.com/freeplane/freeplane/commit/d05a8ea9187930fa7241351c0ba543dddf69ef02) |
| 2018-08-11 | `fix` | bug #2604 Right click on the 'fold minus' BOTH folds and shows the fold/unfold contextual  | `DefaultNodeMouseMotionListener.java` | [aaae8ea9](https://github.com/freeplane/freeplane/commit/aaae8ea94baa5096e4589c42c5160758d448fc93) |
| 2018-08-09 | `fix` | bug #2602 Setting the reminder date using the calendar panel removes the reminder script. | `TimeManagement.java` | [f93443cf](https://github.com/freeplane/freeplane/commit/f93443cf1c2bdcd57cf9a6437633bde55d5eb8b4) |
| 2018-08-05 | `feature` | Add # in front of node alias when node reference is calculated | `MapExplorerController.java` | [c5cba755](https://github.com/freeplane/freeplane/commit/c5cba755d52ac4c699458089df4213fd9f435150) |
| 2018-08-05 | `feature` | add new actions to main menu | `mindmapmodemenu.xml`, `Resources_af.properties` +26 | [ed0de3ae](https://github.com/freeplane/freeplane/commit/ed0de3aea88b0126a2b0b9cfcbe54e970612017e) |
| 2018-08-05 | `fix` | fix test | `MapExplorerSpec.java` | [55db8661](https://github.com/freeplane/freeplane/commit/55db86616da8a73defa5e332a289cdc1cf0c739c) |
| 2018-07-31 | `feature` | Add actions to control new properties | `mindmapmodemenu.xml`, `AssignAliasAction.java` +5 | [93f6f4fa](https://github.com/freeplane/freeplane/commit/93f6f4fa075c481527940e30e724cf2b8a239ba8) |
| 2018-07-19 | `feature` | add new api to api mind map generation script | `EncryptedMap.java`, `MapController.java` +9 | [8a59e966](https://github.com/freeplane/freeplane/commit/8a59e96690a511eeeabc4a4ce6f52973c7eb73eb) |
| 2018-07-19 | `feature` | add new api to api mind map generation script | `EncryptedMap.java`, `MapController.java` +9 | [b5a9ac44](https://github.com/freeplane/freeplane/commit/b5a9ac442323435633992c52341446ecce2a3e0d) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [79de8564](https://github.com/freeplane/freeplane/commit/79de85641fe2c7d9cbb2ecc79238a18fa8b8ae18) |
| 2018-07-19 | `api_change` | loader api javadoc + selectNodeById creates view | `MapLoader.java`, `Controller.java` +3 | [bb1e7869](https://github.com/freeplane/freeplane/commit/bb1e78694778a47fff37f07484c283126847b8ed) |
| 2018-07-19 | `api_change` | MapLoader api and refactoring | `MapController.java`, `MapModel.java` +14 | [d2c45816](https://github.com/freeplane/freeplane/commit/d2c458160eb4a8a1bdb2004903315b5d7c20c444) |
| 2018-07-08 | `api_change` | rename API methods newMap -> openMap, newMapFromTemplate -> openUntitledMap, hiddenMap ->  | `EncryptedMap.java`, `XmlImporter.java` +24 | [a76dc05a](https://github.com/freeplane/freeplane/commit/a76dc05a3fe1d4bb41c642401861949053f14b9e) |
| 2018-07-08 | `fix` | Fix autosaveEnabled flag | `MMapModel.java` | [e959ba96](https://github.com/freeplane/freeplane/commit/e959ba96c2484c75addc5d656c02b2fc7504c7b0) |
| 2018-07-08 | `fix` | Fix memory leak | `LastOpenedList.java` | [4229e185](https://github.com/freeplane/freeplane/commit/4229e185609d29f7deec0cdf85f7d5dfe6872e94) |
| 2018-07-08 | `feature` | Add API method Controller.hiddenMap | `MMapController.java`, `MMapIO.java` +4 | [ba2c7706](https://github.com/freeplane/freeplane/commit/ba2c77064878fb9001a497a3467801cb7eb010f9) |
| 2018-06-24 | `feature` | ignore new tasks after shutdown | `HeadlessUIController.java` | [cea826ea](https://github.com/freeplane/freeplane/commit/cea826ea575c783f60c5f057ec5a0696f51c2d88) |
| 2018-06-19 | `api_change` | freeplane api package must not depend on any other freeplane packages | `build.gradle`, `Connector.java` +20 | [42e21482](https://github.com/freeplane/freeplane/commit/42e214828ff405b0a71adca6f169d13e290b58dd) |
| 2018-06-17 | `feature` | move api to core project and create api jar | `build.gradle`, `AttributeCondition.java` +33 | [4973e455](https://github.com/freeplane/freeplane/commit/4973e455f369a3f93bd3865c4bede8a274a28a71) |
| 2018-06-16 | `fix` | fix #2590 Nodes do not always expand and collapse when you click the area (circle (+) and  | `DefaultNodeMouseMotionListener.java` | [533bef7b](https://github.com/freeplane/freeplane/commit/533bef7b517e4015332e050479900c6692729c7a) |
| 2018-06-16 | `fix` | fix #2592 Freeplane does not keep the state for showAncestors and showDescendants between  | `FilterController.java` | [c11c58c6](https://github.com/freeplane/freeplane/commit/c11c58c6d7574ec239db88fb50bbd31567debbc9) |
| 2018-06-16 | `fix` | fix formatting | `MapViewController.java` | [e756211f](https://github.com/freeplane/freeplane/commit/e756211fe6d2bb24245fb67eb4b182f681a293bb) |
| 2018-06-16 | `fix` | Fix #2595 Exporting presentation clips images | `PresentationPngExporter.java`, `Slide.java` | [48b533f6](https://github.com/freeplane/freeplane/commit/48b533f63886ee3a820831ada7d1dcefb4f41ba6) |
| 2018-06-10 | `feature` | Still support java 7 on 1.6.x | `ActivatorImpl.java` | [239c3ed7](https://github.com/freeplane/freeplane/commit/239c3ed7360535cd19acd90940619eea1c9fff5c) |
| 2018-06-10 | `feature` | Still support java 7 on 1.6.x | `ActivatorImpl.java` | [128a50e9](https://github.com/freeplane/freeplane/commit/128a50e97fb6186f0d390884a30bebf43a1bdc7c) |
| 2018-05-30 | `feature` | add newHiddenMapFromTemplate method to controller scripting API | `MMapController.java`, `MMapIO.java` +2 | [257c29cc](https://github.com/freeplane/freeplane/commit/257c29cc40e4a33b4acf649af5b195c1bda0cd64) |
| 2018-05-02 | `fix` | fix division by zero | `MapScroller.java` | [2323f015](https://github.com/freeplane/freeplane/commit/2323f015aa1d782ba4103e18b49ac839a93b8972) |
| 2018-05-02 | `fix` | fix NPE | `NodeList.java` | [6cfbd182](https://github.com/freeplane/freeplane/commit/6cfbd182043a3478ac1a6a90abd09bd6f9059096) |
| 2018-05-02 | `fix` | fix NPE | `MapView.java` | [012fd84f](https://github.com/freeplane/freeplane/commit/012fd84f3cee215171f0534b7fa33b4e0b13487d) |
| 2018-05-02 | `fix` | Fix handling attribute table update | `AttributePanelManager.java` | [f896bed5](https://github.com/freeplane/freeplane/commit/f896bed51784d799059aa7b087c4302af339c28b) |
| 2018-05-02 | `fix` | fix NPE | `ApplicationViewController.java` | [924fe011](https://github.com/freeplane/freeplane/commit/924fe01117b4cd8440fe8895d099f15de2b5d753) |
| 2018-03-25 | `fix` | fix NPE | `BitmapViewerComponent.java` | [8d505498](https://github.com/freeplane/freeplane/commit/8d5054983c038def5ba087e389a5cc83bc291409) |
| 2018-03-25 | `fix` | fix NPE | `ViewerController.java` | [144e2229](https://github.com/freeplane/freeplane/commit/144e22295cc489208e8390293fa8f40691749209) |
| 2018-03-25 | `feature` | Java9 support | `BigBufferedImage.java` | [048d30aa](https://github.com/freeplane/freeplane/commit/048d30aa8d6cf4d30b551a2fbff39de57c2899cf) |
| 2018-03-25 | `feature` | Add support for Bulgatian, Hindi and Tamil languages | `Resources_bg.properties`, `Resources_hi.properties` +3 | [3348022e](https://github.com/freeplane/freeplane/commit/3348022eb5e3540cfe5d488f592b8c652a1497cd) |
| 2018-03-25 | `feature` | refactor: add flags about moditifation time update and map unsaved flag to NodeChangeEvent | `MapController.java`, `NodeChangeEvent.java` +1 | [000a38bf](https://github.com/freeplane/freeplane/commit/000a38bff1d45269090c1e973499ac67f67462ef) |
| 2018-02-20 | `fix` | fix NPE | `FreeplaneIconFactory.java` | [67305188](https://github.com/freeplane/freeplane/commit/67305188f2ba5b99e4d7426fe4d9fb65ceee920d) |
| 2018-02-08 | `fix` | Fix test: wait until event is processed in the event queue before verification | `JMenuItemBuilderTest.java` | [b14e1dfa](https://github.com/freeplane/freeplane/commit/b14e1dfa360453209807ebc6944fb6f3828fb4a3) |
| 2018-01-27 | `api_change` | Use Icon (interface) instead of SVGIcon or ImageIcon | `ResourceController.java`, `AFreeplaneAction.java` +16 | [9f50b315](https://github.com/freeplane/freeplane/commit/9f50b31569e5724e9929feab8eb2f66610ac7a5e) |
| 2018-01-27 | `fix` | fix test | `HeadlessUIController.java` | [87927d77](https://github.com/freeplane/freeplane/commit/87927d7798b096a4dde0856defa80b3e325b688f) |
| 2018-01-27 | `feature` | Add icon and attribute conditions to style editor | `ModelessAttributeController.java`, `IconController.java` +7 | [31d37ec2](https://github.com/freeplane/freeplane/commit/31d37ec29d1961a915bc3b14c3529c3bf80a7715) |
| 2018-01-25 | `fix` | Fix applet export | `freeplane_applet.jnlp` | [d589dbcf](https://github.com/freeplane/freeplane/commit/d589dbcf2352f250e83da3c3c681789d78624a74) |
| 2018-01-20 | `fix` | #2570 fix icon export to xhtml | `toxhtml.xsl`, `MindMapHTMLWriter.java` +3 | [0b5c0e12](https://github.com/freeplane/freeplane/commit/0b5c0e12a6c805ba053e93978335dc580ee09332) |
| 2018-01-20 | `fix` | #2570 fix icon export to html | `FileUtils.java`, `MindMapHTMLWriter.java` +3 | [f5b0f22d](https://github.com/freeplane/freeplane/commit/f5b0f22dfa0e55ef5f0e7098701cff8265f9168e) |
| 2018-01-07 | `fix` | fix spaces in xslt exports to plain text based formats | `mm2adoc.xsl`, `mm2opml.xsl` +2 | [12084cd6](https://github.com/freeplane/freeplane/commit/12084cd69afdbb18f674cb9c53862a42c2ada446) |

### Dettagli commit con note

**[5dc15caa](https://github.com/freeplane/freeplane/commit/5dc15caa27bbb489f3498c129934055157dab4d5)** (2018-12-31) — Fix #2386 Special characters in add-on translations wrongly displayed

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

**[27e3de61](https://github.com/freeplane/freeplane/commit/27e3de6156813702aa5bccc6e5b6835be86f0982)** (2018-10-16) — fix #2616 Reference from other maps v. 1.7.2_04

> chandle how accessed closed maps are handled

**[cb033d49](https://github.com/freeplane/freeplane/commit/cb033d49721799f6bf696227ff72869a2f629c28)** (2018-09-29) — Fix insertion of new nodes when children are infolded one by one

> Relates to https://sourceforge.net/p/freeplane/discussion/758437/thread/e12c37cc09/#9367

**[f896bed5](https://github.com/freeplane/freeplane/commit/f896bed51784d799059aa7b087c4302af339c28b)** (2018-05-02) — Fix handling attribute table update

> Exception in thread "AWT-EventQueue-0"
> java.lang.ArrayIndexOutOfBoundsException: Array index out of range: 0
> 	at java.util.Vector.get(Unknown Source)
> 	at org.freeplane.features.attribute.NodeAttributeTableModel.getValue(NodeAttributeTableModel.java:214)
> 	at org.freeplane.features.attribute.NodeAttributeTableModel.getValueAt(NodeAttributeTableModel.java:228)
> 	at org.freeplane.view.swing.map.attribute.ExtendedAttributeTableModelDecorator.getValueAt(ExtendedAttributeTableModelDecorator.java:74)
> 	at javax.swing.JTable.getValueAt(Unknown Source)
> 	at org.freeplane.view.swing.map.attribute.AttributePanelManager$TableCreator.setSelectedFormatItem(AttributePanelManager.java:203)
> 	at org.freeplane.view.swing.map.attribute.AttributePanelManager$TableCreator.nodeChanged(AttributePanelManager.java:242)
> 	at org.freeplane.features.map.NodeModel.fireSingleNodeChanged(NodeModel.java:597)
> 	at org.freeplane.features.map.NodeModel.fireNodeChanged(NodeModel.java:591)
> 	at org.freeplane.features.map.MapController.fireNodeChanged(MapController.java:592)
> 	at org.freeplane.features.map.MapController.nodeRefresh(MapController.java:855)
> 	at org.freeplane.features.map.MapController.nodeChanged(MapController.java:807)
> 	at org.freeplane.view.swing.map.attribute.AttributeTable.tableChanged(AttributeTable.java:786)
> 	at javax.swing.table.AbstractTableModel.fireTableChanged(Unknown
> Source)
> 	at org.freeplane.view.swing.map.attribute.ExtendedAttributeTableModelDecorator.tableChanged(ExtendedAttributeTableModelDecorator.java:140)
> 	at org.freeplane.features.attribute.NodeAttributeTableModel.fireTableChanged(NodeAttributeTableModel.java:99)
> 	at org.freeplane.features.attribute.NodeAttributeTableModel.fireTableRowsDeleted(NodeAttributeTableModel.java:107)
> 	at org.freeplane.features.attribute.mindmapmode.MAttributeController$InsertAttributeActor.undo(MAttributeController.java:179)
> 	at org.freeplane.features.attribute.mindmapmode.MAttributeController$RemoveAttributeActor.act(MAttributeController.java:290)
> 	at org.freeplane.features.mode.mindmapmode.MModeController.execute(MModeController.java:142)
> 	at org.freeplane.features.attribute.mindmapmode.MAttributeController.performRemoveRow(MAttributeController.java:685)
> 	at org.freeplane.view.swing.map.attribute.ExtendedAttributeTableModelDecorator.removeRow(ExtendedAttributeTableModelDecorator.java:112)
> 	at org.freeplane.view.swing.map.attribute.AttributeTable.removeRow(AttributeTable.java:708)
> 	at org.freeplane.view.swing.map.attribute.AttributePopupMenu$2.actionPerformed(AttributePopupMenu.java:116)

**[b14e1dfa](https://github.com/freeplane/freeplane/commit/b14e1dfa360453209807ebc6944fb6f3828fb4a3)** (2018-02-08) — Fix test: wait until event is processed in the event queue before verification

> https://github.com/freeplane/freeplane/issues/94


---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-10 | `feature` | add final modifiers | `ApplicationViewController.java` | [3f67c8db](https://github.com/freeplane/freeplane/commit/3f67c8db08afb228b6574f77433916ee8cede229) |
| 2017-12-08 | `fix` | fix regex | `IconStoreFactory.java` | [697e2478](https://github.com/freeplane/freeplane/commit/697e2478a53fbba63ceb160dad91b5c4084b7623) |
| 2017-12-08 | `fix` | fix NPE | `IconStoreFactory.java` | [55d7f467](https://github.com/freeplane/freeplane/commit/55d7f4676d1147e09f85886d39525dcebce79bb2) |
| 2017-12-08 | `fix` | fix user icon sort algorithm | `IconStoreFactory.java` | [344e492f](https://github.com/freeplane/freeplane/commit/344e492fb00fd058f300c90592e15d49eaf140b9) |
| 2017-12-01 | `fix` | Fix deletion of non string attributes from attribute manager | `AttributeController.java`, `AttributeRegistryElement.java` +1 | [55d8df5a](https://github.com/freeplane/freeplane/commit/55d8df5ac686b8909f983339467c367050f9cb34) |
| 2017-11-29 | `fix` | Fix broken undo for removing external image | `ExternalImagePopupMenu.java` | [27f3d12a](https://github.com/freeplane/freeplane/commit/27f3d12a4f4f132fe8699266b3771e72b9fae146) |
| 2017-11-27 | `fix` | bug fix: rename preferences action key as expected by freeplane_mac | `mindmapmodemenu.xml`, `Resources_ar.properties` +37 | [8c27dd01](https://github.com/freeplane/freeplane/commit/8c27dd012bb94fc8a1076eee0b2d933e093b431c) |
| 2017-11-25 | `fix` | fix modifiers | `BigBufferedImage.java` | [f4401b13](https://github.com/freeplane/freeplane/commit/f4401b13e111fe8665d4cdab3ddbbf7fa3fd68ee) |
| 2017-11-16 | `fix` | Fix deselect view of removed node | `MapView.java`, `NodeView.java` | [a9b87c3c](https://github.com/freeplane/freeplane/commit/a9b87c3c42563f88c81f616ec9e592834da665a8) |
| 2017-11-05 | `fix` | Fix failing test on CI | `CssRuleBuilderShould.java` | [6bcdc082](https://github.com/freeplane/freeplane/commit/6bcdc0820461b58bf6776c70e7acda7fbd21717d) |
| 2017-11-05 | `fix` | fix test name | `CssRuleBuilderShould.java` | [7beba426](https://github.com/freeplane/freeplane/commit/7beba426ae0305ab1390db035464e8a538796699) |
| 2017-11-05 | `fix` | fix compiler errors | `MNodeStyleController.java` | [ea0facd8](https://github.com/freeplane/freeplane/commit/ea0facd8271499f7cde89b015429478d31221179) |
| 2017-10-28 | `fix` | Fix class cast exception | `FileRevisionsDialog.java` | [c6dcba2a](https://github.com/freeplane/freeplane/commit/c6dcba2a943816c40565e14534492bb8ac4962fe) |
| 2017-10-28 | `fix` | Fix update check | `HttpVersionClient.java`, `UpdateCheckAction.java` | [91f076a9](https://github.com/freeplane/freeplane/commit/91f076a9f6ce90a09330cfee3ca9a5d4a5041480) |
| 2017-10-28 | `fix` | Fix NPE in Applet | `ConnectorArrows.java` | [6cc8f087](https://github.com/freeplane/freeplane/commit/6cc8f087293a9bccf35fc8523136718bd9691ca5) |
| 2017-10-22 | `fix` | fix mac default hot keys: remove alt+1 and alt+3 | `default_accelerators.properties`, `default_accelerators_mac.properties` | [6dafa8fb](https://github.com/freeplane/freeplane/commit/6dafa8fb4546f8da8746775d9d4574e6757104fc) |
| 2017-10-14 | `feature` | add translations | `Resources_de.properties`, `Resources_en.properties` | [cf0ba2ab](https://github.com/freeplane/freeplane/commit/cf0ba2abeb48fd87aa2cd936bef267b1132f0dba) |
| 2017-10-13 | `feature` | Add travis CI configuration (#63) | `.travis.yml`, `README.md` +1 | [34743e7c](https://github.com/freeplane/freeplane/commit/34743e7c86bd3fc6e43fec41f15e4cbed65d697b) |
| 2017-10-13 | `fix` | Fix java 7 compatibility | `NamedElementCollection.java`, `FrameController.java` | [8b2f3afb](https://github.com/freeplane/freeplane/commit/8b2f3afbbb2afd2558901cccbf45505f3658f89b) |
| 2017-10-13 | `fix` | fix huge fonts only once | `FrameController.java` | [0322eff9](https://github.com/freeplane/freeplane/commit/0322eff9e79fd7d0afc1ec95fc0dbe448e7a6cf5) |
| 2017-10-01 | `feature` | Support translations for Occitan and Kannada | `Resources_kn.properties`, `Resources_oc.properties` +2 | [57f5fd04](https://github.com/freeplane/freeplane/commit/57f5fd04b6b8cd3005773c9e7e4dd2a3556ebb72) |
| 2017-09-23 | `fix` | Fix NPE | `MapView.java` | [2862da13](https://github.com/freeplane/freeplane/commit/2862da1300d5ec4e0f37828bc3f1d0b137b3c714) |
| 2017-09-23 | `fix` | fix NPE | `ScaledStyleSheet.java` | [2d75130d](https://github.com/freeplane/freeplane/commit/2d75130dd704b0938e0798003c19cf32db6ae80d) |
| 2017-09-13 | `fix` | #2541 Huge toolbars after reboot : fix bad menuItemFontSize property value | `FrameController.java` | [898ae4e1](https://github.com/freeplane/freeplane/commit/898ae4e1484bd1059ea483c1bd3e43a64007d577) |
| 2017-09-02 | `fix` | Fix logging | `BitmapViewerComponent.java` | [515e8e6c](https://github.com/freeplane/freeplane/commit/515e8e6c61d2436936085dea9855156b0f4f53fa) |
| 2017-09-02 | `fix` | fix  ArrayIndexOutOfBoundsException: -1 | `TableSorter.java` | [6c3f9e77](https://github.com/freeplane/freeplane/commit/6c3f9e77c92ea0947d6c432174038e1507316ab2) |
| 2017-09-02 | `feature` | Add logging | `UrlManager.java` | [7a5b9ead](https://github.com/freeplane/freeplane/commit/7a5b9ead116dd7d2bee4d4343ccd91f032450f28) |
| 2017-09-02 | `fix` | fix NPE | `MakeLinkFromAnchorAction.java` | [6f49703c](https://github.com/freeplane/freeplane/commit/6f49703ca8ecbfe67ecaee79de315e73f3ceee05) |
| 2017-09-02 | `fix` | Try to fix negativ level number | `AutomaticEdgeStyle.java` | [4e7a0d28](https://github.com/freeplane/freeplane/commit/4e7a0d283d7fcb20aff97a7cd62e2b3d70bf8c1b) |
| 2017-09-02 | `fix` | Fix undo for exporting branch to map | `NodeModel.java`, `ExportBranchAction.java` | [92378f28](https://github.com/freeplane/freeplane/commit/92378f28f0c7a8e39c44f85b874d912dd552a5c6) |
| 2017-09-02 | `feature` | Add logging if node has lost parent | `MainView.java` | [9f2d266c](https://github.com/freeplane/freeplane/commit/9f2d266cbe4eb199ad0694558fc299dda47027b7) |
| 2017-09-02 | `fix` | fix NPE | `MClipboardController.java` | [68a3d3a0](https://github.com/freeplane/freeplane/commit/68a3d3a027de942083cca1151c4fcc7cd20b5c95) |
| 2017-09-02 | `fix` | fix NPE | `MMapMouseListener.java` | [71b6ccb8](https://github.com/freeplane/freeplane/commit/71b6ccb894f0c048e89c1449604ed4d1a8787761) |
| 2017-08-22 | `feature` | add link to bug | `BitmapViewerComponent.java` | [f0f93577](https://github.com/freeplane/freeplane/commit/f0f9357726bc17346f82f93fe85a5bb82701bec3) |
| 2017-08-19 | `fix` | fix edge color configuration related bugs | `EdgeColorConfiguration.java`, `ColorListEditorPanelBuilder.java` | [7c51a227](https://github.com/freeplane/freeplane/commit/7c51a227898a9b9b5b8b1f3afb71289ea3ee81e3) |
| 2017-08-13 | `fix` | Fix NPE | `Handler.java` | [5a993c48](https://github.com/freeplane/freeplane/commit/5a993c48177bf9c7adbff09b640674fea0431ecd) |
| 2017-08-13 | `fix` | fix NPE | `CloudColorShapeControlGroup.java` | [d9c4fe46](https://github.com/freeplane/freeplane/commit/d9c4fe46212f966e42edb8444e711478707e5c00) |
| 2017-08-13 | `feature` | Fix new map from templates with hierarchical icons and without map style | `HierarchicalIcons.java` | [bb9f436d](https://github.com/freeplane/freeplane/commit/bb9f436d6e6563d48edbf74cb4d67d61d8ef7997) |
| 2017-07-29 | `fix` | Fix NPE (missing image)  in SHtml about dialog | `MTextController.java` | [665434f6](https://github.com/freeplane/freeplane/commit/665434f6c121f7dfdea8fcc10efd317836bf7898) |
| 2017-07-23 | `fix` | fix NPE | `LinkController.java` | [0416554e](https://github.com/freeplane/freeplane/commit/0416554eec648249c0acff083c632dd7b1dd0d09) |
| 2017-07-23 | `feature` | Add logging to hunt a bug | `JMenuItemBuilder.java` | [45533a47](https://github.com/freeplane/freeplane/commit/45533a47b8e5f819e6073b2fbd1fc2088b5806a3) |
| 2017-07-15 | `feature` | Add names to map and mode action entries to improve logging | `UserInputListenerFactory.java` | [981990da](https://github.com/freeplane/freeplane/commit/981990da27a0728dde17ae4e9645bf48467eed93) |
| 2017-07-08 | `feature` | Allow access to templates when new maps are created from scripts | `MFileManager.java` | [37e3bfcb](https://github.com/freeplane/freeplane/commit/37e3bfcb79e35ddd9801f4cf1a0bbdc379562baa) |
| 2017-07-08 | `fix` | Fix exception handling | `BitmapViewerComponent.java` | [df9003e9](https://github.com/freeplane/freeplane/commit/df9003e9d9700358df92dabc10e482956372ae94) |
| 2017-06-28 | `fix` | Revert "Fix UI font scaling for java 9" | `FrameController.java` | [36f54a09](https://github.com/freeplane/freeplane/commit/36f54a09db1825482e3aa856a8bf8bb89716fb60) |
| 2017-06-28 | `feature` | Add zooming to Quantity | `Quantity.java`, `QuantityShould.java` | [811c538f](https://github.com/freeplane/freeplane/commit/811c538f64259bf6e077f8510d02e41775e93824) |
| 2017-06-03 | `fix` | #2513 Summary Node Numbering Bug | `NodeStyleBuilder.java`, `NodeStyleController.java` +2 | [40fcaf8d](https://github.com/freeplane/freeplane/commit/40fcaf8d65032b03c54e4a83d074cb49a3ba7991) |
| 2017-05-13 | `fix` | fix btnCopy.setEnabled condition | `CollectionBoxController.java` | [0376abbe](https://github.com/freeplane/freeplane/commit/0376abbeffa0bc80bd911254f4f4065963e85d21) |
| 2017-05-08 | `fix` | Fix UI font scaling for java 9 | `FrameController.java` | [70bf4993](https://github.com/freeplane/freeplane/commit/70bf49939cb8d482d2c8753257d19ec403e2c180) |
| 2017-05-08 | `feature` | #2507 image pasting no longer works : create file directory when  needed | `TargetFileCreator.java` | [c6e9c358](https://github.com/freeplane/freeplane/commit/c6e9c3581a66267dd609627c5cf52ff8c7925ca9) |
| 2017-05-08 | `fix` | Fix dialog title | `SelectedPasteAction.java` | [b20008c2](https://github.com/freeplane/freeplane/commit/b20008c227964ca09a0735d93d67a023af069657) |
| 2017-05-03 | `fix` | #2504 Fix attribute font used in attribute panel | `AttributeTable.java` | [46ce8c1c](https://github.com/freeplane/freeplane/commit/46ce8c1c73c2eca3934b1221b051fe283ab67c6b) |
| 2017-05-02 | `fix` | Fix NPE | `Slide.java`, `MapView.java` | [d3f905f9](https://github.com/freeplane/freeplane/commit/d3f905f9223a278e6eb3b026fb0b41b75181f644) |
| 2017-04-30 | `fix` | #2501 fix SummaryLevels if map has clones or multiple views | `SummaryLevels.java`, `VerticalNodeViewLayoutStrategy.java` | [49a1ce34](https://github.com/freeplane/freeplane/commit/49a1ce34b76cd21d1e30386f0a32778a96b09f9d) |
| 2017-04-30 | `feature` | make const public for add-on compatibility | `FilterController.java` | [74b692d4](https://github.com/freeplane/freeplane/commit/74b692d40c5578ddffebedc1e40b24acc346d82f) |
| 2017-04-29 | `feature` | #2368 Support multi-columns icons toolbar | `FreeplaneToolBar.java`, `OneTouchCollapseResizer.java` +3 | [aaffd3c8](https://github.com/freeplane/freeplane/commit/aaffd3c8b7633b0d147e2eaf14c56e16168f0d1b) |
| 2017-04-29 | `fix` | Fix tooltip scaling with zoom # Conflicts: #	freeplane/src/main/java/org/freeplane/feature | `CssRuleBuilder.java`, `NoteController.java` +3 | [3daeb79d](https://github.com/freeplane/freeplane/commit/3daeb79dc9bd6d512ee744564190b2b5676655ea) |
| 2017-04-29 | `fix` | Fix tooltip scaling with zoom | `CssRuleBuilder.java`, `NoteController.java` +3 | [a8cf66b3](https://github.com/freeplane/freeplane/commit/a8cf66b398eb11069836b1a5c2b44c70b5814e0a) |
| 2017-04-23 | `fix` | fix NPE | `MTextController.java` | [3ba58d9e](https://github.com/freeplane/freeplane/commit/3ba58d9e2108617bcb84dee975cccd7e99997036) |
| 2017-04-23 | `fix` | fix NPE | `MTextController.java` | [b95e7019](https://github.com/freeplane/freeplane/commit/b95e7019d5153f2751d6f6a2b3412c1bcfdc450f) |
| 2017-04-23 | `fix` | Fix NPE | `ImportExplorerFavoritesAction.java` | [5b7d88f3](https://github.com/freeplane/freeplane/commit/5b7d88f322db2fb77d709376064233dde7e3f0d8) |
| 2017-04-20 | `feature` | Add filter composer icons | `AFilterComposerDialog.java`, `freeplane.properties` +9 | [75e65bbe](https://github.com/freeplane/freeplane/commit/75e65bbe5e21aac399e53f165396a3072aa73985) |
| 2017-04-18 | `fix` | Fix spotlight setting for single presentation export | `PresentationPngExporter.java` | [6f0521c4](https://github.com/freeplane/freeplane/commit/6f0521c489d035836199fa949852613f536ae70b) |
| 2017-04-17 | `fix` | Fix slide export | `PresentationPngExporter.java`, `Slide.java` +1 | [2d7584f6](https://github.com/freeplane/freeplane/commit/2d7584f6775b981944163323665017731378c2f3) |
| 2017-04-17 | `fix` | Fix calendar font size | `JDayChooser.java` | [c21b7853](https://github.com/freeplane/freeplane/commit/c21b7853f96870812fabb9a27ec2ad3ea1c9cf82) |
| 2017-04-17 | `feature` | Revert "add logging for screenBounds calculations (FONT_SCALE_FACTOR)" | `UITools.java` | [c96db2c9](https://github.com/freeplane/freeplane/commit/c96db2c961bd263e17c0ffd613869fdd5befeaf5) |
| 2017-04-17 | `fix` | fix html source editor font size | `MTextController.java` | [b52fddc9](https://github.com/freeplane/freeplane/commit/b52fddc9b6e8120d0aae43761787b50b6e3f3021) |
| 2017-04-17 | `fix` | Fix OOM errors for large image exports | `BigBufferedImage.java`, `ExportToImage.java` +1 | [e92c84df](https://github.com/freeplane/freeplane/commit/e92c84dfcf26fd542136a2bc2d2c8c0cabd8f919) |
| 2017-04-16 | `feature` | add logging for screenBounds calculations (FONT_SCALE_FACTOR) | `UITools.java` | [597e496a](https://github.com/freeplane/freeplane/commit/597e496ac3cea1c6067684116a0fc144a6619fa0) |
| 2017-04-16 | `fix` | Fix handling of svg isons containg  xlink:href elements | `FreeplaneIconUtils.java` | [8ad5f7e9](https://github.com/freeplane/freeplane/commit/8ad5f7e9f9e9683c8773864fe7448b2192b70a92) |
| 2017-04-15 | `feature` | add new icon for menu item link action, rename icon for presentation editor | `AddMenuItemLinkAction.png`, `AddMenuItemLinkAction.svg` +2 | [391eeade](https://github.com/freeplane/freeplane/commit/391eeade5599b03b038aa430ef6cbc0813b1633d) |
| 2017-04-13 | `feature` | Add margins to icon toolbar submenu buttons | `MIconController.java` | [d0701078](https://github.com/freeplane/freeplane/commit/d0701078e094e6dbb3e771d6c25c6d72eb748fd5) |
| 2017-04-12 | `fix` | Fix menu item icons | `LinkController.java` | [3ae1df9a](https://github.com/freeplane/freeplane/commit/3ae1df9a2847f04e4abffd43ae04164ac227f08e) |
| 2017-04-11 | `fix` | Fix SetSlideContent.icon | `SlideEditorController.java` | [0b10115f](https://github.com/freeplane/freeplane/commit/0b10115f2267ea2816e31be0e8f78e5ad095bef2) |
| 2017-04-10 | `feature` | New icons | `AddSlideContent.svg`, `CenterSelectedNodeSlideContent.svg` +11 | [b15268f2](https://github.com/freeplane/freeplane/commit/b15268f29b1a907e9cfc6aeea18332a9b61160a2) |
| 2017-04-09 | `feature` | new icons | `AddAttributeAction.png`, `AddAttributeAction.svg` +33 | [0b7cfed4](https://github.com/freeplane/freeplane/commit/0b7cfed4014a391a579f37f08afdfbc1763ad88c) |
| 2017-04-09 | `feature` | inline IconStoreFactory.create() | `FButtonBar.java`, `AttributeController.java` +14 | [16fcbdd5](https://github.com/freeplane/freeplane/commit/16fcbdd5b46e791b3a455ee577c2b05f0bd756f7) |
| 2017-04-09 | `feature` | Add slide editor icons | `AddSlideContent.svg`, `CenterSelectedNodeSlideContent.svg` +13 | [8c1679b3](https://github.com/freeplane/freeplane/commit/8c1679b3df17c07676f0c5e276d08419f80f84d7) |
| 2017-04-09 | `fix` | Allow creation of all internal icons from svg and fix use_svg_icons check | `ResourceController.java`, `FreeplaneIconUtils.java` +7 | [a5f1bca3](https://github.com/freeplane/freeplane/commit/a5f1bca39f16c8a45a660082f5ef0a4bbe6902d3) |
| 2017-04-08 | `fix` | Fix icon resource loading priority | `ResourceController.java`, `ApplicationResourceController.java` | [95fcd2ca](https://github.com/freeplane/freeplane/commit/95fcd2caad1c77b14fcb5657fa455a84d252664c) |
| 2017-04-04 | `feature` | Support icons on view boolean property actions | `SetBooleanMapViewPropertyAction.java` | [b1d53cab](https://github.com/freeplane/freeplane/commit/b1d53cab5d8ad4d9fcc496ab9c4e3c2b2996cf0a) |
| 2017-04-04 | `feature` | Add presentation mode action icon | `presentation_mode.png`, `presentation_mode.svg` +1 | [915cd383](https://github.com/freeplane/freeplane/commit/915cd3830bf93ffe55b9915474fa9fe135a0b628) |
| 2017-03-26 | `feature` | New progress quarter icons | `Progress_quarter_00.svg`, `Progress_quarter_01.svg` +3 | [df5c00d6](https://github.com/freeplane/freeplane/commit/df5c00d6bc65b9561d1777abe1d47da949f8e976) |
| 2017-03-26 | `feature` | Add new progress icons | `Progress_tenth_00.svg`, `Progress_tenth_01.svg` +9 | [28907027](https://github.com/freeplane/freeplane/commit/289070271b19cd404f2f676a487be984211d3c97) |
| 2017-03-19 | `fix` | fix jnlp file generation | `freeplane2ws.xsl`, `ExportWithXSLT.java` | [4cd9bffb](https://github.com/freeplane/freeplane/commit/4cd9bffb3901fd693de581b38f23a28850a97ee2) |
| 2017-03-19 | `fix` | fix jnlp file generation | `freeplane2ws.xsl`, `ExportWithXSLT.java` | [3f27d527](https://github.com/freeplane/freeplane/commit/3f27d5274b88b875b24725b4972f04ce6181f9b9) |
| 2017-03-11 | `fix` | Fix map scrolling | `MapViewScrollPane.java` | [04d31b3b](https://github.com/freeplane/freeplane/commit/04d31b3bff228588acb46e9a87708d7990b14800) |
| 2017-03-07 | `feature` | Fix long node editing for new nodes | `MTextController.java` | [efe5be9d](https://github.com/freeplane/freeplane/commit/efe5be9d88ecb34603e95520e2e23a9b40040b78) |
| 2017-02-26 | `fix` | Fix script security issue | `AFreeplaneAction.java`, `InternationalizedSecurityManager.java` +2 | [f74f473e](https://github.com/freeplane/freeplane/commit/f74f473e7300598a3338b78355e3468ccae5a024) |
| 2017-02-25 | `feature` | Keep centered node id enabled when new slide is created | `Slide.java` | [8ce59eb0](https://github.com/freeplane/freeplane/commit/8ce59eb02d5cb2af9d621537550e69e455fd2d13) |
| 2017-02-25 | `fix` | Fix moving of presentation elements up and down | `UndoableNamedElementCollection.java` | [968b2b43](https://github.com/freeplane/freeplane/commit/968b2b4365e6822e70f89db37f486250bb53c0ae) |
| 2017-02-19 | `fix` | fix conditional style update for scripting conditions | `ASelectableCondition.java`, `ConditionalStyleModel.java` +1 | [634ca837](https://github.com/freeplane/freeplane/commit/634ca83721e890be6d5a8dfcca807a87e9ae3a48) |
| 2017-02-19 | `fix` | fix parent depending node conditional style update | `MapController.java`, `MTextController.java` | [83c6d0ed](https://github.com/freeplane/freeplane/commit/83c6d0ed15b64bbfb92d7b52f41bb5e021b623f5) |
| 2017-02-18 | `feature` | Use new icons for presentation editor buttons | `DeletePresentation.svg`, `DeleteSlide.svg` +14 | [3f90d2cc](https://github.com/freeplane/freeplane/commit/3f90d2cc6ca20acfd027871d05d4173ac5635d00) |
| 2017-02-17 | `feature` | Support non default http port "Open map from URL" | `FreeplaneUriConverter.java` | [b1703fd9](https://github.com/freeplane/freeplane/commit/b1703fd9fe7ecec887db5274fc1db763b8cd1cb4) |
| 2017-02-17 | `feature` | add plausibility size check | `UITools.java` | [9f0f38e1](https://github.com/freeplane/freeplane/commit/9f0f38e1fa1a6da31d39f7f222a45314cbc68f4c) |
| 2017-02-17 | `fix` | Fix show preferences on mac | `ShowPreferencesAction.java` | [3890922e](https://github.com/freeplane/freeplane/commit/3890922ee6a98ec594812472d7fcac36aa725b5f) |
| 2017-02-15 | `fix` | bug fix: unfoldAndScroll should call unfold | `MapController.java` | [13d89d62](https://github.com/freeplane/freeplane/commit/13d89d620bbf53a57b6ba271ec2fae79cfcdbd26) |
| 2017-02-14 | `fix` | Fix unfolding of hidden nodes | `MapController.java` | [f1b9d03a](https://github.com/freeplane/freeplane/commit/f1b9d03a2fc4169adf3a599c5cd2885eb4e98885) |
| 2017-02-05 | `fix` | Fix bug related to clone marks | `MainView.java` | [4441161a](https://github.com/freeplane/freeplane/commit/4441161a380804d2e28bb1cc1ed6360d27615963) |
| 2017-02-05 | `fix` | bug fix + escape key ends presentation | `preferences.xml`, `EscapeKeyEventDispatcher.java` +6 | [b8db947f](https://github.com/freeplane/freeplane/commit/b8db947f8623a898ad453219927746f14dfbffc2) |
| 2017-02-05 | `feature` | #2340 presentation tab . press new presentation , new slide - focus go to edit box | `CollectionBoxController.java` | [74e14aca](https://github.com/freeplane/freeplane/commit/74e14acae649ca73af56c5693ed6250886d563d5) |
| 2017-02-05 | `fix` | Fix img handling in structured html handler | `preferences.xml`, `MClipboardController.java` +2 | [c2560dad](https://github.com/freeplane/freeplane/commit/c2560dad40e4b37465f032839d5c6aa455595664) |
| 2017-02-05 | `feature` | Add standard cloud shape to preferences | `preferences.xml`, `ResourceController.java` +9 | [5110322a](https://github.com/freeplane/freeplane/commit/5110322a4d9a1ddaf170c2130a655e9f5f45c28e) |
| 2017-02-04 | `feature` | Revert "Create Resources_oc.properties" | `Resources_oc.properties` | [6d63afed](https://github.com/freeplane/freeplane/commit/6d63afedcdd54257ec2bef1a3eebd43542eefc2b) |
| 2017-02-03 | `feature` | Create Resources_oc.properties | `Resources_oc.properties` | [56aedfe3](https://github.com/freeplane/freeplane/commit/56aedfe30938f6dca717f44d428f25f07fb80c5e) |
| 2017-01-24 | `feature` | Add translation for afrikaans | `Resources_af.properties`, `freeplane.properties` +1 | [cf48fb68](https://github.com/freeplane/freeplane/commit/cf48fb68de9ca659ec34ea72a5e48ee39d575d38) |
| 2017-01-24 | `feature` | Add translation for afrikaans | `Resources_af.properties`, `freeplane.properties` +1 | [52e23380](https://github.com/freeplane/freeplane/commit/52e2338043c129a953897f2eb8b51a718b1b99ec) |
| 2017-01-22 | `fix` | Fix table column width calculation | `AttributeTable.java` | [2c810412](https://github.com/freeplane/freeplane/commit/2c810412414b186a6f106e53451ba61b4cd3a265) |
| 2017-01-22 | `fix` | Fix table border colors | `AttributeTable.java` | [1c3d6df0](https://github.com/freeplane/freeplane/commit/1c3d6df0339eff511c5a69381e607a928731ab21) |
| 2017-01-21 | `fix` | Fix set filter toggle state | `SlideEditorController.java` | [176ba521](https://github.com/freeplane/freeplane/commit/176ba5216865d0b7b8aea61dbffe02063bdacaa0) |
| 2017-01-21 | `feature` | Allow to add tool tips to presentation panel elements | `TranslatedElementFactory.java`, `SlideEditorController.java` | [ec2f2c06](https://github.com/freeplane/freeplane/commit/ec2f2c06aa8727f306ec137fd7cd10318cd82a52) |
| 2017-01-21 | `feature` | New presentation / new slide buttons | `Resources_eu.properties`, `Resources_fr.properties` +9 | [91ac0f31](https://github.com/freeplane/freeplane/commit/91ac0f310f37be1e6a16e2cb936be8495078982c) |
| 2017-01-21 | `fix` | fix #2442 zoom . underline gets too thick | `ShapedMainView.java` | [e17e0a41](https://github.com/freeplane/freeplane/commit/e17e0a4171c41c2123675c43a7258c8bc7f6349b) |
| 2017-01-20 | `fix` | Fix "Scrollbar thumb disappears with Nimbus L&F" | `FrameController.java` | [a83bd2af](https://github.com/freeplane/freeplane/commit/a83bd2af07bd1c1c48dd6b5a6c5df2a45691d2f1) |
| 2017-01-20 | `fix` | Fix "Scrollbar thumb disappears with Nimbus L&F" | `FrameController.java` | [df900729](https://github.com/freeplane/freeplane/commit/df90072954521a841798d4f4296f46540c2d5d41) |
| 2017-01-20 | `fix` | Fix #2441 increase font size box width | `MUIFactory.java` | [b88d580b](https://github.com/freeplane/freeplane/commit/b88d580bd1cbcbcb3421f77d6d7f4a2df55aca4e) |
| 2017-01-19 | `fix` | Fix table grid painting for Nimbus | `AttributeTable.java`, `AttributeTableCellRenderer.java` | [3ff8ad04](https://github.com/freeplane/freeplane/commit/3ff8ad04362f73bf96ce096842d7d8f0bd28a3c9) |
| 2017-01-19 | `fix` | Fix table grid painting for Nimbus | `AttributeTable.java`, `AttributeTableCellRenderer.java` | [c39b30c6](https://github.com/freeplane/freeplane/commit/c39b30c62dcc423866706ade9e7c5a5a379cb2fb) |
| 2017-01-19 | `fix` | Fix stop after launch | `CommandLineParser.java`, `FreeplaneGUIStarter.java` | [0860ecce](https://github.com/freeplane/freeplane/commit/0860eccedb21688d3e2ba9f17f3c0bc37514dc26) |
| 2017-01-19 | `fix` | Fix stop after launch | `CommandLineParser.java`, `FreeplaneGUIStarter.java` | [8611696e](https://github.com/freeplane/freeplane/commit/8611696e8bc7ffad16da3ebb9b6299780df4fbf1) |
| 2017-01-19 | `fix` | Bug fix: execute initialization scripts after the node has got focus. | `FreeplaneGUIStarter.java` | [2e68075e](https://github.com/freeplane/freeplane/commit/2e68075ef91cfb84958e7a37da465956398c9b84) |
| 2017-01-19 | `fix` | Bug fix: execute initialization scripts after the node has got focus. | `FreeplaneGUIStarter.java` | [e1374a66](https://github.com/freeplane/freeplane/commit/e1374a66ac22c0611479692de95aabe97de1b586) |
| 2017-01-17 | `fix` | Fix #2440 FP 1 6 1 01: cloud shape unstable | `CloudColorShapeControlGroup.java` | [22656296](https://github.com/freeplane/freeplane/commit/226562966d8ae979aec0e12640f6510f2228021c) |
| 2017-01-14 | `feature` | SVG support for applets | `kitfox-svg-salamander-1.1.1-p1.jar`, `ExportWithXSLT.xml` +3 | [67a4b710](https://github.com/freeplane/freeplane/commit/67a4b7100449952da8f024279721df53497ee691) |
| 2017-01-03 | `fix` | Fix class after merge | `IconSizeControlGroup.java` | [712a4f6a](https://github.com/freeplane/freeplane/commit/712a4f6a6a06c973b3d1829f39353b760aab5be4) |
| 2017-01-03 | `fix` | Fix ScrollbarIncrement | `MEdgeController.java` | [e83ba3d1](https://github.com/freeplane/freeplane/commit/e83ba3d1f10d958b47a02fb276359bd6a76302e8) |
| 2017-01-02 | `fix` | Fix wording | `MEdgeController.java`, `StyleControlGroup.java` +1 | [9e53bb90](https://github.com/freeplane/freeplane/commit/9e53bb90211c03fa14af832abdf6c1c4eebc7a50) |
| 2017-01-02 | `fix` | Fix boolean property value | `xml2mm.xsl`, `freeplane.properties` | [8be96783](https://github.com/freeplane/freeplane/commit/8be96783ddd792638a6a4bcbb83628422e5e300e) |

### Dettagli commit con note

**[a9b87c3c](https://github.com/freeplane/freeplane/commit/a9b87c3c42563f88c81f616ec9e592834da665a8)** (2017-11-16) — Fix deselect view of removed node

> (it caused LogUtils.severe("Node" + node + " has lost parent") message)

**[34743e7c](https://github.com/freeplane/freeplane/commit/34743e7c86bd3fc6e43fec41f15e4cbed65d697b)** (2017-10-13) — Add travis CI configuration (#63)

> * Add travis CI configuration
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>
> 
> * Add build status on README.md
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>
> 
> * Build against multiple JDKs.
> 
> Building against:
> - OpenJDK 7
> - OpenJDK 8
> - Oracle JDK 8
> - Oracle JDK 9
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>
> 
> * Fix for InvalidKeyException.
> 
> Fetch dependencies with JDK8 which includes the certificates
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>

**[4e7a0d28](https://github.com/freeplane/freeplane/commit/4e7a0d283d7fcb20aff97a7cd62e2b3d70bf8c1b)** (2017-09-02) — Try to fix negativ level number

> java.lang.ArrayIndexOutOfBoundsException: -3
> 	at java.util.ArrayList.elementData(Unknown Source)
> 	at java.util.ArrayList.get(Unknown Source)
> 	at
> org.freeplane.features.edge.EdgeColorConfiguration.getEdgeColor(EdgeColorConfiguration.java:22)
> 	at
> org.freeplane.features.edge.EdgeController.getEdgeColor(EdgeController.java:345)
> 	at
> org.freeplane.view.swing.map.edge.AutomaticEdgeStyle.<init>(AutomaticEdgeStyle.java:62)
> 	at
> org.freeplane.view.swing.map.NodeView.getEdgeColor(NodeView.java:1480)
> 	at
> org.freeplane.view.swing.map.edge.EdgeView.getColor(EdgeView.java:138)
> 	at
> org.freeplane.view.swing.map.edge.OutlineEdgeView.draw(OutlineEdgeView.java:54)
> 	at org.freeplane.view.swing.map.edge.EdgeView.paint(EdgeView.java:212)
> 	at org.freeplane.view.swing.map.NodeView.paintEdges(NodeView.java:1136)
> 	at
> org.freeplane.view.swing.map.NodeView.paintComponent(NodeView.java:1040)
> 	at javax.swing.JComponent.paint(Unknown Source)
> 	at org.freeplane.view.swing.map.NodeView.paint(NodeView.java:1057)
> 	at javax.swing.JComponent.paintChildren(Unknown Source)
> 	at
> org.freeplane.view.swing.map.MapView.paintChildren(MapView.java:1528)

**[36f54a09](https://github.com/freeplane/freeplane/commit/36f54a09db1825482e3aa856a8bf8bb89716fb60)** (2017-06-28) — Revert "Fix UI font scaling for java 9"

> This reverts commit 70bf49939cb8d482d2c8753257d19ec403e2c180.

**[c96db2c9](https://github.com/freeplane/freeplane/commit/c96db2c961bd263e17c0ffd613869fdd5befeaf5)** (2017-04-17) — Revert "add logging for screenBounds calculations (FONT_SCALE_FACTOR)"

> This reverts commit 597e496ac3cea1c6067684116a0fc144a6619fa0.

**[b1703fd9](https://github.com/freeplane/freeplane/commit/b1703fd9fe7ecec887db5274fc1db763b8cd1cb4)** (2017-02-17) — Support non default http port "Open map from URL"

> Freeplane cannot load URL with non default http port because the FreeplaneUriConverter removes the port part of the URL.

**[6d63afed](https://github.com/freeplane/freeplane/commit/6d63afedcdd54257ec2bef1a3eebd43542eefc2b)** (2017-02-04) — Revert "Create Resources_oc.properties"

> This reverts commit 56aedfe30938f6dca717f44d428f25f07fb80c5e.


---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-12-31 | `fix` | fix test | `UITools.java` | [e7baab4d](https://github.com/freeplane/freeplane/commit/e7baab4d8a20a2a67ede22751de34a198b5230ca) |
| 2016-12-29 | `fix` | Fix endless loop | `ImageIconFactory.java` | [648e5219](https://github.com/freeplane/freeplane/commit/648e52199d29b2380aa5826a59bc7c34053154d0) |
| 2016-12-29 | `feature` | Add more view svgs | `FitToPage.svg`, `kword.svg` +6 | [6ec6d6e5](https://github.com/freeplane/freeplane/commit/6ec6d6e5823960875c790dd46812ed2057aa575d) |
| 2016-12-29 | `feature` | add tools svgs | `ExecuteScriptForAllNodes.svg`, `ExecuteScriptForSelectionAction.svg` +15 | [0a27a7fd](https://github.com/freeplane/freeplane/commit/0a27a7fd6ae92ebef92adae77b0e37a508f33949) |
| 2016-12-29 | `feature` | add navigate svgs | `MoveTo_NextMM.svg`, `MoveTo_NextNode.svg` +4 | [394a8ff0](https://github.com/freeplane/freeplane/commit/394a8ff007c22b3840b4ff16127206c94556b747) |
| 2016-12-29 | `feature` | add f-bar svgs | `f1.svg`, `f10.svg` +10 | [3be8673f](https://github.com/freeplane/freeplane/commit/3be8673f74946797d81c2180fbfd4acd76354a46) |
| 2016-12-29 | `feature` | add connector svgs | `arrow-mode-backward.svg`, `arrow-mode-both.svg` +4 | [e4246a73](https://github.com/freeplane/freeplane/commit/e4246a73c02914118f4e861c5fc786f35b7216d3) |
| 2016-12-23 | `fix` | Fix date formats in generated scanner.xml | `ScannerController.java` | [1ce0dec8](https://github.com/freeplane/freeplane/commit/1ce0dec8ef80d6ef14575015ec4f98e259f340f0) |
| 2016-12-04 | `fix` | fix small issue that results in a runtime error in debian package | `StyleEditorPanel.java` | [1201d689](https://github.com/freeplane/freeplane/commit/1201d6890c5e07ebd64885b5fc3182933fcb64fb) |
| 2016-12-03 | `feature` | add most Format menu SVGs | `AutomaticEdgeColorHookAction.svg`, `Bold16.svg` +8 | [278c1fbf](https://github.com/freeplane/freeplane/commit/278c1fbf0ef026e308c960a451a37dac3812010f) |
| 2016-12-03 | `feature` | add most Edit menu SVGs | `Cloud24.svg`, `DeleteDetailsAction.svg` +37 | [aaecad45](https://github.com/freeplane/freeplane/commit/aaecad45ac9ae1bbcc73e62306cce463176a9551) |
| 2016-12-03 | `feature` | add most File menu SVGs | `export.svg`, `fileopen.svg` +10 | [2bdde79e](https://github.com/freeplane/freeplane/commit/2bdde79ee236fd089abb421981941b44678c7841) |
| 2016-12-01 | `feature` | Implemented four new control group classes & minor code style cleanup. | `EdgeColorControlGroup.java`, `EdgeDashControlGroup.java` +5 | [134e2d8f](https://github.com/freeplane/freeplane/commit/134e2d8fbd6ceffbb274dc35a7025183031cc413) |
| 2016-11-30 | `fix` | fix NPE | `NodeList.java` | [b3612248](https://github.com/freeplane/freeplane/commit/b36122484fbb352f3ccc8ddbb5f28283c868e6e9) |
| 2016-11-28 | `fix` | Fix font family formatting in html fragments: use &quot; instead of " | `CssRuleBuilder.java`, `ScaledEditorKit.java` +6 | [1a400af5](https://github.com/freeplane/freeplane/commit/1a400af554823a1640a950749314964134ab68f1) |
| 2016-11-27 | `feature` | new package | `ControlGroup.java`, `ControlGroupChangeListener.java` +4 | [6cad2953](https://github.com/freeplane/freeplane/commit/6cad295348dcc9c6ca5749dd1f8c89ef921cc83e) |
| 2016-11-26 | `fix` | Fix file mode bugs | `filemodemenu.xml`, `CenterAction.java` +5 | [42132f89](https://github.com/freeplane/freeplane/commit/42132f892671001e094a118457f48d82627eb995) |
| 2016-11-26 | `fix` | Fix handling of maps with same file name | `LastOpenedList.java` | [2fa9d08c](https://github.com/freeplane/freeplane/commit/2fa9d08c32ffa122b64b34da17e10eba797f49c4) |
| 2016-11-21 | `fix` | Fix race condition | `FreeplaneApplet.java` | [a09a7950](https://github.com/freeplane/freeplane/commit/a09a7950785ead3963cc97771c9bd4c0bddcc0b9) |
| 2016-11-21 | `fix` | Fix race condition | `FreeplaneApplet.java` | [6c31d6ac](https://github.com/freeplane/freeplane/commit/6c31d6acc98d5bbc48fbb594358f268784297da2) |
| 2016-11-21 | `fix` | Fix NPE : set current controller before using ResourceController # Conflicts: #	freeplane/ | `FreeplaneApplet.java` | [b6625432](https://github.com/freeplane/freeplane/commit/b6625432325fadb8388d7d901c6837674518b232) |
| 2016-11-21 | `fix` | Fix NPE : set current controller before using ResourceController | `FreeplaneApplet.java` | [a4c7ce3e](https://github.com/freeplane/freeplane/commit/a4c7ce3eb83abaab023359ceb7bb8e7f8a79085c) |
| 2016-11-20 | `fix` | bug fix #2359 ALT + S clears the node while editing | `EditNodeTextField.java` | [9259e673](https://github.com/freeplane/freeplane/commit/9259e673c47648215dbc09cc06a8737c168364a9) |
| 2016-11-19 | `fix` | Bug fix workaround for Knopflerfish bug | `ActivatorImpl.java`, `Launcher.java` | [c54e57da](https://github.com/freeplane/freeplane/commit/c54e57dadccffe0168f73feb5c6f58c4c45a8f95) |
| 2016-11-19 | `fix` | Fix NPE : lazy creation of ConnectorArrow icons | `ConnectorArrows.java` | [268f4f04](https://github.com/freeplane/freeplane/commit/268f4f048f59e265f515bde858f54e72d7630459) |
| 2016-11-18 | `fix` | Fix slide node folding | `Slide.java`, `UndoableSlide.java` | [0fa68a77](https://github.com/freeplane/freeplane/commit/0fa68a773056c110ac847e7d796f0303a03c295d) |
| 2016-11-18 | `feature` | Fix enable UI elements on presentation change | `CollectionBoxController.java` | [3f6e0da8](https://github.com/freeplane/freeplane/commit/3f6e0da82adb321623a81c8944f4951a4fef94ad) |
| 2016-11-18 | `fix` | Bug fix : restore minimized docking windows if their map becomes selected | `MapViewDockingWindows.java` | [c41c69b9](https://github.com/freeplane/freeplane/commit/c41c69b9f38ca60bd89a04b2c4dff6b7de9cf523) |
| 2016-11-18 | `fix` | Bug fix : restore minimized docking windows if their map becomes selected | `MapViewDockingWindows.java` | [3d98f9a5](https://github.com/freeplane/freeplane/commit/3d98f9a5df7b1fdaf5c87e2659e4326ec51bd999) |
| 2016-11-17 | `fix` | Fix copying of node border style | `MNodeStyleController.java` | [333eb07d](https://github.com/freeplane/freeplane/commit/333eb07da8fd2c6d6d0c0796d7555988c62e0174) |
| 2016-11-17 | `feature` | add example svg for UI icon | `HierarchicalIconsAction.svg` | [73a90cd2](https://github.com/freeplane/freeplane/commit/73a90cd203016c09919aa4109b1bee06fdc60059) |
| 2016-11-16 | `fix` | fix for folding / unfolding nodes on different views | `DefaultNodeMouseMotionListener.java` | [e1e887b7](https://github.com/freeplane/freeplane/commit/e1e887b71fd39f0d3e586f2373651afb93170968) |
| 2016-11-16 | `fix` | Cherry-pick fix for folding / unfolding nodes from slides branch | `MapController.java`, `ToggleFoldedAction.java` +1 | [9e36ac38](https://github.com/freeplane/freeplane/commit/9e36ac385efb74f94cc36df737bda4fbe60750a5) |
| 2016-11-16 | `fix` | Fix set_accelerator_on_next_click_helpmessage | `Resources_cs.properties`, `Resources_da.properties` +22 | [7ad89cd8](https://github.com/freeplane/freeplane/commit/7ad89cd8c6b3241cd062cbcefb460af303dd6019) |
| 2016-11-14 | `fix` | Fix  update presentation UI | `CollectionBoxController.java`, `SlideEditorController.java` | [0770f721](https://github.com/freeplane/freeplane/commit/0770f721bf47240e126af95f71d0e6c30f29ba00) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [2e38286e](https://github.com/freeplane/freeplane/commit/2e38286e3b35f58e558c329073a1eba35640d9c7) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | `MModeController.java`, `MacChanges.java` +1 | [096fbd1f](https://github.com/freeplane/freeplane/commit/096fbd1f116b38edc7648618cf2c5e45bcd7b536) |
| 2016-11-05 | `fix` | include upstreamed svgSalamander fix for scaling with fixed height (AUTOSIZE_VERT) | `build.gradle`, `kitfox-svg-salamander-1.1.1-p1-sources.jar` +4 | [0302bd52](https://github.com/freeplane/freeplane/commit/0302bd529fccc55c29abae732249dbc756c50e8a) |
| 2016-11-03 | `fix` | fix warnings | `CollectionBoxController.java` | [ccf8e0f3](https://github.com/freeplane/freeplane/commit/ccf8e0f380d88758fd1435927e963a1679916a83) |
| 2016-11-03 | `fix` | Fix NPE | `SlideEditorController.java` | [0efbe8a0](https://github.com/freeplane/freeplane/commit/0efbe8a0bc8bf28d6885429897346f3aedc98177) |
| 2016-11-01 | `fix` | Fix error output for user defined resources | `ApplicationResourceController.java`, `UserInputListenerFactory.java` | [8e8a83e5](https://github.com/freeplane/freeplane/commit/8e8a83e5f5a8ea9e6d14d717108a0f8f145e7e35) |
| 2016-11-01 | `fix` | try to bug fix user resources for linux / mac | `ApplicationResourceController.java` | [c9a41ac3](https://github.com/freeplane/freeplane/commit/c9a41ac3f33202dfa25c4b3e8073bed2b6a17627) |
| 2016-10-31 | `fix` | try to bug fix user resources for linux / mac | `ApplicationResourceController.java` | [2b3a6e60](https://github.com/freeplane/freeplane/commit/2b3a6e6087fa06c6105b792a4e7256d1d3c9da9c) |
| 2016-10-31 | `fix` | Fix stopping and running presentation | `JAutoToggleButton.java`, `TranslatedElementFactory.java` +2 | [195941d2](https://github.com/freeplane/freeplane/commit/195941d2d602862c74c2f2a7ff7973b66654710e) |
| 2016-10-30 | `fix` | Fix NPE | `LinkController.java`, `MLinkController.java` | [1fd068aa](https://github.com/freeplane/freeplane/commit/1fd068aa1a48d9f027d606d48bf76e3a749b5c60) |
| 2016-10-30 | `feature` | Enable preferences dialog and about action for style editor | `stylemodemenu.xml`, `ShowPreferencesAction.java` +1 | [53c21bcd](https://github.com/freeplane/freeplane/commit/53c21bcdde6c4b7057839828db6064be5e6f6ffb) |
| 2016-10-29 | `fix` | Fix font box width | `MUIFactory.java`, `MModeControllerFactory.java` | [88740d14](https://github.com/freeplane/freeplane/commit/88740d14e40352852b15b2db274ab0e86d36b42e) |
| 2016-10-29 | `fix` | Fix NPE | `LastOpenedList.java` | [79f2a0ae](https://github.com/freeplane/freeplane/commit/79f2a0ae73ed36c0c035b70428cd9ad0e6e2883e) |
| 2016-10-29 | `fix` | Fix class cast exception | `MMapController.java` | [c2d3a41e](https://github.com/freeplane/freeplane/commit/c2d3a41e2f5ab73b95b3362fedbd1f014f1dd6da) |
| 2016-10-29 | `fix` | Bug fix for failing test | `NamedElementCollection.java` | [16c4ff63](https://github.com/freeplane/freeplane/commit/16c4ff631f28c9d4bb7033d644031a4253f611c9) |
| 2016-10-29 | `fix` | fix names | `preferences.xml`, `ConnectorArrows.java` | [622820a4](https://github.com/freeplane/freeplane/commit/622820a4a1cb9f988f80e6449c52195a156ee5e7) |
| 2016-10-29 | `feature` | add private and final | `NavigationPanelController.java` | [d95e06d1](https://github.com/freeplane/freeplane/commit/d95e06d19b62fde36ef0fe4033aaebd2c9ac0c41) |
| 2016-10-25 | `fix` | Fix resizer: make collapsed components invisible | `OneTouchCollapseResizer.java` | [e1816152](https://github.com/freeplane/freeplane/commit/e18161526d88f1d88a629c05bffdc0677ebe5336) |
| 2016-10-25 | `fix` | Fix border color attribute in node style writer | `NodeStyleBuilder.java` | [352299dd](https://github.com/freeplane/freeplane/commit/352299dd3ffacee09685e554847bd50e00fec9f5) |
| 2016-10-24 | `fix` | Fix NPE | `PresentationEditorController.java` | [6dccb997](https://github.com/freeplane/freeplane/commit/6dccb997a5c804842e34bbb0d983899711c1c2c1) |
| 2016-10-24 | `fix` | fix bugs in slides | `DisjunctConditions.java`, `NamedElementCollection.java` +4 | [b0aea822](https://github.com/freeplane/freeplane/commit/b0aea8226fd3b5f08fb4be5445598e18c0663138) |
| 2016-10-22 | `fix` | Fix failing test | `FreeplaneHeadlessStarter.java` | [6527baa1](https://github.com/freeplane/freeplane/commit/6527baa1c5925aa4aa9d25083ec7afa1dee46858) |
| 2016-10-21 | `fix` | Fix presentation state updates | `NavigationPanelController.java`, `PresentationController.java` +1 | [1a4f09cf](https://github.com/freeplane/freeplane/commit/1a4f09cf91ef70ba69ace8e50ca34df9c8691693) |
| 2016-10-20 | `feature` | Add presentation menu items | `mindmapmodemenu.xml`, `PresentationController.java` +1 | [d7d9b01c](https://github.com/freeplane/freeplane/commit/d7d9b01c274e0115ac9d1a1b89a742122a5ff387) |
| 2016-10-18 | `feature` | Implement persistence | `NamedElementCollection.java`, `PresentationBuilder.java` +3 | [65f35045](https://github.com/freeplane/freeplane/commit/65f35045030cbba7d05cbad249d249fa95a3f422) |
| 2016-10-16 | `feature` | Add / remove nodes to slide | `SlideEditorController.java`, `SlideModel.java` | [65bd6de1](https://github.com/freeplane/freeplane/commit/65bd6de145b2a476009ce82209c6e7eddf7edc4f) |
| 2016-10-16 | `feature` | Add missing annotations | `SlideModel.java` | [9fa761bd](https://github.com/freeplane/freeplane/commit/9fa761bd92c197c7f7e105bd0fddcd54e3e60e46) |
| 2016-10-16 | `fix` | Bug fix | `SlideEditorController.java` | [af6628e7](https://github.com/freeplane/freeplane/commit/af6628e7671908f40b23779534498cec154fe564) |
| 2016-10-16 | `fix` | Fix layout | `CollectionBoxController.java`, `NavigationPanelController.java` +1 | [681bd142](https://github.com/freeplane/freeplane/commit/681bd14250fe0d7e2b534b720d009d05c9e62a00) |
| 2016-10-06 | `feature` | Add presentation editor to GUI | `MapPresentations.java`, `PresentationController.java` +1 | [04f2a952](https://github.com/freeplane/freeplane/commit/04f2a95218913ca1abe9054bea4676cfd00e57a2) |
| 2016-10-04 | `feature` | Add presentation collection model | `build.gradle`, `PresentationCollectionModel.java` +2 | [918451e9](https://github.com/freeplane/freeplane/commit/918451e9cd2baeca5fa608979d48b1fae0f3b5c0) |
| 2016-10-04 | `feature` | Add zoom button | `PresentationEditorPanel.java` | [9eae200f](https://github.com/freeplane/freeplane/commit/9eae200f6a8ac3883bf7ad0703ae24afce2787fa) |
| 2016-10-02 | `fix` | fix writeIconSize() with clones | `NodeWriter.java`, `NodeStyleBuilder.java` | [afce84cc](https://github.com/freeplane/freeplane/commit/afce84ccac52ebc4613704889321ca55c68e3d95) |
| 2016-10-02 | `fix` | write ICON_SIZE at the correct place (even if there are no IExtensions), fix icon size ena | `NodeStyleBuilder.java`, `StyleEditorPanel.java` | [278ab8db](https://github.com/freeplane/freeplane/commit/278ab8db0ceff5971decef15c3ac1d8ac758f1c6) |
| 2016-10-02 | `fix` | Fix icon size control | `StyleEditorPanel.java` | [2f54329d](https://github.com/freeplane/freeplane/commit/2f54329d839f7da06ea23f95eb2e3424f6531584) |
| 2016-10-02 | `feature` | icon size persistency: add NodeModel information where needed | `NodeStyleBuilder.java` | [0f96a2d9](https://github.com/freeplane/freeplane/commit/0f96a2d98265668d6a906bf180d4df799207894c) |
| 2016-10-02 | `fix` | Fix node not folded at the end of traversion cycle | `MapNavigationUtils.java` | [93786140](https://github.com/freeplane/freeplane/commit/93786140bac8f33e426a1d9e8ffa39ef4d07b67e) |
| 2016-10-02 | `feature` | Don not try to create relative links for unsaved maps on drag and drop | `MClipboardController.java` | [a00cfbff](https://github.com/freeplane/freeplane/commit/a00cfbff8a95a26b5684605654a81dd649f37fd4) |
| 2016-09-28 | `fix` | Fix line feeds in exported html | `MindMapHTMLWriter.java` | [b28299b5](https://github.com/freeplane/freeplane/commit/b28299b5f8fa5bcb9c3004e971baca5bafd8ebea) |
| 2016-09-28 | `fix` | Fix html export : remove wrong </span> elements | `MindMapHTMLWriter.java` | [10dfc465](https://github.com/freeplane/freeplane/commit/10dfc4653989ed4b5158a952e62069ddf4c44106) |
| 2016-09-27 | `fix` | Fix java.lang.IllegalArgumentException: bad position: | `EditNodeDialog.java` | [43fb18f5](https://github.com/freeplane/freeplane/commit/43fb18f52c72c1b94b1fdd0d5567e5bbd807449f) |
| 2016-09-27 | `fix` | Fix font size for attribute panel attribute editor | `AttributeTable.java` | [e1b39db2](https://github.com/freeplane/freeplane/commit/e1b39db20b030e53420bc8fe4ea85e4663c483bd) |
| 2016-09-27 | `fix` | Fix class cast exception | `MClipboardController.java` | [9a33f63f](https://github.com/freeplane/freeplane/commit/9a33f63fca2beaf7a09cbc93eef77d2dcc9bfb88) |
| 2016-09-25 | `feature` | Rework survey: add "Open link in browser", "frequency" | `FreeplaneGUIStarter.java`, `FreeplaneSurveyProperties.java` +3 | [63f2b8d4](https://github.com/freeplane/freeplane/commit/63f2b8d468c4c866ba84084b942d9a6a91bc4f04) |
| 2016-09-25 | `feature` | SVG: Fetch current node icon size setting from style, support only squared icons | `Resources_de.properties`, `IconController.java` +5 | [fb7bfbbe](https://github.com/freeplane/freeplane/commit/fb7bfbbe4be19150cbc28194ebde4505f7b01445) |
| 2016-09-24 | `feature` | Clean up and add border to message pane | `SurveyRunner.java`, `SurveyStarter.java` | [f7d80dd2](https://github.com/freeplane/freeplane/commit/f7d80dd2ffcdad86ebb44ba0e9f3e7887ed5c373) |
| 2016-09-23 | `feature` | Add option "Later" to survey runner | `SurveyRunner.java` | [7df82a2f](https://github.com/freeplane/freeplane/commit/7df82a2feb69be4d0f2155818cb940c6790a9fa3) |
| 2016-09-22 | `fix` | #2412 fix FP 1 5 16 pre 07: accelerator key any longer available | `ActionAcceleratorManager.java` | [853617f1](https://github.com/freeplane/freeplane/commit/853617f15a881396ea0f134ec438c59df5da5881) |
| 2016-09-21 | `feature` | #2410 Make link to and from anchor should create relative hyperlinks | `LinkController.java`, `MLinkController.java` +2 | [fb3278f3](https://github.com/freeplane/freeplane/commit/fb3278f3ecfd4986977d6f8fad142612fd23c1d0) |
| 2016-09-11 | `feature` | Allow translators to add new tool tips only for English | `UITextChanger.java` | [5daa0ee3](https://github.com/freeplane/freeplane/commit/5daa0ee33f1cd1383f46c9049cbcbe656870eaa7) |
| 2016-09-10 | `fix` | Fix NPE | `NoteManager.java` | [df573e10](https://github.com/freeplane/freeplane/commit/df573e109eb8938853c61c2d79b9c748135d709f) |
| 2016-09-10 | `fix` | Fix accelerator manager initialization | `ResourceController.java` | [1dee4ae5](https://github.com/freeplane/freeplane/commit/1dee4ae5c06515e82b27c38868ba53ac2dece3ff) |
| 2016-09-10 | `fix` | Bug fix: Command line option with node ID | `UrlManager.java` | [0150361f](https://github.com/freeplane/freeplane/commit/0150361f355bc8dbc1c2be27272272af37c5693b) |
| 2016-09-07 | `fix` | Bug fix: load accelerator presets only once | `ModeController.java`, `FreeplaneApplet.java` +1 | [af3889f9](https://github.com/freeplane/freeplane/commit/af3889f94f2b449ee0c6017ea47dea68cf54aac6) |
| 2016-09-05 | `fix` | Bug fix | `NodeAbsolutePath.java`, `NodeRelativePath.java` | [83b7ca7d](https://github.com/freeplane/freeplane/commit/83b7ca7de6b6ea5171f28486a49c92ec5d6188b1) |
| 2016-09-05 | `fix` | Do not use screen resolution values returned by Toolkit: they are never correct. | `preferences.xml`, `Resources_cs.properties` +22 | [12f81ba3](https://github.com/freeplane/freeplane/commit/12f81ba3a8fc177c3d8843a15e74409350139d6d) |
| 2016-09-04 | `fix` | Fix layout for summary nodes if all summarized nodes are free nodes | `VerticalNodeViewLayoutStrategy.java` | [83d465cc](https://github.com/freeplane/freeplane/commit/83d465ccd7aa806183d63a1ae8f6c8b476e38845) |
| 2016-09-04 | `feature` | #2395 Improve multiple screen support | `UITools.java`, `AFilterComposerDialog.java` +1 | [0375d918](https://github.com/freeplane/freeplane/commit/0375d918823cdf017d222629cf9bfccb75a613ab) |
| 2016-09-04 | `feature` | Implement node sort based on position in map tree | `NodeRelativePath.java`, `MapView.java` +1 | [f4a0c282](https://github.com/freeplane/freeplane/commit/f4a0c282865d6677f8f20464a4ebdbb3d4f1ce5c) |
| 2016-09-01 | `feature` | Support transparent border colors | `NodeStyleBuilder.java` | [291c1db3](https://github.com/freeplane/freeplane/commit/291c1db3270dd92bc2030e95f46b22b0a1a943dc) |
| 2016-08-31 | `fix` | Fix saving NodeBorderModel attributes | `NodeStyleBuilder.java` | [ff39019c](https://github.com/freeplane/freeplane/commit/ff39019ca882fb157adb44cc5130926b7a3f2768) |
| 2016-08-30 | `fix` | fix enabled / disabled controls | `StyleEditorPanel.java` | [661b4b16](https://github.com/freeplane/freeplane/commit/661b4b16c49b830202c798e866bf1b247ddc0fc4) |
| 2016-08-30 | `fix` | Fix border size calculation for fork views | `ForkMainView.java` | [68c07071](https://github.com/freeplane/freeplane/commit/68c07071e314a34ff0314d650d7b02d0fefc93de) |
| 2016-08-30 | `feature` | implement changing (SVG) icon size | `Resources_de.properties`, `MultipleImage.java` +10 | [c03e29af](https://github.com/freeplane/freeplane/commit/c03e29af8390992dab0db104dc46b237459220c3) |
| 2016-08-30 | `fix` | Fix property name | `MFileManager.java` | [f6559651](https://github.com/freeplane/freeplane/commit/f65596516cb9189759e54d96d3f45eacc17e320b) |
| 2016-08-30 | `feature` | Create separate class for node border model | `NodeBorderModel.java`, `NodeSizeModel.java` +4 | [a27cffe7](https://github.com/freeplane/freeplane/commit/a27cffe74bc99b2f7b1a75b06eca31ecca2cdd53) |
| 2016-08-30 | `feature` | Add new elements for controlling node border width to editor panel | `StyleEditorPanel.java`, `Resources_en.properties` | [bc82a888](https://github.com/freeplane/freeplane/commit/bc82a88878f3bb0b5262805e2f2a903b88d9d917) |
| 2016-08-30 | `feature` | Add new elements for controlling node border width to model and controller | `mapVersions.xml`, `FreeplaneVersion.java` +5 | [9d7fba86](https://github.com/freeplane/freeplane/commit/9d7fba86a0d20ab9b6def500e19c9f8d0f1c3915) |
| 2016-08-29 | `fix` | Fix class cast exception | `MapController.java` | [8e24d661](https://github.com/freeplane/freeplane/commit/8e24d6619645c9a2ab9dd19f159ee01c9eb43706) |
| 2016-08-29 | `fix` | Bug fix : close edited maps on quit if currently non-editing mode is active | `FrameController.java` | [59b285d6](https://github.com/freeplane/freeplane/commit/59b285d6fa558609bb3b4498108f7449cd1e2f6c) |
| 2016-08-22 | `fix` | Fix colors for items in condition list for numbus UI | `ConditionFactory.java`, `ConditionNotSatisfiedDecorator.java` +5 | [3c6c9208](https://github.com/freeplane/freeplane/commit/3c6c92089d4a6833d9b30c189ce22ff86c647687) |
| 2016-08-21 | `fix` | Bug fix: disallow transparent map background colors | `ColorUtils.java`, `MapStyle.java` | [58db3464](https://github.com/freeplane/freeplane/commit/58db346415524d71e69590a57add59ba8cb37076) |
| 2016-08-21 | `feature` | Pre select standard template in template drop-down for new maps | `MFileManager.java` | [c81de4ee](https://github.com/freeplane/freeplane/commit/c81de4ee298a0e18b0babfe8d3a9a3b976ed661a) |
| 2016-08-20 | `fix` | Fix saving freeplane properties on quit | `Controller.java`, `ApplicationResourceController.java` +1 | [c70cad8b](https://github.com/freeplane/freeplane/commit/c70cad8bbefcb5d257eb9604e2d45ee0aec03a19) |
| 2016-08-16 | `fix` | #2387 fix NPE if null value is set to min / max width | `Quantity.java`, `MLocationController.java` +2 | [2661eb46](https://github.com/freeplane/freeplane/commit/2661eb460402cf1ca73daca81369e6b1f48de71e) |
| 2016-08-15 | `feature` | add UI for changing (SVG) icon size | `StyleEditorPanel.java`, `Resources_en.properties` | [9f91046b](https://github.com/freeplane/freeplane/commit/9f91046b6d00a4f91cdc84fa9714dab40f23caee) |
| 2016-08-15 | `feature` | add and call onApplicationStopped method to ApplicationLifecycleListener | `Controller.java`, `ApplicationLifecycleListener.java` +3 | [50e37859](https://github.com/freeplane/freeplane/commit/50e37859cb3001c3468fa904b4b56370aceb8796) |
| 2016-08-14 | `fix` | use correct method | `FreeplaneIconUtils.java` | [7010d72b](https://github.com/freeplane/freeplane/commit/7010d72b18fc49bcadf019872da174fbd703fd2b) |
| 2016-08-14 | `fix` | Fix loading svg of icons | `FreeplaneIconUtils.java` | [f70f7bb4](https://github.com/freeplane/freeplane/commit/f70f7bb4ea008e1b44e6eda8a360d8a8f004dce5) |
| 2016-08-14 | `feature` | Add navigation to weblate from text changer | `weblate-32.png`, `UITextChanger.java` +2 | [b652fce6](https://github.com/freeplane/freeplane/commit/b652fce602ce66f0ad5bbbd9115cd44b81d1251c) |
| 2016-08-13 | `feature` | #2384 Allow to create icons from add-ons and scripts | `FreeplaneIconUtils.java`, `ImageIconFactory.java` | [485d7811](https://github.com/freeplane/freeplane/commit/485d78116ecbdb56572bb03a00bda68bb8edaa71) |
| 2016-08-13 | `fix` | Fix class cast exception | `NodeView.java` | [4898ca25](https://github.com/freeplane/freeplane/commit/4898ca2582ee2cada9dc97ef7f13fb5e98514cda) |
| 2016-08-13 | `fix` | Fix NPE: change folding only for currently selected maps | `DefaultMouseWheelListener.java` | [0c6386f2](https://github.com/freeplane/freeplane/commit/0c6386f2ecda9b0c0f44c4881cb7dc8a3052138c) |
| 2016-08-13 | `fix` | Fix NPE | `MapView.java` | [14573db7](https://github.com/freeplane/freeplane/commit/14573db74fdd82921b99d2b8cce7c8a22916da93) |
| 2016-08-13 | `fix` | Fix NPE | `MapController.java` | [2a33539c](https://github.com/freeplane/freeplane/commit/2a33539ca5dc5c6d3ef9e6f00f70918da0228e90) |
| 2016-08-13 | `fix` | Fix NPE in MapScroller | `MapScroller.java` | [ae2ca0a5](https://github.com/freeplane/freeplane/commit/ae2ca0a5a06f5f2aa963dd457c78be0d22691335) |
| 2016-08-13 | `fix` | Fix concurrent modification exception | `AttributeRegistry.java` | [5e1be0bb](https://github.com/freeplane/freeplane/commit/5e1be0bbf8e03e09d5b13701a3f8155f4805caf4) |
| 2016-08-06 | `fix` | Prevent class cast exception: use correct mode controller | `DocumentationAction.java` | [21cc502e](https://github.com/freeplane/freeplane/commit/21cc502e00a95697320d36502b242708afda3321) |
| 2016-08-06 | `fix` | Fix linked branch import | `ImportLinkedBranchWithoutRootAction.java` | [d7bee1c2](https://github.com/freeplane/freeplane/commit/d7bee1c229569dd054f06f5774b17eb9d052398e) |
| 2016-08-06 | `fix` | Fix accelerators configured in property files | `ActionAcceleratorManager.java` | [120ed9c3](https://github.com/freeplane/freeplane/commit/120ed9c33499aa02fc0c862b6a40814ac3b6067d) |
| 2016-07-30 | `fix` | FIX: command line format string design | `CommandLineParser.java` | [1088973b](https://github.com/freeplane/freeplane/commit/1088973bbac1edd0100c9749cbc74d77fbe60280) |
| 2016-07-30 | `fix` | FIX: exit Freeplane after showing (optimized) help text on comand line | `CommandLineParser.java` | [0ee7b8ad](https://github.com/freeplane/freeplane/commit/0ee7b8ad63aa29af6979dc28404bf06acb2b20a1) |
| 2016-07-23 | `fix` | Bug fix : do not reload maps if escape is clicked in FileRevisionsDialog | `FileRevisionsDialog.java` | [847a30f8](https://github.com/freeplane/freeplane/commit/847a30f89b307e44f928409b7309f3e2e9638742) |
| 2016-07-22 | `fix` | Bug fix: some connectors were not painted | `MapLinks.java`, `MapView.java` | [831395e6](https://github.com/freeplane/freeplane/commit/831395e6e607bf5e5e49448316427017b76722fa) |
| 2016-07-18 | `fix` | Bug fix: do not reset filter for selected nodes | `MapView.java` | [708de1ea](https://github.com/freeplane/freeplane/commit/708de1ea55d638f143e542d77bccb172bdc464f6) |
| 2016-07-17 | `feature` | Add preference lookandfeel.scaleuifonts | `preferences.xml`, `FrameController.java` +4 | [cab03129](https://github.com/freeplane/freeplane/commit/cab0312941af4ce2ea2ac0fa0a81f1b462f647b6) |
| 2016-07-15 | `feature` | Add logging to analyze NPE | `NodeView.java` | [6d2a3330](https://github.com/freeplane/freeplane/commit/6d2a3330f9541143359f06bade1a1c8aff22c0a3) |
| 2016-07-14 | `fix` | Fix opening files on start for mac OS | `FreeplaneGUIStarter.java` | [dab71802](https://github.com/freeplane/freeplane/commit/dab71802ab7367d48a47222450158cc0b736b2fb) |
| 2016-07-13 | `fix` | #2370 Cannot paste images in Free plane using insert inline images : fix paste from clipbo | `MClipboardController.java`, `ImageAdder.java` +1 | [de7d0370](https://github.com/freeplane/freeplane/commit/de7d03700b21b3bf03ff4aa206feecd03c4e9eb3) |
| 2016-07-09 | `fix` | Fix NPE | `MainView.java` | [0df5b839](https://github.com/freeplane/freeplane/commit/0df5b8394aec424d6f7fc4daa890303f9e4e13ce) |
| 2016-07-05 | `feature` | Add prefs options for SVG rendering | `preferences.xml`, `Resources_de.properties` +4 | [a55c6f84](https://github.com/freeplane/freeplane/commit/a55c6f8497dbc8ab4c5d2018357709bbfa38ed59) |
| 2016-06-26 | `feature` | Add method newMapFromTemplate to controller proxy | `MMapIO.java`, `ControllerProxy.java` +1 | [84413751](https://github.com/freeplane/freeplane/commit/844137510fbd4c4a3fb7dfa45966b34716d3d28d) |
| 2016-06-25 | `fix` | Fix NPE in JOrtho | `CheckerListener.java` | [0476d3a0](https://github.com/freeplane/freeplane/commit/0476d3a0c469fc968a0d3f00f3ae55a0089a0340) |
| 2016-06-25 | `fix` | fix NPE | `NodeList.java` | [c1bd23cd](https://github.com/freeplane/freeplane/commit/c1bd23cd7b68f3572a45bd50af4c7b86986cec0d) |
| 2016-06-18 | `fix` | Fix automatic removing of summary nodes for clones when all their child nodes are moved or | `SummaryNode.java`, `MMapController.java` | [8aa3133d](https://github.com/freeplane/freeplane/commit/8aa3133d338592e4a115ce032037b9f43290ee0f) |
| 2016-06-18 | `fix` | fix NPE | `ColorUtils.java` | [6618aebc](https://github.com/freeplane/freeplane/commit/6618aebcc9977473fa35bfc750fa1a6703e79220) |
| 2016-06-17 | `fix` | #2359 Fix split node implementation: use HTML | `MTextController.java` | [fcf08152](https://github.com/freeplane/freeplane/commit/fcf0815236a07716588464200f0d2d9571bd6e4d) |
| 2016-06-11 | `fix` | fix layout symmetry for summarized nodes | `VerticalNodeViewLayoutStrategy.java` | [6b4cfa01](https://github.com/freeplane/freeplane/commit/6b4cfa01faaaf30dd3562edb6d17322a3d98504c) |
| 2016-06-11 | `fix` | Fix layout for filtered summary nodes if all item nodes are not filtered | `VerticalNodeViewLayoutStrategy.java` | [0359c6a7](https://github.com/freeplane/freeplane/commit/0359c6a7b1039c342b27d918cd86ce40d3783f4e) |
| 2016-06-04 | `fix` | Fix bug when node is moved to subtree clone of its parent | `MMapController.java` | [94a18e7d](https://github.com/freeplane/freeplane/commit/94a18e7da05cfb09c076ede384570bf211fababe) |
| 2016-05-29 | `fix` | fix node selection for URIs containing node IDs | `LastOpenedList.java` | [a6cf1ff3](https://github.com/freeplane/freeplane/commit/a6cf1ff3f75cf7220bfcac5d667dd47e1818e773) |
| 2016-05-29 | `feature` | Support look and feels installed by users | `OptionPanelBuilder.java`, `ClassLoaderFactory.java` +4 | [5804b7ad](https://github.com/freeplane/freeplane/commit/5804b7adaa1c28bfa5b5c75fbc3395cb082ec57d) |
| 2016-05-28 | `fix` | fix stream handling | `OptionPanel.java` | [46d3394c](https://github.com/freeplane/freeplane/commit/46d3394c8f9d17f229f1f3e8989f50729f720136) |
| 2016-05-22 | `fix` | fix online docu action | `OnlineDocumentationAction.java` | [de2a5a7f](https://github.com/freeplane/freeplane/commit/de2a5a7fab72a775ab4dff08480698af6d4e5283) |
| 2016-05-21 | `fix` | Fix class cast exception | `ImagePreview.java`, `ViewerController.java` | [087a0b8b](https://github.com/freeplane/freeplane/commit/087a0b8b7fdd641e014678b3fbf51ecc4c6f8e15) |
| 2016-05-21 | `fix` | Fix ESCAPE hot key from editors | `FreeplaneMenuBar.java`, `ConnectedToMenuView.java` +2 | [f1c6eec5](https://github.com/freeplane/freeplane/commit/f1c6eec5363200a020ccba9d84b91515493dafc4) |
| 2016-05-21 | `feature` | Support translarent colors | `ColorProperty.java`, `ColorUtils.java` +7 | [7f908ecb](https://github.com/freeplane/freeplane/commit/7f908ecbe354de76723e36021aa84839cd96f878) |
| 2016-05-20 | `fix` | Fix opening of files containing # character in path | `MapController.java`, `FreeplaneGUIStarter.java` | [e5cb2127](https://github.com/freeplane/freeplane/commit/e5cb21279dec89f9c59aef7699884da612b0e04f) |
| 2016-05-16 | `fix` | Fix map focus for documentation action | `DocumentationAction.java` | [75f5b715](https://github.com/freeplane/freeplane/commit/75f5b7151c99442c77e8f96fbaa3da9d26f41817) |
| 2016-05-16 | `feature` | Add Basque language to configuration | `OptionPanelBuilder.java`, `freeplane.properties` +1 | [2b843d99](https://github.com/freeplane/freeplane/commit/2b843d99dc3ce1f187836c32f048b6c9ad738b1c) |
| 2016-05-16 | `feature` | Add baskue translation file as requested | `Resources_eu.properties` | [6c070ace](https://github.com/freeplane/freeplane/commit/6c070ace4d808463da76f3b2ee2d00281564b277) |
| 2016-05-16 | `feature` | Select template when new map is created | `history_en.txt`, `preferences.xml` +2 | [76510b1e](https://github.com/freeplane/freeplane/commit/76510b1e26cf6a0e73749c53e36c26e5f3b7b1b6) |
| 2016-05-15 | `feature` | Integrate what's new map | `freeplaneApplications.mm`, `freeplaneApplications_ja.mm` +6 | [580602b7](https://github.com/freeplane/freeplane/commit/580602b70ee3f1366265c4723ea867d5a1585bed) |
| 2016-05-08 | `fix` | Fix mnemonics for shtml dialog with buttons | `Resources_ar.properties`, `Resources_ca.properties` +24 | [2aa63483](https://github.com/freeplane/freeplane/commit/2aa63483771bca649fdf526fbecd59c095b3469c) |
| 2016-05-08 | `fix` | fix use of alt+LETTER short cuts: they should have priority over mnemonics | `ActionAcceleratorManager.java`, `IKeyStrokeProcessor.java` +10 | [a3c29474](https://github.com/freeplane/freeplane/commit/a3c29474f07a6517e5bed65fc03c5737d7ee48dc) |
| 2016-05-08 | `fix` | fix use of alt+LETTER short cuts: they should have priority over mnemonics | `ActionAcceleratorManager.java`, `IKeyStrokeProcessor.java` +10 | [b69d4290](https://github.com/freeplane/freeplane/commit/b69d42904fc00b3bfff8ebef2e0cadc655e1cf25) |
| 2016-05-07 | `fix` | Fix translation editor for properties | `PropertyAdapter.java`, `TextUtils.java` | [0b1b7775](https://github.com/freeplane/freeplane/commit/0b1b77750d7b2db2eef72d0e775dbc02a93386a4) |
| 2016-05-06 | `fix` | Fix case of missing tool tip | `UITextChanger.java` | [0dec6b7f](https://github.com/freeplane/freeplane/commit/0dec6b7f249db3945764d3c98672b486528184fe) |
| 2016-05-05 | `api_change` | Use TextChangeHotKeyAction to configure a hot key for user interface change | `build.gradle`, `mindmapmodemenu.xml` +10 | [e4596726](https://github.com/freeplane/freeplane/commit/e459672605047ac1c5331f4ae8289047a6c6dbc8) |
| 2016-05-05 | `feature` | Support editing titled borders and tool tips | `PropertyAdapter.java`, `SeparatorProperty.java` +4 | [33e9128e](https://github.com/freeplane/freeplane/commit/33e9128e25e6194249e0bb50f9391d07ee15af3c) |
| 2016-05-03 | `fix` | Fix NodeList AKA find and replace dialog | `NodeList.java` | [0d38557e](https://github.com/freeplane/freeplane/commit/0d38557e6af804c82bd9bae920d77026f2ced674) |
| 2016-04-27 | `fix` | Fix NPE | `ActionAcceleratorManager.java` | [55c72e6f](https://github.com/freeplane/freeplane/commit/55c72e6fe78f6cf5c59b85b44f6a2e8ea6edb7c0) |
| 2016-04-25 | `feature` | avoid all translation warnings for add-ons | `AddOnsController.java` | [6a3f1dd0](https://github.com/freeplane/freeplane/commit/6a3f1dd09b19dcbd1a69bcb21ccfead70e276e0f) |
| 2016-04-24 | `feature` | revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations) | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943) |
| 2016-04-24 | `feature` | avoid all translation warnings for add-ons | `AddOnProperties.java`, `AddOnDetailsPanel.java` +2 | [ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c) |
| 2016-04-23 | `fix` | Fix applet | `build.gradle`, `browsemodemenu.xml` +14 | [3a21729b](https://github.com/freeplane/freeplane/commit/3a21729b6e1b63bd74c67b4fe31ca7e1a4d801e4) |
| 2016-04-20 | `fix` | Fix size calculations | `BubbleMainView.java`, `OvalMainView.java` +2 | [f57e1c2b](https://github.com/freeplane/freeplane/commit/f57e1c2b0d6452b2ae2fe349bf1cf3d0d5fed518) |
| 2016-04-17 | `fix` | Fix action accelerator manager for actions shared in different mode controllers | `ActionAcceleratorManager.java`, `IAcceleratorMap.java` +3 | [d0e3edd4](https://github.com/freeplane/freeplane/commit/d0e3edd4d55f786e18e55147569db8307bee62d4) |
| 2016-04-17 | `fix` | Bug fix : freeplane tried to open map twice after grad and drop | `FileOpener.java` | [6ada4d3e](https://github.com/freeplane/freeplane/commit/6ada4d3e651b1ba56e6c5cf055ccbebd6ee40314) |
| 2016-04-16 | `fix` | Fix class cast exception | `MLogicalStyleController.java` | [c4466186](https://github.com/freeplane/freeplane/commit/c446618666121ff0a3756d559cf16b8a558c639b) |
| 2016-04-16 | `feature` | Fix new summary node check if one node is ancestor of the other one | `NewSummaryAction.java` | [6f798c99](https://github.com/freeplane/freeplane/commit/6f798c991511ce99f5da0beebc873373e9a957df) |
| 2016-04-16 | `fix` | Fix NPE | `MapController.java` | [7bb2564d](https://github.com/freeplane/freeplane/commit/7bb2564df859d5eb5fafe2bed1ddfead71b108cb) |
| 2016-04-10 | `feature` | added init script facility | `Controller.java`, `ApplicationLifecycleListener.java` +4 | [7d88585d](https://github.com/freeplane/freeplane/commit/7d88585dfd029e48fe3e62ee8f0aa89e1f0b6271) |
| 2016-03-30 | `fix` | Fix warnings | `ZoomableLabel.java` | [14945853](https://github.com/freeplane/freeplane/commit/14945853280ff33b37ae2eacf3ee1d2761390475) |
| 2016-03-29 | `fix` | Fix warnings | `GrabKeyDialog.java`, `FButtonBar.java` +8 | [c5f78c0c](https://github.com/freeplane/freeplane/commit/c5f78c0c436ab8de7cc3d91aa404d70a8ef652eb) |
| 2016-03-28 | `fix` | Fix URLPermission | `SecureRunner.java`, `ScriptingSecurityManager.java` | [46a4c4d6](https://github.com/freeplane/freeplane/commit/46a4c4d680dbfcccb9c4e79c80d4c1553aa5f4df) |
| 2016-03-27 | `fix` | Fix scripting security issues | `FreeplaneGUIStarter.java`, `FreeplaneSecurityManager.java` +6 | [1490c603](https://github.com/freeplane/freeplane/commit/1490c603c9c143273ca31f118a63cec049c24a3c) |
| 2016-03-19 | `feature` | #2214 Adding updateUrl to add-on leads to installation error fix NPE | `AddOnProperties.java` | [cf444355](https://github.com/freeplane/freeplane/commit/cf444355726206deb29fac26d3afdddcaef03de2) |
| 2016-03-18 | `feature` | #2214 Adding updateUrl to add-on leads to installation error convert updateUrl from URI va | `AddOnProperties.java` | [93bd9880](https://github.com/freeplane/freeplane/commit/93bd9880cb186d343563421b6eb69315bbb8d205) |
| 2016-03-13 | `fix` | Fix test | `MenuBuilderAcceptanceTest.java` | [b5d19334](https://github.com/freeplane/freeplane/commit/b5d193345a0bdcff351f3bac605c6da5786b05a0) |
| 2016-03-13 | `feature` | Add mnemonics to menu bar before showing | `JMenubarBuilder.java`, `MenuMnemonicSetter.java` | [b94768ef](https://github.com/freeplane/freeplane/commit/b94768efe26e3e9b439659096f3e7e8108da3a0e) |
| 2016-03-13 | `fix` | Fix bugs and increase performance of MnemonicSetter | `MnemonicSetter.java`, `MnemonicSetterShould.java` | [ee75282d](https://github.com/freeplane/freeplane/commit/ee75282d1cc4f1cd7eb8967fd2bbde1e45ecc161) |
| 2016-03-12 | `fix` | Fix non ascii mnemonics | `ActionNameMnemonicHolderHolder.java`, `ButtonNameMnemonicHolder.java` | [9a89b005](https://github.com/freeplane/freeplane/commit/9a89b0054284fe9651659c07f73221c5e394ba2b) |
| 2016-03-12 | `fix` | Fix and report class cast exception | `VerticalNodeViewLayoutStrategy.java` | [40ebe816](https://github.com/freeplane/freeplane/commit/40ebe8168c7118da9e49ec80b7a0e5c80a21b8f1) |
| 2016-03-06 | `fix` | Bug fix for handling of local hyperlinks in clones | `ConnectorModel.java`, `HyperTextLinkModel.java` +2 | [f52a99c2](https://github.com/freeplane/freeplane/commit/f52a99c24421f2159ca55e3f7c14e9d89bdf111e) |
| 2016-03-06 | `fix` | Fix NPE | `UrlManager.java` | [237f9c9a](https://github.com/freeplane/freeplane/commit/237f9c9a8ef1d8ebb35c740c1676dd67141e98da) |
| 2016-03-03 | `fix` | Fix layout bug: summarized nodes were not properly centered to their parent node | `VerticalNodeViewLayoutStrategy.java` | [03962352](https://github.com/freeplane/freeplane/commit/039623528d1fc85415915bddf94d07982cc63b63) |
| 2016-02-27 | `fix` | Fix NPE if icon name is missed in xml, ignore it | `IconBuilder.java` | [75baf8a9](https://github.com/freeplane/freeplane/commit/75baf8a9e13c2d7abe47fd0c0bee972a162b5dcf) |
| 2016-02-21 | `feature` | Add added action names to action entries | `EntryAccessor.java`, `EntryAccessorTest.java` | [b73e68d7](https://github.com/freeplane/freeplane/commit/b73e68d7a654ff82cdfeab5dde4f84b5b5d3057a) |
| 2016-02-19 | `fix` | Fix map move on changes of viewport size change | `MapViewScrollPane.java` | [4ed6e325](https://github.com/freeplane/freeplane/commit/4ed6e3252a310cd1a45b359d6f6aefabc82e3b60) |
| 2016-02-19 | `fix` | Fix NPE on map loading | `AutomaticEdgeColorHook.java`, `PersistentNodeHook.java` +2 | [616306f5](https://github.com/freeplane/freeplane/commit/616306f5874a335910dd986d6560bf3e3ead2d90) |
| 2016-02-14 | `fix` | Fix hidden node handling for summary node placement | `VerticalNodeViewLayoutStrategy.java` | [9f5c26c9](https://github.com/freeplane/freeplane/commit/9f5c26c9df4df8ff7b1f5e691b99a03983b48c60) |
| 2016-02-14 | `fix` | Fix \n separator in join nodes | `JoinNodesAction.java` | [14d5e83f](https://github.com/freeplane/freeplane/commit/14d5e83f92effcf3fa80142e149a30ae4b31ba33) |
| 2016-02-14 | `fix` | [bugs:#2320] Encrypted Map Undo Bug | `EncryptionController.java`, `EncryptionModel.java` +1 | [d6990ee3](https://github.com/freeplane/freeplane/commit/d6990ee30ede107198238b478b9a026171e5d838) |
| 2016-02-13 | `fix` | Fix attribute compare conditions for any attribute | `AttributeCompareCondition.java` | [99c2bd5c](https://github.com/freeplane/freeplane/commit/99c2bd5ce5c83cb82348365d34474b7ec66e0e05) |
| 2016-02-13 | `fix` | Fix language properties | `Resources_ar.properties`, `Resources_ca.properties` +30 | [25549679](https://github.com/freeplane/freeplane/commit/2554967910cc81075498c0277a7090ac06a88dc4) |
| 2016-02-07 | `fix` | Bug fix in node layout for summary nodes, | `VerticalNodeViewLayoutStrategy.java` | [d1c8fa0a](https://github.com/freeplane/freeplane/commit/d1c8fa0abe5070d21d18935f983d082b787708e1) |
| 2016-02-07 | `fix` | Fix non ascii character | `Resources_de.properties` | [be07b7e7](https://github.com/freeplane/freeplane/commit/be07b7e718758b3b9f9ad764455442ce6385db4b) |
| 2016-02-07 | `feature` | Change action name "New free node" to "New floating node" | `Resources_cs.properties`, `Resources_da.properties` +19 | [f4a20536](https://github.com/freeplane/freeplane/commit/f4a2053698f5d364e7c09e9f5c1831e4d7851b3b) |
| 2016-02-07 | `fix` | Fix initialization of AlwaysUnfoldedNode actions | `AlwaysUnfoldedNode.java`, `MMapController.java` +4 | [0e4c578b](https://github.com/freeplane/freeplane/commit/0e4c578b9154036b345a1f4837480ddffd9876b2) |
| 2016-02-06 | `fix` | Fix and log any exception in background image | `MapView.java` | [877b780d](https://github.com/freeplane/freeplane/commit/877b780d4b07d9139b8a1777ca3839a37666ff52) |
| 2016-02-06 | `fix` | Fix NPE | `ZoomableLabel.java` | [7e39bc35](https://github.com/freeplane/freeplane/commit/7e39bc351aba58265f93b3556f524ef82367404b) |
| 2016-02-05 | `fix` | Fix selection change on undo | `MapView.java` | [72eee60e](https://github.com/freeplane/freeplane/commit/72eee60eeae57193b059fa7f58feb1ec8489b0c6) |
| 2016-01-30 | `fix` | Fix BlinkingNodeHook for clones | `BlinkingNodeHook.java` | [bba8cb1d](https://github.com/freeplane/freeplane/commit/bba8cb1d1f43e1c990b12a321dbf2b2cb73c2c07) |
| 2016-01-30 | `fix` | Fix reminder icons for clones | `ReminderHook.java` | [a9566382](https://github.com/freeplane/freeplane/commit/a95663827c2857c0302d37b54e1d65a570245ad6) |
| 2016-01-30 | `fix` | Fix NPE | `ReminderExtension.java` | [dfdc8c9f](https://github.com/freeplane/freeplane/commit/dfdc8c9fdbfa3204cad54fe154179984d51d3758) |
| 2016-01-30 | `fix` | Fix class cast exception | `FreeplaneGUIStarter.java` | [e3ae6fdf](https://github.com/freeplane/freeplane/commit/e3ae6fdfa26fdc3d50c10367a0c7a26b7ef64a76) |
| 2016-01-30 | `feature` | Do not add not existing files to last opened list | `LastOpenedList.java` | [3a3098f3](https://github.com/freeplane/freeplane/commit/3a3098f3a60f739d7488b8bba5e6e8aeb0fc8d4c) |
| 2016-01-30 | `feature` | Fix new unsaved map title name | `MMapController.java`, `IMapViewManager.java` +8 | [2d1dbb6f](https://github.com/freeplane/freeplane/commit/2d1dbb6fd25791bf4d67d9c10e4ab8dfc8f467c4) |
| 2016-01-25 | `feature` | Add text() handling to import from and export to xml | `mm2xml.xsl`, `xml2mm.xsl` | [817b50de](https://github.com/freeplane/freeplane/commit/817b50ded10b4cb8790db33cdf59e0f72c52119e) |
| 2016-01-24 | `fix` | Fix NodeStyleBuilder | `NodeStyleBuilder.java` | [ef70d33c](https://github.com/freeplane/freeplane/commit/ef70d33c446e071a6703137693a696049a968535) |
| 2016-01-24 | `feature` | Add try-catch-blocks to xml reader | `TreeXmlReader.java` | [68de7c2d](https://github.com/freeplane/freeplane/commit/68de7c2d042ce1f5f55b0dac510b5920e28412ba) |
| 2016-01-23 | `feature` | new: TextUtils.copyHtmlToClipboard() | `history_en.txt`, `TextUtils.java` +2 | [cb3702e4](https://github.com/freeplane/freeplane/commit/cb3702e422da73f3b18448f6754c1e88bda4be05) |
| 2016-01-23 | `fix` | fix NPE | `IconRegistry.java` | [b0798d04](https://github.com/freeplane/freeplane/commit/b0798d0422480518444ec4d51ff5c48dfbf2c332) |
| 2016-01-23 | `fix` | Bug fixes for search and replace | `NodeList.java` | [3ae952e0](https://github.com/freeplane/freeplane/commit/3ae952e09b7385a90b947e7dbd4ae733c689ffc2) |
| 2016-01-23 | `fix` | Fix NPE | `MTextController.java` | [8d61f50a](https://github.com/freeplane/freeplane/commit/8d61f50ab2eac73bad9b16a11107a0d949d42ecd) |
| 2016-01-23 | `fix` | bug #2305 clicking in icon-area does not select node | `IconController.java`, `IconMouseListener.java` +2 | [ddb73bd9](https://github.com/freeplane/freeplane/commit/ddb73bd9db306cc5078b57a1ad783720db81a590) |
| 2016-01-23 | `fix` | fix imports | `SelectionController.java` | [d7057c0c](https://github.com/freeplane/freeplane/commit/d7057c0cbcab3404d5ec4ed2d13630bca1e958ce) |
| 2016-01-23 | `fix` | CssRuleBuilderShould UT: Fix font-family normalization on linux | `CssRuleBuilderShould.java` | [1b99f98a](https://github.com/freeplane/freeplane/commit/1b99f98a6c8e046f72fae5866bd19807f8714086) |
| 2016-01-23 | `feature` | Open new maps next to the currently selected map | `MapViewDockingWindows.java` | [7ea10e95](https://github.com/freeplane/freeplane/commit/7ea10e951752e965823c00bfba82e4faab894600) |
| 2016-01-23 | `fix` | Fix NPE | `MenuUtils.java` | [a32ce17d](https://github.com/freeplane/freeplane/commit/a32ce17d220c0dab462f80f066e61ab9619e0321) |
| 2016-01-23 | `fix` | Fix ArrayIndexOutOfBoundsException if no option was selected in notification dialog | `ReminderHook.java` | [98632b55](https://github.com/freeplane/freeplane/commit/98632b55777d4c520efc0816bff3b3994e35deda) |
| 2016-01-20 | `feature` | Add noActions menu items and fix node popup style menu | `mindmapmodemenu.xml`, `stylemodemenu.xml` +6 | [3566d397](https://github.com/freeplane/freeplane/commit/3566d397172cb6e461e0b517f61b93f282c4d735) |
| 2016-01-17 | `fix` | fix npe | `MapController.java`, `MapView.java` | [236fa833](https://github.com/freeplane/freeplane/commit/236fa833bae793cc06f3d169a88286c8e3e6a258) |
| 2016-01-17 | `fix` | Fix navigation to reminder from reminder popup | `UITools.java`, `MapController.java` +5 | [dac834a9](https://github.com/freeplane/freeplane/commit/dac834a925674bf3748ca953e962463ed4a2e1e0) |
| 2016-01-10 | `fix` | Fix deletion of connectors inside deleted subtrees | `NodeLinks.java`, `MLinkController.java` | [5b30c085](https://github.com/freeplane/freeplane/commit/5b30c08586ccdf10493993b5bfe73691db5b04cf) |
| 2016-01-09 | `fix` | fix java.util.ConcurrentModificationException | `PhaseProcessor.java` | [1086a69b](https://github.com/freeplane/freeplane/commit/1086a69b9affb516ab73b69a016d9c534aa5aa1c) |
| 2016-01-09 | `fix` | Output error message to fix bug in VerticalNodeViewLayoutStrategy | `VerticalNodeViewLayoutStrategy.java` | [232865b8](https://github.com/freeplane/freeplane/commit/232865b8ac7b84137509d23b2b9d4d7e046bcf0a) |
| 2016-01-09 | `feature` | Change writing connectors according to the new logic | `WriteManager.java`, `LinkBuilder.java` +4 | [58c21dd5](https://github.com/freeplane/freeplane/commit/58c21dd55d95e76a51e9d4a70943db4eb8411be0) |
| 2016-01-06 | `fix` | Fix insert node with invalid indices: insert as last | `MMapController.java` | [89b5a829](https://github.com/freeplane/freeplane/commit/89b5a829d1fc8653c214f70d1e0876d081c71393) |
| 2016-01-06 | `fix` | fix NPE | `MapScroller.java` | [dfc9d430](https://github.com/freeplane/freeplane/commit/dfc9d430d24f6e24273a4860df516549fa854abf) |
| 2016-01-06 | `fix` | bug #2290 Node attributes menu | `mindmapmodemenu.xml` | [1189ec75](https://github.com/freeplane/freeplane/commit/1189ec75d74a0f9bb25fa864a7733d5ce14d7c4d) |
| 2016-01-06 | `fix` | fix spelling | `Resources_hu.properties` | [2b85c3a6](https://github.com/freeplane/freeplane/commit/2b85c3a6284892dc6cac60435d06a25b5e96f666) |
| 2016-01-06 | `fix` | Fix spelling | `Resources_fr.properties`, `Resources_hr.properties` +6 | [99a1f43c](https://github.com/freeplane/freeplane/commit/99a1f43c95399f9dd45440e4d8e52d93d4b11c30) |
| 2016-01-05 | `fix` | fix NPE | `ActionAcceleratorManager.java` | [6c689699](https://github.com/freeplane/freeplane/commit/6c6896999a7fd2fc3cd1f65524437ac8a12171bb) |
| 2016-01-02 | `feature` | Add SetAcceleratorOnNextClickAction to style editor menu | `mindmapmodemenu.xml`, `stylemodemenu.xml` +1 | [3017ae7e](https://github.com/freeplane/freeplane/commit/3017ae7e74a1a0a9d73f60254b47945a50ae6c52) |
| 2016-01-02 | `fix` | Fix class cast exception in setting accelerator in style editor | `GrabKeyDialog.java` | [5aa08b3b](https://github.com/freeplane/freeplane/commit/5aa08b3bd5e0df6439af737081ee21687db7508d) |
| 2016-01-02 | `fix` | Fix accelerators for style editor | `ModeController.java`, `PersistentNodeHook.java` +3 | [25502a10](https://github.com/freeplane/freeplane/commit/25502a108eb288358946007da5f6c9053f6a1d31) |
| 2016-01-02 | `feature` | #2273 Indexfile add-on on Freeplane 1.5.4-alpha-01 | `LinkController.java` | [af07ae4a](https://github.com/freeplane/freeplane/commit/af07ae4af09c9b17bbe10d12c7f7f0f3f21edad0) |
| 2016-01-02 | `feature` | #2282 Script Auto Resize External Images in FP v. 1.5x | `BitmapViewerFactory.java` | [017285d6](https://github.com/freeplane/freeplane/commit/017285d66a46d054402478640ca190bf2c22b9c6) |
| 2016-01-01 | `fix` | Fix NPE | `AutomaticEdgeStyle.java` | [ad2e6109](https://github.com/freeplane/freeplane/commit/ad2e6109044890e339444e44c78810a7b9954504) |
| 2016-01-01 | `fix` | Fix updating of accelerators from old property format | `ActionAcceleratorManager.java` | [1d4f3bfb](https://github.com/freeplane/freeplane/commit/1d4f3bfb440a2b976b913fcf2cb9a5246c23916c) |

### Dettagli commit con note

**[c54e57da](https://github.com/freeplane/freeplane/commit/c54e57dadccffe0168f73feb5c6f58c4c45a8f95)** (2016-11-19) — Bug fix workaround for Knopflerfish bug

> "Knopflerfish fails to start if arbitraty working directory contains
> files with special names"
> https://github.com/knopflerfish/knopflerfish.org/issues/11

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

**[7d88585d](https://github.com/freeplane/freeplane/commit/7d88585dfd029e48fe3e62ee8f0aa89e1f0b6271)** (2016-04-10) — added init script facility

> Scripts in <freeplaneuserdir>/scripts/init are executed after application startup
> i.e. after initialization of the gui (including opening of last maps etc.)
> 
> New ApplicationLifecycleListener are registered in the Controller to be
> executed after startup.

**[d1c8fa0a](https://github.com/freeplane/freeplane/commit/d1c8fa0abe5070d21d18935f983d082b787708e1)** (2016-02-07) — Bug fix in node layout for summary nodes,

> https://youtu.be/19qaWD8B-3U

**[af07ae4a](https://github.com/freeplane/freeplane/commit/af07ae4af09c9b17bbe10d12c7f7f0f3f21edad0)** (2016-01-02) — #2273 Indexfile add-on on Freeplane 1.5.4-alpha-01

> The keys used for actions had been changed from 1.3 to 1.5.
> Changed the LinkController to understand 1.3 style keys too

**[017285d6](https://github.com/freeplane/freeplane/commit/017285d66a46d054402478640ca190bf2c22b9c6)** (2016-01-02) — #2282 Script Auto Resize External Images in FP v. 1.5x

> re-add method that had been extracted to ScalableComponent for
> backward compatibility. Deprecated it so fix your add-ons


---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-31 | `fix` | Fix latex and formula editors | `ConditionalContentTransformer.java`, `Activator.java` +1 | [3d92c063](https://github.com/freeplane/freeplane/commit/3d92c063dd0a69ff6ec6065577406d75f84f8e68) |
| 2015-12-31 | `fix` | Fix property key names in ActionAcceleratorManager | `ActionAcceleratorManager.java` | [d3fac3fd](https://github.com/freeplane/freeplane/commit/d3fac3fd0b062a40970027b51361ef9d1b6e721a) |
| 2015-12-31 | `fix` | [bugs:#2279] fix NPE | `MapView.java` | [01cc5546](https://github.com/freeplane/freeplane/commit/01cc554680402aad8ad41ee95f0b12a11b0a2e08) |
| 2015-12-31 | `fix` | Fix: do not select last visited node twice | `LastOpenedList.java` | [022b7eec](https://github.com/freeplane/freeplane/commit/022b7eec7aa3fb5619dc392a05e8c5bf049302df) |
| 2015-12-31 | `fix` | Fix for case icons have same names | `MIconController.java` | [5b1bb4d9](https://github.com/freeplane/freeplane/commit/5b1bb4d990cf710053f9746961cc2f239a8254c9) |
| 2015-12-31 | `feature` | Refactor FreeplaneActions and let Controller implement it | `ChildActionEntryRemover.java`, `AController.java` +3 | [58597866](https://github.com/freeplane/freeplane/commit/5859786656b65b51e0e2cbc86788247c02d56822) |
| 2015-12-31 | `fix` | Fix working with user defined accelerator sets | `ActionAcceleratorManager.java`, `LoadAcceleratorPresetsAction.java` | [1e4871b6](https://github.com/freeplane/freeplane/commit/1e4871b69c84b4338b529a73352371685866d765) |
| 2015-12-30 | `fix` | Bug fix in ExtensionCopier for icons | `MIconController.java` | [950e4c6c](https://github.com/freeplane/freeplane/commit/950e4c6c05421c4eeda3448b95efa2a182c37fc7) |
| 2015-12-30 | `fix` | Bug: maps lose focus when using ctrl-tab to navigate between maps | `MapViewDockingWindows.java` | [056e3421](https://github.com/freeplane/freeplane/commit/056e3421e44d3302a66e2492122cb7fd222807c5) |
| 2015-12-30 | `fix` | Bug fix for deletion of summary nodes | `SummaryNode.java`, `SummaryGroupEdgeListAdder.java` +1 | [6b82e8ab](https://github.com/freeplane/freeplane/commit/6b82e8ab30f35008597c6be539d96c507b3ace44) |
| 2015-12-30 | `fix` | fix NPE | `PersistentNodeHook.java` | [2f5fa666](https://github.com/freeplane/freeplane/commit/2f5fa6663ec096088759d802287a3971f3285316) |
| 2015-12-30 | `feature` | Copy format to new siblings | `history_en.txt`, `preferences.xml` +3 | [9172d05a](https://github.com/freeplane/freeplane/commit/9172d05a70cb504da5cc2cf74996009bd4906bbd) |
| 2015-12-29 | `fix` | Fix index for moved nodes also for inserts | `MMapController.java` | [4ab8f07a](https://github.com/freeplane/freeplane/commit/4ab8f07ac26566f46ca4ac4b1c8a3394046eca8a) |
| 2015-12-29 | `fix` | [bugs:#2271] fix loading and saving accelerator presets | `ActionAcceleratorManager.java`, `ChildActionEntryRemover.java` +4 | [58979ea6](https://github.com/freeplane/freeplane/commit/58979ea637bc0db747a2a8f3d7f0ca46df86c39f) |
| 2015-12-29 | `fix` | Fix NPE if zoom is set before viewer is completely created | `ExternalResource.java` | [e24a5ca1](https://github.com/freeplane/freeplane/commit/e24a5ca171287a6550fd7ea379ba22155aa077a1) |
| 2015-12-28 | `feature` | SummaryGroupEdgeListAdderShould not add group begin nodes and summary nodes twice | `SummaryGroupEdgeListAdder.java`, `SummaryGroupEdgeListAdderShould.java` | [d36054bd](https://github.com/freeplane/freeplane/commit/d36054bd726cfbf9a2962c48764f43eb8fe6dd15) |
| 2015-12-28 | `fix` | Fix SummaryLevels for group begin node | `SummaryLevels.java`, `SummaryLevelsShould.java` | [ad9b8a51](https://github.com/freeplane/freeplane/commit/ad9b8a51d28d529f4a84981f507f959719425ac3) |
| 2015-12-27 | `feature` | Generalize NodeModel clones : support two clone types in data model | `Cloner.java`, `Clones.java` +8 | [7cc551ee](https://github.com/freeplane/freeplane/commit/7cc551ee6f42afc8fb0527d7f9d7bc14ed0114c0) |
| 2015-12-24 | `fix` | Bug fix in moving nodes to the end position | `MMapController.java` | [cf56d9ee](https://github.com/freeplane/freeplane/commit/cf56d9ee3022fb0be2d335a98e65befae14de051) |
| 2015-12-24 | `fix` | Fix menu related translations | `Resources_ar.properties`, `Resources_ca.properties` +31 | [aaf1ad5e](https://github.com/freeplane/freeplane/commit/aaf1ad5e42a41e020f565fd26369c6735291f64b) |
| 2015-12-24 | `fix` | Fix user icons in menu and preferences | `KeyProperty.java`, `UserIcon.java` +2 | [8ecb1b79](https://github.com/freeplane/freeplane/commit/8ecb1b791bea8edeb2d160081697285c8aacd3c6) |
| 2015-12-23 | `fix` | Fix export to applet | `ExportWithXSLT.xml`, `exportmm2appletmm.xsl` +1 | [0800ce86](https://github.com/freeplane/freeplane/commit/0800ce864cd6a6a74ed1a8edf94183fb5a5dc56f) |
| 2015-12-23 | `feature` | Display add-on menu item locations | `build.gradle`, `EntryAccessor.java` +4 | [1abc7f18](https://github.com/freeplane/freeplane/commit/1abc7f18f501de5541aa2cb904d7429fbe68ea17) |
| 2015-12-23 | `feature` | Build formatted menu location for add-on details | `EntryAccessor.java`, `EntryAccessorTest.java` +1 | [a4f21706](https://github.com/freeplane/freeplane/commit/a4f217063d067d2c3afeb6cc0146beb748616444) |
| 2015-12-22 | `fix` | fix entry accessor test | `EntryAccessorTest.java` | [ed9a7747](https://github.com/freeplane/freeplane/commit/ed9a7747e12a1cbad2450b1ce0d84600b2f71ab2) |
| 2015-12-21 | `fix` | Fix bug in MapController.toggleFolded(Collection<NodeModel>) | `MapController.java` | [92cee0a9](https://github.com/freeplane/freeplane/commit/92cee0a9e8ad8558fceafa9e59d51fee1fb06d25) |
| 2015-12-21 | `fix` | Fix NPE | `SummaryNodeMapUpdater.java` | [2b8394ea](https://github.com/freeplane/freeplane/commit/2b8394eacc75f23b1e8f0babb4052d00c325d1da) |
| 2015-12-21 | `fix` | Fix SummaryNodeMapUpdater for high level summaries | `MMapController.java`, `SummaryNodeMapUpdater.java` | [596cfa7b](https://github.com/freeplane/freeplane/commit/596cfa7bef46af4e5515ce5d6b658472979f60c8) |
| 2015-12-19 | `feature` | Add new methods to SummaryLevels | `NodeModel.java`, `SummaryLevels.java` +1 | [0813ee7f](https://github.com/freeplane/freeplane/commit/0813ee7f371b60197f5283cf062add7542078e4d) |
| 2015-12-12 | `fix` | Fix division by zero | `NodeView.java` | [72240fc9](https://github.com/freeplane/freeplane/commit/72240fc9af183ddd2b0ce57eef0c7d083a69cee3) |
| 2015-12-12 | `fix` | Fix map view scrolling | `MapView.java` | [c4f3d618](https://github.com/freeplane/freeplane/commit/c4f3d61884d4821ecd8cc2956d3dd6319564ebc0) |
| 2015-12-09 | `fix` | Fix: destroy popup menus after the action was executed | `ActionSelectListener.java`, `EntryPopupListener.java` +6 | [761c6c57](https://github.com/freeplane/freeplane/commit/761c6c573631066a8860188ae2facf6eb00d437c) |
| 2015-12-06 | `fix` | fix compilation problems | `MenuUtils.java`, `HeadlessMapViewController.java` | [0a4abbbb](https://github.com/freeplane/freeplane/commit/0a4abbbb0bf74bff0fe4db201a89ae90b79b9731) |
| 2015-12-06 | `fix` | reintroduce getFrame() to fix a breaking change | `UITools.java` | [bd77cd42](https://github.com/freeplane/freeplane/commit/bd77cd4267578152c9a321229908df18a1526ccc) |
| 2015-12-06 | `fix` | Fix memory leaks | `JAutoCheckBoxMenuItem.java`, `JAutoRadioButtonMenuItem.java` +2 | [c88c28c1](https://github.com/freeplane/freeplane/commit/c88c28c1788c9c566aa5091055fb452d14034efd) |
| 2015-12-06 | `feature` | Add typed attributes to Entry | `AttributeAlreadySetException.java`, `Entry.java` +1 | [aa8d9a76](https://github.com/freeplane/freeplane/commit/aa8d9a7619a4dd5d81f92959f9c990fc95554055) |
| 2015-12-06 | `feature` | ViewController can create a list of all maps in their current order | `FrameController.java`, `ViewController.java` +2 | [5f1b735b](https://github.com/freeplane/freeplane/commit/5f1b735bdbc4edc8b6e69219f62a5db92ba06ef1) |
| 2015-12-06 | `fix` | Fix: Always close popup dialogs on Alt+Enter and Enter | `LinkController.java` | [17f94ad5](https://github.com/freeplane/freeplane/commit/17f94ad568bf7f3f79fabd33a88e2772cf881349) |
| 2015-12-05 | `fix` | Fix vertical positioning of zoomed labels | `ZoomableLabelUI.java` | [c1212c27](https://github.com/freeplane/freeplane/commit/c1212c279be27810586c37072f7daf6ef563efa3) |
| 2015-12-05 | `fix` | Fix look and feel property in options | `OptionPanel.java` | [557b7c05](https://github.com/freeplane/freeplane/commit/557b7c05fec912ff1873a4aa4b3c7bbb9e05cf11) |
| 2015-12-05 | `fix` | Fix text alignment for VariableInsetsMainView | `NarrowHexagonMainView.java`, `OvalMainView.java` +3 | [76c9171e](https://github.com/freeplane/freeplane/commit/76c9171e412f6a3d190a4eacad0331b26da5c5c9) |
| 2015-12-05 | `fix` | Fix node layout for summaries of summaries | `VerticalNodeViewLayoutStrategy.java` | [47f8926a](https://github.com/freeplane/freeplane/commit/47f8926ab0503488f6f616a1c9e39acfa102763d) |
| 2015-12-04 | `feature` | Allow new summary nodes if firstGroupNode was set in the middle | `MMapController.java`, `NewSummaryAction.java` +1 | [6a8e51f7](https://github.com/freeplane/freeplane/commit/6a8e51f7796a77f6da4dafa29ffb9f17bf154ba3) |
| 2015-12-04 | `fix` | fix MenuBuilderAcceptanceTest | `MenuBuilderAcceptanceTest.java` | [6c261401](https://github.com/freeplane/freeplane/commit/6c261401dab5c6c8fc472a1c99a7b5deed4a3bf4) |
| 2015-12-04 | `fix` | Fix execute menu item links | `LinkController.java` | [342d2767](https://github.com/freeplane/freeplane/commit/342d2767c3785a41f284f4c915aa97d88b15f2c5) |
| 2015-12-04 | `fix` | Fix item selection in MapPopup and NodePopup | `JMenuItemBuilder.java`, `MapPopupBuilder.java` +4 | [81f9062c](https://github.com/freeplane/freeplane/commit/81f9062ced4582dcf6e804aae39750bc8314aa5b) |
| 2015-12-03 | `fix` | Fix undo folding | `MMapController.java` | [deb82908](https://github.com/freeplane/freeplane/commit/deb82908efdb99322e4c5819e9c27917ada317ae) |
| 2015-12-03 | `fix` | Fix menu structure | `mindmapmodemenu.xml` | [1c1c590d](https://github.com/freeplane/freeplane/commit/1c1c590d8acbbc13c5984faff62f6f6f135f2f0f) |
| 2015-12-02 | `feature` | Add missed actions | `mindmapmodemenu.xml` | [89ae2ee4](https://github.com/freeplane/freeplane/commit/89ae2ee44a1e7254114613edfdb5cf91b4a4853b) |
| 2015-12-02 | `fix` | Fix resource file name for applet menu | `FreeplaneApplet.java` | [63c96662](https://github.com/freeplane/freeplane/commit/63c96662d44c490c0aca8c3e5a52968d902f1fde) |
| 2015-12-02 | `fix` | Fix MenuBuilderAcceptanceTest | `MenuBuilderAcceptanceTest.java` | [5d5972ab](https://github.com/freeplane/freeplane/commit/5d5972ab499aece3c19b8cd7b5ebec1de9c5f062) |
| 2015-12-02 | `fix` | fix style mode menu xml | `stylemodemenu.xml` | [339bedbe](https://github.com/freeplane/freeplane/commit/339bedbe7239370a06ff236171f1577de1b0f330) |
| 2015-12-02 | `fix` | fix filemode menu xml | `filemodemenu.xml` | [01a3b9d0](https://github.com/freeplane/freeplane/commit/01a3b9d08d0120467998f13db82c017151eae711) |
| 2015-12-02 | `fix` | Fix browswemode menus | `browsemodemenu.xml`, `appletmenu.xml` | [b11e8d37](https://github.com/freeplane/freeplane/commit/b11e8d37fc02aa9cafe6f60bae3cb680186e6c6e) |
| 2015-12-02 | `fix` | Fix english translation | `browsemodemenu.xml`, `filemodemenu.xml` +3 | [a92407e6](https://github.com/freeplane/freeplane/commit/a92407e6c768d0060594515def3a067ecfeb9677) |
| 2015-12-01 | `fix` | fix mindmapmodemenu.xml | `mindmapmodemenu.xml` | [198f9048](https://github.com/freeplane/freeplane/commit/198f9048a98338a740120b4049c810402a90fae0) |
| 2015-12-01 | `fix` | Fix MenuBuilderAcceptanceTest running with HeadlessUIController | `FrameController.java`, `HeadlessUIController.java` | [bdbb7acb](https://github.com/freeplane/freeplane/commit/bdbb7acb46286bd0aaf41764bb78ea8b5f1b1ca8) |
| 2015-11-30 | `fix` | Fix maxNodeWidth : use double value consistently | `MNodeStyleController.java`, `ZoomableLabel.java` +1 | [560e3c03](https://github.com/freeplane/freeplane/commit/560e3c0338d6e1e2ab777dbaa73583dbe0626b34) |
| 2015-11-30 | `fix` | Fix maxNodeWidth : use double value consistently | `MNodeStyleController.java`, `ZoomableLabel.java` +1 | [91eb9db0](https://github.com/freeplane/freeplane/commit/91eb9db0270b8a7a57263ae1db585dd59370ef23) |
| 2015-11-30 | `fix` | fix bug #2256 Clickable map export does not function properly | `ExportWithXSLT.java`, `ClickableImageCreator.java` +1 | [afc2c5a9](https://github.com/freeplane/freeplane/commit/afc2c5a944d63b6135313ca2496d5a2e49608f69) |
| 2015-11-30 | `fix` | fix bug #2256 Clickable map export does not function properly | `ExportWithXSLT.java`, `ClickableImageCreator.java` +1 | [f91a61ed](https://github.com/freeplane/freeplane/commit/f91a61edbe23c41efed4433bc932591706462dc7) |
| 2015-11-29 | `fix` | Fix scrolling of invisible maps | `MapView.java` | [86ae31a6](https://github.com/freeplane/freeplane/commit/86ae31a64714114576cf063f5c809b944cd4d69b) |
| 2015-11-29 | `fix` | Fix scrolling of invisible maps | `MapView.java` | [21a2c1ff](https://github.com/freeplane/freeplane/commit/21a2c1ffdaa51d2d0c8e7b04523cd184f5830167) |
| 2015-11-29 | `feature` | ensure that for each script exactly one menu entry is shown | `mindmapmode.generic.xml`, `ExecuteScriptAction.java` +3 | [0d61af06](https://github.com/freeplane/freeplane/commit/0d61af06534d34c7a5f840b529bc7fa85297be57) |
| 2015-11-29 | `api_change` | Delete unused interface with only one implementation class | `PhaseProcessor.java`, `Processor.java` +3 | [a000f382](https://github.com/freeplane/freeplane/commit/a000f38230d8f4126079453e6b9745c548e40be3) |
| 2015-11-29 | `fix` | Fix hidden details preferred size for zoomed maps | `NodeViewFactory.java` | [b59e2f7a](https://github.com/freeplane/freeplane/commit/b59e2f7adc37aeeb78e0d21d6f7337e1a57aa4f1) |
| 2015-11-29 | `fix` | Fix hidden details preferred size for zoomed maps | `NodeViewFactory.java` | [417a2234](https://github.com/freeplane/freeplane/commit/417a2234239f9f06e4d388c0f8adfa01e0b0efe3) |
| 2015-11-28 | `feature` | Bug fix: add vgap attribute handler for stylenodes | `LocationBuilder.java` | [408151fa](https://github.com/freeplane/freeplane/commit/408151fad61077180e8ea6c40b3ab611d812f526) |
| 2015-11-28 | `feature` | Bug fix: add vgap attribute handler for stylenodes | `LocationBuilder.java` | [a0d4e738](https://github.com/freeplane/freeplane/commit/a0d4e738526d80f627dace040d4a7b64c84d6092) |
| 2015-11-28 | `fix` | Fix: Do not delete summary node parent inside undo action | `SummaryNode.java` | [7ba65625](https://github.com/freeplane/freeplane/commit/7ba6562553e41cace9a4404830e46892962f3a27) |
| 2015-11-28 | `fix` | Fix: Do not delete summary node parent inside undo action | `SummaryNode.java` | [330e8221](https://github.com/freeplane/freeplane/commit/330e8221a08fbd511ea9ff26a774eb8ca6c69867) |
| 2015-11-28 | `fix` | Fix narrow hexagon lower point | `NarrowHexagonMainView.java` | [c72c76c2](https://github.com/freeplane/freeplane/commit/c72c76c22b4c7d7f86739edf47790f2d1e01f379) |
| 2015-11-28 | `fix` | Fix narrow hexagon lower point | `NarrowHexagonMainView.java` | [1a34b7ba](https://github.com/freeplane/freeplane/commit/1a34b7bae25625c3771bfe5558347834b9507b57) |
| 2015-11-28 | `fix` | Bug fix in saving details with localized html | `NodeTextBuilder.java` | [19e5abd7](https://github.com/freeplane/freeplane/commit/19e5abd715169284689d4a0dbc3b3eb096e9e3be) |
| 2015-11-28 | `fix` | Bug fix in saving details with localized html | `NodeTextBuilder.java` | [ef95c892](https://github.com/freeplane/freeplane/commit/ef95c892e1b6986aeabcf9a571c5f7afc0782dbe) |
| 2015-11-28 | `fix` | Fix endless loop due to integer arithmetics in label layout | `ZoomableLabelUI.java` | [00b0cddc](https://github.com/freeplane/freeplane/commit/00b0cddcbf2c10c7bb37fc57471dbda175a03e55) |
| 2015-11-28 | `fix` | Fix endless loop due to integer arithmetics in label layout | `ZoomableLabelUI.java` | [faefb733](https://github.com/freeplane/freeplane/commit/faefb733a647b213a165fbf597a60697f999c082) |
| 2015-11-28 | `fix` | Fix text positioning for nodes with sizes smaller than needed | `BubbleMainView.java`, `RectangleMainView.java` +1 | [a9f0eb4f](https://github.com/freeplane/freeplane/commit/a9f0eb4f12d9a44d9d83da93e1a556c70e1058cf) |
| 2015-11-28 | `fix` | Fix text positioning for nodes with sizes smaller than needed | `BubbleMainView.java`, `RectangleMainView.java` +1 | [5856f769](https://github.com/freeplane/freeplane/commit/5856f769f27ef4cbfcf4a45588881dd32123b849) |
| 2015-11-28 | `fix` | Fix shape configuration NPE | `NodeStyleModel.java` | [b29ed90c](https://github.com/freeplane/freeplane/commit/b29ed90c11127b6eb2a81b30af756199102f3c6b) |
| 2015-11-28 | `fix` | Fix shape configuration NPE | `NodeStyleModel.java` | [99a90893](https://github.com/freeplane/freeplane/commit/99a90893afd7a037476b3f30fc553f581c4a5b63) |
| 2015-11-27 | `feature` | Add shape configuration properties to style editor panel # Conflicts: #	freeplane/src/main | `NodeStyleBuilder.java`, `NodeStyleController.java` +4 | [5d76d19f](https://github.com/freeplane/freeplane/commit/5d76d19fe5dd56b757b9eec9828f3323b9e0f5fe) |
| 2015-11-27 | `feature` | Add shape configuration properties to style editor panel | `NodeStyleBuilder.java`, `NodeStyleController.java` +4 | [9f1f467e](https://github.com/freeplane/freeplane/commit/9f1f467ea0548c0faa02a539af39480bc9b9f0a3) |
| 2015-11-26 | `fix` | Fix attribute editor formatting | `AttributeTable.java` | [66d25ca8](https://github.com/freeplane/freeplane/commit/66d25ca8ee534c44cebdc79b35f9296266c7ac20) |
| 2015-11-26 | `fix` | Fix attribute editor formatting | `AttributeTable.java` | [e4d60dc3](https://github.com/freeplane/freeplane/commit/e4d60dc3216c6f3d36e8912daf4b9970140c416a) |
| 2015-11-24 | `fix` | Fix zoomed max width | `ZoomableLabelUI.java` | [4779e1de](https://github.com/freeplane/freeplane/commit/4779e1dec057d0447755bf96daf7a2c93894c729) |
| 2015-11-24 | `fix` | Fix zoomed max width | `ZoomableLabelUI.java` | [8f21a73a](https://github.com/freeplane/freeplane/commit/8f21a73aaaa74cae36fb420d30a8df3ebab9799c) |
| 2015-11-24 | `fix` | Fix bug in NodeView.getChildDistanceContainer | `NodeView.java` | [a2a3af1a](https://github.com/freeplane/freeplane/commit/a2a3af1a9c7cbe7164ccfcb474370d35db0968ba) |
| 2015-11-24 | `fix` | Fix bug in NodeView.getChildDistanceContainer | `NodeView.java` | [bf11708e](https://github.com/freeplane/freeplane/commit/bf11708ec5e4c068c19d50d234441a3829cc6dd5) |
| 2015-11-22 | `fix` | Fix style root format for old maps | `MapStyleModel.java` | [3cb93b6e](https://github.com/freeplane/freeplane/commit/3cb93b6e6e5fefb3908baf36c6458e21f6f3da37) |
| 2015-11-22 | `fix` | Fix style root format for old maps | `MapStyleModel.java` | [dd1930be](https://github.com/freeplane/freeplane/commit/dd1930be66c5ae0c1a58a7c0fe29af9e28ae200a) |
| 2015-11-22 | `fix` | Fix text properties and maps: replace big oval by oval and remove small oval # Conflicts:  | `conceptMap.mm`, `essay.mm` +6 | [55e334ac](https://github.com/freeplane/freeplane/commit/55e334acec23508569eb9d036434d107578bec59) |
| 2015-11-22 | `fix` | Fix text properties and maps: replace big oval by oval and remove small oval | `conceptMap.mm`, `essay.mm` +9 | [bf97785d](https://github.com/freeplane/freeplane/commit/bf97785de5fbcb56593e4b355afd6e38cf39cea1) |
| 2015-11-22 | `fix` | Fix oval shape insets calculation # Conflicts: #	freeplane/src/main/java/org/freeplane/vie | `NodeStyleModel.java`, `BigOvalMainView.java` +5 | [ae36ea45](https://github.com/freeplane/freeplane/commit/ae36ea4584cc00e508f9360cd92886c010c50eb4) |
| 2015-11-22 | `fix` | Fix oval shape insets calculation | `NodeStyleModel.java`, `BigOvalMainView.java` +4 | [b6184bda](https://github.com/freeplane/freeplane/commit/b6184bdacc4ad39db24f05e45457e155f5debee4) |
| 2015-11-21 | `fix` | fix errorneous placeholders usage warning on format-translation | `Resources_nb.properties` | [c62957ea](https://github.com/freeplane/freeplane/commit/c62957ea78df4a19a31dfcd1a5e86988fd13ab15) |
| 2015-11-21 | `fix` | Fix oval/circle node shape color | `BubbleMainView.java`, `MainView.java` +2 | [03ef0163](https://github.com/freeplane/freeplane/commit/03ef016300b49475ed2abe7ecc49718cbc0e7188) |
| 2015-11-21 | `fix` | Fix oval/circle node shape color | `BubbleMainView.java`, `MainView.java` +2 | [a9cc4054](https://github.com/freeplane/freeplane/commit/a9cc405401b007394aadc4f152fb61e08369c16c) |
| 2015-11-20 | `fix` | Fix small bubble problems | `BigMap.mm`, `BigBubbleMainView.java` +5 | [22b181cd](https://github.com/freeplane/freeplane/commit/22b181cdc0f627e8fd89c2b6d3c54e9f154567c2) |
| 2015-11-20 | `fix` | Fix small bubble problems | `BigMap.mm`, `BigBubbleMainView.java` +5 | [75bc400c](https://github.com/freeplane/freeplane/commit/75bc400cf7dcb56091ca0fac59ac529f9f800db6) |
| 2015-11-20 | `feature` | Add new node shapes # Conflicts: #	freeplane/src/main/java/org/freeplane/view/swing/map/Hi | `NodeStyleModel.java`, `MNodeStyleController.java` +8 | [116af7bd](https://github.com/freeplane/freeplane/commit/116af7bda2f2e40241fae307657e0c9177d924c9) |
| 2015-11-20 | `feature` | Add new node shapes | `NodeStyleModel.java`, `MNodeStyleController.java` +8 | [37bc2bf1](https://github.com/freeplane/freeplane/commit/37bc2bf1059055c3b0e6ee10fe797f05e245e5fc) |
| 2015-11-19 | `fix` | Fix NPE bug hash 341f63a261993d67d0fbccb6b9e5ae1e | `NodeView.java` | [30230897](https://github.com/freeplane/freeplane/commit/302308972a010811dcb0bfe4e5c8455a924614cc) |
| 2015-11-19 | `fix` | Fix NPE bug hash 341f63a261993d67d0fbccb6b9e5ae1e | `NodeView.java`, `NodeViewLayoutAdapter.java` | [31608aa7](https://github.com/freeplane/freeplane/commit/31608aa767b5dc3588936540bc9c1d859f7dc0cb) |
| 2015-11-19 | `feature` | Don't create user standard template for now | `FreeplaneGUIStarter.java` | [ee1d6e08](https://github.com/freeplane/freeplane/commit/ee1d6e085b7329caf0ea36c6313432779aedd55d) |
| 2015-11-19 | `feature` | Create user standard template file | `MFileManager.java`, `FreeplaneGUIStarter.java` +1 | [0f344df2](https://github.com/freeplane/freeplane/commit/0f344df205fe6b313d16cb5388456b847e335850) |
| 2015-11-19 | `fix` | Fix createUserStandardTemplate in UserProperiesUpdater | `MFileManager.java`, `FreeplaneGUIStarter.java` +1 | [cbef5126](https://github.com/freeplane/freeplane/commit/cbef5126d42654b4b18eee8050e4a79a18ea9478) |
| 2015-11-19 | `feature` | Add style background info # Conflicts: #	freeplane/external-resources/templates/BigMap.mm | `BigMap.mm`, `JonasBatista.jpg` | [54b1f3a6](https://github.com/freeplane/freeplane/commit/54b1f3a697498240ef79df394c97354204b249da) |
| 2015-11-19 | `feature` | Add style background info | `BigMap.mm`, `JonasBatista.jpg` | [d1ddcc73](https://github.com/freeplane/freeplane/commit/d1ddcc7366cab7e4c5132f8a97904f797e44668a) |
| 2015-11-19 | `feature` | Add minimized node to style node attribute handlers | `NodeTextBuilder.java` | [41de1075](https://github.com/freeplane/freeplane/commit/41de107592ecd75e5e0f2bd8508f82af1ed58612) |
| 2015-11-19 | `feature` | Add minimized node to style node attribute handlers | `NodeTextBuilder.java` | [575605fe](https://github.com/freeplane/freeplane/commit/575605fe40b259bf0a224aed2b7d067051835dcd) |
| 2015-11-19 | `feature` | Add mouse listeners only to nodes that can be edited, style map nodes with levels 0 and 1  | `ModeController.java`, `SModeController.java` +1 | [7ec28be4](https://github.com/freeplane/freeplane/commit/7ec28be45aed0acae11e26cc3fb00f2444ea360e) |
| 2015-11-19 | `feature` | Add mouse listeners only to nodes that can be edited, style map nodes with levels 0 and 1  | `ModeController.java`, `SModeController.java` +1 | [65961281](https://github.com/freeplane/freeplane/commit/65961281133aa07f93d5c0084e9594d46c0b5513) |
| 2015-11-18 | `fix` | Fix CssRuleBuilder tests | `CssRuleBuilderShould.java` | [d3e1dff7](https://github.com/freeplane/freeplane/commit/d3e1dff7fb9ad60bcc82886c6b23f846efc3882a) |
| 2015-11-18 | `fix` | Fix node tool tip preferred size calculation | `NodeTooltip.java` | [19e4d019](https://github.com/freeplane/freeplane/commit/19e4d01906ad495d6cdf50c29a173a35f66013d8) |
| 2015-11-18 | `fix` | Fix node tool tip preferred size calculation | `NodeTooltip.java` | [97e125b2](https://github.com/freeplane/freeplane/commit/97e125b236389210c21537dd81fb2ce0c6fa95f0) |
| 2015-11-18 | `fix` | Do not use revalidate, undo fix for ticket 817: it can cause endless event sequence | `NodeTooltip.java` | [5b076d97](https://github.com/freeplane/freeplane/commit/5b076d9783c79eae266ece2b77c82d6ead435a4f) |
| 2015-11-18 | `fix` | Do not use revalidate, undo fix for ticket 817: it can cause endless event sequence | `NodeTooltip.java` | [2b638c1a](https://github.com/freeplane/freeplane/commit/2b638c1a20f7ace0988d6cb0e0d32ff45df8ac7c) |
| 2015-11-15 | `feature` | add scripting to the node context menu | `mindmapmode.generic.xml` | [ecd8034c](https://github.com/freeplane/freeplane/commit/ecd8034c1cc8770bf2326aa024adf879d2ad25fb) |
| 2015-11-15 | `fix` | fix language code translations for pt_BR | `Resources_pt_BR.properties` | [dc97cd3d](https://github.com/freeplane/freeplane/commit/dc97cd3d5c2de258af7e3838bc82c1a346b8e807) |
| 2015-11-15 | `fix` | Fix accelerators | `mindmapmodemenu.mm` | [c1ef796a](https://github.com/freeplane/freeplane/commit/c1ef796a2bf7d2f27c5727780c6b64160c6e5c02) |
| 2015-11-15 | `fix` | Bug fix : save MinimalDistanceBetweenChildren only on visible nodes | `MNodeMotionListener.java` | [c4cecac9](https://github.com/freeplane/freeplane/commit/c4cecac9c2404e9465597190b45273666cd5e137) |
| 2015-11-15 | `fix` | Bug fix : save MinimalDistanceBetweenChildren only on visible nodes | `MNodeMotionListener.java` | [d2e8a404](https://github.com/freeplane/freeplane/commit/d2e8a404e101916df30063715aa7616deced9cb5) |
| 2015-11-14 | `feature` | add icons for execution mode toggle menu entries | `on_selected_node_recursively_small.png`, `on_selected_node_small.png` +2 | [22ceb495](https://github.com/freeplane/freeplane/commit/22ceb495e18533a220cbba6d46a4476316c62d64) |
| 2015-11-13 | `fix` | rename method, fix test for CssRuleBuilder | `CssRuleBuilder.java`, `TextController.java` +1 | [dc344809](https://github.com/freeplane/freeplane/commit/dc34480924e03e7102df4afa8b6e02e1e3b1c80c) |
| 2015-11-13 | `fix` | Fix tooltip widths and fonts | `CssRuleBuilder.java`, `TextController.java` | [ee9e6bc4](https://github.com/freeplane/freeplane/commit/ee9e6bc49ef73167f02750ee43a340357d735929) |
| 2015-11-13 | `fix` | Fix tooltip widths and fonts | `CssRuleBuilder.java`, `TextController.java` | [bd47312d](https://github.com/freeplane/freeplane/commit/bd47312dbdeda1cdb64bfe5eaaccd32be08ab446) |
| 2015-11-10 | `fix` | fix NPE | `AutomaticLayoutController.java` | [6ee70f36](https://github.com/freeplane/freeplane/commit/6ee70f3662f1cf1be2de2fd3ee711d2ed9e1c576) |
| 2015-11-10 | `fix` | fix NPE | `AutomaticLayoutController.java` | [0f58d52c](https://github.com/freeplane/freeplane/commit/0f58d52ccb5142d73502cf4867e11a1d12e4bfbb) |
| 2015-11-10 | `fix` | Fix stylemode menu toolbar | `stylemodemenu.mm` | [c7b19ee8](https://github.com/freeplane/freeplane/commit/c7b19ee89503dd8e34b7f4c035b96fc87fdf4de1) |
| 2015-11-08 | `feature` | Script Actions Builder for new UI | `mindmapmode.generic.xml`, `ExecutionModeSelector.java` +2 | [91b92cfb](https://github.com/freeplane/freeplane/commit/91b92cfb4e3d5ade5a140a49305aba09b62cd0c5) |
| 2015-11-08 | `fix` | Fix isFoldingPersistent condition | `MMapController.java` | [f4e53662](https://github.com/freeplane/freeplane/commit/f4e536621811aafb0d70558483f019ecfeeec89a) |
| 2015-11-08 | `fix` | Fix isFoldingPersistent condition | `MMapController.java` | [595518d4](https://github.com/freeplane/freeplane/commit/595518d41fdf54c7bdb862ccb84707b008d194e7) |
| 2015-11-08 | `feature` | Create summary child node automatically | `MMapController.java` | [95fd7f1f](https://github.com/freeplane/freeplane/commit/95fd7f1f6efa5f238bb46ef89b54f0e662e5b415) |
| 2015-11-08 | `feature` | Create summary child node automatically | `MMapController.java` | [438a2a7b](https://github.com/freeplane/freeplane/commit/438a2a7bbc0d86cc9cae5ed29cc433b3bef8290d) |
| 2015-11-03 | `fix` | fix columns.mm | `columns.mm`, `MFileManager.java` | [1c2bb632](https://github.com/freeplane/freeplane/commit/1c2bb632fe16eac94f4cf117a530b4e42d3f5329) |
| 2015-11-03 | `fix` | fix columns.mm | `columns.mm`, `MFileManager.java` | [2ffedd60](https://github.com/freeplane/freeplane/commit/2ffedd606fdb362b29866851a30de0c421bb8251) |
| 2015-11-02 | `fix` | Fix ConditionalContentTransformer for 1.5.x | `ConditionalContentTransformer.java` | [70b950c6](https://github.com/freeplane/freeplane/commit/70b950c6da4b2d00af106286dbe159a5fa7ca667) |
| 2015-11-02 | `fix` | fix zoomed insets in EditTextField # Conflicts: #	freeplane/src/main/java/org/freeplane/vi | `RootMainView.java`, `ZoomableLabel.java` +1 | [bde71bb1](https://github.com/freeplane/freeplane/commit/bde71bb1c66f08ddf8d9e7ce4eaae57c30fb780d) |
| 2015-11-02 | `fix` | fix zoomed insets in EditTextField | `RootMainView.java`, `ZoomableLabel.java` +1 | [39bd5f39](https://github.com/freeplane/freeplane/commit/39bd5f394d23a1c35045df991569bbd99bcbb4d2) |
| 2015-11-02 | `fix` | Fix node minimum width when zoom is active | `ZoomableLabelUI.java` | [83ab5a43](https://github.com/freeplane/freeplane/commit/83ab5a430033b636155d743f34be7467ba188d1a) |
| 2015-11-02 | `fix` | Fix node minimum width when zoom is active | `ZoomableLabelUI.java` | [fc2287f3](https://github.com/freeplane/freeplane/commit/fc2287f399c4047fc7f85c5a9183f1c153e24552) |
| 2015-11-01 | `fix` | Fix link popup position on screen | `DefaultMapMouseListener.java` | [ba4a3714](https://github.com/freeplane/freeplane/commit/ba4a37143d097fdebf67ca449472f4066430e739) |
| 2015-11-01 | `fix` | Fix link popup position on screen | `DefaultMapMouseListener.java` | [b6ba17a6](https://github.com/freeplane/freeplane/commit/b6ba17a6bbc07de4d6840ce41f6c92ccb04e71d2) |
| 2015-11-01 | `feature` | Add additional width of 40 pt to root node preferred size # Conflicts: #	freeplane/src/mai | `RootMainView.java` | [f98a5674](https://github.com/freeplane/freeplane/commit/f98a5674b6e1ebb1b2a614bf6a98b29115de71ef) |
| 2015-11-01 | `feature` | Add additional width of 40 pt to root node preferred size | `RootMainView.java` | [88dea472](https://github.com/freeplane/freeplane/commit/88dea472ae8c9a9bee7c9b78380b774f28d133a7) |
| 2015-11-01 | `fix` | Fix update of branch edge colors | `EdgeController.java`, `NodeView.java` | [6b2840e8](https://github.com/freeplane/freeplane/commit/6b2840e804b7af18266295fdba882c8f24d7a222) |
| 2015-11-01 | `fix` | Fix update of branch edge colors | `EdgeController.java`, `NodeView.java` | [096a5d1a](https://github.com/freeplane/freeplane/commit/096a5d1a8e4150e53f327f717d2783dcb6de3054) |
| 2015-11-01 | `feature` | Add method getStyleNode to AutomaticLayoutController | `AutomaticLayoutController.java` | [c9484718](https://github.com/freeplane/freeplane/commit/c94847188a19570ab6fe056b610ad0deea60d5ed) |
| 2015-11-01 | `feature` | Add method getStyleNode to AutomaticLayoutController | `AutomaticLayoutController.java` | [22a5d945](https://github.com/freeplane/freeplane/commit/22a5d9459fa982853c4ae387b058eac55383e3ed) |
| 2015-11-01 | `fix` | Bug fixes in EdgeController | `EdgeController.java`, `AutomaticLayoutController.java` | [57f6c91d](https://github.com/freeplane/freeplane/commit/57f6c91db110291a5b759e6356c23acd2a508fb9) |
| 2015-11-01 | `fix` | Bug fixes in EdgeController | `EdgeController.java`, `AutomaticLayoutController.java` | [cc055e33](https://github.com/freeplane/freeplane/commit/cc055e331fd31294b98e51411f730ee9413fc6a1) |
| 2015-11-01 | `fix` | Bug fix StyleEditorPanel | `StyleEditorPanel.java` | [b4df5204](https://github.com/freeplane/freeplane/commit/b4df52046763cfa8e93f03687cf7a482a527beeb) |
| 2015-11-01 | `fix` | Bug fix StyleEditorPanel | `StyleEditorPanel.java` | [c00d3563](https://github.com/freeplane/freeplane/commit/c00d35633f389416b4f0e307b0bd1088c343834a) |
| 2015-11-01 | `fix` | Fix configuration of automaticalyl set colors | `AutomaticEdgeColorHook.java`, `freeplane.properties` | [a9bc6cd8](https://github.com/freeplane/freeplane/commit/a9bc6cd870515ddb8426ef17138bf47e175b0063) |
| 2015-10-30 | `fix` | Fix file names with special characters in export to applet | `ExportWithXSLT.java` | [09edcae9](https://github.com/freeplane/freeplane/commit/09edcae9fe6a0ff0165bb021f5336db6d52c5047) |
| 2015-10-30 | `fix` | Fix file names with special characters in export to applet | `ExportWithXSLT.java` | [29b7a036](https://github.com/freeplane/freeplane/commit/29b7a036ab1fc135efc1a164df9ea2678905fd24) |
| 2015-10-29 | `fix` | Fix currentMapView bug | `EditStylesAction.java` | [9788e02e](https://github.com/freeplane/freeplane/commit/9788e02eef0e7d4af2384ac03223af083c2090c8) |
| 2015-10-29 | `fix` | Fix currentMapView bug | `EditStylesAction.java` | [f9568b25](https://github.com/freeplane/freeplane/commit/f9568b2566ba824ec5f31dcd997747128e7d61bf) |
| 2015-10-29 | `fix` | Fix Jav 5 issues | `ConstantObject.java`, `RuleReference.java` +3 | [5775ce62](https://github.com/freeplane/freeplane/commit/5775ce62b60389b9f796f897476f8841d81441e2) |
| 2015-10-29 | `fix` | Fix compile errors | `ConstantObject.java`, `RuleReference.java` +2 | [af810911](https://github.com/freeplane/freeplane/commit/af81091125d95ed81797e9bad5df9b4512e354d9) |
| 2015-10-29 | `fix` | Fix caching of edge color in node view # Conflicts: #	freeplane/src/org/freeplane/features | `RuleReference.java`, `EdgeController.java` +2 | [d4908c75](https://github.com/freeplane/freeplane/commit/d4908c75cf936c4e82671ba97505e02ab972305d) |
| 2015-10-29 | `fix` | Fix caching of edge color in node view | `EdgeController.java`, `MEdgeController.java` +2 | [6f122d7f](https://github.com/freeplane/freeplane/commit/6f122d7f9e39447474ae3b6dab34542f198be5b7) |
| 2015-10-28 | `fix` | Fix AutomaticLayout boolean flags | `AutomaticLayout.java` | [140d9c44](https://github.com/freeplane/freeplane/commit/140d9c44a69b83179af638049d976a4a9a4fd8bd) |
| 2015-10-28 | `fix` | Fix AutomaticLayout boolean flags | `AutomaticLayout.java` | [6f73d50a](https://github.com/freeplane/freeplane/commit/6f73d50a30c3ddb4597db37b242501dab9734d67) |
| 2015-10-28 | `fix` | Bug fixes and refactoring for column based edge color # Conflicts: #	freeplane/src/org/fre | `EdgeController.java`, `StyleEditorPanel.java` | [3c56e6a8](https://github.com/freeplane/freeplane/commit/3c56e6a8f114b2359647fd6942551c2dd04c3843) |
| 2015-10-28 | `fix` | Bug fixes and refactoring for column based edge color | `EdgeController.java`, `AutomaticLayoutController.java` +1 | [42431372](https://github.com/freeplane/freeplane/commit/4243137283b23d2e022571079d078e9c953b0474) |
| 2015-10-27 | `feature` | Add public method to AutomaticLayoutController | `AutomaticLayoutController.java` | [c9e8721d](https://github.com/freeplane/freeplane/commit/c9e8721d5a0a1c1a591388b270be0cd438f4b037) |
| 2015-10-27 | `feature` | Add public method to AutomaticLayoutController | `AutomaticLayoutController.java` | [e507224a](https://github.com/freeplane/freeplane/commit/e507224aca19d03effb99ad7dc3d536dc1089890) |
| 2015-10-27 | `fix` | Fix layout: summary node content height should not change positioning of non summary nodes | `VerticalNodeViewLayoutStrategy.java` | [62e807a9](https://github.com/freeplane/freeplane/commit/62e807a93a687142be03f75b3c769755a62ea86c) |
| 2015-10-25 | `fix` | Bug fix: increase font box size | `MUIFactory.java` | [62ca77fb](https://github.com/freeplane/freeplane/commit/62ca77fb6276ac796615d0508c5efb7d4f668e09) |
| 2015-10-25 | `feature` | Add width to tooltip style # Conflicts: #	freeplane/src/test/java/org/freeplane/core/ui/co | `CssRuleBuilder.java`, `TextController.java` | [a31dcdfa](https://github.com/freeplane/freeplane/commit/a31dcdfa8e75aa9e85c91474b24affbd18fcc37b) |
| 2015-10-25 | `feature` | Add width to tooltip style | `CssRuleBuilder.java`, `TextController.java` +1 | [0c2ffc98](https://github.com/freeplane/freeplane/commit/0c2ffc9826fe335f2b8ee598fdc9fc03ff18169a) |
| 2015-10-25 | `feature` | Add group node settings to menu | `mindmapmode.generic.xml` | [9d42b9b8](https://github.com/freeplane/freeplane/commit/9d42b9b8766cc069fc8e49c3d44aee90f5af7309) |
| 2015-10-25 | `fix` | Fix tooltip background # Conflicts: #	freeplane/src/org/freeplane/features/mode/ModeContro | `ModeController.java`, `MainView.java` | [60c86983](https://github.com/freeplane/freeplane/commit/60c869839083d790075d1c86f1419143e4bc7c5b) |
| 2015-10-25 | `fix` | Fix tooltip background | `ModeController.java`, `MainView.java` | [84b9f1ab](https://github.com/freeplane/freeplane/commit/84b9f1ab85a4140afe4c18633b97023b594f1f4f) |
| 2015-10-25 | `fix` | Fix: styleScrollPane shown in StyleEditor | `stylemode.generic.xml`, `SModeControllerFactory.java` | [d878e6ac](https://github.com/freeplane/freeplane/commit/d878e6ac7a1b0f30e5c4a293966c678f0f92b5bf) |
| 2015-10-25 | `fix` | Fix inline editor vertical positioning | `EditNodeTextField.java` | [af1757e1](https://github.com/freeplane/freeplane/commit/af1757e12017a3054254e3d5ddde88d50e64ee72) |
| 2015-10-25 | `fix` | Fix inline editor vertical positioning | `EditNodeTextField.java` | [558ce158](https://github.com/freeplane/freeplane/commit/558ce158ecda399aec63fef174235a5996b49f85) |
| 2015-10-25 | `feature` | Add formatting to tool tips | `TextController.java`, `MainView.java` +1 | [be31b885](https://github.com/freeplane/freeplane/commit/be31b885cd2ee9121de1330856d1425a4485f08e) |
| 2015-10-25 | `feature` | Add formatting to tool tips | `TextController.java`, `MainView.java` +1 | [e743bcc3](https://github.com/freeplane/freeplane/commit/e743bcc3cccd919cfe5055664904244c30298fe3) |
| 2015-10-25 | `fix` | fix var name | `NoteController.java` | [2130412a](https://github.com/freeplane/freeplane/commit/2130412a87a3eaa71351888a64f05ad867383588) |
| 2015-10-25 | `fix` | fix var name | `NoteController.java` | [74194349](https://github.com/freeplane/freeplane/commit/74194349b2301990edd888a1701fdd91184dc60e) |
| 2015-10-25 | `fix` | Fix inline editor positioning | `ZoomableLabelUI.java`, `EditNodeTextField.java` | [57951eae](https://github.com/freeplane/freeplane/commit/57951eae15283a797cb1f31e03bd6c2c84fd1142) |
| 2015-10-25 | `fix` | Fix inline editor positioning | `ZoomableLabelUI.java`, `EditNodeTextField.java` | [ab17c168](https://github.com/freeplane/freeplane/commit/ab17c1680ae0ab88472b873ddc9d8a58ceb7174a) |
| 2015-10-23 | `fix` | Fix caret position for edit details on click | `DetailsViewMouseListener.java` | [276f908f](https://github.com/freeplane/freeplane/commit/276f908f418483f9f330df29aba4d1c7bdb6b93f) |
| 2015-10-23 | `fix` | Fix caret position for edit details on click | `DetailsViewMouseListener.java` | [056caecc](https://github.com/freeplane/freeplane/commit/056caecc1335d0868a373937f73432118828ef32) |
| 2015-10-23 | `fix` | Fix caret position in edit on click | `EditNodeTextField.java` | [31a30e45](https://github.com/freeplane/freeplane/commit/31a30e450b91cdde446b4d11a7845f581f0edeb5) |
| 2015-10-23 | `fix` | Fix caret position in edit on click | `EditNodeTextField.java` | [6ecea988](https://github.com/freeplane/freeplane/commit/6ecea988d2731496ced15ab81caa584bd8015e9d) |
| 2015-10-23 | `fix` | Fix text editor field position for center- and right-aligned nodes | `EditNodeTextField.java` | [78723cf9](https://github.com/freeplane/freeplane/commit/78723cf9a8151d0301c910183fea7c8c1ca8f580) |
| 2015-10-23 | `fix` | Fix text editor field position for center- and right-aligned nodes | `EditNodeTextField.java` | [f938f3fa](https://github.com/freeplane/freeplane/commit/f938f3faa45c61dc2b558772971b6218674c37a6) |
| 2015-10-22 | `fix` | Fix navigate to menu action # Conflicts: #	freeplane/src/org/freeplane/view/swing/ui/MapsM | `NodeView.java`, `MapsMenuActionListener.java` | [9da3f20b](https://github.com/freeplane/freeplane/commit/9da3f20bb17206de831c08c85769f2d65bf14fc6) |
| 2015-10-22 | `fix` | Fix navigate to menu action | `NodeView.java`, `MapsMenuAction.java` | [4bed7b6c](https://github.com/freeplane/freeplane/commit/4bed7b6c14e592b180e4f2d0216aeb71bc9bdc78) |
| 2015-10-22 | `feature` | Add copy and paste format actions to node popup menu | `stylemodemenu.mm` | [4c618407](https://github.com/freeplane/freeplane/commit/4c618407d46858f7b71eb387f8f77ac490cab609) |
| 2015-10-21 | `fix` | Fix : register MLocationController at SModeController | `SModeControllerFactory.java` | [8e4b1197](https://github.com/freeplane/freeplane/commit/8e4b11970dcf2140091aa98b2972def9da73baa2) |
| 2015-10-21 | `fix` | Fix : register MLocationController at SModeController | `SModeControllerFactory.java` | [fc64d43a](https://github.com/freeplane/freeplane/commit/fc64d43aa59ca1d8979f8a31a3fefe753b93d619) |
| 2015-10-21 | `fix` | Fix java 6 issues | `LengthUnits.java`, `MLocationController.java` +1 | [511446ce](https://github.com/freeplane/freeplane/commit/511446ceda9dc2986ece9d6ade785c513f8b678b) |
| 2015-10-21 | `feature` | Add bubble_vertical_margin quantity property to preferences # Conflicts: #	freeplane/resou | `preferences.mm`, `Resources_en.properties` | [3c19aa54](https://github.com/freeplane/freeplane/commit/3c19aa54a40458f988c10f6a410df11b6d573603) |
| 2015-10-21 | `feature` | Add child gap to StyeEditorPanel and implement StyleCopier for LocationModel # Conflicts:  | `BubbleMainView.java`, `freeplane.properties` | [ac7b6bc0](https://github.com/freeplane/freeplane/commit/ac7b6bc06eca5b10ecbad7691cfe05d32754f0cb) |
| 2015-10-21 | `feature` | Add strings for Lengths.pt | `Resources_de.properties`, `Resources_en.properties` | [6652d584](https://github.com/freeplane/freeplane/commit/6652d584218439cb2e316015b8c7204c1be61cea) |
| 2015-10-21 | `feature` | Add strings for Lengths.pt | `Resources_de.properties`, `Resources_en.properties` | [82648e2e](https://github.com/freeplane/freeplane/commit/82648e2eb266edf7d1ad81a90cb206184a311bc2) |
| 2015-10-21 | `feature` | Add bubble_vertical_margin quantity property to preferences | `preferences.xml`, `Resources_en.properties` | [ec03ca65](https://github.com/freeplane/freeplane/commit/ec03ca658482776ccaaa9ee3b2b759ac29baa2cf) |
| 2015-10-21 | `feature` | Add quantity properties to OptionPanelBuilder | `OptionPanelBuilder.java` | [cce7f71c](https://github.com/freeplane/freeplane/commit/cce7f71ce10915042e580d627ed5ab3013d37e6a) |
| 2015-10-21 | `feature` | Add quantity properties to OptionPanelBuilder | `OptionPanelBuilder.java` | [ef45dc81](https://github.com/freeplane/freeplane/commit/ef45dc81ce9f8771a8d06f06d1d91470b50db042) |
| 2015-10-21 | `feature` | Introduce new property bubble_vertical_margin for specifying default vertical bubble space | `BubbleMainView.java`, `freeplane.properties` | [d2fd2f85](https://github.com/freeplane/freeplane/commit/d2fd2f8526932c5bbfb82a43c001db083d26a6b7) |
| 2015-10-21 | `feature` | Add child gap to StyeEditorPanel and implement StyleCopier for LocationModel | `NumberProperty.java`, `IExtensionCopier.java` +3 | [e3ff7230](https://github.com/freeplane/freeplane/commit/e3ff723089859607d8310d47d5cee2ad08da27d0) |
| 2015-10-21 | `feature` | Add child gap to StyeEditorPanel and implement StyleCopier for LocationModel | `NumberProperty.java`, `IExtensionCopier.java` +3 | [50e0db02](https://github.com/freeplane/freeplane/commit/50e0db026ad02a79d2d8d50d3b54183b69b2b6c8) |
| 2015-10-21 | `fix` | Bug fixes in dragging node | `MNodeMotionListener.java` | [836483d5](https://github.com/freeplane/freeplane/commit/836483d5f22e117e67759f1f48e57f0f409d6bd6) |
| 2015-10-21 | `fix` | Bug fixes in dragging node | `MNodeMotionListener.java` | [ae38c9a9](https://github.com/freeplane/freeplane/commit/ae38c9a94db73b1ae8df862e79c405992ddbd66c) |
| 2015-10-20 | `feature` | Add FormatCopy and FormatPaste actions to stylemode node popup menu | `stylemode.generic.xml` | [7e396849](https://github.com/freeplane/freeplane/commit/7e39684924ffe074ef99ccd2f370f8cb2153e090) |
| 2015-10-20 | `feature` | Add builder for toolbar and popups to stylemode.generic.xml | `stylemode.generic.xml` | [e46f1aee](https://github.com/freeplane/freeplane/commit/e46f1aee459f802bddff64b4bca3329c211f45a9) |
| 2015-10-19 | `fix` | improve fix for RotatableLabelUI | `RotatableLabelUI.java` | [0d02eee5](https://github.com/freeplane/freeplane/commit/0d02eee5908f78bcdd2d84618c92e79e064b5dd6) |
| 2015-10-19 | `fix` | improve fix for RotatableLabelUI | `RotatableLabelUI.java` | [056b4ca4](https://github.com/freeplane/freeplane/commit/056b4ca48f6d7b41e73e1d79fed419e75f64289e) |
| 2015-10-19 | `fix` | Patch infonode: RotatableLabelUI paint uses wrong FontMetrics in paint | `RotatableLabelUI.java` | [a3471450](https://github.com/freeplane/freeplane/commit/a34714504aa9f27a4b02c0509aed2518f766420e) |
| 2015-10-19 | `fix` | Patch infonode: RotatableLabelUI paint uses wrong FontMetrics in paint | `RotatableLabelUI.java` | [57942f0c](https://github.com/freeplane/freeplane/commit/57942f0c1de7242aa9fc653b0a778a81388aad4f) |
| 2015-10-18 | `feature` | Add text alignment combo to style panel and fix default text alignment | `NodeStyleBuilder.java`, `NodeStyleController.java` +5 | [f1ccf881](https://github.com/freeplane/freeplane/commit/f1ccf881a67254747451abb7e9d89ae4ff3cad9c) |
| 2015-10-18 | `feature` | Add text alignment combo to style panel and fix default text alignment | `NodeStyleBuilder.java`, `NodeStyleController.java` +5 | [484d3c31](https://github.com/freeplane/freeplane/commit/484d3c31fb881300e7837bb0f376ba11b213583e) |
| 2015-10-18 | `fix` | Fix menus | `mindmapmode.generic.xml`, `stylemode.generic.xml` +1 | [58711446](https://github.com/freeplane/freeplane/commit/587114468b806d83e082190239379625caae228c) |
| 2015-10-18 | `fix` | Fix ConcurrentModificationException | `SelectionController.java` | [7cfd7346](https://github.com/freeplane/freeplane/commit/7cfd7346c07bf02cd53124da96e2667aca7945a4) |
| 2015-10-18 | `fix` | Fix ConcurrentModificationException | `SelectionController.java` | [2a2c61a4](https://github.com/freeplane/freeplane/commit/2a2c61a421b1c7542f533eefbb9cc0daed74ccf2) |
| 2015-10-17 | `feature` | Refactor: extract class CssRuleBuilder to create CSS rules | `CssRuleBuilder.java`, `ScaledEditorKit.java` +5 | [bccd28e7](https://github.com/freeplane/freeplane/commit/bccd28e7bbdc69a8fffa9ae184b472d07451ee7a) |
| 2015-10-17 | `feature` | Refactor: extract class CssRuleBuilder to create CSS rules | `CssRuleBuilder.java`, `ScaledEditorKit.java` +5 | [3bf0c898](https://github.com/freeplane/freeplane/commit/3bf0c898fbc5686892ff9f84e8903bad0e09b898) |
| 2015-10-17 | `fix` | Fix NewLevelStyleAction/DeleteLevelStyleAction | `MapStyleModel.java`, `DeleteLevelStyleAction.java` +1 | [aae0c0a7](https://github.com/freeplane/freeplane/commit/aae0c0a766a9624835c0c7faad5a22de8e4d3f14) |
| 2015-10-13 | `fix` | Fix refresh of last opened maps for ribbons | `mindmapmode.generic.xml`, `RibbonLastOpenedMapsBuilder.java` | [49bb70c3](https://github.com/freeplane/freeplane/commit/49bb70c34b9bd900c9edfa3c3495bc3d78a5c883) |
| 2015-10-13 | `fix` | Fix concurrent modification exception. Also replace HashSet by ArrayList (I do not underst | `SelectionController.java` | [db71cbc7](https://github.com/freeplane/freeplane/commit/db71cbc706db6b75da501c5d00065a96c96be348) |
| 2015-10-13 | `feature` | Improve layout of last opened maps: add horizontal scrolling and make menu elements small | `RibbonLastOpenedMapsBuilder.java` | [a31c0279](https://github.com/freeplane/freeplane/commit/a31c02796ee3ceb12e393c6b6041cd4dd1cfa644) |
| 2015-10-10 | `fix` | Fix in ActionFinder | `ActionFinder.java` | [9a579270](https://github.com/freeplane/freeplane/commit/9a579270115388270245194c7e07a5bea27bb251) |
| 2015-10-10 | `feature` | Add special UI builders for menus File and Edit | `mindmapmode.generic.xml`, `MenuBuildProcessFactory.java` | [55c1ebba](https://github.com/freeplane/freeplane/commit/55c1ebbaeba16242841170e12dc463131b2504b0) |
| 2015-09-05 | `api_change` | removed more old ribbon api calls | `RibbonActionComponentProvider.java`, `FreeplaneGUIStarter.java` +4 | [7f82b617](https://github.com/freeplane/freeplane/commit/7f82b6170eca0e86f447f21f02241d106532a546) |
| 2015-08-30 | `fix` | Fix small issue with array length checks in CommandLineParser.parse() | `CommandLineParser.java` | [101c3f76](https://github.com/freeplane/freeplane/commit/101c3f76321569b5fac8126513aa29f370ba9742) |
| 2015-08-30 | `fix` | Fix -U option: reset userfpdir early (so that backupdir honors this setting) and also set  | `CommandLineParser.java`, `FreeplaneGUIStarter.java` +2 | [f08b1446](https://github.com/freeplane/freeplane/commit/f08b144636c83b5075939376cb15effae7f5d3b0) |
| 2015-07-17 | `feature` | 2195: Make data formatting, formula processing and LaTeX rendering independently configura | `preferences.mm`, `ConditionalContentTransformer.java` +7 | [925ec4ed](https://github.com/freeplane/freeplane/commit/925ec4ed74b24ed116c000393f0ad22e7d7ebe01) |
| 2015-06-22 | `fix` | fix NPE | `UIComponentVisibilityDispatcher.java` | [c2b037f7](https://github.com/freeplane/freeplane/commit/c2b037f738c2498286de0699f41de7c7ab1edd03) |
| 2015-06-22 | `fix` | Fix NPE | `ToggleToolbarAction.java` | [ec1cc0a6](https://github.com/freeplane/freeplane/commit/ec1cc0a6d7ad20e78a7f523e699c4ef96c9d0ba2) |
| 2015-06-13 | `fix` | Fix NPE | `StdXMLBuilder.java` | [cddc3348](https://github.com/freeplane/freeplane/commit/cddc3348b5f25db7b8f236bc6cdaf578d5512702) |
| 2015-06-10 | `fix` | Fix #2232 ctrl+f to seach on undocked window is not working | `FilterConditionEditor.java`, `ToggleToolbarAction.java` | [d796bfc7](https://github.com/freeplane/freeplane/commit/d796bfc7d202491ea189ee858c870ab8e9761428) |
| 2015-05-14 | `feature` | BooleanProperty control can enable / disable their child controls | `BooleanProperty.java`, `OptionPanel.java` | [a1859821](https://github.com/freeplane/freeplane/commit/a18598210dc923c3783c6b9428331b5ca720cb6f) |
| 2015-05-14 | `feature` | Add ability to execute operating system commands or shell commands from clicking nodes. ht | `mindmapmode.generic.xml`, `LinkController.java` +3 | [740221c7](https://github.com/freeplane/freeplane/commit/740221c7e6c99274c6801d8788e0ade4bc26cc18) |
| 2015-05-10 | `fix` | Fix map view change if tab is selected from outside | `MapViewDockingWindows.java` | [bf417a2c](https://github.com/freeplane/freeplane/commit/bf417a2cd86cbc2e396a48b59220df6e2e2a16d2) |
| 2015-05-03 | `fix` | Fix drag and drop of nodes between different map views | `MNodeDropListener.java` | [435a18c4](https://github.com/freeplane/freeplane/commit/435a18c47748ba03c5254fb68621722b0e12aa79) |
| 2015-05-03 | `fix` | fix -U help text | `Compat.java`, `CommandLineParser.java` | [28bcc1cc](https://github.com/freeplane/freeplane/commit/28bcc1cc4ac1dd6b4a9fc0cb73e98cd006d72046) |
| 2015-05-02 | `feature` | Add NewMapViewAction to the menu | `mindmapmode.generic.xml` | [91355506](https://github.com/freeplane/freeplane/commit/91355506b43ce1cf9f5f5fceda590b292cb8fdbb) |
| 2015-04-25 | `feature` | Enable ribbons on this branch again | `UITools.java` | [3d49f4a4](https://github.com/freeplane/freeplane/commit/3d49f4a4cf434b597208793c54513e5865aba0b3) |
| 2015-04-25 | `feature` | Support actions not registered by controllers in ActionAcceleratorManager | `ActionAcceleratorManager.java`, `MenuBuilder.java` +15 | [374d6a73](https://github.com/freeplane/freeplane/commit/374d6a73dba8dbce993eccfee7a9dc87d48064bd) |
| 2015-04-23 | `fix` | Fix date filtering on node content | `CompareConditionAdapter.java`, `NodeTextCompareCondition.java` +2 | [4179ff62](https://github.com/freeplane/freeplane/commit/4179ff62671a1e1071c58803d57535cf5defc83c) |
| 2015-04-23 | `fix` | Fix date filtering on attributes https://sourceforge.net/p/freeplane/discussion/758437/thr | `AttributeCompareCondition.java` | [640110b6](https://github.com/freeplane/freeplane/commit/640110b680ec94b280c6193dfe3cd07029a0c3e7) |
| 2015-04-20 | `fix` | Fix merge of Resources_pt_BR.properties | `Resources_pt_BR.properties` | [2694e983](https://github.com/freeplane/freeplane/commit/2694e983324f21f1262e799dbb0dbc74ed0b70e1) |
| 2015-04-20 | `fix` | Fix [bugs:#2218] Filter with RegExp [] disappears | `AttributeConditionController.java`, `AttributeMatchesCondition.java` +1 | [052ae074](https://github.com/freeplane/freeplane/commit/052ae07498d4444a5d069d50c79b51da33fb4cd1) |
| 2015-04-11 | `fix` | fix rebuild style menu | `MLogicalStyleController.java` | [5c91b617](https://github.com/freeplane/freeplane/commit/5c91b617cb047d2568b71c64ce225bdb83b41a50) |
| 2015-04-06 | `fix` | fix applet | `mindmapmode.generic.xml`, `ActionAcceleratorManager.java` +9 | [da97c6e4](https://github.com/freeplane/freeplane/commit/da97c6e438e409cbeb9b37d1ae59b7aec2cf1a49) |
| 2015-04-06 | `fix` | Fix ActionAcceleratorManager to handle all modes | `ActionAcceleratorManager.java`, `MenuBuilder.java` +3 | [1f65f785](https://github.com/freeplane/freeplane/commit/1f65f785c74570ae2a0263090640e34bace98229) |
| 2015-04-06 | `feature` | Add Freeplane 1.4.0 to allowed map versions | `mapVersions.xml` | [418e2770](https://github.com/freeplane/freeplane/commit/418e27709cde993309f1d03c3b38853d40bf3223) |
| 2015-04-05 | `feature` | Add URL field contributor to the browser toolbar | `BModeControllerFactory.java`, `BToolbarContributor.java` +1 | [86c5b230](https://github.com/freeplane/freeplane/commit/86c5b2306af4423c7f1dd1d470727a55e9e373b2) |
| 2015-04-04 | `feature` | add Entry.findChildRecursively(name) | `Entry.java`, `EntryTest.java` | [7f2b2569](https://github.com/freeplane/freeplane/commit/7f2b2569490dc0739600b9ae6279408b02f89549) |
| 2015-04-03 | `feature` | Add mode and map popup menus to generic UI | `mindmapmode.generic.xml`, `JToolbarBuilder.java` +6 | [66cbb403](https://github.com/freeplane/freeplane/commit/66cbb403552a5bd7786401c12aba8f1747e3c1bc) |
| 2015-04-03 | `feature` | UpdateCheckAction ready for new UI | `FreeplaneGUIStarter.java`, `HttpVersionClient.java` +2 | [9ca8bf59](https://github.com/freeplane/freeplane/commit/9ca8bf59c9546f5962dc62c7a8abe14d53bc328f) |
| 2015-04-02 | `feature` | Add custom components to toolbar | `mindmapmode.generic.xml`, `IUserInputListenerFactory.java` +15 | [a1f314db](https://github.com/freeplane/freeplane/commit/a1f314dbc81126ed5586e3ff2830d8cf8d7a2695) |
| 2015-04-01 | `feature` | Add accelerators | `ActionAcceleratorManager.java`, `AcceleratorBuilder.java` +19 | [7e63bf66](https://github.com/freeplane/freeplane/commit/7e63bf66faae6f2eca00027924f7d1f3a39fdaae) |
| 2015-04-01 | `feature` | add AcceleratorBuilder to menu build phase processor | `MenuBuildProcessFactory.java`, `UserInputListenerFactory.java` +2 | [ce47a275](https://github.com/freeplane/freeplane/commit/ce47a275827365b961c871ab731dbbeb03c5722a) |
| 2015-03-30 | `feature` | fix menu splitter : use this instead of new | `MenuSplitter.java` | [40228dd2](https://github.com/freeplane/freeplane/commit/40228dd273b618527212c2cb283b3abc756ad2bc) |
| 2015-03-27 | `feature` | Start integration of the new menu builders | `.classpath`, `MANIFEST.MF` +4 | [833c8c57](https://github.com/freeplane/freeplane/commit/833c8c57ba6cdd2fa903a69c5ab4e21693e65390) |
| 2015-02-28 | `feature` | Rename RecursiveMenuStructureBilder to RecursiveMenuStructureProcessor, rename builders to | `RecursiveMenuStructureBuilder.java`, `RecursiveMenuStructureProcessor.java` +2 | [b27033e6](https://github.com/freeplane/freeplane/commit/b27033e68ea927f54c1078231aea7ff3ad76e30a) |
| 2015-02-28 | `feature` | Add text and icon to submenu elements | `JMenuItemBuilder.java`, `JMenuItemBuilderTest.java` | [8d6e8896](https://github.com/freeplane/freeplane/commit/8d6e8896f2189035f9aa6cce329481278ce03ed0) |
| 2015-02-23 | `fix` | Fix external image zooming | `BitmapViewerFactory.java`, `ExternalResource.java` +2 | [63e223d8](https://github.com/freeplane/freeplane/commit/63e223d8cc9a1b28dff7852e04007b27a350e470) |
| 2015-02-15 | `feature` | delayChildBuild optional, not all builders support destroy | `AcceleratorBuilder.java`, `JMenubarBuilder.java` +5 | [382f7a53](https://github.com/freeplane/freeplane/commit/382f7a53aa5f3bd5d30357063778b6ac618acd30) |
| 2015-02-15 | `feature` | Support for delayed builds and entry destroy | `AcceleratorBuilder.java`, `ActionFinder.java` +11 | [01fbbd18](https://github.com/freeplane/freeplane/commit/01fbbd1821420d2f030568038557ec3eb7273c1f) |
| 2015-02-14 | `api_change` | own interface EntryPopupListener | `ActionFinder.java`, `EntryPopupListener.java` +6 | [a18dc189](https://github.com/freeplane/freeplane/commit/a18dc189f02a9e85ea69192a4f0719d2cec608c5) |
| 2015-02-07 | `fix` | Workaround for bug introduced in Java 8:  they use wrong component in DefaultCellEditor.Ed | `AttributeTable.java` | [fb494813](https://github.com/freeplane/freeplane/commit/fb4948138d5f0835920c663b5e92952917d4db75) |
| 2015-02-01 | `fix` | bug fix for hot hey map | `MenuBuilder.java` | [29ab3def](https://github.com/freeplane/freeplane/commit/29ab3def8f7e4a062fbfafe6be2957bcb3e71b78) |
| 2015-01-01 | `feature` | add jgoodies-forms/commons, move some java files from src/ to src/main/java | `build.gradle`, `ConditionSnapshotFactory.java` +15 | [bc062b52](https://github.com/freeplane/freeplane/commit/bc062b5210d694fba72d6ad405bdb0ed04a736ed) |

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

**[7ba65625](https://github.com/freeplane/freeplane/commit/7ba6562553e41cace9a4404830e46892962f3a27)** (2015-11-28) — Fix: Do not delete summary node parent inside undo action

> STDERR: Exception in thread "AWT-EventQueue-0" 
> STDERR: java.lang.NullPointerException
> STDERR: 	at
> org.freeplane.features.map.mindmapmode.MMapController.deleteWithoutUndo(MMapController.java:326)
> STDERR: 	at
> org.freeplane.features.map.mindmapmode.MMapController$3.undo(MMapController.java:250)
> STDERR: 	at
> org.freeplane.core.undo.CompoundActor.undo(CompoundActor.java:71)
> STDERR: 	at
> org.freeplane.core.undo.UndoHandler.undo(UndoHandler.java:317)
> STDERR: 	at
> org.freeplane.core.undo.UndoHandler$UndoAction.actionPerformed(UndoHandler.java:47)

**[330e8221](https://github.com/freeplane/freeplane/commit/330e8221a08fbd511ea9ff26a774eb8ca6c69867)** (2015-11-28) — Fix: Do not delete summary node parent inside undo action

> STDERR: Exception in thread "AWT-EventQueue-0" 
> STDERR: java.lang.NullPointerException
> STDERR: 	at
> org.freeplane.features.map.mindmapmode.MMapController.deleteWithoutUndo(MMapController.java:326)
> STDERR: 	at
> org.freeplane.features.map.mindmapmode.MMapController$3.undo(MMapController.java:250)
> STDERR: 	at
> org.freeplane.core.undo.CompoundActor.undo(CompoundActor.java:71)
> STDERR: 	at
> org.freeplane.core.undo.UndoHandler.undo(UndoHandler.java:317)
> STDERR: 	at
> org.freeplane.core.undo.UndoHandler$UndoAction.actionPerformed(UndoHandler.java:47)

**[7ec28be4](https://github.com/freeplane/freeplane/commit/7ec28be45aed0acae11e26cc3fb00f2444ea360e)** (2015-11-19) — Add mouse listeners only to nodes that can be edited, style map nodes with levels 0 and 1 can not be edited

> # Conflicts:
> #	freeplane/src/main/java/org/freeplane/features/mode/ModeController.java


---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-21 | `feature` | Support for unicode characters in case insensitive filters | `AttributeMatchesCondition.java`, `NodeMatchesRegexpCondition.java` +1 | [1cc8a65e](https://github.com/freeplane/freeplane/commit/1cc8a65ec71a8d5ed7e0dddab87a6d62cd8bf06e) |
| 2014-12-21 | `fix` | Fix unicode entities in search and replace http://sourceforge.net/p/freeplane/discussion/7 | `HtmlUtils.java`, `NodeList.java` +1 | [fb23cbf6](https://github.com/freeplane/freeplane/commit/fb23cbf6d6a3f2010e7848c1b3e1c29f06afe031) |
| 2014-12-21 | `feature` | add toString | `WeightedMutableTreeNode.java` | [8aac41ab](https://github.com/freeplane/freeplane/commit/8aac41abb70a11911e3259c46db7ed2c8abaf564) |
| 2014-12-10 | `feature` | 2202: Behavior of read-only maps: Fix close behavior (also clean up and make sure that isS | `MMapController.java`, `MMapModel.java` | [8cbfdba0](https://github.com/freeplane/freeplane/commit/8cbfdba0aaf90e3900d1627af8522fc8b48317a9) |
| 2014-12-10 | `feature` | 2202: Behavior of read-only maps: Fix close behavior (also clean up and make sure that isS | `MMapController.java`, `MMapModel.java` | [7818259f](https://github.com/freeplane/freeplane/commit/7818259fce4e9791e9088787e4a78dda15203c64) |
| 2014-12-09 | `fix` | 2202: Behavior of read-only maps: Fix handling of read-only modified maps on close | `MMapController.java` | [4b738a3e](https://github.com/freeplane/freeplane/commit/4b738a3e574f6733dba39dde9ce75beed16a1f86) |
| 2014-12-09 | `fix` | 2202: Behavior of read-only maps: Fix handling of read-only modified maps on close | `MMapController.java` | [c23dfcee](https://github.com/freeplane/freeplane/commit/c23dfceeb9b60d98534ade2c387a3a6afc3b71eb) |
| 2014-12-09 | `api_change` | 2202: Behavior of read-only maps: - treat read-only maps (chmod -w *.mm) and documentation | `MapModel.java`, `MMapController.java` +5 | [104dc0d1](https://github.com/freeplane/freeplane/commit/104dc0d10b2358faf1c0064554358f2073baac32) |
| 2014-12-09 | `api_change` | 2202: Behavior of read-only maps: - treat read-only maps (chmod -w *.mm) and documentation | `MapModel.java`, `MMapController.java` +5 | [e53e5540](https://github.com/freeplane/freeplane/commit/e53e5540a44e174cfae8be80121e642ff2bebbbd) |
| 2014-11-01 | `feature` | After editing node text was canceled by escape the editing pane becomes not showing but it | `UITools.java` | [65d7f4e3](https://github.com/freeplane/freeplane/commit/65d7f4e385388373e8a0918e43fa71f0e0bdbbf6) |
| 2014-10-30 | `fix` | Fix bug leading to map get unsaved status after loading | `MMapController.java` | [4611a90d](https://github.com/freeplane/freeplane/commit/4611a90dfb1f7296707ee6e8e983419f4946fe11) |
| 2014-10-22 | `fix` | Update zh-CN translations | `Resources_zh_CN.properties` | [9bae2046](https://github.com/freeplane/freeplane/commit/9bae2046b4c5e6122c034d9b4395e3513c6da3e4) |
| 2014-10-22 | `feature` | Update zh-CN translation resources | `Resources_zh_CN.properties` | [96b3060d](https://github.com/freeplane/freeplane/commit/96b3060d44118c3b654a6a675f3ff7175093c3ee) |
| 2014-09-13 | `fix` | fix OptionPanel.tr (Turkmen->Turkish) | `Resources_da.properties`, `Resources_de.properties` +10 | [5cb003ba](https://github.com/freeplane/freeplane/commit/5cb003badb169c00bee21ac057d340269bcc5d69) |
| 2014-09-11 | `feature` | move LayoutData to new file | `LayoutData.java`, `LeftNodeViewLayout.java` +3 | [14d50878](https://github.com/freeplane/freeplane/commit/14d5087861eef628a1217e04664c977162520e12) |
| 2014-09-08 | `fix` | fix for further locations that might be subject of the http://mattryall.net/blog/2009/02/t | `ResourceController.java`, `RibbonActionContributorFactory.java` +1 | [835fac3c](https://github.com/freeplane/freeplane/commit/835fac3c8702bc75eb52d2669c467db0995e63ca) |
| 2014-08-31 | `feature` | add IconMouseListener concept for clicks on icons and use it to call openmaps viewer when  | `MultipleImage.java`, `IconClickedEvent.java` +6 | [83e5bd24](https://github.com/freeplane/freeplane/commit/83e5bd24bfe85be7247b05042907554850433527) |
| 2014-07-28 | `fix` | fix TabDropDownListVisiblePolicy | `MapViewDockingWindows.java` | [08b671d9](https://github.com/freeplane/freeplane/commit/08b671d9dad438d0fc07fdefdad14878360fb6c3) |
| 2014-07-28 | `fix` | fix TabDropDownListVisiblePolicy | `MapViewDockingWindows.java` | [5f648cca](https://github.com/freeplane/freeplane/commit/5f648cca91497bb8ce132d4471f243a176b89d9f) |
| 2014-07-08 | `fix` | fix creation of external viewers for node clones | `ViewerController.java` | [095cd4e7](https://github.com/freeplane/freeplane/commit/095cd4e76e2bb1ab6337dc19e64da39a3490e761) |
| 2014-06-19 | `feature` | extend attribute conditions to support checks for any attribute name or value | `DoubleListModel.java`, `AttributeCompareCondition.java` +7 | [d1c71c88](https://github.com/freeplane/freeplane/commit/d1c71c887d26c83353f82149a7651e78e7880c88) |
| 2014-06-04 | `feature` | new Date().getTime() -> System.currentTimeMillis() | `TimeConditionController.java`, `ReminderConditionController.java` +1 | [c604f332](https://github.com/freeplane/freeplane/commit/c604f332fcec752038d5b36a9d0755e698f1e0b2) |
| 2014-06-01 | `feature` | add check for already deleted nodes in notDeletedClone | `MLinkController.java` | [b40f3798](https://github.com/freeplane/freeplane/commit/b40f3798ab5a29df16043506049fac1d637bd3d8) |
| 2014-05-26 | `fix` | fix handling of links for clones | `NodeLinkModel.java`, `MLinkController.java` +1 | [71ca62e1](https://github.com/freeplane/freeplane/commit/71ca62e16b8bf601da3bfb954ec84e11f6ecc3c6) |
| 2014-05-24 | `fix` | fix class cast exception | `HyperTextLinkModel.java` | [89274d92](https://github.com/freeplane/freeplane/commit/89274d922746d44b8df0a02f9be994126aa15022) |
| 2014-05-14 | `fix` | fix MLinkController.NodeDeletionListener.updateMapLinksForSourceTree : NPE | `MLinkController.java` | [9b9f61db](https://github.com/freeplane/freeplane/commit/9b9f61db28d717630d47f3860aa6aec0bd61b7ee) |
| 2014-05-06 | `fix` | fix for keeping node location on screen after details are shown / hidden | `ToggleDetailsAction.java`, `MapView.java` +3 | [2044c697](https://github.com/freeplane/freeplane/commit/2044c69742c3d679436d4377299e9d6c01edd2bc) |
| 2014-04-22 | `fix` | fix key accelerator conversion from ribbons to menu | `ribbons2menu.xsl` | [38e64d70](https://github.com/freeplane/freeplane/commit/38e64d705f3760d10b985efb6fa6cdb90189f3d2) |
| 2014-04-13 | `fix` | fix xslt to menu xml : edd edit menu based on home ribbon_task | `ribbons2menu.xsl` | [e263dbc9](https://github.com/freeplane/freeplane/commit/e263dbc912543cc612da0d2bd99c63d9b408fff9) |
| 2014-04-13 | `fix` | fix undo for deletion of cloned nodes | `DetachedNodeList.java`, `NodeModel.java` | [d5903a46](https://github.com/freeplane/freeplane/commit/d5903a46c807485d22a09c11c99f99238ddec422) |
| 2014-04-13 | `fix` | Fix unlinking of deleted nodes | `MLinkController.java`, `Clones.java` +2 | [d44bebe1](https://github.com/freeplane/freeplane/commit/d44bebe192bef844ea6f2ccfea21c12f6423660e) |
| 2014-04-13 | `feature` | performance optimization: do not create NPE, return null | `IsoDateParser.java` | [4cf9c81e](https://github.com/freeplane/freeplane/commit/4cf9c81e2208ab706748a0ab465c9ed1330cdf56) |
| 2014-04-13 | `feature` | performance optimization: do not create NPE, return null | `IsoDateParser.java` | [b8286381](https://github.com/freeplane/freeplane/commit/b828638111759976f7ecff3b7bec33c876c79c3e) |
| 2014-04-12 | `feature` | Moved freeplane files to the new structure | `AsyncScalr.java`, `Scalr.java` +924 | [cbde615a](https://github.com/freeplane/freeplane/commit/cbde615a1b35e12ab19be1ed77c5c1d151db6e59) |
| 2014-04-10 | `feature` | new: HtmlUtils.join(String... texts) | `HtmlUtils.java`, `AllFreeplaneUnitTests.java` +1 | [ed2fbb2d](https://github.com/freeplane/freeplane/commit/ed2fbb2d4c14d84f027c6f26219a8e0cad522f9d) |
| 2014-04-10 | `feature` | new: HtmlUtils.join(String... texts) | `HtmlUtils.java`, `AllFreeplaneUnitTests.java` +1 | [d5651113](https://github.com/freeplane/freeplane/commit/d565111395963741289fc1a4f2875a5dbd6ce589) |
| 2014-04-10 | `feature` | Moved JOrtho to the new folder structure | `build.gradle`, `SampleApplet.java` +42 | [e5f90801](https://github.com/freeplane/freeplane/commit/e5f90801ec91bb150fe32f4ba624380a3965984c) |
| 2014-03-25 | `fix` | bug fix | `SharedNodeData.java` | [7eaee090](https://github.com/freeplane/freeplane/commit/7eaee090f7e988b1ae60569160887214cf999989) |
| 2014-03-25 | `fix` | fix NPE for clones | `NodeLinkModel.java`, `MultipleNodeList.java` +1 | [8a250546](https://github.com/freeplane/freeplane/commit/8a250546f17b5d76dc26c3347f7381bd04f696ba) |
| 2014-03-23 | `fix` | Fix connector deletion | `NodeLinks.java` | [03d78836](https://github.com/freeplane/freeplane/commit/03d788368bfd12a099d82e3896e58103b0cee572) |
| 2014-03-23 | `fix` | fix bug in NodeRelativePath | `NodeAbsolutePath.java`, `NodeRelativePath.java` | [ffc0dbf2](https://github.com/freeplane/freeplane/commit/ffc0dbf25681f3734484253068f79a9f13587475) |
| 2014-03-22 | `feature` | Add Format=Unparsed LaTeX and \unparsedlatex node prefix to allow LaTeX content that is so | `mm2latexinput.xsl`, `Resources_de.properties` +4 | [fa8385f0](https://github.com/freeplane/freeplane/commit/fa8385f0fd12f48c206507583caf6a4e7ae30da8) |
| 2014-03-16 | `feature` | avoid ConcurrentModificationExceptions on add-on update check | `AddOnsController.java` | [40bb8a47](https://github.com/freeplane/freeplane/commit/40bb8a478d49e592919ef7ff6a5b9a63711404e0) |
| 2014-03-16 | `feature` | avoid ConcurrentModificationExceptions on add-on update check | `AddOnsController.java` | [eece7ca2](https://github.com/freeplane/freeplane/commit/eece7ca245d5c9671ff30b1ede28f2381ea27628) |
| 2014-03-09 | `feature` | Add revert action to group of open action | `mindmapmoderibbon.xml` | [92c1c643](https://github.com/freeplane/freeplane/commit/92c1c643c7fd15e659a21854d8bb08bb452edd77) |
| 2014-03-08 | `fix` | fix RibbonMapChangeAdapter : it should respond to map change, not to map creation | `RibbonMapChangeAdapter.java`, `MModeControllerFactory.java` | [25c96d2c](https://github.com/freeplane/freeplane/commit/25c96d2c08700805abe874dc2cab290d9787fd77) |
| 2014-03-08 | `fix` | fix loading background image on start | `MapView.java`, `SvgViewerFactory.java` | [af6f06ad](https://github.com/freeplane/freeplane/commit/af6f06ad55bec4b1db46253b2bfa6839820e18e3) |
| 2014-03-08 | `fix` | fix NPE | `ViewerController.java` | [2f71bbdc](https://github.com/freeplane/freeplane/commit/2f71bbdce77eb4732fe7dae875f69bb882938437) |
| 2014-03-06 | `fix` | fix endless repaint in painting background component | `BitmapViewerComponent.java`, `ImageLoadingListener.java` +3 | [5f71fff7](https://github.com/freeplane/freeplane/commit/5f71fff74dae5ef300397ea2c4983946da063ae3) |
| 2014-03-02 | `fix` | fix ribbons2menu.xsl for ribbon actions inside other ribbon actions | `ribbons2menu.xsl` | [32284814](https://github.com/freeplane/freeplane/commit/3228481451138a5c2ffbe6142827035aea9efb15) |
| 2014-03-01 | `feature` | implement node proxy properties horizontalShift, verticalShift and minimalDistanceBetweenC | `LocationController.java`, `ChangeShiftXActor.java` +5 | [d36a6822](https://github.com/freeplane/freeplane/commit/d36a68223bcefa725299da48b5da1430f05255f6) |
| 2014-03-01 | `fix` | Fix loading of background component at opening | `MapView.java` | [db41f811](https://github.com/freeplane/freeplane/commit/db41f811c70882b84c4ab3ad150393c13db070e1) |
| 2014-03-01 | `fix` | Fix centring algorithm for bitmap viewer | `BitmapViewerComponent.java` | [23df3d6b](https://github.com/freeplane/freeplane/commit/23df3d6b0bb7faed86e57c61db09adfb9a3364f3) |
| 2014-03-01 | `fix` | Fix centring problems | `BitmapViewerComponent.java`, `ScalableComponent.java` +2 | [448a6157](https://github.com/freeplane/freeplane/commit/448a61570308d1c13b27554cf0f61a9f317ab9f7) |
| 2014-03-01 | `fix` | Refactor Viewer Components and MapView | `BitmapViewerComponent.java`, `UITools.java` +2 | [42732cd4](https://github.com/freeplane/freeplane/commit/42732cd4b39371b9ab885eff493d494ef9e1f976) |
| 2014-03-01 | `feature` | Update Scalr classes | `AsyncScalr.java`, `Scalr.java` | [2d72ef56](https://github.com/freeplane/freeplane/commit/2d72ef56b942f01b680e3db2041452ac092c72c1) |
| 2014-02-26 | `fix` | fix center node at start: require displayable instead of showing | `MapView.java` | [517dd4f5](https://github.com/freeplane/freeplane/commit/517dd4f5b2311bc755b3712a101ed16901ea7efa) |
| 2014-02-23 | `feature` | Add a call to revalidate | `MapView.java` | [9d5a53b3](https://github.com/freeplane/freeplane/commit/9d5a53b32595c4681aa5e48c641b405b79818b9b) |
| 2014-02-23 | `fix` | Fix algorithm for determining scaled image dimensions | `UITools.java` | [a5916cb1](https://github.com/freeplane/freeplane/commit/a5916cb1656effcd327e72b2270b94045cee9054) |
| 2014-02-22 | `fix` | fix NPE | `MapViewScrollPane.java` | [a6a818a4](https://github.com/freeplane/freeplane/commit/a6a818a4d31507c19bf99279a5d1d75178150a08) |
| 2014-02-21 | `feature` | Create workaround for "fit to zoom" option and limit maximum size | `BitmapViewerComponent.java`, `ScalableComponent.java` +2 | [2eea90dd](https://github.com/freeplane/freeplane/commit/2eea90dd5f4c06ca00fb13642a8be9e41097e4f1) |
| 2014-02-16 | `feature` | insert node actions support clones | `MMapController.java` | [68c1b0a7](https://github.com/freeplane/freeplane/commit/68c1b0a7cf2185b2675c188faa9f48e8e8fa1482) |
| 2014-02-16 | `feature` | add operation for clones | `MMapController.java` | [998d815e](https://github.com/freeplane/freeplane/commit/998d815e92ee2551e020aec42e923f73419f05ea) |
| 2014-02-16 | `fix` | fix centering of the selected node after the map is opened | `MapView.java`, `NodeViewFactory.java` | [e9f44084](https://github.com/freeplane/freeplane/commit/e9f4408408492261ce2f42f6f72ccb321df64101) |
| 2014-02-15 | `feature` | Add option to access background image feature from map pop up | `mindmapmodemenu.mm` | [18bbcd2f](https://github.com/freeplane/freeplane/commit/18bbcd2ff348f5f79c51b16a059963ea9eaf98dc) |
| 2014-02-14 | `feature` | Fix printing bug | `MapView.java` | [c2824534](https://github.com/freeplane/freeplane/commit/c282453481913ba37428e2c3a9d07bb2a525065d) |
| 2014-02-14 | `feature` | Add printing option for this new background feature

The background images are scaled base | `FitMap.java`, `PageAction.java` +2 | [336c057f](https://github.com/freeplane/freeplane/commit/336c057ffbe810cfa9e1e4d0b308acdf08d07a4e) |
| 2014-02-12 | `feature` | Add scaling functionality for bitmap background images | `MapView.java` | [9cf7aed2](https://github.com/freeplane/freeplane/commit/9cf7aed2de391c5577629dfab4c1377ed513f310) |
| 2014-02-11 | `fix` | Fix method to clear image | `MapStyle.java`, `MapBackgroundClearAction.java` +1 | [85939788](https://github.com/freeplane/freeplane/commit/85939788a21f802bbdf5f408f97c1ca06a075f79) |
| 2014-02-11 | `feature` | Add functionality to draw viewer component behind all nodes | `ContentPane.java`, `ForkMainView.java` +3 | [feb31153](https://github.com/freeplane/freeplane/commit/feb3115308d964f114bdc40e548a02a3e42cf311) |
| 2014-02-10 | `feature` | Add option to disable LaTeX Syntax Highlighting Editor | `Resources_de.properties`, `freeplane.properties` +3 | [4ff1f94f](https://github.com/freeplane/freeplane/commit/4ff1f94fb95854b2d7c3981e7b93b18b3398cd79) |
| 2014-02-09 | `feature` | Add SVG support (in progress) | `ViewerController.java`, `MapView.java` | [2a8396b5](https://github.com/freeplane/freeplane/commit/2a8396b5365f7f1eb1655c8a6598ea7b4ea4b683) |
| 2014-02-09 | `fix` | fix text and user object handling | `NodeModel.java`, `SharedNodeData.java` | [1c01a4a8](https://github.com/freeplane/freeplane/commit/1c01a4a8467851b27c7789495bd4ffa6d0c7d52f) |
| 2014-02-09 | `fix` | docking window bug fixes | `ApplicationViewController.java`, `MapViewDockingWindows.java` | [75b8c104](https://github.com/freeplane/freeplane/commit/75b8c104890d9ea69fd45b9bb6a1e66add80bc97) |
| 2014-02-05 | `feature` | NodeModel should not implement TreeNode | `SingleCopySource.java`, `NodeModel.java` | [a1ebb90f](https://github.com/freeplane/freeplane/commit/a1ebb90fe01efaedb8680c5442b9a49d98607592) |
| 2014-02-05 | `fix` | Fix MakeLinkToAnchorAction | `MLinkController.java` | [daa29441](https://github.com/freeplane/freeplane/commit/daa29441d62aff234fba2acb801c13be051935c0) |
| 2014-02-04 | `fix` | Minor fix on how the error message is printed | `MapBackgroundImageAction.java` | [c1b35216](https://github.com/freeplane/freeplane/commit/c1b35216b2c8d568d41cf3e782a72ca11af6974a) |
| 2014-02-03 | `feature` | Add action to clear background image | `MapBackgroundClearAction.png`, `MapBackgroundImageAction.png` +6 | [c3e6b350](https://github.com/freeplane/freeplane/commit/c3e6b350899ed7adecdf2ae6ceca282b5f3cfcff) |
| 2014-02-03 | `fix` | Fix method of centering background image | `MapView.java` | [1c358d7d](https://github.com/freeplane/freeplane/commit/1c358d7d2bc3a8bf0fff3076938d0e3055173c49) |
| 2014-02-02 | `fix` | bug fix for the last change with docking windows | `MapViewDockingWindows.java` | [03b3eedd](https://github.com/freeplane/freeplane/commit/03b3eedd345ab95ea6468c0f9151aff208f3be61) |
| 2014-02-02 | `feature` | Add a way to select and display a background image | `mindmapmodemenu.mm`, `MLogicalStyleController.java` +4 | [4ec02d29](https://github.com/freeplane/freeplane/commit/4ec02d29cd52f2740c0f3765634b35da30d087f9) |
| 2014-01-20 | `fix` | fix version numbers for user dir | `Compat.java`, `UserPropertiesUpdater.java` | [3428a6b1](https://github.com/freeplane/freeplane/commit/3428a6b102a46f8b6097d7979c52a1c7b05589c9) |
| 2014-01-12 | `fix` | fix numbering of single copied nodes | `FormatContentTransformer.java` | [7b06b5cd](https://github.com/freeplane/freeplane/commit/7b06b5cd37bb589df011c25f13631beb9a8efb52) |
| 2014-01-12 | `fix` | fix uri handler for internet explorer | `CopyNodeURIAction.java`, `FreeplaneUriConverter.java` +3 | [1f844c35](https://github.com/freeplane/freeplane/commit/1f844c3523f0dc1fe6786b254cdb3305de62c4df) |
| 2014-01-11 | `fix` | fix bug: use correct OS dependent URI for filter paths | `FilterController.java` | [5128b755](https://github.com/freeplane/freeplane/commit/5128b755e74e4aab88c63bb4fd6fa2d77647813d) |
| 2014-01-05 | `feature` | fix OpenLastOpenedAction, change property key name, add menu contributors | `mindmapmoderibbon.xml`, `ribbons2menu.xsl` +5 | [822f68c2](https://github.com/freeplane/freeplane/commit/822f68c2790bb87f9d37b4360a30446a27cc0329) |
| 2014-01-05 | `feature` | fix filter toolbar layout, add accelerator for filter toolbar | `mindmapmoderibbon.xml`, `FrameController.java` | [301a13fe](https://github.com/freeplane/freeplane/commit/301a13fe9c8023453002db41d816a62f019948ce) |
| 2014-01-04 | `feature` | do not create browser and file modes  if ribbons are in use | `FreeplaneGUIStarter.java` | [382e2d69](https://github.com/freeplane/freeplane/commit/382e2d69729166113ce9d08b739efa3328788b3f) |
| 2014-01-02 | `fix` | fix accelerator presets for menus | `ActionAcceleratorManager.java`, `MenuBuilder.java` +2 | [c7964bbd](https://github.com/freeplane/freeplane/commit/c7964bbdab005c0c3b7ca3676f4321734ece47ab) |

### Dettagli commit con note

**[9bae2046](https://github.com/freeplane/freeplane/commit/9bae2046b4c5e6122c034d9b4395e3513c6da3e4)** (2014-10-22) — Update zh-CN translations

> Apply en strings for missing translations
> Fix inconsistent strings
> Format translation

**[96b3060d](https://github.com/freeplane/freeplane/commit/96b3060d44118c3b654a6a675f3ff7175093c3ee)** (2014-10-22) — Update zh-CN translation resources

> 1. Sync with latest en resources (removed one orphan)
> 2. Leverage Ini Translator to add a few translations and make
> translations consistent

**[42732cd4](https://github.com/freeplane/freeplane/commit/42732cd4b39371b9ab885eff493d494ef9e1f976)** (2014-03-01) — Refactor Viewer Components and MapView

> Removed unnecessary methods due to the updating of the Scalr classes.
> Now the scalable component implementations are responsible for
> centring their images. The only problem that remains is the bug
> involving the off centring of SVG images.

**[2d72ef56](https://github.com/freeplane/freeplane/commit/2d72ef56b942f01b680e3db2041452ac092c72c1)** (2014-03-01) — Update Scalr classes

> The current version now supports the BEST_FIT_BOTH mode, which is
> needed to cleanly implement the bitmap viewer component. Now I can
> delete the scaleProportionallyFromTo method in the UITools that I
> created – it essentially has the same effect as the BEST_FIT_BOTH mode.

**[2eea90dd](https://github.com/freeplane/freeplane/commit/2eea90dd5f4c06ca00fb13642a8be9e41097e4f1)** (2014-02-21) — Create workaround for "fit to zoom" option and limit maximum size

> I created a method in order to adjust the preferred size width/height
> ratio to that of the original image. Moreover, I limited the maximum
> size of the viewer to the preferred size of the MapView, eliminating
> the "out of memory error" occurrences.

**[c2824534](https://github.com/freeplane/freeplane/commit/c282453481913ba37428e2c3a9d07bb2a525065d)** (2014-02-14) — Fix printing bug

> I forgot to add one expression to an if-statement, causing an infinite number of pages to be printed.

**[85939788](https://github.com/freeplane/freeplane/commit/85939788a21f802bbdf5f408f97c1ca06a075f79)** (2014-02-11) — Fix method to clear image

> The background image URI property is now reset by removing the background image URI property key instead of using a constant.

**[feb31153](https://github.com/freeplane/freeplane/commit/feb3115308d964f114bdc40e548a02a3e42cf311)** (2014-02-11) — Add functionality to draw viewer component behind all nodes

> As Dimitry pointed out, I called the viewer component's paint method directly from MapView's paintComponent method. Moreover, I did some minor refactoring. In NodeView's paintComponent method, there were two switch statements in a row with the same switch expression, but is there a specific reason for that? (I merged them into one).

**[2a8396b5](https://github.com/freeplane/freeplane/commit/2a8396b5365f7f1eb1655c8a6598ea7b4ea4b683)** (2014-02-09) — Add SVG support (in progress)

> The image is rendered on top of the nodes. Moreover, I have yet to address the other issues mentioned.

**[4ec02d29](https://github.com/freeplane/freeplane/commit/4ec02d29cd52f2740c0f3765634b35da30d087f9)** (2014-02-02) — Add a way to select and display a background image

> This is a rough attempt at the feature mentioned above.


---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-12-28 | `fix` | #2080: fix issues with empty/invalid auto.mmfilter | `AFilterComposerDialog.java`, `FilterController.java` | [41e8a731](https://github.com/freeplane/freeplane/commit/41e8a731398e02efa7a95b6d87115e73c257a004) |
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [62e125b3](https://github.com/freeplane/freeplane/commit/62e125b331c29ae0c3962a3b0d27e0342bcc18ee) |
| 2013-12-26 | `feature` | 1. Re-implementation of Lynn C. Rees' pull request (https://github.com/freeplane/freeplane | `AddOnProperties.java`, `installScriptAddOn.groovy` +6 | [2c986d3a](https://github.com/freeplane/freeplane/commit/2c986d3abd50356b5bf63f28fb97347deb0cf4e3) |
| 2013-11-28 | `fix` | fix about_text | `Resources_it.properties`, `Resources_nl.properties` | [e172772b](https://github.com/freeplane/freeplane/commit/e172772b5013ee357413d2e212c53ee8d4c2d7d9) |
| 2013-11-28 | `fix` | fix license text | `Resources_it.properties`, `Resources_ja.properties` +3 | [b52711b5](https://github.com/freeplane/freeplane/commit/b52711b5a7c83f0ff58631c42f683e3f1e4d220f) |
| 2013-11-23 | `fix` | extended logging to analyze bug 2070: SEVERE: Can't set the value:com.sun.java.swing.plaf. | `ComboProperty.java` | [62574d7b](https://github.com/freeplane/freeplane/commit/62574d7bc05c2dcf8183e50c79d48a3a9b2828e7) |
| 2013-11-16 | `fix` | Quick fix for Menu Hyperlinks | `MenuBuilder.java`, `LinkController.java` | [5f38e9bb](https://github.com/freeplane/freeplane/commit/5f38e9bb25955f3cd4b1e1671690bfe2214370cc) |
| 2013-11-10 | `feature` | hack: allow to enter external http and https urls in add / change external image dialog | `AddExternalImageAction.java`, `ChangeExternalImageAction.java` +3 | [07f0e24f](https://github.com/freeplane/freeplane/commit/07f0e24f6b0bd49191d7086d6957820a2a29f0ea) |
| 2013-11-03 | `feature` | add more logging for UrlManager to get more information for stack trace: java.lang.NullPoi | `UrlManager.java` | [6a660e58](https://github.com/freeplane/freeplane/commit/6a660e589e6575b2d0375754426ea47798a572c6) |
| 2013-11-02 | `feature` | add port to map base url | `AppletViewController.java` | [9d08c05a](https://github.com/freeplane/freeplane/commit/9d08c05a14da2cbc644869226ce1deab4d40669b) |
| 2013-11-01 | `fix` | bug fix: edge was output twice | `EdgeBuilder.java` | [7f4eefee](https://github.com/freeplane/freeplane/commit/7f4eefee8fb9208c41199a1f2bcc0279398d35d4) |
| 2013-11-01 | `fix` | fix applet export issues | `ExportWithXSLT.xml`, `exportmm2appletmm.xsl` +3 | [f8b37da9](https://github.com/freeplane/freeplane/commit/f8b37da931ac20e8e4c1a7bcf32d70b90cf92d1a) |
| 2013-10-29 | `fix` | Fix: XML parsing errors are not catched if occurring within PCDATA. | `ContentReader.java`, `StdXMLBuilder.java` | [f39a17a1](https://github.com/freeplane/freeplane/commit/f39a17a1e5ae1ca487703894a1f94c49f5df3d1f) |
| 2013-10-28 | `feature` | [Bugs 0002063]: MacOS X: error and data loss saving files on network share (not if file is | `MFileManager.java` | [008a7f03](https://github.com/freeplane/freeplane/commit/008a7f0314f5303ee8764133f1a405456a9401df) |
| 2013-10-28 | `fix` | fix bug when pressing pos1 on a LaTeX node | `EditNodeBase.java` | [800aa94d](https://github.com/freeplane/freeplane/commit/800aa94d3443b53e08addec9d22cd6f034159869) |
| 2013-10-24 | `fix` | fix (force) single instance mode on Linux and Windows (fix BindException on Linux, on W7Pr | `SingleInstanceManager.java` | [90bc64de](https://github.com/freeplane/freeplane/commit/90bc64de578f62b3ccfe60d20a0c46823db4a4f5) |
| 2013-10-24 | `fix` | fix (force) single instance mode on Linux and Windows (fix BindException on Linux, on W7Pr | `SingleInstanceManager.java` | [95262526](https://github.com/freeplane/freeplane/commit/952625263d734385cb60bee267f5334a7b09664b) |
| 2013-10-18 | `fix` | bug fix: generation of temporary file names for cached images should be synchronized | `BitmapViewerComponent.java` | [ffea7d3b](https://github.com/freeplane/freeplane/commit/ffea7d3b9a1cafc9116610070dbcd032184f702e) |
| 2013-10-15 | `fix` | fix local applets in java 7u40 | `AppletViewController.java` | [c5a7420c](https://github.com/freeplane/freeplane/commit/c5a7420ceef02708ad4f3e6cd0de6894ba8fd56b) |
| 2013-10-15 | `fix` | Minor fix to German translation: "Editieren" -> "Bearbeiten". | `Resources_de.properties` | [72408a7c](https://github.com/freeplane/freeplane/commit/72408a7c1210234b6a025d18da6003ad60112fce) |
| 2013-10-15 | `fix` | Minor fix to German translation: "Editieren" -> "Bearbeiten". | `Resources_de.properties` | [72cf22cf](https://github.com/freeplane/freeplane/commit/72cf22cf6d7c8f53b98bdf33a520582eafbb7a73) |
| 2013-10-06 | `fix` | Fix: "attribute contains" only tests first attribute with this name. | `AttributeContainsCondition.java` | [63fc60c6](https://github.com/freeplane/freeplane/commit/63fc60c656a75781c50028612c3de0855e072ec9) |
| 2013-10-05 | `fix` | Fix for the setAnchorId bug | `MLinkController.java`, `HeadlessMModeControllerFactory.java` +3 | [b26ee702](https://github.com/freeplane/freeplane/commit/b26ee7024e8e0b59b664133b31be658455a90fe2) |
| 2013-09-29 | `fix` | fix saving page size in user properties | `PrintController.java` | [3e4cfc33](https://github.com/freeplane/freeplane/commit/3e4cfc334ec270a298a0084107afd0e647b938a3) |
| 2013-09-28 | `fix` | bug fix: map view was not added to applet scroll pane | `AppletViewController.java`, `FreeplaneApplet.java` | [81e18034](https://github.com/freeplane/freeplane/commit/81e18034d25a933314fb8d02afe569e56c7bab9f) |
| 2013-09-28 | `feature` | add port to map base url | `AppletViewController.java` | [85d87d8b](https://github.com/freeplane/freeplane/commit/85d87d8bbd8dc79369ccdaf780ee9759ce337c0c) |
| 2013-09-09 | `feature` | - make version.properties the default add-on version file - refactorings | `FreeplaneVersion.java`, `AddOnProperties.java` +3 | [6325b562](https://github.com/freeplane/freeplane/commit/6325b56206f90704695f01a27e362b21d8edb5e3) |
| 2013-09-04 | `feature` | New: ResourceController.getResourceStream(): open resource as InputStream. | `ResourceController.java` | [743b5d6e](https://github.com/freeplane/freeplane/commit/743b5d6e0a54b0cb87c8ced38cfbc56bc25af310) |
| 2013-08-25 | `fix` | bug fix in NodeView.requestFocusInWindow() : do not scroll if the focus can not be request | `MapView.java`, `NodeView.java` | [61b7a0d9](https://github.com/freeplane/freeplane/commit/61b7a0d98bf3b19b636732e8c5ca006ca6208147) |
| 2013-08-25 | `fix` | try to fix NPE in quit : consider map in close | `MapController.java`, `MMapController.java` +1 | [5e4e7fc1](https://github.com/freeplane/freeplane/commit/5e4e7fc107f9d38d91b4d0ec67eb76f12317d2b8) |
| 2013-08-25 | `fix` | fix NPE | `AddExternalImageAction.java` | [d0753c19](https://github.com/freeplane/freeplane/commit/d0753c1970851656bd705c8ca3d766f3a67a2f95) |
| 2013-08-25 | `fix` | fix NPE | `MainView.java` | [966d2435](https://github.com/freeplane/freeplane/commit/966d243587990bbe9a7f36cca6b03059af5d6be0) |
| 2013-08-25 | `fix` | fix NPE | `DefaultNodeKeyListener.java` | [33b24722](https://github.com/freeplane/freeplane/commit/33b24722b89b7c928d104b79c468bd54626c618e) |
| 2013-08-13 | `feature` | support for new properties : downloadUrl and changelogUrl | `AddOnProperties.java`, `HttpVersionClient.java` +1 | [21d6b2d6](https://github.com/freeplane/freeplane/commit/21d6b2d669c6a40a8a00ec328a64bbbf191dbbe6) |
| 2013-08-13 | `feature` | basic support for .properties file format | `HttpVersionClient.java` | [48535112](https://github.com/freeplane/freeplane/commit/48535112707d584dee87a4ebca94769731d59a9e) |
| 2013-08-13 | `feature` | handling undefined 'homepage' for add-ons | `AddOnProperties.java`, `UpdateCheckAction.java` +1 | [27d5a422](https://github.com/freeplane/freeplane/commit/27d5a422e3ba53e8ffc01a64762f6f13d571b434) |
| 2013-08-12 | `feature` | Try to enable transparency in the splash | `FreeplaneSplashModern.java` | [f599d542](https://github.com/freeplane/freeplane/commit/f599d54211bfcd00f72ddce4d3fc1c752c78c0d2) |
| 2013-08-04 | `feature` | fixed a switch between two buttons (add-on homepage vs add-on update-url) | `UpdateCheckAction.java` | [a0b4fd4c](https://github.com/freeplane/freeplane/commit/a0b4fd4c137ccd57442d34a2ae7d4129804a5555) |
| 2013-08-03 | `feature` | Add prefs option for common/global LaTeX macros | `Resources_de.properties`, `OptionPanelBuilder.java` +9 | [59bad5cd](https://github.com/freeplane/freeplane/commit/59bad5cd722f50340e02287e949c281fb554b472) |
| 2013-07-31 | `feature` | added add-ons update check to updater | `UpdateCheckAction.java`, `Resources_en.properties` | [04aa179a](https://github.com/freeplane/freeplane/commit/04aa179a21d9377911743e58d0812a6d93eb1add) |
| 2013-07-28 | `feature` | Scripting/other languages: * new configuration options:   - script_compilation_disabled_ex | `Resources_de.properties`, `Resources_en.properties` +10 | [2e24f90d](https://github.com/freeplane/freeplane/commit/2e24f90d20f9f3025c4910a675c48fce88cb644f) |
| 2013-07-28 | `feature` | store the last version of an add-on | `AddOnProperties.java` | [ca2858d9](https://github.com/freeplane/freeplane/commit/ca2858d98e86f4f414e91c670eb70a4a76abf7f5) |
| 2013-07-27 | `feature` | added updateUrl property to be abble to check for newer add-ons versions | `AddOnProperties.java` | [794432e1](https://github.com/freeplane/freeplane/commit/794432e16d9c30c7097f700e22148341f3d22221) |
| 2013-07-01 | `api_change` | scripting API for map specific storage | `history_en.txt`, `MapStyle.java` +3 | [8085eff2](https://github.com/freeplane/freeplane/commit/8085eff229490b889722ed5f47071bee8affd8be) |
| 2013-06-30 | `api_change` | scripting API for encrypted nodes refactored EncryptionController to remove direct Swing r | `history_en.txt`, `EncryptionController.java` +7 | [324ee6f1](https://github.com/freeplane/freeplane/commit/324ee6f16aee4c25806e3fbca2255029e19154cb) |
| 2013-06-27 | `feature` | new splash | `intuitive-subset.ttf`, `Freeplane_splash.png` +1 | [4bb25ad3](https://github.com/freeplane/freeplane/commit/4bb25ad3b741ed50467a3ff4fc18329ac21732d1) |
| 2013-06-22 | `fix` | fix error message on not found url | `UrlManager.java` | [4aee587d](https://github.com/freeplane/freeplane/commit/4aee587d4829e8e381823d648530606f1dd76d9e) |
| 2013-06-04 | `feature` | Add a Mindmap representing the current `browsemode` menu structures. | `.gitignore`, `build.xml` +2 | [7cfd05dd](https://github.com/freeplane/freeplane/commit/7cfd05dd176807f5aa75a7ffd82512c288a41855) |
| 2013-06-04 | `feature` | Add some descriptions to the menu mind-maps and enhance styles. | `filemodemenu.mm`, `mindmapmodemenu.mm` +1 | [dc09b4d7](https://github.com/freeplane/freeplane/commit/dc09b4d7348f9f3f5f660a5d64f177ae4556d20d) |
| 2013-06-03 | `feature` | Add ant-tasks to build `preferences.xml` and `*menu.xml` from Mindmap. | `build.xml`, `filemodemenu.xml` +3 | [f8484729](https://github.com/freeplane/freeplane/commit/f84847296101293fd420c0858892a2c632bc18ca) |
| 2013-06-02 | `feature` | Add a Mindmaps representing the current menu structures. | `build.xml`, `filemodemenu.mm` +2 | [a67f66c3](https://github.com/freeplane/freeplane/commit/a67f66c350e92086624fafabb59a83cf3cc20ffa) |
| 2013-06-02 | `feature` | Add a Mindmap representing the current preferences structure. | `build.xml`, `preferences.mm` | [60b081e2](https://github.com/freeplane/freeplane/commit/60b081e28aeabb5ea33dde8973f2d7a7ed7b708a) |
| 2013-06-02 | `fix` | bug fixes for docking windows | `MapViewDockingWindows.java` | [91c2fbd1](https://github.com/freeplane/freeplane/commit/91c2fbd1de514c35a0089d83eda2064e677f2f19) |
| 2013-06-01 | `feature` | Read CSS stylesheet for HTML from a new resource `/html/folding.css`. | `folding.css`, `MindMapHTMLWriter.java` | [453b647a](https://github.com/freeplane/freeplane/commit/453b647acd107ebd562ed30262ed759bee206900) |
| 2013-06-01 | `feature` | Read javascript for folding HTML from a new resource `/html/folding.js`. | `folding.js`, `MindMapHTMLWriter.java` | [a0699664](https://github.com/freeplane/freeplane/commit/a069966464f35d9b80a782fb71cc5adb7ea80fc4) |
| 2013-06-01 | `feature` | New: FileUtils.slurpResource(): read resource into a string. | `FileUtils.java` | [1adcdeab](https://github.com/freeplane/freeplane/commit/1adcdeab23eae8e22a9df858517ffd3be18fb788) |
| 2013-05-31 | `fix` | Fix: oowriter exporter is listed twice in export dialog. | `export2oowriter.manifest.xsl`, `export2oowriter.styles.xsl` +2 | [8d603fc4](https://github.com/freeplane/freeplane/commit/8d603fc40447fcc52462aa65f4cdc9dabbed1025) |
| 2013-05-27 | `fix` | Fix: jgoodies 1.4 no longer accepts RowSpec(string) constructor. | `KeyProperty.java` | [886b5cfc](https://github.com/freeplane/freeplane/commit/886b5cfc5cdf82d3e85397c954a778abc243c2d4) |
| 2013-05-16 | `fix` | Fix additional margins around paragraphs for rich-text-nodes in XHMTL. | `treestyles.css` | [731f7b8c](https://github.com/freeplane/freeplane/commit/731f7b8cabe0142bf3647547be256e937aaf3371) |
| 2013-05-15 | `feature` | Last Opened Maps list : - remove ":" after "Mindmap" label - add space between label and M | `LastOpenedList.java` | [956f5436](https://github.com/freeplane/freeplane/commit/956f5436c8eac25a89b9ceeb4969d83778fafa32) |
| 2013-05-03 | `fix` | fix NPE | `NodeTooltipManager.java` | [42b665a3](https://github.com/freeplane/freeplane/commit/42b665a3385f36a860e1d26c79ba500f8bc97fbe) |
| 2013-05-01 | `fix` | fix loading of user XSLT export scripts by looking for user scripts first (and ignoring ex | `ExportController.java`, `XsltExportEngine.java` +1 | [d645682a](https://github.com/freeplane/freeplane/commit/d645682aa122bdd1168b62e3cb6dd806c681f41c) |
| 2013-05-01 | `fix` | bug fix in setting view tab titles | `FrameController.java`, `ViewController.java` +8 | [09050a4f](https://github.com/freeplane/freeplane/commit/09050a4f67d5dba409bc8c121c423d2fcd435319) |
| 2013-04-30 | `fix` | fix NPE | `DefaultMapMouseListener.java` | [248eb2c0](https://github.com/freeplane/freeplane/commit/248eb2c07221494652ae350febcff11186e72394) |
| 2013-04-30 | `fix` | bug fix for reload / close map | `MapViewDockingWindows.java` | [14a22391](https://github.com/freeplane/freeplane/commit/14a2239114c5454ef23195597030b9a9cd7a6bb5) |
| 2013-04-29 | `fix` | fix memory leaks and saving of last maps | `UITools.java`, `FrameController.java` +6 | [a317a7bc](https://github.com/freeplane/freeplane/commit/a317a7bc0a2ad77aad585d18944bd29d8bb81756) |
| 2013-04-24 | `feature` | Add space in Recent Files List to improve readability | `LastOpenedList.java` | [a5aa1d89](https://github.com/freeplane/freeplane/commit/a5aa1d89b2e64bae67d3e32bcdc00ae640a02c16) |
| 2013-04-21 | `feature` | place new internal frames at different locations | `MapViewFrames.java` | [e8492997](https://github.com/freeplane/freeplane/commit/e8492997f2bd28cbb5c124a6032eb96af2021627) |
| 2013-04-20 | `feature` | add menu selection to popup menu | `browsemodemenu.xml`, `filemodemenu.xml` +5 | [5cfa7fd9](https://github.com/freeplane/freeplane/commit/5cfa7fd9c8248415145abc1d8d85432741f567be) |
| 2013-04-15 | `fix` | fix NPE in headless mode | `FilterController.java` | [b5334a70](https://github.com/freeplane/freeplane/commit/b5334a70fa2c6337758fff513a56bf1737b44e43) |
| 2013-04-13 | `feature` | merge workspace into freeplane/master | `.project`, `.project` +206 | [d91f421e](https://github.com/freeplane/freeplane/commit/d91f421e91cb3746577290e87e8a016462783cdd) |
| 2013-03-31 | `feature` | fix #1929: use LinkController.loadURL() instead of URLManager.loadURL() to support hyperli | `LinkController.java`, `AttributeTable.java` | [dcc6402a](https://github.com/freeplane/freeplane/commit/dcc6402a731456b15ddf37af328add35db5e4e1f) |
| 2013-03-31 | `feature` | fix #1929: use LinkController.loadURL() instead of URLManager.loadURL() to support hyperli | `LinkController.java`, `AttributeTable.java` | [7b99c4c5](https://github.com/freeplane/freeplane/commit/7b99c4c50cda5696a8d36b4fd66b81c74b0ef705) |
| 2013-03-31 | `fix` | fix compiler warnings (unused imports, variables) | `AFreeplaneAction.java`, `AccelerateableAction.java` +16 | [0833b405](https://github.com/freeplane/freeplane/commit/0833b4059009f88fb523ff7a82ab07ccb7fe8b0c) |
| 2013-03-23 | `feature` | add command line option -U <userdir> | `Compat.java`, `CommandLineParser.java` +1 | [5a90bbe3](https://github.com/freeplane/freeplane/commit/5a90bbe3e8a4f631f4943eeb036b4a6fe6f25957) |
| 2013-03-23 | `feature` | Create actions for named filters in Filter menu | `mindmapmodemenu.xml`, `ApplyNamedFilterAction.java` +5 | [46ee4855](https://github.com/freeplane/freeplane/commit/46ee48557d9be5e4b427490d6cb0be7c08d99a24) |
| 2013-03-12 | `fix` | fix javadoc warning | `MenuUtils.java` | [dbe9b552](https://github.com/freeplane/freeplane/commit/dbe9b5529d475aac0d7bcfbaf70e5f406683dc0b) |
| 2013-03-11 | `api_change` | merged from master: scripting API documentation improvements | `MenuUtils.java`, `build.xml` +2 | [72ee848d](https://github.com/freeplane/freeplane/commit/72ee848d04da65d52cd2137a6600a09e2929ffa2) |
| 2013-03-11 | `api_change` | scripting API documentation improvements | `MenuUtils.java`, `build.xml` +2 | [25ee5ed4](https://github.com/freeplane/freeplane/commit/25ee5ed4dbc4fe1eada624606dcab1c6fd042007) |
| 2013-03-10 | `fix` | fix focusing of editor field in find dialog in Mac / Browser: use requestFocusInWindow ins | `FilterConditionEditor.java`, `FindAction.java` | [ff34cb94](https://github.com/freeplane/freeplane/commit/ff34cb946b6b07f3276258131cabf95bfc5735ef) |
| 2013-03-10 | `fix` | fix doc comments | `FormattedFormula.java` | [0b3bb83f](https://github.com/freeplane/freeplane/commit/0b3bb83f015b6551fdfce7ecfabedccc17459a84) |
| 2013-03-09 | `fix` | fix: ignore conditional styles if their conditions can not be created ( it can happen in a | `MapStyle.java` | [f5ca1feb](https://github.com/freeplane/freeplane/commit/f5ca1feb317a76271cb62758b71ed99ab74f01a9) |
| 2013-03-09 | `fix` | fix node tool tip issues | `NodeTooltip.java`, `NodeTooltipManager.java` | [e175c197](https://github.com/freeplane/freeplane/commit/e175c197d9a46d85c82245f4814ab51abeaa1119) |
| 2013-02-22 | `feature` | new app icons | `Freeplane_frame_icon.png`, `ApplicationViewController.java` +2 | [42ca2bea](https://github.com/freeplane/freeplane/commit/42ca2bea70bb0e2d225cafecad79ab917fbc0704) |
| 2013-02-21 | `feature` | - add top button to add-on installer - move malware warning to top and make red - adjust t | `Resources_de.properties`, `Resources_el.properties` +14 | [c802f03f](https://github.com/freeplane/freeplane/commit/c802f03f2456cc0031d7740e6033c99f6f0d7ca4) |
| 2013-02-16 | `fix` | fix class cast exception | `ExportDialog.java` | [bdc831df](https://github.com/freeplane/freeplane/commit/bdc831dfd8138d53b4caf92fbc9a30a8c7ea14a8) |
| 2013-02-12 | `fix` | fix typo showAnchestors -> showAncestors (thanks to kunkel321) | `Filter.java`, `MapView.java` +2 | [6d921264](https://github.com/freeplane/freeplane/commit/6d9212640cc1ff3a54be9bafe10518a1dbd9d89c) |
| 2013-02-03 | `fix` | fix script errors  on CopySingle: use a decorator class SingleCopySource for hidding child | `ClipboardController.java`, `SingleCopySource.java` +2 | [0cf42a53](https://github.com/freeplane/freeplane/commit/0cf42a5351f0457a496273bfb72dac984a3250bb) |
| 2013-01-26 | `fix` | bug fix: remove Tabbed Pane Accelerators (JDK 7) | `MapViewTabs.java` | [4cf524a2](https://github.com/freeplane/freeplane/commit/4cf524a22aa7499d864cc43e9c3c2a147dcf4075) |
| 2013-01-13 | `feature` | #1859: allow using \uFFFF escape sequences in add-ons to circumvent all encoding issues | `AddOnsController.java` | [fa73d64d](https://github.com/freeplane/freeplane/commit/fa73d64d71402bd04a10c8d5d16f8e3c938b1b24) |
| 2013-01-09 | `fix` | fix unfold level actions if some children are hidden | `FoldingController.java` | [9e507256](https://github.com/freeplane/freeplane/commit/9e50725672256d7836083afb563614af412650c7) |
| 2013-01-01 | `feature` | Add @AllowedDuringEditing annotation to some actions | `AboutAction.java`, `DocumentationAction.java` +7 | [378805eb](https://github.com/freeplane/freeplane/commit/378805ebcec4b1235e38bcabb7ce56c008f20da4) |

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

**[f39a17a1](https://github.com/freeplane/freeplane/commit/f39a17a1e5ae1ca487703894a1f94c49f5df3d1f)** (2013-10-29) — Fix: XML parsing errors are not catched if occurring within PCDATA.

> E.g. in "<script>x&;</script>" resulted in an empty PCData, the
> error silently ignored.

**[63fc60c6](https://github.com/freeplane/freeplane/commit/63fc60c656a75781c50028612c3de0855e072ec9)** (2013-10-06) — Fix: "attribute contains" only tests first attribute with this name.

> This effects filtering and conditional styles.
> 
> Was introduced by 2012-02-11T18:25:21Z!felix@bitburger.home.felix.

**[743b5d6e](https://github.com/freeplane/freeplane/commit/743b5d6e0a54b0cb87c8ced38cfbc56bc25af310)** (2013-09-04) — New: ResourceController.getResourceStream(): open resource as InputStream.

> This is a common pattern all over at least xslt-handling.

**[7cfd05dd](https://github.com/freeplane/freeplane/commit/7cfd05dd176807f5aa75a7ffd82512c288a41855)** (2013-06-04) — Add a Mindmap representing the current `browsemode` menu structures.

> Includes an ant-task for building and cleaning and a gitignore-line.

**[dc09b4d7](https://github.com/freeplane/freeplane/commit/dc09b4d7348f9f3f5f660a5d64f177ae4556d20d)** (2013-06-04) — Add some descriptions to the menu mind-maps and enhance styles.

> These have not been translated when processing by a script in
> 2013-06-02T20:33:14Z!h.goebel@crazy-compilers.com.

**[a67f66c3](https://github.com/freeplane/freeplane/commit/a67f66c350e92086624fafabb59a83cf3cc20ffa)** (2013-06-02) — Add a Mindmaps representing the current menu structures.

> The mindmap was generated using helper-xslt for building a mind-map
> out of ´*menu.xml`, texts have been inserted from
> translations/Resources_en.properties (using a script) and styles have
> been added.
> 
> The result as generated by
>   xsltproc freeplane/ant/mm2menu.xsl \
>     freeplane/resources/xml/$menu.mm \
>     > freeplane/resources/xml/$menu.xml
> (with $menu being one of mindmapmodemenu, filemodemenu, stylemodemenu)
> has been verified to result in the same file as the current
> `$menu.xml`.
> 
> Also add a build-rule to not include the mindmaps in the distribution.

**[60b081e2](https://github.com/freeplane/freeplane/commit/60b081e28aeabb5ea33dde8973f2d7a7ed7b708a)** (2013-06-02) — Add a Mindmap representing the current preferences structure.

> The mindmap was generated using helper-xslt for building a mind-map
> out of ´preferences.xml`, texts have been inserted from
> translations/Resources_en.properties (using a script) and styls have
> been added.
> 
> The result as generated by
>  xsltproc freeplane/ant/mm2preferences.xsl \
>     freeplane/resources/xml/preferences.mm \
>     > freeplane/resources/xml/preferences.xml
> has been verified to result in the same file as the current
> `preferences.xml`.
> 
> Also add a build-rule to not include this file in the distribution.

**[1adcdeab](https://github.com/freeplane/freeplane/commit/1adcdeab23eae8e22a9df858517ffd3be18fb788)** (2013-06-01) — New: FileUtils.slurpResource(): read resource into a string.

> Also introduce a prvate method FileUtilsl.slurp() for reading
> data from any Reader into a string.

**[8d603fc4](https://github.com/freeplane/freeplane/commit/8d603fc40447fcc52462aa65f4cdc9dabbed1025)** (2013-05-31) — Fix: oowriter exporter is listed twice in export dialog.

> This is caused by XsltExportEngineFactory, which includes all
> files matching "mm2([\w]+)\.xsl" into the export list. While this is
> conveniant, exporting only the content.xml of a ODT is quite useless.
> 
> Renaming `mm2oowriter*.xslt to `export2oowriter*.xsl` solves this.

**[886b5cfc](https://github.com/freeplane/freeplane/commit/886b5cfc5cdf82d3e85397c954a778abc243c2d4)** (2013-05-27) — Fix: jgoodies 1.4 no longer accepts RowSpec(string) constructor.

> The constructur which is now used is valid for jgoodies 1.2 and 1.4.

**[731f7b8c](https://github.com/freeplane/freeplane/commit/731f7b8cabe0142bf3647547be256e937aaf3371)** (2013-05-16) — Fix additional margins around paragraphs for rich-text-nodes in XHMTL.

> This solves issue #1979.

**[956f5436](https://github.com/freeplane/freeplane/commit/956f5436c8eac25a89b9ceeb4969d83778fafa32)** (2013-05-15) — Last Opened Maps list : - remove ":" after "Mindmap" label - add space between label and MindMap path.

> Benefits : more easy to read for user (space added), less caracters (":"
> removed), multi-linguale support (for instance in french one should
> write : "map : c:\..." and in english "map: c:\...")

**[d91f421e](https://github.com/freeplane/freeplane/commit/d91f421e91cb3746577290e87e8a016462783cdd)** (2013-04-13) — merge workspace into freeplane/master

> -initial version of the new workspace as used for docear


---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-25 | `feature` | Refactor: add method ModeController.isHeadless | `FoldingController.java`, `ModeController.java` +2 | [5b8837de](https://github.com/freeplane/freeplane/commit/5b8837de42ea91c44979a3e50fd68d82f309355b) |
| 2012-12-25 | `fix` | Run tests and fix issues | `MANIFEST.MF`, `FoldingController.java` +10 | [8dd6a47f](https://github.com/freeplane/freeplane/commit/8dd6a47ff18ac70ef6936863c724b616f2192d5c) |
| 2012-12-25 | `feature` | Create headless package. The headless worker thread and executor are maintained in Headles | `UndoHandler.java`, `FrameController.java` +8 | [597493e7](https://github.com/freeplane/freeplane/commit/597493e7db05ac58556af9e67070f90bd7a3b97d) |
| 2012-12-24 | `api_change` | convert FreeplaneStarter to interface | `Controller.java`, `ApplicationResourceController.java` +8 | [55ce224b](https://github.com/freeplane/freeplane/commit/55ce224b3fe41539b712ff29c7de9c8d92b51cbd) |
| 2012-12-24 | `api_change` | Use interface instead of a class in Controller | `Controller.java`, `ToggleFullScreenAction.java` +1 | [2a50e9c4](https://github.com/freeplane/freeplane/commit/2a50e9c4628b7ea4bf10dad31c866e4efb88e76b) |
| 2012-12-24 | `api_change` | make ViewController an interface | `TypedListCellRenderer.java`, `UITools.java` +22 | [61e92a9c](https://github.com/freeplane/freeplane/commit/61e92a9c047737c355d284060b1d10e6db32f85c) |
| 2012-12-15 | `fix` | fix compiler warning | `SpellCheckerController.java` | [7e8f5270](https://github.com/freeplane/freeplane/commit/7e8f5270d9ed97e56dc44bc584f4659d5ea28b1f) |
| 2012-11-25 | `feature` | Add action to make scroll bars visible / not visible | `browsemodemenu.xml`, `filemodemenu.xml` +7 | [4efed239](https://github.com/freeplane/freeplane/commit/4efed239ce74bec5e134b722e542d9b2af973902) |
| 2012-11-23 | `feature` | "Add LaTeX formula...": replace by msgbox telling about deprecation of old LaTeX feature + | `Resources_de.properties`, `freeplane.properties` +5 | [73108439](https://github.com/freeplane/freeplane/commit/731084392c29d4dc42921e2094c32f1a2f49b5ee) |
| 2012-11-17 | `feature` | new splash with fonts Big Dog and Intuitive | `intuitive-license.txt`, `intuitive-subset.ttf` +4 | [f5d2fa43](https://github.com/freeplane/freeplane/commit/f5d2fa4353a2a6930820400626fe92bcd7d52f9a) |
| 2012-10-20 | `feature` | new splash using pecita font | `BPreplay Open Font License.txt`, `BPreplay.ttf` +2 | [720a42cf](https://github.com/freeplane/freeplane/commit/720a42cf46d88f59d7149ce30063b19ae4d67d94) |
| 2012-10-07 | `fix` | fix NPE | `NodeLinkModel.java` | [013649eb](https://github.com/freeplane/freeplane/commit/013649eb76e3474b7b936b02ea90aaa079304760) |
| 2012-10-01 | `fix` | fix NPE | `LockManager.java` | [2b94811b](https://github.com/freeplane/freeplane/commit/2b94811b1633ec549f2c82669f17ea7d80bd6534) |
| 2012-09-22 | `fix` | bug fixes in html map writer | `MindMapHTMLWriter.java` | [996f386e](https://github.com/freeplane/freeplane/commit/996f386edfee55453211ff37512381b5224ad084) |
| 2012-09-22 | `fix` | bug fix: do not cache styles set  by a  conditional style check | `ExclusivePropertyChain.java`, `LogicalStyleController.java` | [112ed9b5](https://github.com/freeplane/freeplane/commit/112ed9b57868a8327f6276bb68a5716dd2428739) |
| 2012-08-14 | `feature` | add integer version information to the map | `mapVersions.xml`, `LinkBuilder.java` +2 | [52894bb5](https://github.com/freeplane/freeplane/commit/52894bb5fabb6b43e365eea83472eb4be500bead) |
| 2012-08-12 | `fix` | fix class cast not found exception in applet | `DetailsViewMouseListener.java` | [8dcade13](https://github.com/freeplane/freeplane/commit/8dcade139b117cde65afba6428f32dbb87e5e180) |
| 2012-08-12 | `fix` | fix l10n properties : replace single '{0}' by double ''{0}'' in formatted strings | `Resources_de.properties`, `Resources_es.properties` +12 | [541921f0](https://github.com/freeplane/freeplane/commit/541921f0ae957ac97529f0ae357f4549f71a9793) |
| 2012-08-12 | `fix` | do not ask to submit bug reports for final versions, assume denied | `FreeplaneVersion.java`, `freeplane.properties` +1 | [40a488bc](https://github.com/freeplane/freeplane/commit/40a488bca434a355638451e7b07bdfd84266ec62) |
| 2012-08-09 | `fix` | fix shape for looped connectors on loading | `LinkBuilder.java` | [13a2ff7a](https://github.com/freeplane/freeplane/commit/13a2ff7a73b4d7d774016904f936b220a5753bc8) |
| 2012-08-01 | `fix` | fix java5 compatibility | `MenuBuilder.java` | [4459ccd4](https://github.com/freeplane/freeplane/commit/4459ccd46755e15f58a3cecf8410aff1ee1dc1ae) |
| 2012-07-19 | `feature` | ignore typed events for new nodes until a new key is pressed | `MTextController.java` | [4c31fc67](https://github.com/freeplane/freeplane/commit/4c31fc67edb6617755df615629d1d19994385424) |
| 2012-07-19 | `feature` | a better solution: allow all menu actions after new node is inserted | `MTextController.java` | [f57ea39c](https://github.com/freeplane/freeplane/commit/f57ea39c2b0739a22af42c752b5068cac27ed874) |
| 2012-07-19 | `feature` | use dialog based editor if edit long accelerator is pressed as first editing action for ne | `MTextController.java` | [9e517f2d](https://github.com/freeplane/freeplane/commit/9e517f2dd5bf1fa985acd4bd29fc2fd8d45f28e7) |
| 2012-07-17 | `feature` | 1743]: Strange ?buffering delay when editing new node | `EventBuffer.java` | [cf0a1c4c](https://github.com/freeplane/freeplane/commit/cf0a1c4c613c7da0a875b582697b3a0f4f21a1eb) |
| 2012-07-15 | `fix` | fix NPE in NodeWriter on encryption problems | `NodeWriter.java` | [9dd900f3](https://github.com/freeplane/freeplane/commit/9dd900f3cab82f459235e37a8771f1f5d64ecb6a) |
| 2012-07-15 | `feature` | support not ascii passwords for encryption | `DesEncrypter.java` | [70d835c6](https://github.com/freeplane/freeplane/commit/70d835c675b0139154d44f55c42bc90cdbc8c32f) |
| 2012-07-14 | `fix` | fix NPE I do not understand the reason for | `MMapController.java` | [905bc897](https://github.com/freeplane/freeplane/commit/905bc89783a926daa84556adf5468d41cbd8ae7c) |
| 2012-07-14 | `fix` | fix regex patterns in html 2 plain text | `HtmlUtils.java` | [5f239adb](https://github.com/freeplane/freeplane/commit/5f239adb4c3907061aab2eff1d0a21c33a3341f1) |
| 2012-07-08 | `fix` | fix note size on start | `MNoteController.java`, `ApplicationViewController.java` | [d4654058](https://github.com/freeplane/freeplane/commit/d465405847d36480caf924a3e8508e3a80d991dd) |
| 2012-07-02 | `fix` | fix NPE for not initialized node views | `MapView.java` | [d94e6543](https://github.com/freeplane/freeplane/commit/d94e65431e5b951777ca8873698fc1410ffb262a) |
| 2012-06-30 | `fix` | fix NPE | `NodeView.java` | [9cf3276d](https://github.com/freeplane/freeplane/commit/9cf3276d5d92d3776d42281c9c8e6c360c31d54c) |
| 2012-06-18 | `fix` | fix NPE | `FormatContentTransformer.java` | [ae0913c9](https://github.com/freeplane/freeplane/commit/ae0913c9cbe354dfa991b098f0134035dc52a467) |
| 2012-06-17 | `feature` | 1695: make it possible for file locks not to expire, or set the expiration time: In 1.2.15 | `LockManager.java`, `freeplane.properties` | [7c291171](https://github.com/freeplane/freeplane/commit/7c291171d80231627e4fefa7b51f2127204fed7d) |
| 2012-06-17 | `feature` | Implement selection state of JAutoRadioButtonMenuItem similar to JAutoCheckBoxMenuItem | `JAutoRadioButtonMenuItem.java` | [ffa98a72](https://github.com/freeplane/freeplane/commit/ffa98a72c888d2e547bce6006bf02715526cdc4b) |
| 2012-06-17 | `fix` | fix umlauts | `resource_de.properties`, `resource_es_MX.properties` | [80801e9e](https://github.com/freeplane/freeplane/commit/80801e9e3c7778ed9528d74d91c01d5609a7a0d7) |
| 2012-06-07 | `fix` | fix potential memory leak in simplyhtml 0.16.04 integration code | `MNoteController.java`, `EditNodeWYSIWYG.java` +2 | [c3a06f00](https://github.com/freeplane/freeplane/commit/c3a06f00d0e52d88773d3d6b1f65a5f32c605089) |
| 2012-06-02 | `feature` | add node style group if they are missing | `MapStyleModel.java`, `NewUserStyleAction.java` +1 | [48bf4966](https://github.com/freeplane/freeplane/commit/48bf496625dac273e436976e9e8695e8801831db) |
| 2012-06-02 | `feature` | fix: enable / disable actions only for active mode controller | `UserInputListenerFactory.java` | [c73b9cbb](https://github.com/freeplane/freeplane/commit/c73b9cbb998eff6824aaac27b450d79715a2db79) |
| 2012-05-27 | `fix` | do not reset values of filter editor on map change: auto bug report | `FilterConditionEditor.java` | [78fdeb4f](https://github.com/freeplane/freeplane/commit/78fdeb4f5b2e6214c6bef28be5d79683b37769cd) |
| 2012-05-27 | `fix` | fix java.awt.IllegalComponentStateException: component must be showing on the screen to de | `TimeComboBoxEditor.java` | [29fc2519](https://github.com/freeplane/freeplane/commit/29fc25192929afe3188c8c2aa4b509ce839a5160) |
| 2012-05-27 | `fix` | fix NPE | `NodeView.java` | [ff72fd73](https://github.com/freeplane/freeplane/commit/ff72fd73e7c4db7ed73f660a5a49a94e74ee2344) |
| 2012-05-27 | `feature` | 1661: New sys icons | `DeleteDetailsAction.png`, `EditDetailsInDialogAction.png` +3 | [a524cb8a](https://github.com/freeplane/freeplane/commit/a524cb8ac6eedf58c3711167f7eff04f2dee5e95) |
| 2012-05-27 | `feature` | enable scroll bars for selection of link target | `GlassPaneNodeSelector.java` | [5ea9732b](https://github.com/freeplane/freeplane/commit/5ea9732bbdc2f1d82571d086f10c73f6e81904b5) |
| 2012-05-26 | `feature` | enable / disable / select / deselect anchor related actions directly from controller | `AFreeplaneAction.java`, `ClearLinkAnchorAction.java` +4 | [dd9ff072](https://github.com/freeplane/freeplane/commit/dd9ff0722ddaf350f647c884036fac131d61d9b8) |
| 2012-05-22 | `fix` | Another fix for 1660]: Outline View is not working : pressing the button / menu item shoul | `ActionToggleButtonModel.java`, `ViewLayoutTypeAction.java` | [418807ac](https://github.com/freeplane/freeplane/commit/418807ac5c8b1c40bc686a701cc62c270424913a) |
| 2012-05-20 | `fix` | fix formatting of stringified numbers | `FormatController.java` | [a2335c4c](https://github.com/freeplane/freeplane/commit/a2335c4cf1a23a57664ec3fa31cb95e4ed6f4d08) |
| 2012-05-20 | `feature` | move PatternFormat.create to FormatController and properly implement creation of special f | `FormatController.java`, `PatternFormat.java` | [30a0deae](https://github.com/freeplane/freeplane/commit/30a0deae2b489e852fccf90b5a460312cebc5f77) |
| 2012-05-18 | `fix` | Fix painting of text rendering icons (e.g. latex) for zoomed maps | `ZoomableLabelUI.java` | [40fc7fcb](https://github.com/freeplane/freeplane/commit/40fc7fcbc59450d719d0095bd4739b3c9daf9b49) |
| 2012-05-17 | `fix` | fix NPE | `NodeView.java` | [a9eb2d43](https://github.com/freeplane/freeplane/commit/a9eb2d4387440c800c95db0bd749ead8911efcc9) |
| 2012-05-17 | `fix` | fix NPE and disable filter toolbar components if all maps are closed | `FilterConditionEditor.java`, `FilterController.java` +1 | [89103b79](https://github.com/freeplane/freeplane/commit/89103b7924b00d45945448b3b5051a261402be00) |
| 2012-05-17 | `fix` | fix paint folding circles over nodes | `MainView.java`, `NodeView.java` | [1221c49d](https://github.com/freeplane/freeplane/commit/1221c49d25f3841f3ce05da24912ca41f07112dd) |
| 2012-05-13 | `fix` | fix start of editing on typed character for characters entered using altGr | `DefaultNodeKeyListener.java` | [a99af342](https://github.com/freeplane/freeplane/commit/a99af3426808369ddd7e0884ba5aa4821b292bd4) |
| 2012-05-13 | `fix` | fix: send not shortened userObject to text trandformers in MainView.updateText | `MainView.java` | [a9869472](https://github.com/freeplane/freeplane/commit/a9869472b1a66da4622cb892cbf4a967af8d4f9c) |
| 2012-05-11 | `feature` | add creation of reminders to the scripting API | `ReminderExtension.java`, `ReminderHook.java` +3 | [94bc7aaf](https://github.com/freeplane/freeplane/commit/94bc7aafd3fab34aa55ce04b732ba27ce103f71c) |
| 2012-05-08 | `fix` | Fix mnemonics for JAutoCheckBoxMenuItem | `MenuBuilder.java`, `JAutoCheckBoxMenuItem.java` | [8d573641](https://github.com/freeplane/freeplane/commit/8d5736416ce1e66f14738b1e4aebf46745fedbb4) |
| 2012-05-06 | `fix` | fix highlight formulas for attributes | `AttributeTableCellRenderer.java` | [fc2ff401](https://github.com/freeplane/freeplane/commit/fc2ff40108c897453cbbafd51d3263a2de46fb12) |
| 2012-05-06 | `fix` | fix NPEs | `MapView.java`, `NodeView.java` | [b5b70379](https://github.com/freeplane/freeplane/commit/b5b7037902e49b003c7f613ce5d3ae11e750bc84) |
| 2012-05-06 | `fix` | fix FreeplaneStarter: select MindMapMode before updating user properties | `FreeplaneStarter.java` | [ff99e6e1](https://github.com/freeplane/freeplane/commit/ff99e6e1238f5bf7e181c4963ac059a0a2739866) |
| 2012-05-01 | `fix` | fix hotkey preset actions | `mindmapmodemenu.xml`, `LoadAcceleratorPresetsAction.java` +3 | [eae1d3f3](https://github.com/freeplane/freeplane/commit/eae1d3f31ffd6b4a554ce03aae40a0da09d73aa3) |
| 2012-05-01 | `feature` | Enable / select / set tooltips for anchor related actions automatically | `AFreeplaneAction.java`, `ClearLinkAnchorAction.java` +4 | [84a5ee2b](https://github.com/freeplane/freeplane/commit/84a5ee2b6de5d5a98d4f97698af4c494a71cda43) |
| 2012-05-01 | `fix` | fix in keeping selection on map view change | `MapView.java` | [66681a0b](https://github.com/freeplane/freeplane/commit/66681a0bff3f6aad54966dfb93c4b5439e811f36) |
| 2012-04-29 | `feature` | move "new summary" action to "new node" submenu | `mindmapmodemenu.xml` | [1edc8303](https://github.com/freeplane/freeplane/commit/1edc830349a2970e2970aedd010bc9753bd0c15e) |
| 2012-04-29 | `feature` | 1629]: Inline editor of new summary node doesn't appear automatically | `MMapController.java`, `NewSummaryAction.java` +1 | [870d92fa](https://github.com/freeplane/freeplane/commit/870d92faf3cb48a89c646fab839d8abad467403a) |
| 2012-04-27 | `fix` | fix rectangle around the formulas | `MainView.java` | [8d44ecb1](https://github.com/freeplane/freeplane/commit/8d44ecb19b3dd6b5faf4701d3e5d9aa2c1f444d4) |
| 2012-04-27 | `feature` | 1623: some words are missing in the traduction file : fix Add Attribute in Dialog action | `AddAttributeAction.java`, `Resources_en.properties` | [b36ab2fd](https://github.com/freeplane/freeplane/commit/b36ab2fdfdbfe75ca8b5d96af38e1a36c39350b9) |
| 2012-04-27 | `fix` | fix background color for printing in dimed mode | `MapView.java` | [186fe60f](https://github.com/freeplane/freeplane/commit/186fe60f9b4c708a27a1d9912c505c22ba3bb1bc) |
| 2012-04-26 | `fix` | fix print scaling, consider screen resolution | `MapView.java` | [debf33af](https://github.com/freeplane/freeplane/commit/debf33af859fcbab36f57e7cc5a81dce0355a12f) |
| 2012-04-25 | `fix` | try to fix NPE | `TimeComboBoxEditor.java` | [1d2fd5bd](https://github.com/freeplane/freeplane/commit/1d2fd5bddca0af5a6fe6eed0aa1f8264b7a79a0f) |
| 2012-04-22 | `fix` | Fix: ShowNextAction is @Enabled, not @Selectable | `ShowNextChildAction.java` | [c3b0c1ea](https://github.com/freeplane/freeplane/commit/c3b0c1ea8c74f1b682a90caf143ed6873048f28a) |
| 2012-04-22 | `fix` | bug fix on view insert | `NodeView.java` | [8f26d100](https://github.com/freeplane/freeplane/commit/8f26d1006a588dd3b2b19c259e2429f19538dbb2) |
| 2012-04-22 | `feature` | refactor: add new NodeView to parent component in the factory method | `NodeView.java`, `NodeViewFactory.java` | [41767ab8](https://github.com/freeplane/freeplane/commit/41767ab869989fdeb56fcb6811566822def5aa52) |
| 2012-04-22 | `feature` | refactoring for adding of new node views | `MapView.java`, `NodeView.java` +1 | [39f17a8f](https://github.com/freeplane/freeplane/commit/39f17a8f6fffc2b3da77b6543643f3914e647414) |
| 2012-04-20 | `fix` | 1610]: When using two "map views" the focus on the second one changes whe i delete node in | `MapView.java`, `NodeView.java` | [7d0079be](https://github.com/freeplane/freeplane/commit/7d0079be88b1d994a0598d147992fa5a83475c9f) |
| 2012-04-20 | `feature` | allow to add user identification to automatic bug reports, display "previous report" heade | `preferences.xml`, `freeplane.properties` +3 | [467eb5cc](https://github.com/freeplane/freeplane/commit/467eb5cca37ad795d68baf010425bd7be91bfb6e) |
| 2012-04-20 | `feature` | Fixes and extensions of the scripting API: | `FilterController.java`, `MapNavigationUtils.java` +5 | [f29a260e](https://github.com/freeplane/freeplane/commit/f29a260e41f44b11fac062b37628821870ef5e73) |
| 2012-04-20 | `feature` | - make Convertible support URLs - extend and fix unit test | `TextUtils.java`, `Convertible.java` +1 | [16f81087](https://github.com/freeplane/freeplane/commit/16f81087856e659448a3e8875146e71fea983649) |
| 2012-04-19 | `fix` | fix: keep focus on attribute table after editor is removed | `AttributeTable.java` | [bcca74f6](https://github.com/freeplane/freeplane/commit/bcca74f64f8827bb2b7634973c61b9f5f6675d4a) |
| 2012-04-18 | `fix` | auto bug fix for attribute editing | `AttributeTable.java` | [cc4c5657](https://github.com/freeplane/freeplane/commit/cc4c5657aeb3f391103901b5ec55e0eb2789e50e) |
| 2012-04-18 | `fix` | bug 1608: detail tooltip font | `TextController.java` | [d25f2457](https://github.com/freeplane/freeplane/commit/d25f24573ee10c4700efcc32ad0599d6d6a2e94b) |
| 2012-04-17 | `fix` | NPE : auto bug reports. Most problem related to maps with several views. | `MFileManager.java`, `MapView.java` +1 | [84d34950](https://github.com/freeplane/freeplane/commit/84d349500e991c470a03656ec88405678c4c2a1e) |
| 2012-04-15 | `feature` | Fixed two problems with attribute formatting/editing: | `AttributeTable.java` | [5fe4def6](https://github.com/freeplane/freeplane/commit/5fe4def60d170c55d7dc35e050ea0f4d392b7770) |
| 2012-04-15 | `fix` | fix NPE | `MMapController.java` | [f405b2d0](https://github.com/freeplane/freeplane/commit/f405b2d01c172513acd8e8f6a2824ab43f496234) |
| 2012-04-15 | `fix` | auto bug fix | `ChangeNodeLevelController.java` | [35ca39e2](https://github.com/freeplane/freeplane/commit/35ca39e2de6960dd979b4871b03ae2aea148f262) |
| 2012-04-15 | `fix` | fix selection for multiple map views | `ViewController.java`, `MapView.java` +1 | [1d54b1a3](https://github.com/freeplane/freeplane/commit/1d54b1a35826bfcf286f59112d8f456ea9f05804) |
| 2012-04-15 | `fix` | fix insertion of node views for multiple map view per map | `MapView.java`, `NodeView.java` +1 | [d8de40e0](https://github.com/freeplane/freeplane/commit/d8de40e09c12d5736e37d3e8bdeabff78ac71b06) |
| 2012-04-15 | `feature` | 1425: "Branch as New Map" ignores formatting : copy information from parent node if necess | `MCloudController.java`, `MEdgeController.java` +7 | [5eba784e](https://github.com/freeplane/freeplane/commit/5eba784e7a189198cf04f1326264696104da7b58) |
| 2012-04-13 | `fix` | fix action tick marks | `AccelerateableAction.java`, `IFreeplaneAction.java` +3 | [5a83210f](https://github.com/freeplane/freeplane/commit/5a83210f0eb2e9d4e0d013929abf5fe82d9caa5b) |
| 2012-04-13 | `fix` | fix UITools imports | `UITools.java` | [0cb59232](https://github.com/freeplane/freeplane/commit/0cb592326925f890f304a11ea992ffb0143a7a7e) |
| 2012-04-13 | `fix` | fix tooltip font sizes | `AttributeController.java`, `ModeController.java` +1 | [cc367d38](https://github.com/freeplane/freeplane/commit/cc367d38b2c5d73e157ab11c8ed2f72829aad135) |
| 2012-04-13 | `feature` | create a copy of ScaledStyleSheet in freeplane because of applet | `ScaledEditorKit.java`, `ScaledHTML.java` +2 | [a03e0cfc](https://github.com/freeplane/freeplane/commit/a03e0cfc59a415f4056ec0105e46198b93e2bdf8) |
| 2012-04-12 | `fix` | Fix default font sizes | `AttributeRegistry.java`, `NodeStyleController.java` +2 | [2045fb65](https://github.com/freeplane/freeplane/commit/2045fb65ac268a25e5a844e958e7ce7d9dd3eb95) |
| 2012-04-12 | `fix` | fix font size calculations | `SimplyHTML.jar`, `UITools.java` +4 | [cf1d95f5](https://github.com/freeplane/freeplane/commit/cf1d95f50fcb7ead42d75c31b41e77efde1ad45b) |
| 2012-04-11 | `fix` | bug fixes | `EditNodeWYSIWYG.java`, `MTextController.java` +2 | [8e967b99](https://github.com/freeplane/freeplane/commit/8e967b998ea64666df4f2ae2e55200107cdf0479) |
| 2012-04-10 | `fix` | Fix font sizes | `SimplyHTML.jar`, `UITools.java` +11 | [6eb547ae](https://github.com/freeplane/freeplane/commit/6eb547ae0780ad95fea5099733e69f97110792b6) |
| 2012-04-06 | `fix` | fix NPE | `UITools.java` | [1049f06e](https://github.com/freeplane/freeplane/commit/1049f06e90b60225b221820ddda247859aaaae84) |
| 2012-04-06 | `fix` | auto bug fix :catch exception | `MainView.java` | [040be1d4](https://github.com/freeplane/freeplane/commit/040be1d4ea3156a9b0e6dda162d7c7bb89e9339c) |
| 2012-04-06 | `fix` | 1578]: error message when numbering: Fix class cast exception for FormattedObject | `FormatContentTransformer.java` | [89ccb9b6](https://github.com/freeplane/freeplane/commit/89ccb9b6e9473a33af56aebf02abceb591e78236) |
| 2012-04-06 | `fix` | bug fix: initialize singleton | `IconStoreFactory.java` | [0ed24f75](https://github.com/freeplane/freeplane/commit/0ed24f757d919f142b865b68249265b29b17b665) |
| 2012-04-05 | `fix` | fix removeChildComponents for menus | `MenuBuilder.java` | [61957a38](https://github.com/freeplane/freeplane/commit/61957a38129245e9381b75243a22c59a2480c26e) |
| 2012-04-04 | `fix` | fix removeChildComponents for menus with extra submenus | `MenuBuilder.java` | [662212cc](https://github.com/freeplane/freeplane/commit/662212ccb009eabdcc99e2f0320b22208d087737) |
| 2012-04-03 | `feature` | basic version of four new actions to realize global links between mindmaps | `Resources_de.properties`, `mindmapmodemenu.xml` +6 | [339a0c9e](https://github.com/freeplane/freeplane/commit/339a0c9e7f0880108f9eca39c20184b11558742f) |
| 2012-04-01 | `feature` | add label "value format" to attribute formatting box | `AttributePanelManager.java`, `Resources_en.properties` | [9ca8d740](https://github.com/freeplane/freeplane/commit/9ca8d740de57959c505f54d0522fc7a3acc99916) |
| 2012-03-31 | `fix` | fix opening of mailto: links in applet | `AppletViewController.java` | [2e0fa22c](https://github.com/freeplane/freeplane/commit/2e0fa22c59a43932f781013e8c166c56ca90a6d2) |
| 2012-03-31 | `fix` | fix: increase folding mark painted area | `MainView.java` | [cd28592d](https://github.com/freeplane/freeplane/commit/cd28592d9c69b6d7fa93ffa83457d3ea0c4a65b3) |
| 2012-03-30 | `fix` | Fix mouse placement for big zoom values | `MNodeMotionListener.java` | [fa2e6a5f](https://github.com/freeplane/freeplane/commit/fa2e6a5f36afe27799b99f9ba4ef32edfa165386) |
| 2012-03-30 | `fix` | fix getLink for zoomed labels | `ZoomableLabel.java` | [a501e1ad](https://github.com/freeplane/freeplane/commit/a501e1ad5af5a8e9990da95939b945a560b69257) |
| 2012-03-30 | `fix` | fix layout of zoomed nodes: insets should always return unzoomed values | `ForkMainView.java`, `ZoomableLabelUI.java` | [5b089819](https://github.com/freeplane/freeplane/commit/5b0898194aed6aca3a85d6ee0a6c0a142b8f51db) |
| 2012-03-30 | `fix` | fix dragging: starting point is captured on mouse pressed event. | `MNodeMotionListener.java` | [2817749b](https://github.com/freeplane/freeplane/commit/2817749b8b35d7baf8b45116da200c8a80ab6a2c) |
| 2012-03-29 | `fix` | fix ZoomableLabelUI.layoutCL for zoomed maps | `ZoomableLabelUI.java` | [786d1611](https://github.com/freeplane/freeplane/commit/786d161171eeb1c5fcc3060b3500135bb9b2a06e) |
| 2012-03-29 | `fix` | fix dragging oval side for left nodes | `MainView.java` | [78dacb77](https://github.com/freeplane/freeplane/commit/78dacb77121c6f5c7072a3151760a59fe400f38c) |
| 2012-03-29 | `fix` | Bug fixes | `FoldingMark.java`, `MainView.java` +4 | [b10baabb](https://github.com/freeplane/freeplane/commit/b10baabbd287b148e3ad7acede2e87b058d9f217) |
| 2012-03-28 | `fix` | fix for concurrent access | `MapController.java` | [bafcd354](https://github.com/freeplane/freeplane/commit/bafcd3540c715d2d6e99686c4318018ec37149cb) |
| 2012-03-28 | `feature` | new german translation | `Resources_de.properties` | [fc149a8d](https://github.com/freeplane/freeplane/commit/fc149a8df7f800582acfef7cc2ff7d9e1c2bf01b) |
| 2012-03-27 | `fix` | fix: reset position only after double click on motion area | `MNodeMotionListener.java` | [70b0d824](https://github.com/freeplane/freeplane/commit/70b0d824dc8d08874f89c2f6f1c8fc265d3a43ce) |
| 2012-03-27 | `fix` | fix drag and drop | `MainView.java`, `DefaultNodeMouseMotionListener.java` +2 | [306878e2](https://github.com/freeplane/freeplane/commit/306878e2099f9359cfafd20c2311155abdd1f2fc) |
| 2012-03-26 | `feature` | Refactor: move FoldingMark to a new file | `FoldingMark.java`, `ForkMainView.java` +1 | [7d8ca910](https://github.com/freeplane/freeplane/commit/7d8ca9109613fc6d3bfd7b81f006282d1a684307) |
| 2012-03-23 | `fix` | fix menu: replace FindNextAction by QuickFindAction-s | `mindmapmodemenu.xml`, `appletMenu.xml` | [16e9e615](https://github.com/freeplane/freeplane/commit/16e9e61546edb8899030d986020b1574035b4b21) |
| 2012-03-23 | `fix` | update action enabled state on map change. Fix because of save action. | `MapController.java`, `LogicalStyleController.java` +2 | [7cdd9a72](https://github.com/freeplane/freeplane/commit/7cdd9a725eba11b44c66b7e2b07fa4d4a7f86e2b) |
| 2012-03-22 | `fix` | 1552]: dragging multiple images (png): Fix for Windows | `MClipboardController.java`, `ViewerController.java` | [4bca456c](https://github.com/freeplane/freeplane/commit/4bca456c27e444b47a167329208ec4df8a38e3b1) |
| 2012-03-17 | `feature` | enable documentation actions if there is no open map | `DocumentationAction.java` | [dbc2b152](https://github.com/freeplane/freeplane/commit/dbc2b1522467c22a15ddaa8f1fc6c7424c95b390) |
| 2012-03-17 | `fix` | fix NPE | `EditAttributesAction.java` | [9ddfd9dd](https://github.com/freeplane/freeplane/commit/9ddfd9dd3325c9093921a2401d2980949fc5279d) |
| 2012-03-17 | `fix` | fix NPE : do not evaluate isSelected() for disabled actions on popup opening | `MenuBuilder.java` | [2896b78d](https://github.com/freeplane/freeplane/commit/2896b78d949711ff71e915cb352fadd561258995) |
| 2012-03-16 | `fix` | fix scaling of external images | `.classpath`, `MANIFEST.MF` +2 | [c6e9c6e2](https://github.com/freeplane/freeplane/commit/c6e9c6e2807d4bf889d9eb4d5c6fcdd744e79c1f) |
| 2012-03-10 | `fix` | fix label of 'Save' button in FilterComposerDialog | `AFilterComposerDialog.java`, `Resources_en.properties` | [10e0f687](https://github.com/freeplane/freeplane/commit/10e0f687a835545dc6520bd1005049cef6bf1e48) |
| 2012-03-08 | `fix` | correct last change | `PropertyAction.java` | [a14923fa](https://github.com/freeplane/freeplane/commit/a14923fa68050589a5171912d9fc3586e5d0582e) |
| 2012-03-08 | `fix` | bug fix: AttributeCompareCondition for multivalued attributes | `AttributeCompareCondition.java` | [e8c137d2](https://github.com/freeplane/freeplane/commit/e8c137d251f04d8295ac5ea273dffa0e99cdfb5b) |
| 2012-03-07 | `feature` | New implementation of SummaryEdgePainter | `NodeView.java`, `SummaryEdgePainter.java` | [610da04f](https://github.com/freeplane/freeplane/commit/610da04ffef80a989ce77eb6361478f85e5f7940) |
| 2012-03-06 | `fix` | Fix default values of 'values' CB in filter toolbar | `IconConditionController.java`, `LinkConditionController.java` | [9651d8a0](https://github.com/freeplane/freeplane/commit/9651d8a0f146701e5341166cd52621a502368185) |
| 2012-03-03 | `feature` | Add Licence header to FixedBasicComboBoxEditor | `FixedBasicComboBoxEditor.java` | [ca19e459](https://github.com/freeplane/freeplane/commit/ca19e459abb17a246d81cac69675e1d2c344b92e) |
| 2012-03-01 | `feature` | add new (float) configuration option 'threshold for approximate matching', add Licence to  | `preferences.xml`, `ResourceController.java` +8 | [f918b77a](https://github.com/freeplane/freeplane/commit/f918b77a0f0ab932cbbcbe42529a3d532520791a) |
| 2012-03-01 | `fix` | fix NPE | `NewParentNode.java` | [3596b8bc](https://github.com/freeplane/freeplane/commit/3596b8bc2ba73d40664d6eec88770138716b1a0f) |
| 2012-03-01 | `fix` | fix NPE : save rich text content only if xmlText != null | `NodeTextBuilder.java` | [a79fc1da](https://github.com/freeplane/freeplane/commit/a79fc1dac2295a60efe12025a27acc6d1e449ff3) |
| 2012-02-26 | `feature` | Add license and fix copyright message in about box and windows installer | `Resources_ar.properties`, `Resources_ca.properties` +40 | [d50ffbf3](https://github.com/freeplane/freeplane/commit/d50ffbf3e583018681a20a5aeeec628b70962f0e) |
| 2012-02-24 | `fix` | fix build issue | `ComboProperty.java` | [5f6fbc8a](https://github.com/freeplane/freeplane/commit/5f6fbc8aebb7768f92ec794196e274974f9e8e0e) |
| 2012-02-22 | `feature` | add hint for developers | `MMapController.java` | [98d7501c](https://github.com/freeplane/freeplane/commit/98d7501c90c283c316e6c69130829b73a76bcdf3) |
| 2012-02-20 | `fix` | busy cursor during search, Fix BasicComboBoxEditor, switch project back to Java5 | `org.eclipse.jdt.core.prefs`, `FixedBasicComboBoxEditor.java` +8 | [1f32157c](https://github.com/freeplane/freeplane/commit/1f32157c2b3e98ba69463f07db50302d0fe6040b) |
| 2012-02-19 | `fix` | Fix handling of node text format set by style in style panel | `StyleEditorPanel.java` | [d1a18b41](https://github.com/freeplane/freeplane/commit/d1a18b4156a4dcb92ac4807ab483dbf2618d8806) |
| 2012-02-19 | `feature` | 1487: add link default field not conducive to Linux highlight/spit feature | `SetLinkByTextFieldAction.java` | [88d2f1cf](https://github.com/freeplane/freeplane/commit/88d2f1cf14be2b66ddc371be0453cbb654ff03b8) |
| 2012-02-17 | `feature` | Add special FilterCancelledException to replace RuntimeException if ScriptCondition cancel | `Filter.java`, `FilterCancelledException.java` +1 | [afbf331b](https://github.com/freeplane/freeplane/commit/afbf331b5adae52b31161687403cdafa1be493ca) |
| 2012-01-30 | `fix` | 1467: Inline editor is not closeable sometimes  : "Another bug" control + shift refactorin | `DefaultNodeKeyListener.java` | [31f1333c](https://github.com/freeplane/freeplane/commit/31f1333c1469f427622226793e9e606cf7194de6) |
| 2012-01-29 | `api_change` | 1478: Attempts to call the Scripting API from the About menu results in a null error | `MMapIO.java` | [d20d56dc](https://github.com/freeplane/freeplane/commit/d20d56dc593ba3ddcfa4d297f13ca521cb688e14) |
| 2012-01-27 | `feature` | new FormatController.formatUsingDefault() | `FormatController.java`, `FreeplaneScriptBaseClass.java` | [7d13a123](https://github.com/freeplane/freeplane/commit/7d13a1234258dc2f05c8ed38bff1065b51c9fb0a) |
| 2012-01-24 | `fix` | bug fix: uninstall key event dispathcher if the editing is cancelled or restarted | `MTextController.java` | [b7af234c](https://github.com/freeplane/freeplane/commit/b7af234c24a30474e909cd7a4f052e82494aba94) |
| 2012-01-22 | `fix` | fix NPEs | `LinkTransformer.java`, `FormulaTextTransformer.java` | [c9bf3de8](https://github.com/freeplane/freeplane/commit/c9bf3de8fbb437fa4823fb8441dc1860bb002427) |
| 2012-01-22 | `feature` | implement NO_FORMAT for attributes: - DecimalPatternFormat: unwrap argument FormattedNumbe | `DecimalPatternFormat.java`, `FormatController.java` +2 | [28868b1b](https://github.com/freeplane/freeplane/commit/28868b1b7a76447b54deb2ef5f920b6015de66b5) |
| 2012-01-21 | `fix` | 1456: Error while parsing file  : fix NPE on loading of hierarchical icons | `HierarchicalIcons.java` | [0032a6ae](https://github.com/freeplane/freeplane/commit/0032a6ae6f5670b5b1c661786a07f9c997645c41) |
| 2012-01-21 | `fix` | fix NPE | `LinkController.java` | [824010f6](https://github.com/freeplane/freeplane/commit/824010f63155e76c76ba4b3d651f7ec97c08f53c) |
| 2012-01-20 | `fix` | fix NPE | `EncryptionModel.java` | [2fca6da3](https://github.com/freeplane/freeplane/commit/2fca6da3aafb3edca2b4ae5318e3d64234705c07) |
| 2012-01-15 | `fix` | fix in MenuBuilder | `MenuBuilder.java` | [bc728167](https://github.com/freeplane/freeplane/commit/bc7281674606462b41ef61ced76d304750839d18) |
| 2012-01-14 | `fix` | auto bug reports | `MapController.java`, `ComboBoxRendererWithTooltip.java` +1 | [179507dd](https://github.com/freeplane/freeplane/commit/179507dd2cdf3f368cf520ce9db214e0e4035fa3) |
| 2012-01-14 | `fix` | fix NPE | `NodeStyleModel.java` | [3b77bd07](https://github.com/freeplane/freeplane/commit/3b77bd07317b3c4d464f69b0b949661cb404da4a) |
| 2012-01-14 | `fix` | fix waiting cursor if map loading was skipped | `MMapController.java` | [14d8a36b](https://github.com/freeplane/freeplane/commit/14d8a36be759883d3bb98834490950b9482fb777) |
| 2012-01-14 | `feature` | Create a new API for map loading and mark an old API as deprecated | `MANIFEST.MF`, `EncryptedMap.java` +17 | [cbcfb2b7](https://github.com/freeplane/freeplane/commit/cbcfb2b73e3c66041a5ebb58252b659384a70a0e) |
| 2012-01-12 | `feature` | Added the following command line arguments:  -X<menukey>: execute menu item with key <menu | `history_en.txt`, `MenuUtils.java` +9 | [347dc196](https://github.com/freeplane/freeplane/commit/347dc196f65a70af6b16f5db6dfe7b32b16ed50a) |
| 2012-01-06 | `fix` | avoid bug reports for SecurityExceptions due to running scripts at the master | `SingleInstanceManager.java` | [f92ae1ad](https://github.com/freeplane/freeplane/commit/f92ae1ad7530e8b3ac5f505255f747a79638a08b) |
| 2012-01-06 | `feature` | create attribute model  if required before adding a row | `AddAttributeAction.java` | [186a0f16](https://github.com/freeplane/freeplane/commit/186a0f1614ba1a3169835cffe68c7516cdee18ac) |
| 2012-01-06 | `fix` | fix error handling for map loading: handle xml errors and factory errors differently. | `UrlManager.java`, `StdXMLParser.java` | [2f8abdc3](https://github.com/freeplane/freeplane/commit/2f8abdc389f64f7f297fe2949d550e429d4371c7) |
| 2012-01-01 | `fix` | fix class cast exception | `MMapController.java` | [981435aa](https://github.com/freeplane/freeplane/commit/981435aac79419039cbba601a3e99e170978ee5f) |
| 2012-01-01 | `fix` | Attempt to fix NPE at at com.sun.java.swing.plaf.windows.WindowsTableHeaderUI.paint | `AttributeTable.java` | [68565b69](https://github.com/freeplane/freeplane/commit/68565b691f21bbf61d284d05197a0728c7d110d2) |
| 2012-01-01 | `fix` | fix NPE | `EditNodeTextField.java` | [64bec6a0](https://github.com/freeplane/freeplane/commit/64bec6a0082e7151a169ec2123d6635214f70c9c) |
| 2012-01-01 | `fix` | fix NPE | `DetailsViewMouseListener.java` | [42516ccd](https://github.com/freeplane/freeplane/commit/42516ccda100d3a3ad950c3d793f21261bb5b10f) |
| 2012-01-01 | `fix` | fix ArrayIndexOutOfBoundsException | `ConvexHull.java` | [56195695](https://github.com/freeplane/freeplane/commit/561956955ff4ba226c6651f975f665e42b138adb) |
| 2012-01-01 | `fix` | bug fixes | `stylemodemenu.xml`, `HtmlUtils.java` +12 | [0e1fc341](https://github.com/freeplane/freeplane/commit/0e1fc34179d5ed351ccfa71147370c82e79e3bc7) |

### Dettagli commit con note

**[7c291171](https://github.com/freeplane/freeplane/commit/7c291171d80231627e4fefa7b51f2127204fed7d)** (2012-06-17) — 1695: make it possible for file locks not to expire, or set the expiration time: In 1.2.15_13 there is a new property

> lock_expiration_time_in_minutes
> 
> with default value 5
> 
> You can set it to 0 if you want that lock is not automatically released or to any positive value.

**[f29a260e](https://github.com/freeplane/freeplane/commit/f29a260e41f44b11fac062b37628821870ef5e73)** (2012-04-20) — Fixes and extensions of the scripting API:

> - properties Node.next and Node.previous (extracted functionality from FilterController to util)
> 
>  - completed API documentations to resolve the FIXMEs
> 
>  - added special support for URL attribute values
> 
>  - removed the necessity to use the ArrowType enum in the scripting API for Connectors

**[5fe4def6](https://github.com/freeplane/freeplane/commit/5fe4def60d170c55d7dc35e050ea0f4d392b7770)** (2012-04-15) — Fixed two problems with attribute formatting/editing:

> 1. If an attribute value had a format like '#.######' this format was not remembered if the value is changed in an editor. The attribute format is assigned to the new value now.
> 
> 2. If you edit a formatted attribute the formatted value was supplied for editing instead of the original, unformatted value.


---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-12-31 | `feature` | 1423: Connector Lines not included with Branch as New Map Export feature | `MMapController.java` | [9a743f86](https://github.com/freeplane/freeplane/commit/9a743f86143de4bc966b4541aaddeb772f39161b) |
| 2011-12-31 | `fix` | fix file mode | `FMapModel.java` | [8aa387f5](https://github.com/freeplane/freeplane/commit/8aa387f544182cac78d8160755a9525290a0b332) |
| 2011-12-30 | `feature` | Rework creation of new maps: refactoring because of bug 1417]: Show node icons heirarchica | `AttributeController.java`, `AttributeRegistry.java` +21 | [d39a5fef](https://github.com/freeplane/freeplane/commit/d39a5fefef1b69a9e5663e7ffc9caca1532ec468) |
| 2011-12-29 | `fix` | fix NPE in UrlManager.getAbsoluteUri if map was not saved before | `UrlManager.java`, `ViewerController.java` | [d92f9e76](https://github.com/freeplane/freeplane/commit/d92f9e763a37fc7ca3b2428b385d4b92c99ccc92) |
| 2011-12-28 | `fix` | fix index == -1 exception | `CursorUpdater.java` | [cca44868](https://github.com/freeplane/freeplane/commit/cca4486861ee10b3cdcf1282175eb2b9ffda7f92) |
| 2011-12-28 | `fix` | fix NPE | `EditNodeTextField.java` | [bf7ed50d](https://github.com/freeplane/freeplane/commit/bf7ed50db144e9da0f5019ff1d2d48eeed79f140) |
| 2011-12-28 | `fix` | fix NPE | `CopyAttributes.java` | [7441ffd6](https://github.com/freeplane/freeplane/commit/7441ffd6f4ddabbd593f79b8c1c0d24dcd860eb3) |
| 2011-12-28 | `fix` | fix NPE | `DefaultNodeMouseMotionListener.java` | [cab68636](https://github.com/freeplane/freeplane/commit/cab6863650e6dbed4f95fe9418b307ee8ad8fae2) |
| 2011-12-28 | `fix` | fix NPE | `AssignStyleAction.java` | [4fc2ec51](https://github.com/freeplane/freeplane/commit/4fc2ec515b02187c69388f8199cb11cacffbf359) |
| 2011-12-28 | `fix` | fix java 7 compiler error | `TypedListCellRenderer.java` | [52932b15](https://github.com/freeplane/freeplane/commit/52932b15018294df8b95cf0aee922dd5a34ce826) |
| 2011-12-28 | `fix` | fix d/M parser - Thanks to Predrag | `DateFormatParser.java` | [8029d846](https://github.com/freeplane/freeplane/commit/8029d8465e02c858879939e881df509db089ddb6) |
| 2011-12-26 | `feature` | add time format by default | `FormatController.java` | [77b4dc2f](https://github.com/freeplane/freeplane/commit/77b4dc2f094b18052cfdfc03b8a517f1b22f2513) |
| 2011-12-26 | `feature` | - fix the Croatian date scanners - thanks to Predrag - add standard scanner if there is no | `history_en.txt`, `Scanner.java` +3 | [dd53271e](https://github.com/freeplane/freeplane/commit/dd53271ed5daf06c578ae0e51a163e74140a0603) |
| 2011-12-26 | `feature` | add a standard list of available locales if Freeplane is started from Eclipse where /trans | `OptionPanelBuilder.java` | [d80b4d41](https://github.com/freeplane/freeplane/commit/d80b4d4182d1dea75d2134fe4eb4b78b727d38c4) |
| 2011-12-25 | `fix` | fix npe | `NodeView.java` | [58fe15ea](https://github.com/freeplane/freeplane/commit/58fe15ead1ffc8da4ebb219aa998b200a81124ee) |
| 2011-12-24 | `fix` | fix java issues on mac | `freeplanemac.jar`, `ActivatorImpl.java` +1 | [09020e12](https://github.com/freeplane/freeplane/commit/09020e127da071497ada3e9d4e87e3e7ff0624b6) |
| 2011-12-24 | `feature` | add cloud action back to toolbar | `mindmapmodemenu.xml` | [e419a22d](https://github.com/freeplane/freeplane/commit/e419a22df2059c12849b1eb2a21788f1032313e6) |
| 2011-12-24 | `feature` | add new view action to menu | `mindmapmodemenu.xml` | [729515d8](https://github.com/freeplane/freeplane/commit/729515d89f4a991925346e7d5d3bfe4e10c8a221) |
| 2011-12-18 | `fix` | fix warnings | `DatePatternFormat.java`, `MFileManager.java` +1 | [3c79f31d](https://github.com/freeplane/freeplane/commit/3c79f31d7bf2120c0b4c454cbf938415f75f4531) |
| 2011-12-18 | `feature` | fix broken auto install on opening add-on packages | `MMapController.java` | [fa603377](https://github.com/freeplane/freeplane/commit/fa6033775591683ed55a1bc2c571e793bfe373e3) |
| 2011-12-15 | `feature` | care for display of keyboard shortcuts in the add-on details | `MenuUtils.java`, `installScriptAddOn.groovy` +1 | [9bcec98d](https://github.com/freeplane/freeplane/commit/9bcec98d71946dd18a29afefe6967df2015f1ad8) |
| 2011-12-14 | `feature` | new icons from Predrag Cuklin | `install_addons.png`, `manage_addons.png` +2 | [ed09f6eb](https://github.com/freeplane/freeplane/commit/ed09f6eb118be38b920a0e53cd5cbb8d66c3d297) |
| 2011-12-13 | `feature` | Add provisory handler for map dialect (currently does nothing) | `MapController.java` | [3128984e](https://github.com/freeplane/freeplane/commit/3128984efb72942468bdf383aca317dddc95e83e) |
| 2011-12-11 | `feature` | Add freeplane version  information into saved mind map files like <map version="0.9.0 dial | `FreeplaneVersion.java`, `MapWriter.java` | [79a13da1](https://github.com/freeplane/freeplane/commit/79a13da1fc24b890cf46502c9cfe89b53b5462a9) |
| 2011-12-04 | `feature` | add links to node menus | `mindmapmodemenu.xml`, `LinkController.java` +1 | [0b483428](https://github.com/freeplane/freeplane/commit/0b4834288f446f5a9619888493497209b6fd3890) |
| 2011-12-04 | `fix` | fix for map file names containing #  character | `MapModel.java` | [58d7ae67](https://github.com/freeplane/freeplane/commit/58d7ae6795a9165e621676d7bb1cc1dd7cc1e3c6) |
| 2011-12-04 | `fix` | fix : ignore directories on file drag and drop | `Compat.java`, `FileOpener.java` | [88053a03](https://github.com/freeplane/freeplane/commit/88053a03c5637c684ceedd6df52d867efa221c74) |
| 2011-12-04 | `feature` | add images to the add-on dialogs | `IconNotFound.java`, `UrlManager.java` +5 | [cb52b0f2](https://github.com/freeplane/freeplane/commit/cb52b0f2bd9c14daf8076783052772e6cd1bdfbb) |
| 2011-11-30 | `feature` | Add-ons dialog: - new 'Themes' tab for add-ons with names ending on 'theme' or 'Theme' - a | `Resources_de.properties`, `Resources_nl.properties` +7 | [8f9fa402](https://github.com/freeplane/freeplane/commit/8f9fa4028740de2e5c86c8cfde265add68764d46) |
| 2011-11-27 | `fix` | Continue Fix layout: consider cloud in node view height | `NodeViewLayoutAdapter.java` | [64a0c1c4](https://github.com/freeplane/freeplane/commit/64a0c1c434630f175cfd7bd5fa1645c016686552) |
| 2011-11-27 | `fix` | Fix layout: consider cloud in node view height | `NodeViewLayoutAdapter.java` | [9f409cb2](https://github.com/freeplane/freeplane/commit/9f409cb2b1ec07865d3db0497e1559de848942f0) |
| 2011-11-26 | `fix` | fix property for displaying script errors | `Resources_de.properties`, `Resources_es.properties` +6 | [c9f6245b](https://github.com/freeplane/freeplane/commit/c9f6245bd212ffddf71fd0580c9f48566cf653e7) |
| 2011-11-22 | `feature` | Support styles, font names and font sizes in main toolbar | `MModeControllerFactory.java`, `MToolbarContributor.java` | [ef76e304](https://github.com/freeplane/freeplane/commit/ef76e3041696b39fbfdb29120363219f0719a12c) |
| 2011-11-22 | `feature` | add addon buttons from Predrag Cuklin | `addons.png`, `install_addons.png` +3 | [6ef92f90](https://github.com/freeplane/freeplane/commit/6ef92f9016c940529be8b47554b59983b42c3b63) |
| 2011-11-22 | `feature` | add a name to the search button | `Resources_de.properties`, `Resources_en.properties` +1 | [c8b508a1](https://github.com/freeplane/freeplane/commit/c8b508a11142a56bd5610e0b28267d6cd0edd4e3) |
| 2011-11-19 | `fix` | auto bug fix | `MClipboardController.java`, `EditNodeTextField.java` | [442c9d6a](https://github.com/freeplane/freeplane/commit/442c9d6abc8c574fcb73cc3e474d0b95109e31d3) |
| 2011-11-19 | `feature` | Add-ons: Differentiate between a fresh install and an update deinstall the old version bef | `Resources_de.properties`, `AddOnsController.java` +2 | [b6bc609a](https://github.com/freeplane/freeplane/commit/b6bc609a0c48dea0e3669d2cc35a129a71845c26) |
| 2011-11-17 | `feature` | Display add-on details on installation | `Resources_de.properties`, `UITools.java` +6 | [8e7b87de](https://github.com/freeplane/freeplane/commit/8e7b87dea5bbb4b557ee2043c9255287e530cd0e) |
| 2011-11-14 | `feature` | Automatically create node width properties in user standard default template | `NodeStyleController.java`, `UserPropertiesUpdater.java` | [7ed48bf9](https://github.com/freeplane/freeplane/commit/7ed48bf95b75a7e737b3c545d4cd6c513155e060) |
| 2011-11-14 | `feature` | ADd node min / max width settings to the formatting panel | `StyleEditorPanel.java`, `Resources_en.properties` | [8d13e600](https://github.com/freeplane/freeplane/commit/8d13e6002dedfbb351626b7f4259ee3cd5a792b3) |
| 2011-11-14 | `fix` | Class cast bug fix | `AttributeTable.java` | [89afe15b](https://github.com/freeplane/freeplane/commit/89afe15ba921f6e66b2022998dcf29751a642af4) |
| 2011-11-07 | `fix` | fix parse error: {0] -> {0} | `Resources_nl.properties` | [14d09c83](https://github.com/freeplane/freeplane/commit/14d09c83468e8345f934329c42f6254892f6d69b) |
| 2011-11-06 | `fix` | fix NPE | `MapStyle.java` | [ce39178d](https://github.com/freeplane/freeplane/commit/ce39178df4f658bec49fa125b877c375113d8e45) |
| 2011-11-06 | `feature` | 1361: add ".png" to saved image file name  if entered file name does not have this extensi | `MClipboardController.java` | [dd4a69fd](https://github.com/freeplane/freeplane/commit/dd4a69fd32b9c89fca825bcb568e1d0a102f7668) |
| 2011-11-06 | `fix` | Fix check for executable links under windows | `Compat.java`, `FileUtils.java` +2 | [b0af1aee](https://github.com/freeplane/freeplane/commit/b0af1aee60aea5396089846c34329385ac23156b) |
| 2011-11-06 | `feature` | revert visorFreeplane.swf to older version: the new one seems to be buggy | `visorFreeplane.swf` | [93badc92](https://github.com/freeplane/freeplane/commit/93badc92a4d64d1156ebfb58def3d62ad9a97ca3) |
| 2011-11-05 | `fix` | fix comment handling in XMLParser | `XMLParser.java` | [c005b46f](https://github.com/freeplane/freeplane/commit/c005b46f16ba40285f86bb70b21fb79fa46af532) |
| 2011-11-01 | `fix` | bug fixes (auto bug reports) | `OpenPathAction.java`, `MapStyle.java` | [623327c8](https://github.com/freeplane/freeplane/commit/623327c8a36a9e1e6a230722ccd2e2c941640bad) |
| 2011-11-01 | `fix` | fix parent frame for prefernces dialog | `PropertyAction.java` | [628805dc](https://github.com/freeplane/freeplane/commit/628805dc5f62ec16adf9bbebf611bfc2525f9d67) |
| 2011-10-31 | `feature` | add new properties author and license and make them optional in the installer | `AddOnProperties.java` | [04d51d49](https://github.com/freeplane/freeplane/commit/04d51d4970e386059af935b5b858807e866eed77) |
| 2011-10-31 | `feature` | add new properties author and license and make them optional in the installer | `AddOnProperties.java`, `Resources_en.properties` +1 | [a1212a08](https://github.com/freeplane/freeplane/commit/a1212a08b7504cc0a0adaff7450ad61d27bf83b9) |
| 2011-10-26 | `feature` | ManageAddOnsDialog: - cope with HTML descriptions - update add-ons table after deinstall o | `AddOnsController.java`, `Resources_en.properties` +1 | [51ab52f2](https://github.com/freeplane/freeplane/commit/51ab52f2ee5c725945068cd2d8a1b1d6fbc20b55) |
| 2011-10-25 | `feature` | new max_text_width.png | `max_text_width.png` | [9d4a1ed7](https://github.com/freeplane/freeplane/commit/9d4a1ed783dd7013db0582640baf7e6ddcbf61ef) |
| 2011-10-24 | `fix` | fix typo | `Resources_de.properties` | [9beac05c](https://github.com/freeplane/freeplane/commit/9beac05c90bee31dcf4a9ab9a9fedfaeface454f) |
| 2011-10-24 | `feature` | new method ResourceController.getInstallationBase() | `ResourceController.java`, `ApplicationResourceController.java` | [a0e58a1b](https://github.com/freeplane/freeplane/commit/a0e58a1b1341bdee69c24f29af8d9ba6c1d40ad0) |
| 2011-10-23 | `feature` | final fixes & implement deactivate and deinstall | `AddOnProperties.java`, `AddOnsController.java` +3 | [17e44ef1](https://github.com/freeplane/freeplane/commit/17e44ef1b2814a60ba462f89c01acc232ec7f2c3) |
| 2011-10-23 | `feature` | move Add-ons more to the top | `mindmapmodemenu.xml` | [6c2d74a5](https://github.com/freeplane/freeplane/commit/6c2d74a5e2ce6d14bb5e3c2c3822f64905ca82b1) |
| 2011-10-23 | `fix` | Auto bug fixes | `AFilterComposerDialog.java`, `ImportLinkedBranchAction.java` +1 | [3d8a5c59](https://github.com/freeplane/freeplane/commit/3d8a5c590f63236ec14accc24ff82fca3c3e9322) |
| 2011-10-23 | `feature` | revert last Stefan's change  : do not add 8 to min node width | `NodeViewLayoutAdapter.java` | [22e664e2](https://github.com/freeplane/freeplane/commit/22e664e2b0ce95f08e4df4f46fcb46976e95adde) |
| 2011-10-21 | `fix` | Fix delay of 8 pixels with maximum node width | `NodeViewLayoutAdapter.java` | [152fc2bd](https://github.com/freeplane/freeplane/commit/152fc2bd2cfce27597f348427239ec5272d117b7) |
| 2011-10-20 | `fix` | fix auto reported bugs | `MClipboardController.java`, `StyleEditorPanel.java` +1 | [788f46a9](https://github.com/freeplane/freeplane/commit/788f46a96015d390933d641e0843798109e22be1) |
| 2011-10-15 | `fix` | fix NPE | `MapStyle.java` | [c43afc3c](https://github.com/freeplane/freeplane/commit/c43afc3ced216ae8c469d309bc2e2eb27f93a56d) |
| 2011-10-15 | `fix` | Bug fix: do nothing on updateUI for ZoomableLable | `ZoomableLabel.java` | [f8c88619](https://github.com/freeplane/freeplane/commit/f8c886196c0f4ae13c63a1980696d70ac34505b7) |
| 2011-10-15 | `fix` | fix ClassCastException | `RedoAction.java` | [75d00dcd](https://github.com/freeplane/freeplane/commit/75d00dcd52aa8f903cfee971816a6e9f9eece8c0) |
| 2011-10-15 | `feature` | Add option "image (separate file)" to selected paste | `MClipboardController.java`, `Resources_en.properties` | [017c469d](https://github.com/freeplane/freeplane/commit/017c469dc50520f51df0b7bf5aed6c021e1bf1e3) |
| 2011-10-15 | `feature` | remove add-on type from the add-ons dialog | `Resources_de.properties`, `Resources_en.properties` +1 | [7688a97f](https://github.com/freeplane/freeplane/commit/7688a97f1f9d8826b67bc0d0300602e4161b9600) |
| 2011-10-15 | `feature` | Paste images from clipboard (like in the new FreeMind alpha) | `MClipboardController.java` | [43ec2b74](https://github.com/freeplane/freeplane/commit/43ec2b74f0b869f60a3740d0eb7b0b7f306a8d0e) |
| 2011-10-09 | `fix` | Fix focus issues for filter toolbar | `FilterController.java`, `ToggleToolbarAction.java` | [72f54882](https://github.com/freeplane/freeplane/commit/72f5488271cb10281bf0e5e7a332c5efd0812596) |
| 2011-10-09 | `fix` | fix: update state (enabled, selected) of ToggleDetailsAction on actionPerformed and nodePo | `ToggleDetailsAction.java` | [115e8200](https://github.com/freeplane/freeplane/commit/115e8200ba9cb48f8731b44dad6bd8b16579e19b) |
| 2011-10-08 | `fix` | Fix auto bugs | `browsemodemenu.xml`, `mindmapmodemenu.xml` +13 | [ed1f1694](https://github.com/freeplane/freeplane/commit/ed1f16943afffb138b24a37265d534cd52aa9c69) |
| 2011-10-08 | `feature` | 1317: 1.2.9_02inconsistent behaviours of symbol of shortened node and of dragging ellipse  | `MMapController.java`, `NewFreeNodeAction.java` +1 | [6b66e829](https://github.com/freeplane/freeplane/commit/6b66e829d6133e37a7de186ec80045aa2da7a929) |
| 2011-10-08 | `feature` | 1314: Characters view in new detail | `EditNodeTextField.java` | [9cc66923](https://github.com/freeplane/freeplane/commit/9cc669231b988c3ef027cc1b94d22adad0e1f1ff) |
| 2011-10-04 | `fix` | Fix empty pages in print / preview | `MapView.java` | [e4d3e0d2](https://github.com/freeplane/freeplane/commit/e4d3e0d27f66c011e4b768d98010fef0b1f50f41) |
| 2011-10-03 | `feature` | All menu xml files have a new structure, move copy format and paste format to menu Format | `browsemodemenu.xml`, `filemodemenu.xml` +3 | [2a201dbe](https://github.com/freeplane/freeplane/commit/2a201dbe75b52c6de029fa64131d179f6b768090) |
| 2011-10-02 | `fix` | minor bug fix | `MNodeMotionListener.java` | [02b4e7df](https://github.com/freeplane/freeplane/commit/02b4e7df154d62534487fe026a5ce207cab3fad0) |
| 2011-10-02 | `feature` | Add class | `TransformationException.java` | [e146584a](https://github.com/freeplane/freeplane/commit/e146584a69653f8e5ac38d658ca7b5b1d3755fc5) |
| 2011-10-01 | `feature` | 1305: key for style to add to contextmenu | `mindmapmodemenu.xml` | [02367fa9](https://github.com/freeplane/freeplane/commit/02367fa988d3760ca7d59c32999f405f35e17539) |
| 2011-10-01 | `fix` | fix property name | `preferences.xml` | [a5048c2b](https://github.com/freeplane/freeplane/commit/a5048c2b053c22e31cdc1e63174ef622755717de) |
| 2011-10-01 | `fix` | fix Compat.isCtrlEvent | `Compat.java` | [b7faa262](https://github.com/freeplane/freeplane/commit/b7faa2627cf3734d367fb4ad8759537b509362ae) |
| 2011-09-28 | `api_change` | Refactoring: replace interface IMapMouseReceiver by standard java interfaces. | `IMapMouseReceiver.java`, `ApplicationViewController.java` +9 | [6a27b2e4](https://github.com/freeplane/freeplane/commit/6a27b2e44c80cc3e7d992d732854ff712913c358) |
| 2011-09-28 | `fix` | fix class cast exception | `DoAutomaticSave.java` | [ec6e35da](https://github.com/freeplane/freeplane/commit/ec6e35da6cea35bd11160e4048b377c6ff418991) |
| 2011-09-27 | `fix` | bug fix | `DocumentationAction.java` | [e448e393](https://github.com/freeplane/freeplane/commit/e448e3936f85c8af4cb388916419e073da0f6c7b) |
| 2011-09-25 | `feature` | add DeleteDetailsAction and SetShortenerStateAction to node popup | `mindmapmodemenu.xml` | [e1e06ac4](https://github.com/freeplane/freeplane/commit/e1e06ac42ef7ec26f99438c594efd13fba93de78) |
| 2011-09-25 | `fix` | Auto bug fixes | `FButtonBar.java`, `DesEncrypter.java` +1 | [ba2dd3c8](https://github.com/freeplane/freeplane/commit/ba2dd3c8a9fbc0d6a49ec21b221aae316b1b5f36) |
| 2011-09-24 | `feature` | 1270: add an extra key for <menu_category name=scripting> to the node context menu too | `mindmapmodemenu.xml`, `ScriptingConfiguration.java` +2 | [403ac5d6](https://github.com/freeplane/freeplane/commit/403ac5d6ca007f624beedbbc7144429155acca2a) |
| 2011-09-24 | `feature` | 1277: New English menu and tutorial/documentation based on 1.2.8_8 | `FilterConsumer.jpg`, `FilterConsumerEnd.jpg` +14 | [fe772afd](https://github.com/freeplane/freeplane/commit/fe772afda02bc4aedc8b57a5d61203cbc214688c) |
| 2011-09-24 | `feature` | Add-on-Installer | `Resources_de.properties`, `AddOnProperties.java` +4 | [e28b1575](https://github.com/freeplane/freeplane/commit/e28b1575f500b619059c69350efbe04d2aaa7c5f) |
| 2011-09-20 | `feature` | new option removeBlankLines in new htmlToPlain(text, strictHtmlOnly, removeNewLines) | `HtmlUtils.java` | [0c454ad6](https://github.com/freeplane/freeplane/commit/0c454ad6d2228761c53600fb3badd8baa6d785f7) |
| 2011-09-18 | `fix` | fix warning for folded style nodes | `NodeBuilder.java` | [691d8e6c](https://github.com/freeplane/freeplane/commit/691d8e6cdcac6f9676736e956f73a02f8520678d) |
| 2011-09-18 | `fix` | fix for summary nodes | `NodeViewLayoutAdapter.java` | [76c3ceaf](https://github.com/freeplane/freeplane/commit/76c3ceaf895046e5b5d6ea3c46479c48ee846faa) |
| 2011-09-15 | `feature` | Prototype of add-on management | `MANIFEST.MF`, `Resources_de.properties` +21 | [39e3ac81](https://github.com/freeplane/freeplane/commit/39e3ac81a46c0768b16729fc56901ba8462e1d33) |
| 2011-09-04 | `fix` | fix for auto bug report | `LogicalStyleController.java` | [6729dd4b](https://github.com/freeplane/freeplane/commit/6729dd4b0b6224bc10a7a895a829916895d6e7eb) |
| 2011-09-04 | `fix` | fix in NodeView.getPreferredVisibleChild | `NodeView.java` | [3b741093](https://github.com/freeplane/freeplane/commit/3b741093729aea9fb979526fa2aff6654d171251) |
| 2011-09-03 | `fix` | fix ClassNotFoundError in Applet | `AttributeController.java`, `MAttributeController.java` +1 | [3db93b7c](https://github.com/freeplane/freeplane/commit/3db93b7c6447bcfda45f2e8f8c2fb23d17f6e44d) |
| 2011-09-03 | `feature` | Similar behaviour for adding of new nodes as sibling and as child | `MMapController.java` | [e7571efe](https://github.com/freeplane/freeplane/commit/e7571efe0c7eaf8ed3259cee5dbef4f965a43020) |
| 2011-09-03 | `fix` | Fix endless loop for selection with shift | `MapView.java` | [137c30f9](https://github.com/freeplane/freeplane/commit/137c30f98ea3540a128ba429cead0f38fc2faf1e) |
| 2011-09-03 | `fix` | bug fix for F-Bar | `FButtonBar.java`, `MModeControllerFactory.java` | [78da2d14](https://github.com/freeplane/freeplane/commit/78da2d142ff8b54bb42f13960e6bacc5e61272ea) |
| 2011-09-03 | `fix` | Bug fix for editing of attribute values | `EventBuffer.java`, `AttributeTable.java` | [e7bdd02c](https://github.com/freeplane/freeplane/commit/e7bdd02c9568c0bda7f9c8cdf2dc41f2c707d7a5) |
| 2011-08-28 | `fix` | fix select continiuos | `UITools.java`, `MapView.java` | [dd3f1339](https://github.com/freeplane/freeplane/commit/dd3f1339c525f92b208258da15de968640e08d9f) |
| 2011-08-28 | `feature` | Set zoom of docu maps to 100%, add zoom box to main tool bar | `freeplane.mm`, `freeplaneTutorial.mm` +2 | [74df0f8d](https://github.com/freeplane/freeplane/commit/74df0f8d6a06964de5102eff91f800f74ab62b7a) |
| 2011-08-28 | `fix` | bug fix in folding of nodes after loading | `NodeBuilder.java` | [bae58b8a](https://github.com/freeplane/freeplane/commit/bae58b8a1d5c9bc1cffa8137698267f42632ff58) |
| 2011-08-28 | `feature` | new english texts and documentation from Jokro | `freeplane.mm`, `freeplaneTutorial.mm` +7 | [7906ac52](https://github.com/freeplane/freeplane/commit/7906ac52aaf7c6304603ac48f2f6053c8f38fa61) |
| 2011-08-28 | `fix` | fix NPE | `SModeControllerFactory.java` | [3dd17f6e](https://github.com/freeplane/freeplane/commit/3dd17f6ead2116826437b14091edb3c8e605cc5d) |
| 2011-08-27 | `fix` | Bug fix: horizontal line was pointed over bubble shaped summary nodes in outline view | `BubbleMainView.java`, `ForkMainView.java` +3 | [704ebd32](https://github.com/freeplane/freeplane/commit/704ebd32c8ebb22ece190d18681f6fb54b929b3a) |
| 2011-08-27 | `fix` | fix: update edge style for invisible parent views | `NodeView.java` | [b28f80a0](https://github.com/freeplane/freeplane/commit/b28f80a029ab10f66e830135f9f71b127e1c9a79) |
| 2011-08-21 | `fix` | fix painting of clouds within hidden nodes | `NodeView.java` | [f319a68d](https://github.com/freeplane/freeplane/commit/f319a68dd1918ba4fd1cd181c00e7396899b9dd4) |
| 2011-08-21 | `fix` | bug fix for shape as_parent | `NodeViewFactory.java` | [c90d3391](https://github.com/freeplane/freeplane/commit/c90d3391d67306219ab83121e280079b322af434) |
| 2011-08-21 | `fix` | fix node shape "as_parent" for root nodes | `BubbleMainView.java`, `ForkMainView.java` +4 | [b8b8323a](https://github.com/freeplane/freeplane/commit/b8b8323a594aa159243765b63f4bd449ea429c8c) |
| 2011-08-20 | `fix` | bug fixes in estimation of node shape "as_parent" | `NodeStyleController.java`, `MNodeStyleController.java` +2 | [77b43d08](https://github.com/freeplane/freeplane/commit/77b43d0894cd05b7f3588b31e2cbe1c6ba6ae303) |
| 2011-08-20 | `fix` | fix auto reported bugs | `XsltExportEngine.java`, `UrlManager.java` | [bdfa074c](https://github.com/freeplane/freeplane/commit/bdfa074c1e8387daa2d80d16d6286e80a4536d76) |
| 2011-08-18 | `fix` | fix background color for node editors | `EditNodeWYSIWYG.java`, `EditNodeTextField.java` | [b0cb3c79](https://github.com/freeplane/freeplane/commit/b0cb3c79240bd2e55d4213aa67a67e4f5a6109f2) |
| 2011-08-18 | `fix` | correct scale factor for painting zoomed maps | `ZoomableLabelUI.java` | [804dea8c](https://github.com/freeplane/freeplane/commit/804dea8ca11e8d3da2c06ae59f981487e35a65a6) |
| 2011-08-15 | `feature` | add style referenced by node  to conditional node style button text | `LogicalStyleController.java` | [ab7439da](https://github.com/freeplane/freeplane/commit/ab7439dafc6995395ddfed84cac933937e7a7cd2) |
| 2011-08-15 | `feature` | add encryption to browswer mode and applet | `browsemodemenu.xml`, `appletMenu.xml` | [656c1ba4](https://github.com/freeplane/freeplane/commit/656c1ba47fae4f37ffa87bd4ee6c9d6e145b9f30) |
| 2011-08-13 | `fix` | fix NPE | `ReducedAttributeTableModelDecorator.java` | [2a95838e](https://github.com/freeplane/freeplane/commit/2a95838eb2c28077e93178e34a8167144683e67c) |
| 2011-08-13 | `fix` | fix NPE: init NoteManager in NodeController | `MNoteController.java` | [f5faf999](https://github.com/freeplane/freeplane/commit/f5faf999403fa1b5d466ee1a96a3771ada2e964b) |
| 2011-08-12 | `fix` | bug  1199: layout of filtered summary nodes | `NodeView.java`, `NodeViewLayoutAdapter.java` | [4b3aef73](https://github.com/freeplane/freeplane/commit/4b3aef730c6dd85072796cc0c3755db5fb74d716) |
| 2011-08-12 | `fix` | bug fix: outline view edges | `EdgeViewFactory.java` | [3e9629af](https://github.com/freeplane/freeplane/commit/3e9629af304f6d2b46451f32253079a19bdc5339) |
| 2011-08-07 | `feature` | Implicitly remove mnemonic symbol "&" from all language properties.  To keep it new method | `SetBooleanPropertyAction.java`, `OptionPanel.java` +37 | [58c24897](https://github.com/freeplane/freeplane/commit/58c248971b98a22c06a0cc262e2989d02573be5c) |
| 2011-08-07 | `fix` | bug fixes for node conditional styles | `AManageConditionalStylesAction.java`, `ManageMapConditionalStylesAction.java` +2 | [3552c1b1](https://github.com/freeplane/freeplane/commit/3552c1b1ba69521def17a8aa4c586fb9cdd20e1d) |
| 2011-08-07 | `feature` | add node listeners for updating info in time management dialog | `TimeManagement.java` | [8fa8bd50](https://github.com/freeplane/freeplane/commit/8fa8bd50d0c80a38ea3d4aa360048995c3613ccf) |
| 2011-08-01 | `fix` | fix bug in ResourceBundles https://sourceforge.net/projects/freeplane/forums/forum/758439/ | `ResourceBundles.java`, `ResourceController.java` +1 | [fe5eb8f1](https://github.com/freeplane/freeplane/commit/fe5eb8f1fe628b337bc0a7f0a822319910e97eea) |
| 2011-07-31 | `fix` | bug fix in paintSummaryEdge | `NodeView.java` | [aa97779e](https://github.com/freeplane/freeplane/commit/aa97779e550ac364ca8e3ec818cf52cd57641d31) |
| 2011-07-23 | `fix` | bug fix: calculation of node width for inline editor | `EditNodeTextField.java` | [3bdaa9ab](https://github.com/freeplane/freeplane/commit/3bdaa9abd064980a34f48fb0160aeeada6c6f07b) |
| 2011-07-23 | `fix` | fix NPE | `RedefineStyleAction.java` | [a6a51802](https://github.com/freeplane/freeplane/commit/a6a518021729bff101b0b961561077b55bb44238) |
| 2011-07-23 | `fix` | fix NPE | `MLinkController.java` | [1a1bca56](https://github.com/freeplane/freeplane/commit/1a1bca56fc01191f7607ad560ad59f676a7a81e4) |
| 2011-07-23 | `fix` | fix NPE | `NewUserStyleAction.java` | [9aa07ca8](https://github.com/freeplane/freeplane/commit/9aa07ca89e0a49cc970c9361238e97fbb0799da6) |
| 2011-07-22 | `api_change` | minor API changes and fixes | `OptionPanelBuilder.java`, `MNoteController.java` +2 | [8696f28f](https://github.com/freeplane/freeplane/commit/8696f28f86c9c594f2cd536d5067903b023352b9) |
| 2011-07-22 | `fix` | fix: tool tips in style editor | `NodeTooltipManager.java` | [9fd9e429](https://github.com/freeplane/freeplane/commit/9fd9e4290ddf230f962dc358a731c460c058652c) |
| 2011-07-22 | `feature` | add note to style extensions | `stylemodemenu.xml`, `MLogicalStyleController.java` +1 | [2f050461](https://github.com/freeplane/freeplane/commit/2f050461aaca7e380dfd0c97097e49c55265a648) |
| 2011-07-21 | `fix` | move AutomaticStyles to another package fix conditional styles for automatic layout displa | `mindmapmodemenu.xml`, `AutomaticLayout.java` +4 | [2648c932](https://github.com/freeplane/freeplane/commit/2648c932123410cc329ca867e727b47cb241a6b4) |
| 2011-07-13 | `feature` | for use in scripting: add accessors for default formats of FormatController | `TextUtils.java` | [14080148](https://github.com/freeplane/freeplane/commit/140801489e153aed52d3596a1db0aab09d4c0831) |
| 2011-07-06 | `fix` | layout bug fix for summary nodes | `NodeViewLayoutAdapter.java` | [cbb04f12](https://github.com/freeplane/freeplane/commit/cbb04f1257e80fac028887304fe533c05c8935c3) |
| 2011-07-05 | `feature` | new icons | `freeplane_app_128x128.png`, `freeplane.icns` +7 | [052a2501](https://github.com/freeplane/freeplane/commit/052a25011011763a937169889e369c072a7e98b9) |
| 2011-07-05 | `fix` | auto bug report fix : use LinkController.createURI for imports from IExplorer | `ImportExplorerFavoritesAction.java` | [b77f5e01](https://github.com/freeplane/freeplane/commit/b77f5e01fb3d709d6eb631f9e2fb99f976bfed93) |
| 2011-07-04 | `feature` | new version of mindmapmodemenu.xml | `mindmapmodemenu.xml` | [97a49fcc](https://github.com/freeplane/freeplane/commit/97a49fcc715f80c8c7974e791510f4a99780a75d) |
| 2011-07-04 | `fix` | fix display of AttributeContainsCondition | `AttributeContainsCondition.java` | [625d0a82](https://github.com/freeplane/freeplane/commit/625d0a8260eeac1fc64fcd48430a86f14db00cdf) |
| 2011-07-04 | `fix` | bug fixes for applet: do not initiwlize some actions | `HelpController.java`, `appletMenu.xml` | [da367879](https://github.com/freeplane/freeplane/commit/da36787964624acbce3bfe441bd14d4ffaf2d878) |
| 2011-07-04 | `fix` | fix formatting of option panel validation errors | `OptionPanel.java` | [607d872b](https://github.com/freeplane/freeplane/commit/607d872b5c3ed82b2de4bc44363841ffc4df3b6b) |
| 2011-06-22 | `fix` | fix "insert link into attribute" action | `AttributePopupMenu.java` | [ff8ec285](https://github.com/freeplane/freeplane/commit/ff8ec2850a97dc49e8ca8379d80702772e32f692) |
| 2011-06-22 | `fix` | fix NPE | `CursorUpdater.java` | [30cb27a8](https://github.com/freeplane/freeplane/commit/30cb27a8d32c5b27bac73f6afd65ed73a1dca103) |
| 2011-06-19 | `feature` | Enable Details for Styles.  Copy style attributes and details if settign of style is the f | `stylemodemenu.xml`, `CopyAttributes.java` +9 | [628cdab8](https://github.com/freeplane/freeplane/commit/628cdab8dab9df18c4b7b5f8ea2ff62b598b44ef) |
| 2011-06-18 | `fix` | fix package names in freeplane_mac | `freeplanemac.jar`, `FilterConditionEditor.java` +1 | [1ce1e2d7](https://github.com/freeplane/freeplane/commit/1ce1e2d7b0f5b5c04e1b650d340a74b5fd3c90ad) |
| 2011-06-16 | `fix` | fix if format.xml is corrupted | `FormatController.java` | [2d3cc609](https://github.com/freeplane/freeplane/commit/2d3cc6095079a2f23ee168b683bfb8296c81e40c) |
| 2011-06-14 | `fix` | fix : ignore transparent filter counting filtered nodes | `FilePropertiesAction.java` | [7b5519df](https://github.com/freeplane/freeplane/commit/7b5519df7f9e599c101a713537969b4f5fd1177d) |
| 2011-06-14 | `feature` | Add number of filtered nodes to map statistics, rename action "map properties" into "map s | `Filter.java`, `FilePropertiesAction.java` +1 | [697ac2b2](https://github.com/freeplane/freeplane/commit/697ac2b2009cd128c9abec531e63f4bd33a0a19d) |
| 2011-06-14 | `fix` | Fix TypeReference factory after renaming packages | `TypeReference.java` | [9e7e45a7](https://github.com/freeplane/freeplane/commit/9e7e45a72e38d05d8d5a70eaf09bfac25a33b459) |
| 2011-06-12 | `fix` | bug fix: handling of importing of not existing linked map files | `MFileManager.java` | [5f162092](https://github.com/freeplane/freeplane/commit/5f162092a709c061cf4c9bc79b8064beb4533aa0) |
| 2011-06-12 | `fix` | fix node tooltip position for dual screens under windows | `NodeTooltipManager.java` | [8d6c6a65](https://github.com/freeplane/freeplane/commit/8d6c6a655a91dcbb7f75fed4efc062c73da4e819) |
| 2011-06-12 | `fix` | fix java.util.NoSuchElementException 	at org.freeplane.core.util.collection.SortedMapVecto | `AttributeConditionController.java` | [d24c14bc](https://github.com/freeplane/freeplane/commit/d24c14bcf927f4bf57f59fa6b1f09457363fdb9b) |
| 2011-06-12 | `fix` | Attempt to fix java.util.NoSuchElementException 	at java.util.LinkedList.remove(LinkedList | `IUndoHandler.java`, `UndoHandler.java` +1 | [4e3f6b0c](https://github.com/freeplane/freeplane/commit/4e3f6b0cc37e32d3d6e91429f99244c57d7e1565) |
| 2011-06-12 | `fix` | fix NPE | `MNoteController.java` | [a50e0f36](https://github.com/freeplane/freeplane/commit/a50e0f3633c4978853b41c118d305990e16b0159) |
| 2011-06-12 | `fix` | fix NPE if no frame can be found by SingleInstanceManager | `SingleInstanceManager.java` | [5818dc8f](https://github.com/freeplane/freeplane/commit/5818dc8f82befc2ee553b3386003d12952cd5ac2) |
| 2011-06-12 | `fix` | auto bug fix: NPE happened probably if table editing sinished with mode change | `TextController.java`, `MTextController.java` | [13acc2d7](https://github.com/freeplane/freeplane/commit/13acc2d74cc7097a51eed6fd4b0b18e20a56fcf0) |
| 2011-06-12 | `fix` | fix ConcurrentModificationException by using array | `MapViewChangeObserverCompound.java` | [35636cc3](https://github.com/freeplane/freeplane/commit/35636cc37544e403c089d2d8283f9567e5195fdf) |
| 2011-06-11 | `feature` | add new action menu_key attributes used in mac changes + related bug fixes | `browsemodemenu.xml`, `filemodemenu.xml` +4 | [e29bd8cd](https://github.com/freeplane/freeplane/commit/e29bd8cd14d3bea07708ca83c8d3648b1a073597) |
| 2011-06-11 | `fix` | bug fix: remove "shadow" for hidden node details | `DetailsView.java`, `NodeViewFactory.java` | [d649d242](https://github.com/freeplane/freeplane/commit/d649d2427f4f714c78a2b21826e40954dc74556c) |
| 2011-06-11 | `feature` | new artwork | `Freeplane_frame_icon.png`, `Freeplane_frame_icon_32x32.png` +16 | [198bd07a](https://github.com/freeplane/freeplane/commit/198bd07a7019abf015879433f10cee8ce1457142) |
| 2011-06-05 | `feature` | new version of mind map menu structure | `mindmapmodemenu.xml` | [a611c386](https://github.com/freeplane/freeplane/commit/a611c3864cd2739d6e04245d90578d700687f019) |
| 2011-06-05 | `feature` | Always run "assign new short cut" for unassigned F-keys | `AccelerateableAction.java`, `SetAcceleratorOnNextClickAction.java` +1 | [85d3e5ff](https://github.com/freeplane/freeplane/commit/85d3e5ff7b374b0963a9f1c7db7fd48907c0c85e) |
| 2011-06-05 | `fix` | 1115]: Ctrl+Arrow Down does not function properly, relates to fix for 1099]: Move node wit | `MMapController.java`, `NodeUpAction.java` +1 | [78a1b066](https://github.com/freeplane/freeplane/commit/78a1b0666cb8c110109b1e6a82a498e09969ad09) |
| 2011-06-03 | `feature` | add method ClipboardController.duplicate | `ClipboardController.java`, `NodeList.java` | [53a63813](https://github.com/freeplane/freeplane/commit/53a6381317f7f23aa731f2af6c0ccd0be636ce5c) |
| 2011-06-02 | `fix` | bug fix : change edge color on node move if automatic edge color is active | `AutomaticEdgeColorHook.java` | [1c8f7bda](https://github.com/freeplane/freeplane/commit/1c8f7bdaaafd0782eebeaa527461f2a847ce1726) |
| 2011-05-31 | `fix` | The node limit fix for the Flash Browser, https://sourceforge.net/tracker/?func=detail&aid | `visorFreeplane.swf` | [8ae4d324](https://github.com/freeplane/freeplane/commit/8ae4d324f7bd4bff64a115e7aacf1e90683ed1b2) |
| 2011-05-29 | `feature` | new rule for selection change: keep selection if MainView was focused and the clicked node | `DefaultNodeMouseMotionListener.java` | [5950f89e](https://github.com/freeplane/freeplane/commit/5950f89e5194f057e262ab6925ebc9342e46ac20) |
| 2011-05-29 | `fix` | fix QuickFindAllAction for root node | `QuickFindAllAction.java` | [7320af23](https://github.com/freeplane/freeplane/commit/7320af23e95b8ac021d12efdefe90f029b19cf9d) |
| 2011-05-24 | `fix` | fix a bug reported by Predrag: Don't insert the date into the hour/minute fields of the ca | `TimeManagement.java` | [9fc43eae](https://github.com/freeplane/freeplane/commit/9fc43eaec05a10c53b8de6dda03207de26faf574) |
| 2011-05-23 | `feature` | script_execution_disabled: added hint were to enable, see https://sourceforge.net/projects | `Resources_de.properties`, `Resources_en.properties` | [14b37148](https://github.com/freeplane/freeplane/commit/14b37148d6e8708e74812edc56e674805728d37e) |
| 2011-05-22 | `fix` | bug fix paint summary edge | `NodeView.java` | [43af3faf](https://github.com/freeplane/freeplane/commit/43af3faf6c666b489fc422cae1d7deebd9ad7ada) |
| 2011-05-21 | `fix` | fix smb2unc | `Compat.java`, `SetLinkByTextFieldAction.java` +1 | [efcfae3f](https://github.com/freeplane/freeplane/commit/efcfae3ff2fe011e1f6accb8f4e294b8a8266808) |
| 2011-05-21 | `fix` | fix java type conversion | `PersistentNodeHook.java` | [b40d53f3](https://github.com/freeplane/freeplane/commit/b40d53f368700fa564f8c07779b3adbad8b2e4fd) |
| 2011-05-21 | `feature` | support for enum based hooks | `PersistentNodeHook.java` | [3e30c0b9](https://github.com/freeplane/freeplane/commit/3e30c0b9fcaecb99dc949572b48368c72359e98d) |
| 2011-05-20 | `feature` | added new option for the locale to use for formatting and scanning data: | `build.xml`, `locales.txt` +4 | [92e314c2](https://github.com/freeplane/freeplane/commit/92e314c2f79caaff7c500b30d2a7693a9e444d16) |
| 2011-05-19 | `fix` | fix errorneous placeholders usage error | `Resources_ko.properties` | [e5c74453](https://github.com/freeplane/freeplane/commit/e5c744535f8add0e364238b38b2b24a5908953fe) |
| 2011-05-18 | `fix` | fix for the error reported by megatop in https://sourceforge.net/projects/freeplane/forums | `Resources_fr.properties` | [2f78b504](https://github.com/freeplane/freeplane/commit/2f78b504b821b7c7ebc1e1cc18cf9ad2fe1c0533) |
| 2011-05-17 | `fix` | bug fix in painting of summary node brackets | `NodeView.java` | [15e79301](https://github.com/freeplane/freeplane/commit/15e79301b78bef0c62801edae15125851fd9fc22) |
| 2011-05-15 | `fix` | fix fillXml(): test for interface IFormattedObject, not for the special implementation For | `CompareConditionAdapter.java` | [36e62176](https://github.com/freeplane/freeplane/commit/36e62176728ed9f430927744410c1d233785e81d) |
| 2011-05-14 | `fix` | fix errorneous error message... | `ScannerController.java` | [5151dd00](https://github.com/freeplane/freeplane/commit/5151dd00a97e0157c0a8c9fee93d3bdfc5682fe9) |
| 2011-05-14 | `fix` | bug fix : exchange position of folding mark and shortened content mark | `MainView.java` | [2e88c28f](https://github.com/freeplane/freeplane/commit/2e88c28f09237f09c383dc165a843a8c573d241f) |
| 2011-05-14 | `fix` | bug fix | `CompareConditionAdapter.java` | [71d5ca63](https://github.com/freeplane/freeplane/commit/71d5ca631db009d0f9fad37aa23ebe8d866c2d43) |
| 2011-05-14 | `fix` | better bug fix for attribute panel if no map is open | `AttributePanelManager.java` | [f2e5d9d1](https://github.com/freeplane/freeplane/commit/f2e5d9d199ff5c7993ce8e0b5710996e43c3385c) |
| 2011-05-09 | `fix` | bug fixes in atribute table, renderer, panel manager | `ViewController.java`, `AttributePanelManager.java` +1 | [f66734bc](https://github.com/freeplane/freeplane/commit/f66734bc57e5245b7c978abff8373c041d0411f4) |
| 2011-05-09 | `fix` | fix unit test: constructing a DecimalFormat with #.#### results in the different pattern # | `FormatController.java`, `freeplane.properties` +1 | [370e58c9](https://github.com/freeplane/freeplane/commit/370e58c96c7300d5bc8a214e296aea4f565cea41) |
| 2011-05-09 | `fix` | Fix in EdgeView | `EdgeView.java` | [d1d9a185](https://github.com/freeplane/freeplane/commit/d1d9a1855f2d924884bb16b103eb676af81e44b5) |
| 2011-05-09 | `fix` | fix default settings of parsers | `Scanner.java`, `ScannerController.java` | [c6daff34](https://github.com/freeplane/freeplane/commit/c6daff3435f733af21faa7da2556e3f3930c97ec) |
| 2011-05-09 | `feature` | implemented input scanner for date and number recognition: - replace options parse_dates a | `Resources_de.properties`, `Resources_fr.properties` +33 | [35d089f0](https://github.com/freeplane/freeplane/commit/35d089f0ac335957e07c5b4df9ac3914cd7934b7) |
| 2011-05-08 | `fix` | another fix | `LinearEdgeView.java` | [4df8f34f](https://github.com/freeplane/freeplane/commit/4df8f34f855e6c2a66b7e5d6671b63b59620c6b7) |
| 2011-05-08 | `fix` | bug fixes after refactoring | `OutlineEdgeView.java`, `OutlineLinkView.java` | [eea511f9](https://github.com/freeplane/freeplane/commit/eea511f9fc1d3540d8617f94bb4395818300f6b7) |
| 2011-05-08 | `feature` | Refactor edge / connector alignment points in main view / node view / edge view, add top a | `BubbleMainView.java`, `ForkMainView.java` +13 | [3ccf817e](https://github.com/freeplane/freeplane/commit/3ccf817e6096df89d37aa3fabea19199922619d8) |
| 2011-05-07 | `fix` | fix in layout | `NodeViewLayoutAdapter.java` | [e8e35cb6](https://github.com/freeplane/freeplane/commit/e8e35cb6efff73ecc1b90a3ea0f173743e0552dd) |
| 2011-05-07 | `feature` | Use dialog instead of popup menu for connectors, add spell check to connector label editor | `ControllerPopupMenuListener.java`, `ContainerMenuItem.java` +7 | [55181dab](https://github.com/freeplane/freeplane/commit/55181dab74f8501d2c5114486b91077f43bd18b6) |
| 2011-05-01 | `feature` | BranchesOverlap add-in and action | `mindmapmodemenu.xml`, `PersistentNodeHook.java` +7 | [44dc6451](https://github.com/freeplane/freeplane/commit/44dc64518512a22ccb978cecd06c83b43b34c095) |
| 2011-05-01 | `fix` | bug fix | `EditNodeBase.java` | [4fb3b39e](https://github.com/freeplane/freeplane/commit/4fb3b39eb8378c776abdc79c76861d00a9c0575c) |
| 2011-04-29 | `feature` | add option 'parse_numbers' in analogy to 'parse_dates' | `preferences.xml`, `MTextController.java` +2 | [4654c705](https://github.com/freeplane/freeplane/commit/4654c7050cb9afb5e938cb2592ad5229318ec7b5) |
| 2011-04-27 | `fix` | fix: make one member variable static | `NodeView.java` | [c2dfdbaf](https://github.com/freeplane/freeplane/commit/c2dfdbaf55719fa8d14cbb9d7368fa377ec8c43d) |
| 2011-04-25 | `fix` | Bug fix: accelerator for DELETE | `mindmapmodemenu.xml`, `KeyEventTranslator.java` | [b8f8810f](https://github.com/freeplane/freeplane/commit/b8f8810f4acff5863e4ab68ea327a7e9d8365e14) |
| 2011-04-24 | `feature` | allow adding of connector to the node itself by add connector action | `AddConnectorAction.java` | [856de12b](https://github.com/freeplane/freeplane/commit/856de12badf4eaca5361411e3bdd034559225474) |
| 2011-04-23 | `feature` | 1057: Add an separate translation key for Menu File > Close | `AssignAttributeDialog.java`, `ListDialog.java` +1 | [d31dcc1d](https://github.com/freeplane/freeplane/commit/d31dcc1daf37ff7693761e5a4f7947f356ff0dd0) |
| 2011-04-22 | `fix` | Fix handling of  first group nodes for summaries of summaries | `SummaryNode.java`, `NodeViewLayoutAdapter.java` | [84c2ed6f](https://github.com/freeplane/freeplane/commit/84c2ed6fc62610d0a88a1feecbfc5d59ce164b7c) |
| 2011-04-22 | `feature` | 1052]: first typed character skipped when ADD CHILD NODE on key type is enabled | `EditNodeBase.java` | [a03710f9](https://github.com/freeplane/freeplane/commit/a03710f9db2d936a2c44dc750e5857b505918fc9) |
| 2011-04-21 | `feature` | 1055]: Latest version of FP does not properly manage text typed into a new node | `EditNodeTextField.java` | [0fd778c7](https://github.com/freeplane/freeplane/commit/0fd778c7a9a5e29cb344832e4dab811f2229622e) |
| 2011-04-17 | `feature` | Add summary nodes to browse mode and applet | `BModeControllerFactory.java` | [b2df93af](https://github.com/freeplane/freeplane/commit/b2df93af4b70f8eb6c465ceceb1d9b9ff7355cb8) |
| 2011-04-17 | `fix` | bug fix in layout for left summary nodes | `NodeViewLayoutAdapter.java` | [b7036e81](https://github.com/freeplane/freeplane/commit/b7036e8130ef2fab8c44bbac31f5e320f9b6786b) |
| 2011-04-13 | `fix` | bug fix: positive Y shift for first child node | `NodeViewLayoutAdapter.java` | [0e9a0b2d](https://github.com/freeplane/freeplane/commit/0e9a0b2d578e7ab51a361c9481e72e8b56c66fbb) |
| 2011-04-13 | `feature` | new: FreeplaneVersion(int,int,int), isOlderThan(), isNewerThan() | `FreeplaneVersion.java` | [7880a104](https://github.com/freeplane/freeplane/commit/7880a104cbe70b29ff989227e1fa5c1813f6a16f) |
| 2011-04-12 | `feature` | "External Object" remove and added  "Add External Image...", "Change External Image..." an | `mindmapmodemenu.xml`, `NodeModel.java` +5 | [67c3e097](https://github.com/freeplane/freeplane/commit/67c3e097c9451ad3471fe50276123e20783bbebf) |
| 2011-04-06 | `fix` | fix mac accelerators | `freeplane_mac.properties` | [5af28261](https://github.com/freeplane/freeplane/commit/5af28261f6ea50dbadc385f97bdf5b220a53957e) |
| 2011-04-02 | `feature` | add dir <user-dir>/resources to resources search path | `ApplicationResourceController.java` | [2808711e](https://github.com/freeplane/freeplane/commit/2808711e7c432521c14cc43f73bfc376369002b4) |
| 2011-04-02 | `feature` | create plugin dependent submenus only if plugin is loaded | `mindmapmodemenu.xml`, `MenuBuilder.java` +1 | [bbbf5690](https://github.com/freeplane/freeplane/commit/bbbf5690ee4f4efe67c67942a37b3e3e82c43505) |
| 2011-03-31 | `fix` | Open User Directory: fix NPE that happened when no map was opened. Thanks to antonimo | `MFileManager.java` | [e0af30ac](https://github.com/freeplane/freeplane/commit/e0af30acbabb991ce962c937aba97f3ea1b26ac4) |
| 2011-03-27 | `fix` | fix compiler warnings | `ResourceController.java`, `TypedListCellRenderer.java` +8 | [d7d93930](https://github.com/freeplane/freeplane/commit/d7d93930265e1fc8747c2a8af35a4a182da75d98) |
| 2011-03-24 | `feature` | #1034: Put Freeplane in the Foreground when opening a new map - only works if iconified | `SingleInstanceManager.java` | [8f8e5184](https://github.com/freeplane/freeplane/commit/8f8e5184c2337d101456a842ad90bde06398c954) |
| 2011-03-24 | `feature` | translation consolidation:  - remove obsolete keys/translations  - add some tooltips to Re | `Resources_ar.properties`, `Resources_ca.properties` +30 | [be5e369d](https://github.com/freeplane/freeplane/commit/be5e369da8d8abdf9f3611ec652846fdd16319df) |
| 2011-03-24 | `fix` | Bug fix: preferences popup did not open | `MIconController.java` | [68854991](https://github.com/freeplane/freeplane/commit/688549914fe88c10d604911a2d4bb3f25f88c2b0) |
| 2011-03-21 | `feature` | new icons + hr translatiion | `EditNoteInDialogAction.png`, `ExecuteScriptForAllNodes.png` +17 | [ed744f06](https://github.com/freeplane/freeplane/commit/ed744f0657ee03b5181b7f3e3c21bba2b6113931) |
| 2011-03-20 | `fix` | Rename KeyTypeAction to FirstAction, fix freeplane_script_plugin | `AccelerateableAction.java`, `IEditHandler.java` +6 | [e88b92a2](https://github.com/freeplane/freeplane/commit/e88b92a232a9c6b2e1d949eae289524abc44331b) |
| 2011-03-20 | `feature` | 1032]: new child node as I start to typing | `Resources_ar.properties`, `Resources_ca.properties` +42 | [31e42914](https://github.com/freeplane/freeplane/commit/31e429143f08be5d68b7828e51187d2b879bc4ad) |
| 2011-03-19 | `fix` | automatic bug report bug fixes | `NodeModel.java`, `NodeTextBuilder.java` +3 | [26ede6e1](https://github.com/freeplane/freeplane/commit/26ede6e108f357e630d94ecf5dba115cfc72c349) |
| 2011-03-13 | `fix` | auto bug report fixes | `MatchCaseNodeContainsCondition.java`, `NodeContainsCondition.java` +4 | [1a6e828b](https://github.com/freeplane/freeplane/commit/1a6e828b8345923a720c3b7bb7854059843a13e0) |
| 2011-03-13 | `feature` | 1019]: Option "Key Type Adds New" is not working properly. | `MNoteController.java`, `NodeView.java` +2 | [dc836aac](https://github.com/freeplane/freeplane/commit/dc836aac430eea1b1300662c103fa3d4dcf27236) |
| 2011-03-12 | `fix` | Fix: update no object type information on content change | `ViewController.java`, `MainView.java` +1 | [5d3b4bfd](https://github.com/freeplane/freeplane/commit/5d3b4bfdab9e2b9a9d1b6d99aee547f3a901d5eb) |
| 2011-03-12 | `fix` | bug fixes | `ContainerComboBoxEditor.java`, `AttributeConditionController.java` +1 | [0fe459c6](https://github.com/freeplane/freeplane/commit/0fe459c6704c29159dd5570debadc6da28bf73ef) |
| 2011-03-07 | `feature` | Scripting API: add support for FreeplaneDate and URIs | `FreeplaneDate.java`, `Convertible.java` +3 | [ae7c454d](https://github.com/freeplane/freeplane/commit/ae7c454d6d176cae169ad4d4d0015c35e7b7d1af) |
| 2011-03-07 | `fix` | fix compiler warnings | `CompareConditionAdapter.java`, `FormulaUpdateChangeListener.java` | [939c9fff](https://github.com/freeplane/freeplane/commit/939c9fff2e301cb126e254906e749312407587b7) |
| 2011-03-06 | `fix` | 1002]: Show all notes feature generates a bug | `NodeViewFactory.java` | [a6c95c0b](https://github.com/freeplane/freeplane/commit/a6c95c0bcfe422a83461b2895abb43a970777c8b) |
| 2011-03-06 | `fix` | bug fixes in calendar pane + date format can be set from calendar pane | `FreeplaneDate.java`, `MTextController.java` +1 | [4b2a969d](https://github.com/freeplane/freeplane/commit/4b2a969d2186dee56ea05d145b719b7a97628a14) |
| 2011-03-05 | `feature` | Save  dateFormat in FreeplaneDate, fixes in CompareConditionAdapter and derived classes to | `FreeplaneDate.java`, `AttributeCompareCondition.java` +7 | [8d60a9ed](https://github.com/freeplane/freeplane/commit/8d60a9edf2a20f30f3f25189b297a63c39bfaaf9) |
| 2011-03-04 | `feature` | add link handler to SimplyHTML | `MTextController.java` | [c889c9d2](https://github.com/freeplane/freeplane/commit/c889c9d23f6027b4d205ad6945fe293efc8c506a) |
| 2011-03-04 | `fix` | Bug fix: remove buggy method MapController.refreshMap, use fireMapChanged instead Remove o | `Resources_ar.properties`, `Resources_ca.properties` +45 | [801ccd7e](https://github.com/freeplane/freeplane/commit/801ccd7e650207b368968997cd25f9e5c8315d68) |
| 2011-03-03 | `fix` | bug fix in NodeLevel condition | `CompareConditionAdapter.java`, `NodeLevelCompareCondition.java` | [f7391164](https://github.com/freeplane/freeplane/commit/f7391164713b1dd74ea78f35b6903b17b0913ee7) |
| 2011-03-03 | `fix` | bug fixes in painting ForkMainView | `ForkMainView.java`, `MainView.java` +1 | [42a2c909](https://github.com/freeplane/freeplane/commit/42a2c90939514ba25c6698b6569a8eab6b6b07ef) |
| 2011-03-03 | `fix` | bug fixes in TypeReference | `FreeplaneDate.java`, `TypeReference.java` +1 | [3b2ea302](https://github.com/freeplane/freeplane/commit/3b2ea30208763edc66e6a2500cdcafaaf661e200) |
| 2011-03-02 | `fix` | bug fix : replace old text if editing starts with pressed character key | `EditNodeTextField.java` | [495cce54](https://github.com/freeplane/freeplane/commit/495cce542ed52e0a5d13c6a5f64987a85a64bcbe) |
| 2011-03-02 | `feature` | add SetBooleanPropertyAction (relates to show tool tip property) | `SetBooleanPropertyAction.java` | [52fb8709](https://github.com/freeplane/freeplane/commit/52fb8709f9263f3686e727a5ce92d2d03d71b761) |
| 2011-03-02 | `feature` | enable / disable tooltips from view / popup menus, show tooltip direct under the node | `browsemodemenu.xml`, `mindmapmodemenu.xml` +5 | [e82ce7d0](https://github.com/freeplane/freeplane/commit/e82ce7d03bdc727b25c30697216241ebd73bf20e) |
| 2011-02-27 | `fix` | bug fix for opening formula editor | `AbstractTextTransformer.java`, `FormulaTextTransformer.java` | [eb1c2432](https://github.com/freeplane/freeplane/commit/eb1c243288cd05138059f95b89a3662047cbb51e) |
| 2011-02-27 | `feature` | Support for links in attribute values | `Compat.java`, `IconController.java` +7 | [c0eec1fd](https://github.com/freeplane/freeplane/commit/c0eec1fd7e5a315ed2fc51c96575afc2d3626e5b) |
| 2011-02-27 | `feature` | implement update of node numbering after structural changes | `NodeView.java` | [72219846](https://github.com/freeplane/freeplane/commit/72219846e3cb3c5200c0ab3785939c50a8b663f7) |
| 2011-02-27 | `fix` | fix compiler warning due to charset issues | `DictionaryBase.java`, `TaskUtils.java` | [21d096a0](https://github.com/freeplane/freeplane/commit/21d096a0965fa71d256d06eb2a502a4c6d45043b) |
| 2011-02-26 | `fix` | fix compilation problem under old log4j versions | `LogUtils.java` | [f19ed3a5](https://github.com/freeplane/freeplane/commit/f19ed3a51e739a58428837b6b732e0b90effbb36) |
| 2011-02-26 | `fix` | fix HtmlUtils.extractRawBody : use "<body>".length() | `HtmlUtils.java` | [3973983f](https://github.com/freeplane/freeplane/commit/3973983f7787437f68e5e0ca320325e9bd91ed2d) |
| 2011-02-21 | `fix` | bug 966 | `MapView.java` | [bc8a897b](https://github.com/freeplane/freeplane/commit/bc8a897b1a98c46d0d81aae17679b1250d9232e2) |
| 2011-02-21 | `feature` | add feature to add raw text content to xml output | `XMLWriter.java` | [45f55b66](https://github.com/freeplane/freeplane/commit/45f55b6692e48b9823aa8fab4a9ed1f72cac5e5b) |
| 2011-02-17 | `fix` | fix NPE | `ApplicationViewController.java` | [73b2085f](https://github.com/freeplane/freeplane/commit/73b2085fae90936113efe1887094524bae23c15a) |
| 2011-02-16 | `feature` | Delay editor selection for new nodes until first key event comes | `MTextController.java` | [9e2ed464](https://github.com/freeplane/freeplane/commit/9e2ed464fa3bd589304f7ccdc8d21285bb9a417f) |
| 2011-02-13 | `feature` | RemoveEncryption action +  support for encrypted nodes in applet browser | `browsemodemenu.xml`, `EncryptionController.java` +10 | [dafd1df8](https://github.com/freeplane/freeplane/commit/dafd1df83ef9718c56b1b77519c113479cda1361) |
| 2011-02-08 | `feature` | Add attributes from style | `mindmapmodemenu.xml`, `stylemodemenu.xml` +8 | [74705a6a](https://github.com/freeplane/freeplane/commit/74705a6a7d235430ff582a91eb21c5069da54d8f) |
| 2011-02-08 | `fix` | fix NPE | `MainView.java` | [e499db16](https://github.com/freeplane/freeplane/commit/e499db16c311163cee001902ba4af963a97c3cc7) |
| 2011-02-08 | `fix` | fix NPE | `MFileManager.java` | [4d1f390d](https://github.com/freeplane/freeplane/commit/4d1f390d2fe1d03e54b303c0a2b5beae709f7dc6) |
| 2011-02-08 | `fix` | fix format {0}  in i18n properties | `Resources_fr.properties`, `Resources_hr.properties` | [d6013381](https://github.com/freeplane/freeplane/commit/d601338170888febb3182120561165dacecfc20a) |
| 2011-02-08 | `fix` | bug fix: select visible nodes after node deletion | `NodeView.java` | [25df58e8](https://github.com/freeplane/freeplane/commit/25df58e88d8d7b05d76d296bd040086ea67fa859) |
| 2011-02-03 | `feature` | new action OpenUserDirAction (menu: Tools->Open User Directory) opens the user dir in a fi | `mindmapmodemenu.xml`, `MFileManager.java` +2 | [6151bdf7](https://github.com/freeplane/freeplane/commit/6151bdf7fa963f44beeafd2ae76390dd14270c40) |
| 2011-02-02 | `feature` | add new binding 'textUtils' as an alias for TextUtils | `TextUtils.java`, `FreeplaneScriptBaseClass.java` | [2b9cfdac](https://github.com/freeplane/freeplane/commit/2b9cfdacadaaa36445a57915da963657309cd46e) |
| 2011-01-31 | `feature` | create and register TemplateTextTransformer from TextController, implement support for tex | `TemplateTextTransformer.java`, `TextController.java` +1 | [c9d8ea43](https://github.com/freeplane/freeplane/commit/c9d8ea43c037e4db32440541f70116c789d888ea) |
| 2011-01-27 | `fix` | fix NPE | `BitmapImagePreview.java` | [46d1dd7d](https://github.com/freeplane/freeplane/commit/46d1dd7d1ce8fc1aff1b68d2e01bc5e2c3af74a3) |
| 2011-01-24 | `api_change` | 942]: Interface gets unusable with no menu and no open documents | `ToggleMenubarAction.java`, `ApplicationViewController.java` +2 | [02d1a7c8](https://github.com/freeplane/freeplane/commit/02d1a7c8b60e35ca3831d4e296805c4743dcfb24) |
| 2011-01-24 | `feature` | 940]: find (and filter) with > or < operators not working well with text and date Implemen | `TextUtils.java`, `AttributeCompareCondition.java` +4 | [b913c62a](https://github.com/freeplane/freeplane/commit/b913c62ab1563859e70d8d9c4bc6c63e26ff5f2c) |
| 2011-01-24 | `fix` | fix for fix | `AttributeBuilder.java` | [a20152de](https://github.com/freeplane/freeplane/commit/a20152de523eec43527c92a2ba9da1aa970e13e4) |
| 2011-01-24 | `fix` | fix NPE | `AttributeBuilder.java` | [8ad31208](https://github.com/freeplane/freeplane/commit/8ad31208835a6b07fc41508fe9c64450108f05ab) |
| 2011-01-22 | `fix` | Fix automatically reported bugs | `AttributeBuilder.java`, `NodeViewFactory.java` | [a9384b5f](https://github.com/freeplane/freeplane/commit/a9384b5fdfa2cbb9f016b48db9919466124f68ef) |
| 2011-01-22 | `fix` | Fix NPEs (auto bug reporter) | `ExternalResource.java`, `MapViewController.java` | [1d673a66](https://github.com/freeplane/freeplane/commit/1d673a66d68abc62f85745623ad9f787e5742c3f) |
| 2011-01-22 | `fix` | bug fix in TimeManagement: use only one  Calendar instance, set it to all views created by | `TimeManagement.java` | [75082d29](https://github.com/freeplane/freeplane/commit/75082d29463167cbb9c397ddf3a557c676fe97bc) |
| 2011-01-22 | `fix` | bug fix in PersistentNodeHook.toggle | `PersistentNodeHook.java` | [79f1c1ac](https://github.com/freeplane/freeplane/commit/79f1c1ac20f0efc8a460e7d470828c8f0770506e) |
| 2011-01-20 | `fix` | fix indentation | `NodeView.java` | [7274bb9f](https://github.com/freeplane/freeplane/commit/7274bb9f15b83148c1db07552eb2a1e8c9dd3d8a) |
| 2011-01-20 | `feature` | create the user icons directory if it doesn't exist | `IconStoreFactory.java` | [c18d708d](https://github.com/freeplane/freeplane/commit/c18d708d7ea1811826eb94c682f1af4119564147) |
| 2011-01-19 | `fix` | Bug : call newMainView.putClientProperty("NODE_VIEW_CONTENT_POSITION", MAIN_VIEWER_POSITIO | `NodeView.java`, `NodeViewFactory.java` | [70a8eb44](https://github.com/freeplane/freeplane/commit/70a8eb44a87d14cf54aea5bbbac9ef81c165f593) |
| 2011-01-17 | `feature` | 936]: Tooltip window remains when attempting to insert a new node | `MainView.java`, `NodeTooltipManager.java` | [5cf359d6](https://github.com/freeplane/freeplane/commit/5cf359d68a2d77451bb51e34970327c37e4365e6) |
| 2011-01-14 | `api_change` | - make HtmlUtil available in scripts as "global variable" htmlUtils - added HtmlUtils to t | `HtmlUtils.java`, `build.xml` +1 | [ac609888](https://github.com/freeplane/freeplane/commit/ac609888f04a1533158d8869dfa35639a7645dbe) |
| 2011-01-14 | `feature` | add FreeplaneVersion to the API documentation | `FreeplaneVersion.java`, `build.xml` | [f23d0442](https://github.com/freeplane/freeplane/commit/f23d0442f784dc1e71ff69842bd00ce6b61cbac7) |
| 2011-01-13 | `api_change` | complete documentation of scripting api | `UITools.java`, `LogUtils.java` +1 | [54a669cd](https://github.com/freeplane/freeplane/commit/54a669cdd25f327648690b72d1660316912b76db) |
| 2011-01-10 | `fix` | fix "phantom bar" - note divider if note is not shown | `SplitPaneLayoutManagerDecorator.java` | [5c161a13](https://github.com/freeplane/freeplane/commit/5c161a13b52f2c395546ea69c5476109a81653cf) |
| 2011-01-09 | `fix` | fix NPE | `AttributeView.java` | [b5c69d6e](https://github.com/freeplane/freeplane/commit/b5c69d6e7ff64673319e14a20f663c6e88771ae4) |
| 2011-01-09 | `feature` | new panel layouts | `JTripleCalendar.java`, `TimeManagement.java` +1 | [55c0f379](https://github.com/freeplane/freeplane/commit/55c0f379d992e2887021c9db38b9ba5663386a59) |
| 2011-01-09 | `fix` | Debugging / Bug fixing | `AttributePanelManager.java`, `AttributeTable.java` +2 | [bdcfaec8](https://github.com/freeplane/freeplane/commit/bdcfaec867312dd60fc5f37f8418f5c2bab090ee) |
| 2011-01-08 | `fix` | Use icons for submenus. Fix for file->import | `MenuBuilder.java`, `freeplane.properties` | [6ea0ad9b](https://github.com/freeplane/freeplane/commit/6ea0ad9b604bc5b193448c87fc29f287105074a8) |
| 2011-01-08 | `feature` | new icons and hr translation | `AutomaticEdgeColorHookAction.png`, `DecreaseNodeFontAction.png` +16 | [ef32c9fa](https://github.com/freeplane/freeplane/commit/ef32c9faa04283f9837d2ac6b3d39434235f5e61) |
| 2011-01-07 | `feature` | Add JTimeChooser to TimeCondition and JCalendar | `DayDate.java`, `TimeComboBoxEditor.java` +5 | [13073df7](https://github.com/freeplane/freeplane/commit/13073df799520587e2a5c6edd2ef0df0726f9864) |
| 2011-01-05 | `fix` | 926]: Manage filters : crash when "Set name / Cancel" : fix NPE | `AFilterComposerDialog.java` | [f51539f2](https://github.com/freeplane/freeplane/commit/f51539f27e2f6b006f0dfd8231b16777ddaa685c) |
| 2011-01-04 | `fix` | Bug fixes for note editor in split pane | `MNoteController.java`, `ShowHideNoteAction.java` +1 | [9ab244cd](https://github.com/freeplane/freeplane/commit/9ab244cdc4f2997b1a926cef48f033bb6a36a713) |
| 2011-01-02 | `feature` | initial implementation of new style options node numbering and text templates | `NodeStyleController.java`, `NodeStyleModel.java` +10 | [431f2103](https://github.com/freeplane/freeplane/commit/431f21038e18f0bdaacc9afd1c2fad050f0652d8) |
| 2011-01-02 | `feature` | Add new connector options to preferences for setting the standard values | `preferences.xml`, `OptionPanelBuilder.java` +4 | [04f20b6a](https://github.com/freeplane/freeplane/commit/04f20b6a49b135e79071c9a4febc3cd3c94d8c85) |
| 2011-01-02 | `fix` | bug fix: use proper default colors in color picker | `ColorTracker.java`, `ColorProperty.java` +5 | [243f495f](https://github.com/freeplane/freeplane/commit/243f495f94af95063f232e2a1c6ac37ded35b69d) |
| 2011-01-02 | `feature` | New link formatting options : width, transparency | `ColorUtils.java`, `ConnectorModel.java` +12 | [4fa46c76](https://github.com/freeplane/freeplane/commit/4fa46c761a0c16be36b447322bc9545411c25317) |
| 2011-01-01 | `fix` | Bug fix: use only note  related rich text element in mm file in note builder | `NoteBuilder.java` | [a7e3779c](https://github.com/freeplane/freeplane/commit/a7e3779ce17ec2fd97efd058593a555d18e10beb) |

### Dettagli commit con note

**[92e314c2](https://github.com/freeplane/freeplane/commit/92e314c2f79caaff7c500b30d2a7693a9e444d16)** (2011-05-20) — added new option for the locale to use for formatting and scanning data:

> - manage the available list of translations via the build in locales.txt
>  - group the formatting options in a section
>  - new preferences 'widget' named 'languages'


---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-12-30 | `feature` | Change "Page setup..." dialog and add mnemonics to it | `Resources_de.properties`, `PageAction.java` +1 | [fb569031](https://github.com/freeplane/freeplane/commit/fb56903191aa37d63c2344c416cec15ed39a1d39) |
| 2010-12-29 | `fix` | bug fix in FreeplaneToolbar : use only its own layout manager | `FreeplaneToolBar.java` | [5eabbc35](https://github.com/freeplane/freeplane/commit/5eabbc357860f91a3156e1297097a30e3bb42437) |
| 2010-12-29 | `fix` | fix compiler warnings | `AFilterComposerDialog.java`, `ASelectableCondition.java` +11 | [994b1d7e](https://github.com/freeplane/freeplane/commit/994b1d7ec5361b429600512afa9d128f3d66f2ba) |
| 2010-12-29 | `fix` | bug fix : scroll tool tip up | `NodeTooltipManager.java` | [44c05d32](https://github.com/freeplane/freeplane/commit/44c05d326f12670d8e85567f8398f167487d27b0) |
| 2010-12-28 | `fix` | fix typo | `AttributeCompareCondition.java`, `AttributeExistsCondition.java` +34 | [0288b2d1](https://github.com/freeplane/freeplane/commit/0288b2d1d6066022ca3620f4b05cb2656ac5e438) |
| 2010-12-27 | `fix` | fix in NodeView.nodeChanged | `NodeView.java` | [0ff3a80f](https://github.com/freeplane/freeplane/commit/0ff3a80f590eb9abf411d1ab69fb0ead82699a74) |
| 2010-12-26 | `fix` | fix NPE in NodeView | `NodeView.java` | [31178e22](https://github.com/freeplane/freeplane/commit/31178e22bca48884f96d1a9715747b8e64ec68d4) |
| 2010-12-24 | `feature` | 884]: fix class cast exception in new automatic level style action | `NewLevelStyleAction.java` | [ff955045](https://github.com/freeplane/freeplane/commit/ff955045918a4c1f36e30b15909e3d0bfdc6c1f3) |
| 2010-12-24 | `fix` | bug fix: MapView constuctor for style editing: note controller is not available | `MapView.java` | [89f250ce](https://github.com/freeplane/freeplane/commit/89f250ce446c9e28784f447ed985683a1848612e) |
| 2010-12-24 | `fix` | bug fix: update of hierarchical icons on style changes | `HierarchicalIcons.java` | [c3ed20d3](https://github.com/freeplane/freeplane/commit/c3ed20d3a020f5d8d34a623166120293bc19c020) |
| 2010-12-23 | `fix` | bug fix in rendering of long nodes (containing \n) with limited node width | `ZoomableLabel.java` | [2f10efea](https://github.com/freeplane/freeplane/commit/2f10efea6cc861ef7a35eb115f19a35b7dc9bafd) |
| 2010-12-23 | `fix` | fix NPE | `NodeView.java` | [770590bc](https://github.com/freeplane/freeplane/commit/770590bcd2bad720936200407eb5a50b03e4ce0e) |
| 2010-12-19 | `fix` | fix #837: Making a hyperlink to the menu Icons crashes Freeplane -> fixed URI handling | `LinkController.java` | [43d9b427](https://github.com/freeplane/freeplane/commit/43d9b42756471b52d6506534c481b6bddcc08f5c) |
| 2010-12-18 | `feature` | add NodeIdHighlighter | `MapController.java`, `FormulaTextTransformer.java` +5 | [7b52a2fd](https://github.com/freeplane/freeplane/commit/7b52a2fd70ce82ac966121e1b27b428c7677f5b9) |
| 2010-12-18 | `feature` | fix: do not add attribute "FOLDED" to root stylenode | `NodeWriter.java` | [6fc5df91](https://github.com/freeplane/freeplane/commit/6fc5df91581a1dc2ff4135d0b222f1c5de574148) |
| 2010-12-18 | `fix` | fix NPE | `IconStore.java` | [c4daf051](https://github.com/freeplane/freeplane/commit/c4daf0513691085b03261d2083bcb51f7f662d10) |
| 2010-12-18 | `fix` | bug fix: NPE | `FButtonBar.java` | [c44046e0](https://github.com/freeplane/freeplane/commit/c44046e08236bea54b6a5b0f0501f02ba48ca2a4) |
| 2010-12-18 | `fix` | bug fix continued | `AttributeViewTypeAction.java`, `ModelessAttributeController.java` +1 | [49e3a88e](https://github.com/freeplane/freeplane/commit/49e3a88efcbba603dba22b17d550a588adc7f64b) |
| 2010-12-18 | `fix` | fix NPE if editing is canceled by map change / closing | `MTextController.java`, `EditNodeTextField.java` | [fe4dbdad](https://github.com/freeplane/freeplane/commit/fe4dbdadca3879a70f0cd732e7289ec3fb4ef42e) |
| 2010-12-18 | `feature` | Refactoring for AutoCompletion PLug-in : create all JEditorPane  instances in MTextControl | `NoteModel.java`, `DetailTextModel.java` +10 | [cd622d14](https://github.com/freeplane/freeplane/commit/cd622d14427091cd4cda503f5ae20908e5d712cf) |
| 2010-12-13 | `fix` | Bug fix in replacement for plain text | `NodeList.java` | [5d5cba9c](https://github.com/freeplane/freeplane/commit/5d5cba9c77b6c54b0511fb2f8502b76540aaadf4) |
| 2010-12-12 | `feature` | add checks for investigating NPE in NodeView.addContent | `NodeView.java` | [70692db1](https://github.com/freeplane/freeplane/commit/70692db1f6d1df1f21cd25d056510c07191e7bd2) |
| 2010-12-12 | `fix` | fix NPE in BlinkingNodeHook | `BlinkingNodeHook.java` | [4f0722e7](https://github.com/freeplane/freeplane/commit/4f0722e71e7697948ba62ce65810b5a3e7861336) |
| 2010-12-12 | `fix` | fix NPE in ConnectorExistsCondition | `ConnectorExistsCondition.java` | [8fe1c11f](https://github.com/freeplane/freeplane/commit/8fe1c11fc3ca88e32c573bbc55841c87afd2d422) |
| 2010-12-11 | `fix` | bug fixes for displaying and configuration of note editor on mode and map change | `ViewController.java`, `MNoteController.java` +6 | [b79395a0](https://github.com/freeplane/freeplane/commit/b79395a04338229a59ad3ef750c6f06a1fdc2b5a) |
| 2010-12-11 | `feature` | Support drag and drop of files if no map is open | `FileOpener.java`, `ApplicationViewController.java` +1 | [2919fd6a](https://github.com/freeplane/freeplane/commit/2919fd6aed0fd5358a0e552f5cd47e3d9577a980) |
| 2010-12-11 | `fix` | Bug fix in map layout | `NodeView.java`, `NodeViewLayoutAdapter.java` +1 | [1f0b8cb4](https://github.com/freeplane/freeplane/commit/1f0b8cb4d7229de342617347d1bcf9145f0557c6) |
| 2010-12-10 | `fix` | bug fix: display icons on the left side of node inline editor for left nodes too. | `EditNodeTextField.java` | [d99d6ca0](https://github.com/freeplane/freeplane/commit/d99d6ca0597bd162a3acbdcab9c7f6a9e04bec02) |
| 2010-12-10 | `fix` | 867]: Imported branch meshed up at screen Bug fixes for import branch actions | `MapController.java`, `ImportBranchAction.java` +2 | [1900e7f8](https://github.com/freeplane/freeplane/commit/1900e7f891ff3259b4522ec83f0f5603e3e4b99b) |
| 2010-12-05 | `fix` | bug fix: avoid NPE | `EditNodeTextField.java` | [477510f3](https://github.com/freeplane/freeplane/commit/477510f32026a25fe0fc8c534187c4bce021f5f9) |
| 2010-12-05 | `fix` | fix call of MacChanges from Compat | `Compat.java` | [9de736e2](https://github.com/freeplane/freeplane/commit/9de736e227448a15b7c2b5e485593236d34accdd) |
| 2010-12-04 | `feature` | applied new format-translation task to remove empty lines | `Resources_ar.properties`, `Resources_ca.properties` +26 | [d5e381fa](https://github.com/freeplane/freeplane/commit/d5e381fa4cd82a84691919001155f38861820fc8) |
| 2010-12-04 | `fix` | Bug fixes in style copiers for MEdgeController and MLogicalStyleController | `MEdgeController.java`, `MLogicalStyleController.java` | [1c8e092b](https://github.com/freeplane/freeplane/commit/1c8e092b382c13cd480e3c697387314da5a8dfe9) |
| 2010-12-04 | `fix` | bug fix: Perform style change rollback if style editor is closed with yes/no/cancel dialog | `SModeController.java` | [54704539](https://github.com/freeplane/freeplane/commit/5470453994a6f9afa192658cd7facb2962d624aa) |
| 2010-12-01 | `feature` | 847]: New style not attached to the correct branch | `LogicalStyleController.java`, `NewUserStyleAction.java` +1 | [202fc53f](https://github.com/freeplane/freeplane/commit/202fc53fa6c2e6f68ed2b6cf2ef1307f537ed96c) |
| 2010-12-01 | `fix` | Bug fix : use class StyleNamedObject instead of NamedObject in Builder / StyleCondition | `LogicalStyleController.java`, `StyleCondition.java` +2 | [cabbc5b1](https://github.com/freeplane/freeplane/commit/cabbc5b124b85ae526d716388dede1e1b9372349) |
| 2010-11-30 | `fix` | Bug fix in layout of EditNodeTextField | `EditNodeTextField.java` | [1e303a09](https://github.com/freeplane/freeplane/commit/1e303a09a40f3d7e12a6b0f1cdaa0698fe597928) |
| 2010-11-29 | `fix` | bug fix: paint line uinder the fork view,  do not overlap node text | `ForkMainView.java`, `MainView.java` +1 | [dfa441e8](https://github.com/freeplane/freeplane/commit/dfa441e8acdd4fa846520462fc0740415cb18060) |
| 2010-11-28 | `feature` | new icons from Predrag | `export.png`, `import.png` +5 | [5f14886a](https://github.com/freeplane/freeplane/commit/5f14886aa55fde0a42948b145385444b3551104a) |
| 2010-11-28 | `feature` | Enable rich text editing features in inline editor. SimplyHTML updated to version 0.13.8 | `SimplyHTML.jar`, `preferences.xml` +14 | [c4ea1ac1](https://github.com/freeplane/freeplane/commit/c4ea1ac1393640dc2ce62d30289d5a2186872320) |
| 2010-11-27 | `feature` | Use separate options for showing rich text editor for entering new and editing old nodes | `Resources_de.properties`, `Resources_es.properties` +22 | [e4210fb2](https://github.com/freeplane/freeplane/commit/e4210fb27a5e6c3af4de19edd94c43ab32944360) |
| 2010-11-26 | `feature` | enable menu icons in SelectMenuItemDialog (before it only worked if Freeplane was started  | `MenuUtils.java`, `IconNotFound.java` +2 | [20fdf9e8](https://github.com/freeplane/freeplane/commit/20fdf9e84eb32d5521012216745ed5e868f8b6e8) |
| 2010-11-24 | `fix` | bug fix: QuickFilterAction, QuickFindAction should do nothing if no valid condition is ent | `QuickFilterAction.java`, `QuickFindAction.java` | [35bd63ac](https://github.com/freeplane/freeplane/commit/35bd63acb041c5e7c0cf987d4f2b8ea3f6d9a5ee) |
| 2010-11-24 | `fix` | bug fix : NodeContainsCondition should ignore letter case | `NodeContainsCondition.java` | [92c7881d](https://github.com/freeplane/freeplane/commit/92c7881df8a34d37692611d4d34204df0e37a272) |
| 2010-11-24 | `fix` | bug fix: the closest child selection (NodeView.getPreferredVisibleChild) | `NodeView.java` | [6a9c4a35](https://github.com/freeplane/freeplane/commit/6a9c4a355371b53d89c16a3333f64690b536b056) |
| 2010-11-20 | `feature` | new icons and Resources_hr.properties from Predrag | `copy_id.png`, `edit_details.png` +11 | [a49003aa](https://github.com/freeplane/freeplane/commit/a49003aa4760ef80a952e0014291cf975670ee22) |
| 2010-11-20 | `feature` | bug 821:  add backslash to <base href... /> element | `MainView.java` | [06f91567](https://github.com/freeplane/freeplane/commit/06f915670a7ec2fada5b64573cf4b17bda85e568) |
| 2010-11-16 | `fix` | bug fixes in text Conditions | `NodeContainsCondition.java`, `NodeMatchesRegexpCondition.java` | [f8442038](https://github.com/freeplane/freeplane/commit/f8442038aa21a7f4e9792c926e01dff9e0c9ac5a) |
| 2010-11-15 | `fix` | bug fix: register AttributeTableModelDecoratorAdapter as node change listener only on the  | `ViewController.java`, `INodeView.java` +4 | [4a256e13](https://github.com/freeplane/freeplane/commit/4a256e132ae7760351cba7efed57283ae16a6fab) |
| 2010-11-14 | `fix` | fix: replace calls of NodeModel.toString by NodeModel.getText | `MindMapHTMLWriter.java`, `FindAction.java` +2 | [24615b15](https://github.com/freeplane/freeplane/commit/24615b1594fe138433d58ab90aad903d038577a3) |
| 2010-11-14 | `fix` | bug fix: updating of formula results in AttributeTable | `AttributeTable.java`, `AttributeTableModelDecoratorAdapter.java` +3 | [0c6585ac](https://github.com/freeplane/freeplane/commit/0c6585acbaedf08efd71739ade958506d7be94c8) |
| 2010-11-14 | `fix` | bug fix: update formula results on node change, not during the painting | `AttributeTableCellRenderer.java`, `AttributeTableModelDecoratorAdapter.java` +3 | [7994ddab](https://github.com/freeplane/freeplane/commit/7994ddabad2ae66d939c98036d3b618b96211121) |
| 2010-11-13 | `feature` | Fix #804: Scripting errors due to missing read permissions: | `IValidator.java`, `OptionPanel.java` +10 | [13a5bddc](https://github.com/freeplane/freeplane/commit/13a5bddc10aa653f528995994a6ce478a6b1e9ba) |
| 2010-11-13 | `feature` | 808]: root node named "New Mindmap" in french | `standard.mm`, `MFileManager.java` | [163ca7fc](https://github.com/freeplane/freeplane/commit/163ca7fc9d0d05df69311e63b75f1a6abce32b8a) |
| 2010-11-13 | `feature` | Add format-translation to jortho build and apply. | `build.xml`, `resource.properties` +10 | [f5692d1d](https://github.com/freeplane/freeplane/commit/f5692d1dcabf1fdbea597cf40e796568cc0b961e) |
| 2010-11-13 | `feature` | add dutch translation to JOrtho | `resource_nl.properties` | [f2ef8fa6](https://github.com/freeplane/freeplane/commit/f2ef8fa616b734d04dcbb23eda41fa138a3f9d79) |
| 2010-11-04 | `feature` | another Jortho synchronisazion issue: add highlighters in EventQueue thread only | `AutoSpellChecker.java` | [e696a29a](https://github.com/freeplane/freeplane/commit/e696a29a1926979cd25f032a1f777dd033342d8b) |
| 2010-11-04 | `fix` | bug fix: RedZigZagPainter should restore stroke after painting | `RedZigZagPainter.java` | [8aaada28](https://github.com/freeplane/freeplane/commit/8aaada28dd6817f77c128d1a82bff7d5135a74fa) |
| 2010-11-04 | `fix` | bug fix: freeplane did not start if unsupported language code was set in properties | `ResourceBundles.java` | [6901643c](https://github.com/freeplane/freeplane/commit/6901643c1a627ead85bf7357fb7d95580076de74) |
| 2010-11-02 | `feature` | Added new icons for previous/next map, previous/next node, undo and redo | `MoveTo_NextMM.png`, `MoveTo_NextNode.png` +5 | [8ff50190](https://github.com/freeplane/freeplane/commit/8ff5019011ba9ebdcd0d6d6589e190a1d7d148f4) |
| 2010-11-02 | `fix` | removed some unused imports and solved a bug that enabled NavigationNextMapAction and Navi | `ApplicationViewController.java` | [30b40b3d](https://github.com/freeplane/freeplane/commit/30b40b3d83a9c5c76ccf0612a100ffe03e5f61d9) |
| 2010-11-01 | `feature` | removed Java 1.6 construct - FIXME: re-enable once Freeplane switches to 1.6 | `AttributeTable.java` | [9dc5b999](https://github.com/freeplane/freeplane/commit/9dc5b9996be357037cbae0b20c1480d8896ce975) |
| 2010-10-31 | `feature` | Formula plugin: Display evaluated formulas...  - in attribute table  - in attribute toolti | `NodeAttributeTableModel.java`, `ITextTransformer.java` +5 | [3677d7a3](https://github.com/freeplane/freeplane/commit/3677d7a3048dd03dfb049168d1f417657d6740ff) |
| 2010-10-31 | `fix` | bug fix: text field editors not correctly shown in find dialog /  filter condition dialog | `LinkConditionController.java`, `NoteConditionController.java` +1 | [aa781d90](https://github.com/freeplane/freeplane/commit/aa781d909c58c6ef358fa07778e501f4a54c782b) |
| 2010-10-31 | `feature` | optimization: do not set map zoom if the old value is equal to the new one | `MapViewController.java` | [0fd134dd](https://github.com/freeplane/freeplane/commit/0fd134dd8b95012750f8a3a5a61f0aea178f2b9a) |
| 2010-10-30 | `feature` | start editor after new parent was created | `NewParentNode.java` | [456018e6](https://github.com/freeplane/freeplane/commit/456018e6cce862359cd50c90b0a53e513b82fc84) |
| 2010-10-29 | `fix` | Fix handling of mouse events by map, node and details views | `DelayedMouseListener.java`, `MModeControllerFactory.java` +5 | [24512383](https://github.com/freeplane/freeplane/commit/2451238352d926905a3eddf2c35b04324778c4b5) |
| 2010-10-28 | `feature` | Add icons for rating | `Resources_de.properties`, `freeplane.properties` +11 | [532e324f](https://github.com/freeplane/freeplane/commit/532e324f1f708dad73291d5aaa7f5ca161c06214) |
| 2010-10-28 | `feature` | added new formula icon by Predrag Cuklin installed it as an icon for EvaluateAllAction | `formula.png`, `defaults.properties` | [519d314f](https://github.com/freeplane/freeplane/commit/519d314faf6f684e1eeb21a2ade4027c1652d488) |
| 2010-10-28 | `fix` | fix compile error with java 5 | `NodeTooltipManager.java` | [1c5a39a9](https://github.com/freeplane/freeplane/commit/1c5a39a9fe44788517337b607e93fb52afc73f50) |
| 2010-10-27 | `fix` | bug fix: showTipWindow if the mouse returns to the same node | `NodeTooltipManager.java` | [8ead80ba](https://github.com/freeplane/freeplane/commit/8ead80ba74b6126645ae8d6947bc55db6da9f79b) |
| 2010-10-27 | `fix` | bug fix: do not display tooltips if they do not contain text | `NodeModel.java`, `NodeTooltip.java` | [aaa4f221](https://github.com/freeplane/freeplane/commit/aaa4f221e7ad677cc2b527fa297ca52bb3b4bd75) |
| 2010-10-27 | `fix` | Tooltip location + tooltip bug fixes | `MainView.java`, `NodeTooltip.java` +1 | [d9873b99](https://github.com/freeplane/freeplane/commit/d9873b997d1645b6cada5f5fe2cd5e910c387a42) |
| 2010-10-23 | `fix` | bug fix NPE in org.freeplane.view.swing.map.MapView.anchorToSelected(NodeView, float, floa | `MapView.java` | [fbec92d6](https://github.com/freeplane/freeplane/commit/fbec92d636e7a7b27e9ff08ae882a56be6ebeba0) |
| 2010-10-23 | `feature` | Add ApplySelectedViewConditionAction to filterToolbar | `FilterController.java` | [7dc6bd67](https://github.com/freeplane/freeplane/commit/7dc6bd677c7169fbc883b7b35b523096ba0ad23a) |
| 2010-10-23 | `fix` | related bug fixes | `ConjunctConditions.java`, `DisjunctConditions.java` +3 | [cffe256a](https://github.com/freeplane/freeplane/commit/cffe256a64d710fab273f0aec3a6526541c88f05) |
| 2010-10-23 | `feature` | Refactor condittions Add equals and hashCode methods using org.apache.commons.lang.builder | `AttributeCompareCondition.java`, `AttributeConditionController.java` +70 | [dab47919](https://github.com/freeplane/freeplane/commit/dab479199e537868bcb48e7623ec58eeb212afe0) |
| 2010-10-22 | `feature` | add missing icons for SimplyHTML | `Bold_on16.png`, `Italic_on16.png` +1 | [7e138a4d](https://github.com/freeplane/freeplane/commit/7e138a4da77c129d73acc7861f3f819123743656) |
| 2010-10-22 | `feature` | Allow use of html editor for new nodes | `MClipboardController.java`, `EditAction.java` +1 | [b2e3a179](https://github.com/freeplane/freeplane/commit/b2e3a179d6506bac750527af30052f5f67fe16b0) |
| 2010-10-21 | `feature` | removed dead code: path does not support attribute defaultValue | `preferences.xml` | [e9e6fcf8](https://github.com/freeplane/freeplane/commit/e9e6fcf8ce74dc990d2dbfc654d77e25341f708f) |
| 2010-10-17 | `fix` | Tooltips for node, details. Fix tooltip order established. | `NodeAttributeTableModel.java`, `MapController.java` +7 | [108710e3](https://github.com/freeplane/freeplane/commit/108710e3a49abaa670ff514f70c21487221b6637) |
| 2010-10-17 | `fix` | Bug fix: tooltip for notes after map loading | `NoteBuilder.java` | [05407f31](https://github.com/freeplane/freeplane/commit/05407f3117dc1f5f8c63b45fa67ad99b85e10fea) |
| 2010-10-16 | `feature` | add node details to toxhtml.xsl | `toxhtml.xsl` | [b1b49e8f](https://github.com/freeplane/freeplane/commit/b1b49e8f6c32ae8b71d21fcbb7b2ddc82ddb39bb) |
| 2010-10-16 | `feature` | 586]: request: new functionality in Icon Selection : display use icons first in "Select Ic | `IconSelectionPlugin.java`, `MModeControllerFactory.java` | [3fe3ac2b](https://github.com/freeplane/freeplane/commit/3fe3ac2bbde90294c4cb1c0bbc5b811b0fab0739) |
| 2010-10-16 | `feature` | only add the display_node_id listener if configured in the preferences | `MMapController.java` | [1c55f979](https://github.com/freeplane/freeplane/commit/1c55f9792c7aaddc96b0f386a66f4a194e34dd26) |
| 2010-10-16 | `feature` | new option panel property type PathProperty | `OptionPanelBuilder.java`, `PathProperty.java` +1 | [3e011497](https://github.com/freeplane/freeplane/commit/3e011497c14fc87af3056162d77a2c4caef4c073) |
| 2010-10-13 | `fix` | fix NPE | `NodeList.java` | [7c89f24a](https://github.com/freeplane/freeplane/commit/7c89f24a019ca3cbee3e7089d23cf70274f7f9bf) |
| 2010-10-13 | `feature` | new preference 'Use single directory for backup files' | `history_en.txt`, `preferences.xml` +5 | [1f2b30d9](https://github.com/freeplane/freeplane/commit/1f2b30d93fb6206cd53a8b7d524825bccdf2c9c9) |
| 2010-10-12 | `fix` | Bug fix : FormulaTextTransformer removed HTML formatting even if no script | `MainView.java`, `FormulaTextTransformer.java` +1 | [833005e6](https://github.com/freeplane/freeplane/commit/833005e60e6e8531b73311d27b3b0e7683e87a2a) |
| 2010-10-12 | `feature` | - read plugin default from file defaults.properties to avoid hardcoded defaults. Used in s | `ResourceController.java`, `AppletResourceController.java` +8 | [1309850d](https://github.com/freeplane/freeplane/commit/1309850ddbc06d0a413751be29bb975264bbb548) |
| 2010-10-11 | `fix` | Bug fix : NPE | `ConditionalStyleModel.java` | [0326ce1f](https://github.com/freeplane/freeplane/commit/0326ce1f7c66ee632448c6107c83282057fb0f6d) |
| 2010-10-11 | `fix` | Bug fix for saving conditional styles | `MapStyle.java` | [062653aa](https://github.com/freeplane/freeplane/commit/062653aacf063348dac21dc432f557488595c611) |
| 2010-10-10 | `fix` | Bug fix in freeplane/src/org/freeplane/main/osgi/ActivatorImpl.java : load all plug-ins be | `ActivatorImpl.java` | [b4304a68](https://github.com/freeplane/freeplane/commit/b4304a68f5a862a8e816bbdc3088780d81ad98fd) |
| 2010-10-09 | `fix` | move constants FILTER_NODE, FILTER_DETAILS and FILTER_PARENT to TextController fix complie | `IgnoreCaseNodeContainsCondition.java`, `NodeContainsCondition.java` +6 | [a4051418](https://github.com/freeplane/freeplane/commit/a4051418841190480a4a1b6e78dd77ef711cf405) |
| 2010-10-09 | `fix` | Bug fix: in NodeView: wrong mouse listener was attached to DetailsView | `NodeView.java` | [54ddb714](https://github.com/freeplane/freeplane/commit/54ddb7144ba46552fedd1bff2b3b1c29d18a9da9) |
| 2010-10-04 | `feature` | Add hide/show details to browse mode Drag map if detail view is being dragged | `DelayedMouseListener.java`, `TextController.java` +2 | [8010b368](https://github.com/freeplane/freeplane/commit/8010b3680da6d954235f24a73e7580bad7428106) |
| 2010-10-04 | `feature` | Add edit detail actions to the node pop-up menu | `mindmapmodemenu.xml` | [36e0b75a](https://github.com/freeplane/freeplane/commit/36e0b75a71456975cb29e7dcdf8a26d26ee042c7) |
| 2010-10-03 | `fix` | Fix layout for long textes in BNodeNoteViewer: use JEditorPane instead of JLabel | `BNodeNoteViewer.java` | [d3252f78](https://github.com/freeplane/freeplane/commit/d3252f7833ff96ad7341ef8a6d9a7b357e516afc) |
| 2010-10-03 | `feature` | - handle circular references - new option 'don't mark formula nodes' | `MainView.java`, `Resources_en.properties` +8 | [35e29691](https://github.com/freeplane/freeplane/commit/35e296913e602a3c3e037b49aebb9eefaad990f8) |
| 2010-09-19 | `fix` | Bug fixes for obtaining edge style informations | `EdgeController.java` | [553f0853](https://github.com/freeplane/freeplane/commit/553f08534c0f52c6b692a9704781a584e6e2588b) |
| 2010-09-19 | `fix` | Bug fixes for obtaining node style informations | `NodeStyleController.java` | [25fc9672](https://github.com/freeplane/freeplane/commit/25fc967244264d7ae9075d934197d8e8089bdf70) |
| 2010-09-19 | `feature` | Add CopyFormat and PAsteFormat actions to tool bar and node popup of the style editor dial | `stylemodemenu.xml` | [201fbd9b](https://github.com/freeplane/freeplane/commit/201fbd9b0e61dc3f6daa058796631574ab137c0b) |
| 2010-09-18 | `feature` | add AutomaticLayout check box to StyleEditorPanel | `PersistentNodeHook.java`, `LogicalStyleController.java` +2 | [5594faf8](https://github.com/freeplane/freeplane/commit/5594faf8fd98491dc4f4e838d61657260a1f6c3b) |
| 2010-09-17 | `feature` | Implement AutomaticLayout using property handlers for styles | `PersistentNodeHook.java`, `ConditionalStyleModel.java` +1 | [06204e34](https://github.com/freeplane/freeplane/commit/06204e341f7d61cdd2ab47881713ab40b304fbde) |
| 2010-09-17 | `feature` | Refactoring: implement LogicalStyleController.getStyles using property handlers | `LogicalStyleController.java` | [964bd393](https://github.com/freeplane/freeplane/commit/964bd3938c04d7fd448d0cde6f987616b26d3fda) |
| 2010-09-15 | `feature` | add "stop processing" column to conditional styles | `ConditionalStyleModel.java`, `LogicalStyleController.java` +4 | [55add967](https://github.com/freeplane/freeplane/commit/55add967b85e4c8f7c9de2f6fb919ae22792ecdb) |
| 2010-09-15 | `feature` | bug fix if add conditional style dialog is cancelled | `ManageConditionalStylesAction.java` | [41ab4e77](https://github.com/freeplane/freeplane/commit/41ab4e77c9924569575a1b094f02c42bc961946a) |
| 2010-09-15 | `feature` | Refactor: let all styles implement IStyle | `CloudController.java`, `EdgeController.java` +20 | [637e7f05](https://github.com/freeplane/freeplane/commit/637e7f05ba39b32bc862f2a581cd5f899fa279c3) |
| 2010-09-06 | `fix` | bug fixes for copyStyle : update map background, use default style if no style was set in  | `MapStyle.java`, `MapView.java` | [8b277333](https://github.com/freeplane/freeplane/commit/8b27733319338e8cd9ad12858b68f1319252594b) |
| 2010-09-04 | `feature` | add putExtension methods to ExtensionContainer bug fixes in initializing MapStyleModel | `ExtensionContainer.java`, `MapModel.java` +3 | [a45dc9df](https://github.com/freeplane/freeplane/commit/a45dc9df7b9930ce365f64ce74dd43af11f849e8) |
| 2010-09-04 | `fix` | bug fix for 676]: Search and replace function ignore upper / lower case | `FlatNodeTableFilterModel.java` | [0eb64a47](https://github.com/freeplane/freeplane/commit/0eb64a47b4482ea54862ae604c6ca195b53d84fc) |
| 2010-09-04 | `feature` | add file SkipException.java | `SkipException.java` | [9e427205](https://github.com/freeplane/freeplane/commit/9e42720564d7316f432b3efa405f74646ee3ee26) |
| 2010-09-04 | `fix` | fix in undo for EditStylesAction | `EditStylesAction.java` | [70af7039](https://github.com/freeplane/freeplane/commit/70af70397b30202794f5a58f7d6192c19086f6e7) |
| 2010-08-29 | `feature` | add quit action (hot key ESCAPE) to style editor dialog | `stylemodemenu.xml`, `Controller.java` +4 | [2a5bb064](https://github.com/freeplane/freeplane/commit/2a5bb0642fdd9a99656f347929624bc2066088ab) |
| 2010-08-29 | `feature` | add option standard_template and remove option patternsfile to preferences dialog | `Resources_ar.properties`, `Resources_ca.properties` +35 | [63908172](https://github.com/freeplane/freeplane/commit/63908172714346d1a63552b3ebca1c8d0997e355) |
| 2010-08-28 | `feature` | Improvements in style editor dialog:  handling of close dialog  new style action transform | `stylemodemenu.xml`, `ModeController.java` +7 | [f16ca717](https://github.com/freeplane/freeplane/commit/f16ca71771f122b263ed5030119291b59f10a3b9) |
| 2010-08-26 | `feature` | large script API overhaul mostly for formula use: * Script API / Attribute   - deprecated: | `ViewController.java`, `FreeplaneIconUtils.java` +22 | [40c1e149](https://github.com/freeplane/freeplane/commit/40c1e14960af350fc09e1936e4a113717e37629a) |
| 2010-08-24 | `fix` | bug fix for style map in undo action | `RedoAction.java`, `UndoAction.java` | [d94f847e](https://github.com/freeplane/freeplane/commit/d94f847e24a4e10682c2c3640c21ab706df1d3d3) |
| 2010-08-24 | `fix` | NPE bug fixes, also FreeplaneStarter, ActivatorImpl, SingleInstanceManager fixes | `StyleEditorPanel.java`, `FreeplaneStarter.java` +3 | [df906bd7](https://github.com/freeplane/freeplane/commit/df906bd7ec14e26d72d45ac6e246b3156d25cd10) |
| 2010-08-18 | `feature` | - allow for node ids used as variables: ID_1234567.text returns the text   of the node wit | `FreeplaneSecurityManager.java`, `FreeplaneScriptBaseClass.java` +1 | [6fefd4d7](https://github.com/freeplane/freeplane/commit/6fefd4d732b57c9b75537cdee07d4e0b0611e2df) |
| 2010-08-18 | `fix` | fix some compiler warnings with Eclipse 3.6 | `ResourceBundles.java`, `BitmapImagePreview.java` +7 | [32e5b086](https://github.com/freeplane/freeplane/commit/32e5b086a8d68f5b15b7b5e9c67ce89f9c750c2d) |
| 2010-08-14 | `feature` | new fix for 724]: Preeplane alpha version does not display Japanese letters of nodes corre | `NodeStyleModel.java`, `MapStyleModel.java` +1 | [85155722](https://github.com/freeplane/freeplane/commit/8515572204483747580344d6c4422e18a3025826) |
| 2010-08-08 | `fix` | xslt removing style info (back to freeplane 1.1, freemind) + bug fixes in CloudBuilder, Ed | `mm2freeplane1_1-mm.xsl`, `mm2xbel.xsl` +5 | [d55eef14](https://github.com/freeplane/freeplane/commit/d55eef1454b7e365b9d49337ee17a1b66163e1f2) |
| 2010-08-01 | `fix` | Preparations for spreadsheet/formula plugin: | `Resources_es.properties`, `Resources_fr.properties` +13 | [2da72e95](https://github.com/freeplane/freeplane/commit/2da72e95375cec64654569b0fdd0af6ad81cc24c) |
| 2010-07-30 | `feature` | take application data location from environment variable for windows os + use new user fol | `ApplicationResourceController.java`, `FreeplaneStarter.java` +7 | [c2918488](https://github.com/freeplane/freeplane/commit/c291848869ff446ce6e282a0227c3357ad5e6b05) |
| 2010-07-29 | `feature` | Check for exceptions when saving hooks, add runtime checks to XMLElement | `PersistentNodeHook.java`, `XMLElement.java` | [b3503a24](https://github.com/freeplane/freeplane/commit/b3503a2466cddd27b0da9768c81c44dcb5ea701d) |
| 2010-07-29 | `feature` | 714]: Exception on saving which truncates the file : do not create latex extension without | `PersistentNodeHook.java`, `LatexNodeHook.java` | [bb606d13](https://github.com/freeplane/freeplane/commit/bb606d137b3bc01bb0a5c0c5e902fd28d8c4eb81) |
| 2010-07-27 | `feature` | make getTextTransformers() public, add removeTextTransformer | `TextController.java` | [22a1dd20](https://github.com/freeplane/freeplane/commit/22a1dd20961c0a49d5e9411bc250fe0157c9209e) |
| 2010-07-27 | `fix` | bug fix: getNodeLevel did not work in CopySingle | `NodeModel.java` | [09f36cc2](https://github.com/freeplane/freeplane/commit/09f36cc24dc74ffa9efa0290cb8c862c45ca7863) |
| 2010-07-25 | `feature` | applet synchronization + enable all folding actions in applet | `browsemodemenu.xml`, `mindmapmodemenu.xml` +11 | [b9f1933f](https://github.com/freeplane/freeplane/commit/b9f1933f027e4ce8743ecd3ed5b25db565f37b0d) |
| 2010-07-24 | `feature` | add parameter ResourceController to SingleInstanceManager | `FreeplaneStarter.java`, `SingleInstanceManager.java` +1 | [7ff5f600](https://github.com/freeplane/freeplane/commit/7ff5f6008b437f1c3b4c422b2202d36ff41b5093) |
| 2010-07-24 | `fix` | bug fixes: 1. synchronization of different applets 2. install node drag / grop listeners f | `FreeplaneApplet.java`, `NodeView.java` +5 | [d179a27d](https://github.com/freeplane/freeplane/commit/d179a27d3b39e8ede948b922a88cd51fe08086a6) |
| 2010-07-18 | `fix` | bug fixes in AppletResourceController, FreeplaneApplet and Browser note viewer | `BNodeNoteViewer.java`, `AppletResourceController.java` +1 | [4759897a](https://github.com/freeplane/freeplane/commit/4759897a02a12a2ffe40cb27f408b2eb256207bf) |
| 2010-07-18 | `fix` | bug fix for applet: do not return file for map if url protocol is not "file" | `MapModel.java` | [f4ea45e1](https://github.com/freeplane/freeplane/commit/f4ea45e199615636b6058afe1ef04d11bea60b38) |
| 2010-07-17 | `fix` | use fix order of content viewers | `ExternalResource.java`, `ViewerController.java` +4 | [29ff1989](https://github.com/freeplane/freeplane/commit/29ff198914b7f15b19fbc32594de1b693242fc4b) |
| 2010-07-17 | `fix` | bug fix in NewParentNode action : copy selection before sorting | `NewParentNode.java` | [8c33f4c8](https://github.com/freeplane/freeplane/commit/8c33f4c8ea4b8caa54731490728c0ccb791f33fd) |
| 2010-07-03 | `fix` | bug fix for node up / node down action in direct root children for outline view | `NodeUpAction.java` | [4b4d3f68](https://github.com/freeplane/freeplane/commit/4b4d3f6883a7a0e17fec1033b6a4acd0d36a42ee) |
| 2010-06-26 | `feature` | add hook ITextTransformer to ModeController | `ITextTransformer.java`, `ModeController.java` +1 | [adb9675e](https://github.com/freeplane/freeplane/commit/adb9675e7009182e87b43d96d319cac525bfd8f3) |
| 2010-06-25 | `feature` | - move scripting option panel configuration to new tab 'Plugins' - add scripting configura | `preferences.xml`, `ConfigurationUtils.java` +5 | [aad11d2f](https://github.com/freeplane/freeplane/commit/aad11d2fee37e0696598df89513d40de363ca1b3) |
| 2010-06-22 | `fix` | fix deprecation warning | `NodeModel.java`, `MNoteController.java` | [a6838952](https://github.com/freeplane/freeplane/commit/a68389529bc288d01f96b2872cb61c7d5121cbc1) |
| 2010-06-21 | `fix` | bug fixes for ConditionalStyleTable | `AFilterComposerDialog.java`, `ConditionalStyleModel.java` +3 | [7bd47e16](https://github.com/freeplane/freeplane/commit/7bd47e165bd9620a5a92212af5bbbbdeba136de0) |
| 2010-06-20 | `feature` | #343: single instance mode: add forgotten file | `preferences.xml` | [12356f64](https://github.com/freeplane/freeplane/commit/12356f64d98f7d3c5c2a774ee451131fec05206c) |
| 2010-06-13 | `feature` | 665]: After a contextual "Copy" the "Paste" command creates a new node | `EditNodeBase.java` | [889b349d](https://github.com/freeplane/freeplane/commit/889b349d80daaf8543ffe60084e2887accf02bcc) |
| 2010-06-11 | `fix` | 662]: Printing all works wrongly after printing defined page(s) (windows java bug) | `PrintController.java` | [e93dcffb](https://github.com/freeplane/freeplane/commit/e93dcffb1a6ca6b04ea8414b2b2ca8c21ab3db42) |
| 2010-06-10 | `fix` | Refactoring and bug fix in PrintController: 662]: Printing all works wrongly after printin | `PageAction.java`, `PrintAction.java` +1 | [6fa024ac](https://github.com/freeplane/freeplane/commit/6fa024ac4037b1e4de98e9ab06cf0caf7b0b51a3) |
| 2010-06-07 | `feature` | NewerFileRevisionsFoundDialog: - remove separate Replace button - enable selection of the  | `MFileManager.java`, `NewerFileRevisionsFoundDialog.java` +1 | [2239e197](https://github.com/freeplane/freeplane/commit/2239e197c4bf4138bf76d2dd45f8a96d6380b8d1) |
| 2010-06-05 | `feature` | Bug fix: new child action does not work after styles have been edited | `MMapController.java` | [806f5922](https://github.com/freeplane/freeplane/commit/806f59228c747d5ed89be4a6f4ec464ef16c3a28) |
| 2010-06-04 | `fix` | Bug fix: call centerNode only after the MapView was laid out | `MapView.java` | [e2a71cb9](https://github.com/freeplane/freeplane/commit/e2a71cb9831ea6a2eb9626109541c0e027d60687) |
| 2010-05-27 | `feature` | auto bug fix: java.nio.channels.OverlappingFileLockException 	at sun.nio.ch.FileChannelImp | `MFileManager.java` | [0116ec05](https://github.com/freeplane/freeplane/commit/0116ec051bc93425f7f20b2969b7677583e21dfc) |
| 2010-05-22 | `fix` | fix style panel layout | `ColorProperty.java`, `StyleEditorPanel.java` +1 | [cf3d6b56](https://github.com/freeplane/freeplane/commit/cf3d6b56eb5ad7a7ba4c5bd303861218df0c00b5) |
| 2010-05-20 | `feature` | 646]: Command  "New encrypted map" should always be available in Freeplane | `EncryptedMap.java` | [fba11dae](https://github.com/freeplane/freeplane/commit/fba11daeb01550fd260c235958ceb3c8992deb83) |
| 2010-05-17 | `fix` | bug fixes for attribute table | `AttributePopupMenu.java`, `AttributeTable.java` +3 | [20cb1819](https://github.com/freeplane/freeplane/commit/20cb18196bf85bfd5b7fdbd0e92f94a59aec3636) |
| 2010-05-17 | `fix` | auto bug fixes in NextNodeAction and getAbsoluteUrl | `UrlManager.java`, `NextNodeAction.java` +1 | [17c37fe4](https://github.com/freeplane/freeplane/commit/17c37fe423b4a40e0503c80f7d3c26984a5a3634) |
| 2010-05-15 | `fix` | ug fix: make page number label in preview dialog wider | `PreviewDialog.java` | [85ee0db1](https://github.com/freeplane/freeplane/commit/85ee0db1cd3777247a945035cff787d591cf8b14) |
| 2010-05-13 | `fix` | bug fix for: ignore gragging  of connectors in outline view | `MMouseMotionListener.java` | [7389b625](https://github.com/freeplane/freeplane/commit/7389b6251f0882de245ef143aa91654606a9f5fc) |
| 2010-05-13 | `fix` | bug fix for inserting text strings as siblings using drag and drop | `MClipboardController.java` | [e365b825](https://github.com/freeplane/freeplane/commit/e365b825587fa2f5f9cc520bf2453dcb16871b25) |
| 2010-05-02 | `api_change` | remove dependencies from google-translate-api | `build.xml`, `Resources_ar.properties` +33 | [9a799adb](https://github.com/freeplane/freeplane/commit/9a799adb94852d6ced8c94b1f4f9c02f5e92d8f4) |
| 2010-04-30 | `fix` | bug fix in FreeplaneStarter loadMaps | `FreeplaneStarter.java`, `freeplane.properties` | [04b98f6b](https://github.com/freeplane/freeplane/commit/04b98f6bc7599d04be66d365e766bb2c1e7f4392) |
| 2010-04-30 | `fix` | bug fix: for URL recognition pattern from text | `MLinkController.java` | [30aa27a1](https://github.com/freeplane/freeplane/commit/30aa27a16c176aa575fe8cc8df13dfe01750b83f) |
| 2010-04-29 | `fix` | bug fix: show/hide attributes in browser mode | `AttributeView.java` | [15497619](https://github.com/freeplane/freeplane/commit/154976195021f94b4d007e111702f781c2658e8e) |
| 2010-04-29 | `api_change` | 604]: Java applet cannot be displayed after upgrade from 1.0.41 beta to 1.0.42 rc | `ModeController.java`, `EnterPassword.java` +4 | [a1882115](https://github.com/freeplane/freeplane/commit/a188211556f23e225b3c82e77de83c3be36b3739) |
| 2010-04-28 | `feature` | create new map if no maps were loaded on start | `FreeplaneStarter.java` | [4dd99e92](https://github.com/freeplane/freeplane/commit/4dd99e92a9e26f4c93e782ee036234999a007484) |
| 2010-04-28 | `api_change` | 604]: Java applet cannot be displayed after upgrade from 1.0.41 beta to 1.0.43 rc | `history_en.txt`, `AppletResourceController.java` | [6f58ed70](https://github.com/freeplane/freeplane/commit/6f58ed7038902043fea6280715cc53fb86f166f9) |
| 2010-04-28 | `feature` | option Environment->Files->Load last and new maps | `Resources_ar.properties`, `Resources_ca.properties` +33 | [99d9c303](https://github.com/freeplane/freeplane/commit/99d9c303f44be0bfb919a2b112bc8241f5058995) |
| 2010-04-28 | `fix` | change mode menu before enabling the actions, otherwise bug on mac os | `Controller.java`, `DocumentationAction.java` +1 | [b0749b8a](https://github.com/freeplane/freeplane/commit/b0749b8a6840b58a57335542b44a0e6a795a762f) |
| 2010-04-28 | `feature` | bug fix: enable actions after map and mode change | `AFreeplaneAction.java` | [711c1982](https://github.com/freeplane/freeplane/commit/711c1982b5df8086c1a5af0aee3ee951f84f531f) |
| 2010-04-24 | `feature` | add Menu Reference map to the Help menu | `browsemodemenu.xml`, `filemodemenu.xml` +4 | [b97a6ead](https://github.com/freeplane/freeplane/commit/b97a6eadfcc739640f7ce75873808e956caacfcf) |
| 2010-04-24 | `fix` | bug fix: use proper link color on outline view change: set standard link width to 2 | `LinkController.java`, `MapView.java` +3 | [aef28cfd](https://github.com/freeplane/freeplane/commit/aef28cfde6db157424eede30c91bd70feaf162bd) |
| 2010-04-22 | `fix` | revert bug fix 576] | `EditNodeWYSIWYG.java`, `freeplane.properties` | [6c9d9340](https://github.com/freeplane/freeplane/commit/6c9d9340f324738eef02cf691ac029b207e26d73) |
| 2010-04-18 | `feature` | bug fix for layout of the new revision dialog | `NewerFileRevisionsFoundDialog.java` | [d24262fd](https://github.com/freeplane/freeplane/commit/d24262fdc015ff5e7615edd28209c4ccb6f6bd25) |
| 2010-04-15 | `fix` | auto bug report fix for attribute popup | `AttributePopupMenu.java` | [5c5aff3c](https://github.com/freeplane/freeplane/commit/5c5aff3c9abce33a90cf8ac507ca4f5489de11e8) |
| 2010-04-11 | `fix` | MAttributeController: bug fix for removing attributes / values using AttributeManagerDIalo | `MAttributeController.java` | [bac787c1](https://github.com/freeplane/freeplane/commit/bac787c1c626ee21f803b454759bdd681d38f546) |
| 2010-04-11 | `fix` | Bug fix: do not save node text after editing if the map was already closed/deselected | `EditAction.java` | [3216e07c](https://github.com/freeplane/freeplane/commit/3216e07c4f79fd8dcdd1f55291a3b0558137b3a3) |
| 2010-04-11 | `feature` | applied format-translation -> new sort order | `Resources_ar.properties`, `Resources_ca.properties` +26 | [6b62c24f](https://github.com/freeplane/freeplane/commit/6b62c24f57e4ea489097bc57bc6e592f86f7f454) |
| 2010-04-11 | `api_change` | fixed wrong translations that happened due to Google's treatment of placeholders: - {0} -> | `Resources_ar.properties`, `Resources_ca.properties` +20 | [a9e01266](https://github.com/freeplane/freeplane/commit/a9e012660a13d701e0e1d44ff0e50a1603c120a9) |
| 2010-04-10 | `fix` | MNoteController start up fix | `MNoteController.java`, `Resources_en.properties` | [758af91f](https://github.com/freeplane/freeplane/commit/758af91f566afc92b2fb7d3b1fec0fb3e78768f6) |
| 2010-04-04 | `fix` | bug fix: display note editor only after the first map view is open | `MNoteController.java` | [02d5d8ec](https://github.com/freeplane/freeplane/commit/02d5d8ec35f4dc61f4ef4a485fe0f467841895f5) |
| 2010-04-03 | `fix` | Bug fix: ignore key events without modifiers if text component is a source | `FreeplaneMenuBar.java` | [edf5bf3e](https://github.com/freeplane/freeplane/commit/edf5bf3ec3e94a65c309ccc427b11eed9e569091) |
| 2010-04-02 | `fix` | automatic bug report fixes: FilterController, ExportDialog, ImportAttributesDialog, Export | `FilterController.java`, `ExportDialog.java` +2 | [88b1ef79](https://github.com/freeplane/freeplane/commit/88b1ef79821606429eb6cb00e33f0c13541e2666) |
| 2010-04-02 | `fix` | Bug fix in FindAction / FindNextAction | `NextNodeAction.java`, `FindAction.java` +7 | [8d694a0f](https://github.com/freeplane/freeplane/commit/8d694a0fafe55e263b9fd7592e8af8557990245e) |
| 2010-03-30 | `fix` | rename FpStringUtils to TextUtil, move it into core.util package and move all static metho | `MANIFEST.MF`, `ColorTracker.java` +163 | [06ed5406](https://github.com/freeplane/freeplane/commit/06ed54068f045191f8031fd9399021fd060c58ad) |
| 2010-03-29 | `fix` | Bug fix: HierarchicalIcons caused endless node refreshs | `MapController.java`, `HierarchicalIcons.java` +2 | [8ca36049](https://github.com/freeplane/freeplane/commit/8ca36049cf142ea226e7e327f1719e88d44ff6af) |
| 2010-03-24 | `fix` | Correct action name "Filter" -> "Filter Toolbar" | `Resources_ar.properties`, `Resources_ca.properties` +29 | [e681b922](https://github.com/freeplane/freeplane/commit/e681b9224e8cbb83eb187ce794c9559e5ec3471f) |
| 2010-03-24 | `feature` | 521]: Change item-order in Filter menu and add separators to Filter- and Edit-Menu | `mindmapmodemenu.xml` | [03b2f3d3](https://github.com/freeplane/freeplane/commit/03b2f3d3fa9d8f36bbb982531d826c3dd1580a7b) |
| 2010-03-11 | `fix` | fix the rendered html: The '<tag' name was omitted in case of an empty element. Since Simp | `HtmlTools.java` | [ea7e0ca6](https://github.com/freeplane/freeplane/commit/ea7e0ca656ae404f7a099925cc7e62526eba5848) |
| 2010-03-09 | `fix` | SimplyHTML.jar: bug fix for drag and drop AttributePopupMenu: do not display it if table i | `SimplyHTML.jar`, `AttributePopupMenu.java` +1 | [5aef69b5](https://github.com/freeplane/freeplane/commit/5aef69b53c19386152ceb0085221635194507480) |
| 2010-03-09 | `fix` | bug fix in JoinNodesAction for not standard html nodes | `JoinNodesAction.java` | [6dcc6b76](https://github.com/freeplane/freeplane/commit/6dcc6b763af391fc6aae383d9b5467673266e239) |
| 2010-03-09 | `fix` | bug fixes in AttributeTable and FButtonBar | `FButtonBar.java`, `FreeplaneMenuBar.java` +1 | [0bddb9c8](https://github.com/freeplane/freeplane/commit/0bddb9c84e5488d02833693de21e7c31ce627ff3) |
| 2010-03-09 | `fix` | make icon assignments for menu items storable (without this patch icons of menu nodes do n | `IconStore.java`, `AFreeplaneAction.java` +3 | [b838e242](https://github.com/freeplane/freeplane/commit/b838e2420717e3bbded75b1fee6df2180f8aa8d9) |
| 2010-03-09 | `feature` | add HTML table of key bindings to the documentation map as first node in the automatically | `Resources_de.properties`, `HtmlTools.java` +3 | [85383741](https://github.com/freeplane/freeplane/commit/85383741f5096ab6b5b992b7d9bd4da7a7af781e) |
| 2010-03-08 | `fix` | 479]: Valid URL triggers Automatic Bug Report | `SetLinkByTextFieldAction.java` | [78057c08](https://github.com/freeplane/freeplane/commit/78057c08b8af951961828a847008bc9b9f64cd0a) |
| 2010-03-07 | `fix` | bug fixes for automatic bug reports | `ComboProperty.java`, `FontProperty.java` +9 | [9ff0fbed](https://github.com/freeplane/freeplane/commit/9ff0fbed97ccb276cd5522c2d1cafee9ef74e1b9) |
| 2010-03-06 | `feature` | 470]: Experimental file locking problem in  - Export Branch as new map | `ExportBranchAction.java` | [e146c1d5](https://github.com/freeplane/freeplane/commit/e146c1d5c5946e13a50987b9dfe32fc52b8f1f54) |
| 2010-03-06 | `fix` | Toolbar layout bug fix Painting of toggled buttons under mac improved | `mindmapmodemenu.xml`, `FilterController.java` +7 | [01e6b108](https://github.com/freeplane/freeplane/commit/01e6b1086622debb008f79eec28f855d24983c57) |
| 2010-03-05 | `fix` | bug fix for full screen under linux | `ViewController.java` | [ddb2967a](https://github.com/freeplane/freeplane/commit/ddb2967af2e5089139505c5de7ec667fe36ee061) |
| 2010-03-04 | `feature` | * class UnfoldAll: moved registration of the actions to a   separate methods addActionsAtM | `browsemodemenu.xml`, `UnfoldAll.java` +2 | [449a0636](https://github.com/freeplane/freeplane/commit/449a0636b54b072ebc092368fcdf61e279f99f35) |
| 2010-02-27 | `feature` | 425]: Drag and drop from file explorer under Linux does not create a node with relative li | `MClipboardController.java`, `ExportBranchAction.java` +11 | [3abd79ef](https://github.com/freeplane/freeplane/commit/3abd79effb49ad0cd6d478759533f4f539d94343) |
| 2010-02-27 | `feature` | Reduce size of buffer for exporting map as image 406]: Clouds are truncated when exporting | `MapViewController.java`, `freeplane.properties` | [75474f42](https://github.com/freeplane/freeplane/commit/75474f425c71a65dfdf8923d456415708fad4dff) |
| 2010-02-21 | `fix` | fix comment handling in richcontent | `XMLParser.java` | [d419d52b](https://github.com/freeplane/freeplane/commit/d419d52b530f614cb8d709c8ec83af71fd7e090a) |
| 2010-02-21 | `fix` | correct translation key | `MFileManager.java` | [9c916d62](https://github.com/freeplane/freeplane/commit/9c916d624d64eb8499ace3cc40614d6e8df2297d) |
| 2010-02-21 | `api_change` | remove call of Java 1.6 API method | `MFileManager.java` | [50eaa869](https://github.com/freeplane/freeplane/commit/50eaa8696c3ca50f7072a5aa48cc478a7f9c4fda) |
| 2010-02-20 | `fix` | match plain text instead of html for notes too (like in bug 437) | `IgnoreCaseNoteContainsCondition.java`, `NoteContainsCondition.java` | [1054a0cb](https://github.com/freeplane/freeplane/commit/1054a0cb6e63a13fc330d5470141a0dff53917cf) |
| 2010-02-19 | `feature` | enable undo for setLastModifiedAt() and setCreatedAt() | `HistoryInformationModel.java`, `NodeProxy.java` | [b72ff2b6](https://github.com/freeplane/freeplane/commit/b72ff2b62680f7ebf87165a04c935545a5f45344) |
| 2010-02-19 | `feature` | extracted checkNode() from ICondition to a new interface - renamed ICondition to ISelectab | `Filter.java`, `FilterComposerDialog.java` +39 | [1d33574b](https://github.com/freeplane/freeplane/commit/1d33574b0e4134a56917f55be8a09b747d89c8d3) |
| 2010-02-18 | `fix` | fix two translations | `Resources_de.properties` | [3e4e0385](https://github.com/freeplane/freeplane/commit/3e4e038565ef2dba86e31f4722e3a68a27e8a222) |
| 2010-02-16 | `feature` | IMapLoader as a solution for creating of new maps programmatically | `IMapLoader.java`, `MapController.java` +5 | [d1509e49](https://github.com/freeplane/freeplane/commit/d1509e49d2e7c772baad1d3cbc94dae558f434df) |
| 2010-02-16 | `fix` | Fix minimized dock icon under Mac OS X | `ApplicationViewController.java` | [94f95234](https://github.com/freeplane/freeplane/commit/94f952345eb3faa6b97aa953603a6f64f98bc36d) |
| 2010-02-16 | `feature` | new NodeCondition named NodeMatchesRegexpCondition matches the plain node text | `ConditionFactory.java`, `NodeMatchesRegexpCondition.java` +1 | [36606ab5](https://github.com/freeplane/freeplane/commit/36606ab5d1fe5a44d48b6ebbad5bc01361f9d390) |
| 2010-02-15 | `feature` | new action HotKeyMapAction for the help menu that displays the actual hot keys in form of  | `Resources_de.properties`, `mindmapmodemenu.xml` +3 | [521b542e](https://github.com/freeplane/freeplane/commit/521b542e985832477ce2b3368eb7ad08f83d8d27) |
| 2010-02-13 | `feature` | 426]: Encrypted portions of maps don't export properly: new writer mode EXPORT | `MapWriter.java`, `NodeWriter.java` +3 | [cd6321e5](https://github.com/freeplane/freeplane/commit/cd6321e5e409f7b3955d10340f2f4a237bccf50a) |
| 2010-02-12 | `feature` | 425]: Drag and drop from file explorer under Linux does not create a node with relative li | `MLinkController.java` | [e3364ab7](https://github.com/freeplane/freeplane/commit/e3364ab7c7c73132536accae755f85f9c01b1cb8) |
| 2010-02-12 | `fix` | bug fix for GrabKeyDialog if no input event occured | `GrabKeyDialog.java` | [50df605c](https://github.com/freeplane/freeplane/commit/50df605ce28074885f3fbfde1c5d06d9b554ebf1) |
| 2010-02-07 | `feature` | user meta+control+alt for setting new short cut under mac os | `GrabKeyDialog.java`, `AccelerateableAction.java` | [b8c5f518](https://github.com/freeplane/freeplane/commit/b8c5f51893646e36564bada9fe87954e0996381e) |
| 2010-02-06 | `fix` | correct merge | `MainView.java` | [1aa8062b](https://github.com/freeplane/freeplane/commit/1aa8062b343a8fdc805174b6a6a4d9a87a406187) |
| 2010-02-05 | `fix` | use a shorter title for the 'replace shortcut?' dialog to fix rendering of the dialog titl | `Resources_ar.properties`, `Resources_ca.properties` +30 | [de92a1cb](https://github.com/freeplane/freeplane/commit/de92a1cb18ef25bf6b0d8134a32b276fa6d39c95) |
| 2010-02-01 | `fix` | LinkController - bug fix in link creation | `LinkController.java` | [eb0ddf30](https://github.com/freeplane/freeplane/commit/eb0ddf30694cc644373b838d0480da39e20062c3) |
| 2010-02-01 | `feature` | Add Hot Key Reference action to Help menu | `mindmapmodemenu.xml`, `DocumentationAction.java` +3 | [dc22d4eb](https://github.com/freeplane/freeplane/commit/dc22d4ebf832cfd3a3fd820fbc35622ea9d5cd6e) |
| 2010-01-30 | `feature` | 410]: Unable to assign space bar to insert new node | `KeyEventTranslator.java` | [babfa42e](https://github.com/freeplane/freeplane/commit/babfa42ea21a7be99894619a6356d4a86304db31) |
| 2010-01-30 | `feature` | Add OK and Cancel buttons to Latex Editor | `Resources_ar.properties`, `Resources_ca.properties` +29 | [5610d61c](https://github.com/freeplane/freeplane/commit/5610d61c3fc7f734efb92a475559d887760a829e) |
| 2010-01-28 | `fix` | update undo redo buttons bug fix | `CompoundActor.java`, `UndoHandler.java` | [e4dc5a13](https://github.com/freeplane/freeplane/commit/e4dc5a1367c414c1cf1b6ca28c00d81b1f7d7dbc) |
| 2010-01-24 | `feature` | mac os and meta key support | `GrabKeyDialog.java`, `KeyEventTranslator.java` +8 | [379e490b](https://github.com/freeplane/freeplane/commit/379e490b3af691b0ad8a3a98259dc33846740ee4) |
| 2010-01-20 | `fix` | layout bug | `NodeViewLayoutAdapter.java` | [91141f5d](https://github.com/freeplane/freeplane/commit/91141f5d84c60df2193fe15bb2581644cba830d7) |
| 2010-01-18 | `fix` | bug fixes for link target management | `MapController.java`, `MapModel.java` +13 | [43acb8b1](https://github.com/freeplane/freeplane/commit/43acb8b17cd9ccab343d3dfb6a400dddec1e2e07) |
| 2010-01-17 | `fix` | bug fix in MapModel.getNodeForID | `MapModel.java` | [8c660335](https://github.com/freeplane/freeplane/commit/8c6603352258670d761aede222fad3fa08bf9142) |
| 2010-01-14 | `feature` | added scripts configuration to the OptionPanel, ohne group per script | `Resources_de.properties`, `ResourceBundles.java` +5 | [f91a4165](https://github.com/freeplane/freeplane/commit/f91a4165a628cb54efe938fd336bff6b0afc9793) |
| 2010-01-12 | `fix` | Better fix for 376]: designating the tab key...: equally handle all key codes between 1 an | `KeyEventTranslator.java` | [0340f312](https://github.com/freeplane/freeplane/commit/0340f312605e5582952733e90a900e6c7901b050) |
| 2010-01-12 | `fix` | bug fix in org.freeplane.core.url.UrlManager.getUpdateReader(File, String) | `UrlManager.java` | [5d7ef2b3](https://github.com/freeplane/freeplane/commit/5d7ef2b39d7b224cbcfaf8ad5a18bfc1235dcfdd) |
| 2010-01-10 | `feature` | 376]: designating the tab key as the default for insert new child doesn't work on new inst | `KeyEventTranslator.java` | [80607f8d](https://github.com/freeplane/freeplane/commit/80607f8d1a399e7d88754bcd798a4fff68f17e93) |
| 2010-01-10 | `fix` | status bar bug fix | `ViewController.java`, `AppletViewController.java` +6 | [666c0e4f](https://github.com/freeplane/freeplane/commit/666c0e4f3ed42048d33527527abbc8d485629d47) |
| 2010-01-10 | `feature` | new menu for styles | `mindmapmodemenu.xml`, `MLogicalStyleController.java` +3 | [00449a47](https://github.com/freeplane/freeplane/commit/00449a47845757317ae854d8b706fde9ced1e1eb) |
| 2010-01-10 | `fix` | bug fix in ToggleToolbarAction.selectMode | `ToggleToolbarAction.java`, `ViewController.java` | [99bdb717](https://github.com/freeplane/freeplane/commit/99bdb71741e4af61cb1d2997b9fc4ac7cd7a86e4) |
| 2010-01-09 | `feature` | add copy & paste format actions into style editor | `mindmapmodemenu.xml`, `stylemodemenu.xml` +6 | [8a4b30ca](https://github.com/freeplane/freeplane/commit/8a4b30caf03450a73598c1cd4d4b0d1436e76a23) |
| 2010-01-09 | `feature` | enable spell check for note editor  only while it has focus | `MNoteController.java`, `SpellCheckerController.java` +3 | [bb3f857d](https://github.com/freeplane/freeplane/commit/bb3f857db4741976076671b58abd5882debe4435) |
| 2010-01-09 | `fix` | bug fixes in attribute dialogs | `AttributeRegistry.java`, `AssignAttributesAction.java` | [d07a0a77](https://github.com/freeplane/freeplane/commit/d07a0a7758f06c6894283c96b49bcbfa2158e797) |
| 2010-01-08 | `feature` | new icons | `button_ok.png`, `cancel_button.png` +3 | [8a873a9e](https://github.com/freeplane/freeplane/commit/8a873a9e95e7c8b3e2b4d9b20f2b209f9b176eae) |
| 2010-01-08 | `feature` | new icons | `bell.png`, `flag.png` +4 | [73cbb8b5](https://github.com/freeplane/freeplane/commit/73cbb8b5fa55527677b5f869cfc63aaef4137a3d) |
| 2010-01-07 | `fix` | bug fix in UndoHandler for transactions | `CompoundActor.java`, `UndoHandler.java` +1 | [b4efbbca](https://github.com/freeplane/freeplane/commit/b4efbbca6dfd555be5facb8c16cbaaf3ccae3204) |
| 2010-01-06 | `feature` | add ok anc cancel actions to style dialog | `stylemodemenu.xml`, `ControlToolbar.java` +6 | [08a45f61](https://github.com/freeplane/freeplane/commit/08a45f6145534f5fd9d246c5bc2dc3269bbaff4a) |
| 2010-01-06 | `feature` | 372]: Unable to create filter "containing attribute icon. | `DefaultConditionRenderer.java`, `IconConditionController.java` | [77bcb9d5](https://github.com/freeplane/freeplane/commit/77bcb9d58eda257a457fb20854024bedb1776b0d) |
| 2010-01-05 | `feature` | replace Pattern by IExtensionCopier implementations add ControlToolbar to EditStylesAction | `IExtensionCopier.java`, `ViewController.java` +17 | [0c878bab](https://github.com/freeplane/freeplane/commit/0c878babcc5d525e7e44091f339ec20281c89193) |
| 2010-01-02 | `feature` | Add selectable action "toggle formatting panel" to view menu and map popup menu | `mindmapmodemenu.xml`, `IUserInputListenerFactory.java` +4 | [7d38a01d](https://github.com/freeplane/freeplane/commit/7d38a01d12a75f5cf5e9879bcf87e7cfb3ffc356) |

### Dettagli commit con note

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

**[3677d7a3](https://github.com/freeplane/freeplane/commit/3677d7a3048dd03dfb049168d1f417657d6740ff)** (2010-10-31) — Formula plugin: Display evaluated formulas...  - in attribute table  - in attribute tooltip  - in note tooltip  - when 'Show Notes in Map' is enabled

> Refactored TextController:
>  - getText() renamed to getTransformedText()
>  - new getText() returns untransformed text
>  - avoid direct model access in MainView

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

**[449a0636](https://github.com/freeplane/freeplane/commit/449a0636b54b072ebc092368fcdf61e279f99f35)** (2010-03-04) — * class UnfoldAll: moved registration of the actions to a   separate methods addActionsAtMenuBuilder(menuBuilder) and allow   manual registration via getAnnotatedActions()

> * add the following actions to the browse menu:
>   - FoldAllAction
>   - FoldOneLevelAction
>   - UnfoldAllAction
>   - UnfoldOneLevelAction
> 
> * remove trailing separators

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
| 2009-12-28 | `feature` | new italian translation + automatic translations | `Resources_ar.properties`, `Resources_ca.properties` +25 | [363bab15](https://github.com/freeplane/freeplane/commit/363bab15d288eab397a8887188d78f26481802b9) |
| 2009-12-28 | `fix` | 363]: Two minor bug about note | `history_en.txt`, `MenuBuilder.java` +2 | [e632929f](https://github.com/freeplane/freeplane/commit/e632929f596ba2376d8fa5cffe2a1e9efd12cc57) |
| 2009-12-27 | `feature` | support spellchecker options | `SpellChecker.java`, `.classpath` +6 | [ad2bc894](https://github.com/freeplane/freeplane/commit/ad2bc894fbe56cc703aced3ab2abcab2adf31a42) |
| 2009-12-24 | `fix` | 356]: Encryption violation triggers Automatic bug report | `NodeModel.java`, `XmlRpcHandler.java` | [d50325de](https://github.com/freeplane/freeplane/commit/d50325de9aded537e806bd1438102399b7a443e9) |
| 2009-12-19 | `fix` | bug fixes in scripting | `MapView.java`, `ScriptingEngine.java` +1 | [09d2a805](https://github.com/freeplane/freeplane/commit/09d2a8058ae74d77f8b1aa01555594191bd241d6) |
| 2009-12-16 | `fix` | Bug for % in user icon names | `UserIcon.java` | [bec3a52d](https://github.com/freeplane/freeplane/commit/bec3a52d79297e5a3916c970fec7d49deeeedc0c) |
| 2009-12-16 | `fix` | bug fix for SelectAllAction | `SelectAllAction.java`, `MapView.java` | [7d381e8b](https://github.com/freeplane/freeplane/commit/7d381e8b9c074284427549d2064db8217b3465d2) |
| 2009-12-16 | `fix` | bug fix in ExportBranchAction bug fix in OpenUri with map | `UrlManager.java`, `ExportBranchAction.java` | [6fd850a7](https://github.com/freeplane/freeplane/commit/6fd850a72df9b85856b8bb993a97ec66e895e31a) |
| 2009-12-15 | `fix` | bug fix: do not request focus in note editor on start | `MNoteController.java` | [7b0eddfc](https://github.com/freeplane/freeplane/commit/7b0eddfcaac7f9b18682f6dfa3678a76370ff788) |
| 2009-12-15 | `api_change` | 341]: Scripting API bugs | `Resources_ar.properties`, `Resources_ca.properties` +46 | [ed3927bf](https://github.com/freeplane/freeplane/commit/ed3927bfeb39dad3e77c1b515b89c91defcb78b0) |
| 2009-12-15 | `fix` | bug fix in grabbing short cut | `AccelerateableAction.java` | [8325ed10](https://github.com/freeplane/freeplane/commit/8325ed107420a11993ff879ef976186a4f100f45) |
| 2009-12-07 | `fix` | bug fix in open url | `ApplicationViewController.java` | [2ba8a9d1](https://github.com/freeplane/freeplane/commit/2ba8a9d145482a3ca59bafebfcfc723e811d2c0d) |
| 2009-11-29 | `fix` | bug fixes for automatic bug reports | `BitmapViewerComponent.java`, `SetLinkByTextFieldAction.java` +3 | [a6d11130](https://github.com/freeplane/freeplane/commit/a6d111303d557cf088a25cb232bacbedca9a7adb) |
| 2009-11-29 | `fix` | bug fixes for menu bar, f-bar and NodeView.contains | `mindmapmodemenu.xml`, `FButtonBar.java` +1 | [064a8cb2](https://github.com/freeplane/freeplane/commit/064a8cb21202ee2a9aaa8018f12efcf1d399799f) |
| 2009-11-27 | `feature` | new  createURI (by Eric and Dimitry) | `Compat.java`, `LinkController.java` | [fe7b1ebc](https://github.com/freeplane/freeplane/commit/fe7b1ebc37d231604010499580ea0d98c2262dc1) |
| 2009-11-27 | `fix` | bug fix for Clear Case: do not lock read file | `MFileManager.java` | [f7129384](https://github.com/freeplane/freeplane/commit/f712938408a1a825a5c953a4cae3a75ba881435c) |
| 2009-11-22 | `api_change` | proxy API | `PersistentNodeHook.java`, `ExternalResource.java` +19 | [3bd96b9f](https://github.com/freeplane/freeplane/commit/3bd96b9fd523572488ef80bf3c16a885f7495509) |
| 2009-11-21 | `api_change` | script API part 1 | `ArrowType.java`, `ConnectorModel.java` +27 | [9c1dac83](https://github.com/freeplane/freeplane/commit/9c1dac834afe0125cbb200fee4645199f7dcfbe7) |
| 2009-11-16 | `feature` | new art | `Freeplane_application_icon_blue.png`, `Freeplane_frame_icon.png` +19 | [808081fb](https://github.com/freeplane/freeplane/commit/808081fbf8a750afcc7cfb31b8754a204fbc1f8b) |
| 2009-11-14 | `fix` | 310]: note window - refresh bug | `ViewController.java` | [213109c3](https://github.com/freeplane/freeplane/commit/213109c3df8ec11558e1e4630eb9f99a1e51d06f) |
| 2009-11-08 | `feature` | new splash layout | `Freeplane_splash.png`, `FreeplaneVersion.java` +3 | [8009277a](https://github.com/freeplane/freeplane/commit/8009277adc082c68ceef39d656dc8bfdd2f03751) |
| 2009-11-06 | `fix` | bug fix in icon toolbar menu hierarchy | `MIconController.java` | [fed1b491](https://github.com/freeplane/freeplane/commit/fed1b491c4e5da792828dc8bdb616654015c9cd3) |
| 2009-11-05 | `feature` | new splash screen | `Freeplane_splash.png` | [5478acac](https://github.com/freeplane/freeplane/commit/5478acac5e91d102f1ee5a9a59d6e1ab4d672839) |
| 2009-11-04 | `feature` | new icons | `arrow-mode-backward.png`, `arrow-mode-both.png` +8 | [6c9b158f](https://github.com/freeplane/freeplane/commit/6c9b158f5f07a2f942abd75ce5dfa1ade928c97a) |
| 2009-11-02 | `fix` | bug 303: Hierarchical Icons unacceptably slow performance | `UIIcon.java`, `UserIcon.java` +11 | [dc2b2f99](https://github.com/freeplane/freeplane/commit/dc2b2f9942546d9029b6827625953cab8527aa67) |
| 2009-11-01 | `fix` | patch 293 javadoc comment corrected | `FixedHTMLWriter.java` | [8eb42c53](https://github.com/freeplane/freeplane/commit/8eb42c5388aed2cecd302ae8a97bc7f712e5b67e) |
| 2009-10-31 | `fix` | bug fix 288: Missing key for translation Map menu | `Controller.java`, `ResourceController.java` +6 | [451c84dd](https://github.com/freeplane/freeplane/commit/451c84dd36ca9ab3d51110cabad6aa82dd4c9d76) |
| 2009-10-31 | `fix` | bug fix 292: NullPointerException while opening help map | `MNoteController.java` | [14e03b5b](https://github.com/freeplane/freeplane/commit/14e03b5bb9d7d721bfe86636c875c9df6e21cc11) |
| 2009-10-31 | `fix` | bug 291: Priority filtering is broken | `PriorityCompareCondition.java` | [ab8e71ec](https://github.com/freeplane/freeplane/commit/ab8e71ec5a01477256694dca4cc96f0ec389487e) |
| 2009-10-27 | `fix` | bug fix for update check for localized versions | `UpdateCheckAction.java` | [7ef40e1d](https://github.com/freeplane/freeplane/commit/7ef40e1da209f4c475bb9370ee8f1619271f7d4f) |
| 2009-10-27 | `fix` | use URI for open URL (bug fix) | `ApplicationViewController.java` | [72f3beba](https://github.com/freeplane/freeplane/commit/72f3beba7cb078b2c1067c0601ea0faba16fc7d4) |
| 2009-10-25 | `feature` | bug fix 228: load empty files as a new mindmap | `MFileManager.java` | [d0273b67](https://github.com/freeplane/freeplane/commit/d0273b67970b77d1cbe1ebae61a9df80a0f7ed3c) |
| 2009-10-25 | `fix` | bug 227: In the preferences > Move "Hyperlink Types" from "Appearance" tab: moved to envir | `preferences.xml` | [80d1b234](https://github.com/freeplane/freeplane/commit/80d1b23443352674659cec9a6099c67a2a5f3e26) |
| 2009-10-25 | `fix` | Bug fix 216 Focus after note window | `MNoteController.java` | [34e4a164](https://github.com/freeplane/freeplane/commit/34e4a16475a6fd75d0ddaa3c084893d5b80c1998) |
| 2009-10-25 | `fix` | bug fix  	 0000177: Modification times | `NodeModel.java`, `CreationModificationPlugin.java` | [9fbfbf47](https://github.com/freeplane/freeplane/commit/9fbfbf47c30f7e82b7dd9275228514ef48c02f9c) |
| 2009-10-22 | `feature` | [Bugs 0000277]: After saving a new map, exception thrown when selecting "Map1" on right-cl | `ViewController.java` | [474798c4](https://github.com/freeplane/freeplane/commit/474798c40e9792596cf408e03cc9211a7328700e) |
| 2009-10-22 | `fix` | bug fix in xhtml writer [Bugs 0000276]: 1.0.32-1019 alpha: complicated bug blocks Freeplan | `NodeModel.java`, `XHTMLWriter.java` +1 | [da571fe0](https://github.com/freeplane/freeplane/commit/da571fe09380670f6e60ff6e0faf4738a2ddc5e8) |
| 2009-10-20 | `fix` | bug fix in find & replace dialog | `FlatNodeTableFilterModel.java` | [165d8db9](https://github.com/freeplane/freeplane/commit/165d8db9d3d6dbc786b8bde0d049482364e2170d) |
| 2009-10-20 | `fix` | bug fix [Bugs 0000269]: Freeplane does not execute Freemind interemaps-from-node-to-node h | `UrlManager.java` | [e2357536](https://github.com/freeplane/freeplane/commit/e235753616acc67280f0d0d3a3b998583c0e42a1) |
| 2009-10-19 | `fix` | Bug fix  Freeplane 1.0.32 a does not open encrypted maps | `DesEncrypter.java` | [9f0cd174](https://github.com/freeplane/freeplane/commit/9f0cd174d4a632125d67de320f8b7006d8db9dce) |
| 2009-10-19 | `fix` | bug 0000234: desactivation of hierarchical icon | `UIIconSet.java`, `NodeModel.java` +1 | [f4e0bdcb](https://github.com/freeplane/freeplane/commit/f4e0bdcbb4a7011d9de10ccfab285493b392d85e) |
| 2009-10-19 | `feature` | new clock2.png log all executed commands | `Controller.java`, `UrlManager.java` +3 | [1b2a0bfd](https://github.com/freeplane/freeplane/commit/1b2a0bfd6e5e09b50967a5d7cb95fd2e37e84447) |
| 2009-10-14 | `fix` | BUG 266 fix merged from branch 1_0_x | `UIIcon.java`, `MultipleImage.java` +1 | [104218f1](https://github.com/freeplane/freeplane/commit/104218f1e7414f557164737d3e3395bf45f936d1) |
| 2009-10-14 | `fix` | BUG 266: fixing 'Show icons hierarchically' action | `UIIcon.java`, `UIIconSet.java` +3 | [d621160c](https://github.com/freeplane/freeplane/commit/d621160c91b006b7d6327f963b496d271489a0ae) |
| 2009-10-13 | `fix` | fix in html2xhtml | `XHTMLWriter.java` | [b7fd669e](https://github.com/freeplane/freeplane/commit/b7fd669e40ff3becb6e3a7d649185cce84670b03) |
| 2009-10-12 | `feature` | bug fix: always add '/' at the end of all empty tags | `XHTMLWriter.java` | [90fbd481](https://github.com/freeplane/freeplane/commit/90fbd481aee8723f638993f8607008cc7c3a4a12) |
| 2009-10-11 | `feature` | change node map after export for all nodes:  	 0000253: can't edit name on exported branch | `NodeModel.java` | [c984f56c](https://github.com/freeplane/freeplane/commit/c984f56c5011c2678a43a3b6e4b693b66b8aa9cf) |
| 2009-10-11 | `fix` | bug fix:  	 0000251: Error parsing file. rename icon file | `NodeAttributeTableModel.java`, `freeplane.properties` | [c6dbb1c1](https://github.com/freeplane/freeplane/commit/c6dbb1c1e9be02dd6a1490608c6ae110854a8ce2) |
| 2009-10-11 | `fix` | bug fixes for file mode 0000245: Navigation in File Mode is (almost) not working | `FNodeModel.java` | [d770035a](https://github.com/freeplane/freeplane/commit/d770035a5061ffa4d176bca66837d5030307ceda) |
| 2009-10-11 | `fix` | bug  	 0000243: Find and replace doesn't replace all occurrence of a pattern within a node | `NodeList.java` | [7920293c](https://github.com/freeplane/freeplane/commit/7920293c5e21c174fafcadd762c4ebef1ba74404) |
| 2009-10-11 | `fix` | bug fix for showing context  menus for horizontal edges bug 0000236: simulate edge feature | `HorizontalEdgeView.java`, `CollisionDetector.java` | [42378a3f](https://github.com/freeplane/freeplane/commit/42378a3fac25bcfdcc42af995b686e74fb1b85f6) |
| 2009-10-11 | `feature` | bug fix : create no extended object if no file is returned | `ViewerController.java` | [4e4ea930](https://github.com/freeplane/freeplane/commit/4e4ea93012bedf45fd0e2904563143465e6c41d0) |
| 2009-10-11 | `fix` | bug fox for decryption with empty password | `DesEncrypter.java` | [43500702](https://github.com/freeplane/freeplane/commit/43500702db5c3bc7668c19adab0d69ae7462948c) |
| 2009-10-11 | `fix` | bug fix: ignore wrong content entered in font size box | `MToolbarContributor.java` | [3bda54df](https://github.com/freeplane/freeplane/commit/3bda54df221fa58ad79ca69319e904a0634ed653) |
| 2009-10-11 | `fix` | bug fix for not available file preview | `ViewerController.java` | [d57afaba](https://github.com/freeplane/freeplane/commit/d57afaba66eb9ebf8b858ca80e7e17e69d16bafd) |
| 2009-10-11 | `fix` | bug fixes for icons | `ResourceController.java`, `AppletResourceController.java` | [419cb531](https://github.com/freeplane/freeplane/commit/419cb531d9c40c26eb2584bc86d06bbc66d637ff) |
| 2009-10-11 | `fix` | bug fixes icons | `IconStoreFactory.java`, `ImageIconFactory.java` | [7080b2d6](https://github.com/freeplane/freeplane/commit/7080b2d60902630cacc170a4351c7795fd14dfb8) |
| 2009-10-11 | `fix` | bug fix for icons | `RemoveIconAction.java` | [f3ab689b](https://github.com/freeplane/freeplane/commit/f3ab689b14b0242e01514413c534ad14026cc80d) |
| 2009-10-09 | `fix` | bug fixes | `MLogicalStyleController.java`, `ApplyPatternAction.java` | [287a9671](https://github.com/freeplane/freeplane/commit/287a9671cd8541ec7a4cfd854a0dbb0bc46b4884) |
| 2009-10-09 | `fix` | bug fixes for class and icon loading | `ZoomIn24.gif`, `ZoomIn24.gif.png` +22 | [b6e89c6e](https://github.com/freeplane/freeplane/commit/b6e89c6ef7c1b76e620fac173d659b6f65f1adee) |
| 2009-10-04 | `fix` | bug fixes in map html writer | `MindMapHTMLWriter.java` | [dd1423ef](https://github.com/freeplane/freeplane/commit/dd1423efbcfcf207b92f771550b33ec95892f961) |
| 2009-10-04 | `feature` | new/delete user/level styles | `stylemodemenu.xml`, `DeleteLevelStyleAction.java` +5 | [a74f9d77](https://github.com/freeplane/freeplane/commit/a74f9d779a576ddfe03d2fe3f2e6eda53ac35b8a) |
| 2009-09-28 | `feature` | support for icons in logical styles | `Filter.java`, `FilterController.java` +33 | [50b36f21](https://github.com/freeplane/freeplane/commit/50b36f21f70cbed8368e6d0b160da9bb1b984b62) |
| 2009-09-28 | `feature` | new reminder icons | `bell.png`, `flag.png` | [2e568db3](https://github.com/freeplane/freeplane/commit/2e568db34883e3260ed1a469c6205ab36751445b) |
| 2009-09-24 | `fix` | bug fixes | `NoteController.java`, `MModeController.java` | [3656ada1](https://github.com/freeplane/freeplane/commit/3656ada1ec5c02f1ccece8f2a4c95685a5dbd039) |
| 2009-09-20 | `feature` | New Croatian translation | `Resources_hr.properties` | [ae6a6d3a](https://github.com/freeplane/freeplane/commit/ae6a6d3a5243ae4860cd2ea97dc04f92a6fdb944) |
| 2009-09-20 | `feature` | new icon for Italic in Simply html tool bar | `Italic_on16.png` | [c47e1043](https://github.com/freeplane/freeplane/commit/c47e1043e44f6e54bdf31814c766d22d5d645b9a) |
| 2009-09-20 | `feature` | new icon for Symply html toolbar | `Bold_on16.png` | [678f5fdf](https://github.com/freeplane/freeplane/commit/678f5fdf67527d87dc758639b548676bc6f94171) |
| 2009-09-10 | `feature` | new icons for View menu | `CenterSelectedNodeAction.png`, `FitToPage.png` +2 | [26233c49](https://github.com/freeplane/freeplane/commit/26233c4980cecf028971ab9b14eab3cdcd7a140f) |
| 2009-09-09 | `feature` | new Croatian translation | `Resources_hr.properties` | [51845289](https://github.com/freeplane/freeplane/commit/518452892028ae41d8e54f7be1126deeaa3eeb7e) |
| 2009-09-09 | `feature` | smaller icon for italic and bold new icon for simplyhtml | `Bold16.png`, `Italic16.png` +1 | [5fa73f15](https://github.com/freeplane/freeplane/commit/5fa73f1594653ae387824bdbb7ac18e6438add64) |
| 2009-09-09 | `fix` | bug fix for full screen mode: properly display modal dialogs on top | `ViewController.java` | [425aa583](https://github.com/freeplane/freeplane/commit/425aa583fc0cc270c1da42efc8e8a2a2d42e5e76) |
| 2009-09-09 | `feature` | new icons for Show Modification Time | `kword.png` | [bd770cda](https://github.com/freeplane/freeplane/commit/bd770cda9ec353e026f1449816b0fa455f954f6f) |
| 2009-09-08 | `fix` | bug fix: null pointer exception | `EditAction.java` | [2f4ce51d](https://github.com/freeplane/freeplane/commit/2f4ce51da2e9614e698f779336d672ccbf4aa99e) |
| 2009-09-08 | `fix` | fixed bug where multiple state icons of the same kind are added to a node | `NodeIconSetModel.java`, `NodeModel.java` +2 | [6206f93e](https://github.com/freeplane/freeplane/commit/6206f93efc6e27128089511cc7b78b7b052f8a8e) |
| 2009-09-08 | `fix` | fixing shortcut bug | `IconNotFound.java`, `MindIcon.java` +3 | [e04cf958](https://github.com/freeplane/freeplane/commit/e04cf9585ee824e27a18e2e8c073fd17ef104819) |
| 2009-09-07 | `feature` | new bold and italic icons | `Bold16.gif`, `Bold16.png` +2 | [85733a9b](https://github.com/freeplane/freeplane/commit/85733a9b01808c173b5d84a50a489954c905bdc3) |
| 2009-09-06 | `feature` | re-factoring icon handling, various cleanups, new icons | `MANIFEST.MF`, `bell.png` +65 | [5d0b17f1](https://github.com/freeplane/freeplane/commit/5d0b17f12fb900a52a82df5deacd6fefc0183919) |
| 2009-09-06 | `feature` | new icons | `colorpicker.png`, `designer.png` +1 | [323aef8c](https://github.com/freeplane/freeplane/commit/323aef8ccd992bc033a6ffaf45f79ea85ba3f3d7) |
| 2009-09-04 | `feature` | new icon | `color_fill.png` | [ebfc2446](https://github.com/freeplane/freeplane/commit/ebfc2446fcd4700a0a20bd389ddce987333b1a8f) |
| 2009-09-04 | `feature` | new icons | `Bold16.gif`, `Italic16.gif` +2 | [f3952e8f](https://github.com/freeplane/freeplane/commit/f3952e8ffdf0cc87d8a2d3cfc8903bb482d05311) |
| 2009-09-04 | `feature` | new icon for split node in Tools menu | `split_node.png` | [8849d94f](https://github.com/freeplane/freeplane/commit/8849d94f9031af6715633b6f4b675c7fbfc5abac) |
| 2009-09-03 | `fix` | bug fix for opening file URLs with spaces | `ApplicationViewController.java` | [a3398b48](https://github.com/freeplane/freeplane/commit/a3398b4869b8a1bbf307623089891230a08c4db4) |
| 2009-09-03 | `feature` | new toolbar icons | `1leftarrow.png`, `1rightarrow.png` +15 | [487fa4ef](https://github.com/freeplane/freeplane/commit/487fa4ef66df461f564b6b5f4b040be9fcce44ea) |
| 2009-09-03 | `feature` | New Croatian translation | `Resources_hr.properties` | [66c37c87](https://github.com/freeplane/freeplane/commit/66c37c8787c57a9650671575d1162b3669f9f638) |
| 2009-09-02 | `feature` | [Bugs 0000217]: Enter key gives new line in node rather than end node edit | `Resources_cs.properties`, `Resources_da.properties` +24 | [c752db1c](https://github.com/freeplane/freeplane/commit/c752db1c65a565aadb80a429da254330bbc2cde8) |
| 2009-09-01 | `feature` | new splash | `Freeplane_splash.png`, `FreeplaneSplashModern.java` | [04f4839f](https://github.com/freeplane/freeplane/commit/04f4839fd84f8de55a701927541d480e9962d192) |
| 2009-08-31 | `fix` | bug fix for blinking node if no view exists | `NodeModel.java` | [447e069a](https://github.com/freeplane/freeplane/commit/447e069aa9a72a58aeea0a53d4cb09c3b58f5163) |
| 2009-08-31 | `feature` | bug fix: do not create already existing edgemodel and cloudmodel on loading | `PersistentNodeHook.java`, `CloudBuilder.java` +2 | [e4c74471](https://github.com/freeplane/freeplane/commit/e4c7447157fe4edc22fd5ee6d270c3b3b9962367) |
| 2009-08-30 | `fix` | options "fit map to page width", "fit map to page height" bug fixes for printing | `Resources_ar.properties`, `Resources_ca.properties` +34 | [280aed72](https://github.com/freeplane/freeplane/commit/280aed7219b31b23f0fb52c176e1d8469f80bd22) |
| 2009-08-30 | `fix` | bug fix for applet | `ViewController.java`, `AppletResourceController.java` +1 | [7c968168](https://github.com/freeplane/freeplane/commit/7c9681689b01fe3a50bb739d11283490302e3209) |
| 2009-08-30 | `fix` | bug fix for mouse cursor simply html improvements for outline view | `SimplyHTML.jar`, `browsemodemenu.xml` +12 | [6acbcd68](https://github.com/freeplane/freeplane/commit/6acbcd6874c497985f81645ceea927a717fdba93) |
| 2009-08-29 | `fix` | bug fix: size of external bitmaps loaded wrong | `BitmapViewerFactory.java`, `ViewerLayoutManager.java` | [829a2239](https://github.com/freeplane/freeplane/commit/829a2239a18e4ca0e6b4323564cbcdf2d7da3a5d) |
| 2009-08-29 | `fix` | bug fix: crash on returning from full screen mode if freeplane starts maximized | `ViewController.java`, `FreeplaneStarter.java` +1 | [ea23da64](https://github.com/freeplane/freeplane/commit/ea23da64e3ec5d97a04e798b64ab05a8d01f8019) |
| 2009-08-26 | `fix` | save map after node is encrypted bug fixes in reminder: properly show and remove state ico | `ViewController.java`, `BitmapImagePreview.java` +8 | [470920d9](https://github.com/freeplane/freeplane/commit/470920d926f953b21bdd04e86f2b0b7f9442036b) |
| 2009-08-26 | `feature` | new Croatian translation | `Resources_hr.properties` | [67afc159](https://github.com/freeplane/freeplane/commit/67afc1595a6d202710cd92f846a0d195140dfac3) |
| 2009-08-26 | `feature` | new Croatian translation | `Resources_hr.properties` | [63649813](https://github.com/freeplane/freeplane/commit/636498139aa48d47c52294f19d5c856d28d9bd01) |
| 2009-08-25 | `fix` | bug fixes for automatic bug reports | `IconSelectionPopupDialog.java`, `UrlManager.java` +10 | [9416d392](https://github.com/freeplane/freeplane/commit/9416d3922d9fac2a3ec8c4f1f2327d360567cc2c) |
| 2009-08-16 | `fix` | bug fix in "repaint visible" | `MapView.java`, `MMouseMotionListener.java` | [d80ae2ec](https://github.com/freeplane/freeplane/commit/d80ae2ec0adb1b5c57fa2e8961d59cf1709f4567) |
| 2009-08-16 | `feature` | new icons: 0%, 25%, 50%, 75%, 25%, icon_trash and icon_remove | `icon_remove.png`, `icon_trash.png` +7 | [6ee9229f](https://github.com/freeplane/freeplane/commit/6ee9229f9b0f6c5de4d4a9aa734dc8d82bfc7c15) |
| 2009-08-13 | `fix` | Connector Label Filter Condition refactoring: replace proprietary class SortedMapListModel | `FilterController.java`, `RedoFilterAction.java` +39 | [c8d9d617](https://github.com/freeplane/freeplane/commit/c8d9d61716d57069da94bff0ee4e7cda73f6cf39) |
| 2009-08-13 | `fix` | bug fix: remove link from map links if its source node is removed | `MLinkController.java` | [e53e4fa4](https://github.com/freeplane/freeplane/commit/e53e4fa44cf5b8104973d6e2613093b21f4166fd) |
| 2009-08-12 | `fix` | bug fix in painting of edited main view for zoomed maps | `EditNodeTextField.java`, `MainView.java` | [804fe3a0](https://github.com/freeplane/freeplane/commit/804fe3a00d4dd8b47b6e38d9cfb7e606b863e9fb) |
| 2009-08-12 | `feature` | do not add already registered LoadAcceleratorPResetsAction when preset file is saved again | `LoadAcceleratorPresetsAction.java` | [ab2261d3](https://github.com/freeplane/freeplane/commit/ab2261d3397992f6d58d4b48eac07a529acd8170) |
| 2009-08-09 | `fix` | bug fix in date filter bug fix in map positioning if root is selected after the filter was | `Filter.java`, `FilterConditionEditor.java` +4 | [3e5dd1ff](https://github.com/freeplane/freeplane/commit/3e5dd1ffaaf167b11bedb4e796e50a110939fec2) |
| 2009-08-09 | `fix` | bug fixes in calculating text area editor size | `EditNodeTextField.java` | [c6e3fcc5](https://github.com/freeplane/freeplane/commit/c6e3fcc54fefeb0938c1ad3e007989276b6cafe8) |
| 2009-08-06 | `fix` | bug fix: do not process events after text area is hidden | `EditNodeTextField.java` | [73c2e510](https://github.com/freeplane/freeplane/commit/73c2e5105a198d381f9bdc873642b097e987c869) |
| 2009-08-06 | `api_change` | use old style long node editor for nodes containing line break | `EditAction.java` | [49fbf66c](https://github.com/freeplane/freeplane/commit/49fbf66cebdfc664ad95206bc5950d9428218a9b) |
| 2009-08-06 | `fix` | bug fixes for edge style null ignore wrong zip file by importMindManagerFiles | `EdgeBuilder.java`, `EdgeStyle.java` +4 | [3f91d93e](https://github.com/freeplane/freeplane/commit/3f91d93eac60f4604fbdfb95985722d27093ab31) |
| 2009-08-04 | `feature` | add svn keywords to history_en.txt | `history_en.txt` | [9a09b63c](https://github.com/freeplane/freeplane/commit/9a09b63c8b4a0a5c6965b0b3710a13f951a62a55) |
| 2009-08-03 | `fix` | bug fix: close edit field if node is deleted | `EditNodeTextField.java` | [d22a54b7](https://github.com/freeplane/freeplane/commit/d22a54b7e0d01664431fb912fc4c65fccced0f4c) |
| 2009-08-02 | `feature` | enable link pop-up menu even if neither target nor source node is selected. Links where ta | `MapView.java` | [ec390ba2](https://github.com/freeplane/freeplane/commit/ec390ba24646419182f5937fecdbd6fac114e661) |
| 2009-08-02 | `fix` | bug fix for  cut / paste alert [freeplane - Open Discussion] | `IMapChangeListener.java`, `MapController.java` +10 | [70a06b41](https://github.com/freeplane/freeplane/commit/70a06b411a3c2e25c8e190534b9d2e8665beb331) |
| 2009-08-01 | `fix` | applying patches from bug 0000159 | `Filter.java`, `FilterComposerDialog.java` +19 | [80f5c245](https://github.com/freeplane/freeplane/commit/80f5c2452e6dffad5588cf1493063210d4f3c305) |
| 2009-08-01 | `feature` | always display f-bar on a new line | `ToggleToolbarAction.java`, `ViewController.java` +3 | [5fb2653a](https://github.com/freeplane/freeplane/commit/5fb2653a24afeed6e6fc300d625b2321bd15c702) |
| 2009-07-31 | `fix` | bug if in "import folder structure" | `ImportFolderStructureAction.java` | [cb400f9e](https://github.com/freeplane/freeplane/commit/cb400f9e252606f0f9c57e9dc316beb136524595) |
| 2009-07-31 | `fix` | bug fixes for deleted nodes in reminder blinker and in node history | `ReminderHook.java`, `NodeHistory.java` | [dd6ade19](https://github.com/freeplane/freeplane/commit/dd6ade1981269d817ea752adae75464932b6d77c) |
| 2009-07-29 | `fix` | bug fixes for automatically reported  bugs | `MapModel.java`, `LinkController.java` +2 | [81d56be4](https://github.com/freeplane/freeplane/commit/81d56be413d6b73c1d1b300a10caa4e6fe388e07) |
| 2009-07-26 | `fix` | bug fix in last opened list for '&' in file names | `MenuBuilder.java`, `FreeplaneStarter.java` +2 | [dd698f40](https://github.com/freeplane/freeplane/commit/dd698f400e53d09a18a18b2aeef3b1d10b4cfa99) |
| 2009-07-26 | `fix` | bug fix: keep selected node position after filtering bug fix: use actual values for select | `FilterInfo.java`, `UnfoldAncestorsAction.java` +5 | [d37f3d62](https://github.com/freeplane/freeplane/commit/d37f3d6267d8dd42b287b4089f0a519a4f8d799d) |
| 2009-07-25 | `fix` | bug fix in last opened list | `LastOpenedList.java` | [e7a9491e](https://github.com/freeplane/freeplane/commit/e7a9491e63bde632082d96634101e629b4595136) |
| 2009-07-25 | `fix` | split_pane patch 153 (thanks to Tamas Eppel) | `SetNoteWindowPosition.java` | [22ff90b8](https://github.com/freeplane/freeplane/commit/22ff90b8b87465714bfe4e7045eff06008f4c14b) |
| 2009-07-25 | `fix` | export_branch_name patch 154 (thanks to Tamas Eppel) | `ExportBranchAction.java` | [15c1f006](https://github.com/freeplane/freeplane/commit/15c1f006b86b1e8f1ac55106ce039f743e591204) |
| 2009-07-25 | `fix` | find_bugs patch 152 (thanks to Tamas Eppel) | `TreeXmlWriter.java`, `MapModel.java` +27 | [e2548d29](https://github.com/freeplane/freeplane/commit/e2548d29cc2c80bb501d2960284725f30df9b130) |
| 2009-07-25 | `fix` | bug fixes for last open file list | `Controller.java`, `LastOpenedList.java` | [bd377975](https://github.com/freeplane/freeplane/commit/bd3779751f29a75f22d91f3cc34dbf7099b26491) |
| 2009-07-24 | `feature` | new keys for i18n | `Resources_hr.properties` | [3602152f](https://github.com/freeplane/freeplane/commit/3602152f9b6314dfabc36635d3fae06f5aab10a9) |
| 2009-07-23 | `feature` | bug fix: do not start new timer on blinking in reminder | `ReminderExtension.java`, `ReminderHook.java` +1 | [fcb759d7](https://github.com/freeplane/freeplane/commit/fcb759d7d8056f55f752148b4620f57df144b4e5) |
| 2009-07-22 | `fix` | bug fix: resize tool bar pane on all validateTree events | `ToggleToolbarAction.java`, `ViewController.java` | [e5af6784](https://github.com/freeplane/freeplane/commit/e5af67842e94239642d5d32206f7867a3e644371) |
| 2009-07-22 | `fix` | bug fix in pasting file list from clipboard | `LinkController.java`, `PasteAction.java` | [07a4e8f1](https://github.com/freeplane/freeplane/commit/07a4e8f1f0b6109321eede8540ba9d3146404159) |
| 2009-07-21 | `fix` | bug fix: child nodes of encrypted node loaded in wrong order | `EncryptionModel.java` | [334d608b](https://github.com/freeplane/freeplane/commit/334d608bc39e7aa81b5982e9a4129492609f793c) |
| 2009-07-21 | `fix` | bug fix: links to mind map files | `UrlManager.java` | [0d73cff7](https://github.com/freeplane/freeplane/commit/0d73cff79fb0c7e1d44c2d69188547bf8adde576) |
| 2009-07-21 | `fix` | bug fix: properly display button selection | `FreeplaneToolBar.java` | [10c4285e](https://github.com/freeplane/freeplane/commit/10c4285ed027d26cd0713e424146dd8c2408cf62) |
| 2009-07-20 | `fix` | do not send bug report if look and feel is not found | `Controller.java` | [994cd3e0](https://github.com/freeplane/freeplane/commit/994cd3e06d68e6b5e3cc1171c6dc5b490c59ba4b) |
| 2009-07-19 | `fix` | bug fix: use cloud properties copying/pasting format | `Pattern.java`, `StylePatternFactory.java` | [7f51db0d](https://github.com/freeplane/freeplane/commit/7f51db0d946c9b46c8efd673cb3ff8e6eb3f2b85) |
| 2009-07-19 | `fix` | bug fix in f-bar | `FButtonBar.java`, `Compat.java` +1 | [d4481a2f](https://github.com/freeplane/freeplane/commit/d4481a2f0dfb5f087378a237e0b705030e68b937) |
| 2009-07-18 | `fix` | bug fix: update map view name after exporting branch | `ExportBranchAction.java` | [2e13ba03](https://github.com/freeplane/freeplane/commit/2e13ba03fd41e34fa3556657f71e5fed36d73c6d) |
| 2009-07-15 | `fix` | bug fix: display all maps in recently opened map list | `LastOpenedList.java` | [f6cdca85](https://github.com/freeplane/freeplane/commit/f6cdca85db1c57dd09b18e156a8e56368ae29167) |
| 2009-07-11 | `fix` | bug fix: completely hide tool bar panel if all tool bars are disabled | `ViewController.java` | [0f7e58e0](https://github.com/freeplane/freeplane/commit/0f7e58e0c2bac81ab3623161453c04b1ed67e08f) |
| 2009-07-10 | `fix` | bug fix in copy single node | `NodeWriter.java` | [7b167f29](https://github.com/freeplane/freeplane/commit/7b167f29b1a837be4b759223b694d5f2f6dd40b5) |
| 2009-07-09 | `fix` | bug fix [Bugs 0000130]: Ambiguous filter options state in menu after switching to another  | `ApplyToVisibleAction.java`, `FilterController.java` +7 | [b68eb7c9](https://github.com/freeplane/freeplane/commit/b68eb7c9bc4d8aa230cf2e45aaadad1d3a494126) |
| 2009-07-09 | `fix` | bug fix on loading | `AutomaticLayout.java` | [d50eebd6](https://github.com/freeplane/freeplane/commit/d50eebd6d3f9b9f4ae13004a5c4a95c35497c99a) |
| 2009-07-09 | `fix` | [Bugs 0000133]: SEVERE BUG: specially formatted nodes within encrypted nodes automatically | `NodeTextBuilder.java` | [7d91a967](https://github.com/freeplane/freeplane/commit/7d91a967675784882481904cbd29830fa4a0d66c) |
| 2009-07-08 | `fix` | bug fix: can not close map if no map is open | `MapViewController.java` | [f155a73a](https://github.com/freeplane/freeplane/commit/f155a73a1423671c794b5e9aa11028dd29119b2e) |
| 2009-07-06 | `fix` | bug fixes for applet | `FilterController.java` | [7afc05a6](https://github.com/freeplane/freeplane/commit/7afc05a6bbe384cd136e24dd01fc48847128c666) |
| 2009-07-06 | `fix` | bug fixes for applet | `browsemodemenu.xml`, `MenuBuilder.java` +7 | [93c89b9d](https://github.com/freeplane/freeplane/commit/93c89b9d61e19aa4c5b775542588414bb41a72e1) |
| 2009-07-05 | `fix` | multiple bug fixes f-bar | `textPatterns.properties`, `f1.png` +53 | [6cab03d2](https://github.com/freeplane/freeplane/commit/6cab03d2c832f1dd7c43ca2b077f2a9bb081df2e) |
| 2009-06-28 | `fix` | bug fix: do not repaint removed selected nodes | `NodeView.java` | [75b1a9a0](https://github.com/freeplane/freeplane/commit/75b1a9a006366250a425dce30bcb315daa96e30a) |
| 2009-06-28 | `fix` | bug fixes in saving links | `MapModel.java`, `NodeModel.java` +1 | [b95d750e](https://github.com/freeplane/freeplane/commit/b95d750e77ea349195a170e76c750d6257eab7ed) |
| 2009-06-23 | `fix` | bug fix: saving of notes being edited | `NoteController.java`, `NoteWriter.java` +1 | [a8be0e77](https://github.com/freeplane/freeplane/commit/a8be0e7728797911f421b3c1473b05c6a1751592) |
| 2009-06-21 | `feature` | add new edge styles to default selection in preferences | `preferences.xml` | [f16e364f](https://github.com/freeplane/freeplane/commit/f16e364f5625da1b8a1d73e1e0aed4175a58e504) |
| 2009-06-20 | `fix` | bug fix: keep map file change in last open list | `IMapTitleChangeListener.java`, `ViewController.java` +8 | [6641101d](https://github.com/freeplane/freeplane/commit/6641101d0ce659c30330017e8f0dd7808889220a) |
| 2009-06-20 | `fix` | bug fix for tool tip width | `Resources_cs.properties`, `Resources_da.properties` +26 | [b1c1504f](https://github.com/freeplane/freeplane/commit/b1c1504f979bc1d550b963335860c3dec3f43b9f) |
| 2009-06-19 | `feature` | add show/hide note window action to map popup menu | `mindmapmodemenu.xml` | [98a7ddec](https://github.com/freeplane/freeplane/commit/98a7ddecbc32076af31fb23eb3f982c4bc78a08c) |
| 2009-06-19 | `fix` | bug fix for editing nodes with images for unsaved maps | `NoteManager.java`, `EditNodeWYSIWYG.java` | [4fa6296c](https://github.com/freeplane/freeplane/commit/4fa6296ce82675f2b427ec13b1ca4b8e28da0b4e) |
| 2009-06-19 | `feature` | close attribute manager dialog if new map == null or has no attributes | `AttributeManagerDialog.java` | [084f11bc](https://github.com/freeplane/freeplane/commit/084f11bccd81bb7d63e678ed2f9b28cb7350571b) |
| 2009-06-19 | `fix` | bug fix: ignore set attribute view type if no map is opened | `HideAllAttributesAction.java`, `ShowAllAttributesAction.java` +1 | [a6899bda](https://github.com/freeplane/freeplane/commit/a6899bda3735239828925599aa68d1c7384eab43) |
| 2009-06-19 | `fix` | bug fix for remove reminder action: make it @enabled action | `ModeController.java`, `AFreeplaneAction.java` +4 | [cb2736e0](https://github.com/freeplane/freeplane/commit/cb2736e03833d28e2d33472f419d5bdabe8e676a) |
| 2009-06-18 | `fix` | bug fix in find dialog | `FindAction.java` | [cb2ca807](https://github.com/freeplane/freeplane/commit/cb2ca80734576c72a25675bd1e37cd22c0c926ac) |
| 2009-06-18 | `feature` | bug fix: always add icon at the end | `IconAction.java` | [829d9c01](https://github.com/freeplane/freeplane/commit/829d9c01ed9ed9587fd2b6deb51f2cec1944de8d) |
| 2009-06-18 | `fix` | bug fix map change event | `MapChangeEvent.java`, `MapStyle.java` +1 | [ead48ce5](https://github.com/freeplane/freeplane/commit/ead48ce5aeae3d2a757a23649ed2500cbefedacf) |
| 2009-06-18 | `fix` | bug fix | `CreationModificationPlugin.java` | [957e575e](https://github.com/freeplane/freeplane/commit/957e575ed3dfbb28c8eba792c463ed17aae10849) |
| 2009-06-18 | `feature` | [Bugs 0000109]: "key type add new" option, first character missing | `NewChildAction.java` | [ad1eb69b](https://github.com/freeplane/freeplane/commit/ad1eb69b9046c0898552c3889fc381994a0de0a1) |
| 2009-06-17 | `fix` | bug fixes | `AttributeConditionController.java`, `FindAction.java` | [bfc52c87](https://github.com/freeplane/freeplane/commit/bfc52c8781ece9d602843fd1655048770b8ba02e) |
| 2009-06-16 | `feature` | patch "Support for arbitrary URIs" https://sourceforge.net/tracker/index.php?func=detail&a | `ViewController.java`, `MapController.java` +2 | [aabc414d](https://github.com/freeplane/freeplane/commit/aabc414d06c899479ce06e05a5ce5597fbef6fb8) |
| 2009-06-16 | `fix` | bug fix on removing edit node text field | `EditNodeTextField.java` | [baaae814](https://github.com/freeplane/freeplane/commit/baaae81476a1827a782d574971251a12bbaf3b81) |
| 2009-06-16 | `fix` | bug fixes | `MapController.java`, `NodeStyleModel.java` +3 | [9c7dd81b](https://github.com/freeplane/freeplane/commit/9c7dd81b7b5fd938780dbc6f035a5263b3849abc) |
| 2009-06-14 | `fix` | bug report dialog and bug report policy option in preferences | `preferences.xml`, `freeplane.properties` +2 | [9631078d](https://github.com/freeplane/freeplane/commit/9631078d9682493f964a7e855bdd3192807cf8d0) |
| 2009-06-11 | `fix` | [Bugs 0000094]: Error splitting (rich text) long node - with revsion tracking Bug fix in s | `MapController.java`, `CreationModificationPlugin.java` +1 | [6ba409ff](https://github.com/freeplane/freeplane/commit/6ba409ff044bbbeea2ce81e051c139e66ab9775a) |
| 2009-06-05 | `fix` | bug fix: disable use of escape characters in internal representation of URLs for files | `Compat.java` | [695bd42c](https://github.com/freeplane/freeplane/commit/695bd42c1bf33cd9aedb6f13f90f4faca07a81d6) |
| 2009-06-05 | `fix` | bug fix: disable use of escape characters in internal representation of URLs for files | `Compat.java` | [cb5d3253](https://github.com/freeplane/freeplane/commit/cb5d3253d8897ae0e0638a55ca68d977ff526408) |
| 2009-06-05 | `fix` | bug fix: disable use of escape characters in internal representation of URLs for files | `Compat.java` | [8365f0d5](https://github.com/freeplane/freeplane/commit/8365f0d5ccc5f166d3185a3d75ff2fe14bbd80a4) |
| 2009-06-05 | `fix` | bug fix: disable use of escape characters in internal representation of URLs for files | `Compat.java`, `MapModel.java` +3 | [635b235a](https://github.com/freeplane/freeplane/commit/635b235a1e291a7c65d2e17d6d9141b00acdd867) |
| 2009-05-28 | `feature` | [Bugs 0000071]: In Notes Window, the default font remains as Serif even if you change Pref | `SimplyHTML.jar`, `MNoteController.java` +2 | [21fbc4bb](https://github.com/freeplane/freeplane/commit/21fbc4bb343d07d45e8ab7537dc8b1843c3bfbbc) |
| 2009-05-27 | `fix` | [Bugs 0000063] bug fixes when empty mode is selected | `Controller.java`, `ViewController.java` +6 | [3a33e9fc](https://github.com/freeplane/freeplane/commit/3a33e9fcb461584c78c99645ecda98ccc51c4778) |
| 2009-05-24 | `fix` | bug fix [Bugs 0000061]: reading of attribute registry | `AttributeBuilder.java` | [440103fb](https://github.com/freeplane/freeplane/commit/440103fbb12060d9943d7727d79e981ada129579) |
| 2009-05-22 | `fix` | bug fixes for encrypted nodes and maps | `EncryptionModel.java`, `DesEncrypter.java` +2 | [04c644ac](https://github.com/freeplane/freeplane/commit/04c644ac258a22e5ea1d204f44536081b24220d5) |
| 2009-05-18 | `fix` | bug fix [Bugs 0000058]: short node edit mode toggle | `NewChildAction.java` | [199ea425](https://github.com/freeplane/freeplane/commit/199ea425d43cc8bc9bcc068ad1954bab84ad1c5d) |
| 2009-05-18 | `fix` | bug fix [Bugs 0000049]: missed edge styles in node format menu | `StylePatternPanel.java`, `Resources_en.properties` | [247f4bc1](https://github.com/freeplane/freeplane/commit/247f4bc1f7009d06a16ec549e530d42c808037a4) |
| 2009-05-18 | `fix` | bug fix [Bugs 0000049]: missed edge styles in node format menu | `StylePatternPanel.java` | [4c60f08f](https://github.com/freeplane/freeplane/commit/4c60f08fff15b2090423a9a2a2f0d271dde3add1) |
| 2009-05-18 | `fix` | bug request, feature request and help request actions | `browsemodemenu.xml`, `filemodemenu.xml` +14 | [b181724e](https://github.com/freeplane/freeplane/commit/b181724e5affeb58b2678c78e741e40c337774c4) |
| 2009-05-11 | `fix` | bug fix: disable reading of local files when running groovy scripts | `MANIFEST.MF`, `UpdateCheckAction.java` +3 | [0aff8c4b](https://github.com/freeplane/freeplane/commit/0aff8c4b6d7b9d90fc1dd0ea09aa9c8e89e90775) |
| 2009-05-10 | `fix` | bug fix: use original file name in automatically saved files | `DoAutomaticSave.java` | [858e3317](https://github.com/freeplane/freeplane/commit/858e331725612f66dab9a06eec99550f976fe28a) |
| 2009-05-10 | `fix` | bug fix for nodes changing map side bug fix for list of last opened maps | `browsemodemenu.xml`, `filemodemenu.xml` +4 | [3611725a](https://github.com/freeplane/freeplane/commit/3611725a3ed4907a723d6f3ff1848bd166f3f26d) |
| 2009-05-09 | `fix` | bug fix for save all action options for editor dialog placement and layout | `Resources_ar.properties`, `Resources_ca.properties` +34 | [48209d8c](https://github.com/freeplane/freeplane/commit/48209d8c92e3510399321132bc5472493833d9ae) |
| 2009-05-07 | `fix` | bug fix in xml parser | `XMLParser.java` | [ce629909](https://github.com/freeplane/freeplane/commit/ce629909a21122f9d24ab04bee428ec345dcb5fe) |
| 2009-05-06 | `fix` | bug fix in remove icon action | `RemoveIconAction.java` | [34bd717b](https://github.com/freeplane/freeplane/commit/34bd717b6cfe063eb10d7a6bdcd8689681be8886) |
| 2009-05-05 | `fix` | bug fix: place dialogs visible if properties become corrupted | `WindowConfigurationStorage.java`, `UITools.java` +1 | [b1fd963c](https://github.com/freeplane/freeplane/commit/b1fd963c9d567d434650d29d61c9ad06fea8052c) |
| 2009-05-05 | `fix` | bug fix: drag and drop oh html links from firefox bug fix: encrypted nodes bug fix: Java e | `preferences.xml`, `ShowFilterToolbarAction.java` +11 | [5556c20e](https://github.com/freeplane/freeplane/commit/5556c20eae1dededc74091921415519334bb6eaa) |
| 2009-05-02 | `fix` | bug fix saving patterns.xml | `Pattern.java` | [7bf30c62](https://github.com/freeplane/freeplane/commit/7bf30c62fe7c09ddd0055e181103f599f699b2bd) |
| 2009-05-01 | `fix` | bug fix: ignore false note document update events | `MapController.java`, `MNoteController.java` | [6afcd9df](https://github.com/freeplane/freeplane/commit/6afcd9dfbe5e260fdbe79c8c199d1ac6e7c34039) |
| 2009-05-01 | `fix` | minor bug fixes | `ExportWithXSLT.xml`, `mindmapmodemenu.xml` +2 | [52844859](https://github.com/freeplane/freeplane/commit/528448596b348fcf604b59cd536d3c8c12af5688) |
| 2009-05-01 | `fix` | Bug fixes in filter controller | `ApplyToVisibleAction.java`, `FilterController.java` +2 | [1d0272b0](https://github.com/freeplane/freeplane/commit/1d0272b04ce96977d7796493ed5749347aa30e97) |
| 2009-04-30 | `fix` | bug fixes for automatic layout | `MEdgeController.java`, `Pattern.java` +1 | [1fc099ed](https://github.com/freeplane/freeplane/commit/1fc099ed4f1e4d0460280581e9e423709997a24c) |
| 2009-04-30 | `fix` | bug fix for folding | `MMapController.java` | [bc6ca106](https://github.com/freeplane/freeplane/commit/bc6ca106102bcad48d090edfe508c1db811eceac) |
| 2009-04-27 | `fix` | bug fixes | `Resources_ar.properties`, `Resources_ca.properties` +38 | [6d5f6959](https://github.com/freeplane/freeplane/commit/6d5f6959d357fdb7acf5a9568eb98cab8cee04f7) |
| 2009-04-25 | `fix` | text labels for links bug fix: note editor size after switching from browse mode to tab wi | `ArrowLinkModel.java`, `LinkBuilder.java` +9 | [80edbaa5](https://github.com/freeplane/freeplane/commit/80edbaa54847dddef01c17f8b49103c0653bfd5b) |
| 2009-04-24 | `fix` | Bug fix: note editor on mode change | `MNoteController.java` | [4e0110cc](https://github.com/freeplane/freeplane/commit/4e0110cc4c4f97ae17f1aff729306b681e30c6d0) |
| 2009-04-22 | `fix` | minor bug fixes | `ExportWithXSLT.xml`, `FpStringUtils.java` +4 | [fc48a51d](https://github.com/freeplane/freeplane/commit/fc48a51d8343584e3eb8ccb40dae2e5be156de55) |
| 2009-04-21 | `fix` | Bug fixes for remove icon | `RemoveIconAction.java` | [4f9439e1](https://github.com/freeplane/freeplane/commit/4f9439e1ac17b31288fba7cb808c60bf7a61d813) |
| 2009-04-21 | `fix` | Bug fix for [Bugs 0000038]: Key mapping failures | `browsemodemenu.xml`, `filemodemenu.xml` +3 | [6bd43e42](https://github.com/freeplane/freeplane/commit/6bd43e4244950d70941b6098061909dfe311fb65) |
| 2009-04-20 | `fix` | bug fixes for exporting flash and applet | `MANIFEST.MF`, `flashobject.js` +31 | [0f7a3193](https://github.com/freeplane/freeplane/commit/0f7a3193cb26bbcc72ebf9856e49b85559a9e674) |
| 2009-04-19 | `fix` | Bug fix [Bugs 0000037]: Filter toolbar does not turn off via toolbar icon | `FreeplaneVersion.java`, `ShowFilterToolbarAction.java` +1 | [f6b3c028](https://github.com/freeplane/freeplane/commit/f6b3c0282ac8e31ae19875d5e995ab56f8b9a154) |
| 2009-04-19 | `fix` | bug fix for initial map loading | `ApplicationResourceController.java`, `FreeplaneStarter.java` +2 | [7f6e61fc](https://github.com/freeplane/freeplane/commit/7f6e61fceb16dc9e475a8d0627309585b37104ba) |
| 2009-04-18 | `fix` | bug fix if no map is loaded | `FreeplaneVersion.java`, `FreeplaneStarter.java` | [21f3c121](https://github.com/freeplane/freeplane/commit/21f3c1219eb1e305a079721c81f8fa9e2fd485a6) |
| 2009-04-14 | `feature` | Frame initialization New icons | `Freeplane_frame_icon.png`, `Freeplane_splash.png` +14 | [6aafee69](https://github.com/freeplane/freeplane/commit/6aafee69dd585bbafe41b8dca227984762056a28) |
| 2009-04-13 | `fix` | CenterSelectedNodeAction bug fix minor other fixes | `CenterSelectedNodeAction.java`, `EdgeWidthAction.java` +1 | [16b5e199](https://github.com/freeplane/freeplane/commit/16b5e19905bcb65646a579afda358a788645eb7f) |
| 2009-04-12 | `fix` | minor bug fixes | `Resources_da.properties`, `Resources_de.properties` +4 | [b0b0fec7](https://github.com/freeplane/freeplane/commit/b0b0fec7b1e8acae99fa4bdf43b57c1e542375c8) |
| 2009-04-11 | `fix` | minor changes bug fix for [Bugs 0000024]: insert and then CTRL + Z leaves screen artifacts | `Resources_ar.properties`, `Resources_cs.properties` +43 | [f9f239b8](https://github.com/freeplane/freeplane/commit/f9f239b8eb2ff1e89efabcbb3268aed965ad5386) |
| 2009-03-30 | `fix` | bug fix filter history | `Filter.java`, `FilterHistory.java` | [3e30dd33](https://github.com/freeplane/freeplane/commit/3e30dd33c3246c37aa6a88eb3fd25003924af9b3) |
| 2009-03-29 | `fix` | bug fix edge width should be applied to the line under the fork style node | `ForkMainView.java` | [5319a4c1](https://github.com/freeplane/freeplane/commit/5319a4c141c797b15ef323c5e25d1170a9f722e9) |
| 2009-03-28 | `fix` | bug fix in map layout for filtered maps | `NodeViewLayoutAdapter.java` | [5fa9f8ed](https://github.com/freeplane/freeplane/commit/5fa9f8ed85aa4d0b753da02af594e8d8a5ea6cbd) |
| 2009-03-27 | `fix` | Bug fix 0000022: following a link to a closed node fails Bug fix: link antialiasing | `MapController.java`, `MapView.java` | [2c8e6fa8](https://github.com/freeplane/freeplane/commit/2c8e6fa8a16fafeca1fd4bbffdf3c007bcfbfd75) |
| 2009-03-27 | `fix` | Bug fix 0000021: Selected node's order reverses when moved under parent node | `ChangeNodeLevelController.java` | [33023825](https://github.com/freeplane/freeplane/commit/33023825b956efe52fcd360620645c637b7061ac) |
| 2009-03-27 | `fix` | Bug fix 0000011: "Enter Confirms" Not remembered by freeplane | `EditNodeDialog.java` | [1f5a8c43](https://github.com/freeplane/freeplane/commit/1f5a8c43ef853ae1a57d1f65f99812aa8a276831) |
| 2009-03-21 | `fix` | Bug fixes for file mode | `NodeModel.java`, `FNodeModel.java` | [6da20ec6](https://github.com/freeplane/freeplane/commit/6da20ec6ae4f014a0e206864220085b3a0e6f2e7) |
| 2009-03-21 | `fix` | Bug fix: [Bugs 0000016]: List of maps missing from Maps menu | `browsemodemenu.xml`, `filemodemenu.xml` +7 | [c111f4d5](https://github.com/freeplane/freeplane/commit/c111f4d5060ee0f52428ed97d6410e87ff1e20d8) |
| 2009-03-21 | `fix` | Bug fix for [Bugs 0000021]: Selected node's order reverses when moved under parent node | `ChangeNodeLevelController.java` | [09b43e1a](https://github.com/freeplane/freeplane/commit/09b43e1ab97f518ba71477536b0b54af3376490d) |
| 2009-03-20 | `feature` | Refactoring: IFreeplaneAction moved to org.freeplane.core.resources.ui New Action Extractr | `Resources_de.properties`, `mindmapmodemenu.xml` +49 | [b6f3eb2c](https://github.com/freeplane/freeplane/commit/b6f3eb2c8fe14617d562a63cbf1716451e35db86) |
| 2009-03-19 | `fix` | bug fix for centering the root node after map is onpen | `ViewController.java`, `NoteModel.java` +6 | [23ca0d17](https://github.com/freeplane/freeplane/commit/23ca0d179081ba2aa1176b9860305c9afd3577e2) |
| 2009-03-18 | `fix` | bug fixes in drag, drop and paste | `MMapController.java`, `NodeUpAction.java` +4 | [d7f90082](https://github.com/freeplane/freeplane/commit/d7f9008295c0f98020fa81cf055961ee542410df) |
| 2009-03-18 | `fix` | bug fix: filter for numeric values bug fix: creation of format change dialog | `CompareConditionAdapter.java`, `StylePatternFactory.java` | [10019d8d](https://github.com/freeplane/freeplane/commit/10019d8d44f69c5a5d96720a2a59965dfeb1781c) |
| 2009-03-15 | `fix` | bug fix for zoom out | `ViewController.java` | [c910d4d7](https://github.com/freeplane/freeplane/commit/c910d4d708644294417573eeb4c23f2f58a786d6) |
| 2009-03-15 | `fix` | bug fixes for local hyperlinks | `MapController.java`, `FollowLinkAction.java` +4 | [e86620e0](https://github.com/freeplane/freeplane/commit/e86620e05435dc058194a89cb3de12f93f887aaa) |
| 2009-03-13 | `fix` | Bug fixes for DontShowMeAgain dialog properties DontShowNotificationPropterty replaced by  | `preferences.xml`, `DontShowNotificationProperty.java` +11 | [33f5d760](https://github.com/freeplane/freeplane/commit/33f5d760fd8dc37772d9b04e4f2a049e2ab0be57) |
| 2009-03-11 | `fix` | 1. Map background saved in map file 2. Reset to default as option for color selection dial | `MANIFEST.MF`, `Resources_ar.properties` +107 | [2caa43aa](https://github.com/freeplane/freeplane/commit/2caa43aaacf0db56a238274df9f7de39a667793c) |
| 2009-03-08 | `feature` | New XSLT export dialog translations from ewl | `Resources_de.properties`, `Resources_fr.properties` | [720705d1](https://github.com/freeplane/freeplane/commit/720705d1cd20d4d925592a444c3ff8b673ba2573) |
| 2009-03-08 | `feature` | New options for saving <combo name="save_folding"> 	<choice value="never_save_folding"/> 	 | `Resources_de.properties`, `preferences.xml` +21 | [5c258283](https://github.com/freeplane/freeplane/commit/5c258283054d909b06a1f8784618449a2ce1666e) |
| 2009-03-07 | `fix` | Zoom keep selected node position Bug fix: zoomcombibox displayed | `ViewController.java`, `MapView.java` | [5a559fae](https://github.com/freeplane/freeplane/commit/5a559fae660c8556f4b1f79850ae4924931b3b36) |
| 2009-03-07 | `fix` | bug in AttributePopupMenu fixed bug in PaintFoldingMark fixed | `ForkMainView.java`, `MainView.java` +2 | [3eb6f7fd](https://github.com/freeplane/freeplane/commit/3eb6f7fd818dd6ba9da9a6855d61e3bacbe4d62b) |
| 2009-03-01 | `fix` | Bug fix 0000008: using CTRL + arrow key left moves node to next parent freeplane.sh improv | `MMapController.java`, `NodeUpAction.java` +7 | [4888373c](https://github.com/freeplane/freeplane/commit/4888373c7c5f2312378b9e14726befa649964342) |
| 2009-02-26 | `feature` | Bug fix: pressing escape while editing a new node causes visual artifacts | `EditNodeTextField.java`, `MapViewController.java` | [87585dd3](https://github.com/freeplane/freeplane/commit/87585dd357ae99502d056abf167ce970b9e2389d) |
| 2009-02-26 | `feature` | Patch "New XSLT export dialog working like a normal Save As dialog" Thanks to ewl | `ExportDialog.java`, `ExportWithXSLT.java` +1 | [afdae1ed](https://github.com/freeplane/freeplane/commit/afdae1ed495bace41bb06f56aa1db5a3b424ac9b) |
| 2009-02-26 | `feature` | Bug fix: scrolling for icon tool bar New icons for windows and linux | `ViewController.java`, `JAutoScrollBarPane.java` +5 | [38a87988](https://github.com/freeplane/freeplane/commit/38a879887a706a387fc1bf7640fd123a9e39cb3c) |
| 2009-02-23 | `fix` | FreeMind patch [ 2601419 ] Location of the Note Window can be set on the Menu integrated. | `Resources_de.properties`, `mindmapmodemenu.xml` +5 | [2ba8e8ff](https://github.com/freeplane/freeplane/commit/2ba8e8ff693ad2a1cdf162401a0cd79d62a8a32f) |
| 2009-02-22 | `fix` | unget services requested in Freeplane osgi activator bug fix: set flag map changed from la | `Activator.java`, `LatexNodeHook.java` | [296accb9](https://github.com/freeplane/freeplane/commit/296accb9fded1f9b93164e5b18c36828100ce0c1) |
| 2009-02-22 | `api_change` | prefix "I" added to interface names | `IFreeplaneAction.java`, `INamed.java` +1 | [03ddeb1b](https://github.com/freeplane/freeplane/commit/03ddeb1b991f4333f26ca8e843c32ad4b585df1d) |
| 2009-02-22 | `api_change` | prefix "I" added to interface names | `Activator.java`, `IControllerExtensionProvider.java` +5 | [e208b809](https://github.com/freeplane/freeplane/commit/e208b809b1f042ce568f0438947b9140e1a1f348) |
| 2009-02-16 | `feature` | in general, i brushed up collection handling in some classes, did some refactorings to get | `MANIFEST.MF`, `Compat.java` +189 | [4a143a61](https://github.com/freeplane/freeplane/commit/4a143a61e047a3ccc33f0757de41ceacef344dd9) |
| 2009-01-17 | `fix` | automatic clean up after previous bug fixing | `PersistentNodeHook.java`, `CreationModificationPlugin.java` +3 | [533f693d](https://github.com/freeplane/freeplane/commit/533f693d5fb26fb5cfd32077ce5606dd33601203) |

### Dettagli commit con note

**[5c258283](https://github.com/freeplane/freeplane/commit/5c258283054d909b06a1f8784618449a2ce1666e)** (2009-03-08) — New options for saving <combo name="save_folding"> 	<choice value="never_save_folding"/> 	<choice value="save_folding_if_map_is_changed"/> 	<choice value="always_save_folding"/> </combo> <boolean name="save_modification_times"/>

> New options for loading
> <comboname="load_folding">
> 	<choice value="always_fold_all_after_load"/>
> 	<choice value="load_folding_from_map_default_fold_all"/>
> 	<choice value="load_folding_from_map_default_unfold_all"/>
> 	<choice value="always_unfold_all_after_load"/>
> </combo>

**[4a143a61](https://github.com/freeplane/freeplane/commit/4a143a61e047a3ccc33f0757de41ceacef344dd9)** (2009-02-16) — in general, i brushed up collection handling in some classes, did some refactorings to get to a cleaner structure. i introduced some places to manage constants and did some changes to the controller class. I refactored some static methods and grouped them together. This commit shouldn't have any impact on the end user experience.

> - introduced Compat.java which handles jdk specific things
> - IFreeplaneAction should be implemented by every Freeplane Action, it should define what is the essence of a freeplane action
> - brushed up handling of 'quit' action in controller using the new interface
> - renamed FreeplaneVersionInformation to FreeplaneVersion
> - introduced ResourceControllerProperties which is the start for enum handling
> - deprecated ActionController, will do the same for ExtensionHashMap, ListHashMap and others
> - edited various commands in order to conform with IFreeplaneAction
> - renamed FreeplaneAction to AFreeplaneAction
> - generally tried to reduce cross cutting dependencies
> 
> - annotated code with TODOS - they could be used as a hint what is left to do - use eclipse tasklist in order to see the tasks
>   - the number of such todos should be kept low in order to keep the noise ratio low, thus i'll execute the todos sooner or later (or somebody else does it)


---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
