# CLAUDE.md

## Identità del progetto

**Nome:** Habit Tracker
**Tipo:** Applicazione Python — CLI
**Scopo:** Supportare l'utente nella fase di adozione di nuove abitudini, tracciandone l'andamento e fornendo segnali per capire cosa funziona e cosa no.

**Contesto per Claude Code:**
Stai lavorando su un progetto Python strutturato con documentazione formale MkDocs e vault Obsidian.
Il tuo ruolo è duplice: supporto all'analisi dei requisiti e supporto allo sviluppo.
Segui sempre le regole di questo file. In caso di dubbio, chiedi prima di agire.

\---

## Struttura del vault

```
project-root/
├── CLAUDE.md               ← questo file
├── raw/                    ← materiale grezzo in input (NON modificare i file esistenti)
│   ├── meetings/           ← note di meeting da analizzare
│   ├── brainstorm/         ← idee informali e appunti
│   └── manifest.md         ← registro implicito dei file analizzati (aggiornato da /analyze)
├── docs/                   ← documentazione formale (output)
│   ├── index.md            ← home del progetto + tabella user stories
│   ├── business/
│   │   └── objectives.md   ← obiettivi di business
│   ├── user-stories/
│   │   └── US-\\\*.md         ← user stories con RF e AC in Gherkin
│   ├── requirements/
│   │   ├── non-functional.md  ← requisiti non funzionali
│   │   └── business-rules.md ← business rule condivise
│   ├── changes/
│   │   └── CR-\\\*.md         ← change request
│   ├── decisions/
│   │   └── ADR-\\\*.md        ← architecture decision records
│   ├── architecture/
│   │   ├── overview.md     ← componenti principali e diagramma sistema
│   │   ├── data-model.md   ← entità dati e relazioni (con diagramma ER Mermaid)
│   │   └── class-diagram.md ← diagramma classi (generato da /generate-arch)
│   └── setup.md            ← guida installazione
├── wiki/                   ← knowledge base di lavoro (mantenuta da Claude Code)
│   ├── requirements/       ← requisiti estratti da raw/ in lavorazione
│   ├── decisions/          ← decisioni in bozza
│   └── concepts/           ← glossario del dominio
├── graphify-out/           ← output Graphify (NON modificare manualmente)
│   ├── graph.json
│   └── GRAPH\\\_REPORT.md
├── src/                    ← codice sorgente Python
├── templates/              ← template Obsidian
└── logs/                   ← log delle sessioni di lavoro
```

**Regola fondamentale sulla struttura:**

* `raw/` è input — non modificare mai i file esistenti, solo leggerli
* `wiki/` è lavoro in corso — puoi creare e modificare liberamente
* `docs/` è output formale — modifica solo su comando esplicito o dopo conferma
* `graphify-out/` è generato automaticamente — non toccare mai

**Convenzione file grezzi analizzati:**
Un file in `raw/` si considera analizzato quando esiste un file corrispondente in
`wiki/requirements/` con il nome della fonte nel filename
(es. `raw/meetings/kickoff.md` → `wiki/requirements/2026-05-20-kickoff.md`).
Non modificare i file in `raw/` per segnalarne lo stato: la traccia vive nel wiki
e in `raw/manifest.md`.

\---

## Modi operativi

### Modalità Analista

Attiva quando lavori su requisiti, user stories, business rules, change request.

* Leggi sempre `docs/index.md` per il contesto delle US esistenti
* Leggi sempre `docs/requirements/business-rules.md` prima di formalizzare nuovi requisiti
* Segnala sempre ambiguità, sovrapposizioni e dipendenze prima di salvare
* Chiedi conferma prima di scrivere in `docs/`

### Modalità Sviluppatore

Attiva quando lavori su codice, architettura, debugging.

* Leggi sempre `graphify-out/GRAPH\\\_REPORT.md` all'inizio della sessione (se disponibile)
* Leggi sempre `docs/architecture/overview.md` per il contesto architetturale corrente (se disponibile)
* Leggi sempre `logs/` per capire il contesto delle sessioni precedenti
* Segui le convenzioni di `docs/decisions/ADR-\\\*.md` per scelte architetturali

\---

## Comandi

### /start

**Scopo:** Riprendere il lavoro da dove si era interrotto.
**Azioni:**

