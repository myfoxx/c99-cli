#!/usr/bin/env python3

import requests
import json
from tqdm import tqdm
import time
import os


API_KEY = "XXXX"  # Sostituisci con la tua chiave API

# Funzione per stampare JSON in modo leggibile, con chiavi in grassetto e valore limitato in lunghezza
def my_print_json(data, indent=0, max_length=50):
    for key, value in data.items():
        if isinstance(value, dict):
            print(" " * indent + "\033[1m" + f"{key}:\033[0m")  # Grassetto
            my_print_json(value, indent + 4, max_length)
        elif isinstance(value, list):
            print(" " * indent + "\033[1m" + f"{key}:\033[0m")  # Grassetto
            for item in value:
                if isinstance(item, dict):
                    my_print_json(item, indent + 4, max_length)
                else:
                    print(" " * (indent + 4) + str(item))
        else:
            value_str = str(value)
            if len(value_str) > max_length:
                print(" " * indent + "\033[1m" + f"{key} =\033[0m {value_str[:max_length]}...")  # Grassetto per la chiave
            else:
                print(" " * indent + "\033[1m" + f"{key} =\033[0m {value_str}")  # Grassetto per la chiave
    print("\n")

# Elabora la risposta JSON e stampa in un formato leggibile
def process_response(response):
    try:
        data = response.json()
        if data.get("success", False):
            print("\n\033[91mEcco il risultato:\033[0m\n")  # Rosso
            my_print_json(data)
        else:
            print("Risposta non riuscita")
    except json.JSONDecodeError:
        print("Errore nel processare la risposta JSON")

# Esegue chiamate API e processa la risposta
def execute_api_call(api_url, parameters):
    clear_screen()
    print("\n")
    print("\033[1mDrin Driin, wake up NEO, chiamata API...\033[0m")
    response = requests.get(api_url, params=parameters)
    # Simula un'attività con una barra di progresso
    for _ in tqdm(range(100), desc="Elaborazione..."):
        time.sleep(0.02)  
    process_response(response)
    print("Chiamata API completata, tuu tuuu tuuuu")

# IP TOOL 

# Definizione delle funzioni API per ciascun tipo di target
api_functions = {
    # Funzioni per il target IP
    "ip": {
        "1": {"title": "IP Lookup", "url": "https://api.c99.nl/ip2domains", "param_key": "ip"},
        "2": {"title": "Proxy Detector", "url": "https://api.c99.nl/proxydetector", "param_key": "ip"},
        "3": {"title": "Port Scanner", "url": "https://api.c99.nl/portscanner", "param_key": "host"},
        "4": {"title": "IP to Host", "url": "https://api.c99.nl/gethostname", "param_key": "host"},
        "5": {"title": "IP 2 Domains", "url": "https://api.c99.nl/ip2domains", "param_key": "ip"},
        "6": {"title": "IP Validator", "url": "https://api.c99.nl/ipvalidator", "param_key": "ip"}
    },
    # Funzioni per il target URL
    "url": {
        "1": {"title": "Subdomain Finder", "url": "https://api.c99.nl/subdomainfinder", "param_key": "domain"},
        "2": {"title": "(WAF) Detector", "url": "https://api.c99.nl/firewalldetector", "param_key": "url"},
        "3": {"title": "DNS Checker", "url": "https://api.c99.nl/dnschecker", "param_key": "url"},
        "4": {"title": "Host to IP", "url": "https://api.c99.nl/portscanner", "param_key": "url"},
        "5": {"title": "Alexa Rank Checker", "url": "https://api.c99.nl/alexarank", "param_key": "url"},
        "6": {"title": "Whois Checker", "url": "https://api.c99.nl/whois", "param_key": "domain"},
        "7": {"title": "Site/URL Reputation Checker", "url": "https://api.c99.nl/reputationchecker", "param_key": "url"}
    },
    # Funzioni per il target host
    "host": {
        "1": {"title": "Get Website Headers", "url": "https://api.c99.nl/getheaders", "param_key": "host"},
        "2": {"title": "Proxy Check", "url": "https://api.c99.nl/proxycheck", "param_key": "host"},
        "3": {"title": "GeoIP Lookup", "url": "https://api.c99.nl/geoip", "param_key": "host"},
        "4": {"title": "Port Scanner", "url": "https://api.c99.nl/portscanner", "param_key": "host"}
    },
    # Funzioni per il target EMAIL
    "email": {
        "1": {"title": "Email Validator", "url": "https://api.c99.nl/emailvalidator", "param_key": "email"},
        "2": {"title": "Disposable Mail Check", "url": "https://api.c99.nl/disposablemailchecker", "param_key": "email"}
    },
    # Funzioni per il target VARIE
    "varie": {
        "1": {"title": "TO DO ... work in progress", "url": "https://api.c99.nl/getheaders", "param_key": "host"}
    }
}

