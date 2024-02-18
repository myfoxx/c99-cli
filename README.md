# C99 API Command Line Tool

Questo script è uno strumento da riga di comando che interagisce con varie API fornite da c99.nl. Permette agli utenti di eseguire diverse operazioni di rete e di analisi come il lookup di IP, la verifica di proxy, la geolocalizzazione IP, e altro ancora.

## Requisiti

- Python 3.x
- Librerie richieste: `requests`, `json` (e `tqdm` se implementato)

## Uso

Esegui lo script da linea di comando per accedere a una serie di funzionalità API.

All'avvio, verrà visualizzato un menu principale con le seguenti opzioni:

1. IP
2. URL
3. Host
4. Email
5. Varie
6. Help

Scegli un'opzione numerica per specificare il tipo di verifica che desideri effettuare. Dopo aver selezionato il tipo di verifica (ad esempio, IP, URL o Host), ti verrà chiesto di inserire il target specifico per quella categoria.

Ad esempio, se scegli "1. IP", dovrai inserire un indirizzo IP per procedere con la verifica.

In ogni momento, hai la possibilità di tornare al menu principale e scegliere un tipo di verifica o un target diverso utilizzando le opzioni:

- `98. Cambia Target` per selezionare un nuovo target.
- `99. Esci` per uscire dal programma.

Ogni scelta porta a un set di funzionalità API specifiche per il tipo di target selezionato.

## Installazione

Clona il repository e installa le dipendenze:

```bash
git clone https://github.com/myfoxx/c99-cli.git
cd c99-cli
pip install -r requirements.txt
