# Freeplane Plugin Timeline — Rapporto storico

_Generato il 2026-04-25 10:12_

---

## Indice dei plugin

- [Core](#freeplane-core) — **13039** commit
- [Altro](#other) — **1803** commit
- [Script / Groovy](#freeplane-plugin-script) — **1290** commit
- [Framework OSGi](#freeplane-framework) — **669** commit
- [LaTeX](#freeplane-plugin-latex) — **210** commit
- [Formula](#freeplane-plugin-formula) — **187** commit
- [API pubblica](#freeplane-api) — **173** commit
- [SVG](#freeplane-plugin-svg) — **159** commit
- [Add-ons](#addons) — **157** commit
- [Bug Report](#freeplane-plugin-bugreport) — **136** commit
- [OpenMaps](#freeplane-plugin-openmaps) — **82** commit
- [Debug Helper](#freeplane-debughelper) — **49** commit
- [JSyntaxPane](#freeplane-plugin-jsyntaxpane) — **45** commit
- [Markdown](#freeplane-plugin-markdown) — **37** commit

---

## Core
**Chiave modulo:** `freeplane_core`  
**Commit totali:** 13039

> Il **nucleo** dell'applicazione: gestione delle mappe `.mm`, rendering del canvas, sistema di nodi/edge, filtri, export, UI principale e tutto ciò che non è un plugin separato.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |  505  ████████ |
| 2025 | 1165  ████████████████████ |
| 2024 |  715  ████████████ |
| 2023 |  844  ██████████████ |
| 2022 |  825  ██████████████ |
| 2021 |  955  ████████████████ |
| 2020 |  728  ████████████ |
| 2019 |  382  ██████ |
| 2018 |  495  ████████ |
| 2017 |  709  ████████████ |
| 2016 |  783  █████████████ |
| 2015 | 1109  ███████████████████ |
| 2014 |  468  ████████ |
| 2013 |  373  ██████ |
| 2012 |  578  █████████ |
| 2011 |  933  ████████████████ |
| 2010 |  860  ██████████████ |
| 2009 |  607  ██████████ |
| 2008 |    5  █ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 9267 | 71% |
| fix | 1910 | 15% |
| feature | 1162 | 9% |
| refactor | 446 | 3% |
| build | 146 | 1% |
| api_change | 58 | 0% |
| test | 27 | 0% |
| docs | 23 | 0% |

### Top contributor

- **Dimitry Polivaev** — 5269 commit
- **dpolivaev** — 2051 commit
- **dpolivaev@users.sourceforge.net** — 998 commit
- **Ldm Public** — 322 commit
- **boercher** — 300 commit
- **Pedro Albuquerque** — 276 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-03-29 | `feature` | 2026-03-29-copy-markdown Add chat markdown copy action | [235726bb](https://github.com/freeplane/freeplane/commit/235726bb73c0097f6b7d451e8cf2f7c0e9ea11e6) |
| 2026-03-16 | `feature` | add methods that determine childNodesLayout origin | [94b7deb4](https://github.com/freeplane/freeplane/commit/94b7deb42a4a962a65d89d8c9a0e0d869856599a) |
| 2026-03-16 | `feature` | make it clear that getStyles returns List (ordered); add JavaDoc | [3fabbea3](https://github.com/freeplane/freeplane/commit/3fabbea32825e20adb663fa17f98b68c7449c572) |
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, scrip | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |
| 2026-03-15 | `fix` | Issue #2845 fix locking view root node with password | [cf1d28d6](https://github.com/freeplane/freeplane/commit/cf1d28d6bc2cdd0b500f112ba209554955d40da8) |
| 2026-02-20 | `feature` | Add tag category characterization baseline tests (2026-02-20-expose-tags-ai-tool | [290c2cff](https://github.com/freeplane/freeplane/commit/290c2cff344058fb8ce9da0eb8a360dfb3c678e7) |
| 2026-02-20 | `api_change` | 2026-02-20-expose-styles-ai-tools Expose styles in AI tools and unify list API | [5432e96f](https://github.com/freeplane/freeplane/commit/5432e96f9c9492b88242fcbaec14455da46f731b) |
| 2026-02-20 | `feature` | 2026-02-20-mcp-bearer: support MCP bearer auth with legacy fallback | [011b24a2](https://github.com/freeplane/freeplane/commit/011b24a255e75801e93a2d6b8cfe02038613d5db) |
| 2026-02-20 | `feature` | 2026-02-20-ollama-token-auth: add Ollama token auth and cache invalidation | [a7d66d2c](https://github.com/freeplane/freeplane/commit/a7d66d2c18f8d25c59be07d8f223ddca8242e8df) |
| 2026-02-15 | `fix` | Fix svg icons using accent colors | [0b006673](https://github.com/freeplane/freeplane/commit/0b006673bd50dcd9161833d629e2b5496535dca9) |
| 2026-02-15 | `fix` | 2026-02-15-secret-property-reads: extract ApplicationPropertyStore and fix secre | [899ffda0](https://github.com/freeplane/freeplane/commit/899ffda0eee42b40c4d9132e19709d2222e73ec7) |
| 2026-02-14 | `feature` | 2026-02-14-ai-panel-font-size: scale AI panel styles and add configurable font s | [dae8d16b](https://github.com/freeplane/freeplane/commit/dae8d16bc1556f2b36bca9ee15e89d0de7f99306) |
| 2026-02-14 | `feature` | 2026-02-14-bootstrap-activator: add Java 8 bootstrap activator with Java 17 runt | [92367151](https://github.com/freeplane/freeplane/commit/923671512a2b2658c7a8496da3f6085461b301c0) |
| 2026-02-09 | `feature` | 2026-02-05-mcp-authentication: Add MCP API key auth with generated key flow | [a1b8d59c](https://github.com/freeplane/freeplane/commit/a1b8d59c8fa1c04f1b413efcf371322b386855b9) |
| 2026-02-08 | `feature` | 2026-02-05-secret-settings: add secret settings field with show/hide icons | [76ee422b](https://github.com/freeplane/freeplane/commit/76ee422b2abeacfc8a68b3d1f4f708e37aa60408) |
| 2026-02-08 | `feature` | 2026-02-08-profile-menu: add AI profile manager menu entry | [46b78cf5](https://github.com/freeplane/freeplane/commit/46b78cf5d1e14486c09b2213340c80797529893a) |
| 2026-02-06 | `fix` | fix profile icon | [76f609e8](https://github.com/freeplane/freeplane/commit/76f609e80afd92112a267d5cd4cc4bf2a5070ddc) |
| 2026-02-06 | `feature` | 2026-02-03-assistant-profiles: add profile management UI, structured profile tra | [63c83935](https://github.com/freeplane/freeplane/commit/63c83935626315cf774bb8bd355c9f5573cb89d6) |
| 2026-02-02 | `feature` | Add user readme about configuration location. | [f5e3b154](https://github.com/freeplane/freeplane/commit/f5e3b154e06c20bc2c0ee1b5062cc8a378d9638d) |
| 2026-02-01 | `fix` | fix NPE | [085bd1c8](https://github.com/freeplane/freeplane/commit/085bd1c801fb60b3e4311c7c3284d0222aeb9733) |

---

## Altro
**Chiave modulo:** `other`  
**Commit totali:** 1803

> Commit che toccano aree **trasversali** o non classificabili in un singolo plugin: build system, CI, traduzioni, documentazione generale del progetto.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |  184  ████████████████████ |
| 2025 |   84  █████████ |
| 2024 |  152  ████████████████ |
| 2023 |  147  ████████████████ |
| 2022 |   52  █████ |
| 2021 |   37  ████ |
| 2020 |   46  █████ |
| 2019 |   31  ███ |
| 2018 |   45  █████ |
| 2017 |   80  ████████ |
| 2016 |  105  ███████████ |
| 2015 |  160  █████████████████ |
| 2014 |   91  ██████████ |
| 2013 |  160  █████████████████ |
| 2012 |   75  ████████ |
| 2011 |  121  █████████████ |
| 2010 |  169  ██████████████████ |
| 2009 |   63  ███████ |
| 2008 |    1  █ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 1156 | 64% |
| feature | 282 | 16% |
| fix | 175 | 10% |
| build | 81 | 4% |
| refactor | 47 | 3% |
| docs | 32 | 2% |
| test | 16 | 1% |
| api_change | 14 | 1% |

### Top contributor

- **Dimitry Polivaev** — 949 commit
- **dpolivaev** — 295 commit
- **dpolivaev@users.sourceforge.net** — 140 commit
- **Felix Natter** — 117 commit
- **Hartmut Goebel** — 69 commit
- **boercher** — 50 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-03-29 | `api_change` | expose-node-tags-ai-tools: Align task script naming with MapTag API | [998bc8c6](https://github.com/freeplane/freeplane/commit/998bc8c60e2e4586878f535ddc02808ab986ad79) |
| 2026-03-17 | `feature` | 2026-03-17-clarify-create: Clarify createNodes optional overrides and blank styl | [6e405f6e](https://github.com/freeplane/freeplane/commit/6e405f6ef20808a43d2655d64593a7e9ec7dde27) |
| 2026-03-15 | `feature` | 2026-03-15-provider-model-discovery-fallback: add model list fallback | [8cc17ad3](https://github.com/freeplane/freeplane/commit/8cc17ad318ce78471356e8a4b838a7dc5690e8f1) |
| 2026-02-20 | `feature` | 2026-02-20-expose-tags-ai-tools: add AI map-level tag category tools | [e8e66c8b](https://github.com/freeplane/freeplane/commit/e8e66c8ba7c0878605745e79f7d2f0ac8e9a053f) |
| 2026-02-19 | `fix` | 2026-02-18-hyperlinks: open chat history links via LinkController and fix error  | [fcd8e951](https://github.com/freeplane/freeplane/commit/fcd8e9517da4de3ca49a64d0d335a93b820d34bf) |
| 2026-02-16 | `fix` | fix constitution location in AGENTS.md | [4d952192](https://github.com/freeplane/freeplane/commit/4d952192d70352b53406670b0adedb0eb7cae0f6) |
| 2026-02-15 | `feature` | add harmonization statement | [6fedc207](https://github.com/freeplane/freeplane/commit/6fedc20742e0d55e8b57a0fdc415e65b062c6fc1) |
| 2026-02-15 | `fix` | fix AI panel font size | [82fc7d71](https://github.com/freeplane/freeplane/commit/82fc7d7185c868013e84dc9add458357cd2d6211) |
| 2026-02-09 | `feature` | Enable multi-row chat deletion in chat list dialog | [90e69ebd](https://github.com/freeplane/freeplane/commit/90e69ebd146cbfd0fcd7f4825332c7273ee3a19e) |
| 2026-02-08 | `fix` | 2026-02-08-transcript-window: preserve full transcript and fix context boundary  | [4cdfbcc7](https://github.com/freeplane/freeplane/commit/4cdfbcc70031fd6d130d0d719729a1bc6a9f0dc0) |
| 2026-02-07 | `feature` | 2026-02-06-chat-turn: add translated undo/redo tooltips and working keyboard sho | [586d39d0](https://github.com/freeplane/freeplane/commit/586d39d0c7c3a0dc2b27a350dd1c78a5b64d740e) |
| 2026-02-07 | `feature` | Fix initial profile injection in new chat sessions | [3f166861](https://github.com/freeplane/freeplane/commit/3f1668618d06364b63983cb942c5db53f2039c56) |
| 2026-02-07 | `feature` | 2026-02-06-conversation-state: add chat memory task drafts | [2b73b0e8](https://github.com/freeplane/freeplane/commit/2b73b0e83bd70fb1c2252aed690bdfeb9e7cacc2) |
| 2026-02-06 | `feature` | 2026-02-06-conversation-state: add conversation projector and parity tests | [f8cef994](https://github.com/freeplane/freeplane/commit/f8cef9945ac2e1738de6c65159ace7733e914127) |
| 2026-02-06 | `feature` | 2026-02-06-conversation-state: add chat state core and planning tasks | [95642042](https://github.com/freeplane/freeplane/commit/95642042949314c0691ba71549e0a5382653b82f) |
| 2026-02-05 | `feature` | Add new tasks to backlog | [261ff399](https://github.com/freeplane/freeplane/commit/261ff3991e91ba007751d357763e7f338fe72561) |
| 2026-02-03 | `feature` | 2026-02-03-assistant-profiles: add assistant profile chat memory | [eec8e09c](https://github.com/freeplane/freeplane/commit/eec8e09c756f27390b4859e4761a8baa555b3e36) |
| 2026-02-01 | `feature` | Add hint for LLM where to find tasks | [173c8f14](https://github.com/freeplane/freeplane/commit/173c8f14816a08ac1b57574d274e24d99b2062df) |
| 2026-01-31 | `feature` | Add "AI panel" to latest freeplane features | [963c008e](https://github.com/freeplane/freeplane/commit/963c008e62e8fa35095598f9e2f6a1d68f10ed2f) |
| 2026-01-31 | `feature` | 2026-01-31-map-warning: add map selection guidance | [24f30cbd](https://github.com/freeplane/freeplane/commit/24f30cbd5da0479e88b10c5a7d5f0ffa3c0be3aa) |

---

## Script / Groovy
**Chiave modulo:** `freeplane_plugin_script`  
**Commit totali:** 1290

> Permette di eseguire script **Groovy** (e altri linguaggi JVM) direttamente sulle mappe. È il cuore dell'automazione in Freeplane: si usa per generare nodi, trasformare testo, interrogare API esterne o costruire workflow personalizzati.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |    4  █ |
| 2025 |   35  ███ |
| 2024 |   24  ██ |
| 2023 |   27  ███ |
| 2022 |   52  █████ |
| 2021 |   53  █████ |
| 2020 |   50  █████ |
| 2019 |   65  ███████ |
| 2018 |  150  ████████████████ |
| 2017 |   55  ██████ |
| 2016 |   78  ████████ |
| 2015 |   86  █████████ |
| 2014 |   74  ████████ |
| 2013 |   90  ██████████ |
| 2012 |   76  ████████ |
| 2011 |  198  ████████████████████ |
| 2010 |  149  ████████████████ |
| 2009 |   24  ██ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 620 | 48% |
| feature | 286 | 22% |
| fix | 190 | 15% |
| api_change | 74 | 6% |
| refactor | 70 | 5% |
| build | 29 | 2% |
| docs | 18 | 1% |
| test | 3 | 0% |

### Top contributor

- **Dimitry Polivaev** — 546 commit
- **boercher** — 243 commit
- **Volker Boerchers** — 160 commit
- **dpolivaev** — 146 commit
- **dpolivaev@users.sourceforge.net** — 61 commit
- **Felix Natter** — 48 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, scrip | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |
| 2026-02-20 | `api_change` | 2026-02-20-expose-styles-ai-tools Expose styles in AI tools and unify list API | [5432e96f](https://github.com/freeplane/freeplane/commit/5432e96f9c9492b88242fcbaec14455da46f731b) |
| 2025-09-01 | `feature` | Issue #2641 New script action is difficult to find in script editor | [4410f359](https://github.com/freeplane/freeplane/commit/4410f359d08e95059a2b8315fa45579689dbbcca) |
| 2025-08-03 | `feature` | Fix UI component references for UI-follows-focus architecture | [44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf) |
| 2025-07-12 | `feature` | Scripting API: deprecate StrikedThrough, add Strikethrough | [ee27a149](https://github.com/freeplane/freeplane/commit/ee27a14956ce8172aa22bd3bfcb9e8ad19085a76) |
| 2025-07-12 | `fix` | Scripting API: rename underlined to underline | [67ea65c1](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2) |
| 2025-07-05 | `feature` | Issue #2560 add underline | [b48e383d](https://github.com/freeplane/freeplane/commit/b48e383db28b2952d37152d5e667c4c2c53d996b) |
| 2025-06-20 | `api_change` | Improve Bookmark API | [c7cf203a](https://github.com/freeplane/freeplane/commit/c7cf203af1717dfd3a21c45b6b716f6f1e5b3e00) |
| 2025-06-20 | `feature` | Add open methods to NodeBookmark API and implement in NodeBookmarkProxy class | [5ac0a772](https://github.com/freeplane/freeplane/commit/5ac0a7720f05a438e951c1f3a3dc8a950a13bee9) |
| 2025-06-19 | `fix` | fix GroovyStaticImports in javadoc | [e29da9c1](https://github.com/freeplane/freeplane/commit/e29da9c16216188cd6f64c17569c2e22e9a1e8a2) |
| 2025-06-19 | `feature` | do not add values to API mind map, they mostly have no meaning | [89dbe0e5](https://github.com/freeplane/freeplane/commit/89dbe0e573aefecdc4bfbc9825351a228761a412) |
| 2025-06-19 | `feature` | add GroovyStaticImports to javadoc | [9cb7d12e](https://github.com/freeplane/freeplane/commit/9cb7d12e2888112424acfd208a40f158b370986c) |
| 2025-06-19 | `api_change` | include GroovyStaticImports in API generation | [7bb11c94](https://github.com/freeplane/freeplane/commit/7bb11c94294edbfe485bfa080a2911b0b57b2b0e) |
| 2025-06-19 | `feature` | Add utility methods and documentation to Enhance and document GroovyStaticImport | [7d354270](https://github.com/freeplane/freeplane/commit/7d3542700f3fcc94449e95d436c37f794fde382d) |
| 2025-06-15 | `feature` | Implement bookmark functionality in Freeplane node api | [0b3743d5](https://github.com/freeplane/freeplane/commit/0b3743d5fd6f27f70eb7c8fd20ba67879b89bfa9) |
| 2025-06-15 | `api_change` | Improve internal scrolling API | [4dfbb7be](https://github.com/freeplane/freeplane/commit/4dfbb7be38f7adf3b6ee1110aed8a3384ac5873e) |
| 2025-06-15 | `api_change` | align Numbering API with API for other formatting properties | [54bf4ef7](https://github.com/freeplane/freeplane/commit/54bf4ef747fe37ec18bfcf9b4a3230a54d3b79fa) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy sc | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-01-04 | `fix` | Issue #2190 Fix script exception handling | [c5c1ff61](https://github.com/freeplane/freeplane/commit/c5c1ff6100cc43d5fdad1d9631ef90700e475cbc) |
| 2024-08-24 | `feature` | Rework tag categories, add option to show tag categories | [ccea2b9d](https://github.com/freeplane/freeplane/commit/ccea2b9dcc98113f3707c893144e7f9fef7f6a92) |

---

## Framework OSGi
**Chiave modulo:** `freeplane_framework`  
**Commit totali:** 669

> Il **framework OSGi** che gestisce il ciclo di vita dei plugin: caricamento, dipendenze, isolamento dei moduli. È la spina dorsale dell'architettura modulare di Freeplane.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |   12  ██ |
| 2025 |   21  ████ |
| 2024 |   38  ███████ |
| 2023 |   19  ███ |
| 2022 |   31  ██████ |
| 2021 |   34  ██████ |
| 2020 |   26  █████ |
| 2019 |   21  ████ |
| 2018 |   49  █████████ |
| 2017 |   27  █████ |
| 2016 |   51  ██████████ |
| 2015 |   29  █████ |
| 2014 |   34  ██████ |
| 2013 |   47  █████████ |
| 2012 |   39  ███████ |
| 2011 |   27  █████ |
| 2010 |  107  ████████████████████ |
| 2009 |   57  ███████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 304 | 45% |
| build | 201 | 30% |
| feature | 71 | 11% |
| fix | 65 | 10% |
| api_change | 10 | 1% |
| refactor | 9 | 1% |
| docs | 6 | 1% |
| test | 3 | 0% |

### Top contributor

- **Dimitry Polivaev** — 297 commit
- **dpolivaev** — 211 commit
- **dpolivaev@users.sourceforge.net** — 49 commit
- **Felix Natter** — 40 commit
- **boercher** — 20 commit
- **Dimitry** — 10 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-02-09 | `fix` | fix windows installer script | [b6ce1731](https://github.com/freeplane/freeplane/commit/b6ce1731e2e8536dfcefd36c5162bb176b834cbf) |
| 2025-08-10 | `feature` | Fix Gradle 9.0 test discovery strictness | [7098c15e](https://github.com/freeplane/freeplane/commit/7098c15e87743baf55f6b44f419b5695a74bfebd) |
| 2025-08-10 | `fix` | Fix Gradle 9.0.0 compatibility issues | [bad0e0cd](https://github.com/freeplane/freeplane/commit/bad0e0cddbfc0fae7824d19acc61687d4294aebf) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy sc | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-02-28 | `fix` | fix package name | [bd746d1f](https://github.com/freeplane/freeplane/commit/bd746d1faaa25bf13d591a4a17f2712f5c7b5a07) |
| 2024-11-30 | `feature` | create 2 windows distributions | [9ca50c55](https://github.com/freeplane/freeplane/commit/9ca50c55feb5deba9d4e0fe7ca8c708d8ce32898) |
| 2024-11-24 | `fix` | fix encoding | [0ed3dcad](https://github.com/freeplane/freeplane/commit/0ed3dcad056e057d253a4374380171da19780bca) |
| 2024-11-24 | `feature` | Add new options to freeplane.bat | [1db8e0c5](https://github.com/freeplane/freeplane/commit/1db8e0c56229b04246b600060f738726fba5358c) |
| 2024-08-24 | `fix` | Fix exclusion pattern for l4j.ini files in windown installer | [4e9a5abf](https://github.com/freeplane/freeplane/commit/4e9a5abf528b7ced092782bc8ed7f1fd7e73c5e3) |
| 2024-08-17 | `fix` | fix version number | [64602f40](https://github.com/freeplane/freeplane/commit/64602f406af00c3893d1dd7529022dd61aa5f88b) |
| 2024-02-02 | `fix` | fix eclipse configuration in gradle | [ce7cf789](https://github.com/freeplane/freeplane/commit/ce7cf789de677eb858829b58f74785fbd7421936) |
| 2024-01-22 | `fix` | fix launcher (revert) | [fb719bb4](https://github.com/freeplane/freeplane/commit/fb719bb4dc30eef6eac669941192b8c660b209e3) |
| 2024-01-22 | `fix` | fix launcher configuration | [e653bc1e](https://github.com/freeplane/freeplane/commit/e653bc1ee2309ccff82334d44cabddf798e20f99) |
| 2024-01-19 | `fix` | fix java 8 version number | [0604b4ec](https://github.com/freeplane/freeplane/commit/0604b4ec408426d0a1bbc59a150add1a77f98e5e) |
| 2024-01-17 | `feature` | Support running Freeplane under Java 8 and Java 11 on Windows | [8fe2aa54](https://github.com/freeplane/freeplane/commit/8fe2aa54115a5805935fec5f47c06141b84e7f29) |
| 2023-10-15 | `feature` | update launch4j config files to support the latest launch4j version 3.50 | [676e7b6d](https://github.com/freeplane/freeplane/commit/676e7b6d63d76b3562071fedee26210b69fba6bb) |
| 2022-10-29 | `feature` | add permission java.awt.AWTPermission "watchMousePointer" | [c725f317](https://github.com/freeplane/freeplane/commit/c725f31740618b65c9ebd4bf7a5f191a64cae726) |
| 2022-09-11 | `feature` | add url parameter architecture=x86-64-bit | [b7d1a428](https://github.com/freeplane/freeplane/commit/b7d1a428b290d0819a67d512b43c708a49232d8d) |
| 2022-03-27 | `feature` | add missing bracket | [46551618](https://github.com/freeplane/freeplane/commit/465516188f4de4789cf3f0626f6f4971d0f46fd6) |
| 2022-03-27 | `feature` | create windows distribution containing java-runtime | [07b76b95](https://github.com/freeplane/freeplane/commit/07b76b95b6711a5467fcf13bebd270b175e9475f) |

---

## LaTeX
**Chiave modulo:** `freeplane_plugin_latex`  
**Commit totali:** 210

> Integra il rendering **LaTeX/MathJax** nei nodi. Indispensabile per chi usa Freeplane in ambito scientifico, matematico o accademico per inserire equazioni e notazione formale nelle mappe.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |    1  █ |
| 2025 |    5  █████ |
| 2024 |    2  ██ |
| 2023 |    2  ██ |
| 2022 |    3  ███ |
| 2021 |   23  ████████████████████ |
| 2020 |    3  ███ |
| 2019 |   10  ██████████ |
| 2018 |    4  ████ |
| 2017 |    5  █████ |
| 2016 |    8  ████████ |
| 2015 |   14  ██████████████ |
| 2014 |   24  ████████████████████ |
| 2013 |   11  ███████████ |
| 2012 |   30  ████████████████████ |
| 2011 |   20  ████████████████████ |
| 2010 |   32  ████████████████████ |
| 2009 |   13  █████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 125 | 60% |
| feature | 30 | 14% |
| fix | 23 | 11% |
| build | 16 | 8% |
| refactor | 14 | 7% |
| api_change | 1 | 0% |
| docs | 1 | 0% |

### Top contributor

- **Dimitry Polivaev** — 60 commit
- **dpolivaev** — 58 commit
- **Felix Natter** — 50 commit
- **dpolivaev@users.sourceforge.net** — 25 commit
- **boercher** — 5 commit
- **Stefan** — 5 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-04-04 | `fix` | Issue #2867 fix NPE | [b27609a2](https://github.com/freeplane/freeplane/commit/b27609a277783114a3b12cbe51385075c54d2023) |
| 2025-09-24 | `fix` | Issue #2682 Fix class cast exception | [3de9d1e2](https://github.com/freeplane/freeplane/commit/3de9d1e2cedcb46254e6999d3ee8ad32a67e491c) |
| 2025-07-23 | `fix` | Fix latex rendered width, font and colors | [c9e842a5](https://github.com/freeplane/freeplane/commit/c9e842a5781f3b9389fb68f48f3a4ca157848b46) |
| 2025-05-18 | `feature` | Better support input method events | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2021-06-03 | `fix` | fix editor background colors on VAqua | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-05-13 | `fix` | Fix jsyntaxpane package import | [fd935f1f](https://github.com/freeplane/freeplane/commit/fd935f1f882564cecd9d3998e2f710e406daaa82) |
| 2021-02-05 | `fix` | fix latex note editor | [aaac8d35](https://github.com/freeplane/freeplane/commit/aaac8d35f171aa6eeba7d4a80dbde7e20cca4f08) |
| 2021-01-18 | `fix` | fix LatexRenderer | [7bb3b7d5](https://github.com/freeplane/freeplane/commit/7bb3b7d56515eca9781bdf3a563c62c27a1d0622) |
| 2021-01-16 | `fix` | fix note views in maps | [b72ceda3](https://github.com/freeplane/freeplane/commit/b72ceda36165440f7e142cc9ea89b11cf4eb8c39) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |
| 2020-12-24 | `fix` | make latex editor non modal and fix blocking editor treatment | [a6f20816](https://github.com/freeplane/freeplane/commit/a6f208166ce4b6dfe06327c0191a725bf6cc2048) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2019-10-18 | `fix` | fix plugin bundle imports | [bf81ff64](https://github.com/freeplane/freeplane/commit/bf81ff641d0a30e86271969f16da235483aa7b2e) |
| 2019-09-14 | `feature` | Support dark mode | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2017-12-08 | `feature` | add testCompile dependencies | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-09-17 | `feature` | add dependencies on jlatex-math fonts | [820920af](https://github.com/freeplane/freeplane/commit/820920afa2c1556250ef8fbcb6990d7ab5703c57) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because O | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2015-12-31 | `fix` | Fix latex and formula editors | [3d92c063](https://github.com/freeplane/freeplane/commit/3d92c063dd0a69ff6ec6065577406d75f84f8e68) |

---

## Formula
**Chiave modulo:** `freeplane_plugin_formula`  
**Commit totali:** 187

> Aggiunge il supporto alle **formule** nei nodi (sintassi simile a spreadsheet). Consente calcoli automatici, riferimenti ad altri nodi e aggregazioni, trasformando Freeplane in uno strumento di analisi dati visuale.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2025 |    3  ███ |
| 2024 |    2  ██ |
| 2023 |    4  ████ |
| 2022 |    6  ██████ |
| 2021 |   17  █████████████████ |
| 2020 |    3  ███ |
| 2019 |   10  ██████████ |
| 2018 |   37  ████████████████████ |
| 2017 |    4  ████ |
| 2016 |    5  █████ |
| 2015 |   10  ██████████ |
| 2014 |   15  ███████████████ |
| 2013 |    6  ██████ |
| 2012 |   13  █████████████ |
| 2011 |   27  ████████████████████ |
| 2010 |   25  ████████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 114 | 61% |
| feature | 25 | 13% |
| fix | 25 | 13% |
| refactor | 14 | 7% |
| build | 8 | 4% |
| api_change | 1 | 1% |

### Top contributor

- **Dimitry Polivaev** — 91 commit
- **dpolivaev** — 25 commit
- **dpolivaev@users.sourceforge.net** — 24 commit
- **Felix Natter** — 22 commit
- **boercher** — 21 commit
- **Hartmut Goebel** — 2 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2025-05-18 | `feature` | Better support input method events | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2025-04-04 | `fix` | fix NPE | [5b8d5f72](https://github.com/freeplane/freeplane/commit/5b8d5f72f48eb6ee5fda233615eb2a44cd56b485) |
| 2024-08-14 | `fix` | Simplify and fix ClassCastException | [4a01a75a](https://github.com/freeplane/freeplane/commit/4a01a75a2e75b4ca44f1efbad0a5c90264ac8de1) |
| 2024-06-21 | `fix` | fix formula result refresh for nodes accessing clones | [66effa94](https://github.com/freeplane/freeplane/commit/66effa9440f7d0f5e1666d5b94c48bf45be0232f) |
| 2022-11-24 | `feature` | Issue  #843 conditional formating script filter rules are not applied to the new | [8f17ede4](https://github.com/freeplane/freeplane/commit/8f17ede4e786720796ad7c4feafb8d5dd97072c1) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2021-06-03 | `fix` | fix editor background colors on VAqua | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-03-07 | `feature` | Option to enforce modal editor dialogs | [e30072b5](https://github.com/freeplane/freeplane/commit/e30072b59691a0cfe8393094c8e09bf0d3c976a5) |
| 2021-01-17 | `fix` | fix rendering | [0c305a86](https://github.com/freeplane/freeplane/commit/0c305a867024a10fc23a8d8d07572fd669f419e8) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |
| 2020-12-24 | `fix` | make latex editor non modal and fix blocking editor treatment | [a6f20816](https://github.com/freeplane/freeplane/commit/a6f208166ce4b6dfe06327c0191a725bf6cc2048) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2019-09-28 | `feature` | Add new properties  to connector API : dashArray, opacity, width, labelFontFamil | [f4c86c81](https://github.com/freeplane/freeplane/commit/f4c86c8129390c482d1823494186137497d77f63) |
| 2019-09-14 | `feature` | Support dark mode | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2019-08-10 | `feature` | Add NodeChangeListener to Freeplane API | [746e83e0](https://github.com/freeplane/freeplane/commit/746e83e0565e3b37e24ea881802e16a2ed768b4b) |
| 2018-12-11 | `fix` | fix exception trace pane width in formula editor | [66415885](https://github.com/freeplane/freeplane/commit/6641588575f68e94533431515e9a81ddb2003df8) |
| 2018-11-25 | `feature` | Support selection of multiple cells in attribute tables | [3a90c16b](https://github.com/freeplane/freeplane/commit/3a90c16bdb0bc7269676dc6897d76a04f5d87cc8) |
| 2018-10-16 | `fix` | fix #2616 Reference from other maps v. 1.7.2_04 | [27e3de61](https://github.com/freeplane/freeplane/commit/27e3de6156813702aa5bccc6e5b6835be86f0982) |
| 2018-10-15 | `fix` | Fix docu and names | [82aecb58](https://github.com/freeplane/freeplane/commit/82aecb5843e6667536ba8ee0af2dba85eb060d46) |

---

## API pubblica
**Chiave modulo:** `freeplane_api`  
**Commit totali:** 173

> L'**API pubblica** di Freeplane: le interfacce e le classi esposte agli sviluppatori di plugin e script. Definisce il contratto stabile tra il core e le estensioni esterne.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |    4  ██ |
| 2025 |   16  ████████ |
| 2024 |   11  █████ |
| 2023 |   25  ████████████ |
| 2022 |   43  ████████████████████ |
| 2021 |   17  ████████ |
| 2020 |   12  ██████ |
| 2019 |   15  ███████ |
| 2018 |   30  ███████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 62 | 36% |
| feature | 52 | 30% |
| api_change | 26 | 15% |
| fix | 19 | 11% |
| refactor | 8 | 5% |
| docs | 4 | 2% |
| build | 2 | 1% |

### Top contributor

- **Dimitry Polivaev** — 144 commit
- **macmarrum** — 15 commit
- **EdoFro** — 3 commit
- **Leonidas Spyropoulos** — 2 commit
- **Beniamin Kalinowski** — 2 commit
- **dimitry** — 2 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2026-03-16 | `feature` | Add javadoc for tag category API | [3ae0781b](https://github.com/freeplane/freeplane/commit/3ae0781b8af6f779b772eaf65236e773149e7432) |
| 2026-03-15 | `feature` | expose-node-tags-to-ai-tools: implement shared tag category access for UI, scrip | [b4726030](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51) |
| 2025-07-12 | `feature` | Scripting API: deprecate StrikedThrough, add Strikethrough | [ee27a149](https://github.com/freeplane/freeplane/commit/ee27a14956ce8172aa22bd3bfcb9e8ad19085a76) |
| 2025-07-12 | `fix` | Scripting API: rename underlined to underline | [67ea65c1](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2) |
| 2025-07-05 | `feature` | Issue #2560 add underline | [b48e383d](https://github.com/freeplane/freeplane/commit/b48e383db28b2952d37152d5e667c4c2c53d996b) |
| 2025-06-22 | `fix` | Issue #2423 Fix paths containing RTL letters in folder and file names. | [708df2e1](https://github.com/freeplane/freeplane/commit/708df2e12c3e7971ffa9e9d1128edb78e8b85be7) |
| 2025-06-20 | `api_change` | Improve Bookmark API | [c7cf203a](https://github.com/freeplane/freeplane/commit/c7cf203af1717dfd3a21c45b6b716f6f1e5b3e00) |
| 2025-06-20 | `feature` | Add open methods to NodeBookmark API and implement in NodeBookmarkProxy class | [5ac0a772](https://github.com/freeplane/freeplane/commit/5ac0a7720f05a438e951c1f3a3dc8a950a13bee9) |
| 2025-06-15 | `feature` | Implement bookmark functionality in Freeplane node api | [0b3743d5](https://github.com/freeplane/freeplane/commit/0b3743d5fd6f27f70eb7c8fd20ba67879b89bfa9) |
| 2025-06-15 | `api_change` | align Numbering API with API for other formatting properties | [54bf4ef7](https://github.com/freeplane/freeplane/commit/54bf4ef747fe37ec18bfcf9b4a3230a54d3b79fa) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy sc | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2025-05-09 | `fix` | fix layout | [36a31464](https://github.com/freeplane/freeplane/commit/36a31464e13ec59d108452aeec3e45e1aae8c714) |
| 2024-05-09 | `feature` | add API methods and filters for tag categories | [b1ee9533](https://github.com/freeplane/freeplane/commit/b1ee9533bb8073270a365b1883c77e472e96f5f1) |
| 2024-05-09 | `feature` | rename methods and parameters in Tags scripting API | [0f8d2842](https://github.com/freeplane/freeplane/commit/0f8d2842aa2bb432ea07d390cb9f8c0730e93dd7) |
| 2024-04-04 | `feature` | Add methods supporting tags to Freeplane API | [53ca172d](https://github.com/freeplane/freeplane/commit/53ca172d140794625a4d3b4fa2c5ac01a94738fb) |
| 2024-02-18 | `feature` | extend API: add get/set for followed map and associated template | [574a4f2e](https://github.com/freeplane/freeplane/commit/574a4f2edbb06a5b8b78a873dc58feb8cf028e57) |
| 2023-11-24 | `feature` | new api method: mindMap.copyUserStylesFrom(...) (#1541) | [8d8c71a0](https://github.com/freeplane/freeplane/commit/8d8c71a04e1ad0b141f1e8e87ecebd2aeb49d6ef) |
| 2023-10-29 | `feature` | API changes (node's border and edge) (#1355) | [2a803599](https://github.com/freeplane/freeplane/commit/2a80359962a8ea7b3aa98caa760dd781e7ffd5c3) |
| 2023-10-03 | `feature` | wip right-to-left text writing direction support | [42f9c353](https://github.com/freeplane/freeplane/commit/42f9c35356f5dd6f9550bcf08b5654775ad5d659) |
| 2023-10-02 | `feature` | Add horizontal text alignment to API | [c54d215e](https://github.com/freeplane/freeplane/commit/c54d215e9760368c013203dd3232124c95dd7863) |

---

## SVG
**Chiave modulo:** `freeplane_plugin_svg`  
**Commit totali:** 159

> Supporto per immagini e grafici **SVG** embedded nei nodi. Permette di arricchire le mappe con grafica vettoriale scalabile e di visualizzare diagrammi generati da script.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2025 |    2  ██ |
| 2024 |    5  █████ |
| 2023 |    2  ██ |
| 2022 |    6  ██████ |
| 2021 |   11  ███████████ |
| 2020 |    4  ████ |
| 2019 |   12  ████████████ |
| 2018 |   13  █████████████ |
| 2017 |    8  ████████ |
| 2016 |    7  ███████ |
| 2015 |   11  ███████████ |
| 2014 |   25  ████████████████████ |
| 2013 |    6  ██████ |
| 2012 |    4  ████ |
| 2011 |    9  █████████ |
| 2010 |   17  █████████████████ |
| 2009 |   17  █████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 87 | 55% |
| fix | 30 | 19% |
| build | 16 | 10% |
| refactor | 13 | 8% |
| feature | 13 | 8% |

### Top contributor

- **Dimitry Polivaev** — 60 commit
- **dpolivaev** — 38 commit
- **Felix Natter** — 27 commit
- **dpolivaev@users.sourceforge.net** — 14 commit
- **worldbright** — 7 commit
- **Blair Archibald** — 4 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2025-04-28 | `fix` | fix typo | [a9451631](https://github.com/freeplane/freeplane/commit/a945163128013a1f7889b007ed17b7da8f1fcecd) |
| 2024-11-02 | `fix` | Update and fix dependency versions for apache batik and fop | [3b3475ab](https://github.com/freeplane/freeplane/commit/3b3475ab130d8e66202d91ed7069188e7037be1c) |
| 2024-07-27 | `fix` | Do not change look and feel during export to SVG/PDF | [93af3ff1](https://github.com/freeplane/freeplane/commit/93af3ff1a5ed81e05ed29ac7889e0035586c35db) |
| 2024-03-05 | `feature` | add pdf export to codeexplorer | [0e97fb58](https://github.com/freeplane/freeplane/commit/0e97fb5833cc4cb6316957294d2eac0b7ca2f01a) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-01-07 | `feature` | Replace darcula LAF by supported Flat Darcula LAF and add Flat Light LAF | [40eb7bdf](https://github.com/freeplane/freeplane/commit/40eb7bdfd07db8ecfd5424ba4f765be268a7428e) |
| 2021-08-20 | `fix` | fix pdf export removing font search un user directory performed by fop | [1cd87dfe](https://github.com/freeplane/freeplane/commit/1cd87dfef08fb030b4a3acf7dd8c0c74c0726d4c) |
| 2021-03-21 | `feature` | Add warning for first PDF export | [7a921d80](https://github.com/freeplane/freeplane/commit/7a921d80cd7a2f286968a9c1154a3b221f13c48a) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-02-22 | `fix` | Fix SVG backgrounds | [02b5f924](https://github.com/freeplane/freeplane/commit/02b5f924779846aff5dd9bfcf7c126b84a55dbcb) |
| 2020-02-21 | `fix` | fix svg images | [65d1fe0f](https://github.com/freeplane/freeplane/commit/65d1fe0f7cb233dc6d1baf30f394d606723ef8c0) |
| 2019-12-14 | `fix` | Workaround for fop 2.4 bug https://issues.apache.org/jira/browse/FOP-2896 | [f0c2c90b](https://github.com/freeplane/freeplane/commit/f0c2c90b084b5c1d626caa83f645c84491f22ebb) |
| 2019-12-14 | `fix` | fix fop 2.4 dependency | [a863367b](https://github.com/freeplane/freeplane/commit/a863367bc951e76366dc088d6b39ed46cda68b49) |
| 2019-09-21 | `fix` | Fix SVG and PDF export with Darcula LaF | [13e03dbf](https://github.com/freeplane/freeplane/commit/13e03dbfd4d1bf1e17c9658e9539db0f465d18c4) |
| 2018-12-24 | `fix` | fix svg in previews and tooltips | [971c4ae4](https://github.com/freeplane/freeplane/commit/971c4ae4df0bfab9cdbad63a398c8df55d6da26b) |
| 2018-02-25 | `fix` | Fix embedded text in PDF export | [17ddd648](https://github.com/freeplane/freeplane/commit/17ddd648d920febcb610b35c98fa2c7297bd47e0) |
| 2017-12-08 | `feature` | add testCompile dependencies | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-10-14 | `fix` | fix batik export of gradients in svgSalamander's SVG icons | [2e72152f](https://github.com/freeplane/freeplane/commit/2e72152f360acdbcda610e5d2ef9f893c02674b1) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because O | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |

---

## Add-ons
**Chiave modulo:** `addons`  
**Commit totali:** 157

> **Add-on di terze parti** distribuiti tramite il repository ufficiale. Pacchetti installabili dall'utente che estendono Freeplane senza modificare il core.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2025 |    3  █ |
| 2023 |    3  █ |
| 2022 |    4  ██ |
| 2021 |    6  ███ |
| 2020 |   11  █████ |
| 2019 |    4  ██ |
| 2018 |    5  ██ |
| 2017 |    2  █ |
| 2016 |   15  ███████ |
| 2015 |   12  ██████ |
| 2014 |   13  ██████ |
| 2013 |   20  ██████████ |
| 2012 |    7  ███ |
| 2011 |   52  ████████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 68 | 43% |
| feature | 60 | 38% |
| fix | 17 | 11% |
| refactor | 9 | 6% |
| build | 2 | 1% |
| docs | 1 | 1% |

### Top contributor

- **Dimitry Polivaev** — 47 commit
- **boercher** — 45 commit
- **Volker Boerchers** — 33 commit
- **dpolivaev** — 13 commit
- **seb4stien** — 7 commit
- **Felix Natter** — 3 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2025-08-03 | `feature` | Fix UI component references for UI-follows-focus architecture | [44056f66](https://github.com/freeplane/freeplane/commit/44056f668ebe714e8c04e8834f8b902bb5f85fbf) |
| 2025-05-24 | `feature` | Issue #2473 Add JFileChooser wrapper to fix FlatLaf security issues in Groovy sc | [05c2e755](https://github.com/freeplane/freeplane/commit/05c2e755dc58b0baf0515cde3cce7a70ad2da0f3) |
| 2021-01-07 | `feature` | introduce interface INodeDuplicator and add operation duplicate on nodes | [63fca871](https://github.com/freeplane/freeplane/commit/63fca871c8305e7418d15443033fced1f40dc2c8) |
| 2020-10-24 | `feature` | #2837 Add-on's jar file removed when upgrading | [3a0e0f2f](https://github.com/freeplane/freeplane/commit/3a0e0f2fe14d29eae423c61745cc705e64c0918a) |
| 2020-07-04 | `feature` | #2796 Add-on deinstallation fails to delete jar | [de3c82e8](https://github.com/freeplane/freeplane/commit/de3c82e86d75d5c545a1fdf3e5ebf5d88fdfcf3d) |
| 2020-06-05 | `fix` | Fix slow JFileChooser for windows by not using Windows icons | [80be70f5](https://github.com/freeplane/freeplane/commit/80be70f5fcf55c2fcdc29e071ab706fb40a4c9be) |
| 2020-03-06 | `fix` | fix dialog icon | [df67c1fb](https://github.com/freeplane/freeplane/commit/df67c1fb597b504cee6dd68db29461c7809c8ced) |
| 2020-02-11 | `feature` | rename methods, add method HtmlUtils.textToHTML | [adcdd4ac](https://github.com/freeplane/freeplane/commit/adcdd4ac97e67df07fc788e4882efbd43fe7f9fc) |
| 2020-01-27 | `fix` | #2726 fix manage addons dialog icon | [66543b82](https://github.com/freeplane/freeplane/commit/66543b824c040b2c3e20b5ad6e9d12e2b9c0a5cd) |
| 2019-09-28 | `fix` | Fix table row heights after font scaling | [15384981](https://github.com/freeplane/freeplane/commit/15384981d8172c23ee2004eb05d286ba07802dde) |
| 2019-02-15 | `fix` | fix NPE | [c45e067c](https://github.com/freeplane/freeplane/commit/c45e067c39210331320e852ddd628dbd4d84903b) |
| 2018-12-31 | `feature` | Fix #2386 Special characters in add-on translations wrongly displayed | [d3fa8d97](https://github.com/freeplane/freeplane/commit/d3fa8d97c65f75ca8c09e548622989a09ee52730) |
| 2018-12-19 | `feature` | Fix for #2386 Special characters in add-on translations wrongly displayed | [c9b7a8a2](https://github.com/freeplane/freeplane/commit/c9b7a8a2b4899e3a2d79bcf71a9bf12c4a1cbdb5) |
| 2016-12-29 | `feature` | add tools svgs | [0a27a7fd](https://github.com/freeplane/freeplane/commit/0a27a7fd6ae92ebef92adae77b0e37a508f33949) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | [096fbd1f](https://github.com/freeplane/freeplane/commit/096fbd1f116b38edc7648618cf2c5e45bcd7b536) |
| 2016-11-06 | `fix` | fix ShowPreferencesAction for mac | [2e38286e](https://github.com/freeplane/freeplane/commit/2e38286e3b35f58e558c329073a1eba35640d9c7) |
| 2016-08-18 | `feature` | fix missing parseFreeplaneVersion() | [b89c27a9](https://github.com/freeplane/freeplane/commit/b89c27a9739565de6a256623afc6c2493aa4521d) |
| 2016-04-25 | `feature` | avoid all translation warnings for add-ons | [6a3f1dd0](https://github.com/freeplane/freeplane/commit/6a3f1dd09b19dcbd1a69bcb21ccfead70e276e0f) |
| 2016-04-24 | `feature` | revert ca85480cd4561bf74d2d5efa50d93b40b2f1318c (add-on translations) | [7b27e63d](https://github.com/freeplane/freeplane/commit/7b27e63d83d579aa82e6475a7b0b4528c436c943) |
| 2016-04-24 | `feature` | avoid all translation warnings for add-ons | [ca85480c](https://github.com/freeplane/freeplane/commit/ca85480cd4561bf74d2d5efa50d93b40b2f1318c) |

---

## Bug Report
**Chiave modulo:** `freeplane_plugin_bugreport`  
**Commit totali:** 136

> Strumento interno per la **segnalazione bug**: raccoglie informazioni di sistema, log e contesto della mappa per facilitare il reporting agli sviluppatori.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2024 |    6  ██████ |
| 2023 |    4  ████ |
| 2022 |    7  ███████ |
| 2021 |    2  ██ |
| 2020 |    3  ███ |
| 2019 |    8  ████████ |
| 2018 |    9  █████████ |
| 2017 |    4  ████ |
| 2016 |   11  ███████████ |
| 2015 |    8  ████████ |
| 2014 |   12  ████████████ |
| 2013 |    4  ████ |
| 2012 |   10  ██████████ |
| 2011 |    9  █████████ |
| 2010 |   18  ██████████████████ |
| 2009 |   21  ████████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 72 | 53% |
| fix | 26 | 19% |
| feature | 14 | 10% |
| build | 13 | 10% |
| refactor | 10 | 7% |
| api_change | 1 | 1% |

### Top contributor

- **Dimitry Polivaev** — 54 commit
- **dpolivaev** — 44 commit
- **Felix Natter** — 18 commit
- **dpolivaev@users.sourceforge.net** — 12 commit
- **boercher** — 4 commit
- **Blair Archibald** — 2 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2024-03-05 | `fix` | Generate bug reports only for Freeplane own errors | [d7534fad](https://github.com/freeplane/freeplane/commit/d7534fad09ca3d0fcfad6ffb2e49a6424b1730b3) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-02-27 | `feature` | add null check | [bc1ce11b](https://github.com/freeplane/freeplane/commit/bc1ce11b449a9531c81d8580d414fde218452454) |
| 2022-02-27 | `fix` | Don't submit bug reports related to groovy runtime errors | [510b9eb9](https://github.com/freeplane/freeplane/commit/510b9eb92fe9d2fb79be9e94dc0fd3f6c5f54b47) |
| 2022-02-27 | `fix` | remove file paths from submitted bug reports | [a16efaf5](https://github.com/freeplane/freeplane/commit/a16efaf53193e58e122a7cb0d37b971c7507c3a0) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2019-01-30 | `fix` | fix bug report url | [3150b7fb](https://github.com/freeplane/freeplane/commit/3150b7fb847195fafdd42d11c1b56445f48e6978) |
| 2018-11-24 | `fix` | Do not show bug report dialog in headless mode | [132c472a](https://github.com/freeplane/freeplane/commit/132c472a487468148b51da2525dc7a949e8b6d5a) |
| 2018-08-21 | `feature` | Add "deny" button to quick filter | [a8a1253f](https://github.com/freeplane/freeplane/commit/a8a1253f5b0fbab1a0ecac9f3456a508ca351f8c) |
| 2018-01-27 | `api_change` | Use Icon (interface) instead of SVGIcon or ImageIcon | [9f50b315](https://github.com/freeplane/freeplane/commit/9f50b31569e5724e9929feab8eb2f66610ac7a5e) |
| 2017-12-08 | `feature` | add testCompile dependencies | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-04-02 | `fix` | Fix error bitton icon and size | [98e2422e](https://github.com/freeplane/freeplane/commit/98e2422e4ae4c29534bb02cabc0ba6006a50f560) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because O | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-06-18 | `fix` | Show bug report dialog even in final version if property org.freeplane.plugin.bu | [040b42c3](https://github.com/freeplane/freeplane/commit/040b42c31b1f2e56eef081391219a75327b5a4a4) |
| 2016-04-10 | `fix` | execute bug report submission as privileged action | [11bc0b2e](https://github.com/freeplane/freeplane/commit/11bc0b2e44cfb0b807c96c874dd25d9f5c994fe7) |
| 2016-04-10 | `fix` | Fix some bugs related to security checks | [0ee6aef1](https://github.com/freeplane/freeplane/commit/0ee6aef160140dd19c6c2e71588de8a221751604) |
| 2015-11-28 | `fix` | Fix git revision information | [44e35149](https://github.com/freeplane/freeplane/commit/44e351491102142447dc4d6c2a8b5e70b1d383a5) |
| 2015-11-28 | `fix` | Fix git revision information | [820e67e6](https://github.com/freeplane/freeplane/commit/820e67e6b7fadcdbefbe12fa86bf77f43a530102) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for  | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a mav | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |

---

## OpenMaps
**Chiave modulo:** `freeplane_plugin_openmaps`  
**Commit totali:** 82

> Integrazione con **OpenStreetMap**: permette di visualizzare e agganciare coordinate geografiche ai nodi, utile per mappe concettuali con componente spaziale.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2025 |    2  ██ |
| 2024 |    2  ██ |
| 2023 |    2  ██ |
| 2022 |    3  ███ |
| 2021 |    2  ██ |
| 2020 |    2  ██ |
| 2019 |    7  ███████ |
| 2018 |    2  ██ |
| 2017 |    4  ████ |
| 2016 |    7  ███████ |
| 2015 |    8  ████████ |
| 2014 |   15  ███████████████ |
| 2013 |    1  █ |
| 2012 |   25  ████████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 52 | 63% |
| feature | 12 | 15% |
| fix | 8 | 10% |
| build | 7 | 9% |
| refactor | 2 | 2% |
| test | 1 | 1% |

### Top contributor

- **Dimitry Polivaev** — 28 commit
- **Blair Archibald** — 26 commit
- **Felix Natter** — 26 commit
- **dpolivaev** — 1 commit
- **Beniamin Kalinowski** — 1 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2019-12-13 | `fix` | Fix OpenMapsViewer by setting Freeplane specific user agent | [5d541e27](https://github.com/freeplane/freeplane/commit/5d541e27673112557fcb9dd0f68a52749fea496b) |
| 2017-04-09 | `feature` | inline IconStoreFactory.create() | [16fcbdd5](https://github.com/freeplane/freeplane/commit/16fcbdd5b46e791b3a455ee577c2b05f0bd756f7) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because O | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-01-23 | `fix` | bug #2305 clicking in icon-area does not select node | [ddb73bd9](https://github.com/freeplane/freeplane/commit/ddb73bd9db306cc5078b57a1ad783720db81a590) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for  | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a mav | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-08-31 | `feature` | add IconMouseListener concept for clicks on icons and use it to call openmaps vi | [83e5bd24](https://github.com/freeplane/freeplane/commit/83e5bd24bfe85be7247b05042907554850433527) |
| 2014-07-08 | `feature` | Moved OpenMaps plugin to the new directory structure, couldn't find a maven repo | [7c7bdca9](https://github.com/freeplane/freeplane/commit/7c7bdca9ab49dc012dd5c00ca732131aea0eee99) |
| 2012-10-12 | `feature` | Undo now removes the openMaps data if the last command was a creation. Still nee | [8898b0b9](https://github.com/freeplane/freeplane/commit/8898b0b9e19bf47f192dd68f13fba149cd9f1a38) |
| 2012-09-28 | `fix` | fixed bug in storing the zoom | [40afbeb6](https://github.com/freeplane/freeplane/commit/40afbeb642bb4817efcc80c588c987b6f625d780) |
| 2012-09-23 | `fix` | Fixed bug with multiple NodeHooks being created | [c2288b9a](https://github.com/freeplane/freeplane/commit/c2288b9a3a110abad26d495cf6df7e3168b018b1) |
| 2012-09-23 | `fix` | Various Bug fixes | [c6f9d625](https://github.com/freeplane/freeplane/commit/c6f9d62586c8749d4a762aae2b6ef4e4d27698a5) |
| 2012-09-09 | `feature` | Added new listener for selecting locations (over a loop) | [5b1416d3](https://github.com/freeplane/freeplane/commit/5b1416d3a7e72db9639fecd734ca6ed50e9302f3) |
| 2012-09-08 | `feature` | Added a new controller to allow double click location adding. Switched to Coordi | [004ee3f7](https://github.com/freeplane/freeplane/commit/004ee3f752d4b9e025c9abe67befdd373c37d133) |
| 2012-08-26 | `fix` | Fixed missing OpenMapsNodeHookAction.text bug and overided serveral persistant n | [8d89b703](https://github.com/freeplane/freeplane/commit/8d89b7031513fbdf9332fe494b7edf2868960b03) |

---

## Debug Helper
**Chiave modulo:** `freeplane_debughelper`  
**Commit totali:** 49

> Utilità per il **debug** in sviluppo: strumenti di ispezione dello stato interno, logging avanzato e assistenza agli sviluppatori di plugin.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2025 |    5  █████ |
| 2024 |    3  ███ |
| 2023 |    4  ████ |
| 2022 |    5  █████ |
| 2021 |    7  ███████ |
| 2020 |    7  ███████ |
| 2019 |    4  ████ |
| 2018 |   14  ██████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| fix | 19 | 39% |
| other | 18 | 37% |
| feature | 10 | 20% |
| build | 1 | 2% |
| refactor | 1 | 2% |

### Top contributor

- **Dimitry Polivaev** — 44 commit
- **dimitry** — 2 commit
- **dpolivaev** — 1 commit
- **Beniamin Kalinowski** — 1 commit
- **Amadej Kastelic** — 1 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2025-09-07 | `fix` | outline: fix incorrect content-level indentation by using computed parent-chain  | [c3338a39](https://github.com/freeplane/freeplane/commit/c3338a39ba88f9127febc463ae66923cc506fd96) |
| 2025-08-17 | `fix` | Multiple bug fixes for auxillary component and for startup | [d18cef3d](https://github.com/freeplane/freeplane/commit/d18cef3d0e5e657c131f2b08cf8a9f5fe77baa3c) |
| 2025-08-14 | `feature` | Add option "UI elements follow selected map" true by default | [aefa5f32](https://github.com/freeplane/freeplane/commit/aefa5f3249e0b95449cbc0350e70b892de3586df) |
| 2024-01-22 | `fix` | fix launcher configuration | [e653bc1e](https://github.com/freeplane/freeplane/commit/e653bc1ee2309ccff82334d44cabddf798e20f99) |
| 2023-05-24 | `feature` | Add logging properties to launch configurations | [63bd0533](https://github.com/freeplane/freeplane/commit/63bd0533126d2e13401c54d590fac8f4fbeecdcb) |
| 2022-10-29 | `feature` | add permission java.awt.AWTPermission "watchMousePointer" | [c725f317](https://github.com/freeplane/freeplane/commit/c725f31740618b65c9ebd4bf7a5f191a64cae726) |
| 2022-04-09 | `fix` | fix gradle config | [679dd696](https://github.com/freeplane/freeplane/commit/679dd696cdc7be1d2f6e4a77ef4ea862d2919f5c) |
| 2022-04-09 | `fix` | fix gradle config | [ccb66e26](https://github.com/freeplane/freeplane/commit/ccb66e2650b3828ffbabf7e99195997952c91037) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-02-28 | `fix` | Deprecated properties set to the correct values. | [f10c27bf](https://github.com/freeplane/freeplane/commit/f10c27bffd3d76ac997cff05f1fd4cf1f85df007) |
| 2021-04-18 | `fix` | fix idea run configurations (tested with Intellij CE 2021.1) | [8447fc1c](https://github.com/freeplane/freeplane/commit/8447fc1c24c1f9020bdfec602cef6153c50140b9) |
| 2021-04-16 | `feature` | add exports to non public API used by darcula | [ee7f685c](https://github.com/freeplane/freeplane/commit/ee7f685c3bc06b1d87bc82cce3bac0ab5961e419) |
| 2021-03-21 | `fix` | fix access to com.apple.eawt.Application.requestToggleFullScreen by reflection | [e850d1de](https://github.com/freeplane/freeplane/commit/e850d1de2f907b05f3d9565347d13e17a52095a1) |
| 2021-01-04 | `fix` | fix eclipse dist launch classpaths | [3b194526](https://github.com/freeplane/freeplane/commit/3b194526758c7c29f52413dac52e2733f1f68c16) |
| 2020-12-23 | `fix` | fix freeplane_debughelper for MacOS | [f852e189](https://github.com/freeplane/freeplane/commit/f852e1893a5cd967b78260d57d08e7347e3df08d) |
| 2020-11-14 | `fix` | fix launch configurations | [1f534dad](https://github.com/freeplane/freeplane/commit/1f534dad20c2318f7b3a1487b9cfb7ddbb86f80b) |
| 2020-04-05 | `fix` | fix eclipse freeplane launch configuration | [6c90f1c8](https://github.com/freeplane/freeplane/commit/6c90f1c8a3585883d6cbbe59e598abbf1aa10338) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-01-25 | `fix` | fix gradle configuration | [8c57581b](https://github.com/freeplane/freeplane/commit/8c57581b81fc4aec3c2cdd2f4a461dc405fc5bff) |
| 2020-01-12 | `feature` | Add -Dsun.awt.disablegrab=true to launcher configurations | [becf7c79](https://github.com/freeplane/freeplane/commit/becf7c79c6e9b5886e9521e119d2df4e468b8393) |

---

## JSyntaxPane
**Chiave modulo:** `freeplane_plugin_jsyntaxpane`  
**Commit totali:** 45

> Evidenziazione della **sintassi del codice** nell'editor script interno. Rende più leggibile e modificabile il codice Groovy/script direttamente nell'interfaccia.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2024 |    6  ██████ |
| 2023 |    1  █ |
| 2022 |   11  ███████████ |
| 2021 |    1  █ |
| 2020 |    2  ██ |
| 2019 |    6  ██████ |
| 2018 |    5  █████ |
| 2017 |    6  ██████ |
| 2016 |    5  █████ |
| 2015 |    2  ██ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 18 | 40% |
| fix | 11 | 24% |
| feature | 8 | 18% |
| refactor | 4 | 9% |
| build | 4 | 9% |

### Top contributor

- **Dimitry Polivaev** — 38 commit
- **Felix Natter** — 6 commit
- **dimitry** — 1 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2024-10-06 | `fix` | Fix: register latex content type | [e41960cf](https://github.com/freeplane/freeplane/commit/e41960cfa963473ad4cd773ed8d0a0df668a221c) |
| 2024-04-05 | `feature` | Support sorting tags in tag editor | [fd067897](https://github.com/freeplane/freeplane/commit/fd067897212b829876fe93f4848d789ea51a3372) |
| 2024-04-03 | `feature` | implement tags | [10ac51da](https://github.com/freeplane/freeplane/commit/10ac51da9104bde5fe2a8516f86babf38fb90a20) |
| 2024-02-02 | `fix` | fix eclipse configuration in gradle | [ce7cf789](https://github.com/freeplane/freeplane/commit/ce7cf789de677eb858829b58f74785fbd7421936) |
| 2022-09-24 | `fix` | fix "goto  line" | [83230b8d](https://github.com/freeplane/freeplane/commit/83230b8d21064b7b89f24107c983e3dc0c980f7c) |
| 2022-09-24 | `fix` | fix insets handling | [ddacf51b](https://github.com/freeplane/freeplane/commit/ddacf51b06a49460c0f2839b006e3874685c7594) |
| 2022-09-24 | `fix` | patch SyntaxPane | [9c3e102d](https://github.com/freeplane/freeplane/commit/9c3e102d8dee4b65cb28eeb262b634995556b544) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-01-14 | `feature` | support dark themes in syntax editor | [eb4166a7](https://github.com/freeplane/freeplane/commit/eb4166a7612d80849365d13cff940940fab72e09) |
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2018-07-21 | `fix` | fix memory leak | [7b71ff09](https://github.com/freeplane/freeplane/commit/7b71ff098d25ff64ac4a097aea251e7c1485a1c8) |
| 2018-04-24 | `fix` | fix #2586 by porting https://github.com/nordfalk/jsyntaxpane change to the Debia | [5e72a474](https://github.com/freeplane/freeplane/commit/5e72a474d5905a6b4d3cd4d77e16f033726041aa) |
| 2017-12-08 | `feature` | add testCompile dependencies | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-03-21 | `fix` | fix warning | [4ba02411](https://github.com/freeplane/freeplane/commit/4ba0241152b219d91baf18858a6f200d3c2576d4) |
| 2017-03-19 | `fix` | fix warning | [77dd6fec](https://github.com/freeplane/freeplane/commit/77dd6fec1e0a13d38e8bde9fe817c1fd80ff386c) |
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because O | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-10-16 | `fix` | fix warning including a break statement in switch case | [475a8d27](https://github.com/freeplane/freeplane/commit/475a8d275c08d5e8bc2880b94e20ac35dfde435d) |
| 2015-04-07 | `feature` | add gradle task for latex.flex->LaTeXLexer.java (for use with srcpure) | [b5500710](https://github.com/freeplane/freeplane/commit/b55007106640d9b3df295dfdc5145498bae71f0d) |

---

## Markdown
**Chiave modulo:** `freeplane_plugin_markdown`  
**Commit totali:** 37

> Rendering **Markdown** nel pannello note dei nodi. Consente di scrivere note ricche (titoli, grassetti, liste, codice) in sintassi standard Markdown invece di HTML.

### Attività per anno

| Anno | Commit |
|------|--------|
| 2026 |    1  █ |
| 2025 |    7  ███████ |
| 2024 |    1  █ |
| 2023 |    1  █ |
| 2022 |    3  ███ |
| 2021 |   24  ████████████████████ |

### Tipi di modifica

| Categoria | Commit | % |
|-----------|--------|---|
| other | 25 | 68% |
| feature | 6 | 16% |
| fix | 5 | 14% |
| refactor | 1 | 3% |

### Top contributor

- **Dimitry Polivaev** — 33 commit
- **macmarrum** — 3 commit
- **dimitry** — 1 commit

### Commit rilevanti (ultimi 20 tra feature/fix/api)

| Data | Tipo | Descrizione | Hash |
|------|------|-------------|------|
| 2025-05-18 | `feature` | Better support input method events | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2025-01-06 | `feature` | Issue #2082 add PlantUML support to Markdown | [e602267e](https://github.com/freeplane/freeplane/commit/e602267e07b2287b7a9e84c5503887faf732c6bd) |
| 2023-07-21 | `fix` | bump markedj version | [af979af4](https://github.com/freeplane/freeplane/commit/af979af40cebfd059acbeb9ab6b7bb51f6d9ac04) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2021-06-03 | `fix` | fix editor background colors on VAqua | [b1cec127](https://github.com/freeplane/freeplane/commit/b1cec127d88e7540672b9c699c78175e1ccdd2d2) |
| 2021-05-13 | `fix` | Fix jsyntaxpane package import | [fd935f1f](https://github.com/freeplane/freeplane/commit/fd935f1f882564cecd9d3998e2f710e406daaa82) |
| 2021-05-01 | `feature` | #2920 add borders to Markdown table | [5edf77c9](https://github.com/freeplane/freeplane/commit/5edf77c9523afab976e43cc825102e256be055f4) |
| 2021-02-21 | `feature` | #2877 add translations for markdown preferences | [06fbf85f](https://github.com/freeplane/freeplane/commit/06fbf85f1d39cb57002c423d19f461baa0a63356) |
| 2021-01-17 | `fix` | fix rendering | [0c305a86](https://github.com/freeplane/freeplane/commit/0c305a867024a10fc23a8d8d07572fd669f419e8) |
| 2021-01-16 | `fix` | fix note views in maps | [b72ceda3](https://github.com/freeplane/freeplane/commit/b72ceda36165440f7e142cc9ea89b11cf4eb8c39) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |

---

## Legenda categorie

| Categoria | Significato |
|-----------|-------------|
| `feature` | Nuova funzionalità o comportamento aggiunto |
| `fix` | Correzione di bug o regressione |
| `refactor` | Ristrutturazione del codice senza cambi funzionali |
| `api_change` | Modifica alle interfacce pubbliche / breaking change |
| `docs` | Documentazione, commenti, JavaDoc |
| `test` | Test unitari o di integrazione |
| `build` | Sistema di build, dipendenze, release |
| `other` | Traduzioni, merge, configurazione, non classificato |
