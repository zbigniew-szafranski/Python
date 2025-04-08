# Pobierz dane o zakażeniach COVID ze strony https://covid-api.mmediagroup.fr/v1/cases
# Znajdź w dokumentacji biblioteki requests, w jaki sposób możesz skonwertować string zawierający JSON na Pythonowe pozagnieżdżane słowniki i listy. Link do dokumentacji: https://docs.python-requests.org/en/latest/user/quickstart/
# Następnie wyciągnij informację o liczbie wszystkich zakażeń w Polsce. Wyświetl także ostatnią datę aktualizacji danych.
# Nowy link do dokumentacji biblioteki requests: https://requests.readthedocs.io/en/latest/user/quickstart/
#
# Uwaga! covid-api.mmediagroup.fr już nie działa. Wciąż możesz jednak pobrać dane z tego adresu:
#
# URL = "https://praktycznypython.pl/cases.json"
#
# Dane nie są już tam jednak aktualizowane, więc dostaniesz stan z grudnia 2022 roku.

import requests
import sys
URL = "https://praktycznypython.pl/cases.json"
resp= requests.get(URL)

if not resp.ok:
    print("Błąd pobierania danych")
    sys.exit(1)

data = resp.json()
print(data['Poland'])
total_cases = data['Poland']['All']['confirmed']
last_update = data['Poland']['All']['updated']
print('Całkowita liczba zakażeń: ', total_cases)
print('Ostatnia aktualizacja: ', last_update)

