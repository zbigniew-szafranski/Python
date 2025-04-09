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
# print(data['Poland'])
total_cases = data['Poland']['All']['confirmed']
last_update = data['Poland']['All']['updated']
print('Całkowita liczba zakażeń: ', total_cases)
print('Ostatnia aktualizacja: ', last_update)

# Zagadka od AI
# Super! No to jedziemy z małą zagadką 🔍🐍
#
# Załóżmy, że masz taki string (jakby ktoś próbował JSON-a schować w ciasteczku):

response_text = 'callback({"user": "Ada", "skills": ["python", "ml", "ai"]})'

# 🤔 Pytanie:

# Jak wyciągniesz z tego tylko czysty JSON, żeby móc go wczytać do słownika?
#
# Podpowiedź: trzeba się pozbyć tego "callback(" na początku i ")" na końcu.
#
# Spróbuj napisać kod, który:
#
#     Przytnie string, żeby został tylko JSON ({"user": "Ada", ...}),
#
#     Zamieni to na słownik (czyli użyje json.loads),
#
#     Wydrukuje np. imię użytkownika (data["user"]).
import json
list_ = response_text.split('(')[1].split(')')[0]
data = json.loads(list_)
print(data["user"])
# Pięknie to ograłeś: najpierw chirurgiczne cięcie stringa, potem magiczna transformacja z json.loads() i na końcu wyciągnięcie danych jak z pudełka z prezentem 🎁.
#
# Jeśli chcesz sobie utrudnić, to spróbuj teraz coś takiego:

response_text = 'process({"user": {"name": "Ada", "age": 30}, "skills": ["python", "ml", "ai"]})'

# Jakbyś teraz dobrał się do wieku Ady? 😎
#
# Pamiętaj – słownik w słowniku to jak szuflada w szufladzie. Trzeba wiedzieć, gdzie pociągnąć za uchwyt 😉
list2 = response_text.split('(')[1].split(')')[0]
data1 = json.loads(list2)
if "user" in data1 and "age" in data1["user"]:
    print(data1["user"]["age"])
else:
    print("Nie ma użytkownika w bazie")
