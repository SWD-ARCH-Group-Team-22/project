# Debug Helper — Commit rilevanti

**Modulo:** `freeplane_debughelper`  
**Commit rilevanti (feature / fix / api_change):** 29 su 49 totali

> Utilità per il **debug** in sviluppo: strumenti di ispezione dello stato interno, logging avanzato e assistenza agli sviluppatori di plugin.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2025](#2025) — 3 commit
- [2024](#2024) — 1 commit
- [2023](#2023) — 1 commit
- [2022](#2022) — 5 commit
- [2021](#2021) — 4 commit
- [2020](#2020) — 7 commit
- [2019](#2019) — 3 commit
- [2018](#2018) — 5 commit

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-09-07 | `fix` | outline: fix incorrect content-level indentation by using computed parent-chain depth | `BlockPanel.java`, `NodePositioning.java` +1 | [c3338a39](https://github.com/freeplane/freeplane/commit/c3338a39ba88f9127febc463ae66923cc506fd96) |
| 2025-08-17 | `fix` | Multiple bug fixes for auxillary component and for startup | `AuxillaryEditorSplitPane.java`, `FrameComponentMover.java` +1 | [d18cef3d](https://github.com/freeplane/freeplane/commit/d18cef3d0e5e657c131f2b08cf8a9f5fe77baa3c) |
| 2025-08-14 | `feature` | Add option "UI elements follow selected map" true by default | `preferences.xml`, `ApplicationViewController.java` +7 | [aefa5f32](https://github.com/freeplane/freeplane/commit/aefa5f3249e0b95449cbc0350e70b892de3586df) |

### Dettagli commit con note

**[c3338a39](https://github.com/freeplane/freeplane/commit/c3338a39ba88f9127febc463ae66923cc506fd96)** (2025-09-07) — outline: fix incorrect content-level indentation by using computed parent-chain depth

> - BlockPanel computes X from actual node depth instead of FlatNode.depth.
> - NodePositioning aligns navigation buttons using computed depth for content area.
> - Remove temporary stdout diagnostics.
> 
> This corrects cases where first-level nodes appeared at deeper levels under wrong parents in the outline.


---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-01-22 | `fix` | fix launcher configuration | `build.gradle`, `freeplane.xml` +3 | [e653bc1e](https://github.com/freeplane/freeplane/commit/e653bc1ee2309ccff82334d44cabddf798e20f99) |

---

## 2023

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2023-05-24 | `feature` | Add logging properties to launch configurations | `freeplane dist mac.launch`, `freeplane dist.launch` +3 | [63bd0533](https://github.com/freeplane/freeplane/commit/63bd0533126d2e13401c54d590fac8f4fbeecdcb) |

---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-10-29 | `feature` | add permission java.awt.AWTPermission "watchMousePointer" | `freeplane.policy`, `freeplane.policy` | [c725f317](https://github.com/freeplane/freeplane/commit/c725f31740618b65c9ebd4bf7a5f191a64cae726) |
| 2022-04-09 | `fix` | fix gradle config | `build.gradle` | [ccb66e26](https://github.com/freeplane/freeplane/commit/ccb66e2650b3828ffbabf7e99195997952c91037) |
| 2022-04-09 | `fix` | fix gradle config | `build.gradle` | [679dd696](https://github.com/freeplane/freeplane/commit/679dd696cdc7be1d2f6e4a77ef4ea862d2919f5c) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-02-28 | `fix` | Deprecated properties set to the correct values. | `build.gradle`, `linux-packages.gradle` | [f10c27bf](https://github.com/freeplane/freeplane/commit/f10c27bffd3d76ac997cff05f1fd4cf1f85df007) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-04-18 | `fix` | fix idea run configurations (tested with Intellij CE 2021.1) | `freeplane.xml`, `freeplane_dist.xml` | [8447fc1c](https://github.com/freeplane/freeplane/commit/8447fc1c24c1f9020bdfec602cef6153c50140b9) |
| 2021-04-16 | `feature` | add exports to non public API used by darcula | `freeplane dist mac.launch`, `freeplane mac.launch` +1 | [ee7f685c](https://github.com/freeplane/freeplane/commit/ee7f685c3bc06b1d87bc82cce3bac0ab5961e419) |
| 2021-03-21 | `fix` | fix access to com.apple.eawt.Application.requestToggleFullScreen by reflection | `freeplane dist mac.launch`, `freeplane mac.launch` +1 | [e850d1de](https://github.com/freeplane/freeplane/commit/e850d1de2f907b05f3d9565347d13e17a52095a1) |
| 2021-01-04 | `fix` | fix eclipse dist launch classpaths | `freeplane dist mac.launch`, `freeplane dist.launch` | [3b194526](https://github.com/freeplane/freeplane/commit/3b194526758c7c29f52413dac52e2733f1f68c16) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-12-23 | `fix` | fix freeplane_debughelper for MacOS | `build.gradle` | [f852e189](https://github.com/freeplane/freeplane/commit/f852e1893a5cd967b78260d57d08e7347e3df08d) |
| 2020-11-14 | `fix` | fix launch configurations | `freeplane dist.launch`, `freeplane.launch` | [1f534dad](https://github.com/freeplane/freeplane/commit/1f534dad20c2318f7b3a1487b9cfb7ddbb86f80b) |
| 2020-04-05 | `fix` | fix eclipse freeplane launch configuration | `freeplane.launch` | [6c90f1c8](https://github.com/freeplane/freeplane/commit/6c90f1c8a3585883d6cbbe59e598abbf1aa10338) |
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-01-25 | `fix` | fix gradle configuration | `build.gradle`, `build.gradle` | [8c57581b](https://github.com/freeplane/freeplane/commit/8c57581b81fc4aec3c2cdd2f4a461dc405fc5bff) |
| 2020-01-12 | `feature` | Add -Dsun.awt.disablegrab=true to launcher configurations | `freeplane dist mac.launch`, `freeplane dist.launch` +2 | [7a4e9e30](https://github.com/freeplane/freeplane/commit/7a4e9e303cfea19c1f46d055a6d567919f19ec6f) |
| 2020-01-12 | `feature` | Add -Dsun.awt.disablegrab=true to launcher configurations | `freeplane dist mac.launch`, `freeplane dist.launch` +2 | [becf7c79](https://github.com/freeplane/freeplane/commit/becf7c79c6e9b5886e9521e119d2df4e468b8393) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-09-14 | `feature` | Support dark mode | `build.gradle`, `history_en.txt` +9 | [da8243fc](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a) |
| 2019-07-26 | `feature` | Support for data URLs as specified in RFC 2397 | `build.gradle`, `Handler.java` +5 | [d8ea124e](https://github.com/freeplane/freeplane/commit/d8ea124ed16b0409b63da98be7f067cd5cc49467) |
| 2019-01-16 | `feature` | consider new location of java-atk-wrapper under linux in policy files | `freeplane.policy`, `freeplane.policy` | [6759ef7e](https://github.com/freeplane/freeplane/commit/6759ef7e473c9bbbf2fac408c6123db4dfb0a063) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-29 | `fix` | Fix external resource dir in eclipse launcher | `freeplane.launch` | [330ba9a0](https://github.com/freeplane/freeplane/commit/330ba9a0f850f00cc966ef2c65ec84107db1688a) |
| 2018-08-31 | `fix` | fix eclipse config | `build.gradle`, `build.gradle` | [ad8ee742](https://github.com/freeplane/freeplane/commit/ad8ee7425a2c2c3a1371fea75e5bc907924e2b16) |
| 2018-08-23 | `fix` | fix loading external resources in intellij / netbeans launchers | `build.gradle`, `freeplane.xml` | [a8a7c9e1](https://github.com/freeplane/freeplane/commit/a8a7c9e11bc18d09d62d2cff72ed3c65a5fe0c3a) |
| 2018-08-22 | `fix` | fix launcher directories | `freeplane knopflerfish mac.launch`, `freeplane knopflerfish.launch` +5 | [f654d5a4](https://github.com/freeplane/freeplane/commit/f654d5a4981f01961cd6cdc70e7392eb4391aedd) |
| 2018-08-22 | `fix` | fix for idea | `build.gradle`, `build.gradle` | [8c706070](https://github.com/freeplane/freeplane/commit/8c70607072fda8e09843b6a35f0100676179f69d) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
