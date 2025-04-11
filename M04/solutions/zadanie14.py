### 🔴 Ćwiczenie

# Rozwiń program z M04L12 tak, aby potrafił odróżnić brak rozszerzenia (np. "plik") od pustego rozszerzenia (np. "plik.").
import os
import glob
import sys

DEFAULT_EXTENSION = '.bak'
pattern = input('Podaj wzorzec: ')
filenames = glob.glob(pattern)
operations = []

try:
    path = sys.argv[1]
    new_extension = "."+path
except IndexError:
    new_extension = DEFAULT_EXTENSION

for  filename in filenames:
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1)
            name, extension = tokens
        else:
            name= filename
            extension = None
        new_filename = name + new_extension
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