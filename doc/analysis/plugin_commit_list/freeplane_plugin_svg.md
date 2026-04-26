# SVG — Commit rilevanti

**Modulo:** `freeplane_plugin_svg`  
**Commit rilevanti (feature / fix / api_change):** 43 su 159 totali

> Supporto per immagini e grafici **SVG** embedded nei nodi. Permette di arricchire le mappe con grafica vettoriale scalabile e di visualizzare diagrammi generati da script.

_Generato il 2026-04-26 17:07_

---

## Indice per anno

- [2025](#2025) — 1 commit
- [2024](#2024) — 3 commit
- [2022](#2022) — 3 commit
- [2021](#2021) — 2 commit
- [2020](#2020) — 3 commit
- [2019](#2019) — 3 commit
- [2018](#2018) — 2 commit
- [2017](#2017) — 2 commit
- [2016](#2016) — 1 commit
- [2015](#2015) — 6 commit
- [2014](#2014) — 9 commit
- [2013](#2013) — 3 commit
- [2012](#2012) — 1 commit
- [2011](#2011) — 1 commit
- [2010](#2010) — 2 commit
- [2009](#2009) — 1 commit

---

## 2025

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2025-04-28 | `fix` | fix typo | `ResourceController.java`, `IconSelectionPopupDialog.java` +17 | [a9451631](https://github.com/freeplane/freeplane/commit/a945163128013a1f7889b007ed17b7da8f1fcecd) |

---

## 2024

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2024-11-02 | `fix` | Update and fix dependency versions for apache batik and fop | `build.gradle` | [3b3475ab](https://github.com/freeplane/freeplane/commit/3b3475ab130d8e66202d91ed7069188e7037be1c) |
| 2024-07-27 | `fix` | Do not change look and feel during export to SVG/PDF | `ExportVectorGraphic.java` | [93af3ff1](https://github.com/freeplane/freeplane/commit/93af3ff1a5ed81e05ed29ac7889e0035586c35db) |
| 2024-03-05 | `feature` | add pdf export to codeexplorer | `Activator.java` | [0e97fb58](https://github.com/freeplane/freeplane/commit/0e97fb5833cc4cb6316957294d2eac0b7ca2f01a) |

### Dettagli commit con note

**[93af3ff1](https://github.com/freeplane/freeplane/commit/93af3ff1a5ed81e05ed29ac7889e0035586c35db)** (2024-07-27) — Do not change look and feel during export to SVG/PDF

> It reverts a bug fix from 2013-12-02
> and relates to issue #1920
> "Freeplane menu fonts are increased each time File > Export > PDF is used"


---

## 2022

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2022-04-17 | `feature` | add command line option -R to run groovy scripts on start | `CommandLineOptions.java`, `CommandLineParser.java` +19 | [b0316941](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528) |
| 2022-03-19 | `feature` | Freeplane 1.10.x with Java 17 support | `build.gradle`, `build.gradle` +18 | [4b16c43d](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612) |
| 2022-01-07 | `feature` | Replace darcula LAF by supported Flat Darcula LAF and add Flat Light LAF | `build.gradle`, `FixDarculaToggleButtonUI.java` +4 | [40eb7bdf](https://github.com/freeplane/freeplane/commit/40eb7bdfd07db8ecfd5424ba4f765be268a7428e) |

---

## 2021

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2021-08-20 | `fix` | fix pdf export removing font search un user directory performed by fop | `Resources_de.properties`, `Resources_es.properties` +22 | [1cd87dfe](https://github.com/freeplane/freeplane/commit/1cd87dfef08fb030b4a3acf7dd8c0c74c0726d4c) |
| 2021-03-21 | `feature` | Add warning for first PDF export | `Resources_en.properties`, `ExportPdf.java` | [7a921d80](https://github.com/freeplane/freeplane/commit/7a921d80cd7a2f286968a9c1154a3b221f13c48a) |

---

## 2020

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2020-02-22 | `fix` | fix gradle warnings (now requires gradle 5.1 or later) | `build.gradle`, `bin.dist.gradle` +17 | [4043456b](https://github.com/freeplane/freeplane/commit/4043456b9d7f14cc41006b2912507a2cfd46279d) |
| 2020-02-22 | `fix` | Fix SVG backgrounds | `BitmapViewerFactory.java`, `IViewerFactory.java` +3 | [02b5f924](https://github.com/freeplane/freeplane/commit/02b5f924779846aff5dd9bfcf7c126b84a55dbcb) |
| 2020-02-21 | `fix` | fix svg images | `BitmapViewerFactory.java`, `ExternalResource.java` +3 | [65d1fe0f](https://github.com/freeplane/freeplane/commit/65d1fe0f7cb233dc6d1baf30f394d606723ef8c0) |

---

## 2019

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2019-12-14 | `fix` | Workaround for fop 2.4 bug https://issues.apache.org/jira/browse/FOP-2896 | `ExportPdf.java` | [f0c2c90b](https://github.com/freeplane/freeplane/commit/f0c2c90b084b5c1d626caa83f645c84491f22ebb) |
| 2019-12-14 | `fix` | fix fop 2.4 dependency | `build.gradle` | [a863367b](https://github.com/freeplane/freeplane/commit/a863367bc951e76366dc088d6b39ed46cda68b49) |
| 2019-09-21 | `fix` | Fix SVG and PDF export with Darcula LaF | `ExportVectorGraphic.java` | [13e03dbf](https://github.com/freeplane/freeplane/commit/13e03dbfd4d1bf1e17c9658e9539db0f465d18c4) |

---

## 2018

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2018-12-24 | `fix` | fix svg in previews and tooltips | `ImageTooltipRendererFactory.java`, `SvgViewerFactory.java` | [971c4ae4](https://github.com/freeplane/freeplane/commit/971c4ae4df0bfab9cdbad63a398c8df55d6da26b) |
| 2018-02-25 | `fix` | Fix embedded text in PDF export | `ExportPdf.java`, `ExportSvg.java` +1 | [17ddd648](https://github.com/freeplane/freeplane/commit/17ddd648d920febcb610b35c98fa2c7297bd47e0) |

---

## 2017

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2017-12-08 | `feature` | add testCompile dependencies | `build.gradle`, `build.gradle` +4 | [6833cbc2](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829) |
| 2017-10-14 | `fix` | fix batik export of gradients in svgSalamander's SVG icons | `ExportVectorGraphic.java`, `GradientExtensionHandler.java` | [2e72152f](https://github.com/freeplane/freeplane/commit/2e72152f360acdbcda610e5d2ef9f893c02674b1) |

---

## 2016

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2016-11-13 | `feature` | Remove instruction 'Bundle-RequiredExecutionEnvironment', 'JavaSE-1.7' because OSGi does n | `build.gradle`, `build.gradle` +6 | [65c3efd1](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d) |

---

## 2015

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2015-11-19 | `fix` | Fix NPE | `SvgViewerFactory.java` | [24581795](https://github.com/freeplane/freeplane/commit/2458179551f40a19af50810e28ffc997b4cfb815) |
| 2015-11-19 | `fix` | Fix NPE | `SvgViewerFactory.java` | [a0f1cac4](https://github.com/freeplane/freeplane/commit/a0f1cac473807e2c1bd43094abf9f51222fa01c0) |
| 2015-02-23 | `fix` | Fix external image zooming | `BitmapViewerFactory.java`, `ExternalResource.java` +2 | [63e223d8](https://github.com/freeplane/freeplane/commit/63e223d8cc9a1b28dff7852e04007b27a350e470) |
| 2015-01-26 | `feature` | add copyEclipseSettings task, remove .settings from version control (except for templates) | `org.eclipse.core.resources.prefs`, `org.eclipse.core.runtime.prefs` +55 | [1c7cc029](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668) |
| 2015-01-24 | `feature` | add xerces dependency to svg plugin (necessary for pdf export) | `build.gradle` | [96b107c8](https://github.com/freeplane/freeplane/commit/96b107c826e0ace11a0535881678b405c60ba9e7) |
| 2015-01-02 | `feature` | remove all MANIFESTs, include only those artifacts in git which are not in a maven repo, a | `MANIFEST.MF`, `build.gradle` +24 | [45ae8049](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) |

### Dettagli commit con note

**[24581795](https://github.com/freeplane/freeplane/commit/2458179551f40a19af50810e28ffc997b4cfb815)** (2015-11-19) — Fix NPE

> java.lang.NullPointerException
> 	at
> org.freeplane.view.swing.features.filepreview.ExternalResource.setZoom(ExternalResource.java:68)
> 	at
> org.freeplane.view.swing.features.filepreview.ExternalResource.setZoom(ExternalResource.java:85)
> 	at
> org.freeplane.plugin.svg.SvgViewerFactory$1.gvtRenderingCompleted(SvgViewerFactory.java:91)
> 	at
> org.apache.batik.swing.gvt.GVTTreeRenderer$4.dispatch(GVTTreeRenderer.java:193)

**[a0f1cac4](https://github.com/freeplane/freeplane/commit/a0f1cac473807e2c1bd43094abf9f51222fa01c0)** (2015-11-19) — Fix NPE

> java.lang.NullPointerException
> 	at
> org.freeplane.view.swing.features.filepreview.ExternalResource.setZoom(ExternalResource.java:68)
> 	at
> org.freeplane.view.swing.features.filepreview.ExternalResource.setZoom(ExternalResource.java:85)
> 	at
> org.freeplane.plugin.svg.SvgViewerFactory$1.gvtRenderingCompleted(SvgViewerFactory.java:91)
> 	at
> org.apache.batik.swing.gvt.GVTTreeRenderer$4.dispatch(GVTTreeRenderer.java:193)


---

## 2014

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2014-12-30 | `fix` | fix "Export-Package: *" (:freeplane) problem by bypassing bnd (f*ck bnd!) | `build.gradle`, `build.gradle` +5 | [df4412fe](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) |
| 2014-12-26 | `feature` | add Bundle-ClassPath manifest header | `build.gradle`, `build.gradle` +5 | [d00550c5](https://github.com/freeplane/freeplane/commit/d00550c5813be270e0fa1b773225660af041a457) |
| 2014-07-21 | `feature` | Moved svg plugin source code to the new directory structure | `Activator.java`, `ExportPdf.java` +4 | [8d27d685](https://github.com/freeplane/freeplane/commit/8d27d6855f2a1a5772ff38272070646bd2c6737d) |
| 2014-03-08 | `fix` | fix loading background image on start | `MapView.java`, `SvgViewerFactory.java` | [af6f06ad](https://github.com/freeplane/freeplane/commit/af6f06ad55bec4b1db46253b2bfa6839820e18e3) |
| 2014-03-06 | `fix` | fix endless repaint in painting background component | `BitmapViewerComponent.java`, `ImageLoadingListener.java` +3 | [5f71fff7](https://github.com/freeplane/freeplane/commit/5f71fff74dae5ef300397ea2c4983946da063ae3) |
| 2014-03-01 | `fix` | Fix centring problems | `BitmapViewerComponent.java`, `ScalableComponent.java` +2 | [448a6157](https://github.com/freeplane/freeplane/commit/448a61570308d1c13b27554cf0f61a9f317ab9f7) |
| 2014-03-01 | `fix` | Refactor Viewer Components and MapView | `BitmapViewerComponent.java`, `UITools.java` +2 | [42732cd4](https://github.com/freeplane/freeplane/commit/42732cd4b39371b9ab885eff493d494ef9e1f976) |
| 2014-02-21 | `feature` | Create workaround for "fit to zoom" option and limit maximum size | `BitmapViewerComponent.java`, `ScalableComponent.java` +2 | [2eea90dd](https://github.com/freeplane/freeplane/commit/2eea90dd5f4c06ca00fb13642a8be9e41097e4f1) |
| 2014-01-24 | `fix` | fix change to previous look and feel after svg export | `ExportVectorGraphic.java` | [1ac96c42](https://github.com/freeplane/freeplane/commit/1ac96c42546d1b4206e2afe6d3c8504ef3eb84d2) |

### Dettagli commit con note

**[42732cd4](https://github.com/freeplane/freeplane/commit/42732cd4b39371b9ab885eff493d494ef9e1f976)** (2014-03-01) — Refactor Viewer Components and MapView

> Removed unnecessary methods due to the updating of the Scalr classes.
> Now the scalable component implementations are responsible for
> centring their images. The only problem that remains is the bug
> involving the off centring of SVG images.

**[2eea90dd](https://github.com/freeplane/freeplane/commit/2eea90dd5f4c06ca00fb13642a8be9e41097e4f1)** (2014-02-21) — Create workaround for "fit to zoom" option and limit maximum size

> I created a method in order to adjust the preferred size width/height
> ratio to that of the original image. Moreover, I limited the maximum
> size of the viewer to the preferred size of the MapView, eliminating
> the "out of memory error" occurrences.


---

## 2013

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2013-12-02 | `fix` | fix PDF/SVG Export when using GTK/Nimbus L&Fs and node attributes II: don't call frame.pac | `ExportVectorGraphic.java` | [f4c963b4](https://github.com/freeplane/freeplane/commit/f4c963b41c1e306ce1b61575179937bd358e5218) |
| 2013-12-02 | `fix` | fix PDF/SVG Export when using GTK/Nimbus L&Fs and node attributes | `ExportVectorGraphic.java` | [a804a173](https://github.com/freeplane/freeplane/commit/a804a173a14630c4d62ee0b1dce039830948cef5) |
| 2013-03-31 | `fix` | fix compiler warnings (unused imports, variables) | `AFreeplaneAction.java`, `AccelerateableAction.java` +16 | [0833b405](https://github.com/freeplane/freeplane/commit/0833b4059009f88fb523ff7a82ab07ccb7fe8b0c) |

---

## 2012

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2012-04-27 | `fix` | fix resolution for pdf export | `ExportPdf.java` | [d19bb1d8](https://github.com/freeplane/freeplane/commit/d19bb1d87d20a78eca34bb95c4bb95704c3307c1) |

---

## 2011

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2011-06-13 | `fix` | fix package import | `SvgViewerFactory.java` | [6ae393fb](https://github.com/freeplane/freeplane/commit/6ae393fbec2eae1899a3a21fa538f27e83425fb7) |

---

## 2010

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2010-03-30 | `fix` | rename FpStringUtils to TextUtil, move it into core.util package and move all static metho | `MANIFEST.MF`, `ColorTracker.java` +163 | [06ed5406](https://github.com/freeplane/freeplane/commit/06ed54068f045191f8031fd9399021fd060c58ad) |
| 2010-01-21 | `fix` | bug fix for displaying svg graphics with not integer dimension | `SvgViewerFactory.java` | [c9ce9936](https://github.com/freeplane/freeplane/commit/c9ce9936bef5df9e11205806f7a9cefb0b735f18) |

---

## 2009

| Data | Tipo | Descrizione | File principali | Hash |
|------|------|-------------|-----------------|------|
| 2009-12-15 | `fix` | build patch from ewl: separate properties | `ant.properties`, `build.xml` +12 | [db2ac954](https://github.com/freeplane/freeplane/commit/db2ac9547e843ffe9123d133e7e6cb30292727f9) |

---

## Legenda

| Tipo | Significato |
|------|-------------|
| `feature` | Nuova funzionalità aggiunta |
| `fix` | Correzione di bug o regressione |
| `api_change` | Modifica alle interfacce pubbliche |
