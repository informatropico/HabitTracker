Genera i criteri di accettazione in formato Gherkin per una User Story. L'utente fornisce l'ID della US (es. US-001).

Esegui le seguenti azioni:
1. Leggi `docs/user-stories/[US-ID].md` — user story e requisiti funzionali
2. Per ogni RF significativo genera scenari Gherkin con struttura:
   Given [precondizione]
   When [azione]
   Then [risultato atteso]
3. Includi per ogni RF:
   - Almeno uno scenario happy path
   - Almeno uno scenario di errore o caso limite
4. Mostra la bozza completa e chiedi conferma prima di aggiornare la sezione "Criteri di Accettazione" nel file US
