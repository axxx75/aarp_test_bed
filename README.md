# aarp-test-bed

Repository di test per esercitazioni e analisi statiche.

Contenuto:
- `config.yaml` con una chiave mancante o errata.
- `src/main.py` entrypoint con un bug logico e un import inesistente.
- `src/utils.py` con due funzioni utility (una contiene un errore di tipo/sintassi).
- `src/database.py` connessione DB con password hardcoded (security finding).
- `scripts/deploy.sh` script bash con sintassi non-POSIX e variabile non quotata.

Scopo: fornire un piccolo progetto (200–300 righe) per test automatici, code review e rilevamento di problemi.