1. Leggi gli ultimi 3 file in `logs/` ordinati per data
2. Leggi `docs/index.md` per lo stato corrente delle US
3. Produci un sommario: cosa è stato fatto, cosa è in sospeso, cosa è il prossimo passo suggerito

\---

### /query "\[domanda]"

**Scopo:** Rispondere a una domanda sul progetto cercando nelle fonti documentali rilevanti.
**Azioni:**

1. Analizza la domanda e identifica il tipo di risposta cercata:

   * Decisione presa → leggi `docs/decisions/ADR-\\\*.md`
   * Comportamento del sistema / requisito → leggi `docs/user-stories/US-\\\*.md` e `docs/requirements/business-rules.md`
   * Criteri di accettazione / test → leggi le sezioni Gherkin nelle US pertinenti
   * Obiettivo di business → leggi `docs/business/objectives.md`
   * Storico sessioni / cosa è stato fatto → leggi tutti i file in `logs/`
   * Stato di un artefatto → leggi `docs/index.md` poi il file specifico
   * Concetto di dominio → leggi `wiki/concepts/` e `docs/requirements/business-rules.md`
2. Prima di leggere i file completi, scansiona gli indici:

   * Leggi `docs/index.md` per identificare US pertinenti per titolo
   * Elenca i file ADR disponibili in `docs/decisions/`
   * Elenca i file in `wiki/` pertinenti per nome
3. Leggi solo i file rilevanti identificati nel passo 2 — non leggere tutto
4. Produci la risposta:

   * Rispondi in modo diretto e sintetico
   * Cita sempre la fonte: file e sezione specifica (es. "secondo ADR-002, sezione Decisione")
   * Se la risposta non è presente nella documentazione, dichiaralo esplicitamente
   * Se la documentazione è ambigua o incompleta su quel punto, segnalalo
   * Se ci sono fonti che si contraddicono, mostralo
5. In fondo alla risposta, elenca i file consultati con il path completo

Esempi di utilizzo:

* `/query "come è stato deciso di gestire l'assimilazione di un habit?"`
* `/query "ci sono criteri di accettazione delle ultime US non ancora compilati?"`
* `/query "quali business rule si applicano alla registrazione serale?"`

\---

### /save

**Scopo:** Chiudere la sessione corrente con un log strutturato.
**Azioni:**

1. Crea un file `logs/YYYY-MM-DD-HH-MM.md` con:

   * Cosa è stato fatto in questa sessione
   * Artefatti creati o modificati (con path)
   * Decisioni prese
   * Questioni aperte o da riprendere
2. Conferma il salvataggio

\---

### /add-us "\[testo informale]"

**Scopo:** Formalizzare una user story e salvarla nella struttura docs.
**Azioni:**

1. Leggi tutti i file `docs/user-stories/US-\\\*.md` per identificare l'ID successivo e le US esistenti
2. Formalizza la user story nel formato: *"Come \[utente], voglio \[azione], così da \[beneficio]"*
3. Assegna ID progressivo (es. US-017)
4. Compila il template US (vedi sezione Template)
5. Identifica dipendenze con US esistenti
6. Segnala eventuali sovrapposizioni o ambiguità
7. Mostra la bozza e chiedi conferma prima di salvare in `docs/user-stories/US-NNN.md`
8. Dopo conferma, aggiorna la tabella in `docs/index.md`

\---

### /add-rf \[US-ID]

**Scopo:** Estrarre e formalizzare i requisiti funzionali per una user story.
**Azioni:**

1. Leggi il file `docs/user-stories/\\\[US-ID].md`
2. Leggi `docs/requirements/business-rules.md` per verificare BR applicabili
3. Proponi i requisiti funzionali con formalismo "Il sistema deve/dovrebbe/può"
4. Assegna ID progressivi (es. RF-017-01, RF-017-02...)
5. Segnala se un RF dipende da o contraddice RF esistenti in altre US
6. Mostra la bozza e chiedi conferma prima di aggiornare il file

\---

### /add-nfr "\[descrizione]"

**Scopo:** Aggiungere un requisito non funzionale.
**Azioni:**

1. Leggi `docs/requirements/non-functional.md`
2. Classifica il NFR per categoria: Performance, Sicurezza, Usabilità, Manutenibilità, Portabilità
3. Assegna ID progressivo (es. NFR-001)
4. Verifica se il NFR impatta US esistenti e segnalalo
5. Mostra bozza e chiedi conferma prima di salvare

