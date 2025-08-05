### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby wyświetlał komunikat błędu, gdy użytkownik nie poda nazwy pliku. Wyświetl błąd także wtedy, gdy poda więcej niż jeden plik.
import sys
if len(sys.argv) == 1:
    print("Missing file")
    sys.exit(1)
elif len(sys.argv)>2:
    print("Too much files")
    sys.exit(2)

PUNCTATIONS = ".,?!"
print('sys.argv =', sys.argv)

for el in sys.argv:
    names, path = sys.argv
with open(path) as stream:
    content = stream.read().strip()
    for punc in PUNCTATIONS:
        content = content.replace(punc, "")
lines = content.splitlines()
words = content.split()
lenght = len(content)
words = len(words)
print(f"Ilość znaków: {lenght}")
print(f"Ilość słów: ", words)
print(f"Ilość lini: ", len(lines))
