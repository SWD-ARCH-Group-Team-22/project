# JSyntaxPane — Commit rilevanti

**Modulo:** `freeplane_plugin_jsyntaxpane`  
**Commit rilevanti (feature / fix / api_change):** 19 su 45 totali

> Evidenziazione della **sintassi del codice** nell'editor script interno. Rende più leggibile e modificabile il codice Groovy/script direttamente nell'interfaccia.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2024](#2024) — 4 commit
- [2022](#2022) — 5 commit
- [2021](#2021) — 1 commit
- [2020](#2020) — 1 commit
- [2018](#2018) — 2 commit
- [2017](#2017) — 3 commit
- [2016](#2016) — 2 commit
- [2015](#2015) — 1 commit

---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-10-06 | `fix` | Fix: register latex content type | `Activator.java` | [e41960cf](https://github.com/freeplane/freeplane/commit/e41960cfa963473ad4cd773ed8d0a0df668a221c) |
| 2024-04-05 | `feature` | Support sorting tags in tag editor | `TagEditor.java`, `Resources_en.properties` +3 | [fd067897](https://github.com/freeplane/freeplane/commit/fd067897212b829876fe93f4848d789ea51a3372) |
| 2024-04-03 | `feature` | implement tags | `build.gradle`, `mindmapmodemenu.xml` +19 | [10ac51da](https://github.com/freeplane/freeplane/commit/10ac51da9104bde5fe2a8516f86babf38fb90a20) |
| 2024-02-02 | `fix` | fix eclipse configuration in gradle | `build.gradle`, `build.gradle` | [ce7cf789](https://github.com/freeplane/freeplane/commit/ce7cf789de677eb858829b58f74785fbd7421936) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-09-24 | `fix` | fix "goto  line" | `SyntaxDocument.java`, `ActionUtils.java` +1 | [83230b8d](https://github.com/freeplane/freeplane/commit/83230b8d21064b7b89f24107c983e3dc0c980f7c) |
| 2022-09-24 | `fix` | fix insets handling | `LineNumbersRuler.java` | [ddacf51b](https://github.com/freeplane/freeplane/commit/ddacf51b06a49460c0f2839b006e3874685c7594) |
| 2022-09-24 | `fix` | patch SyntaxPane | `DefaultSyntaxKit.java`, `WrappedSyntaxView.java` +3 | [9c3e102d](https://github.com/freeplane/freeplane/commit/9c3e102d8dee4b65cb28eeb262b634995556b544) |
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-01-14 | `feature` | support dark themes in syntax editor | `build.gradle`, `SourceTextEditorUIConfigurator.java` +3 | [eb4166a7](https://github.com/freeplane/freeplane/commit/eb4166a7612d80849365d13cff940940fab72e09) |

### Dettagli commit con note

**[9c3e102d](https://github.com/freeplane/freeplane/commit/9c3e102d8dee4b65cb28eeb262b634995556b544)** (2022-09-24) — patch SyntaxPane

> https://github.com/Sciss/SyntaxPane/pull/37


---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-01-02 | `feature` | replace proprietary jsyntaxpane by more recent de.sciss.syntaxpane with markdown support | `build.gradle`, `FormulaEditor.java` +14 | [ba8adffd](https://github.com/freeplane/freeplane/commit/ba8adffdf6996114858114231470e131a336dfa2) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-07-21 | `fix` | fix memory leak | `NodeIdHighLighter.java` | [7b71ff09](https://github.com/freeplane/freeplane/commit/7b71ff098d25ff64ac4a097aea251e7c1485a1c8) |
| 2018-04-24 | `fix` | fix #2586 by porting https://github.com/nordfalk/jsyntaxpane change to the Debian repo | `build.gradle`, `jsyntaxpane-0.9.6~r156-5.jar` +2 | [5e72a474](https://github.com/freeplane/freeplane/commit/5e72a474d5905a6b4d3cd4d77e16f033726041aa) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-03-21 | `fix` | fix warning | `LaTeXLexer.java` | [4ba02411](https://github.com/freeplane/freeplane/commit/4ba0241152b219d91baf18858a6f200d3c2576d4) |
| 2017-03-19 | `fix` | fix warning | `LaTeXLexer.java` | [77dd6fec](https://github.com/freeplane/freeplane/commit/77dd6fec1e0a13d38e8bde9fe817c1fd80ff386c) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |
| 2016-10-16 | `fix` | fix warning including a break statement in switch case | `LaTeXLexer.java` | [475a8d27](https://github.com/freeplane/freeplane/commit/475a8d275c08d5e8bc2880b94e20ac35dfde435d) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-04-07 | `feature` | add gradle task for latex.flex->LaTeXLexer.java (for use with srcpure) | `build.gradle` | [b5500710](https://github.com/freeplane/freeplane/commit/b55007106640d9b3df295dfdc5145498bae71f0d) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