\---

### /add-ac \[US-ID]

**Scopo:** Generare criteri di accettazione in formato Gherkin per una user story.
**Azioni:**

1. Leggi `docs/user-stories/\\\[US-ID].md` — user story e RF
2. Genera scenari Gherkin (Given / When / Then) per ogni RF significativo
3. Includi scenari happy path e scenari di errore
4. Mostra bozza e chiedi conferma prima di aggiornare il file US

\---

### /analyze \[file o testo]

**Scopo:** Analizzare materiale grezzo ed estrarre requisiti, vincoli e business rule.
**Azioni:**

1. Leggi il file indicato da `raw/` (o elabora il testo fornito)
2. Estrai e classifica:

   * **Requisiti candidati** — cosa il sistema deve fare
   * **Vincoli** — limitazioni tecniche, temporali, normative
   * **Business rule** — regole di dominio applicabili a più contesti
   * **Ambiguità** — affermazioni non chiare che richiedono chiarimento
3. Salva l'analisi in `wiki/requirements/YYYY-MM-DD-\\\[nome-fonte].md`
4. Per ogni business rule candidata, verifica se è già in `docs/requirements/business-rules.md`
5. Aggiorna `raw/manifest.md` aggiungendo una riga con: file analizzato, data, path output in wiki
6. Produci un sommario e chiedi come procedere

\---

### /analyze-mockup \[file]

**Scopo:** Analizzare uno schema, wireframe o mockup ed estrarre requisiti impliciti.
**Azioni:**

1. Analizza il file visivo fornito (immagine, canvas Obsidian `.canvas`, PDF, descrizione testuale)
2. Identifica: componenti UI, flussi di navigazione, stati, validazioni implicite
3. Mappa ogni elemento a requisiti funzionali candidati
4. Segnala elementi non coperti dalle US esistenti
5. Salva l'analisi in `wiki/requirements/YYYY-MM-DD-mockup-\\\[nome].md`
6. Aggiorna `raw/manifest.md` con il file analizzato
7. Chiedi come procedere con gli elementi non coperti

\---

### /add-goal "\[obiettivo]"

**Scopo:** Formalizzare un obiettivo di business.
**Azioni:**

1. Leggi `docs/business/objectives.md`
2. Assegna ID progressivo (es. OB-001)
3. Formalizza con: descrizione, metrica di successo se identificabile, US collegate
4. Mostra bozza e chiedi conferma prima di salvare

\---

### /set-status \[ID] \[nuovo-stato]

**Scopo:** Cambiare lo stato di un requisito, user story o altro artefatto.
**Stati validi per US:** Bozza → In revisione → Approvata → Implementata → Suddivisa → Obsoleta
**Stati validi per RF:** Proposto → Approvato → Implementato → Eliminato
**Stati validi per CR:** Aperta → In valutazione → Approvata → Rifiutata → Chiusa
**Stati validi per OB:** Proposto → Approvato → Raggiunto → Abbandonato
**Azioni:**

1. Individua il file corretto dall'ID
2. Verifica che il nuovo stato sia valido per il tipo di artefatto
3. Aggiorna il campo Stato nei metadati
4. Aggiorna la Data ultima modifica
5. Aggiorna la tabella in `docs/index.md` se applicabile
6. Logga la modifica con data e motivazione nel file
7. Mostra le modifiche e chiedi conferma prima di salvare

\---

### /split-us \[US-ID]

**Scopo:** Suddividere una user story troppo grande in storie più piccole e gestibili.
**Azioni:**

1. Leggi il file `docs/user-stories/\\\[US-ID].md`
2. Analizza la US e proponi una suddivisione in storie più piccole, motivando i criteri di split
3. Per ogni storia derivata proposta:

   * Assegna ID progressivo nuovo (es. US-017, US-018...)
   * Proponi come vengono ridistribuiti i RF dell'originale tra le derivate
   * Segnala RF che vanno modificati o raffinati nella derivata rispetto all'originale
   * Segnala RF che non trovano posto in nessuna derivata (richiedono attenzione)
4. Mostra il piano completo di split e chiedi conferma prima di procedere
5. Dopo conferma:

   * Crea i file delle storie derivate con il template US, stato "Bozza" e dipendenza "Derivata da \[US-ID]"
   * In ogni derivata, i RF ereditati o modificati hanno stato "Proposto"
   * Aggiorna la US originale:

     * Stato → "Suddivisa"
     * Rimuovi lo stato dai RF (diventano archivio storico senza stato attivo)
     * Aggiungi sezione "Storie derivate" con link alle nuove US
   * Aggiorna la tabella in `docs/index.md` con le nuove US e lo stato aggiornato dell'originale

