Genera o aggiorna la documentazione tecnica in `docs/architecture/`.
Può operare su uno o più target. Se l'utente non specifica, genera tutto.

---

### Target disponibili

#### `class-diagram`
1. Leggi tutti i file `.py` in `src/`
2. Identifica: classi, metodi pubblici, attributi, relazioni (ereditarietà, composizione, dipendenza)
3. Genera un diagramma Mermaid `classDiagram` completo
4. Mostra il diagramma e chiedi conferma
5. Dopo conferma, salva in `docs/architecture/class-diagram.md` con intestazione e data generazione

#### `data-model`
1. Leggi i file di schema dati del progetto (JSON schema, dataclass, modelli Pydantic, file `.json` di esempio)
2. Documenta: entità principali, campi, tipi, relazioni tra entità
3. Genera un diagramma Mermaid `erDiagram` se applicabile
4. Mostra bozza e chiedi conferma
5. Dopo conferma, salva in `docs/architecture/data-model.md`

#### `overview`
1. Leggi `src/` per identificare i moduli principali
2. Leggi `docs/decisions/ADR-*.md` per decisioni architetturali rilevanti
3. Leggi `graphify-out/GRAPH_REPORT.md` se disponibile
4. Scrivi una descrizione dei componenti principali del sistema, le loro responsabilità e come interagiscono
5. Includi un diagramma Mermaid `graph TD` dei componenti
6. Mostra bozza e chiedi conferma
7. Dopo conferma, salva in `docs/architecture/overview.md`

---

### Regole
- Non modificare mai file esistenti in `docs/architecture/` senza mostrare la bozza e ottenere conferma
- Se un file esiste già, mostra le differenze rispetto alla versione precedente prima di aggiornarlo
- Aggiungi sempre in fondo al file: `*Generato automaticamente il YYYY-MM-DD — aggiornare dopo ogni refactor significativo.*`
- Usa sempre Mermaid per i diagrammi (compatibile con MkDocs Material)
- Documenta in italiano
