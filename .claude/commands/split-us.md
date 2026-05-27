Suddividi una User Story troppo grande in storie più piccole e gestibili. L'utente fornisce l'ID della US da suddividere (es. US-001).

Esegui le seguenti azioni:
1. Leggi il file `docs/user-stories/[US-ID].md`
2. Analizza la US e proponi una suddivisione motivando i criteri di split
3. Per ogni storia derivata proposta:
   - Assegna un nuovo ID progressivo
   - Definisci come vengono ridistribuiti i RF dell'originale
   - Segnala RF da modificare o raffinare nella derivata
   - Segnala RF che non trovano posto in nessuna derivata
4. Mostra il piano completo di split e chiedi conferma prima di procedere
5. Dopo conferma:
   - Crea i file delle storie derivate con template US completo
   - Stato delle derivate: Bozza
   - Dipendenza nelle derivate: "Derivata da [US-ID]"
   - I RF nelle derivate hanno stato "Proposto"
   - Aggiorna la US originale:
     * Stato → Suddivisa
     * Rimuovi lo stato dai RF (diventano archivio storico senza stato attivo)
     * Aggiungi sezione "Storie derivate" con link alle nuove US
   - Aggiorna la tabella in `docs/index.md`