\---

### /add-cr "\[descrizione del cambiamento]"

**Scopo:** Aprire una change request formale.
**Azioni:**

1. Leggi `docs/changes/` per identificare l'ID successivo
2. Compila il template CR (vedi sezione Template)
3. Identifica gli artefatti impattati (US, RF, BR, ADR)
4. Valuta l'impatto: Basso / Medio / Alto
5. Mostra bozza e chiedi conferma prima di salvare in `docs/changes/CR-NNN.md`

\---

### /generate-arch \[target?]

**Scopo:** Generare o aggiornare la documentazione tecnica in `docs/architecture/`.
**Target disponibili:** `class-diagram`, `data-model`, `overview` (default: tutti e tre)
**Azioni per `class-diagram`:**

1. Leggi tutti i file `.py` in `src/`
2. Identifica: classi, metodi pubblici, attributi, relazioni (ereditarietà, composizione, dipendenza)
3. Genera un diagramma Mermaid `classDiagram` completo
4. Mostra il diagramma e chiedi conferma
5. Dopo conferma, salva in `docs/architecture/class-diagram.md`

**Azioni per `data-model`:**

1. Leggi i file di schema dati (dataclass, modelli Pydantic, file `.json` di esempio, JSON schema)
2. Documenta: entità principali, campi, tipi, relazioni tra entità
3. Genera un diagramma Mermaid `erDiagram`
4. Mostra bozza e chiedi conferma
5. Dopo conferma, salva in `docs/architecture/data-model.md`

**Azioni per `overview`:**

1. Leggi `src/` per identificare i moduli principali
2. Leggi `docs/decisions/ADR-\\\*.md` per decisioni architetturali rilevanti
3. Leggi `graphify-out/GRAPH\\\_REPORT.md` se disponibile
4. Scrivi una descrizione dei componenti principali, le loro responsabilità e come interagiscono
5. Includi un diagramma Mermaid `graph TD` dei componenti
6. Mostra bozza e chiedi conferma
7. Dopo conferma, salva in `docs/architecture/overview.md`

**Regole comuni:**

* Non modificare mai file esistenti in `docs/architecture/` senza mostrare la bozza e ottenere conferma
* Se un file esiste già, mostra le differenze rispetto alla versione precedente prima di aggiornarlo
* Aggiungi sempre in fondo al file: `\\\*Generato automaticamente il YYYY-MM-DD — aggiornare dopo ogni refactor significativo.\\\*`
* Usa sempre Mermaid per i diagrammi (compatibile con MkDocs Material)
* Documenta in italiano

\---

\### /setup-arch

\*\*Scopo:\*\* Avviare un processo guidato di configurazione architetturale del progetto.

Produce decisioni formalizzate come ADR, struttura iniziale di `src/` e documentazione in `docs/architecture/`.

Il processo si svolge in fasi sequenziali con conferma esplicita tra una e l'altra.



\*\*FASE 1 — Lettura contesto\*\*

1\. Leggi `docs/index.md` per lo stato delle US e il perimetro del sistema

2\. Leggi `docs/business/objectives.md` per gli obiettivi di business

3\. Leggi tutte le US in `docs/user-stories/` per capire i comportamenti richiesti

4\. Leggi `docs/requirements/non-functional.md` per i vincoli di qualità

5\. Leggi `docs/requirements/business-rules.md` per le regole di dominio

6\. Se esistono già ADR in `docs/decisions/`, leggili per non duplicare decisioni già prese

7\. Produci un sommario: tipo di sistema, attori, flussi principali, vincoli rilevanti

8\. Chiedi conferma prima di procedere alla Fase 2



\*\*FASE 2 — Decisioni fondamentali\*\*

Per ognuna delle seguenti aree, proponi 2-3 opzioni con pro e contro,

attendi la scelta dell'utente e formalizza ogni decisione come ADR in `docs/decisions/ADR-NNN.md`.



\- \*\*Architettura generale\*\* — struttura flat vs layered (presentazione / dominio / persistenza)

