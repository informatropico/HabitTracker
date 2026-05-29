Avvia un processo guidato di configurazione architetturale del progetto.
Obiettivo: produrre decisioni architetturali formalizzate, struttura src/ iniziale
e documentazione in docs/architecture/.

Il processo si svolge in fasi sequenziali con conferma esplicita tra una e l'altra.

---

**FASE 1 — Lettura contesto**
1. Leggi `docs/index.md` per lo stato delle US e il perimetro del sistema
2. Leggi `docs/business/objectives.md` per gli obiettivi di business
3. Leggi tutte le US in `docs/user-stories/` per capire i comportamenti richiesti
4. Leggi `docs/requirements/non-functional.md` per i vincoli di qualità
5. Leggi `docs/requirements/business-rules.md` per le regole di dominio
6. Se esistono già ADR in `docs/decisions/`, leggili per non duplicare decisioni già prese
7. Produci un sommario: tipo di sistema, attori, flussi principali, vincoli rilevanti
8. Chiedi conferma prima di procedere alla Fase 2

---

**FASE 2 — Decisioni fondamentali**
Per ognuna delle seguenti aree, proponi 2-3 opzioni con pro e contro,
chiedi all'utente di scegliere, poi formalizza la decisione come ADR.

**2a. Architettura generale**
- Struttura a moduli flat vs layered (presentazione / dominio / persistenza)
- Motivazione in base ai requisiti rilevati nella Fase 1

**2b. Strategia di persistenza**
- File JSON / SQLite / altro
- Considerare: volume dati atteso, requisiti di query, semplicità di setup

**2c. Entry point e interazione utente**
- CLI con argparse / menu interattivo / altro
- Considerare: flussi identificati nelle US

**2d. Gestione degli errori**
- Strategia: eccezioni custom vs codici di ritorno vs logging silenzioso
- Livello di dettaglio del feedback all'utente

Per ogni decisione:
- Mostra le opzioni con pro e contro
- Attendi la scelta dell'utente
- Crea l'ADR corrispondente in `docs/decisions/ADR-NNN.md`
- Chiedi conferma prima di procedere alla decisione successiva

---

**FASE 3 — Struttura moduli**
Sulla base delle decisioni della Fase 2:
1. Proponi la struttura delle cartelle e dei moduli in `src/`
2. Per ogni modulo, descrivi:
   - Responsabilità
   - Classi o funzioni principali previste
   - Dipendenze da altri moduli
3. Mostra la struttura completa e chiedi conferma
4. Dopo conferma, crea i file `.py` con:
   - Docstring del modulo in italiano
   - Classi/funzioni principali come stub (firma + docstring, corpo `pass`)
   - Import necessari già impostati

---

**FASE 4 — Documentazione architetturale**
1. Genera `docs/architecture/overview.md`:
   - Descrizione dei componenti e delle loro responsabilità
   - Diagramma Mermaid `graph TD` dei moduli e delle dipendenze
2. Genera `docs/architecture/data-model.md`:
   - Entità principali del dominio
   - Diagramma Mermaid `erDiagram` se applicabile
3. Mostra ogni documento e chiedi conferma prima di salvare

---

**FASE 5 — Riepilogo**
1. Elenca tutti gli artefatti prodotti:
   - ADR creati (con titolo e decisione presa)
   - File `src/` creati (con responsabilità)
   - Documenti `docs/architecture/` generati
2. Segnala eventuali aree ancora da definire o decisioni rinviate
3. Suggerisci il prossimo passo (es. prima US da implementare con `/implement-us`)

---

**Regole**
- Non saltare mai una fase o una decisione senza conferma esplicita
- Non creare file in `src/` o `docs/` senza aver mostrato la bozza
- Se una decisione dipende da informazioni non ancora disponibili, segnalarlo
  e proporre una scelta provvisoria con motivazione esplicita
- Tutte le scelte devono essere tracciabili negli ADR
