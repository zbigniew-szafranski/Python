### 🔴 Obsługa błędów

# Sytuacje wyjątkowe to nie tylko IndexError (index poza listą), KeyError (brak klucza w słowniku) czy ZeroDivisionError.
# Może się też okazać, że chcemy otworzyć plik, którego nie ma. Wtedy funkcja open() RZUCA wyjątek FileNotFoundError.

# stream = open('missing.txt')  # ==> FileNotFoundError

### 🔴 Ćwiczenie

# Rozwiń program z M04L05. Dodaj możliwość użycia przełącznika "--ignore-missing". Jeżeli zostanie on przez użytkownika podany, wówczas program nie powinien zatrzymywać się, gdy któryś z plików nie istnieje. W takiej sytuacji wyświetl pauzę ('-') zamiast konkretnej liczby linii, słów i znaków, a następnie przejdź do kolejnego pliku.
# Co zrobisz, aby w string formatting wyrównać pauzę do prawej strony, tak samo jak liczby? Znajdź odpowiedź w internecie (gdzie dokładnie - zagadka dla Ciebie :) ).
# W jaki sposób wykryjesz, czy został dodany przełącznik --ignore-missing?
# W jaki sposób oddzielisz go od listy plików?

# Przykładowe uruchomienia:
# $ python solutions/M04L15.py example.txt missing.txt another.txt --ignore-missing
# $ python solutions/M04L15.py example.txt missing.txt --ignore-missing another.txt 
# $ python solutions/M04L15.py example.txt missing.txt another.txt 