\- \*\*Strategia di persistenza\*\* — file JSON / SQLite / altro; considerare volume dati atteso e requisiti di query

\- \*\*Entry point e interazione utente\*\* — CLI con argparse / menu interattivo / altro

\- \*\*Gestione degli errori\*\* — eccezioni custom vs codici di ritorno, livello di feedback all'utente



Per ogni decisione: mostra le opzioni, attendi la scelta, crea l'ADR, chiedi conferma prima di procedere alla successiva.



\*\*FASE 3 — Struttura moduli\*\*

1\. Proponi la struttura delle cartelle e dei moduli in `src/` sulla base delle decisioni della Fase 2

2\. Per ogni modulo descrivi: responsabilità, classi o funzioni principali previste, dipendenze da altri moduli

3\. Mostra la struttura completa e chiedi conferma

4\. Dopo conferma, crea i file `.py` con:

&#x20;  - Docstring del modulo in italiano

&#x20;  - Classi e funzioni principali come stub (firma + docstring, corpo `pass`)

&#x20;  - Import necessari già impostati



\*\*FASE 4 — Documentazione architetturale\*\*

1\. Genera `docs/architecture/overview.md` con descrizione dei componenti e diagramma Mermaid `graph TD`

2\. Genera `docs/architecture/data-model.md` con entità del dominio e diagramma Mermaid `erDiagram`

3\. Mostra ogni documento e chiedi conferma prima di salvare

4\. Aggiorna `mkdocs.yml` con le nuove voci in `nav`



\*\*FASE 5 — Riepilogo\*\*

1\. Elenca tutti gli artefatti prodotti: ADR creati, file `src/` creati, documenti `docs/architecture/` generati

2\. Segnala eventuali aree ancora da definire o decisioni rinviate

3\. Suggerisci il prossimo passo (prima US da implementare con `/implement-us`)



\*\*Regole:\*\*

\- Non saltare mai una fase senza conferma esplicita

\- Non creare file in `src/` o `docs/` senza aver mostrato la bozza

\- Tutte le scelte architetturali devono essere tracciate in un ADR prima di procedere alla fase successiva



\---



\### /implement-us \[US-ID]

\*\*Scopo:\*\* Implementare una User Story leggendo il contesto completo e procedendo fase per fase.



\*\*FASE 1 — Lettura contesto\*\*

1\. Leggi `docs/user-stories/\[US-ID].md` — user story, RF e criteri di accettazione

2\. Leggi le US da cui dipende (sezione Dipendenze) per capire il contesto

3\. Leggi `docs/requirements/business-rules.md` per le BR applicabili

4\. Leggi `docs/architecture/overview.md` e `docs/architecture/class-diagram.md` se disponibili

5\. Leggi `graphify-out/GRAPH\_REPORT.md` se disponibile

6\. Leggi `docs/decisions/ADR-\*.md` per le convenzioni architetturali già stabilite



\*\*FASE 2 — Piano di implementazione\*\*

7\. Proponi un piano strutturato con:

&#x20;  - File da creare (path e responsabilità)

&#x20;  - File esistenti da modificare (con motivazione)

&#x20;  - Classi e funzioni principali da implementare

&#x20;  - Dipendenze tra i componenti

8\. Segnala esplicitamente se:

&#x20;  - Mancano criteri di accettazione → suggerisci `/add-ac \[US-ID]` prima di procedere

&#x20;  - La US ha dipendenze non ancora implementate

&#x20;  - Servono nuovi ADR prima di procedere

9\. Mostra il piano e chiedi conferma prima di scrivere codice



\*\*FASE 3 — Implementazione\*\*

10\. Implementa un componente alla volta mostrando il codice completo prima di salvarlo

11\. Per ogni file: mostra il contenuto e chiedi conferma prima di scrivere

12\. Dopo ogni componente, verifica la coerenza con i RF della US

13\. Al termine, mostra un riepilogo dei file creati o modificati



\*\*FASE 4 — Chiusura\*\*

14\. Proponi di aggiornare lo stato della US: `/set-status \[US-ID] Implementata`

15\. Se durante l'implementazione sono emerse decisioni architetturali significative,

&#x20;   proponi di formalizzarle con `/add-cr` o creando un ADR



\*\*Regole:\*\*

\- Non scrivere mai codice senza aver mostrato la bozza e ottenuto conferma

\- Rispettare le convenzioni di naming e stile già presenti nel codebase

