# Altro — Commit rilevanti

**Modulo:** `other`  
**Commit rilevanti (feature / fix / api_change):** 471 su 1803 totali

> Commit che toccano aree **trasversali** o non classificabili in un singolo plugin: build system, CI, traduzioni, documentazione generale del progetto.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2026](#2026) — 53 commit
- [2025](#2025) — 24 commit
- [2024](#2024) — 41 commit
- [2023](#2023) — 30 commit
- [2022](#2022) — 13 commit
- [2021](#2021) — 4 commit
- [2020](#2020) — 12 commit
- [2019](#2019) — 13 commit
- [2018](#2018) — 11 commit
- [2017](#2017) — 25 commit
- [2016](#2016) — 37 commit
- [2015](#2015) — 55 commit
- [2014](#2014) — 25 commit
- [2013](#2013) — 59 commit
- [2012](#2012) — 14 commit
- [2011](#2011) — 23 commit
- [2010](#2010) — 21 commit
- [2009](#2009) — 11 commit

---

## 2026

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2026-03-29 | `api_change` | expose-node-tags-ai-tools: Align task script naming with MapTag API | `expose-node-tags-to-ai-tools.md` | [998bc8c6](https://github.com/freeplane/freeplane/commit/998bc8c60e2e4586878f535ddc02808ab986ad79) |
| 2026-03-17 | `feature` | 2026-03-17-clarify-create: Clarify createNodes optional overrides and blank style errors | `015-clarify-create-nodes-optional-fields.md`, `AIToolSet.java` +2 | [6e405f6e](https://github.com/freeplane/freeplane/commit/6e405f6ef20808a43d2655d64593a7e9ec7dde27) |
| 2026-03-15 | `feature` | 2026-03-15-provider-model-discovery-fallback: add model list fallback | `fallback-model-selection-when-provider-model-discovery-fails.md`, `AIModelCatalog.java` +1 | [8cc17ad3](https://github.com/freeplane/freeplane/commit/8cc17ad318ce78471356e8a4b838a7dc5690e8f1) |
| 2026-02-20 | `feature` | 2026-02-20-expose-tags-ai-tools: add AI map-level tag category tools | `expose-node-tags-to-ai-tools.md`, `AIToolSet.java` +5 | [e8e66c8b](https://github.com/freeplane/freeplane/commit/e8e66c8ba7c0878605745e79f7d2f0ac8e9a053f) |
| 2026-02-19 | `fix` | 2026-02-18-hyperlinks: open chat history links via LinkController and fix error URL linkif | `010-open-hyperlinks-from-chat-message-history.md`, `AIChatPanel.java` +4 | [fcd8e951](https://github.com/freeplane/freeplane/commit/fcd8e9517da4de3ca49a64d0d335a93b820d34bf) |
| 2026-02-16 | `fix` | fix constitution location in AGENTS.md | `AGENTS.md` | [4d952192](https://github.com/freeplane/freeplane/commit/4d952192d70352b53406670b0adedb0eb7cae0f6) |
| 2026-02-15 | `feature` | add harmonization statement | `AGENTS.md` | [6fedc207](https://github.com/freeplane/freeplane/commit/6fedc20742e0d55e8b57a0fdc415e65b062c6fc1) |
| 2026-02-15 | `fix` | fix AI panel font size | `AIChatPanel.java`, `ChatMessageStyleApplier.java` +1 | [82fc7d71](https://github.com/freeplane/freeplane/commit/82fc7d7185c868013e84dc9add458357cd2d6211) |
| 2026-02-09 | `feature` | Enable multi-row chat deletion in chat list dialog | `ChatListDialog.java`, `ChatListDialogTest.java` | [90e69ebd](https://github.com/freeplane/freeplane/commit/90e69ebd146cbfd0fcd7f4825332c7273ee3a19e) |
| 2026-02-08 | `fix` | 2026-02-08-transcript-window: preserve full transcript and fix context boundary handling | `048-preserve-full-transcript-outside-context-window.md`, `AIChatPanel.java` +9 | [4cdfbcc7](https://github.com/freeplane/freeplane/commit/4cdfbcc70031fd6d130d0d719729a1bc6a9f0dc0) |
| 2026-02-07 | `feature` | 2026-02-06-chat-turn: add translated undo/redo tooltips and working keyboard shortcuts | `043-ai-chat-turn-undo-redo-and-interrupted-input.md`, `AIChatPanel.java` | [586d39d0](https://github.com/freeplane/freeplane/commit/586d39d0c7c3a0dc2b27a350dd1c78a5b64d740e) |
| 2026-02-07 | `feature` | Fix initial profile injection in new chat sessions | `AssistantProfileSelectionSync.java`, `AssistantProfileSelectionSyncTest.java` | [3f166861](https://github.com/freeplane/freeplane/commit/3f1668618d06364b63983cb942c5db53f2039c56) |
| 2026-02-07 | `feature` | 2026-02-06-conversation-state: add chat memory task drafts | `ai-chat-turn-undo-redo-and-interrupted-input.md`, `token-based-chat-memory-window.md` +1 | [2b73b0e8](https://github.com/freeplane/freeplane/commit/2b73b0e83bd70fb1c2252aed690bdfeb9e7cacc2) |
| 2026-02-06 | `feature` | 2026-02-06-conversation-state: add conversation projector and parity tests | `unified-conversation-state-for-chat-and-history.md`, `ConversationProjector.java` +1 | [f8cef994](https://github.com/freeplane/freeplane/commit/f8cef9945ac2e1738de6c65159ace7733e914127) |
| 2026-02-06 | `feature` | 2026-02-06-conversation-state: add chat state core and planning tasks | `ai-chat-turn-undo-redo-and-interrupted-input.md`, `token-based-chat-memory-window.md` +10 | [95642042](https://github.com/freeplane/freeplane/commit/95642042949314c0691ba71549e0a5382653b82f) |
| 2026-02-05 | `feature` | Add new tasks to backlog | `add-mcp-server-api-key-authentication.md`, `add-secret-field-type-for-settings.md` | [261ff399](https://github.com/freeplane/freeplane/commit/261ff3991e91ba007751d357763e7f338fe72561) |
| 2026-02-03 | `feature` | 2026-02-03-assistant-profiles: add assistant profile chat memory | `chat-memory-system-messages.md`, `AssistantProfileChatMemory.java` +7 | [eec8e09c](https://github.com/freeplane/freeplane/commit/eec8e09c756f27390b4859e4761a8baa555b3e36) |
| 2026-02-01 | `feature` | Add hint for LLM where to find tasks | `AGENTS.md` | [173c8f14](https://github.com/freeplane/freeplane/commit/173c8f14816a08ac1b57574d274e24d99b2062df) |
| 2026-01-31 | `feature` | Add "AI panel" to latest freeplane features | `latestFreeplaneFeatures.mm` | [963c008e](https://github.com/freeplane/freeplane/commit/963c008e62e8fa35095598f9e2f6a1d68f10ed2f) |
| 2026-01-31 | `feature` | 2026-01-31-map-warning: add map selection guidance | `SystemMessageBuilder.java` | [24f30cbd](https://github.com/freeplane/freeplane/commit/24f30cbd5da0479e88b10c5a7d5f0ffa3c0be3aa) |
| 2026-01-31 | `feature` | 2026-01-24-chat-history-transcripts: add transcript store tests | `tool-capable-chat-history-transcripts.md`, `ChatSessionMemoryControllerTest.java` +1 | [ca303015](https://github.com/freeplane/freeplane/commit/ca303015d90e879bcc7f010054f229268cf33e9f) |
| 2026-01-25 | `feature` | 2026-01-18-node-links-and-clone-metadata: add connector editing and node link/clone metada | `expose-node-links-and-clone-metadata-in-tools.md`, `033-expose-node-links-and-clone-metadata-in-tools.md` +30 | [c87733ab](https://github.com/freeplane/freeplane/commit/c87733ab274215250078170e67a2475bd78d6a1e) |
| 2026-01-23 | `fix` | fix history file format | `history_en.txt` | [2b941fbf](https://github.com/freeplane/freeplane/commit/2b941fbfd9409529b36454ee0c93ccd18da9d108) |
| 2026-01-18 | `feature` | 2026-01-18-chat-history-storage Add task for chat history storage | `2026-01-18-chat-history-storage.md` | [786b627e](https://github.com/freeplane/freeplane/commit/786b627eef68620f685fcf6887d70506c35433cd) |
| 2026-01-18 | `feature` | 2026-01-18-node-links-and-clone-metadata Add task for node links and clone metadata tools | `2026-01-18-node-links-and-clone-metadata-tools.md` | [407dc631](https://github.com/freeplane/freeplane/commit/407dc631cde01fae71a80c22aa1725df17139b78) |
| 2026-01-18 | `feature` | 2026-01-18-stop-chat-requests Add task description for stop chat requests | `2026-01-18-stop-chat-requests.md` | [8b17603e](https://github.com/freeplane/freeplane/commit/8b17603ec9bf64c2d1479210c637c142f33a5bcb) |
| 2026-01-18 | `fix` | fix ai plugin bundle imports | `build.gradle` | [72e26512](https://github.com/freeplane/freeplane/commit/72e26512f0c0e92157c53ba9eb2026d5b2830c3d) |
| 2026-01-17 | `feature` | Add delete nodes tool with subtree-root filtering | `add-node-delete-tool.md`, `029-add-node-delete-tool.md` +5 | [3a443ae8](https://github.com/freeplane/freeplane/commit/3a443ae8fa537407771c8d992bdadd4d04c0db5b) |
| 2026-01-17 | `feature` | Add selection tools with selection modes and single-node selection | `add-node-selection-tools-for-ai.md`, `028-add-node-selection-tools-for-ai.md` +11 | [3fd5d90c](https://github.com/freeplane/freeplane/commit/3fd5d90ce947f9075b7902fa360533684bd72148) |
| 2026-01-14 | `feature` | Add provider model allowlist preferences | `add-llm-provider-model-preferences.md`, `AIModelCatalog.java` +4 | [b16f9427](https://github.com/freeplane/freeplane/commit/b16f94278393a01a5e0b5da32ed12566a41eb20d) |
| 2026-01-14 | `feature` | Add new tasks to the backlog | `add-llm-provider-model-preferences.md`, `move-system-prompt-default-to-plugin-properties.md` | [465f8c97](https://github.com/freeplane/freeplane/commit/465f8c9791e472511b756f4d6b4b8bc0afcb73f5) |
| 2026-01-14 | `feature` | Enable Gemini 3 thinking signatures and rely on default base URL | `AIChatModelFactory.java`, `defaults.properties` | [959bf789](https://github.com/freeplane/freeplane/commit/959bf7893961758091cd638f858425e8672fcfa1) |
| 2026-01-12 | `feature` | Add content type selection for new nodes | `add-node-content-edit-tool.md`, `NodeContentApplier.java` +4 | [2f8b630e](https://github.com/freeplane/freeplane/commit/2f8b630e8129fea622a53c3f7ccbbdc59b38eb64) |
| 2026-01-12 | `feature` | Add icon catalog tool and normalize emoji icons | `add-node-content-edit-tool.md`, `AIToolSet.java` +4 | [0510736a](https://github.com/freeplane/freeplane/commit/0510736aae9e7e617ae8914c90edf6c069c260e7) |
| 2026-01-12 | `feature` | Enable bulk edit requests with per-item node identifiers | `constitution.md`, `add-apply-attributes-tool.md` +38 | [d151f8cb](https://github.com/freeplane/freeplane/commit/d151f8cb49a4eeda49815dc50639b277c06c2947) |
| 2026-01-11 | `feature` | Update node content editing and editable content support | `add-node-content-edit-tool.md`, `AIToolSet.java` +27 | [cd33d9cf](https://github.com/freeplane/freeplane/commit/cd33d9cf38f993ce13b4bad3ee4e4991eb2289d0) |
| 2026-01-11 | `feature` | Add undo-aware node content editing with controller injection and tests | `add-node-content-edit-tool.md`, `AIToolSet.java` +17 | [d69c8c0b](https://github.com/freeplane/freeplane/commit/d69c8c0b582085cdd79e24bb48f5d3961ce0deda) |
| 2026-01-11 | `feature` | Add edit tool API definitions | `AIToolSet.java`, `ContentType.java` +3 | [d78fd3fc](https://github.com/freeplane/freeplane/commit/d78fd3fcef518f8c7745c1d33e0f303e00183ca4) |
| 2026-01-11 | `feature` | Add MCP tool call logging in AI panel | `018-add-mcp-tool-calls-to-ai-panel.md`, `Activator.java` +5 | [a73ddcc7](https://github.com/freeplane/freeplane/commit/a73ddcc79317e699b2024fd91e7b3cf72e6882ec) |
| 2026-01-10 | `feature` | Mark task "Add node create and move tools" as finished | `017-add-node-create-and-move-tools-with-anchor-and-summary-rules.md` | [b11f2245](https://github.com/freeplane/freeplane/commit/b11f2245afd76766d20f34c2f06583b6597d6334) |
| 2026-01-10 | `fix` | fix git version information in build | `git.gradle` | [c1530ce2](https://github.com/freeplane/freeplane/commit/c1530ce27f02652801ce0c6f64c2e3d5ee879e63) |
| 2026-01-08 | `feature` | Add node create/move/summary tools with helpers | `add-node-create-and-move-tools-with-anchor-and-summary-rules.md`, `AIToolSet.java` +17 | [202608fc](https://github.com/freeplane/freeplane/commit/202608fcca073d4ac2639e35192763ac07266a43) |
| 2026-01-08 | `feature` | Implement data structures  and define tools for summary nodes | `add-node-create-and-move-tools-with-anchor-and-summary-rules.md`, `AIToolSet.java` +8 | [408eac4d](https://github.com/freeplane/freeplane/commit/408eac4d6cba5cd3f1b673f5977578d839cd2f7f) |
| 2026-01-06 | `feature` | Support summary nodes in node creation / move operations | `add-node-create-and-move-tools-with-anchor-and-summary-rules.md`, `CreateNodesRequest.java` +2 | [2dca187c](https://github.com/freeplane/freeplane/commit/2dca187c137b08b615034cc88a3c77965b4f8b4e) |
| 2026-01-06 | `feature` | Implement subtask: Define request and response structures | `add-node-create-and-move-tools-with-anchor-and-summary-rules.md`, `AnchorPlacement.java` +6 | [0f6fc1e0](https://github.com/freeplane/freeplane/commit/0f6fc1e0fc3bc94e0788a80399f91abc162806e2) |
| 2026-01-05 | `fix` | refactor and fix "enforce budget" condition | `ReadNodeWithContextTool.java`, `ReadNodesWithContextRequest.java` | [c220d73c](https://github.com/freeplane/freeplane/commit/c220d73c2ae47afb68030e902111d1f1dd4dcb58) |
| 2026-01-05 | `feature` | Add motivation section to task definition and split one of the tasks | `constitution.md`, `add-editable-content-for-safe-edits.md` +3 | [766c1d41](https://github.com/freeplane/freeplane/commit/766c1d4117e6afa7293a24daf17e33a346fca5c0) |
| 2026-01-05 | `feature` | plan new tasks | `sprint-002.md` | [b6e3895e](https://github.com/freeplane/freeplane/commit/b6e3895ee53df3aed022ef33892fdede21294224) |
| 2026-01-04 | `feature` | Implement new tools for search and reading | `AIToolSet.java`, `AttributesContentReader.java` +24 | [4ba27cf7](https://github.com/freeplane/freeplane/commit/4ba27cf77e47ace8e35757b55572e62db2992eff) |
| 2026-01-03 | `api_change` | wip Tools API imorovements | `sprint-002.md`, `AIToolSet.java` +13 | [3f95be55](https://github.com/freeplane/freeplane/commit/3f95be55db1acfa76e62273d5d87d289a62c8953) |
| 2026-01-01 | `feature` | Add JsonCreator annotations to support deserialization with Jackson | `ApplyAttributesRequest.java`, `ApplyAttributesResponse.java` +48 | [68270835](https://github.com/freeplane/freeplane/commit/682708352c7c79b05069a1d9e992c38a6ea75209) |
| 2026-01-01 | `feature` | Add refacroting tracking to the constitution | `constitution.md` | [7369faf5](https://github.com/freeplane/freeplane/commit/7369faf5fc5e237b210412c78fd137e6c2aa6804) |
| 2026-01-01 | `feature` | refactor and implement getBreadcrumbs AI tool | `backlog.md`, `sprint-001.md` +7 | [2fc51936](https://github.com/freeplane/freeplane/commit/2fc51936cfd8703eb9ab52c4d4e5d311d4be466e) |

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-12-28 | `feature` | Add backlog and consitution | `backlog.md`, `constitution.md` | [e31c3d99](https://github.com/freeplane/freeplane/commit/e31c3d990c3f710548378de24cbae4b8cd241f8a) |
| 2025-12-28 | `feature` | Add model selector drop-down box | `build.gradle`, `AIChatModelFactory.java` +8 | [7f8d656d](https://github.com/freeplane/freeplane/commit/7f8d656dd8b353223b323249877c784e0e2b4eda) |
| 2025-12-07 | `fix` | fix format translation for mixed escaped and unescaped characters in strings | `FormatTranslation.java`, `FormatTranslationTest.java` | [7cd2304b](https://github.com/freeplane/freeplane/commit/7cd2304b0af633e6ea520427970ed1cd96e8b1af) |
| 2025-08-24 | `feature` | Add AGENTS.md documentation | `AGENTS.md` | [bc81f155](https://github.com/freeplane/freeplane/commit/bc81f155f65d92d7a6be34dc7ccedcfbe2e7e6c0) |
| 2025-08-22 | `feature` | Add SourceForge default download configuration | `publish-sourceforge.yml` | [7dc022e4](https://github.com/freeplane/freeplane/commit/7dc022e435a9a6d3457d9a59db00e7c67539838e) |
| 2025-08-22 | `feature` | Add GitHub Action to publish releases to SourceForge | `publish-sourceforge.yml` | [d80f0bf5](https://github.com/freeplane/freeplane/commit/d80f0bf5ae781247d19069820736d3fe86460245) |
| 2025-08-12 | `feature` | Enhance GitHub release deployment with parallel uploads and tag push | `deploy-github-release.sh` | [bd7312d3](https://github.com/freeplane/freeplane/commit/bd7312d398bf1956b717e05cb7851cd9a107766d) |
| 2025-08-11 | `feature` | Support missing top level classes | `ClassNode.java`, `CodeNode.java` | [7f1b6225](https://github.com/freeplane/freeplane/commit/7f1b6225f87b51c7f76a0d6c3db97df13d7a2531) |
| 2025-08-10 | `feature` | Add GitHub release deployment script | `.gitignore`, `deploy-github-release.sh` | [278dad15](https://github.com/freeplane/freeplane/commit/278dad155da9395443beab67fae1006fbcf7d44a) |
| 2025-08-10 | `fix` | Fix archivePath deprecation in Gradle 9.0 | `mac.dist.gradle` | [ad629e70](https://github.com/freeplane/freeplane/commit/ad629e70ce90242029798480b8360b4cf1df7195) |
| 2025-08-01 | `feature` | Add .claude/ to gitignore | `.gitignore` | [f40e9448](https://github.com/freeplane/freeplane/commit/f40e944859406e35b10e503182e1a5d27338c2ee) |
| 2025-07-31 | `fix` | Update shtml to fix NPE | `build.gradle` | [ffde2697](https://github.com/freeplane/freeplane/commit/ffde2697507a4b8eb3e27fdfe4027bea443ca6c3) |
| 2025-07-29 | `feature` | Add mandatory validation for automated translation work | `CLAUDE.md` | [3c049543](https://github.com/freeplane/freeplane/commit/3c049543d47da398ee9e5b0a08f625fff89b074c) |
| 2025-07-29 | `fix` | Fix directory structure documentation to reflect development reality | `CLAUDE.md` | [b2124111](https://github.com/freeplane/freeplane/commit/b21241115b0b916de708dc64d3cb6cda8497d2b8) |
| 2025-07-29 | `feature` | Enforce mandatory native2ascii usage for translation files | `CLAUDE.md` | [e9a1cfd1](https://github.com/freeplane/freeplane/commit/e9a1cfd1edacaa9c0bce773856b6f922d4248c12) |
| 2025-07-28 | `feature` | Document translation file encoding requirements in CLAUDE.md | `CLAUDE.md` | [c24e4863](https://github.com/freeplane/freeplane/commit/c24e48632fb6f44b11d06d46fb67f884843851d9) |
| 2025-07-27 | `feature` | Add comprehensive CLAUDE.md documentation to 1.12.x | `CLAUDE.md` | [0cc1623e](https://github.com/freeplane/freeplane/commit/0cc1623ec0c3f043b184323ac392feb3b53e7e6c) |
| 2025-07-27 | `feature` | Add mandatory Feature-Driven Testing Process to CLAUDE.md | `CLAUDE.md` | [c03b6bb8](https://github.com/freeplane/freeplane/commit/c03b6bb80e46fd40d9ebeb1d366a7c4d8b733dfc) |
| 2025-07-27 | `feature` | Add unused imports cleanup to CLAUDE.md code standards | `CLAUDE.md` | [f76ec90e](https://github.com/freeplane/freeplane/commit/f76ec90ebd71c94306ae55e6410c78f7850e8033) |
| 2025-05-17 | `feature` | Enable VAqua for apple silicon | `mac.dist.gradle` | [8c58c5cf](https://github.com/freeplane/freeplane/commit/8c58c5cf2ecd42d6da3e8119cf6993a84a6202f7) |
| 2025-04-15 | `feature` | add info about plantuml-include.txt | `history_en.txt` | [7e272422](https://github.com/freeplane/freeplane/commit/7e27242246c77310d2ff9f7fdb6f4f0604260acc) |
| 2025-03-05 | `fix` | fix spelling | `RmiMatcher.java` | [423cb002](https://github.com/freeplane/freeplane/commit/423cb002bf5e3db2d077468042a39c211bc8316b) |
| 2025-03-04 | `fix` | Fix "delete violations" button | `ArchitectureViolationsPanel.java` | [7a29fe64](https://github.com/freeplane/freeplane/commit/7a29fe640d139a6b8ff8bf686234b71489b487d4) |
| 2025-01-24 | `fix` | try to fix showing preferences on mac startup | `MacChanges.java` | [d9688581](https://github.com/freeplane/freeplane/commit/d9688581c85ebecb096523887d1b9bdba59d441a) |

### Dettagli commit con note

**[bc81f155](https://github.com/freeplane/freeplane/commit/bc81f155f65d92d7a6be34dc7ccedcfbe2e7e6c0)** (2025-08-24) — Add AGENTS.md documentation

> Documents agent usage and collaboration patterns for development work.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[7dc022e4](https://github.com/freeplane/freeplane/commit/7dc022e435a9a6d3457d9a59db00e7c67539838e)** (2025-08-22) — Add SourceForge default download configuration

> - Set macOS default: Freeplane-apple.dmg
> - Set Windows default: Freeplane-Setup.exe
> - Set Linux/Others default: freeplane_bin.zip
> - Uses SourceForge Release API after upload
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[d80f0bf5](https://github.com/freeplane/freeplane/commit/d80f0bf5ae781247d19069820736d3fe86460245)** (2025-08-22) — Add GitHub Action to publish releases to SourceForge

> - Supports automatic publishing on release
> - Manual trigger with release tag selection
> - Dry run mode for testing
> - Uploads to both stable and archive directories
> - Handles release- and v tag prefixes
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[bd7312d3](https://github.com/freeplane/freeplane/commit/bd7312d398bf1956b717e05cb7851cd9a107766d)** (2025-08-12) — Enhance GitHub release deployment with parallel uploads and tag push

> - Add git push --tags before creating release to ensure tag availability
> - Implement parallel asset uploading with dynamic pool of 2 concurrent uploads
> - Maintain upload order while maximizing throughput
> - Preserve resume capability and skip already-uploaded assets
> - Track success/failure status for each upload with proper error reporting
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[278dad15](https://github.com/freeplane/freeplane/commit/278dad155da9395443beab67fae1006fbcf7d44a)** (2025-08-10) — Add GitHub release deployment script

> Automates the process of creating and publishing GitHub releases
> with distribution assets from the DIST directory. Features include:
> 
> - Automatic version detection from distribution files
> - Support for pre-releases (pre, alpha, beta, rc suffixes)
> - Incremental asset upload with resume capability
> - Release notes extraction from history files
> - Draft creation before publishing for safety
> - Validation of GitHub CLI authentication
> 
> The script uploads all standard distribution formats:
> - Windows installers (standard and touchscreen)
> - macOS disk images (Apple Silicon and Intel)
> - Portable Windows application
> - Debian package
> - Binary ZIP archive
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[ad629e70](https://github.com/freeplane/freeplane/commit/ad629e70ce90242029798480b8360b4cf1df7195)** (2025-08-10) — Fix archivePath deprecation in Gradle 9.0

> Replace binZip.archivePath with binZip.archiveFile.get().asFile
> for macOS distribution build task compatibility
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[f40e9448](https://github.com/freeplane/freeplane/commit/f40e944859406e35b10e503182e1a5d27338c2ee)** (2025-08-01) — Add .claude/ to gitignore

> Exclude Claude Code configuration directory from version control.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[3c049543](https://github.com/freeplane/freeplane/commit/3c049543d47da398ee9e5b0a08f625fff89b074c)** (2025-07-29) — Add mandatory validation for automated translation work

> Add validation requirements specifically for automated translation tools:
> - File integrity checks (ASCII text validation)
> - Broken Unicode escape pattern detection
> - Git diff validation before commits
> - Clear stop conditions for corruption patterns
> 
> Targets the actual source of Unicode corruption (automated tools)
> rather than adding overhead for manual translation work.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[b2124111](https://github.com/freeplane/freeplane/commit/b21241115b0b916de708dc64d3cb6cda8497d2b8)** (2025-07-29) — Fix directory structure documentation to reflect development reality

> Correct the project structure documentation to show the practical working view
> from git repository root, rather than trying to document variable system paths:
> 
> - Start from git root perspective (where Claude Code actually works)
> - Show the freeplane/ main subproject as seen during development
> - Use relative paths from git root for all file locations
> - Remove confusing absolute path references that vary between installations
> 
> The documentation now matches what developers actually see when working
> with the repository, making it much clearer and more useful.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[e9a1cfd1](https://github.com/freeplane/freeplane/commit/e9a1cfd1edacaa9c0bce773856b6f922d4248c12)** (2025-07-29) — Enforce mandatory native2ascii usage for translation files

> Add critical requirements to prevent Unicode corruption in Java properties files:
> - MANDATORY use of native2ascii tool for UTF-8 → Unicode escape conversion
> - Required workflow: UTF-8 temp file → native2ascii → merge to target file
> - Validation requirement: file command must show "ASCII text" output
> - Always run gradle format_translation after translation changes
> 
> Prevents systematic corruption patterns experienced 2025-07-28:
> - Double UTF-8 encoding causing garbled characters
> - Broken Unicode escapes with null byte injection
> - Binary data corruption breaking Weblate integration
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[c24e4863](https://github.com/freeplane/freeplane/commit/c24e48632fb6f44b11d06d46fb67f884843851d9)** (2025-07-28) — Document translation file encoding requirements in CLAUDE.md

> Add critical information about translation file encoding to prevent
> Unicode handling issues when adding translations to non-Latin scripts:
> 
> - Properties files use ISO-8859-1 encoding with Unicode escapes
> - Non-ASCII characters must be properly Unicode-escaped
> - Examples for Russian, Chinese, and Arabic translations
> - Tool requirements for proper Unicode escaping
> - Verification guidelines using existing translations
> 
> This documentation prevents translation corruption and ensures proper
> handling of international character sets in Freeplane translations.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[0cc1623e](https://github.com/freeplane/freeplane/commit/0cc1623ec0c3f043b184323ac392feb3b53e7e6c)** (2025-07-27) — Add comprehensive CLAUDE.md documentation to 1.12.x

> Copy complete CLAUDE.md from feature branch containing:
> - Build system commands and architecture overview
> - Development guidelines and code standards
> - Feature-Driven Testing Process (MANDATORY)
> - Translation system conventions
> - Mouse event handling patterns
> - Property management and migration patterns
> - OSGi bundle configuration
> - Testing framework setup
> - Logging system knowledge
> 
> This establishes development standards and AI collaboration patterns
> for the main branch, ensuring consistent development practices.
> 
> Key addition: Mandatory extract-test-integrate pattern for all feature work.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[c03b6bb8](https://github.com/freeplane/freeplane/commit/c03b6bb80e46fd40d9ebeb1d366a7c4d8b733dfc)** (2025-07-27) — Add mandatory Feature-Driven Testing Process to CLAUDE.md

> Establish extract-test-integrate pattern as the standard approach for all
> feature development. This ensures:
> 
> - Business logic is extracted from UI handlers into testable units
> - Features are built using tested, reliable components
> - Technical debt accumulates as byproduct of feature work, not separate sessions
> - Claude has explicit responsibility to enforce this pattern
> 
> CORE PRINCIPLE: Tests follow features, not vice versa.
> 
> This process will accelerate feature development through immediate feedback
> loops while building sustainable testing infrastructure.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>

**[f76ec90e](https://github.com/freeplane/freeplane/commit/f76ec90ebd71c94306ae55e6410c78f7850e8033)** (2025-07-27) — Add unused imports cleanup to CLAUDE.md code standards

> Document the practice of removing unused imports after coding changes
> to maintain clean and tidy code. This is especially important after
> refactoring operations that may leave behind unused import statements.
> 
> 🤖 Generated with [Claude Code](https://claude.ai/code)
> 
> Co-Authored-By: Claude <noreply@anthropic.com>


---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-11-27 | `fix` | fix folding and deleted locations | `ProjectNode.java` | [22de24f5](https://github.com/freeplane/freeplane/commit/22de24f5e7a421e0d1c48a9f4c0e3999482b54d6) |
| 2024-11-25 | `fix` | fix it | `ClassesNode.java`, `CodeMap.java` +6 | [5ca54c0e](https://github.com/freeplane/freeplane/commit/5ca54c0e02d1ed5328256a857e6c8ad9a6a475b9) |
| 2024-11-25 | `fix` | filter classes by selected dependencies from panel + bug fixes | `CodeDependenciesPanel.java`, `FilterClassesByDependencies.java` +1 | [c5441b27](https://github.com/freeplane/freeplane/commit/c5441b276f9fe6dc9d59869237379b47bdeae1da) |
| 2024-11-23 | `feature` | add new java options to windows distribution | `win.dist.gradle` | [70f0e9ac](https://github.com/freeplane/freeplane/commit/70f0e9acc86231560a2bca78726e847d93d8a0bc) |
| 2024-11-22 | `feature` | Add logging for RMi groups | `ParsedConfiguration.java`, `RmiMatcher.java` +1 | [973bae1e](https://github.com/freeplane/freeplane/commit/973bae1ef2dccc63f2abb1812e07610aaaecf9cb) |
| 2024-11-16 | `fix` | Fix fontconfig.properties of embedded java | `createJavaRuntimeImage.sh` | [09bcdb8c](https://github.com/freeplane/freeplane/commit/09bcdb8c004a76794e1d09a69fb58ba78b2ccca8) |
| 2024-11-14 | `fix` | fix mac signatures | `mac.dist.gradle` | [4bf066cd](https://github.com/freeplane/freeplane/commit/4bf066cde25752c3daba167d60bfd6172e07ecbf) |
| 2024-11-03 | `fix` | fix macos notarization for intel vaqua | `mac.dist.gradle` | [2da224b5](https://github.com/freeplane/freeplane/commit/2da224b5dd1a389f1489813d013805d68d1b093a) |
| 2024-11-03 | `fix` | fix macos notarization for intel | `mac.dist.gradle` | [93a12850](https://github.com/freeplane/freeplane/commit/93a12850d51bc64599f6f17ec9bd38afeac83a17) |
| 2024-11-03 | `fix` | fix macos notarization | `.gitignore`, `sign-jars-on-mac.sh` +1 | [3aebf23d](https://github.com/freeplane/freeplane/commit/3aebf23da311062daad66158e05a310b4a062fc2) |
| 2024-08-19 | `api_change` | Issue #1979 1.12.4 scripting API is in German | `build.gradle` | [cea44388](https://github.com/freeplane/freeplane/commit/cea443889a9337dc225dcb0560824ee0c0707e90) |
| 2024-08-16 | `feature` | Document new features in attached mind maps | `freeplaneUserGuide.mm`, `latestFreeplaneFeatures.mm` | [02c37073](https://github.com/freeplane/freeplane/commit/02c370738ece335d3025716af8028fe20b1cb432) |
| 2024-05-26 | `feature` | add info about clone and "minimized" marks improvements | `history_en.txt` | [2552e02d](https://github.com/freeplane/freeplane/commit/2552e02da6138feadd252528bea94c7dd9c95043) |
| 2024-05-25 | `feature` | add info about new feature (issue #1649) | `history_en.txt` | [160b9842](https://github.com/freeplane/freeplane/commit/160b98428ff5455784a4f5eccd0a46286dbefa44) |
| 2024-04-29 | `feature` | add version 1.11.13 to history | `history_en.txt` | [6e9b21a4](https://github.com/freeplane/freeplane/commit/6e9b21a44a5e6b8097d72d1c85fb723ece4d005a) |
| 2024-04-06 | `feature` | allow matching packages or single classes using new keyword in rules | `ClassNameMatcher.java`, `DirectoryMatcher.java` +2 | [d1fd2d1a](https://github.com/freeplane/freeplane/commit/d1fd2d1a36cd4168ee7c8ce5eaf35e883ee33027) |
| 2024-03-31 | `fix` | fix default gradle classes directories | `DirectoryMatcher.java` | [8ddf3484](https://github.com/freeplane/freeplane/commit/8ddf348458277412d84571200f2d9254289e6ed9) |
| 2024-03-24 | `feature` | Handle classes with names ending with $ in group matcher to support Scala | `DirectoryMatcher.java` | [72edea5c](https://github.com/freeplane/freeplane/commit/72edea5c197c670f23a8bb00d2385422debda5dc) |
| 2024-03-23 | `fix` | Fix annotations that were shown as interfaces. | `ClassNode.java` | [ae213846](https://github.com/freeplane/freeplane/commit/ae2138465f57bc321593eaee7098666ef034397e) |
| 2024-03-23 | `fix` | Fix regex | `IgnoredClassMatcher.java` | [e2ee2ea0](https://github.com/freeplane/freeplane/commit/e2ee2ea00749f21f206d958e8032a95c1c9334a2) |
| 2024-03-23 | `fix` | Fix regex | `IgnoredClassMatcher.java` | [76c2f0a1](https://github.com/freeplane/freeplane/commit/76c2f0a1fa45d4e24cee0c3383ade5ebda721a4a) |
| 2024-03-22 | `feature` | Support class names ending with $ | `CodeDependency.java`, `ClassNode.java` | [4b8e33bb](https://github.com/freeplane/freeplane/commit/4b8e33bb8a007cafa1536e579ee7352c17b30fa9) |
| 2024-03-17 | `fix` | Fix empty groups | `ProjectRootNode.java` | [6e55705b](https://github.com/freeplane/freeplane/commit/6e55705b941078aefb1fbfbcd15d2e600abfa0fa) |
| 2024-03-17 | `feature` | Add code explorer section | `freeplaneUserGuide.mm` | [53e6ae9b](https://github.com/freeplane/freeplane/commit/53e6ae9b33257c917cbfdf455177a005afc6b2cc) |
| 2024-03-10 | `feature` | Fix error for new configuration files | `CodeExplorerConfigurations.java` | [f7ee4378](https://github.com/freeplane/freeplane/commit/f7ee43783201d0710eca44e1c8b7f562ee117664) |
| 2024-03-10 | `feature` | Don't overwrite new code explorer configuration file if its path is changed | `CodeExplorerConfigurations.java` | [df951f2e](https://github.com/freeplane/freeplane/commit/df951f2e57d600ce52ae16385eff85f5ab1b708e) |
| 2024-03-10 | `feature` | Add group name parts to named groups | `ClassNameMatcher.java` | [4a682ab3](https://github.com/freeplane/freeplane/commit/4a682ab3b433f9c7d8cdd38231a0290056b262a3) |
| 2024-03-09 | `fix` | fix formatting | `ParsedConfiguration.java` | [5705dc64](https://github.com/freeplane/freeplane/commit/5705dc64565e1c9f9313933b5f4bbe10f0ce38d9) |
| 2024-03-09 | `fix` | fix test | `ParsedConfiguration.java` | [9b4467e0](https://github.com/freeplane/freeplane/commit/9b4467e07699e46d849cf5e7756f600e7873192b) |
| 2024-02-29 | `feature` | add link to freeplane-archunit-extension on GitHub | `history_en.txt`, `latestFreeplaneFeatures.mm` | [a7bd7abf](https://github.com/freeplane/freeplane/commit/a7bd7abf67182e260a31863b6ebd20f27f2ad185) |
| 2024-02-21 | `fix` | fix NPEs | `CodeMapPersistenceManager.java`, `UserDefinedCodeExplorerConfiguration.java` | [6455ef19](https://github.com/freeplane/freeplane/commit/6455ef19e186517deb3f040f95afbc31d48ea1de) |
| 2024-02-19 | `fix` | fix selected connectors if only one node is selected | `DependencySelection.java` | [9326ac7c](https://github.com/freeplane/freeplane/commit/9326ac7cbdbafbb629b51f4e4664e9b656ef7841) |
| 2024-02-16 | `fix` | fix selected connectors if ancestor nodes are selected | `DependencySelection.java` | [507a50e7](https://github.com/freeplane/freeplane/commit/507a50e73a687f26641c928fbf95af470a6fe25c) |
| 2024-02-15 | `feature` | Use new transfer object data structure | `ArchitectureViolationsConfiguration.java`, `ArchitectureViolationsPanel.java` | [506f0779](https://github.com/freeplane/freeplane/commit/506f077912160cc54891e1d972018daa250109fa) |
| 2024-02-13 | `fix` | Fix NPE | `CodeMapPersistenceManager.java` | [76c1d8f5](https://github.com/freeplane/freeplane/commit/76c1d8f5d5e2931ca86d33af96c5833cdfd95440) |
| 2024-02-10 | `feature` | Hide all attributes for new code maps by default | `CodeMapPersistenceManager.java` | [dcf16740](https://github.com/freeplane/freeplane/commit/dcf16740ab5c0423f367b858b64be6c1ab32ec46) |
| 2024-02-06 | `fix` | fix test | `CodeExplorerConfigurationsTest.java` | [e297e89b](https://github.com/freeplane/freeplane/commit/e297e89b5922d58e27863b455d921f3596d085ae) |
| 2024-02-05 | `fix` | Fix layout bug | `CodeExplorerConfigurator.java` | [c4ce9717](https://github.com/freeplane/freeplane/commit/c4ce9717ebdd442df5f7c7d17560e013eea125fb) |
| 2024-02-02 | `fix` | bug fix for duplicate top level classes with different inner classes | `ClassNode.java`, `ClassesNode.java` +2 | [05dbce6b](https://github.com/freeplane/freeplane/commit/05dbce6ba7abb3e913a8ee7f050035e7e322b499) |
| 2024-01-10 | `api_change` | Issue #1632 API is being generated in German | `build.gradle` | [70858b84](https://github.com/freeplane/freeplane/commit/70858b84b2d75c5f1a22307f4fe596380bd9f69d) |
| 2024-01-03 | `fix` | Fix dependency panel update after filter change | `CodeDependenciesPanel.java` | [1c44b2b0](https://github.com/freeplane/freeplane/commit/1c44b2b061b9d515c00a9e97c91756ec06590998) |

---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-12-26 | `fix` | fix task dependencies | `src.dist.gradle` | [13329dbc](https://github.com/freeplane/freeplane/commit/13329dbcba6a86edb4d1501a2829141a04f37039) |
| 2023-12-26 | `fix` | fix task dependencies | `src.dist.gradle` | [00f4062a](https://github.com/freeplane/freeplane/commit/00f4062abebcfe5bb5a1da6d8c5eac876c545ebc) |
| 2023-12-24 | `feature` | implement code explorer filter actions non showing ancestor nodes | `AncestorsHider.java`, `FilterCyclesAction.java` +2 | [ec93caa5](https://github.com/freeplane/freeplane/commit/ec93caa592d851446edebb9694ef7a0fb525c6eb) |
| 2023-12-24 | `fix` | fix case of no dependencies | `ShowDependingNodesAction.java` | [61cce37a](https://github.com/freeplane/freeplane/commit/61cce37a7417bf64d747fddd56ccf0ac3bd283a2) |
| 2023-12-22 | `fix` | fix list of last opened maps for code explorer mode | `CodeModeControllerFactory.java` | [5a4a18e3](https://github.com/freeplane/freeplane/commit/5a4a18e3c6e4f896289fffacf671fb9fc5be9de9) |
| 2023-12-15 | `fix` | fix import | `CodeDependenciesPanel.java` | [2b311601](https://github.com/freeplane/freeplane/commit/2b3116018f76a8470860171a34ab2f341def2e35) |
| 2023-12-12 | `fix` | fix NPE | `CodeLinkController.java` | [84e31cec](https://github.com/freeplane/freeplane/commit/84e31cec90e3cc74f3fd4720dcd3ec2ef9c4929e) |
| 2023-12-12 | `feature` | support separate search in "description" column | `CodeDependenciesPanel.java` | [6bca8489](https://github.com/freeplane/freeplane/commit/6bca848916878b5501cf3d6b9902944cab3db019) |
| 2023-12-11 | `feature` | add tool tips and improve filtering for dependencies | `CodeDependenciesPanel.java` | [b3e39736](https://github.com/freeplane/freeplane/commit/b3e397361d7351e3deab01839d4ad56755c2033c) |
| 2023-12-09 | `fix` | fix warnings | `CodeModeController.java`, `CodeProjectController.java` +5 | [781e6733](https://github.com/freeplane/freeplane/commit/781e673316a5c9167e85794751cc2a3e3bccf3b8) |
| 2023-12-04 | `fix` | fix: we need selected node for following operations | `CodeMapController.java` | [86941393](https://github.com/freeplane/freeplane/commit/869413931cecb7d00c6ee43fd503b1689e4c1a37) |
| 2023-12-03 | `feature` | fix new node condition | `PackageNode.java` | [38cf274d](https://github.com/freeplane/freeplane/commit/38cf274d27185fba73c6b7ec423569e264184e81) |
| 2023-12-03 | `fix` | fix package child node calculation | `PackageNode.java` | [21e2d7ab](https://github.com/freeplane/freeplane/commit/21e2d7abfb874b3fdc3423303413caf6af05e703) |
| 2023-12-02 | `fix` | fix "incoming and outgoing" direction | `ShowDependingNodesAction.java` | [0c741c5d](https://github.com/freeplane/freeplane/commit/0c741c5dcb2b64f9f58732de71bbff3d049f1742) |
| 2023-11-30 | `fix` | fix location table width | `CodeExplorerConfigurator.java` | [5344ca25](https://github.com/freeplane/freeplane/commit/5344ca2541a15d88c4d29ea769a0299fc3a7817c) |
| 2023-11-30 | `feature` | adapt to new API | `Activator.java` | [3a4a2d2d](https://github.com/freeplane/freeplane/commit/3a4a2d2d9e6283803201c622012fb995726046ac) |
| 2023-11-30 | `fix` | Fix configuration serialization using json | `build.gradle`, `CodeExplorerConfigurations.java` +2 | [38a334d1](https://github.com/freeplane/freeplane/commit/38a334d129769323dd88a81f9d2c44fda2f7ad78) |
| 2023-11-28 | `fix` | fix counting child nodes of package node | `PackageNodeModel.java` | [c30070ae](https://github.com/freeplane/freeplane/commit/c30070ae9313f4b137e74eed78e53a44752a34e5) |
| 2023-11-28 | `fix` | fix node names | `ClassesNodeModel.java`, `PackageNodeModel.java` | [b1705727](https://github.com/freeplane/freeplane/commit/b170572789359d4afa274f828cdd5be35e89e8a3) |
| 2023-11-26 | `feature` | support another minor version formats in gradle build | `build.gradle`, `dist.gradle` | [7f2b082b](https://github.com/freeplane/freeplane/commit/7f2b082bc915b36899c4c593904ef3d772f5bed2) |
| 2023-11-26 | `fix` | Use correct connector types | `GraphCycleFinder.java`, `GraphNodeSort.java` | [d5fec5eb](https://github.com/freeplane/freeplane/commit/d5fec5eb4fd0c7fc363e715cb783fb9f4f8cfea0) |
| 2023-11-25 | `fix` | fix classes node sort | `ClassesNodeModel.java` | [b4d840bd](https://github.com/freeplane/freeplane/commit/b4d840bdafcb1d1ce5c1adafb7da1b26d41280b1) |
| 2023-11-25 | `fix` | fix package node sort | `PackageNodeModel.java` | [b27111b0](https://github.com/freeplane/freeplane/commit/b27111b02aedf304ad7b4a832c7661c068f94a01) |
| 2023-11-07 | `feature` | add ArchUnit as runtime dependency | `build.gradle` | [42680e1f](https://github.com/freeplane/freeplane/commit/42680e1fdbce0066ea0b6814bea4e6056ed91fdc) |
| 2023-10-27 | `feature` | sign with new certificate | `kitfox-svg-salamander-1.1.1-p1.jar` | [3d12ada0](https://github.com/freeplane/freeplane/commit/3d12ada072f2c3f8f716afe90dcacf2882e7de5a) |
| 2023-08-19 | `fix` | Update shtml to fix html paste issues | `build.gradle` | [f44737e6](https://github.com/freeplane/freeplane/commit/f44737e65ec94d7543059211e6c1bdcfb243b9cc) |
| 2023-08-12 | `feature` | Update shtml | `build.gradle` | [a95f0b3a](https://github.com/freeplane/freeplane/commit/a95f0b3af2208334d7e5719b218573e49ce1c14f) |
| 2023-05-15 | `feature` | add a link to the detailed changelog | `latestFreeplaneFeatures.mm` | [f4690665](https://github.com/freeplane/freeplane/commit/f4690665e461f3ab58c4477dd5524d91522f9f1f) |
| 2023-01-20 | `fix` | try to fix eol format in freeplane.desktop | `.gitattributes` | [f7600140](https://github.com/freeplane/freeplane/commit/f760014096b6240b8169fbcb8dfb7fe10e8be5b7) |
| 2023-01-15 | `fix` | Issue  #935 Note editor: Font size is fixed after changing the fontssize | `build.gradle` | [3c3140be](https://github.com/freeplane/freeplane/commit/3c3140be406c1f1ed6cea1c3f689be09743afe36) |

### Dettagli commit con note

**[a95f0b3a](https://github.com/freeplane/freeplane/commit/a95f0b3af2208334d7e5719b218573e49ce1c14f)** (2023-08-12) — Update shtml

> Issue #1331 FP 1.11.5: Editing node details of FP 1.11.4 mindmap results in illegible details
> Issue #1325 New highlighters: remove highlighter is not working after closing the inline editor

**[f7600140](https://github.com/freeplane/freeplane/commit/f760014096b6240b8169fbcb8dfb7fe10e8be5b7)** (2023-01-20) — try to fix eol format in freeplane.desktop

> Issue #929 [freeplane.desktop] Wront EOL format on some lines

**[3c3140be](https://github.com/freeplane/freeplane/commit/3c3140be406c1f1ed6cea1c3f689be09743afe36)** (2023-01-15) — Issue  #935 Note editor: Font size is fixed after changing the fontssize

> (but I do not understand the reason for the bug)


---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-11-23 | `feature` | Create initial CI configuration with GitHub Actions | `ci.yml` | [0cb09d81](https://github.com/freeplane/freeplane/commit/0cb09d811be5821263b5f6da17afede6d478bb47) |
| 2022-10-31 | `feature` | sign using new certificate | `kitfox-svg-salamander-1.1.1-p1.jar` | [52872dd9](https://github.com/freeplane/freeplane/commit/52872dd9dd89e4fd35e429940ace1ebfa6367edf) |
| 2022-09-17 | `feature` | add gradle task for notarytool | `mac.dist.gradle`, `macapp.example.properties` | [cdd5560c](https://github.com/freeplane/freeplane/commit/cdd5560cec2e8b19715a72d41a9257aafe8a9202) |
| 2022-09-17 | `fix` | fix mac dist, prepare app for notarization | `mac.dist.gradle` | [9d57bdbb](https://github.com/freeplane/freeplane/commit/9d57bdbb46ab3bfdb58c32357bcd93999058e9f5) |
| 2022-09-11 | `feature` | Add separator lines | `README.md` | [e960d896](https://github.com/freeplane/freeplane/commit/e960d896b8792cbea7256897adff0849e2aff50f) |
| 2022-09-10 | `fix` | Update README.md | `README.md` | [8e13fc28](https://github.com/freeplane/freeplane/commit/8e13fc28a1064a9e49747c99b8088ed70e14097b) |
| 2022-09-06 | `feature` | add hints to configuration example | `macapp.example.properties` | [5c84c57d](https://github.com/freeplane/freeplane/commit/5c84c57d1def189975b425c79eeee06cb917f2d8) |
| 2022-05-26 | `fix` | fix vaqua dependencies | `build.gradle` | [fe0a3a35](https://github.com/freeplane/freeplane/commit/fe0a3a357b7a93a4d67947e8114c3f29bf6a9c99) |
| 2022-05-26 | `feature` | Update README.md | `README.md` | [37bb77eb](https://github.com/freeplane/freeplane/commit/37bb77ebc90078c8862dd6f81614f9812092a32d) |
| 2022-03-27 | `fix` | fix gradle build | `win.dist.gradle` | [d66742dc](https://github.com/freeplane/freeplane/commit/d66742dccab2a907dfe19c59e45306486571ba71) |
| 2022-03-25 | `fix` | fix mac build | `build.gradle` | [9d3c20e2](https://github.com/freeplane/freeplane/commit/9d3c20e26cc7efa1ce0572d27a773a744165a2e4) |
| 2022-01-27 | `feature` | feat: add support for reproducible builds | `build.gradle` | [d27bab4d](https://github.com/freeplane/freeplane/commit/d27bab4d8d5fc4cbcbd22d9d476ca75970cc5c9a) |
| 2022-01-03 | `feature` | Add StartupWMClass key to desktop file to avoid a separate running application icon | `freeplane.desktop` | [efce53ad](https://github.com/freeplane/freeplane/commit/efce53adb372e43479895fd786fb8206d9f19772) |

### Dettagli commit con note

**[0cb09d81](https://github.com/freeplane/freeplane/commit/0cb09d811be5821263b5f6da17afede6d478bb47)** (2022-11-23) — Create initial CI configuration with GitHub Actions

> Create an initial CI configuration with GitHub Actions. It builds and checks Freeplane, currently on Java 17 and 18 on Ubuntu.
> 
> It runs on each push and pull request, when manually triggered and once a week on the default branch.
> 
> It's based on the current Travis CI configuration: https://github.com/freeplane/freeplane/blob/1.10.x/.travis.yml

**[8e13fc28](https://github.com/freeplane/freeplane/commit/8e13fc28a1064a9e49747c99b8088ed70e14097b)** (2022-09-10) — Update README.md

> fix link to freeplane main site

**[37bb77eb](https://github.com/freeplane/freeplane/commit/37bb77ebc90078c8862dd6f81614f9812092a32d)** (2022-05-26) — Update README.md

> updated the outdated links and info. added the new features screenshots

**[d27bab4d](https://github.com/freeplane/freeplane/commit/d27bab4d8d5fc4cbcbd22d9d476ca75970cc5c9a)** (2022-01-27) — feat: add support for reproducible builds

> As per gradle [docs] add support to remove timestamps and package with same order which is required from [reproducible] builds
> 
> [docs]: https://docs.gradle.org/current/userguide/working_with_files.html#sec:archives
> [reproducible]: https://reproducible-builds.org/
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>


---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-07-17 | `api_change` | #2976 Freeplane API documentation is not accesible on portable apps | `win.dist.gradle` | [f87b691e](https://github.com/freeplane/freeplane/commit/f87b691eb0f4372f3bb6349bd3d735bd5c1aa71c) |
| 2021-06-29 | `fix` | Use try-with-resources, StandardCharsets and fix deprecated API | `TaskUtils.java` | [66dca3db](https://github.com/freeplane/freeplane/commit/66dca3db93eda55b18a88f2aaf5043147b8e157a) |
| 2021-04-16 | `feature` | add exports to non public API used by darcula | `mac.dist.gradle` | [d30d14fa](https://github.com/freeplane/freeplane/commit/d30d14faa4a2b5eefae264706a78a01cf896ad32) |
| 2021-03-07 | `fix` | fix mac changes | `MacChanges.java` | [78fcc544](https://github.com/freeplane/freeplane/commit/78fcc5444098aee91002dce354cc9589bc34dce9) |

### Dettagli commit con note

**[66dca3db](https://github.com/freeplane/freeplane/commit/66dca3db93eda55b18a88f2aaf5043147b8e157a)** (2021-06-29) — Use try-with-resources, StandardCharsets and fix deprecated API

> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>


---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-04 | `fix` | fix test library dependency | `build.gradle` | [8cce354f](https://github.com/freeplane/freeplane/commit/8cce354fcc10c1bbbdcf63a30a983cc633ed05de) |
| 2020-10-04 | `fix` | fix signjar.gradle | `signjar.gradle` | [6f772896](https://github.com/freeplane/freeplane/commit/6f772896f3e4c97d819e23b88121c440eb0b605b) |
| 2020-03-14 | `feature` | add dependency https://github.com/haraldk/TwelveMonkeys#jpeg | `build.gradle` | [4f411362](https://github.com/freeplane/freeplane/commit/4f4113625dceef3d9cbb48ebfd30758d24df351c) |
| 2020-03-13 | `fix` | fix debian gradle task | `linux-packages.gradle` | [98d82281](https://github.com/freeplane/freeplane/commit/98d8228156f5ce6a007f1c5dd836ef77059ab209) |
| 2020-02-28 | `fix` | fix encoding | `emoji.gradle` | [41211b40](https://github.com/freeplane/freeplane/commit/41211b40444698a593705976b24244f11c65b1d2) |
| 2020-02-23 | `fix` | fix source archive file names in distributions | `src.dist.gradle` | [48f94699](https://github.com/freeplane/freeplane/commit/48f94699dbce0dd1ee7a7cace5624e1e76d7feed) |
| 2020-02-23 | `feature` | fix build to support java 11 for freeplane_mac | `build.gradle` | [2e70513b](https://github.com/freeplane/freeplane/commit/2e70513b671abe4bc30ff88d7fdac089f0ecbf3b) |
| 2020-01-31 | `fix` | Fix Central 501 HTTPS Required when fetching maven dependencies (#150) | `build.gradle` | [bfef621d](https://github.com/freeplane/freeplane/commit/bfef621dd907786adef0740daddb31b86fa17de3) |
| 2020-01-25 | `fix` | fix build | `build.gradle` | [e33f76a3](https://github.com/freeplane/freeplane/commit/e33f76a3c12cb0b5463f265dd556085042a98c83) |
| 2020-01-25 | `fix` | fix build | `build.gradle`, `emoji.gradle` | [286798e6](https://github.com/freeplane/freeplane/commit/286798e65f8585a68007439c7bf389ea4b7ba12a) |
| 2020-01-25 | `fix` | fix build | `build.gradle`, `emoji.gradle` | [d974c1f4](https://github.com/freeplane/freeplane/commit/d974c1f421ecb77bf0ca9689f08007390dd68ec6) |
| 2020-01-03 | `fix` | fix comment | `build.gradle` | [3412d396](https://github.com/freeplane/freeplane/commit/3412d3969da313d78b4fe6c456fa56158813055c) |

### Dettagli commit con note

**[bfef621d](https://github.com/freeplane/freeplane/commit/bfef621dd907786adef0740daddb31b86fa17de3)** (2020-01-31) — Fix Central 501 HTTPS Required when fetching maven dependencies (#150)

> Effective January 15, 2020, The Central Repository no longer supports insecure communication over plain HTTP and requires that all requests to the repository are encrypted over HTTPS, see https://www.alphabot.com/security/blog/2020/java/Your-Java-builds-might-break-starting-January-13th.html
> 
> Signed-off-by: Leonidas Spyropoulos <artafinde@gmail.com>


---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-12-13 | `api_change` | include apple java api as jar file because maven repo is not available | `build.gradle`, `AppleJavaExtensions-1.5.4.jar` | [91421936](https://github.com/freeplane/freeplane/commit/91421936624922aef1d5bed362c32103e5719aa1) |
| 2019-12-13 | `feature` | Add https://repository.jboss.org/maven2/ | `build.gradle` | [a97452aa](https://github.com/freeplane/freeplane/commit/a97452aad9475102ef18e9ccd8d75bb3e8c72a4f) |
| 2019-12-06 | `feature` | update nebula.ospackage gradle plugin (.deb support) in order to support gradle6 and fix a | `build.gradle` | [0aeb9d28](https://github.com/freeplane/freeplane/commit/0aeb9d288c3d02781bd391a100ed034e61a89ebc) |
| 2019-10-18 | `fix` | fix osgi manifests: id = bundle-symbolicname | `build.gradle` | [2772c0b4](https://github.com/freeplane/freeplane/commit/2772c0b4b68acc473f2c668f42023bd44f7ad92b) |
| 2019-10-12 | `fix` | fix osgi manifest creation with bnd | `build.gradle`, `build.gradle` | [81dc5749](https://github.com/freeplane/freeplane/commit/81dc5749e20bc71bfb42050ba612d67b544c5873) |
| 2019-10-11 | `feature` | [work in progress] use new bnd-gradle plugin | `build.gradle` | [8e68abf3](https://github.com/freeplane/freeplane/commit/8e68abf3c437f9bef885eeee01933ff1416f0f04) |
| 2019-09-15 | `fix` | fix build | `build.gradle`, `build.gradle` | [ef527fa9](https://github.com/freeplane/freeplane/commit/ef527fa966297ab422b408144447d42ea3bd22cd) |
| 2019-02-15 | `fix` | fix build | `build.gradle` | [6917ae8e](https://github.com/freeplane/freeplane/commit/6917ae8e4ece04906a84786c35861d25cf47bb0f) |
| 2019-02-09 | `fix` | fix NPE | `MacChanges.java` | [7d0dc771](https://github.com/freeplane/freeplane/commit/7d0dc7713fb99fe0d1741ab22c0b75e1b97ad3a4) |
| 2019-02-04 | `fix` | fix build for mac | `build.gradle` | [85d81dae](https://github.com/freeplane/freeplane/commit/85d81dae9223ae9eea1ef32fce29b80571bf6fa2) |
| 2019-01-15 | `fix` | try to fix gradle wrapper call on jdk11 | `.travis.yml` | [e002e2fa](https://github.com/freeplane/freeplane/commit/e002e2fad71221f4587c7bd3bb0d7fd4ce531bc7) |
| 2019-01-15 | `feature` | Add gradle wrapper configuration to travis and run build on openJDK 11 | `.gitignore`, `.travis.yml` +1 | [24364096](https://github.com/freeplane/freeplane/commit/24364096ec077322de69b0637c462aa97df1f38d) |
| 2019-01-08 | `fix` | fix mac build on JDK 8 and update freeplane_mac jar | `freeplane_mac-1.5.jar`, `freeplane_mac-1.7.4.jar` +1 | [cdb8a9a0](https://github.com/freeplane/freeplane/commit/cdb8a9a02afddf5f2aafd51456c434285db23172) |

### Dettagli commit con note

**[91421936](https://github.com/freeplane/freeplane/commit/91421936624922aef1d5bed362c32103e5719aa1)** (2019-12-13) — include apple java api as jar file because maven repo is not available

> (sources http://hg.openjdk.java.net/jdk8u/jdk8u/jdk/file/tip/src/macosx/classes/com/apple/eawt)


---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-10-25 | `feature` | update deb package gradle plugin in order to support gradle 5.x | `build.gradle` | [ca679781](https://github.com/freeplane/freeplane/commit/ca6797812f45aca082384d136d169837720e95a0) |
| 2018-10-06 | `feature` | add /out/ to gitignore | `.gitignore` | [1c24fb25](https://github.com/freeplane/freeplane/commit/1c24fb258c67c4945d2a0af735077cd4f49a2e90) |
| 2018-09-23 | `feature` | add maven-central() to project config | `build.gradle` | [7006134a](https://github.com/freeplane/freeplane/commit/7006134a4fad664fea9dea7338684406a122c020) |
| 2018-08-31 | `fix` | fix test config | `build.gradle` | [21c71523](https://github.com/freeplane/freeplane/commit/21c715233adb9b7fd11864661044cac40f4ffa98) |
| 2018-08-29 | `fix` | fix build | `build.gradle` | [c55382e5](https://github.com/freeplane/freeplane/commit/c55382e51e789a5024a39bf0d6eba7a66770a507) |
| 2018-08-29 | `fix` | fix build | `build.gradle` | [f2719ad2](https://github.com/freeplane/freeplane/commit/f2719ad2529a392dbe3128430e4873c04f60d066) |
| 2018-08-26 | `fix` | fix build if git is not available | `git.gradle` | [61b3bde9](https://github.com/freeplane/freeplane/commit/61b3bde979b4121ad17dcd706acb34c7e667630e) |
| 2018-08-26 | `fix` | fix format_translation | `format_translation.gradle` | [de06ee18](https://github.com/freeplane/freeplane/commit/de06ee18684d7860a7cd26a12d14e22bd7dc174a) |
| 2018-08-22 | `feature` | add resources to main | `build.gradle` | [6fd9e8eb](https://github.com/freeplane/freeplane/commit/6fd9e8eb3169a375946bf691186cb838707a1f88) |
| 2018-07-03 | `feature` | add check_translation task to travis config | `.travis.yml` | [0ea12167](https://github.com/freeplane/freeplane/commit/0ea12167970af92cffe796ea8a52b10a8ef53937) |
| 2018-01-07 | `fix` | Fix map popup in style editor | `stylemodemenu.xml` | [ddd22fa3](https://github.com/freeplane/freeplane/commit/ddd22fa3d2c041289ee612b1035d8d1c720f72e3) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-25 | `feature` | work around for new gradle bug if subproject name equals to root dir name | `build.gradle` | [d0b93286](https://github.com/freeplane/freeplane/commit/d0b9328692a2057d41377cad7d0912871e9488ff) |
| 2017-11-27 | `fix` | fix icon ref in docu | `freeplane.mm`, `freeplane_ja.mm` | [90b71240](https://github.com/freeplane/freeplane/commit/90b71240de09c32cc2988a30480502a5dc903b52) |
| 2017-11-01 | `feature` | Do not add line feed at the last line when source distribution is produced | `src.dist.gradle` | [1edc752e](https://github.com/freeplane/freeplane/commit/1edc752e1cde2034661a9cf860369e7157889126) |
| 2017-10-28 | `feature` | add missing properties to example file | `signjar-example.properties` | [220b7f7e](https://github.com/freeplane/freeplane/commit/220b7f7eebb446d2217af13c2f78dae5a3263a8e) |
| 2017-10-26 | `fix` | fix certificate chain | `kitfox-svg-salamander-1.1.1-p1.jar`, `signjar.gradle` | [bd4189e5](https://github.com/freeplane/freeplane/commit/bd4189e5dbe1788c292c6b6bc8c8499be96a3ae5) |
| 2017-10-25 | `feature` | use new certum certificate | `codesign-example.bat`, `kitfox-svg-salamander-1.1.1-p1.jar` +2 | [95389d8e](https://github.com/freeplane/freeplane/commit/95389d8ed0ef96ae8a2f48b5429c0ecff76d1d7f) |
| 2017-10-21 | `feature` | create mac distribution from zip distribution | `dist.gradle`, `mac.dist.gradle` | [01d4b95d](https://github.com/freeplane/freeplane/commit/01d4b95d2870125a1c02e27c9e0827767424c553) |
| 2017-10-13 | `fix` | fix travis link in readme | `README.md` | [13eb7cc4](https://github.com/freeplane/freeplane/commit/13eb7cc41df2c369b91fd0c31e98ae70497528f6) |
| 2017-10-13 | `fix` | fix travis link in readme | `README.md` | [20215990](https://github.com/freeplane/freeplane/commit/20215990b937e41c575f9fb054b1f37df6161437) |
| 2017-10-07 | `feature` | Add buzan map template (thanks to Predrag Cuklin) | `BuzanMap.mm` | [3a1c7d08](https://github.com/freeplane/freeplane/commit/3a1c7d08a2c763239500966cf3b691f884cdd4bc) |
| 2017-09-30 | `fix` | Fix NPE for mac actions | `MacChanges.java` | [09e80814](https://github.com/freeplane/freeplane/commit/09e8081446f0a71a083f0d085aff133437d96f5c) |
| 2017-08-25 | `feature` | deb task: make sure that real Debian packages take precedence (better security support) | `linux-packages.gradle` | [5d18aab6](https://github.com/freeplane/freeplane/commit/5d18aab693eddc0dde3f268153637777ad46f3b8) |
| 2017-08-21 | `feature` | add mime-type info and desktop file for .deb | `freeplane.desktop`, `freeplane.mime` +2 | [81d5e051](https://github.com/freeplane/freeplane/commit/81d5e051ff5d2eaeb9b559fb5a2ca655ff3c4936) |
| 2017-06-24 | `feature` | New freeplaneTutorial.mm | `freeplaneTutorial.mm` | [c842708c](https://github.com/freeplane/freeplane/commit/c842708cdbb28c5bdea4c02c938af04a7b0a2bad) |
| 2017-05-07 | `feature` | add all BUILD* directories to gitignore | `.gitignore` | [6b08c60b](https://github.com/freeplane/freeplane/commit/6b08c60b700bfb6b69471d72ca9d5c60ce52a666) |
| 2017-05-07 | `feature` | add all BUILD* directories to gitignore | `.gitignore` | [856d113e](https://github.com/freeplane/freeplane/commit/856d113ee1007d8a509726e9984e6e03b44e6d4f) |
| 2017-04-30 | `fix` | fix action text | `Resources_en.properties` | [4bf537bf](https://github.com/freeplane/freeplane/commit/4bf537bf73346d77b66ec76719028791537a300e) |
| 2017-04-29 | `feature` | Menu actions for new view settings | `filemodemenu.xml`, `mindmapmodemenu.xml` +1 | [0cbfad4e](https://github.com/freeplane/freeplane/commit/0cbfad4ec2e2f0a11e249b029283faef58d9b876) |
| 2017-04-22 | `fix` | Fix icon | `showAttributes.svg` | [6c72dc1c](https://github.com/freeplane/freeplane/commit/6c72dc1c87a52377d00875d3c9762bc152237a21) |
| 2017-03-26 | `feature` | new mind map icons | `mindmap.png`, `mindmap.svg` | [abeceb8f](https://github.com/freeplane/freeplane/commit/abeceb8f51ebd78cac454cde84640df56e50aac4) |
| 2017-02-05 | `fix` | fix build | `git.gradle` | [5245ee4a](https://github.com/freeplane/freeplane/commit/5245ee4aa963941821583cf93a4560af1222cdfe) |
| 2017-01-22 | `fix` | fix icon toolbar | `freeplane.properties` | [87531a6c](https://github.com/freeplane/freeplane/commit/87531a6c3d18ec8c81bb08250ac9be9cfad4018e) |
| 2017-01-22 | `fix` | Fix update translation task | `format_translation.gradle`, `Resources_en.properties` | [57481f53](https://github.com/freeplane/freeplane/commit/57481f5307905f42ac99e9a914eed8e1e3025de0) |
| 2017-01-22 | `feature` | Add slide tool tips again | `Resources_en.properties` | [6c14d6bf](https://github.com/freeplane/freeplane/commit/6c14d6bf4f46e39c1fb43c21d795cb224b70997c) |
| 2017-01-21 | `feature` | add new tool tips to presentation panel | `format_translation.gradle`, `Resources_en.properties` | [fe0f314e](https://github.com/freeplane/freeplane/commit/fe0f314e5cfba06eba238a9b0e2f149367fab40a) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-12-31 | `feature` | add default value for menuItemFontSize | `freeplane.properties` | [2ab2c8dd](https://github.com/freeplane/freeplane/commit/2ab2c8dd989df458f1213ed6df75a2ea505b6340) |
| 2016-12-29 | `feature` | add missing highlight_matching_nodes.svg | `highlight_matching_nodes.svg` | [122d1f38](https://github.com/freeplane/freeplane/commit/122d1f3850fe1ca8ff18b9e3e9ab8fe3d08db9ec) |
| 2016-12-29 | `feature` | add more navigate svgs | `fold_one_level.svg`, `unfold_one_level.svg` | [ed7e0ed4](https://github.com/freeplane/freeplane/commit/ed7e0ed4fab1807ca68cf333e820dd9286723f5e) |
| 2016-12-29 | `feature` | add filter svgs | `applies_to_filtered_nodes.svg`, `apply_quick_filter.svg` +10 | [453183f3](https://github.com/freeplane/freeplane/commit/453183f3740daa4fb3b48b4f7ae3a8c40dc1d650) |
| 2016-12-03 | `fix` | fix compilation with Java7 | `build.gradle` | [b888afae](https://github.com/freeplane/freeplane/commit/b888afaed33eec49ff7c304e50d0f46412166bab) |
| 2016-11-26 | `fix` | Fix applet menu | `appletmenu.xml` | [59c53e9d](https://github.com/freeplane/freeplane/commit/59c53e9d38a4dabef2299d1237a5f46fde09c9f1) |
| 2016-11-26 | `fix` | Fix applet menu | `appletmenu.xml` | [2216ca75](https://github.com/freeplane/freeplane/commit/2216ca753f1463694fc2b6b705c0e37333140c35) |
| 2016-11-20 | `fix` | fix .gitignore | `.gitignore` | [c9bb562e](https://github.com/freeplane/freeplane/commit/c9bb562e5fba2c440a27c6e22d5810a3538acffd) |
| 2016-11-19 | `fix` | Fix help menu in applet | `appletmenu.xml` | [ab5c5dd4](https://github.com/freeplane/freeplane/commit/ab5c5dd4722f388417b862cf095fbdb0109b13cc) |
| 2016-11-16 | `feature` | add missing text | `Resources_en.properties` | [8112d081](https://github.com/freeplane/freeplane/commit/8112d0813c46db5a64ea9b54379c447ca86fbe9a) |
| 2016-11-15 | `feature` | Add introduction statement to tutorial | `freeplaneTutorial.mm` | [cc02fabe](https://github.com/freeplane/freeplane/commit/cc02fabe2f4e410c5ae837576b3f941150cc58b1) |
| 2016-10-25 | `feature` | Add default accelerators to slide actions | `mindmapmodemenu.xml` | [dbd1fa07](https://github.com/freeplane/freeplane/commit/dbd1fa0729abe5fd36ffd5b5a01cc12d74b4d39e) |
| 2016-10-23 | `fix` | fix translation | `Resources_en.properties` | [63607a43](https://github.com/freeplane/freeplane/commit/63607a4332ed29d2ba23390b7fb6bf792869fb1e) |
| 2016-09-29 | `fix` | Fix neverShowSurvey property name | `preferences.xml`, `Resources_en.properties` | [70cba1ab](https://github.com/freeplane/freeplane/commit/70cba1abff761c454b4e683218467c812e1ba72f) |
| 2016-09-04 | `feature` | take new translations from 1.6.x so that they can be translated right now | `Resources_en.properties` | [8878fef7](https://github.com/freeplane/freeplane/commit/8878fef7b37e78115fa402669d2b9d020db924eb) |
| 2016-08-29 | `fix` | fix #2390 Node detail duplicated in doc export for nodes with a note | `mm2wordml_utf8.xsl` | [7be62b29](https://github.com/freeplane/freeplane/commit/7be62b29d5b96b8ec1e6dd5c7d9d01998c5786d0) |
| 2016-08-03 | `feature` | add SVG icons from Predrag Cuklin | `0%.svg`, `100%.svg` +101 | [8299563b](https://github.com/freeplane/freeplane/commit/8299563bbf08d6b2fa28ec5be94cb8127dba5995) |
| 2016-07-17 | `feature` | Add translation strings for option panel lookandfeel.scaleuifonts | `Resources_en.properties` | [f855d07a](https://github.com/freeplane/freeplane/commit/f855d07af7d7bddc66ddb0f0d75b40f6e98a8cb1) |
| 2016-06-19 | `feature` | remove background image from whats new map | `Freeplane_splash_ alpha50.png`, `whatsNew-1.5.x.mm` +1 | [941eec3b](https://github.com/freeplane/freeplane/commit/941eec3bacad66e97aafd9b0efdd4e8c6c68ee04) |
| 2016-05-21 | `feature` | Update what's new map | `Freeplane_splash_ alpha50.png`, `whatsNew-1.5.x.mm` +1 | [5f30c362](https://github.com/freeplane/freeplane/commit/5f30c36206ca122125b8425057f2d083b1328d06) |
| 2016-05-16 | `feature` | What's new action added to menu | `mindmapmodemenu.xml` | [2496d8c6](https://github.com/freeplane/freeplane/commit/2496d8c63de1980b6701e89450518348a427461a) |
| 2016-05-06 | `fix` | Fix encoding of tests | `build.gradle` | [603af9f4](https://github.com/freeplane/freeplane/commit/603af9f4479f62baac9da35f1dfe4c3c5fd9e794) |
| 2016-05-05 | `fix` | Fix format translation tests | `FormatTranslationTest.java` | [83551795](https://github.com/freeplane/freeplane/commit/835517952a65bc83c577e28f3aa2946ddb9096d2) |
| 2016-05-03 | `feature` | new task for updating translations from user translation resources UserResources_*.propert | `format_translation.gradle` | [7bff568b](https://github.com/freeplane/freeplane/commit/7bff568b197fc7104f26fcc9acb83cbc5b5eef03) |
| 2016-05-03 | `feature` | new task for updating translations from user translation resources UserResources_*.propert | `format_translation.gradle` | [2e3ee503](https://github.com/freeplane/freeplane/commit/2e3ee5039b705e138485ef413a53cf536a534c39) |
| 2016-05-03 | `feature` | format translation should support latin1 characters | `FormatTranslation.java`, `TaskUtils.java` | [1854f272](https://github.com/freeplane/freeplane/commit/1854f2727a1723ca13d9bb3b960767eee12b26d5) |
| 2016-05-03 | `feature` | format translation should support latin1 characters | `FormatTranslation.java`, `TaskUtils.java` | [9a8eb8cd](https://github.com/freeplane/freeplane/commit/9a8eb8cd23f9ba497bddadb8bff45eab46d4cd47) |
| 2016-04-26 | `fix` | Fix icons for find next / find previous actions | `freeplane.properties` | [7ba9c5ce](https://github.com/freeplane/freeplane/commit/7ba9c5ce4e6fd847d506cfa62e50e1c8ce1d82d8) |
| 2016-04-26 | `fix` | Fix icons for find next / find previous actions | `freeplane.properties` | [462bb186](https://github.com/freeplane/freeplane/commit/462bb186d23eb9e9f81c658c97547021e7d97fab) |
| 2016-03-18 | `fix` | Fix mnemonics for &Save and Save &All | `Resources_en.properties` | [2bb7ce42](https://github.com/freeplane/freeplane/commit/2bb7ce427b44131f62338fdccc8f5481066fbd0c) |
| 2016-03-06 | `fix` | Fix building of navigate to map actions | `browsemodemenu.xml`, `filemodemenu.xml` +1 | [05c41441](https://github.com/freeplane/freeplane/commit/05c41441027924dfaf211a685a45214480f52a2c) |
| 2016-02-13 | `fix` | Fix freeplane props | `freeplane.properties` | [9e5f030a](https://github.com/freeplane/freeplane/commit/9e5f030aa5cdf8e7fdccd0cb0faee8e47b8c3329) |
| 2016-02-13 | `fix` | fix preferences | `preferences.xml` | [a7ad4b8f](https://github.com/freeplane/freeplane/commit/a7ad4b8f418613db5e7c10fcf2761bd705c8d4c8) |
| 2016-02-01 | `fix` | Refactor dependency handling in gradle, another small fix | `build.gradle` | [4e97ab44](https://github.com/freeplane/freeplane/commit/4e97ab44f8563cd84de19aa6d1002b6d509aa921) |
| 2016-01-10 | `fix` | Fix .gitattributes: remove obsolete line | `.gitattributes` | [3f3aeaa7](https://github.com/freeplane/freeplane/commit/3f3aeaa7fe179c31e5dc39ca257c15a112fb820e) |
| 2016-01-10 | `fix` | fix MacChanges.java but delete freeplane_mac from build | `MacChanges.java`, `settings.gradle` | [2a9f2a7b](https://github.com/freeplane/freeplane/commit/2a9f2a7b6465ee2a8462519c7a9bf8bfd93361a0) |
| 2016-01-01 | `fix` | Fix standard.mm | `standard.mm` | [75a36071](https://github.com/freeplane/freeplane/commit/75a360710b668dc6cf90b0edb4dbedff5a5e6a1e) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-12-19 | `fix` | use simplyhtml 0.16.11 with correct displayed version | `SimplyHTML-0.16.11-sources.jar`, `SimplyHTML-0.16.11.jar` | [6aaa7b05](https://github.com/freeplane/freeplane/commit/6aaa7b05e9f85ba3d03a727e0000ee1ecda56d81) |
| 2015-12-04 | `feature` | consider minor version property and create git tag from gradle release task | `dist.gradle` | [bbcc0c0b](https://github.com/freeplane/freeplane/commit/bbcc0c0b1c8aa273bf89d72537499566b51e0d16) |
| 2015-11-28 | `feature` | Update template BigMap.mm to use new node shape concept | `BigMap.mm` | [ad08eb93](https://github.com/freeplane/freeplane/commit/ad08eb93e93803e7ddbf3f1b313ef2763cde624e) |
| 2015-11-28 | `feature` | Update template BigMap.mm to use new node shape concept | `BigMap.mm` | [a77dc26c](https://github.com/freeplane/freeplane/commit/a77dc26c784cc8f5b285c9353007421336fabdfc) |
| 2015-11-26 | `feature` | Add attribute style configuration to BigMap | `BigMap.mm` | [d2bb59a0](https://github.com/freeplane/freeplane/commit/d2bb59a03cf4c4146a01ce4bd1c17ad4d88cdb43) |
| 2015-11-26 | `feature` | Add attribute style configuration to BigMap | `BigMap.mm` | [cfd701b4](https://github.com/freeplane/freeplane/commit/cfd701b4f0983303a82b11e23f1367d596d2a4e1) |
| 2015-11-22 | `fix` | Fix template map inconsistencies | `BigMap.mm`, `standard.mm` | [6775b75e](https://github.com/freeplane/freeplane/commit/6775b75ea4f2c0ff312b144ffa229955e28ce463) |
| 2015-11-22 | `fix` | Fix template map inconsistencies | `BigMap.mm`, `standard.mm` | [02a54824](https://github.com/freeplane/freeplane/commit/02a54824cfcbdb12780793cfe47da8130e7dfae3) |
| 2015-11-20 | `feature` | Modify templates to use new node shapes # Conflicts: #	freeplane/external-resources/templa | `BigMap.mm`, `conceptMap.mm` +2 | [3f45a7ae](https://github.com/freeplane/freeplane/commit/3f45a7aeb6a9a5fcf84691a8191b398db84858d4) |
| 2015-11-20 | `feature` | Modify templates to use new node shapes | `BigMap.mm`, `conceptMap.mm` +2 | [3a3c4190](https://github.com/freeplane/freeplane/commit/3a3c419011f0a2d8630b0c618879304c4f9316fc) |
| 2015-11-19 | `fix` | fix html in text translation | `Resources_en.properties` | [40e3337b](https://github.com/freeplane/freeplane/commit/40e3337b298c1ee14be4382aa7a7b19aa2ecd671) |
| 2015-11-19 | `fix` | fix html in text translation | `Resources_en.properties` | [e1c277eb](https://github.com/freeplane/freeplane/commit/e1c277eb29e540f7e557129dad0c1feee546a50a) |
| 2015-11-17 | `feature` | add SimplyHTML-0.16.11 | `build.gradle`, `SimplyHTML-0.16.09.jar` +2 | [e4f054d4](https://github.com/freeplane/freeplane/commit/e4f054d411fffec863646dc9ed0a21e26f8b8cbc) |
| 2015-11-16 | `feature` | New standard template by Jonas | `BigMap.mm` | [4e710147](https://github.com/freeplane/freeplane/commit/4e7101470413f8f0256feb4e1727db70b281b612) |
| 2015-11-04 | `feature` | new Columns.mm | `Columns.mm`, `columns.mm` +1 | [d9d565be](https://github.com/freeplane/freeplane/commit/d9d565be3974f10ea703e5ccea92fbc994e032c1) |
| 2015-11-04 | `feature` | new Columns.mm | `Columns.mm`, `columns.mm` +1 | [512c9200](https://github.com/freeplane/freeplane/commit/512c9200d63e865d97ae2d624003a684d52ed9f5) |
| 2015-11-03 | `feature` | Add columns.mm and change standard properties # Conflicts: #	freeplane/viewer-resources/fr | `columns.mm`, `freeplane.properties` | [3df3e8a3](https://github.com/freeplane/freeplane/commit/3df3e8a3975a9d9b696c3584c4c67c34462f1e91) |
| 2015-11-03 | `feature` | Add columns.mm and change standard properties | `columns.mm`, `freeplane.properties` | [5b55735a](https://github.com/freeplane/freeplane/commit/5b55735ab950b077b2ae581250075e6a1dc1beb0) |
| 2015-10-29 | `feature` | Add missed text string | `Resources_en.properties` | [b64afc17](https://github.com/freeplane/freeplane/commit/b64afc1718613a6f52cf4c200e7e4efe51e22953) |
| 2015-10-29 | `feature` | Add missed text string | `Resources_en.properties` | [71aa5580](https://github.com/freeplane/freeplane/commit/71aa55808cdcc7cab3ac5b93b3565f641ee4e0d7) |
| 2015-10-29 | `feature` | Add missed text string | `Resources_en.properties` | [1c94d66e](https://github.com/freeplane/freeplane/commit/1c94d66e5bf19932aa7527fb421b63e47a9c7f44) |
| 2015-10-18 | `fix` | Fix menus # Conflicts: #	freeplane/viewer-resources/translations/Resources_en.properties | `Resources_en.properties` | [3c686278](https://github.com/freeplane/freeplane/commit/3c686278b9a2eea777c6d4928b61ae58f9bcbf97) |
| 2015-04-12 | `feature` | Add new packages to plug-in exports | `build.gradle` | [2e9c6af4](https://github.com/freeplane/freeplane/commit/2e9c6af4233a0ee08d14bb38f4f8bf3b87c7e3c0) |
| 2015-04-06 | `feature` | add gradle-build support for signing freeplaneviewer.jar | `build.gradle`, `signjar-example.properties` +1 | [d3d285ed](https://github.com/freeplane/freeplane/commit/d3d285edbfbc9932ff15bd5adecd268473b8599e) |
| 2015-03-28 | `feature` | Add test resource directories to gradle configuration | `build.gradle` | [6eb2a3df](https://github.com/freeplane/freeplane/commit/6eb2a3dfa2f9aa414770c97d82895afc91476e86) |
| 2015-03-28 | `feature` | Add test resource directories to gradle configuration | `build.gradle` | [b05c9e71](https://github.com/freeplane/freeplane/commit/b05c9e71e95210fb04f89d074c54568dad0ec508) |
| 2015-03-28 | `feature` | add compile dependencies, update flamingo to 7.3 | `build.gradle` | [3dd58546](https://github.com/freeplane/freeplane/commit/3dd585462d06cab8ed594d47526212fb00310f4f) |
| 2015-03-26 | `feature` | add DIST/ to .gitignore | `.gitignore` | [577252ae](https://github.com/freeplane/freeplane/commit/577252ae904749967cff8b645596b0e1f00f2fc9) |
| 2015-03-25 | `feature` | Add BUILD to .gitignore | `.gitignore` | [cafffd66](https://github.com/freeplane/freeplane/commit/cafffd66a5dffc12308302a64d8e33a9a0476349) |
| 2015-03-25 | `feature` | add apache.common.lang3 lib to classpath | `.classpath` | [9a3a78a2](https://github.com/freeplane/freeplane/commit/9a3a78a28dbd8033e051a1ac377a1ce280354e7e) |
| 2015-03-20 | `feature` | gradle: add gitinfo.txt/gitinfo.properties handling (also considering builds from outside  | `dist.gradle`, `build.gradle` +2 | [3eb73e8e](https://github.com/freeplane/freeplane/commit/3eb73e8e3b2c3969ccc7f830eeee6b474238a620) |
| 2015-03-19 | `feature` | add zip4mac and dmg4mac tasks | `dist.gradle`, `mac.dist.gradle` | [780f3d7f](https://github.com/freeplane/freeplane/commit/780f3d7f8c41307d4ea86cb614a4fa669b9146cf) |
| 2015-03-09 | `feature` | add runGit task which generates gitinfo.txt and gitinfo.properties | `dist.gradle` | [0c1159fc](https://github.com/freeplane/freeplane/commit/0c1159fc03cbf1156f4445ff8803a0a61ea3e703) |
| 2015-03-08 | `fix` | fix some problems in macosxapp task | `dist.gradle`, `mac.dist.gradle` | [1df105e4](https://github.com/freeplane/freeplane/commit/1df105e4419cae04e4397ca177ddab2c4bed2001) |
| 2015-03-08 | `feature` | add macosxapp task (untested) | `dist.gradle`, `mac.dist.gradle` | [4da1420a](https://github.com/freeplane/freeplane/commit/4da1420af6ed7e74991d6dfdf6141b6cfb8a8693) |
| 2015-03-08 | `fix` | better mm2html.xsl | `mm2html.xsl` | [d7265676](https://github.com/freeplane/freeplane/commit/d7265676fe6f734b03f07e52da789c337e598dd2) |
| 2015-03-07 | `fix` | fix windowsPortableInstaller gradle task | `dist.gradle` | [ca4ff706](https://github.com/freeplane/freeplane/commit/ca4ff70605f09000a3fee304f2b6d0980489ec5c) |
| 2015-03-07 | `api_change` | exclude doc/api from portable exe | `dist.gradle` | [f2518f4f](https://github.com/freeplane/freeplane/commit/f2518f4fab069aa72f002f1aaec227ee026752e3) |
| 2015-02-16 | `fix` | fix dist.gradle to handle the case ISCC.exe is not available | `dist.gradle` | [6c7d5f39](https://github.com/freeplane/freeplane/commit/6c7d5f39569ee01c0d4c4917b50b5deb5057a958) |
| 2015-02-16 | `feature` | create windowsInstaller task | `dist.gradle` | [daebed69](https://github.com/freeplane/freeplane/commit/daebed699159e77c5faa7b263554f1d49f16eefe) |
| 2015-02-14 | `feature` | add srcTarGz task which tars src and normalizes line endings for some text files (compile  | `dist.gradle` | [322313fb](https://github.com/freeplane/freeplane/commit/322313fbb390ea6a70001cd390e5245f5011c045) |
| 2015-02-07 | `feature` | create distZip target (freeplane_bin-<version>.zip) | `build.gradle`, `dist.gradle` +1 | [c0e506ca](https://github.com/freeplane/freeplane/commit/c0e506cad1897ad7818eb414d841c179a03e5666) |
| 2015-01-31 | `feature` | make source attachments work for local (git) deps, upgrade SimplyHTML to 0.16.09, add sour | `build.gradle`, `build.gradle` +4 | [fd37d500](https://github.com/freeplane/freeplane/commit/fd37d500cded6e36115fa89638e9186dbf98545b) |
| 2015-01-27 | `fix` | fix .gitignore for gradle (.project/.classpath/.settings) generated/copied | `.gitignore` | [97356fad](https://github.com/freeplane/freeplane/commit/97356fad6f35ab22f707c67646d132be20cd9bb8) |
| 2015-01-25 | `fix` | Fix maven repository for Gradle 2.2.1 (http://stackoverflow.com/questions/26675814/gradle- | `build.gradle` | [2d966747](https://github.com/freeplane/freeplane/commit/2d96674776a24ce752bdaccfae945e08e7f1ebc8) |
| 2015-01-16 | `fix` | fix filtered OSGi manifests for eclipse: unwrap, replace paths, wrap | `build.gradle` | [4664e216](https://github.com/freeplane/freeplane/commit/4664e216d96823d5b38ee22f551a5bd46e1182f6) |
| 2015-01-15 | `fix` | fix filtered OSGi manifests (normalize MANIFEST first) | `build.gradle` | [78f2737d](https://github.com/freeplane/freeplane/commit/78f2737d87eb162115ca2afb0a1bcb9e9bfe0dc0) |
| 2015-01-15 | `fix` | fix simplyhtml (pull gnu-regexp) | `build.gradle` | [2ece2eb7](https://github.com/freeplane/freeplane/commit/2ece2eb7469fae7891b99640b1d95db14e8cc20a) |
| 2015-01-15 | `feature` | create filtered OSGi MANIFEST.MFs for eclipse OSGi configuration | `build.gradle` | [81dfc5b4](https://github.com/freeplane/freeplane/commit/81dfc5b4642cc100bd7fb2901c261690e205b4e8) |
| 2015-01-13 | `feature` | remove 'ant create-plugin' + support files, made obsolute by gradle build | `README.txt`, `CreatePlugin.java` +2 | [9eee68d5](https://github.com/freeplane/freeplane/commit/9eee68d5ab51a3360c697ab3a01050233e8c7e5e) |
| 2015-01-11 | `fix` | java 1.7 compatibility fix | `ClonesTest.java` | [efde1dbb](https://github.com/freeplane/freeplane/commit/efde1dbb36c779f6917b6ae3161cdc1afde86a34) |
| 2015-01-11 | `fix` | java 1.7 compatibility fix | `JMenuBuilderTest.java`, `RecursiveMenuStructureBuilderForPaths.java` | [fbd276f2](https://github.com/freeplane/freeplane/commit/fbd276f2fcfdb3aeec7ff831298dcdcf7d3ec76d) |
| 2015-01-10 | `feature` | Use entry attribute map for all new helper attributes | `ActionFinderTest.java`, `Entry.java` | [4ec5270d](https://github.com/freeplane/freeplane/commit/4ec5270db9f6329b351000062d669b76c325ea4e) |
| 2015-01-09 | `feature` | freeplane_ant: enable tests and fix FormatTranslation[Test] | `build.gradle`, `FormatTranslation.java` +1 | [505af17a](https://github.com/freeplane/freeplane/commit/505af17ac508e954629626cee8c63bd96685aece) |
| 2015-01-08 | `feature` | implement format/check_translation for :freeplane | `build.gradle`, `build.gradle` +2 | [c408ac06](https://github.com/freeplane/freeplane/commit/c408ac067f145935cac2df809cfec33b12a5dd37) |

### Dettagli commit con note

**[d7265676](https://github.com/freeplane/freeplane/commit/d7265676fe6f734b03f07e52da789c337e598dd2)** (2015-03-08) — better mm2html.xsl

> fix indent
> output image


---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-10-14 | `feature` | add clean task for removing ./DIST | `build.gradle` | [a5395fb7](https://github.com/freeplane/freeplane/commit/a5395fb7be3eef128d3c3921b973034494979815) |
| 2014-10-12 | `feature` | add freeplaneosgi.jar, use includeEmptyDirs=false | `build.gradle` | [889cfc72](https://github.com/freeplane/freeplane/commit/889cfc728bc2008c62c7a4ea37fd117784e533d9) |
| 2014-10-12 | `feature` | add generic copy_plugin_jars task | `build.gradle` | [2d7c8735](https://github.com/freeplane/freeplane/commit/2d7c873542c1dfb4940868714cb72ea801b32a97) |
| 2014-10-12 | `feature` | add freeplaneeditor.jar and include freeplane{editor,viewer}.jar in jar target | `build.gradle` | [6e1a5efa](https://github.com/freeplane/freeplane/commit/6e1a5efa0ac51c96051685ca650b7265aa129b5d) |
| 2014-10-10 | `feature` | create (non-OSGi) manifest for freeplaneviewer.jar | `build.gradle` | [4650100b](https://github.com/freeplane/freeplane/commit/4650100b11b6cecf1559121fd9a254199b6d5986) |
| 2014-09-16 | `feature` | add Application-Library-Allowable-Codebase attribute to manifest | `build.xml` | [dbdd2c07](https://github.com/freeplane/freeplane/commit/dbdd2c0704c65ed89ee40f0001fad85f4b5aae5a) |
| 2014-08-03 | `feature` | add option -nosplash toeclipse  mac launcher | `freeplane-osgi-mac.launch` | [a2851e58](https://github.com/freeplane/freeplane/commit/a2851e58d19c2e05b4fd1ed6a4eac9561b2baea5) |
| 2014-07-17 | `feature` | add LaTeX beamer export filter, thanks to Igor Garcia Olaizola | `mm2latexbeamer_richcontent_1.3.x.xsl` | [14e124b2](https://github.com/freeplane/freeplane/commit/14e124b277ea72562acebd9387c6d700f36c73f2) |
| 2014-06-24 | `fix` | include Freeplane_LaTeX.mm in distribution, fix link in doc/freeplane.mm | `Freeplane_LaTeX.mm`, `freeplane.mm` | [e251b5c1](https://github.com/freeplane/freeplane/commit/e251b5c1d12dc3c2a6eb6b4aeae9b94dbc26fbfd) |
| 2014-06-23 | `fix` | fix links in README.md | `README.md` | [ba1d9cf7](https://github.com/freeplane/freeplane/commit/ba1d9cf7c5ad4e5bc5fd31d67dcb8500c032cafc) |
| 2014-06-05 | `fix` | Update mm2wordml_utf8.xsl | `mm2wordml_utf8.xsl` | [5ac64878](https://github.com/freeplane/freeplane/commit/5ac648781026a4c628c130a5215511c8eb6b5c3d) |
| 2014-05-27 | `feature` | Moved the help plugin to the new directory structure | `build.gradle`, `jhall.jar` +60 | [0e6fffc7](https://github.com/freeplane/freeplane/commit/0e6fffc754816c48853f54abb3047e66beebe1fa) |
| 2014-05-06 | `feature` | add missing menu / ribbons keys for Scripts to translation file | `Resources_en.properties` | [6c6dde91](https://github.com/freeplane/freeplane/commit/6c6dde916600cbed0bbee5a05ea37cc907d158e3) |
| 2014-04-26 | `feature` | new icons for clones | `clone.png`, `cloneroot.png` | [b846dc9b](https://github.com/freeplane/freeplane/commit/b846dc9b66fd47228390812c3b103a12166b3081) |
| 2014-04-13 | `fix` | fix generated release tag nomenclature | `build.xml` | [b411e98d](https://github.com/freeplane/freeplane/commit/b411e98d0c1e1f909c53c917c2cb806dde9efe83) |
| 2014-04-09 | `feature` | Moved tests to the new folder structure. Note that a test failure causes builds to fail. U | `build.gradle`, `junit.jar` +4 | [2b4d28f4](https://github.com/freeplane/freeplane/commit/2b4d28f497638ac7fefb7af32d68ab0505c9f780) |
| 2014-04-09 | `feature` | Started moving towards the new directory structure | `build.gradle`, `CreatePlugin.java` +5 | [cd9788ee](https://github.com/freeplane/freeplane/commit/cd9788ee02290d8e5116762953191b4610ac6b24) |
| 2014-04-08 | `fix` | Fixed a resource loading bug in freeplane ant | `build.gradle` | [2e9cc17f](https://github.com/freeplane/freeplane/commit/2e9cc17f55f6034f387689b42134c2c61252c422) |
| 2014-03-21 | `api_change` | Scripting API: node.style.numberingEnabled, node shifts, node.minimalDistanceBetweenChildr | `history_en.txt` | [0bb19ec3](https://github.com/freeplane/freeplane/commit/0bb19ec3d47282b12ba3c9cccfad4b023bc816ce) |
| 2014-03-21 | `api_change` | Scripting API: node.style.numberingEnabled, node shifts, node.minimalDistanceBetweenChildr | `history_en.txt` | [7a8eb2f3](https://github.com/freeplane/freeplane/commit/7a8eb2f30d7f7de88162933de9f64bacfa025772) |
| 2014-03-02 | `feature` | use new version of insubstantial for ribbons menu | `.classpath`, `MANIFEST.MF` +8 | [b298837f](https://github.com/freeplane/freeplane/commit/b298837fed655d8c62462cc5a3e65e3e40b46f61) |
| 2014-02-07 | `fix` | fix mac quit handler | `freeplanemac.jar`, `MacChanges.java` | [fe6ae6ea](https://github.com/freeplane/freeplane/commit/fe6ae6eaa748929ed8e883e0979f924c057759de) |
| 2014-02-07 | `fix` | fix NPE | `freeplanemac.jar`, `MacChanges.java` | [1bbcdf2d](https://github.com/freeplane/freeplane/commit/1bbcdf2dd03e516422390989c95ed7e263409633) |
| 2014-01-26 | `fix` | fix template activator | `Activator.java` | [d6170da5](https://github.com/freeplane/freeplane/commit/d6170da5b597bfa7fa492e34839a1927f614892f) |
| 2014-01-26 | `feature` | add ribbon filter translation | `Resources_en.properties` | [a191a2fc](https://github.com/freeplane/freeplane/commit/a191a2fc52c29dd903bad8efa12d883306c4ee7b) |

### Dettagli commit con note

**[5ac64878](https://github.com/freeplane/freeplane/commit/5ac648781026a4c628c130a5215511c8eb6b5c3d)** (2014-06-05) — Update mm2wordml_utf8.xsl

> fix #34 - fix export of Notes to Word


---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-12-25 | `fix` | fix some deprecation warnings in test code | `FreeplaneWindow.java`, `Node.java` +2 | [5c1b2238](https://github.com/freeplane/freeplane/commit/5c1b2238b489a13f07e4fe3078162d51d9af2394) |
| 2013-11-12 | `feature` | support time stamping in java applet certificate | `build.xml`, `signjar-example.properties` | [523ce8ac](https://github.com/freeplane/freeplane/commit/523ce8aceceaa946943d58985dee8f53d707637a) |
| 2013-11-02 | `feature` | add signjar-example.properties | `build.xml`, `signjar-example.properties` | [899d56f2](https://github.com/freeplane/freeplane/commit/899d56f2d614aa25b01766effd591f3e610e5009) |
| 2013-10-13 | `feature` | Create README.md | `README.md` | [387f66e7](https://github.com/freeplane/freeplane/commit/387f66e72ab4606ee8832fdafb6f1446c7743692) |
| 2013-09-18 | `feature` | add 'release' target which runs clean, dist, tag-release | `build.xml` | [c086ae22](https://github.com/freeplane/freeplane/commit/c086ae2288daa0e438bc0016909f09d1963973f6) |
| 2013-09-10 | `feature` | Add documentation for last change. | `export2oowriter.xsl` | [b96a78e8](https://github.com/freeplane/freeplane/commit/b96a78e8438b6d30e17e12d554a66f6802dc0133) |
| 2013-09-10 | `feature` | Export2odt: Make list-, details- and note-styles be kids of node-style. | `export2oowriter.styles.xsl`, `export2oowriter.xsl` | [11220b0b](https://github.com/freeplane/freeplane/commit/11220b0b772285f70c87d48f5f178a9dafa41e46) |
| 2013-08-11 | `feature` | Add "common LaTeX macros" to history_en.txt | `history_en.txt` | [25fcad12](https://github.com/freeplane/freeplane/commit/25fcad1285c78b106bb2ccc47a5d8414119da08a) |
| 2013-06-30 | `api_change` | scripting API for export was added too | `history_en.txt` | [10db3a56](https://github.com/freeplane/freeplane/commit/10db3a5650ef751a20a442da6aabcc5f4ee72bbb) |
| 2013-06-26 | `fix` | fix typo in html tag | `Resources_en.properties` | [bd8fddf6](https://github.com/freeplane/freeplane/commit/bd8fddf6d05f3fa531f50beb7e9540870be01dd9) |
| 2013-06-22 | `feature` | 2010: Unable to create new map | `WorkspaceNewMapAction.java` | [13e0d949](https://github.com/freeplane/freeplane/commit/13e0d949683eceadd5d779e65fb4811cb6e20ebf) |
| 2013-06-11 | `feature` | Add a template mindmap containing preferences- and menu-nodes. | `Menu_Prefs_Templates.mm` | [03e8bef5](https://github.com/freeplane/freeplane/commit/03e8bef566d0d48c06ec6d9f5a5f403579b4354d) |
| 2013-06-04 | `feature` | Add xml-files generated from mind-maps to .gitignore. | `.gitignore` | [72489a55](https://github.com/freeplane/freeplane/commit/72489a55bddba6d4b1add2da65a6bbd970d22f66) |
| 2013-06-04 | `fix` | Fix: xml-files generated from mind-maps are not cleaned. | `build.xml` | [8f262da9](https://github.com/freeplane/freeplane/commit/8f262da9f4b8bf56272ef9efaa5c635b959b1a66) |
| 2013-06-04 | `feature` | Add a Mindmap representing the current `appletMenu` structures. | `build.xml`, `appletMenu.mm` +1 | [54e8921a](https://github.com/freeplane/freeplane/commit/54e8921a53a298da62dc6b3fe277712b964b04d3) |
| 2013-06-03 | `fix` | Fix git-attributes for **/help/doc/JavaHelpSearch/OFFSETS. | `.gitattributes`, `.gitattributes` | [f3c8cd32](https://github.com/freeplane/freeplane/commit/f3c8cd321aba1902f6d80b48cb5c6984c3a3f7fe) |
| 2013-06-02 | `feature` | Add a style-sheet for generating `*menu.xml` from a Mindmap. | `mm2menu.xsl` | [05ce6e6e](https://github.com/freeplane/freeplane/commit/05ce6e6ebbb47831bcab207bff8156e23bfa2f38) |
| 2013-06-02 | `fix` | Fix a typo. | `mm2preferences.xsl` | [5aa338d6](https://github.com/freeplane/freeplane/commit/5aa338d62cdbb1560c342ce985bb3e14739433ae) |
| 2013-06-02 | `feature` | Add a style-sheet for generating `preferences.xml` from a Mindmap. | `mm2preferences.xsl` | [13c5936a](https://github.com/freeplane/freeplane/commit/13c5936a3def487deb816cdbad525bac91b8cd1a) |
| 2013-06-02 | `feature` | Create a helper-xslt for building a mind-map out of ´*menu*.xml`. | `menu2map.xsl` | [fd7bea31](https://github.com/freeplane/freeplane/commit/fd7bea3189fd7673fc9aa8d4ee847fc9189e44ee) |
| 2013-06-02 | `feature` | Create a helper-xslt for building a mind-map out of ´preferences.xml`. | `prefs2map.xsl` | [03b347c3](https://github.com/freeplane/freeplane/commit/03b347c34dbea09b915783fd42c84aca434e1197) |
| 2013-05-31 | `fix` | Fix typos. | `freeplane.mm` | [a609b534](https://github.com/freeplane/freeplane/commit/a609b53400bc254a7a4c7bf2b84a97e159f06b4c) |
| 2013-05-31 | `feature` | Add support for background-color in styles. | `mm2oowriter.styles.xsl` | [30efd232](https://github.com/freeplane/freeplane/commit/30efd23293d8d56c5705c40947f1efcf2ca7b80b) |
| 2013-05-31 | `fix` | Fix a typo. | `mm2oowriter.xsl` | [500d0f3a](https://github.com/freeplane/freeplane/commit/500d0f3ae855fa7feed87362445bbec0c4d392af) |
| 2013-05-31 | `feature` | Update documentation: add some remarks about rich-text nodes. | `mm2oowriter.xsl` | [3446d099](https://github.com/freeplane/freeplane/commit/3446d099cd711cb5a82747a0f779eb1624700add) |
| 2013-05-30 | `feature` | Add styles for marking errors in rich-text nodes. | `mm2oowriter.styles.xsl` | [bc51d073](https://github.com/freeplane/freeplane/commit/bc51d073adce9bb57d815122ec41afa5e97b0eea) |
| 2013-05-30 | `feature` | Add support for nested lists in rich-nodes. | `mm2oowriter.xsl` | [f43d7970](https://github.com/freeplane/freeplane/commit/f43d7970de11ef47f05d30998f86454b112254e9) |
| 2013-05-30 | `fix` | Fix: Additional, empty paragraphs after lists in rich-tect nodes. | `mm2oowriter.xsl` | [383a2a3c](https://github.com/freeplane/freeplane/commit/383a2a3c2ac48522af47c3d1562ed70f68078de1) |
| 2013-05-30 | `feature` | Add documentation to the odt-style-sheet. | `mm2oowriter.xsl` | [ab055833](https://github.com/freeplane/freeplane/commit/ab055833725d6c7b260f3a50e0d77c73f5ade992) |
| 2013-05-30 | `feature` | Fix: style `Numbering Symbols` was missing. | `mm2oowriter.styles.xsl` | [aac85671](https://github.com/freeplane/freeplane/commit/aac85671d2ea23bb0a15e0c304cf09b31e22a34b) |
| 2013-05-30 | `feature` | Add support for auto-numbering nodes, these are becoming numbered lists. | `mm2oowriter.xsl` | [0c070f89](https://github.com/freeplane/freeplane/commit/0c070f89e069fda9233d82836ac1c15dc06326e1) |
| 2013-05-30 | `feature` | Implement a generator for bullet list styles. | `mm2oowriter.styles.xsl` | [9818b417](https://github.com/freeplane/freeplane/commit/9818b417524c570d6e09c600d74c95f938b10109) |
| 2013-05-30 | `feature` | Implement a generator for numbering list styles. | `mm2oowriter.styles.xsl` | [fd99c23b](https://github.com/freeplane/freeplane/commit/fd99c23b001ced86968bd84af886d3f75068f494) |
| 2013-05-30 | `feature` | Fix: A new list is made for each list-item. | `mm2oowriter.xsl` | [332724e3](https://github.com/freeplane/freeplane/commit/332724e36e6e1119be2be55ab1871674d872e0f2) |
| 2013-05-30 | `feature` | Add some comments for what the automatic-styles are used. | `mm2oowriter.xsl` | [4826fedf](https://github.com/freeplane/freeplane/commit/4826fedf1aca7f479717d43bc23ce7c595e267e0) |
| 2013-05-28 | `feature` | Introduce a new template for output of paragraph-styles. | `mm2oowriter.styles.xsl` | [c87f9080](https://github.com/freeplane/freeplane/commit/c87f90803559ffe0ff0ec9d8f7e299ea7fcd7d92) |
| 2013-05-28 | `feature` | Introduce a new template for output of headings. | `mm2oowriter.xsl` | [5d330ee3](https://github.com/freeplane/freeplane/commit/5d330ee37ce150b88a44ba6aa622d5a305029810) |
| 2013-05-28 | `feature` | Add color attribute. | `mm2oowriter.styles.xsl` | [f9cc2243](https://github.com/freeplane/freeplane/commit/f9cc224318124faa935cd792fd3b0fdf77b8408a) |
| 2013-05-28 | `fix` | Fix: Size needs to contain a unit (`pt`). | `mm2oowriter.styles.xsl` | [8d87295b](https://github.com/freeplane/freeplane/commit/8d87295b3cf691cfcea8db66122a6c8f3fe1f5df) |
| 2013-05-28 | `fix` | Fix tests for bold and italic font-style. | `mm2oowriter.styles.xsl` | [8a4188d1](https://github.com/freeplane/freeplane/commit/8a4188d1c5b1217ac6740a53fd4e6a97d36bb243) |
| 2013-05-28 | `feature` | Add a todo-comment. | `mm2oowriter.styles.xsl` | [5d8d9e8d](https://github.com/freeplane/freeplane/commit/5d8d9e8dbef694c5f27a01212673ac5b92b77005) |
| 2013-05-28 | `feature` | Add display-name for style and replace space by underscore in name. | `mm2oowriter.styles.xsl` | [125541d4](https://github.com/freeplane/freeplane/commit/125541d472869060e1c6ce803e6e523f0d666ae5) |
| 2013-05-20 | `fix` | fix eclipse preferences for freeplane_plugin_workspace | `.classpath`, `org.eclipse.core.resources.prefs` +1 | [e0cad2ce](https://github.com/freeplane/freeplane/commit/e0cad2ceb7e9b35fc909700a163de3900947ce8d) |
| 2013-05-10 | `feature` | added restriction to "new project" dialog | `Resources_en.properties`, `WorkspaceImportProjectAction.java` +4 | [e73eecd5](https://github.com/freeplane/freeplane/commit/e73eecd58d331cca64d19f33de4c3f09f0701a02) |
| 2013-04-27 | `feature` | add idw-gpl.jar | `.classpath`, `MANIFEST.MF` +3 | [513df31b](https://github.com/freeplane/freeplane/commit/513df31bbae5a293a336c013eb4b80c2c0da1e8c) |
| 2013-04-25 | `feature` | changed DefaultWorkspaceTreeModel to support nodes in root other than projects | `AWorkspaceTreeNode.java`, `WorkspaceModel.java` +3 | [54fde07b](https://github.com/freeplane/freeplane/commit/54fde07b427666ae99b27f74c85cb271e4b39a09) |
| 2013-04-19 | `api_change` | upgrade to commons-lang-2.6 | `.classpath`, `MANIFEST.MF` +6 | [71b01210](https://github.com/freeplane/freeplane/commit/71b0121061f0682dad0bab6752a73b927e077edb) |
| 2013-04-16 | `feature` | fixed a problem with the new action enable method and workspace action | `AWorkspaceAction.java`, `WorkspaceRemoveProjectAction.java` +1 | [2f64fce5](https://github.com/freeplane/freeplane/commit/2f64fce595b74792b9a6ae20767bd4c9992cca01) |
| 2013-04-15 | `feature` | bugfix for "new project folder was not created" | `WorkspaceNewProjectAction.java` | [433a4e63](https://github.com/freeplane/freeplane/commit/433a4e6375f77639313aac4fab6e430d4bfacbc1) |
| 2013-04-14 | `feature` | add configuration options for running from command line | `FormatTranslation.java` | [0d69e23c](https://github.com/freeplane/freeplane/commit/0d69e23ce0a7995db165d46122ae0c5da82b4d95) |
| 2013-03-29 | `feature` | add link to Freeplane_LaTeX.mm in doc/freeplane.mm | `freeplane.mm` | [63a532b6](https://github.com/freeplane/freeplane/commit/63a532b6bc75c2b763fd49867286b8b5093cc1de) |
| 2013-03-26 | `fix` | correct text | `Resources_en.properties` | [9d01db92](https://github.com/freeplane/freeplane/commit/9d01db929563120c5bda397d440be7ed1bdccf66) |
| 2013-03-16 | `feature` | Add ... in the Menu | `Resources_en.properties` | [96bf9137](https://github.com/freeplane/freeplane/commit/96bf9137968fe218d25667e6b48bd5d9347adc8e) |
| 2013-03-02 | `fix` | fix ant build | `build.xml` | [afc80bf6](https://github.com/freeplane/freeplane/commit/afc80bf60ec9e5d1e35913e549e5a2eb4592a97a) |
| 2013-02-10 | `fix` | 1895]: Input error of dialog editor : fix NPE in shtml (0.16.07) | `SimplyHTML.jar` | [02e0ccb9](https://github.com/freeplane/freeplane/commit/02e0ccb92428aa45e9b2d1632e255bd2a2ced160) |
| 2013-01-26 | `feature` | add freeplaneDebugJDK.bat | `freeplaneDebugJDK.bat` | [00033254](https://github.com/freeplane/freeplane/commit/00033254ae4cd2458a2ebf8d1404a306f87d11a6) |
| 2013-01-21 | `feature` | add lib/jortho.jar to .classpath, otherwise freeplane does not compile under eclipse | `.classpath` | [7d9bbed1](https://github.com/freeplane/freeplane/commit/7d9bbed17a1debf8b0702337f45982e8195bef57) |
| 2013-01-20 | `feature` | add batch file for remote debugging with -Xdebug -Xrunjdwp:transport=dt_socket,address=104 | `freeplaneDebug.bat` | [38e08e79](https://github.com/freeplane/freeplane/commit/38e08e79a3699068d4131c7cbb1354fe6e33867a) |
| 2013-01-08 | `feature` | Add documentation for new 1.3.x features (Blair's OpenMapsIntegration and latex in core) t | `freeplane.mm` | [28462475](https://github.com/freeplane/freeplane/commit/28462475a06d6ca81c4a860b6315e852557e3e30) |

### Dettagli commit con note

**[11220b0b](https://github.com/freeplane/freeplane/commit/11220b0b772285f70c87d48f5f178a9dafa41e46)** (2013-09-10) — Export2odt: Make list-, details- and note-styles be kids of node-style.

> This includes:
> * For each style in the map, create depending style with the same name,
>   just " Note" resp. " Details" appended.
> * For each style in the map and their" Note" and "Details" styles,
>   create additional automatic styles for the lists.

**[54e8921a](https://github.com/freeplane/freeplane/commit/54e8921a53a298da62dc6b3fe277712b964b04d3)** (2013-06-04) — Add a Mindmap representing the current `appletMenu` structures.

> Includes an ant-task for building.

**[f3c8cd32](https://github.com/freeplane/freeplane/commit/f3c8cd321aba1902f6d80b48cb5c6984c3a3f7fe)** (2013-06-03) — Fix git-attributes for **/help/doc/JavaHelpSearch/OFFSETS.

> The path in top-level .gitattributes file does not match. Since the
> path is quite long I decided to local .gitattributes file down there.

**[f43d7970](https://github.com/freeplane/freeplane/commit/f43d7970de11ef47f05d30998f86454b112254e9)** (2013-05-30) — Add support for nested lists in rich-nodes.

> This may not catch all cases, though.

**[383a2a3c](https://github.com/freeplane/freeplane/commit/383a2a3c2ac48522af47c3d1562ed70f68078de1)** (2013-05-30) — Fix: Additional, empty paragraphs after lists in rich-tect nodes.

> There must be no additional paragraphs! If you want distance behind the
> list, change the style in your word-processor.

**[aac85671](https://github.com/freeplane/freeplane/commit/aac85671d2ea23bb0a15e0c304cf09b31e22a34b)** (2013-05-30) — Fix: style `Numbering Symbols` was missing.

> This resulted in a new style `Numbering_20_Symbols` when showing
> styles in LibreOffice.

**[332724e3](https://github.com/freeplane/freeplane/commit/332724e36e6e1119be2be55ab1871674d872e0f2)** (2013-05-30) — Fix: A new list is made for each list-item.

> Instead of this now create a common list for all nodes sharing the
> same parent node. This means the parent node is creating the list, and
> the node itself is only creating the list-item.

**[e73eecd5](https://github.com/freeplane/freeplane/commit/e73eecd58d331cca64d19f33de4c3f09f0701a02)** (2013-05-10) — added restriction to "new project" dialog

> -prevent the user from creating more than one project with the same name or path


---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-12-12 | `fix` | Fix link to Freeplane_LaTex.mm in doc/freeplane.mm | `freeplane.mm` | [4bc299ed](https://github.com/freeplane/freeplane/commit/4bc299ed9fcbd1177114e6fcebcb811789cab430) |
| 2012-09-24 | `fix` | fix .gitignore from bzr | `.gitignore` | [7c41c63f](https://github.com/freeplane/freeplane/commit/7c41c63fc869f4ed95d64d4e6329ebb983a5ae60) |
| 2012-08-12 | `fix` | Do not submit auto bug reports by default (final version) | `freeplane.properties` | [cf8ea458](https://github.com/freeplane/freeplane/commit/cf8ea458f477b34ee9bfaab68416b0dd7596866a) |
| 2012-07-08 | `feature` | not try to generate automatic bug reports for new users | `freeplane.properties` | [8c14aff8](https://github.com/freeplane/freeplane/commit/8c14aff85b718edc9c5f57b45b48c70590eb14ad) |
| 2012-05-28 | `feature` | history fnatter rich text editor: add "Paste plain text" context menu item and "default pa | `history_en.txt` | [3cdef526](https://github.com/freeplane/freeplane/commit/3cdef526f53c9044e6b7ce9b384ddf56017a049c) |
| 2012-05-13 | `api_change` | reminder scripting API | `history_en.txt` | [841df160](https://github.com/freeplane/freeplane/commit/841df16016c83163932f63e264365719055686f1) |
| 2012-04-25 | `feature` | new docu | `BackgroundContextMenu.png`, `In-lineEditContextMenu.png` +8 | [d725622c](https://github.com/freeplane/freeplane/commit/d725622c41cb9559b8df57209e376631c649c6fc) |
| 2012-03-04 | `feature` | add "- character to VM args in launch configurations | `freeplane core.launch`, `freeplane-osgi.launch` | [9f0c5dac](https://github.com/freeplane/freeplane/commit/9f0c5daccd7045f814d20c773d4159d45e339d05) |
| 2012-03-03 | `fix` | Fix english in dialect_info.unknownApp | `Resources_en.properties` | [8ec7d474](https://github.com/freeplane/freeplane/commit/8ec7d474a5f9bd4189bf2badd8d435390aec7918) |
| 2012-03-03 | `feature` | add what I've done to history_en.txt | `history_en.txt` | [c9cd6d2b](https://github.com/freeplane/freeplane/commit/c9cd6d2ba12553977d919eb6640c847cb8fa9182) |
| 2012-02-25 | `feature` | add more test cases to EditDistanceStringMatchingStrategiesTest | `EditDistanceStringMatchingStrategiesTest.java` | [8eb72a42](https://github.com/freeplane/freeplane/commit/8eb72a421ef58068903ff2ae12ce197bf767a9ed) |
| 2012-02-12 | `fix` | export to excel (fix from ewl) | `mm2xls_utf8.xsl` | [f5e0d533](https://github.com/freeplane/freeplane/commit/f5e0d53302d8d28a64cb5474838dc8e46a82866a) |
| 2012-01-17 | `feature` | update formatter.xml to new eclipse | `formatter.xml` | [189884f6](https://github.com/freeplane/freeplane/commit/189884f62dab1c384c2dee644dd94258374bf904) |
| 2012-01-07 | `feature` | add tooltip for single instance mode | `Resources_en.properties` | [da19da5f](https://github.com/freeplane/freeplane/commit/da19da5ff3de831d7b8bd4feb57c3140c62bfdbc) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-12-29 | `feature` | new icon for matching nodes | `highlight_matching_nodes.png` | [1b76e170](https://github.com/freeplane/freeplane/commit/1b76e170a07bb89dced166a11139f29eed59ce9d) |
| 2011-12-24 | `feature` | Rename cation "New cloud" to "Add / remove cloud" | `Resources_en.properties` | [2d851cc1](https://github.com/freeplane/freeplane/commit/2d851cc1a847689a39e737734f5d86d7eb5d6c6c) |
| 2011-12-06 | `feature` | add freeplane core launch configuration | `freeplane core.launch` | [0cc46c7a](https://github.com/freeplane/freeplane/commit/0cc46c7a463999146f654650eb1a8eb21008faeb) |
| 2011-10-30 | `feature` | Add-ons: remove unused column header names | `Resources_en.properties` | [2d1b3181](https://github.com/freeplane/freeplane/commit/2d1b31814edbe62ee4e4552ca25c84b6db2e1e05) |
| 2011-10-23 | `feature` | release add-ons | `history_en.txt` | [4b8e9153](https://github.com/freeplane/freeplane/commit/4b8e91531b8b3194c5ead6d4a790de49a92d058d) |
| 2011-10-23 | `feature` | New docu version from Jokro | `freeplane.mm`, `freeplaneApplications.mm` +3 | [c294534d](https://github.com/freeplane/freeplane/commit/c294534d41a3bf9ed4e2e00374dcf946f144d001) |
| 2011-10-16 | `feature` | History, new icons for links | `history_en.txt`, `Link.png` +1 | [51b3a43b](https://github.com/freeplane/freeplane/commit/51b3a43b3bdfdccde140e5d5516a9f2b469c4b72) |
| 2011-10-09 | `fix` | fix: rename ja docu files | `Freeplane_ja.mm`, `freeplaneTutorial_ja.mm` +2 | [d535fd43](https://github.com/freeplane/freeplane/commit/d535fd43fd1eed58a81bcb561c49170e1c30161d) |
| 2011-10-08 | `feature` | new link icons | `Link.png`, `LinkLocal.png` | [6cfe7506](https://github.com/freeplane/freeplane/commit/6cfe7506ff157006490e1bbd7658a36af90124fe) |
| 2011-10-08 | `feature` | new icon close.png | `close.png` | [25763385](https://github.com/freeplane/freeplane/commit/25763385497356068a144a42df5a0f4370b2f248) |
| 2011-09-25 | `feature` | add Serbian to i18n | `Resources_en.properties` | [11724819](https://github.com/freeplane/freeplane/commit/11724819d1c9504327a348429ac35939158ee6b5) |
| 2011-09-03 | `feature` | new docu | `freeplane.mm`, `freeplaneTutorial.mm` | [4f2b83c5](https://github.com/freeplane/freeplane/commit/4f2b83c53439256ab644eee81a4b133d199bc9bb) |
| 2011-09-03 | `feature` | enable editing of hyperlinks in editor | `freeplane.properties`, `Resources_en.properties` | [2d03eef9](https://github.com/freeplane/freeplane/commit/2d03eef9a5ffb09d3f2d0ddf0b68b1aa995ced3a) |
| 2011-08-28 | `feature` | new english property file made by Jokro | `Resources_en.properties` | [cd1ddfdf](https://github.com/freeplane/freeplane/commit/cd1ddfdf1d38ba27cb47ee8545ba256dc197063f) |
| 2011-08-08 | `feature` | new docu (jokro) | `freeplane.mm` | [135a028d](https://github.com/freeplane/freeplane/commit/135a028d14513a1ceb8bd8bfd3ac3559268d5717) |
| 2011-06-12 | `fix` | fix xml syntax errors in mm2msp_utf8.xsl | `mm2msp_utf8.xsl` | [e0c431dd](https://github.com/freeplane/freeplane/commit/e0c431dd5f8a98e44309de7d97e8a3f0604aa601) |
| 2011-05-07 | `feature` | enable BranchesOverlap on standard templates | `conceptMap.mm`, `standard.mm` | [ef42f702](https://github.com/freeplane/freeplane/commit/ef42f702eae3ae7086eb0f775b0de2b2a0013111) |
| 2011-04-29 | `fix` | updated for DecimalPatternFormat fix | `FormattedObjectTest.java` | [1dadb649](https://github.com/freeplane/freeplane/commit/1dadb649c7b1675e5cb01af8a72a8882e57aa515) |
| 2011-04-13 | `fix` | fix errorneous message | `Resources_en.properties` | [20931309](https://github.com/freeplane/freeplane/commit/209313095a1094e7b72ee6fbc146a76757d465d3) |
| 2011-03-06 | `feature` | Enable printing from rich text editor | `SimplyHTML.jar`, `freeplane.properties` +1 | [eb249712](https://github.com/freeplane/freeplane/commit/eb2497121e491c63a79f2ab441db80c76ef881f9) |
| 2011-03-03 | `feature` | add doc/FP_Key_Mappings_Quick_Guide_nl.odt , doc/freeplane_nl.jpg | `FP_Key_Mappings_Quick_Guide_nl.odt`, `freeplane_nl.jpg` | [ccafdb3b](https://github.com/freeplane/freeplane/commit/ccafdb3b5383be1370230897deffb7c803bfe3a3) |
| 2011-02-26 | `fix` | fix freeplane_uitest and move PatternFormatTest to this project | `.classpath`, `MANIFEST.MF` +13 | [384211a3](https://github.com/freeplane/freeplane/commit/384211a32c25decffa26d7b81edc415484769f1e) |
| 2011-01-14 | `api_change` | added a link to the API documentation to the user manual | `freeplane.mm` | [eeb70d26](https://github.com/freeplane/freeplane/commit/eeb70d263c983bc6bf21e0c2fc58992e45b28d8f) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-12-28 | `feature` | add release dates | `history_en.txt` | [6710aefc](https://github.com/freeplane/freeplane/commit/6710aefc4a0aaf73a4127b9b74a137f5af3c78a1) |
| 2010-12-26 | `feature` | added new check for use of $1 instead of {0} | `FormatTranslation.java` | [ab027632](https://github.com/freeplane/freeplane/commit/ab027632a9ffc69d802e2b663014d3931b8ca7a3) |
| 2010-12-26 | `feature` | added new check for correct usage of {0} and {1} | `FormatTranslation.java` | [57607876](https://github.com/freeplane/freeplane/commit/57607876eec7b9625632d6030dd063ec777b87dc) |
| 2010-12-04 | `feature` | fix freeplane_mac accordingly to the new API | `MacChanges.java` | [94f7b3f1](https://github.com/freeplane/freeplane/commit/94f7b3f155cd485fef1107f1e48fe19fae8d43d9) |
| 2010-11-15 | `fix` | fix MANIFEST.MF | `MANIFEST.MF` | [32ee22a6](https://github.com/freeplane/freeplane/commit/32ee22a63df62c8f750183ea5d7dd7936b2178e9) |
| 2010-11-14 | `fix` | fix typo | `Resources_en.properties` | [5a992809](https://github.com/freeplane/freeplane/commit/5a992809afcaf302caaa42e853db5c5918fb50ef) |
| 2010-11-14 | `feature` | modify source settings for freeplane knopflerfish.launch: add formula plugin | `freeplane knopflerfish.launch` | [a656853c](https://github.com/freeplane/freeplane/commit/a656853c9f9399fb21bf25f3d39e069a312a285e) |
| 2010-11-13 | `fix` | fix xsl files | `mm2oowriter.xsl`, `mm2wordml_utf8.xsl` | [27e665cf](https://github.com/freeplane/freeplane/commit/27e665cf0ee3e57a40bcea9d96211c5f3596a2dd) |
| 2010-10-03 | `fix` | Bug fix in remove format action of simply html | `SimplyHTML.jar` | [50f748fe](https://github.com/freeplane/freeplane/commit/50f748fe385fe4dd821bd2953d80dc0bb70b2a82) |
| 2010-08-02 | `feature` | added new features listed on 1.1.x-1.2.x wiki page | `history_en.txt` | [f7ee7273](https://github.com/freeplane/freeplane/commit/f7ee7273c5aa9b318a489750aee83edcf162325a) |
| 2010-07-13 | `feature` | - remove junit dependency from the ant build - enable debug on javac - re-indented | `build.xml` | [e3ac17ea](https://github.com/freeplane/freeplane/commit/e3ac17ea99647bb06a75141fecd4fe78e6461398) |
| 2010-05-22 | `fix` | fix freeplane/ant/ant.properties | `ant.properties` | [c9f025a1](https://github.com/freeplane/freeplane/commit/c9f025a1f185ffba2966097fa9d59f351deaaadd) |
| 2010-04-29 | `feature` | Add Map.getFile() to scripting API | `history_en.txt` | [44d87ac1](https://github.com/freeplane/freeplane/commit/44d87ac1221a107eb1dc1565439ebad739914710) |
| 2010-04-28 | `feature` | Start Mac menu diffs in Menu Reference; add Help About to freeplane.mm | `FP_MenuReference.mm`, `freeplane.mm` | [2f9372a6](https://github.com/freeplane/freeplane/commit/2f9372a6b61978f95ca541a70cec7870e7d7704e) |
| 2010-04-23 | `fix` | Major edits to freeplane.mm but still needs update for Mantis Bug 587 | `freeplane.mm` | [e7b3072b](https://github.com/freeplane/freeplane/commit/e7b3072be5f722441e072a07d917f4427431918c) |
| 2010-03-14 | `feature` | better support for rich text and notes in mm2text | `mm2text.xsl` | [9bba9a72](https://github.com/freeplane/freeplane/commit/9bba9a72579573368b6e7afca240b1f33df3f325) |
| 2010-03-11 | `feature` | add missing key for icon_not_found icon that is referenced in the documentation maps | `Resources_en.properties` | [a9322f62](https://github.com/freeplane/freeplane/commit/a9322f62f97032e09a30e079cf7a2db1c42fc575) |
| 2010-03-09 | `feature` | add empty icon empty.png to resources | `empty.png` | [d86efc23](https://github.com/freeplane/freeplane/commit/d86efc23ae044ece60a4e89f156806e268fe3cfb) |
| 2010-02-28 | `feature` | 1.0.40: add forgotten feature: Filter by regexp | `history_en.txt` | [e01e9ce8](https://github.com/freeplane/freeplane/commit/e01e9ce8c9a1773970bece53039443db40562a9d) |
| 2010-02-23 | `api_change` | Script API: corrected entries for find methods of Controller and Nodes | `history_en.txt` | [d423a8e3](https://github.com/freeplane/freeplane/commit/d423a8e3fb8f7118796038caaf068eb2af9cda9e) |
| 2010-02-01 | `fix` | 402]: 2 errors when loading online help in 1.0.39 -- Fix links in docu maps | `freeplane.mm`, `freeplane_de.mm` +6 | [f4e81f4e](https://github.com/freeplane/freeplane/commit/f4e81f4e5192553e45f4598d28e6243e7c64ba9c) |

---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-09-23 | `feature` | new reminder icon | `clock2.png` | [72109698](https://github.com/freeplane/freeplane/commit/72109698f8297cc36cf45f0b19e02088eab7d4af) |
| 2009-09-20 | `feature` | New icons for Simplyhtml | `Resources_en.properties` | [cdc043c0](https://github.com/freeplane/freeplane/commit/cdc043c0797dd5d425f4d75bbc2a91d9ef41f3dc) |
| 2009-09-20 | `feature` | new paths for Simply html tool bar | `Resources_en.properties` | [554036f4](https://github.com/freeplane/freeplane/commit/554036f4915b63a3231a04dd153fd59ed6059b48) |
| 2009-09-10 | `feature` | new icons for View menu | `freeplane.properties` | [a727e2f6](https://github.com/freeplane/freeplane/commit/a727e2f648c1cd6acc2007c1871d42ade780576f) |
| 2009-09-09 | `feature` | new paths for simplyhtml toolbar icons | `freeplane.properties` | [b03f71a0](https://github.com/freeplane/freeplane/commit/b03f71a0d7dc150c40279336dc4439ad34425acd) |
| 2009-09-07 | `feature` | new icons for decrypted and encrypted node | `decrypted.png`, `encrypted.png` | [3b1a9103](https://github.com/freeplane/freeplane/commit/3b1a91030914408fc99f663a9956e5bb43962f0c) |
| 2009-09-06 | `feature` | new icon | `knotes.png` | [7d97c696](https://github.com/freeplane/freeplane/commit/7d97c696d388d9eac7fff349e7aceba3ce420af9) |
| 2009-09-04 | `feature` | new attributes icon | `showAttributes.gif` | [5e0e1184](https://github.com/freeplane/freeplane/commit/5e0e1184110e692dee88bd208ba6457520c14f21) |
| 2009-09-04 | `feature` | new icons | `back.png`, `editcopy.png` +4 | [3637c391](https://github.com/freeplane/freeplane/commit/3637c39175253023957335dd848957d4683ba967) |
| 2009-09-03 | `feature` | new icons | `back.png`, `editcopy.png` +4 | [9f5cccc3](https://github.com/freeplane/freeplane/commit/9f5cccc3d766a3d778794f1c60dccfa249c61954) |
| 2009-08-26 | `feature` | add dictionary_hr.ortho | `dictionary_hr.ortho` | [997608cb](https://github.com/freeplane/freeplane/commit/997608cb457504f75aad50aa2b96a514319e74aa) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
