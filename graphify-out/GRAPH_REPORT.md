# Graph Report - .  (2026-05-28)

## Corpus Check
- Corpus is ~14,263 words - fits in a single context window. You may not need a graph.

## Summary
- 107 nodes · 196 edges · 13 communities (11 shown, 2 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.88)
- Token cost: 107,500 input · 20,231 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Comandi Analisi & Requisiti|Comandi Analisi & Requisiti]]
- [[_COMMUNITY_Stati Habit & Business Rules|Stati Habit & Business Rules]]
- [[_COMMUNITY_User Stories & Template|User Stories & Template]]
- [[_COMMUNITY_Sessione Mattutina & Serale|Sessione Mattutina & Serale]]
- [[_COMMUNITY_Modalita Sviluppatore & Architettura|Modalita Sviluppatore & Architettura]]
- [[_COMMUNITY_Struttura Vault & Analisi Raw|Struttura Vault & Analisi Raw]]
- [[_COMMUNITY_Stack Tecnico Python|Stack Tecnico Python]]
- [[_COMMUNITY_Modulo Logger|Modulo Logger]]
- [[_COMMUNITY_Template ADR|Template ADR]]
- [[_COMMUNITY_Template Manifest Raw|Template Manifest Raw]]

## God Nodes (most connected - your core abstractions)
1. `US-001 Dichiarazione mattutina degli habit` - 20 edges
2. `US-008 Archiviazione habit come routine` - 12 edges
3. `US-009 Marcatura habit abbandonato` - 11 edges
4. `docs/index.md (Home + tabella US)` - 10 edges
5. `BR-004 Perimetro di habit attivo` - 10 edges
6. `NFR-001 Essenzialità e basso attrito` - 10 edges
7. `Log sessione 2026-05-27 08:33` - 10 edges
8. `BR-003 Stati habit e transizioni ammesse` - 9 edges
9. `US-002 Consuntivo serale degli habit` - 9 edges
10. `US-006 Habit raramente dichiarati` - 9 edges

## Surprising Connections (you probably didn't know these)
- `Changelog` --references--> `logger module`  [EXTRACTED]
  docs/changelog.md → src/habit_tracker/logger.py
- `Modalita Analista` --references--> `docs/index.md (Home + tabella US)`  [EXTRACTED]
  CLAUDE.md → docs/index.md
- `User Story (US)` --conceptually_related_to--> `Criteri di Accettazione in Gherkin`  [INFERRED]
  CLAUDE.md → .claude/commands/add-ac.md
- `/start` --references--> `docs/index.md (Home + tabella US)`  [EXTRACTED]
  .claude/commands/start.md → docs/index.md
- `/query` --references--> `docs/index.md (Home + tabella US)`  [EXTRACTED]
  .claude/commands/query.md → docs/index.md

## Hyperedges (group relationships)
- **Pipeline requisiti raw -> wiki -> docs** — raw_folder, wiki_folder, docs_folder, cmd_analyze, raw_manifest [INFERRED 0.85]
- **Ciclo di vita User Story** — cmd_add_us, cmd_add_rf, cmd_add_ac, cmd_set_status, cmd_split_us, concept_user_story [INFERRED 0.85]
- **Generazione documentazione architetturale** — cmd_generate_arch, docs_arch_overview, docs_arch_class_diagram, docs_arch_data_model, mermaid_diagrams [EXTRACTED 1.00]
- **Flusso giornata: mattutina, serale, aggiunta posteriori, accesso** — us_us001, us_us002, us_us003, us_us013, us_us017 [INFERRED 0.85]
- **Ciclo vita habit: creazione, assimilazione, abbandono, ripristino** — us_us011, us_us008, us_us009, us_us012, br_br003, br_br004 [INFERRED 0.85]
- **Segnali abitudini non sostenibili** — us_us005, us_us006, us_us007, objectives_ob002, br_br002 [INFERRED 0.75]

## Communities (13 total, 2 thin omitted)

### Community 0 - "Comandi Analisi & Requisiti"
Cohesion: 0.10
Nodes (22): Modalita Analista, Formalismo requisiti (deve/dovrebbe/puo), Nomenclatura artefatti, Template Change Request, /add-cr, /add-goal, /add-nfr, /add-rf (+14 more)

### Community 1 - "Stati Habit & Business Rules"
Cohesion: 0.35
Nodes (17): BR-001 Transizione ad Assimilato su azione utente, BR-002 Transizione ad Abbandonato su azione utente, BR-003 Stati habit e transizioni ammesse, BR-004 Perimetro di habit attivo, State Machine Habit (In corso/Assimilato/Abbandonato), Transizioni di stato user-driven, Why del progetto (vivere, non compilare app), OB-002 Riconoscere e gestire abitudini non sostenibili (+9 more)

### Community 2 - "User Stories & Template"
Cohesion: 0.16
Nodes (17): Template User Story, /add-ac, /add-us, /set-status, /split-us, Criteri di Accettazione in Gherkin, Habit (abitudine), Routine (habit assimilato) (+9 more)

### Community 3 - "Sessione Mattutina & Serale"
Cohesion: 0.34
Nodes (16): Modello compose-commit sessione mattutina, Log sessione 2026-05-27 08:33, NFR-001 Essenzialità e basso attrito, OB-001 Supportare la transizione verso una nuova abitudine, RF-001-07 Sessione mattutina vuota, RF-001-09 Compose libero pre-save, RF-001-10 Salvataggio sessione mattutina, RF-001-13 Immutabilità post-save (+8 more)

### Community 4 - "Modalita Sviluppatore & Architettura"
Cohesion: 0.24
Nodes (10): Modalita Sviluppatore, /generate-arch, /save, /start, docs/architecture/class-diagram.md, docs/architecture/data-model.md, docs/architecture/overview.md, graphify-out/GRAPH_REPORT.md (+2 more)

### Community 5 - "Struttura Vault & Analisi Raw"
Cohesion: 0.31
Nodes (10): CLAUDE.md Project Instructions, /analyze, /analyze-mockup, docs/ (output formale), graphify-out/ (generato automaticamente), raw/ (input grezzo), raw/manifest.md, Convenzione file grezzi analizzati (+2 more)

### Community 6 - "Stack Tecnico Python"
Cohesion: 0.33
Nodes (6): Claude Code, Graphify Tool, Logger riutilizzabile, MkDocs (documentation), Poetry (dependency management), Setup Template Python

### Community 7 - "Modulo Logger"
Cohesion: 0.50
Nodes (3): get_logger(), Logger, str

## Knowledge Gaps
- **14 isolated node(s):** `str`, `Logger`, `CLAUDE.md Project Instructions`, `Template User Story`, `Template Change Request` (+9 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `docs/index.md (Home + tabella US)` connect `User Stories & Template` to `Comandi Analisi & Requisiti`, `Modalita Sviluppatore & Architettura`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Why does `Nomenclatura artefatti` connect `Comandi Analisi & Requisiti` to `User Stories & Template`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `User Story (US)` connect `User Stories & Template` to `Comandi Analisi & Requisiti`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **What connects `str`, `Logger`, `CLAUDE.md Project Instructions` to the rest of the system?**
  _28 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Comandi Analisi & Requisiti` be split into smaller, more focused modules?**
  _Cohesion score 0.09956709956709957 - nodes in this community are weakly interconnected._