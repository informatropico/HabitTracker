Analizza materiale grezzo ed estrai requisiti, vincoli e business rule. L'utente fornisce il path di un file in raw/ oppure incolla direttamente il testo.

Esegui le seguenti azioni:
1. Leggi il file indicato da `raw/` o elabora il testo fornito
2. Estrai e classifica tutto il contenuto in:
   - **Requisiti candidati** — cosa il sistema deve fare
   - **Vincoli** — limitazioni tecniche, temporali, normative
   - **Business rule** — regole di dominio applicabili a più contesti
   - **Ambiguità** — affermazioni non chiare che richiedono chiarimento
3. Per ogni business rule candidata: verifica se è già presente in `docs/requirements/business-rules.md`
4. Per ogni requisito candidato: verifica se è già coperto da US esistenti in `docs/user-stories/`
5. Salva l'analisi in `wiki/requirements/YYYY-MM-DD-[nome-fonte].md`
6. Produci un sommario e chiedi come procedere (es. creare nuove US, aggiungere BR, ecc.)
