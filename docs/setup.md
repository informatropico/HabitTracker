# Setup

## Descrizione Template

Questo è un template Python moderno che integra:

- **Poetry**: gestione delle dipendenze e del packaging
- **MkDocs**: documentazione automatica e sito statico
- **Python**: linguaggio di programmazione

Il template è mantenuto con diversi branch, ognuno corrispondente a una versione specifica. Il branch `main` contiene sempre l'ultima versione disponibile.

### Versionamento

Ogni versione del template ha il proprio branch dedicato. Per accedere a una versione specifica, checkout il relativo branch. Il branch `main` contiene tutte le versioni precedenti nel changelog.

## Installazione

### Configurazione dell'ambiente (macOS)
Verifica che tutti i compoenti necessari siano installati

```bash
xcode-select --install
xcode-select -p

#Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew --version

#Una cosa importante: alla fine dell'installazione Homebrew ti darà probabilmente 2-3 comandi da eseguire per aggiungerlo al PATH. Sono fondamentali — senza di quelli il terminale non troverà brew.
#Copia quei comandi e incollali esattamente come te li dà.

#pyenv (gestire più versioni di python)
brew install pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc
pyenv --version

#Python
brew install xz #facoltativo (compressione)
pyenv install 3.14
pyenv global 3.14
python --version

#pipx per la gestione dei tool in virtualenv
brew install pipx
pipx ensurepath
source ~/.zshrc
pipx --version

#poetry per la gestione dei pacchetti
pipx install poetry
poetry --version

#git e ssh
#verifica di avere un account github
git --version
git config --global user.name "tuo user"
git config --global user.email "tua@email.com"
git config --list

ls ~/.ssh
ssh-keygen -t ed25519 -C "tua@email.com"
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519

mkdir -p ~/.ssh
nano ~/.ssh/config
```
Copia nel file di configurazione:

```
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519
```

Poi salva: Ctrl+O → Invio → Ctrl+X per uscire.

```bash
cat ~/.ssh/id_ed25519.pub
#Copiare chiave su github

ssh -T git@github.com

#VS Code
brew install --cask visual-studio-code
```

Una volta scaricato il template, è necessario installare tutte le dipendenze:

```bash
poetry install
```

Questo comando installerà:
- Tutte le dipendenze principali
- Tutte le dipendenze di sviluppo
- Gli strumenti necessari per la documentazione e il testing

## Logger

Il template include un logger riutilizzabile in `src/python_template/logger.py`.

Per usarlo in un modulo:

```python
from python_template.logger import get_logger

logger = get_logger(__name__)
logger.info("messaggio")
```

Nel file di entry point, configura il level prima di tutto:

```python
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

## Changelog

Il file changelog documenta tutte le variazioni e gli aggiornamenti di ogni versione del template. Il branch main contiene tutti gli aggiornamenti del template.

### Versione Corrente

Questa versione fa riferimento alla versione del template 1.x.y, trovi lo stesso template nel branch `templateV1`