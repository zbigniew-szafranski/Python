### 🔴 Ćwiczenie

# Rozwiń program z M04L05. Dodaj możliwość użycia przełącznika "--ignore-missing". Jeżeli zostanie on przez użytkownika podany, wówczas program nie powinien zatrzymywać się, gdy któryś z plików nie istnieje. W takiej sytuacji wyświetl pauzę ('-') zamiast konkretnej liczby linii, słów i znaków, a następnie przejdź do kolejnego pliku.
# Co zrobisz, aby w string formatting wyrównać pauzę do prawej strony, tak samo jak liczby? Znajdź odpowiedź w internecie (gdzie dokładnie - zagadka dla Ciebie :) ).
# W jaki sposób wykryjesz, czy został dodany przełącznik --ignore-missing?
# W jaki sposób oddzielisz go od listy plików?

# Przykładowe uruchomienia:
# $ python solutions/M04L15.py example.txt missing.txt another.txt --ignore-missing
# $ python solutions/M04L15.py example.txt missing.txt --ignore-missing another.txt
# $ python solutions/M04L15.py example.txt missing.txt another.txt
import sys

IGNORE_MISSING_PARNAME = '--ignore-missing'
filenames = sys.argv[1:]
PUNCTUATIONS = ".,?!"

ignore_miss = False
if IGNORE_MISSING_PARNAME in filenames:
    ignore_miss = True
    filenames.remove(IGNORE_MISSING_PARNAME)

print(" LINES  WORDS  CHARS  FILENAME")
for filename in filenames:
    try:
        with open(filename) as stream:
            content = stream.read()
            for punc in PUNCTUATIONS:
                content = content.replace(punc, "")
    except FileNotFoundError:
        content = None

    if content is None:
        lines_counter = '-'
        words_counter = '-'
        characters_counter = '-'
    else:
        lines = content.split('\n')
        lines_counter = len(lines)
        words_counter = len(content.split())
        characters_counter = len(content)

    print(f'{lines_counter:>6} {words_counter:>6} {characters_counter:>6} {filename:20}')