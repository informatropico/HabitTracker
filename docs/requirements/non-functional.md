# Requisiti Non Funzionali

## Panoramica
Questa sezione raccoglie i requisiti non funzionali del sistema, trasversali alle singole user stories.

## Categorie
- **Performance** — tempi di risposta, throughput
- **Sicurezza** — protezione dei dati, accessi
- **Usabilità** — facilità d'uso, accessibilità
- **Manutenibilità** — leggibilità del codice, estensibilità
- **Portabilità** — compatibilità con sistemi operativi e ambienti

---

| ID | Categoria | Descrizione | US impattate | Stato |
|----|-----------|-------------|--------------|-------|
| [NFR-001](#nfr-001--essenzialità-e-basso-attrito) | Usabilità | Tempo sessione mattutina/serale < 30s; principio generale di basso attrito | US-001, US-002, US-003, US-011, US-013, US-014, US-016 | Attivo |

---

## NFR-001 — Essenzialità e basso attrito

### Descrizione
Lo strumento **deve** restare essenziale e a basso attrito, in modo che l'interazione quotidiana non venga percepita dall'utente come un impegno gravoso aggiuntivo. L'utente deve poter completare le sessioni quotidiane in un tempo comparabile a "leggere un post-it sul frigo".

### Metrica di successo
Tempo medio per completare una sessione (mattutina o serale) **< 30 secondi**, misurato dal momento di avvio della sessione alla conferma finale.

### Razionale
Deriva direttamente dal "Why" del progetto:
> *"Lo scopo della vita è vivere, non compilare una app. […] Uno strumento semplice, con un unico obiettivo."*

È il NFR che protegge il progetto dalla deriva tipica delle habit-tracker app: aggiungere feature, statistiche elaborate, gamification, finché l'app stessa diventa l'attività invece dello strumento per l'attività.

> ⚠️ Nota metodologica: il target dei 30 secondi è una metrica **proxy** misurabile, ma il principio sottostante ("essenziale, basso attrito") è più ampio e si applica anche a operazioni non temporizzate (aggiunta habit, accesso a giornate precedenti). Va tenuto come criterio di design generale.

### Metadati
| Campo | Valore |
|-------|--------|
| ID | NFR-001 |
| Categoria | Usabilità |
| Stato | Attivo |
| Data creazione | 2026-05-27 |
| Data ultima modifica | — |

### US impattate
**Impatto diretto sul tempo di sessione:**
| US | Impatto |
|----|---------|
| [US-001](../user-stories/US-001.md) | Dichiarazione mattutina — sessione direttamente misurata dal target 30s |
| [US-002](../user-stories/US-002.md) | Consuntivo serale — sessione direttamente misurata dal target 30s |
| [US-013](../user-stories/US-013.md) | Accesso alla giornata in corso — punto di ingresso, deve essere immediato |

**Principio di basso attrito applicabile (non temporizzato):**
| US | Impatto |
|----|---------|
| [US-003](../user-stories/US-003.md) | Aggiunta a posteriori — flow di recupero, deve restare semplice |
| [US-011](../user-stories/US-011.md) | Aggiunta nuovo habit — non deve diventare un form complesso |
| [US-014](../user-stories/US-014.md) | Modifica giornata precedente — accesso semplice senza navigazione profonda |
| [US-016](../user-stories/US-016.md) | Accesso elenco habit — visualizzazione immediata |

### Note
La combinazione dei 14 RF di US-001 va verificata in fase di definizione AC per assicurarsi che l'insieme dei flussi (conferma, annullamento, modifica) non porti la sessione mattutina oltre il target dei 30 secondi.