# Genera e stampa il menu delle opzioni in base al tipo di target
def generate_menu(target_type, target):
    print("\n")
    print("\033[1m[[ MENU \033[96m" +target_type.upper()+"\033[0m\033[1m  ]]\033[0m")
    print("\033[1m[[ TARGET: \033[96m" +target.upper()+"\033[0m\033[1m  ]]\033[0m")
    for key, value in api_functions[target_type].items():
        print(f"{key}. {value['title']}")
    print("98. Torna al menu principalet")
    print("99. Esci")

# Ottiene l'input dell'utente in base al tipo di target
def get_input(type):
    return input(f"Inserisci {type}: ")

# Mostra un menu per scegliere il tipo di target, con scelte numeriche
def target_type_menu():
    menu_items = [
        "1. IP", "2. URL",
        "3. Host", "4. Email",
        "5. Varie", "6. Help"
    ]
    for i in range(0, len(menu_items), 2):
        print(f"{menu_items[i]:<15}{menu_items[i + 1] if i + 1 < len(menu_items) else ''}")
    choice = input("Scegli il tipo di target: ")
    return choice

# Stampa la guida all'uso dello strumento
def print_help():
    print("Guida all'uso dello strumento...")

def clear_screen():
    # 'cls' per Windows, 'clear' per altri sistemi operativi
    os.system('cls' if os.name == 'nt' else 'clear')


# Vabbé dai questa non te la devo spiegare :-) 
def main():
    target = None
    target_type = None

    while True:
        if not target_type:
            print("\033[95m[[ --|---------- + --------|-- ]]\033[0m")  # Colorazione in magenta
            print("\033[96m[[ --| C99.nl Command line |-- ]]\033[0m")  # Colorazione in ciano
            print("\033[95m[[ --|           +         |-- ]]\033[0m")  # Colorazione in magenta
            print("\033[96m[[ --|         Myfox       |-- ]]\033[0m")  # Colorazione in magenta
            print("\033[95m[[ --|---------- + --------|-- ]]\033[0m")  # Colorazione in magenta

            print("\n") 
            
            choice = target_type_menu()
            if choice == "6":
                print_help()
                continue
            elif choice in ["1", "2", "3", "4", "5"]:
                target_types = {"1": "ip", "2": "url", "3": "host", "4": "email", "5": "varie"}
                target_type = target_types[choice]
                target = get_input(target_type)
            else:
                print("Selezione non valida. Riprova.")

        generate_menu(target_type, target)
        choice = input("Scegli un'opzione: ")
        if choice in api_functions[target_type]:
            api_info = api_functions[target_type][choice]
            execute_api_call(api_info["url"], {api_info["param_key"]: target, "key": API_KEY, "json": ""})
        elif choice == "98":
            target_type = None
            target = None
            continue
        elif choice == "99":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")


# pare che le due linee seguenti servano a qualcosa di importante ! 
if __name__ == "__main__":
    main()
