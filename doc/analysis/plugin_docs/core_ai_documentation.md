# Storia dei plugin di Freeplane — Analisi narrativa

_Basata sui commit rilevanti (feature / fix / api_change) estratti dalla repo Git_

---

## Indice

1. [freeplane_core — Il nucleo](#1-freeplane_core--il-nucleo)
2. [freeplane_framework — Il contenitore OSGi](#2-freeplane_framework--il-contenitore-osgi)
3. [freeplane_plugin_script — Lo scripting Groovy](#3-freeplane_plugin_script--lo-scripting-groovy)
4. [freeplane_plugin_svg — Grafica vettoriale e PDF](#4-freeplane_plugin_svg--grafica-vettoriale-e-pdf)
5. [freeplane_plugin_openmaps — La mappa dentro la mappa](#5-freeplane_plugin_openmaps--la-mappa-dentro-la-mappa)
6. [other — Il cantiere trasversale](#6-other--il-cantiere-trasversale)
7. [Come comunicano i plugin? Core o API pubblica?](#7-come-comunicano-i-plugin-core-o-api-pubblica)

---

## 1. `freeplane_core` — Il nucleo

**3130 commit rilevanti su 13039 totali**, copertura 2009–2026.

### L'era delle fondamenta (2009–2011)

Il core nasce come aggregato monolitico in cui tutto coabita: rendering dei nodi, parsing del formato `.mm`, gestione degli attributi, sistema degli hook. Il codice di questa fase è prevalentemente in Swing puro e riflette una architettura a plugin rudimentale, dove le estensioni vengono "agganciate" al modello del nodo tramite classi come `PersistentNodeHook`. Non esisteva ancora separazione netta tra logica di dominio e presentazione.

In questi anni il ritmo dei commit è elevatissimo — 239 nel solo 2009, 284 nel 2011 — segno che il progetto era in uno stato di evoluzione rapida e spesso non pianificata. I fix si accumulano sulle stesse aree: il sistema di filtri, la serializzazione XML, l'editing in-place dei nodi.

### La grande ristrutturazione (2012–2016)

Il 2012 segna una svolta strutturale. Arriva la separazione tra modalità `MindMap` e modalità `Browse`, si introducono i `ConditionalStyles` e il sistema di plugin OSGi viene reso più rigido. Un commit del 2012 introduce il supporto headless ([`597493e7`](https://github.com/freeplane/freeplane/commit/597493e7db05ac58556af9e67070f90bd7a3b97d)), che permette di eseguire Freeplane senza UI — fondamentale per l'automazione con script.

Nel 2014 avviene la migrazione al build system Gradle: il commit [`df4412fe`](https://github.com/freeplane/freeplane/commit/df4412fe6e3d65a427aa95cdb18928ea1ed02715) descrive il dolore di un workaround per bypassare `bnd` ("f*ck bnd!") durante la generazione dei bundle OSGi. Nel 2015 viene eliminata la gestione manuale dei `MANIFEST.MF` e si passa a Maven per le dipendenze esterne ([`45ae8049`](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5)).

Il periodo 2015–2016 è dominato da una massiccia attività sulla UI: 270 commit nel 2015 e 247 nel 2016. Vengono introdotti i `ConditionalStyles` per i template, il sistema di icone viene unificato e inizia la transizione verso SVG per le icone interne.

### Il rinnovamento della UI (2017–2021)

Nel 2019 arriva il supporto per la **dark mode** ([`da8243fc`](https://github.com/freeplane/freeplane/commit/da8243fcb37b7dd3337c40d0fed301f20e713e5a)), un commit che tocca trasversalmente molti plugin contemporaneamente. Nel 2021 viene sostituita l'icona dell'applicazione con la nuova artwork di Stuart Robertson ([`1965cfa0`](https://github.com/freeplane/freeplane/commit/1965cfa0f26a11df397b02455909a95911ac144a)) e viene introdotta la modalità VAqua per macOS.

Nel 2022 il core assorbe il cambio più impattante del periodo: la migrazione a **Java 17** ([`4b16c43d`](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612)), con tutte le implicazioni per i moduli OSGi che devono esplicitare i propri export. Nello stesso anno viene introdotto il nuovo sistema di layout verticale (`VerticalNodeViewLayoutStrategy`) che diventa il cantiere principale del core per gli anni successivi.

### La grande espansione dell'outline (2024–2025)

Il 2025 è l'anno in cui il core subisce la sua trasformazione più radicale dalla fondazione: l'introduzione dell'**outline view**, una vista alternativa alla mappa ad albero tradizionale. Il lavoro è enorme — oltre 80 commit in tre mesi (agosto-ottobre 2025) — e procede per fasi strutturate che il team chiama esplicitamente "phase 2", "phase 3", "phase 6", "phase 7", visibili nei titoli dei commit:

- Phase 2 — centralizzazione dei key binding ([`3b3677f5`](https://github.com/freeplane/freeplane/commit/3b3677f55f7dc01feec91ed51db589758e2f931d))
- Phase 3 — introduzione di `NodeButton` ([`dd34a602`](https://github.com/freeplane/freeplane/commit/dd34a602a703e5ca9fe9c7b67b23beee64e54f73))
- Phase 6 — delega della selezione a `OutlineSelectionManager` ([`589d09ef`](https://github.com/freeplane/freeplane/commit/589d09ef41a9add470303a30da12e6e4154838d7))
- Phase 7 — test AssertJ per `BreadcrumbPath` e `OutlineSelectionManager` ([`5ebe3500`](https://github.com/freeplane/freeplane/commit/5ebe35001df44f8ac5d75de9f7becd770cd613ac))

Vengono anche implementati i **bookmarks** come feature trasversale ([`a8c33b98`](https://github.com/freeplane/freeplane/commit/a8c33b989165cb0d05510fb2c703b89f24115b1b)), con toolbar dedicata, drag-and-drop e API per gli script.

### L'integrazione AI (2026)

Il 2026 segna l'ingresso dell'intelligenza artificiale nel core. Vengono aggiunti un **pannello AI di chat** ([`747ada3e`](https://github.com/freeplane/freeplane/commit/747ada3e271e27a183c08a2845d9892011fb09f2)), un **server MCP** per esposizione degli strumenti a modelli linguistici esterni, supporto per autenticazione bearer e API key, e un sistema di profili per gli assistenti AI. I tag dei nodi vengono esposti agli strumenti AI tramite un `TagCategoryAccess` unificato ([`b4726030`](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51)). È un cambio di paradigma: Freeplane non è più solo uno strumento per umani, ma anche una piattaforma su cui gli LLM possono operare direttamente.

---

## 2. `freeplane_framework` — Il contenitore OSGi

**146 commit rilevanti su 669 totali**, copertura 2009–2026.

### Origini e scelta di OSGi (2009–2010)

Il framework è il layer che permette a Freeplane di esistere come applicazione modulare. La scelta di OSGi (implementata con Knopflerfish) risale ai primissimi anni del progetto. In questo periodo il framework gestisce il ciclo di vita dei bundle — avvio, sospensione, riavvio — e i file `.policy` che regolano i permessi Java di sicurezza.

Il 2010 è l'anno più intenso per il framework (22 commit rilevanti): vengono stabiliti i pattern di avvio, la struttura dei `props.xargs` per la configurazione OSGi e le prime dipendenze inter-bundle.

### La transizione Gradle (2014–2016)

Nel 2014–2015, come per il core, il framework migra da Ant a Gradle. Il lavoro qui è particolarmente delicato perché i bundle OSGi richiedono manifesti precisi e dipendenze dichiarate esplicitamente. Il commit [`45ae8049`](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5) rimuove tutti i `MANIFEST.MF` manuali, delegando la generazione a Gradle.

Nel 2016 viene rimossa l'istruzione `Bundle-RequiredExecutionEnvironment: JavaSE-1.7` da tutti i moduli ([`65c3efd1`](https://github.com/freeplane/freeplane/commit/65c3efd11bdf90445eab566ba9ef710eecda071d)), liberando il progetto dal vincolo esplicito di Java 7. Nello stesso anno viene risolto un bug di Knopflerfish che causava problemi all'avvio ([`c54e57da`](https://github.com/freeplane/freeplane/commit/c54e57dadccffe0168f73feb5c6f58c4c45a8f95)).

### Il salto a Java moderno (2018–2022)

Il 2018 introduce un cambiamento importante: l'API pubblica viene separata strutturalmente da tutti gli altri moduli con il vincolo esplicito che `freeplane_api` non deve dipendere da nessun altro package di Freeplane ([`42e21482`](https://github.com/freeplane/freeplane/commit/42e214828ff405b0a71adca6f169d13e290b58dd)). Questo è il momento in cui l'architettura acquisisce la forma che ha oggi: `freeplane_api` come layer di contratto puro, isolato.

Nel 2020 viene aggiunto il supporto per VAqua 9 (look-and-feel macOS) ([`063077bd`](https://github.com/freeplane/freeplane/commit/063077bd4ebfce0903a83203e810f37d9e0d62d7)). Nel 2021 vengono aggiornate le icone dell'applicazione. Nel 2022 il framework supporta Java 15, 16 e 17 ([`64bd241e`](https://github.com/freeplane/freeplane/commit/64bd241ed2e99fd98ee2b5cebcf1ebe96423f0bb)) e viene creata la prima distribuzione Windows con Java runtime bundled ([`07b76b95`](https://github.com/freeplane/freeplane/commit/07b76b95b6711a5467fcf13bebd270b175e9475f)).

### La modernizzazione del build (2024–2025)

Nel 2024 arriva il supporto per eseguire Freeplane sia su Java 8 che su Java 11 su Windows ([`8fe2aa54`](https://github.com/freeplane/freeplane/commit/8fe2aa54115a5805935fec5f47c06141b84e7f29)) — scelta compatibilistica per gli utenti enterprise bloccati su versioni vecchie di Java. Nel 2025 vengono corretti i problemi di compatibilità con Gradle 9.0 ([`bad0e0cd`](https://github.com/freeplane/freeplane/commit/bad0e0cddbfc0fae7824d19acc61687d4294aebf)), che richiedeva la riscrittura di alcune API di build deprecate — un commit generato con assistenza di Claude Code, come indicato nel body del commit.

---

## 3. `freeplane_plugin_script` — Lo scripting Groovy

**550 commit rilevanti su 1290 totali**, copertura 2009–2026. È il plugin più attivo dopo il core.

### La nascita: da bozza a strumento potente (2009–2011)

I primi commit del plugin script risalgono al 2009 e mostrano un sistema ancora rudimentale. Il linguaggio supportato è Groovy, e l'integrazione con il modello di Freeplane avviene tramite oggetti "proxy" che wrappano le entità interne esponendole allo script. Il 2011 è l'anno d'oro dello scripting con 105 commit rilevanti — la fase in cui il sistema di proxy (i `NodeProxy`, `MapProxy`, `ControllerProxy`) viene definito nella sua forma essenziale.

In questo periodo viene costruito il meccanismo di sicurezza basato su `freeplane.policy`: gli script vengono eseguiti in un contesto Java Security Manager che limita le operazioni potenzialmente pericolose. La politica viene raffinata continuamente negli anni successivi.

### La maturità dell'API script (2012–2016)

Il 2012–2013 è il periodo in cui il plugin script raggiunge una prima maturità. Il meccanismo di menu e binding degli script ai comandi dell'utente viene consolidato. Si lavora molto sulla compatibilità tra versioni di Groovy e sul sistema di compilazione degli script.

Nel 2014 avviene la migrazione alla nuova struttura Gradle, che introduce anche una separazione più netta tra il runtime di Groovy (incluso come bundle OSGi separato) e il plugin stesso. Vengono anche aggiunti i `testCompile` dependencies nel 2017 ([`6833cbc2`](https://github.com/freeplane/freeplane/commit/6833cbc2bdd3f674675aeee2120ebd8374d93829)), segnale che il codice del plugin inizia ad essere testato sistematicamente.

### Il bloom dell'API pubblica (2018–2019)

Il 2018 è il momento più denso per lo scripting con 65 commit rilevanti. In questo periodo viene ridefinita l'API di scripting in profondità: i metodi vengono rinominati per maggiore consistenza (`newMap` → `openMap`, `hiddenMap` → `headlessMap`, `loader` → `mapLoader`) in una serie di `api_change` che rompono la backward compatibility — segnale che il team ha deciso di investire nella qualità a lungo termine accettando di rompere gli script esistenti.

Il 2019 introduce `MapLoader` come API stabile per caricare mappe da script ([`d2c45816`](https://github.com/freeplane/freeplane/commit/d2c458160eb4a8a1bdb2004903315b5d7c20c444)), e rinomina definitivamente `Map` in `MindMap` nell'interfaccia pubblica ([`04b99850`](https://github.com/freeplane/freeplane/commit/04b9985053bac60f98a4bbf2404b4e818d26993a)).

### L'espansione dell'API (2020–2023)

Il 2022 è un anno particolarmente ricco: vengono implementati il modello di layout dei nodi (stacked, flow, etc.) accessibile via script ([`4f2aef94`](https://github.com/freeplane/freeplane/commit/4f2aef9423a4ae60c225b7609bfb56f99a4ad69a)), le `ConditionalStyles` tramite API ([`61f92526`](https://github.com/freeplane/freeplane/commit/61f9252654b98faee1433e98a562c3b43392d016)), e la distanza base dei nodi figli ([`06614fd5`](https://github.com/freeplane/freeplane/commit/06614fd5dfa0721230b09c7fa1f49c63a0ea4c36)). Arriva anche la possibilità di lanciare script da riga di comando con l'opzione `-R` ([`b0316941`](https://github.com/freeplane/freeplane/commit/b0316941c74c738a8beedf46b944b29b21a72528)), che trasforma Freeplane in uno strumento batch scriptabile.

Nel 2023 vengono aggiunti i metodi `getBranchAsTextOutline` e `appendTextOutlineAsBranch` ([`023d7d9d`](https://github.com/freeplane/freeplane/commit/023d7d9de5adcccd492e2f2b3c0f1c14b29d9f95)) — operazioni di import/export testuale del ramo che aprono nuove possibilità di integrazione con editor esterni.

Nel 2023 viene anche risolto un problema delicato con i percorsi relativi per le risorse esterne negli script ([`ca0c9524`](https://github.com/freeplane/freeplane/commit/ca0c95243801593441f6492ef03e995f0782caf7)), necessario per l'add-on `PackAndGo`.

### I tag e i bookmark (2024–2025)

Il 2024 porta il sistema di **tag categories** nell'API script: i tag possono essere organizzati in categorie con colori e filtri ([`0469cdfd`](https://github.com/freeplane/freeplane/commit/0469cdfd525609755cf7567e1fc41dab33583209)). Nel 2025 arrivano nell'API i **bookmark** come entità di prima classe ([`c7cf203a`](https://github.com/freeplane/freeplane/commit/c7cf203af1717dfd3a21c45b6b716f6f1e5b3e00)), la proprietà `underline` ([`67ea65c1`](https://github.com/freeplane/freeplane/commit/67ea65c12d85fa07961f2109450e7d7b9a16d0f2)) e il fix del nome `strikethrough` (con spiegazione linguistica inclusa nel commit body — una rarità gustosa).

Nel 2026 le tag categories vengono esposte anche agli strumenti AI tramite un `TagCategoryAccess` condiviso tra UI, script e AI ([`b4726030`](https://github.com/freeplane/freeplane/commit/b4726030e23aea19368d720fcd54787c69ebce51)).

---

## 4. `freeplane_plugin_svg` — Grafica vettoriale e PDF

**43 commit rilevanti su 159 totali**, copertura 2009–2025.

### Le origini: immagini embedded (2009–2012)

Il plugin SVG nasce per consentire l'inserimento di immagini vettoriali nei nodi di Freeplane, usando la libreria Apache Batik per il rendering. I primissimi commit riguardano fix di base: calcolo della dimensione delle immagini, gestione della risoluzione per l'export PDF ([`d19bb1d8`](https://github.com/freeplane/freeplane/commit/d19bb1d87d20a78eca34bb95c4bb95704c3307c1)), correzione dei package import dopo ristrutturazioni del core ([`6ae393fb`](https://github.com/freeplane/freeplane/commit/6ae393fbec2eae1899a3a21fa538f27e83425fb7)).

### Il refactoring del viewer (2014)

Il 2014 è l'anno più intenso per il plugin SVG (9 commit rilevanti). Viene riscritto il sistema di `ViewerComponent` che gestisce la visualizzazione delle immagini scalabili. Il commit [`42732cd4`](https://github.com/freeplane/freeplane/commit/42732cd4b39371b9ab885eff493d494ef9e1f976) documenta il motivo del refactoring: "Removed unnecessary methods due to the updating of the Scalr classes. Now the scalable component implementations are responsible for centring their images." Il commit [`2eea90dd`](https://github.com/freeplane/freeplane/commit/2eea90dd5f4c06ca00fb13642a8be9e41097e4f1) introduce un workaround per l'opzione "fit to zoom" e limita la dimensione massima del viewer per evitare errori "out of memory" — problema reale su mappe con molte immagini grandi.

Nello stesso anno viene spostato il plugin alla nuova struttura Gradle ([`8d27d685`](https://github.com/freeplane/freeplane/commit/8d27d6855f2a1a5772ff38272070646bd2c6737d)).

### Il problema cronico dell'export PDF (2013–2024)

Una delle storyline più interessanti del plugin SVG è la lotta decennale con l'export PDF. Il primo fix risale al 2013 con [`f4c963b4`](https://github.com/freeplane/freeplane/commit/f4c963b41c1e306ce1b61575179937bd358e5218): "fix PDF/SVG Export when using GTK/Nimbus L&Fs and node attributes". Questo fix viene poi **revertato** nel 2024 con il commit [`93af3ff1`](https://github.com/freeplane/freeplane/commit/93af3ff1a5ed81e05ed29ac7889e0035586c35db) perché causava un altro bug — i font del menu crescevano ad ogni export PDF. Il body del commit è una rarità: "It reverts a bug fix from 2013-12-02 and relates to issue #1920 'Freeplane menu fonts are increased each time File > Export > PDF is used'". Undici anni per chiudere il cerchio.

Nel 2019 viene aggiornata la libreria FOP alla versione 2.4, ma questa introduce immediatamente un nuovo bug ([`f0c2c90b`](https://github.com/freeplane/freeplane/commit/f0c2c90b084b5c1d626caa83f645c84491f22ebb)) che richiede un workaround specifico.

### Il fix degli sfondi SVG e il dark mode (2020–2022)

Nel 2020 vengono corretti problemi gravi con gli sfondi SVG e le immagini nelle anteprime ([`02b5f924`](https://github.com/freeplane/freeplane/commit/02b5f924779846aff5dd9bfcf7c126b84a55dbcb), [`65d1fe0f`](https://github.com/freeplane/freeplane/commit/65d1fe0f7cb233dc6d1baf30f394d606723ef8c0)). Nel 2022 viene sostituito il look-and-feel Darcula con FlatDarcula ([`40eb7bdf`](https://github.com/freeplane/freeplane/commit/40eb7bdfd07db8ecfd5424ba4f765be268a7428e)) — cambiamento che tocca trasversalmente il plugin SVG perché molti workaround esistenti erano specifici per Darcula.

---

## 5. `freeplane_plugin_openmaps` — La mappa dentro la mappa

**20 commit rilevanti su 82 totali**, copertura 2012–2022.

### La nascita: un esperimento geografico (2012)

OpenMaps è il plugin più "di nicchia" dell'ecosistema Freeplane. Nasce nel 2012 come contributo esterno — probabilmente di un singolo sviluppatore — con l'obiettivo di embedded una mappa OpenStreetMap interattiva nei nodi. I commit del 2012 rivelano un plugin giovane e instabile: tre fix in una settimana ([`c2288b9a`](https://github.com/freeplane/freeplane/commit/c2288b9a3a110abad26d495cf6df7e3168b018b1), [`c6f9d625`](https://github.com/freeplane/freeplane/commit/c6f9d62586c8749d4a762aae2b6ef4e4d27698a5), [`8d89b703`](https://github.com/freeplane/freeplane/commit/8d89b7031513fbdf9332fe494b7edf2868960b03)) per "various bug fixes", "fixed bug in storing the zoom", "Fixed missing OpenMapsNodeHookAction.text bug".

Il commit [`004ee3f7`](https://github.com/freeplane/freeplane/commit/004ee3f752d4b9e025c9abe67befdd373c37d133) introduce un controller per il doppio clic per aggiungere coordinate, passando alla classe `Coordinate` della libreria JMapViewer. Il commit [`5b1416d3`](https://github.com/freeplane/freeplane/commit/5b1416d3a7e72db9639fecd734ca6ed50e9302f3) aggiunge un listener per la selezione di luoghi tramite loop — un approccio interattivo per scegliere la posizione sulla mappa.

### L'integrazione nell'ecosistema (2014–2016)

Nel 2014 il plugin viene migrato alla nuova struttura Gradle e integrato nel meccanismo di `IconMouseListener` ([`83e5bd24`](https://github.com/freeplane/freeplane/commit/83e5bd24bfe85be7247b05042907554850433527)): il click sull'icona di un nodo che ha coordinate geografiche apre il viewer OpenMaps. Questo è il momento in cui OpenMaps smette di essere un esperimento e diventa una feature vera, accessibile dall'interfaccia standard.

Il commit [`7c7bdca9`](https://github.com/freeplane/freeplane/commit/7c7bdca9ab49dc012dd5c00ca732131aea0eee99) documenta onestamente la situazione con la libreria: "Moved OpenMaps plugin to the new directory structure, **couldn't find a maven repo for openm**[aps]" — la libreria JMapViewer deve essere inclusa manualmente nel bundle perché non è disponibile su Maven Central.

### La stabilizzazione silenziosa (2016–2022)

Dopo il 2016 l'attività sul plugin si riduce drasticamente. I commit rilevanti sono pochi e si concentrano su aggiornamenti del build system e fix marginali. Il fix più interessante è del 2019 ([`5d541e27`](https://github.com/freeplane/freeplane/commit/5d541e27673112557fcb9dd0f68a52749fea496b)): "Fix OpenMapsViewer by setting Freeplane specific user agent". OpenStreetMap aveva iniziato a bloccare le richieste senza un User-Agent identificativo — il plugin doveva presentarsi correttamente per non essere bannato dai tile server.

Nel 2022 il plugin riceve il supporto a Java 17 ([`4b16c43d`](https://github.com/freeplane/freeplane/commit/4b16c43db17fd5af83f196b5f5e0156132090612)), ma non vengono aggiunte nuove funzionalità. È un plugin "in manutenzione": funziona, è usato da una nicchia di utenti, e non riceve investimenti attivi.

---

## 6. `other` — Il cantiere trasversale

**471 commit rilevanti su 1803 totali**, copertura 2009–2026.

### Che cos'è "other"?

Il bucket `other` raccoglie i commit che toccano aree trasversali non riconducibili a un singolo plugin: il build system, le traduzioni, la CI/CD, la documentazione di progetto, e — negli ultimi anni — l'intero plugin AI. È un indicatore della salute sistemica del progetto: quando `other` è molto attivo, il progetto sta attraversando una fase di ristrutturazione infrastrutturale o di esplorazione di nuove aree.

### Le grandi migrazioni (2013–2015)

Il 2013 è l'anno con più commit rilevanti nel bucket `other` (59): è il periodo della migrazione da Ant a Gradle, che richiede decine di commit su `build.gradle`, `build.xml`, file di configurazione Eclipse, template di progetto. Ogni singolo plugin deve essere migrato e i manifesti OSGi devono essere rigenerati.

Nel 2015 arriva la rimozione di tutti i `MANIFEST.MF` manuali ([`45ae8049`](https://github.com/freeplane/freeplane/commit/45ae804948fb0c8ec5efa48bfb1e529544aa03e5)) e l'aggiunta dei task Gradle per le impostazioni Eclipse ([`1c7cc029`](https://github.com/freeplane/freeplane/commit/1c7cc0294929f1029e8e0930771f41969fdf1668)). Il 2015 ha 55 commit rilevanti in `other` — la fase finale della migrazione al build moderno.

### Le traduzioni come proxy dell'adozione (2009–2022)

Una parte significativa dei commit `other` riguarda le traduzioni. Questo è un proxy interessante per misurare la diffusione del software: quando una lingua nuova appare, significa che Freeplane ha raggiunto quella comunità. Le lingue arrivano in tempi diversi: il croato al 99.8% già nel 2013, l'ungherese al 30% nello stesso anno, il portoghese brasiliano in crescita costante.

### L'esplosione AI (2025–2026)

Il 2026 è dominato dal plugin AI, che per ragioni classificatorie finisce in `other` (non esiste un `freeplane_plugin_ai` come modulo separato nella naming convention del tool). I 53 commit rilevanti del 2026 in `other` includono: l'implementazione di strumenti AI per creare/spostare nodi ([`202608fc`](https://github.com/freeplane/freeplane/commit/202608fcca073d4ac2639e35192763ac07266a43)), l'aggiunta di strumenti per leggere il contesto della mappa, l'implementazione di un sistema di profili per gli assistenti AI ([`eec8e09c`](https://github.com/freeplane/freeplane/commit/eec8e09c756f27390b4859e4761a8baa555b3e36)), e la gestione della cronologia delle chat con transcript persistenti.

Notabile: il file `AGENTS.md` compare nel 2026 come documento di "costituzione" del progetto per gli agenti AI — un meta-documento che descrive le regole operative per i contributi automatizzati.

---

## 7. Come comunicano i plugin? Core o API pubblica?

Questa è la domanda architettuale più interessante. La risposta è **stratificata nel tempo** e dipende dal tipo di plugin.

### La risposta breve

I plugin usano **entrambi** i canali, ma in modo diverso a seconda dell'era e del tipo di plugin:

- **Plugin "legacy" (openmaps, svg, bugreport, jsyntaxpane)**: comunicano prevalentemente con il **core interno**, tramite classi e interfacce del package `org.freeplane.features.*`. Non passano dall'API pubblica.
- **Plugin "scripting-oriented" (script, formula)**: comunicano attraverso l'**API pubblica** (`freeplane_api`), che è il contratto stabile esposto agli script Groovy.
- **Plugin "content viewer" (svg, latex, markdown)**: comunicano col core tramite il sistema di **hook** (`PersistentNodeHook`, `ViewerController`, `NodeHook`) — un meccanismo interno che precede l'API pubblica.

### Le evidenze nei commit

**1. Il vincolo del 2018: `freeplane_api` viene isolata**

Il commit chiave è [`42e21482`](https://github.com/freeplane/freeplane/commit/42e214828ff405b0a71adca6f169d13e290b58dd) del giugno 2018: "freeplane api package must not depend on any other freeplane packages". Prima di questo commit, `freeplane_api` importava classi da `freeplane_core`. Dopo, diventa un layer completamente autonomo — solo interfacce Java pure, senza dipendenze interne.

Questo vincolo è fondamentale: significa che i plugin che usano `freeplane_api` ottengono un contratto stabile indipendente dalle refactoring interne del core.

**2. Il meccanismo dei proxy (scripting)**

Il plugin script non chiama direttamente le classi del core. Usa classi come `NodeProxy`, `MapProxy`, `ControllerProxy` che implementano le interfacce dell'API pubblica (`Node`, `MindMap`, `Controller`) wrappando i corrispondenti oggetti interni. Questa mediazione è esplicita: quando nel 2022 viene aggiunto il supporto per i layout dei nodi via script ([`4f2aef94`](https://github.com/freeplane/freeplane/commit/4f2aef9423a4ae60c225b7609bfb56f99a4ad69a)), il lavoro coinvolge sia le interfacce in `freeplane_api` sia le implementazioni proxy in `freeplane_plugin_script`.

**3. Il meccanismo degli hook (SVG, Latex, OpenMaps)**

I plugin come SVG e OpenMaps usano il sistema di `NodeHook` per agganciarsi al lifecycle del nodo. Classi come `SvgViewerFactory`, `LatexNodeHook`, `OpenMapsNodeHook` implementano interfacce del core (`IViewerFactory`, `INodeHook`) — non dell'API pubblica. Questo è il canale "legacy" di comunicazione, che non passa da `freeplane_api`.

Il commit sul SVG [`24581795`](https://github.com/freeplane/freeplane/commit/2458179551f40a19af50810e28ffc997b4cfb815) mostra una `NullPointerException` direttamente nel stack trace di `SvgViewerFactory` che chiama `ExternalResource.setZoom` — una classe interna del core. Il plugin SVG conosce e usa i dettagli interni del core.

**4. Il `ViewerController` come mediatore**

Un elemento interessante emerge dal file `freeplane_plugin_latex.md`: il commit [`3de9d1e2`](https://github.com/freeplane/freeplane/commit/3de9d1e2cedcb46254e6999d3ee8ad32a67e491c) del 2025 risolve un "class cast exception" in `ViewerController.java` e `LatexNodeHook.java`. `ViewerController` è un componente del core che gestisce la visualizzazione dei contenuti speciali (immagini, SVG, LaTeX) e funge da registry per i factory dei viewer. I plugin "viewer" si registrano presso questo controller — è una forma di dependency injection interna al core, non mediata dall'API pubblica.

**5. Il caso OpenMaps: dipendenza diretta da classi UI del core**

Il commit [`16fcbdd5`](https://github.com/freeplane/freeplane/commit/16fcbdd5b46e791b3a455ee577c2b05f0bd756f7) del 2017 modifica `FButtonBar.java` e `AttributeController.java` — classi del core. Questo fix coinvolge anche OpenMaps, che dipende da `IconMouseListener` definito nel core. È il caso più netto di comunicazione diretta core→plugin tramite meccanismi interni.

### Schema riassuntivo

```
                 ┌─────────────────────────────────┐
                 │       freeplane_framework        │
                 │   (OSGi lifecycle, class loading) │
                 └──────────────┬──────────────────┘
                                │ carica e isola
           ┌────────────────────┼────────────────────┐
           │                   │                    │
    ┌──────▼──────┐    ┌───────▼──────┐    ┌───────▼───────┐
    │freeplane_api│    │freeplane_core│    │  plugin_svg   │
    │ (contratto  │◄───│  (impl. di   │◄───│  plugin_latex │
    │  stabile)   │    │  freeplane_  │    │  openmaps     │
    └──────▲──────┘    │   api)       │    │  (hook/viewer)│
           │           └──────▲───────┘    └───────────────┘
           │                  │
    ┌──────┴──────────────────┴───────┐
    │     freeplane_plugin_script     │
    │  (proxy che implementano la api │
    │   e delegano al core)           │
    └─────────────────────────────────┘
```

In sintesi: **i plugin di visualizzazione e integrazione esterna (SVG, LaTeX, OpenMaps) passano per il core interno tramite hook e factory registrate**. **I plugin di automazione (script, formula) passano per l'API pubblica tramite il pattern proxy**. Il framework OSGi garantisce l'isolamento dei classloader, ma non impedisce le dipendenze dirette al core per i plugin "trusted" distribuiti nel bundle ufficiale.

L'API pubblica è quindi **non l'unico canale** di comunicazione, ma è il **canale stabile e documentato** pensato per gli script utente e per i plugin di terze parti che non vogliono dipendere dai dettagli implementativi interni.