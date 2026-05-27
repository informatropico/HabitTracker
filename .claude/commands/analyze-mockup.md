Analizza uno schema, wireframe o mockup ed estrai requisiti impliciti. L'utente fornisce il file o descrive il mockup.

Formati accettati: immagine (PNG, JPG), PDF, canvas Obsidian (.canvas), descrizione testuale.

Esegui le seguenti azioni:
1. Analizza il contenuto visivo o la descrizione fornita
2. Identifica e documenta:
   - Componenti UI presenti
   - Flussi di navigazione impliciti
   - Stati dell'interfaccia
   - Validazioni implicite
   - Comportamenti attesi
3. Mappa ogni elemento identificato a requisiti funzionali candidati
4. Segnala elementi non coperti da nessuna US esistente in `docs/user-stories/`
5. Salva l'analisi in `wiki/requirements/YYYY-MM-DD-mockup-[nome].md`
6. Aggiorna `raw/manifest.md` aggiungendo una riga con: file analizzato, data analisi, path output in wiki.
   Se `raw/manifest.md` non esiste, crealo con questa intestazione prima di aggiungere la riga:
   ```
   # Manifest — File Grezzi Analizzati

   | File | Tipo | Data analisi | Output wiki |
   |------|------|--------------|-------------|
   ```
7. Chiedi come procedere con gli elementi non coperti
