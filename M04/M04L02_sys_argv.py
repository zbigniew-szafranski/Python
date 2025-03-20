### 🔴 Jakie przewagi mają skrypty uruchamiane z linii poleceń?

# Zazwyczaj nasz program potrzebuje danych wejściowych, takich jak tekst, liczby czy pliki, na których ma pracować nasz program. Do tej pory pytaliśmy o nie użytkownika przy pomocy funkcji input(). To podejście na dłuższą metę jest niewygodne, bo wymaga za każdym razem ręcznego podawania tych danych.

# Jest lepszy sposób, dzięki któremu można to zautomatyzować. Takie dane podamy w terminalu (= wierszu polecenia), w tej samej linii, w której określamy nazwę skryptu. Te dane będziemy teraz nazywać ARGUMENTAMI WIERSZA POLECEŃ. Przykładowe uruchomienie tego skryptu w terminalu:

# $ python M04/M04L02_sys_argv.py nazwa_pewnego_pliku.txt 1234 "tekst i nazwy plików zawierające spacje muszą być w cudzysłowach"

# Jednak jak można odczytać te argumenty w programie?

import sys

print('sys.argv =', sys.argv)
print()

for el in sys.argv:
    print(type(el), el)

# Zwróć uwagę, że napisy możemy przekazywać także bez cudzysłowów jeśli tylko nie zawierają spacji. 

# sys.argv to lista stringów, nawet jeśli któryś argument jest liczbą! Trzeba ręcznie konwertować!

# sys.argv jako pierwszy element zawiera nazwę skryptu, a dopiero potem trzy argumenty!

### 🔴 Ćwiczenie

# Napisz program, który otwiera wskazany przez użytkownika plik (wskazany jako argument linii poleceń, a nie przez input()) i zlicza ile jest w nim znaków, słów i linii.