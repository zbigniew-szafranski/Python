### 🔴 Ćwiczenie

# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.
import sys

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