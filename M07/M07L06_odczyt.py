### 🔴 pickle - odczyt

# Jak wczytać dane z pliku data.db z poprzedniej lekcji?

import pickle

filename = 'data.db'
with open(filename, 'rb') as stream:
    obj_restored = pickle.load(stream)
    
print('obj_restored =', obj_restored)

### 🔴 Ćwiczenie

# Napisz program, który będzie bazował na pliku todos.db stworzonym w poprzednim ćwiczeniu.
# Załaduj plik do pamięci i wyświetl wszystkie zadania w formie tabeli.