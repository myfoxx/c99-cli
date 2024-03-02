#!/usr/bin/env python3

import requests
import json
from tqdm import tqdm
import time
import os


API_KEY = "XXXX"  # Replace with your API key

# Function to print JSON legibly, with bold keys and limited value in length

def my_print_json(data, indent=0, max_length=50):
    for key, value in data.items():
        if isinstance(value, dict):
            print(" " * indent + "\033[1m" + f"{key}:\033[0m")  # Bold
            my_print_json(value, indent + 4, max_length)
        elif isinstance(value, list):
            print(" " * indent + "\033[1m" + f"{key}:\033[0m")  # Bold
            for item in value:
                if isinstance(item, dict):
                    my_print_json(item, indent + 4, max_length)
                else:
                    print(" " * (indent + 4) + str(item))
        else:
            value_str = str(value)
            if len(value_str) > max_length:
                print(" " * indent + "\033[1m" + f"{key} =\033[0m {value_str[:max_length]}...")  # Bold for the key
            else:
                print(" " * indent + "\033[1m" + f"{key} =\033[0m {value_str}")  # Bold for the key
    print("\n")

# Process JSON response and print in a readable format
def process_response(response):
    try:
        data = response.json()
        if data.get("success", False):
            print("\n\033[91mEere is the result:\033[0m\n")  # Rosso
            my_print_json(data)
        else:
            print("Unsuccessful answer")
    except json.JSONDecodeError:
        print("Error processing the JSON response")

# Run API calls and process response
def execute_api_call(api_url, parameters):
    clear_screen()
    print("\n")
    print("\033[1mDrin Driin, wake up NEO, API call...\033[0m")
    response = requests.get(api_url, params=parameters)
    # Simulate a task with a progress bar
    for _ in tqdm(range(100), desc="Processing..."):
        time.sleep(0.02)  
    process_response(response)
    print("API call completed, tuu tuuu tuuuu")


# IP TOOL 

# Definition of API functions for each target type
api_functions = {
    # Functions for the IP target
    "ip": {
        "1": {"title": "Proxy Detector", "url": "https://api.c99.nl/proxydetector", "param_key": "ip"},
        "2": {"title": "Port Scanner", "url": "https://api.c99.nl/portscanner", "param_key": "host"},
        "3": {"title": "IP to Host", "url": "https://api.c99.nl/gethostname", "param_key": "host"},
        "4": {"title": "IP 2 Domains", "url": "https://api.c99.nl/ip2domains", "param_key": "ip"},
        "5": {"title": "IP Validator", "url": "https://api.c99.nl/ipvalidator", "param_key": "ip"}
    },
    # Functions for the target URL
    "url": {
        "1": {"title": "Subdomain Finder", "url": "https://api.c99.nl/subdomainfinder", "param_key": "domain"},
        "2": {"title": "(WAF) Detector", "url": "https://api.c99.nl/firewalldetector", "param_key": "url"},
        "3": {"title": "DNS Checker", "url": "https://api.c99.nl/dnschecker", "param_key": "url"},
        "4": {"title": "Host to IP", "url": "https://api.c99.nl/portscanner", "param_key": "url"},
        "5": {"title": "Alexa Rank Checker", "url": "https://api.c99.nl/alexarank", "param_key": "url"},
        "6": {"title": "Whois Checker", "url": "https://api.c99.nl/whois", "param_key": "domain"},
        "7": {"title": "Site/URL Reputation Checker", "url": "https://api.c99.nl/reputationchecker", "param_key": "url"}
    },
    # Functions for the target host
    "host": {
        "1": {"title": "Get Website Headers", "url": "https://api.c99.nl/getheaders", "param_key": "host"},
        "2": {"title": "Proxy Check", "url": "https://api.c99.nl/proxycheck", "param_key": "host"},
        "3": {"title": "GeoIP Lookup", "url": "https://api.c99.nl/geoip", "param_key": "host"},
        "4": {"title": "Port Scanner", "url": "https://api.c99.nl/portscanner", "param_key": "host"}
    },
    # Functions for the EMAIL target
    "email": {
        "1": {"title": "Email Validator", "url": "https://api.c99.nl/emailvalidator", "param_key": "email"},
        "2": {"title": "Disposable Mail Check", "url": "https://api.c99.nl/disposablemailchecker", "param_key": "email"}
    },
    # Functions for the target VARIOUS
    "varie": {
        "1": {"title": "TO DO ... work in progress", "url": "https://api.c99.nl/getheaders", "param_key": "host"}
    }
}

# Generate and print options menu based on target type
def generate_menu(target_type, target):
    print("\n")
    print("\033[1m[[ MENU \033[96m" +target_type.upper()+"\033[0m\033[1m  ]]\033[0m")
    print("\033[1m[[ TARGET: \033[96m" +target.upper()+"\033[0m\033[1m  ]]\033[0m")
    for key, value in api_functions[target_type].items():
        print(f"{key}. {value['title']}")
    print("98. Back to the main menu")
    print("99. Exit")

# Get user input based on target type
def get_input(type):
    return input(f"Insert {type}: ")

# Show a menu to choose the type of target, with numeric choices
def target_type_menu():
    menu_items = [
        "1. IP", "2. URL",
        "3. Host", "4. Email",
        "5. Various", "6. Help"
    ]
    for i in range(0, len(menu_items), 2):
        print(f"{menu_items[i]:<15}{menu_items[i + 1] if i + 1 < len(menu_items) else ''}")
    choice = input("Select the target type: ")
    return choice

# Stampa la guida all'uso dello strumento
def print_help():
    print("Guide to using the tool...")

def clear_screen():
    # 'cls' for Windows, 'clear' for other operating systems
    os.system('cls' if os.name == 'nt' else 'clear')


# Well, I don’t have to explain this to you :-)
def main():
    target = None
    target_type = None

    while True:
        if not target_type:
            print("\033[95m[[ --|---------- + --------|-- ]]\033[0m")  
            print("\033[96m[[ --| C99.nl Command line |-- ]]\033[0m")  
            print("\033[95m[[ --|           +         |-- ]]\033[0m") 
            print("\033[96m[[ --|         Myfox       |-- ]]\033[0m") 
            print("\033[95m[[ --|---------- + --------|-- ]]\033[0m") 

            print("\n")
            
            choice = target_type_menu()
            if choice == "6":
                print_help()
                continue
            elif choice in ["1", "2", "3", "4", "5"]:
                target_types = {"1": "ip", "2": "url", "3": "host", "4": "email", "5": "various"}
                target_type = target_types[choice]
                target = get_input(target_type)
            else:
                print("Invalid selection. Please try again.")

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
            print("Exit.")
            break
        else:
            print("Try again, the option is not valid.")


# From what I can tell, the following two lines serve a vital purpose!
if __name__ == "__main__":
    main()
