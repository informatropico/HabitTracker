Implementa una User Story. L'utente fornisce l'ID della US (es. US-001).

Esegui le seguenti azioni:

**FASE 1 — Lettura contesto**
1. Leggi `docs/user-stories/[US-ID].md` — user story, RF e criteri di accettazione
2. Leggi le US da cui dipende (sezione Dipendenze) per capire il contesto
3. Leggi `docs/requirements/business-rules.md` per le BR applicabili
4. Leggi `docs/architecture/overview.md` e `docs/architecture/class-diagram.md` se disponibili
5. Leggi `graphify-out/GRAPH_REPORT.md` se disponibile per capire la struttura attuale del codice
6. Leggi `docs/decisions/ADR-*.md` per le convenzioni architetturali già stabilite

**FASE 2 — Piano di implementazione**
7. Proponi un piano strutturato che include:
   - File da creare (con path e responsabilità)
   - File esistenti da modificare (con motivazione)
   - Classi e funzioni principali da implementare
   - Dipendenze tra i componenti
   - Eventuali decisioni architetturali necessarie (che richiederebbero un ADR)
8. Segnala esplicitamente se:
   - Mancano criteri di accettazione (suggerisci di eseguire `/add-ac [US-ID]` prima)
   - La US ha dipendenze non ancora implementate
   - Servono nuove BR o ADR prima di procedere
9. Mostra il piano e chiedi conferma prima di scrivere codice

**FASE 3 — Implementazione**
10. Implementa un componente alla volta, mostrando il codice completo prima di salvarlo
11. Per ogni file: mostra il contenuto e chiedi conferma prima di scrivere
12. Dopo ogni componente, verifica che il codice sia coerente con gli RF della US
13. Al termine dell'implementazione, mostra un riepilogo dei file creati/modificati

**FASE 4 — Chiusura**
14. Proponi di aggiornare lo stato della US con `/set-status [US-ID] Implementata`
15. Se durante l'implementazione sono emerse decisioni architetturali significative,
    proponi di formalizzarle con `/add-cr` o creando un ADR

**Regole**
- Non scrivere mai codice senza aver mostrato la bozza e ottenuto conferma
- Rispettare le convenzioni di naming e stile già presenti nel codebase
- Ogni funzione/metodo deve avere docstring in italiano
- Aggiungere type hints su tutte le funzioni
- Se un RF è ambiguo, chiedere chiarimento prima di implementare
