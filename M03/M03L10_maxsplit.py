### 🔴 Chcę dzielić, ale jednak nie do końca...

line = '25.00  opis   wydatku'
tokens = line.split()
print('tokens =', tokens)
expense = float(tokens[0])
print('expense =', expense)

# Z pomocą przychodzi parametr maxsplit
two_tokens = line.split(maxsplit=1)
print('two_tokens =', two_tokens)
expense = float(two_tokens[0])
print('expense =', expense)
description = two_tokens[1]
print('description =', description)

### 🔴 Ćwiczenie

# Napisz program, który pyta o nazwę pliku, a następnie zmienia jego rozszerzenie na ".bak".
# Na ten moment wystarczy, że wyświetlisz nową nazwę pliku. Realną zmianą nazwy pliku zajmiemy się w kolejnych lekcjach.
# W tym celu podzielisz nazwę pliku na "właściwą" nazwę pliku oraz rozszerzenie.
# Uwaga! Program powinien działać także dla plików, które nie mają rozszerzenia, a także dla takich, które mają w nazwie więcej niż jedną kropkę! Na przykład:
#
#   NAZWA PLIKU      -> WŁAŚCIWA NAZWA     ROZSZERZENIE
#   plik.txt         -> plik               txt
#   wiele.kropek.txt -> wiele.kropek       txt
#   bez_rozszerzenia -> bez_rozszerzenia   (pusty string)
#
# Metoda .split() zaczyna dzielenie od lewej strony. W tym przypadku konieczne jest dzielenie od prawej strony - znajdź odpowiednią do tego metodę.

# Hint: jak sprawdzić, czy nazwa pliku zawiera kropkę? Bardzo prosto:
filename = 'plik.txt'
if '.' in filename:
    print('ma kropkę')
else:
    print('nie ma kropki')

# Hint: jak połączyć dwa stringi?
name = 'plik'
extension = '.txt'
filename = name + extension
print('filename =', filename)