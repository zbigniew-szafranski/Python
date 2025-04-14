import requests
import sys
from dateutil import parser

# Definicje zmiennych i stałych
IGNORE_MISSING_PARNAME = '--ignore-missing'
args = sys.argv[1:]
ignore_missing = False
code = None  # Waluta
date = None  # Data

# Sprawdzamy argumenty i flagi w wierszu poleceń
for arg in args:
    if arg == IGNORE_MISSING_PARNAME:
        ignore_missing = True
        print("Flaga obecna")
    elif not code:
        code = arg.lower()
    elif not date:
        date = parser.parse(arg)
        date = date.strftime("%Y-%m-%d")

# Jeśli brak wymaganych parametrów, pobierz od użytkownika
if not code:
    code = input("Podaj kod waluty: ").lower()
if not date:
    date = input("Podaj datę (RRRR-MM-DD): ")
    date = parser.parse(date)
    date = date.strftime("%Y-%m-%d")

# Przygotowanie URL
URL = f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"

# Pobieranie danych
try:
    # Pobierz dane z API z ustawionym timeout
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()  # Rzuć wyjątek, jeśli odpowiedź to 4xx/5xx

    # Zweryfikuj format odpowiedzi
    if "application/json" not in resp.headers.get("Content-Type", ""):
        raise ValueError("Odpowiedź nie zawiera danych w formacie JSON.")

    # Parsowanie odpowiedzi JSON
    data = resp.json()
    rates = data.get("rates")
    if not rates or not isinstance(rates, list) or "mid" not in rates[0]:
        raise KeyError("Brak wymaganych danych w odpowiedzi API.")

    # Wyświetlenie kursu
    rate = rates[0]["mid"]
    print(f"Kurs waluty {code.upper()} w dniu {date}: {rate} PLN")

except requests.exceptions.HTTPError as e:
    print(f"Błąd: Nie można znaleźć danych dla waluty {code.upper()} w dniu {date}. Szczegóły: {e}")
except requests.exceptions.RequestException as e:
    print(f"Błąd: Nie udało się nawiązać połączenia z API NBP. Szczegóły: {e}")
except KeyError as e:
    print(f"Błąd: Otrzymano nieprawidłowe dane z API. Szczegóły: {e}")
except ValueError as e:
    print(f"Błąd: {e}")
