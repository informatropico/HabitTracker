# Obiettivi di Business

## Panoramica
Questa sezione raccoglie gli obiettivi di business del progetto, derivati dal contesto strategico e dai bisogni utente identificati nella fase di analisi.

| ID | Obiettivo | Metrica di successo | US collegate | Stato |
|----|-----------|---------------------|--------------|-------|
| [OB-001](#ob-001--supportare-la-transizione-verso-una-nuova-abitudine) | Supportare la transizione verso una nuova abitudine | Tempo mediano impiegato dall'utente per dichiarare un habit "Assimilato" (US-008) — misura osservativa | US-001, US-002, US-008, US-011, US-013 | Attivo |
| [OB-002](#ob-002--riconoscere-e-gestire-abitudini-non-sostenibili) | Riconoscere e gestire abitudini non sostenibili | % habit con basso tasso di rispetto esplicitamente abbandonati invece di lasciati attivi | US-004, US-005, US-006, US-007, US-009 | Attivo |

---

## OB-001 — Supportare la transizione verso una nuova abitudine

### Descrizione
Supportare l'utente nella fase di transizione verso una nuova abitudine, riducendo le frizioni iniziali e fornendo una motivazione esterna nel periodo in cui l'azione non è ancora automatica.

### Razionale
L'app non serve a tracciare abitudini già consolidate — quelle non hanno bisogno di un'app. Serve nel periodo di costruzione, quando ancora esistono attriti e la persona ha bisogno di un "post-it sul frigo" che la richiami al proprio impegno. Lo strumento accompagna fino a quando l'abitudine diventa routine (o viene abbandonata consapevolmente).

### Metrica di successo
Tempo mediano impiegato dall'utente per dichiarare un habit come "Assimilato" (US-008), a partire dalla data di creazione dell'habit.

Si tratta di una **misura osservativa**, non di una soglia applicata dal sistema: per [BR-001](../requirements/business-rules.md#br-001--transizione-ad-assimilato-su-azione-utente) la transizione ad "Assimilato" avviene solo per azione esplicita dell'utente, mai automaticamente. La metrica indica quanto velocemente l'app riesce a portare gli utenti al momento del riconoscimento consapevole.

### Metadati
| Campo | Valore |
|-------|--------|
| ID | OB-001 |
| Stato | Attivo |
| Data creazione | 2026-05-27 |
| Data ultima modifica | — |

### US collegate
| US | Perché collegata |
|----|------------------|
| [US-001](../user-stories/US-001.md) | Dichiarazione mattutina — il momento di impegno quotidiano che crea la motivazione |
| [US-002](../user-stories/US-002.md) | Consuntivo serale — il momento di verifica che rinforza il ciclo |
| [US-008](../user-stories/US-008.md) | Archiviazione come routine — il "successo" dell'obiettivo |
| [US-011](../user-stories/US-011.md) | Aggiunta di un nuovo habit — il punto di ingresso nel percorso |
| [US-013](../user-stories/US-013.md) | Accesso alla giornata in corso — il touchpoint quotidiano |

---

## OB-002 — Riconoscere e gestire abitudini non sostenibili

### Descrizione
Aiutare l'utente a riconoscere e gestire consapevolmente le abitudini che non riesce a sostenere, sia abbandonandole esplicitamente sia indagandone i motivi per modificare il proprio comportamento.

### Razionale
Il valore dell'app non sta solo nel celebrare i successi, ma nel restituire un segnale onesto sui fallimenti. Un habit dichiarato e mai rispettato è un'informazione preziosa: l'app deve renderla visibile e offrire un'uscita pulita (abbandono consapevole) invece di lasciarla decadere in silenzio. Evita la "shelf-ware delle abitudini": liste di buoni propositi mai mantenuti che generano colpa invece di consapevolezza.

Deriva dal user need: *"Come Utente ho la necessità di comprendere quali abitudini non riesco a rispettare per indagarne i motivi e modificare il mio comportamento."*

### Metrica di successo
% di habit "In corso" da oltre N giorni con tasso di rispetto sotto una certa soglia che vengono **esplicitamente abbandonati** dall'utente (US-009), invece di essere lasciati indefinitamente attivi.

> ⚠️ Domanda aperta: soglia di "tasso di rispetto basso" e finestra temporale da definire (probabilmente con la stessa BR/ADR di OB-001).

### Metadati
| Campo | Valore |
|-------|--------|
| ID | OB-002 |
| Stato | Attivo |
| Data creazione | 2026-05-27 |
| Data ultima modifica | — |

### US collegate
| US | Perché collegata |
|----|------------------|
| [US-004](../user-stories/US-004.md) | Consultazione statistiche — il dato che alimenta la riflessione |
| [US-005](../user-stories/US-005.md) | Habit dichiarati ma non rispettati — il segnale primario |
| [US-006](../user-stories/US-006.md) | Habit raramente dichiarati — segnale debole di disinteresse |
| [US-007](../user-stories/US-007.md) | Habit non più dichiarati — segnale forte di abbandono di fatto |
| [US-009](../user-stories/US-009.md) | Marcatura habit abbandonato — l'uscita consapevole |
