### 🔴 Parametry pozycyjne vs nazwane (positional vs keyword arguments)

# Prawie wszystkie argumenty przekazywaliśmy do tej pory jako argumenty pozycyjne. Jedynie funkcję print mogliśmy wywołać przekazując end=' ' jako parametr tzw. nazwany:

first_positional = 1
second_positional = 2
print(first_positional, second_positional, end=' ')
print('!')

# Każdy argument możemy przekazać jako pozycyjny lub jako nazwany - to nasz wybór:

def add(a, b, c, force_conversion=False):
    if force_conversion:
        a = float(a)
        b = float(b)
        c = float(c)
    return a + b + c

print(add('1', '2', '3', True))
print(add('1', '2', c='3', force_conversion=True))
print(add('1', '2', force_conversion=True, c='3'))  # ✅ parametry nazwane możesz przekazać w dowolnej kolejności
# print(add('1', '2', force_conversion=False, '3'))  # ==> SyntaxError: positional argument follows keyword argument  # ❌ parametry nazwane muszą znaleźć się na końcu, po wszystkich pozycyjnych (tak samo jak definiując funkcję parametry opcjonalne muszą znaleźć się za wymaganymi)
print(add('1', '2', c='3'))  # ✅ wartości domyślne dalej działają
        
### 🔴 W praktyce argumenty przekazujemy w sposób nazwany gdy:

# 1. W wywołaniu nie jest oczywiste, jakie jest znaczenie argumentu:

print(add(1, 2, 3, True))  # ❌ co oznacza ten False? Nie wiemy dopóki nie zaglądniemy w dokumentację lub w definicję funkcji
print(add(1, 2, 3, force_conversion=True))  # ✅ i od razu wiadomo, za co odpowiada to True

# 2. Gdy musielibyśmy podać argumenty opcjonalne, których nie chcemy podawać, bo chcemy skorzystać z domyślnej wartości.

def load_file(filename, ignore_missing_lines=False, encoding='utf-8', mode='r', binary=False, convert_floats=False):
    print('Loading and processing file.')
    
load_file('pliczek.txt', False, 'utf-8', 'r', True)  # ❌ ugh, tyle roboty, żeby określić jedynie że plik jest binarny
load_file('pliczek.txt', binary=True)  # ✅ dobrze

# 3. (Rzadka sytuacja) Gdy funkcja przyjmuje dowolną liczbą argumentów pozycyjnych tak jak print.

print('Komunikat', end=' ')  # ✅ chcemy osiągnąć ten rezultat
print('Komunikat', ' ')  # ❌ to ma zupełnie inne znaczenie

### 🔴 Ćwiczenie

# Usprawnij rozwiązanie poprzedniego ćwiczenia - zastosuj parametry nazwane w M05L05_dodatek.