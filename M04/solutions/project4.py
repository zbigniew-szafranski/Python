# Pomóż szwajcarskiemu bankowi HSBC tworząc aplikację, która odczytuje i analizuje dane z Narodowego Banku Polskiego (NBP) udostępnione przez API i podaje ile była warta wskazana waluta we wskazanym dniu.

# Dzięki Tobie HSBC będzie mógł poprawnie wystawiać w Polsce faktury w walucie obcej - przepisy wymagają, aby kwoty na takich fakturach przeliczać na złotówki wg kursów NBP z określonych dni.

# 1. Zapoznaj się z opisem API: http://api.nbp.pl.
#    1. Ustal jak wygląda URL, pod którym znajdziesz kurs danej waluty z danego dnia?
#    2. W jakim formacie musi być data?
#    3. Co trzeba zmienić w URLu, aby otrzymać odpowiedź w JSONie zamiast XMLu?
# 2. Tabele kursów są publikowane tylko w dni robocze. Przeczytaj w dokumentacji co się stanie, gdy zapytasz o kurs z weekendu lub innego dnia wolnego od pracy?
# 3. Twój program przyjmuje walutę oraz datę jako dwa argumenty wiersza poleceń. Jeśli jednak nie zostaną podane, wówczas poproś użytkownika o podanie tych dwóch informacji przy pomocy funkcji input.
import requests
import sys
from dateutil import parser


# URL = https://api.nbp.pl/api/exchangerates/rates/{table}/code}/{date}/
args = sys.argv[1:]
IGNORE_MISSING_PARNAME = '--ignore-missing'

ignore_missing = False
code = None  # Na razie brak waluty
date = None  # Na razie brak daty

# Sprawdzamy, czy flaga i inne argumenty są obecne
for arg in args:
    if arg == IGNORE_MISSING_PARNAME:
        ignore_missing = True
        print("Flaga obecna")
    elif not code:  # Jeśli waluta jeszcze nie została znaleziona
        code = arg.lower()
    elif not date:  # Jeśli waluta jest ustawiona, szukamy daty
        date = parser.parse(arg)
        date = date.strftime("%Y-%m-%d")

# Jeśli nie ma daty lub waluty, poproś użytkownika
if not code:
    code = input("Podaj kod waluty: ").lower()
if not date:
    date = input("Podaj datę: ")
    date = parser.parse(date)
    date = date.strftime("%Y-%m-%d")



URL = f"https://api.nbp.pl/api/exchangerates/rates/a/{code}/{date}/?format=json"


try:
    resp = requests.get(URL, timeout=10)
    resp.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
    data = resp.json()
    rates = data.get("rates")
    if not rates or not isinstance(rates, list) or "mid" not in rates[0]:
        raise KeyError("Brak wymaganych danych w odpowiedzi API.")
    rate = data["rates"][0]["mid"]
    print(f"Kurs waluty {code.upper()} w dniu {date}: {rate} PLN")
except requests.exceptions.HTTPError:
    print(f"Błąd: Nie można znaleźć danych dla waluty {code.upper()} w dniu {date}.")
except requests.exceptions.RequestException:
    print("Błąd: Nie udało się nawiązać połączenia z API NBP.")
except KeyError:
    print("Błąd: Otrzymano nieprawidłowe dane z API.")
