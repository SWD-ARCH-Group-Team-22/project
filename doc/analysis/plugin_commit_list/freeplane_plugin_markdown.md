# Markdown — Commit rilevanti

**Modulo:** `freeplane_plugin_markdown`  
**Commit rilevanti (feature / fix / api_change):** 11 su 37 totali

> Rendering **Markdown** nel pannello note dei nodi. Consente di scrivere note ricche (titoli, grassetti, liste, codice) in sintassi standard Markdown invece di HTML.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2025](#2025) — 2 commit
- [2023](#2023) — 1 commit
- [2022](#2022) — 1 commit
- [2021](#2021) — 7 commit

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-05-18 | `feature` | Better support input method events | `IEditHandler.java`, `IUserInputListenerFactory.java` +18 | [ddf41d1f](https://github.com/freeplane/freeplane/commit/ddf41d1fe8e72aecade6ca1e4a37f9c3fcd6d56d) |
| 2025-01-06 | `feature` | Issue #2082 add PlantUML support to Markdown | `history_en.txt`, `build.gradle` +3 | [e602267e](https://github.com/freeplane/freeplane/commit/e602267e07b2287b7a9e84c5503887faf732c6bd) |

---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-07-21 | `fix` | bump markedj version | `build.gradle` | [af979af4](https://github.com/freeplane/freeplane/commit/af979af40cebfd059acbeb9ab6b7bb51f6d9ac04) |

### Dettagli commit con note

**[af979af4](https://github.com/freeplane/freeplane/commit/af979af40cebfd059acbeb9ab6b7bb51f6d9ac04)** (2023-07-21) — bump markedj version

> because 1.0.18 includes a fix for hard line breaks by backslash at EOL -> https://github.com/gitbucket/markedj/pull/41


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
| 2021-05-01 | `feature` | #2920 add borders to Markdown table | `ModeController.java`, `MarkdownRenderer.java` | [5edf77c9](https://github.com/freeplane/freeplane/commit/5edf77c9523afab976e43cc825102e256be055f4) |
| 2021-02-21 | `feature` | #2877 add translations for markdown preferences | `Resources_es.properties`, `Resources_fr.properties` +6 | [06fbf85f](https://github.com/freeplane/freeplane/commit/06fbf85f1d39cb57002c423d19f461baa0a63356) |
| 2021-01-17 | `fix` | fix rendering | `FormatContentTransformer.java`, `MainView.java` +4 | [0c305a86](https://github.com/freeplane/freeplane/commit/0c305a867024a10fc23a8d8d07572fd669f419e8) |
| 2021-01-16 | `fix` | fix note views in maps | `MainView.java`, `NodeViewFactory.java` +4 | [b72ceda3](https://github.com/freeplane/freeplane/commit/b72ceda36165440f7e142cc9ea89b11cf4eb8c39) |
| 2021-01-14 | `feature` | enable dialog editors for latex, markdown and formula in details and notes | `NoteDialogStarter.java`, `RichTextModel.java` +9 | [fc5bf434](https://github.com/freeplane/freeplane/commit/fc5bf434e30d44cbc819ee11f9debcb98c481d55) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
