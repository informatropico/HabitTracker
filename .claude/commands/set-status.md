Cambia lo stato di un requisito, user story o altro artefatto. L'utente fornisce l'ID e il nuovo stato.

Stati validi:
- US: Bozza → In revisione → Approvata → Implementata → Suddivisa → Obsoleta
- RF: Proposto → Approvato → Implementato → Eliminato
- CR: Aperta → In valutazione → Approvata → Rifiutata → Chiusa
- OB: Proposto → Approvato → Raggiunto → Abbandonato

Esegui le seguenti azioni:
1. Individua il file corretto dall'ID fornito
2. Verifica che il nuovo stato sia valido per il tipo di artefatto
3. Aggiorna il campo Stato nei metadati
4. Aggiorna la Data ultima modifica con la data odierna
5. Aggiorna la tabella in `docs/index.md` se l'artefatto è una US
6. Aggiungi una riga di log in fondo al file con: data, stato precedente → nuovo stato, motivazione fornita dall'utente
7. Mostra le modifiche e chiedi conferma prima di salvare
