### 🔴 Pobieranie danych z zewnętrznych API

# Wiele serwisów udostępnia dwa rodzaje interfejsu:
# - UI (User Interface) - do korzystania przez człowieka
# - API (Application Programming Interface) - do korzystania przez maszynę/skrypt.

# W przypadku webowego UI (czyli działającego w przeglądarce, a nie jako aplikacja desktopowa) dane są zwracane w postaci HTML + załączniki (pliki CSS, obrazki oraz skrypty w Javascript). Pobierzmy stronę z Wikipedii:

import requests

URL = 'https://pl.wikipedia.org/wiki/Wikipedia:Strona_główna'

resp = requests.get(URL)

print('type(resp) =', type(resp))

# Nie otrzymujemy od razu zawartości strony jako string, tylko obiekt response. To podobnie jak w przypadku plików, gdzie korzystaliśmy ze strumieni.

# Sprawdźmy najpierw, czy nie było jakiegoś błędu - np. serwer Wikipedii mógł zwrócić informację, że nasze żądanie jest niepoprawne (np. niepoprawny URL).

print('resp.ok =', resp.ok)

# Wyświetly jak wygląda HTML Wikipedii:

print()
print(resp.text[:1000])

### 🔴 Ćwiczenie

# Wejdź na stronę API Narodowego Banku Polskiego, pobierz stamtąd aktualne kursy walut (URL: http://api.nbp.pl/api/exchangerates/tables/a/), a następnie zapisz je do pliku kursy.json.