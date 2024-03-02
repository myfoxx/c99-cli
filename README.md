# C99 API Command Line Tool

This script is a command-line tool that interacts with various APIs provided by [C99.nl](https://api.c99.nl/). It allows users to perform different network and analysis tasks such as IP lookup, proxy verification, IP geolocation, and more.

## Requirements

- Python 3.x
- Required libraries: `requests`, `json` (e `tqdm` if implemented)

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/myfoxx/c99-cli.git
cd c99-cli
pip install -r requirements.txt
chmod +x c99-cli.py
```

## Use

Set your API key C99.nl

```
API_KEY =  "VALUE"
```
Run the command line script to access a number of API features.
On startup, you will see a main menu with the following options:

1. IP
2. URL
3. Host
4. Email
5. Varius (TO DO) 
6. Help


## Usage
Run the script from the command line. A menu will appear with options to choose from various API functionalities. The usage flow is:
1. Select the type of check (e.g., IP, URL, Host).
2. Input the target based on the selected check type.
3. Choose from the specific options provided for that check type.
   - Example: If 'IP' is selected, options like IP Lookup, Proxy Check, etc., are available.
4. Users can go back to change the check type and target as needed.

## Contributing
Contributions to the C99 Tool CLI are welcome. Feel free to fork the repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Donations
If you find this tool helpful and would like to support its development, donations are appreciated. DOGE DN4MEB5L41u98EP99cpTgZXt1QbEfQUVJx

## Credits
Developed by _MYFOX_. Special thanks to contributors and the C99.nl API services.

## TODO 
- Implement the missing APIs
- possibility to save the results to a file
- anything else you consider useful

## License
This project is released under the GNU General Public License.


