### 🔴 Ćwiczenie

# Zmodyfikuj program z ćwiczenia M03L16. W tamtym programie prosiłæś użytkownika o ścieżkę do wielu plików, a następnie program zmieniał rozszerzenie wszystkich plików na ".bak".
# Zmodyfikuj program tak, aby docelowe rozszerzenie można było podać jako argument wiersza poleceń. Przy czym jeśli nie zostanie on podany, wówczas użyj ".bak".

# Podpowiedź: używając składni lista[index], jeżeli index wykracza poza listę, wówczas otrzymujesz wyjątek IndexError.
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
            extension = ""
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