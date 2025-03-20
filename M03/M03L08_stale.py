### 🔴 Stałe

# Stałe to specjalne zmienne, których wartości nie zamierzasz zmieniać i które mają "zahardcodowane" wartości.
# Odróżniamy je od zwykłych zmiennych używająć WIELKICH_LITER i umieszczając je na samym początku skryptu.
# Takie stałe to np. umieszczona w kodzie nazwa pliku.

# ✅ Dobrze

EXPENSES_FILENAME = 'expenses.txt'

with open(EXPENSES_FILENAME) as stream:
    content = stream.read()

# ❌ Źle

with open('expenses.txt') as stream:
    content = stream.read()

# Stałe są przez Pythona traktowane tak jak zwykłe zmienne - a więc dalej można je nadpisać.

CONST = 50
CONST = 80

# Jednak nie powinniśmy tak robić. WIELKIE_LITERY to pewna konwencja, czyli umowa między programistami.
    
### 🔴 Ćwiczenie

# Napisz program, który ocenia jak bardzo "naukowo" brzmi dany tekst. W tym celu policz jak często w tym zdaniu pojawiają się liczby. Wyświetl jaki procent wszystkich "słów" to właśnie liczby.
# Postaraj się, aby program nie zwracał uwagi na interpunkcję. To znaczy, że w zdaniu "Numer 1234." drugie słowo to "1234.". Potraktuj je jako liczbę, pomimo że zawiera kropkę.
# To oznacza, że zdefiniujesz stałą zawierającą kilka znaków interpunkcyjnych.
# Samodzielnie znajdź metodę do określania, czy dany string jest liczbą.