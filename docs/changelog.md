# Changelog
## [template v2.1.0] — 2026-05-27

### Aggiunto
- Comando `/query` — ricerca semantica sulla documentazione di progetto
- Comando `/generate-arch` — generazione automatica documentazione tecnica
- Directory `docs/architecture/` con tre target: overview, data-model, class-diagram
- Convenzione implicita per il tracking dei file analizzati in `raw/`
  (traccia in wiki/, non markup sui file originali)

# Changelog
## Versione 2 - branch `AI-powered`
### 2.0.0
Template realizzato impostando:
- sistema di supporto per Claude Code
- non è stata gestito un manifest.md per settare i documenti in raw/ elaborati dalla AI

## Versione 1 - branch `templateV1`
### 1.0.0
Template realizzato impostando:
- setup del template con Poetry
- progetto mkdocs (con Material) per documentazione e sito statico
- implementazione di un logger personalizzato