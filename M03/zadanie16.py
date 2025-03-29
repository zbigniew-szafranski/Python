### 🔴 Ćwiczenie

# Rozwiń program z M03L12 tak, aby program najpierw wyświetlił jakie nastąpią zmiany plików, następnie poprosił użytkownika o potwierdzenie i dopiero potem dokonał zmiany nazw.
# W tym celu potrzebujesz listę zmian. Każda zmiana będzie dwuelementową listą zawierającą starą i nową nazwę pliku. Będziesz mieć do czynienie z listą list.

import os
import glob
NEW_EXTENSION = '.bak'
pattern = input('Podaj wzorzec: ')
filenames = glob.glob(pattern)
operations = []

for  filename in filenames:
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1)
            name, extension = tokens
        else:
            name= filename
            extension = ""
        new_filename = name + NEW_EXTENSION
        operation = [filename, new_filename]
        operations.append(operation)
print("Zostaną dokonane następujące zmiany:")
for old, new in operations:
    print(old, "->", new)
choice = input("Czy kontynuować? [t/n] ")
if choice.lower() == 't':
    for old, new in operations:
        os.rename(old, new)
        print("Zmieniono:", old, "→", new)
    print("Success!")
else:
    print("Anulowano!")