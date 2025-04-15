import requests
import sys
from dateutil import parser

# Definitions of variables and constants
IGNORE_MISSING_PARNAME = '--ignore-missing'
args = sys.argv[1:]
ignore_missing = False
code = None  # Waluta
date = None  # Data

# Check arguments and flags on the command linefor arg in args:
for arg in args:
    if arg == IGNORE_MISSING_PARNAME:
        ignore_missing = True
        print("Flaga obecna")
    elif not code:
        code = arg.lower()
    elif not date:
        date = parser.parse(arg).strftime("%Y-%m-%d")

# If the required parameters are missing, download from the user
if not code:
    code = input("Podaj kod waluty: ").lower()
if not date:
    date = input("Podaj datę (RRRR-MM-DD): ")
    date = parser.parse(date).strftime("%Y-%m-%d")

# Prepare URL
URL = f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"

# Data download
try:
    # Get data from API with timeout set
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()  # Rzuć wyjątek, jeśli odpowiedź to 4xx/5xx

    # Verify response format
    if "application/json" not in resp.headers.get("Content-Type", ""):
        raise ValueError("Odpowiedź nie zawiera danych w formacie JSON.")

    # JSON response parsing
    data = resp.json()
    rates = data.get("rates")
    if not rates or not isinstance(rates, list) or "mid" not in rates[0]:
        raise KeyError("Brak wymaganych danych w odpowiedzi API.")

    # Displaying the course
    rate = rates[0]["mid"]
    print(f"Kurs waluty {code.upper()} w dniu {date}: {rate} PLN")

except requests.exceptions.HTTPError:
    print(f"Brak danych dla waluty {code.upper()} w dniu {date}.")
