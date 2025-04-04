### 🔴 Jakie przewagi mają skrypty uruchamiane z linii poleceń?

# Zazwyczaj nasz program potrzebuje danych wejściowych, takich jak tekst, liczby czy pliki, na których ma pracować nasz program. Do tej pory pytaliśmy o nie użytkownika przy pomocy funkcji input(). To podejście na dłuższą metę jest niewygodne, bo wymaga za każdym razem ręcznego podawania tych danych.

# Jest lepszy sposób, dzięki któremu można to zautomatyzować. Takie dane podamy w terminalu (= wierszu polecenia), w tej samej linii, w której określamy nazwę skryptu. Te dane będziemy teraz nazywać ARGUMENTAMI WIERSZA POLECEŃ. Przykładowe uruchomienie tego skryptu w terminalu:

# $ python M04/M04L02_sys_argv.py nazwa_pewnego_pliku.txt 1234 "tekst i nazwy plików zawierające spacje muszą być w cudzysłowach"

# Jednak jak można odczytać te argumenty w programie?

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


# Zwróć uwagę, że napisy możemy przekazywać także bez cudzysłowów jeśli tylko nie zawierają spacji. 

# sys.argv to lista stringów, nawet jeśli któryś argument jest liczbą! Trzeba ręcznie konwertować!

# sys.argv jako pierwszy element zawiera nazwę skryptu, a dopiero potem trzy argumenty!

### 🔴 Ćwiczenie

# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.