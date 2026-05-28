# Business Rules

## Panoramica
Questa sezione raccoglie le regole di dominio che si applicano trasversalmente a più user stories.
Una business rule è un vincolo o una politica del dominio che il sistema deve rispettare indipendentemente dal contesto di utilizzo.

---

| ID | Descrizione | US impattate | Fonte | Stato |
|----|-------------|--------------|-------|-------|
| [BR-001](#br-001--transizione-ad-assimilato-su-azione-utente) | La transizione ad "Assimilato" avviene esclusivamente su azione esplicita dell'utente | US-007, US-008, OB-001 | Decisione di prodotto 2026-05-27 | Attiva |
| [BR-002](#br-002--transizione-ad-abbandonato-su-azione-utente) | La transizione ad "Abbandonato" avviene esclusivamente su azione esplicita dell'utente | US-005, US-006, US-007, US-009, OB-002 | Decisione di prodotto 2026-05-27 | Attiva |
| [BR-003](#br-003--stati-habit-e-transizioni-ammesse) | Stati ammessi per un habit (In corso / Assimilato / Abbandonato) e transizioni valide, inclusa l'eliminazione definitiva | US-001, US-008, US-009, US-010, US-011, US-012, US-016, US-018 | Modello di dominio | Attiva |
| [BR-004](#br-004--perimetro-di-habit-attivo) | Solo gli habit "In corso" sono considerati attivi; gli altri restano visibili solo in consultazione storica e archivio | US-001, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-016 | Modello di dominio | Attiva |

---

## BR-001 — Transizione ad "Assimilato" su azione utente

### Descrizione
La transizione di un habit allo stato **Assimilato** avviene **esclusivamente** su azione esplicita dell'utente. Il sistema non promuove mai automaticamente un habit a routine, indipendentemente dal numero di giorni consecutivi di rispetto o da qualsiasi altra metrica.

### Razionale
L'app è uno strumento per supportare l'utente nella decisione, non per prenderla al suo posto. Il riconoscimento "questa è ormai una routine" è un atto consapevole dell'utente, parte stessa del valore del prodotto. Coerente con il "Why" (*"Lo scopo della vita è vivere, non compilare una app"*).

### Metadati
| Campo | Valore |
|-------|--------|
| ID | BR-001 |
| Stato | Attiva |
| Data creazione | 2026-05-27 |
| Fonte | Decisione di prodotto del 2026-05-27 |

### US impattate
| US | Impatto |
|----|---------|
| [US-007](../user-stories/US-007.md) | Risolve l'ambiguità sull'interpretazione di "habit non più dichiarati": se l'utente non ha agito, l'habit è ancora "In corso" e in deriva |
| [US-008](../user-stories/US-008.md) | Definisce che il cambio di stato è user-driven, non automatico |
| [OB-001](../business/objectives.md#ob-001--supportare-la-transizione-verso-una-nuova-abitudine) | La metrica diventa osservativa (tempo che l'utente impiega per dichiarare assimilazione), non una soglia applicata dal sistema |

---

## BR-002 — Transizione ad "Abbandonato" su azione utente

### Descrizione
La transizione di un habit allo stato **Abbandonato** avviene **esclusivamente** su azione esplicita dell'utente. Il sistema può segnalare habit candidati all'abbandono tramite US-005, US-006, US-007, ma non li sposta mai automaticamente fuori dallo stato "In corso".

### Razionale
Coerenza con BR-001. Allineato con OB-002 ("riconoscere e gestire abitudini non sostenibili"): il valore è nell'azione consapevole di abbandono, non in un decadimento silenzioso che lascerebbe l'utente senza il momento di riflessione che l'app vuole indurre.

### Metadati
| Campo | Valore |
|-------|--------|
| ID | BR-002 |
| Stato | Attiva |
| Data creazione | 2026-05-27 |
| Fonte | Decisione di prodotto del 2026-05-27 |

### US impattate
| US | Impatto |
|----|---------|
| [US-005](../user-stories/US-005.md) | Le soglie sono per segnalazione, non per azione automatica |
| [US-006](../user-stories/US-006.md) | Idem |
| [US-007](../user-stories/US-007.md) | Idem |
| [US-009](../user-stories/US-009.md) | L'abbandono è l'azione esplicita che chiude il ciclo segnalazione → riflessione → decisione |
| [OB-002](../business/objectives.md#ob-002--riconoscere-e-gestire-abitudini-non-sostenibili) | La metrica misura abbandoni espliciti, non transizioni automatiche |

---

## BR-003 — Stati habit e transizioni ammesse

### Descrizione
Un habit può trovarsi in uno e uno solo dei seguenti stati: **In corso**, **Assimilato**, **Abbandonato**. Sono ammesse le seguenti transizioni:

| Da | A | Condizione | Origine |
|----|---|------------|---------|
| (creazione) | In corso | — | US-011 |
| In corso | Assimilato | — | US-008 (per BR-001) |
| In corso | Abbandonato | — | US-009 (per BR-002) |
| Assimilato | In corso | — | US-012 |
| Abbandonato | In corso | — | US-012 |
| Qualsiasi | [eliminato] | Habit mai selezionato in nessun record di giornata | US-018 |

**Non sono ammesse** transizioni dirette tra Assimilato e Abbandonato: per passare dall'uno all'altro è necessario tornare prima a "In corso".

L'**eliminazione** (`[eliminato]`) non è uno stato del ciclo di vita: rimuove l'habit dal sistema in modo permanente e irreversibile. È applicabile da qualsiasi stato, ma esclusivamente se l'habit non è mai comparso in nessun record di giornata. Un habit che ha avuto anche una sola occorrenza in dichiarazione o consuntivo non è eliminabile.

### Razionale
Definisce la macchina a stati canonica del dominio, riferimento condiviso per tutte le US che leggono o modificano lo stato di un habit. La transizione diretta Assimilato↔Abbandonato non ha senso semantico: un habit assimilato che si rimette in discussione è di fatto "rimesso in corso" prima di essere eventualmente abbandonato. L'eliminazione copre il caso di habit creati per errore o non ancora adottati, che non hanno storia e quindi possono essere rimossi senza perdita di informazione.

### Metadati
| Campo | Valore |
|-------|--------|
| ID | BR-003 |
| Stato | Attiva |
| Data creazione | 2026-05-27 |
| Data ultima modifica | 2026-05-28 |
| Fonte | Modello di dominio |

### US impattate
US-001, US-008, US-009, US-010, US-011, US-012, US-016, US-018 (tutte le US che leggono o modificano lo stato di un habit).

---

## BR-004 — Perimetro di habit "attivo"

### Descrizione
Solo gli habit nello stato **In corso** sono considerati **attivi** ai fini del sistema. Un habit attivo:
- è selezionabile nelle sessioni di dichiarazione (US-001)
- è incluso nelle statistiche di segnalazione (US-005, US-006, US-007)
- è incluso nell'elenco principale degli habit (US-016)

Un habit **Assimilato** o **Abbandonato** è considerato **non attivo**:
- non è selezionabile in dichiarazione (vedi RF-001-05)
- non è incluso nelle statistiche di segnalazione **dalla data di cambio stato in poi**
- rimane visibile nelle statistiche di consultazione storica (US-004)
- rimane visibile nell'archivio (US-010)

### Razionale
Definisce in modo univoco il significato di "attivo" su cui si appoggiano molte US, evitando duplicazione e ambiguità. Oggi questa regola è ripetuta nei RF di US-008 e US-009: con BR-004 i singoli RF possono semplicemente riferirsi alla BR.

### Metadati
| Campo | Valore |
|-------|--------|
| ID | BR-004 |
| Stato | Attiva |
| Data creazione | 2026-05-27 |
| Fonte | Modello di dominio |

### US impattate
US-001, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-016.
