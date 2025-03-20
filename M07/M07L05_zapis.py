### 🔴 pickle - najprostszy mechanizm perzystencji danych - zapis

# Często programy muszą przechowywać dane pomiędzy uruchomieniami.
# Dlatego przechowujemy dane w bazach danych albo prościej, w plikach CSV i innych formatach.
# Wymagają one jednak napisania kawałka kodu, który importuje i eksportuje takie dane.
# Moduł pickle pozwala Ci w bardzo prosty sposób zapisać dowolne obiekty do pliku - liczby, stringi, listy, słowniki, a nawet obiekty Twoich własnych klas.

import pickle

obj = [1, 2, 3]  # To może być dowolny obiekt, który chcesz zapisać.

filename = 'data.db'  # rozszerzenie pliku nie ma znaczenia, tutaj użyliśmy .db
with open(filename, 'wb') as stream:  # plik należy otworzyć w trybie BINARNYM zamiast tekstowym, stąd litera 'b'
    pickle.dump(obj, stream)

### 🔴 Ćwiczenie

# Napisz program, który tworzy plik todos.db, w którym będzie przechowywana lista zadań.
# Po uruchomieniu tego programu lista zadań powinna być pusta, chyba że podano przełącznik --example - wówczas powinna zawierać przykładowe zadania (możesz zahardcodować je w kodzie).