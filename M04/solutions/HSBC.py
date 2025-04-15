from dateutil import parser
import sys
import requests

# Definitions of variables and constants
IGNORE_MISSING_PARNAME = '--ignore-missing'
DATA_FORMAT = "%Y-%m-%d"
code = None # currency
date = None # date_of_currency
args = sys.argv[1:]

ignore_missing = False

print("KALKULATOR WALUT")
# Check arguments and flags on the command linefor arg in args:
for arg in args:
    if arg == IGNORE_MISSING_PARNAME:
        ignore_missing = True
    elif not code:
        code = arg.upper()
    elif not date:
        date = parser.parse(arg).strftime(DATA_FORMAT)
# If the required parameters are missing, download from the user
if not code:
    code = input("Podaj kod waluty: ").upper()
if not date:
    date = input("Podaj datę: ")
    date = parser.parse(date).strftime(DATA_FORMAT)

# Prepare URL
URL = f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"

# Data download
try:
    resp = requests.get(URL)
    data = resp.json()

    # Displaying the course
    rate = data['rates'][0]['mid']
    print(f"Kurs waluty {code} na dzień {date} wynosi {rate}")

    #If out of date
except ValueError:
    print("Brak danych")