\- Ogni funzione e metodo deve avere docstring in italiano

\- Aggiungere type hints su tutte le funzioni

\- Se un RF è ambiguo, chiedere chiarimento prima di implementare



\---

## Template

### Template User Story (US-\*.md)

```markdown
# \\\[US-ID] — \\\[Titolo]
\\\[Torna alla Home](../index.md)

## User Story
\\\*\\\*Come\\\*\\\* \\\[utente], \\\*\\\*voglio\\\*\\\* \\\[azione], \\\*\\\*così da\\\*\\\* \\\[beneficio].

## Metadati
| Campo | Valore |
|-------|--------|
| ID | \\\[US-ID] |
| Stato | Bozza |
| Priorità | Alta / Media / Bassa |
| Data creazione | YYYY-MM-DD |
| Data ultima modifica | — |

## Dipendenze
| ID | Titolo | Relazione |
|----|--------|-----------|
| — | — | — |

## Storie derivate
> Compilare solo se questa US è stata suddivisa (/split-us).

| ID | Titolo |
|----|--------|
| — | — |

## Requisiti Funzionali
| ID Requisito | Descrizione | Stato |
|--------------|-------------|-------|
| RF-NNN-01 | Il sistema \\\*\\\*deve/dovrebbe/può\\\*\\\* ... | Proposto |

## Criteri di Accettazione
```gherkin
Scenario: \\\[nome scenario]
  Given \\\[precondizione]
  When \\\[azione]
  Then \\\[risultato atteso]
```

## Note e Domande Aperte

> \\\[Note o domande aperte. Rimuovere se vuoto.]

```

---

### Template Change Request (CR-\\\*.md)
```markdown
# \\\[CR-ID] — \\\[Titolo]

## Descrizione
\\\[Cosa cambia e perché]

## Metadati
| Campo | Valore |
|-------|--------|
| ID | \\\[CR-ID] |
| Stato | Aperta |
| Impatto | Basso / Medio / Alto |
| Data apertura | YYYY-MM-DD |
| Richiedente | — |

## Artefatti impattati
| ID | Tipo | Modifica richiesta |
|----|------|--------------------|
| — | — | — |

## Analisi impatto
\\\[Descrizione dell'impatto sul progetto]

## Decisione
\\\[ ] Approvata \\\[ ] Rifiutata \\\[ ] In attesa
```

\---

### Template ADR (ADR-\*.md)

```markdown
# \\\[ADR-ID] — \\\[Titolo della decisione]

## Stato
\\\[Proposta / Accettata / Superata]

## Contesto
\\\[Perché è stata necessaria questa decisione]

## Opzioni considerate
1. \\\[Opzione A]
2. \\\[Opzione B]

## Decisione
\\\[Cosa è stato scelto e perché]

## Conseguenze
\\\[Cosa cambia, pro e contro]
```

\---

### Template manifest raw (raw/manifest.md)

```markdown
# Manifest — File Grezzi Analizzati

| File | Tipo | Data analisi | Output wiki |
|------|------|--------------|-------------|
| — | — | — | — |
```

\---

## Regole

### Nomenclatura

* User Stories: `US-NNN` (tre cifre, es. US-001)
* Requisiti funzionali: `RF-NNN-NN` (US di riferimento + progressivo)
* Requisiti non funzionali: `NFR-NNN`
* Business rule: `BR-NNN`
* Change request: `CR-NNN`
* ADR: `ADR-NNN`
* Obiettivi di business: `OB-NNN`

### Formalismo requisiti

* **deve** → requisito obbligatorio (shall)
* **dovrebbe** → requisito raccomandato (should)
* **può** → requisito facoltativo (may)

### Comportamento generale

* Non modificare mai file in `raw/` (eccetto `raw/manifest.md`)
* Non modificare mai file in `graphify-out/`
* Mostrare sempre una bozza e chiedere conferma prima di scrivere in `docs/`
* Segnalare sempre ambiguità e dipendenze prima di formalizzare
* In caso di dubbio tra due interpretazioni, presentare entrambe e chiedere
* Usare sempre italiano per la documentazione

\---

## Sessione

### All'avvio (senza comando esplicito)

Se non viene dato un comando specifico all'avvio, esegui automaticamente `/start` e attendi istruzioni.

### Alla chiusura

Ricorda sempre all'utente di eseguire `/save` prima di terminare la sessione.

