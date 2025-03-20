### 🔴 JSON

# API najczęściej zwraca dane w formacie JSON, XML lub CSV.

# JSON jest bardzo często stosowanym formatem wymiany danych, zbliżonym bardzo do tego, co jest wbudowane w Pythonie.
# Więcej o tym formacie: https://en.wikipedia.org/wiki/JSON#Data_types

import requests

URL = "https://covid-api.mmediagroup.fr/v1/cases"

resp = requests.get(URL)

print('type(resp.text) =', type(resp.text))
print('resp.text[:1000] =', resp.text[:1000])

### 🔴 Ćwiczenie

# Pobierz dane o zakażeniach COVID ze strony https://covid-api.mmediagroup.fr/v1/cases
# Znajdź w dokumentacji biblioteki requests, w jaki sposób możesz skonwertować string zawierający JSON na Pythonowe pozagnieżdżane słowniki i listy. Link do dokumentacji: https://docs.python-requests.org/en/latest/user/quickstart/
# Następnie wyciągnij informację o liczbie wszystkich zakażeń w Polsce. Wyświetl także ostatnią datę aktualizacji danych.