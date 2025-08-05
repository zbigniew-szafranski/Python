# Wejdź na stronę API Narodowego Banku Polskiego, pobierz stamtąd aktualne kursy walut (URL: http://api.nbp.pl/api/exchangerates/tables/a/), a następnie zapisz je do pliku kursy.json.

import requests
import sys

URL = "http://api.nbp.pl/api/exchangerates/tables/a/?format=json"
OUTPUT_FILE = 'kursy.json'
resp = requests.get(URL)
if not resp.ok:
    print("Błąd pobierania danych:")
    sys.exit(1)
content = resp.text
with open(OUTPUT_FILE, 'w') as stream:
    status = stream.write(content)
if status:
    print("Zapisano plik: ", OUTPUT_FILE)