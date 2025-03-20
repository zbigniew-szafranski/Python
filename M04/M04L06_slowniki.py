### 🔴 Listy nie dają rady! Słowniki, przybywajcie na pomoc!

# Listy to najczęściej wykorzystywana tzw. kolekcja - czyli typ pozwalający przechowywać wiele wartości w jednym obiekcie.
# Listy są jak arkusz kalkulacyjny z jedną kolumną - w każdym wierszu jest tylko jedna wartość.

# Słowniki są jak arkusze z dwoma kolumnami. Pierwszą z nich nazywamy KLUCZAMI, a drugą WARTOŚCIAMI. Jeden wiersz nazywamy ITEM.

person = {
    'first_name': 'Jan',  # pierwsz para klucz: wartość
    'last_name': 'Kowalski',
    'id': 123,
}
print('person =', person)

# Słowniki różnią się od arkusza tym, że mają unikalne klucze i że służą do mapowania - łatwego znalezienia wartości dla danego klucza.

print("person['first_name'] =", person['first_name'])  # ==> Jan  # w ten sposób wyświetlamy wartość dla danego klucza

# print(person['nie-istnieje'])  # ==> KeyError  
lista = ['A', 'B', 'C']
# print(lista[5])  # ==> IndexError  # w przypadku niepoprawnego indexu dla list otrzymujemy błąd IndexError

# Możemy dodać nowe klucze i wartości do słownika używając poniższej składni:

person['pesel'] = '12345678901'
print('person =', person)  # ==> {'first_name': 'Jan', ..., 'pesel': '12345678901'}

# Jeżeli jednak klucz się powtarza, wówczas NADPISUJEMY wartość dla tego klucza:

person['id'] = 456
print('person =', person)  # ==> {'first_name': 'Jan', 'last_name': 'Kowalski', 'id': 456, 'pesel': '12345678901'}  # klucz 'id' pojawia się wciąż tylko raz, a starą wartość utraciliśmy!

### 🔴 Ćwiczenie

# Narodowy Bank Polski udostępnia przez swoje API historyczne kursy walut. Otrzymałæś odpowiedź taką jak poniżej

response = {
    "table": "A",
    "currency": "dolar amerykański",
    "code": "USD",
    "rates": [
        {
            "no": "148/A/NBP/2021",
            "effectiveDate": "2021-08-03",
            "mid": 3.8315,
        },
    ],
}

# Jest to kurs waluty USD z dnia 3 sierpnia 2021. Z tak zagnieżdżonej struktury wyciągnij kurs waluty (klucz "mid").