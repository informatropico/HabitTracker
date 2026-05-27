Rispondi a una domanda sul progetto cercando nelle fonti documentali rilevanti.
L'utente fornisce una domanda in linguaggio naturale (es. "come è stato deciso di gestire l'assimilazione di un habit?").

Esegui le seguenti azioni:

**1. Analizza la domanda e identifica il tipo di risposta cercata:**
- Decisione presa → leggi `docs/decisions/ADR-*.md`
- Comportamento del sistema / requisito → leggi `docs/user-stories/US-*.md` e `docs/requirements/business-rules.md`
- Criteri di accettazione / test → leggi `docs/user-stories/US-*.md` cercando sezioni Gherkin
- Obiettivo di business → leggi `docs/business/objectives.md`
- Cosa è stato fatto / storico sessioni → leggi `logs/` (tutti i file, non solo gli ultimi 3)
- Stato di un artefatto → leggi `docs/index.md` poi il file specifico
- Concetto di dominio → leggi `wiki/concepts/` e `docs/requirements/business-rules.md`

**2. Prima di leggere i file completi, scansiona gli indici:**
- Leggi `docs/index.md` per identificare US pertinenti per titolo
- Elenca i file ADR disponibili in `docs/decisions/`
- Elenca i file in `wiki/` pertinenti per nome

**3. Leggi solo i file rilevanti** identificati nel passo 2.
   Non leggere tutti i file: seleziona in base alla pertinenza con la domanda.

**4. Produci la risposta:**
- Rispondi in modo diretto e sintetico
- Cita sempre la fonte: file e sezione specifica (es. "secondo ADR-002, sezione Decisione")
- Se la risposta non è presente nella documentazione, dichiaralo esplicitamente
- Se la documentazione è ambigua o incompleta su quel punto, segnalalo
- Se ci sono più fonti che si contraddicono, mostralo

**5. In fondo alla risposta, elenca i file consultati** con il path completo.
