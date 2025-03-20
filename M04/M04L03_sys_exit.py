### 🔴 Jak przedwcześnie zakończyć działanie programu?

# W tym celu wywołujemy sys.exit() przekazując kod zakończenia programu.

import sys

sys.exit(1)

print("Ten kod nie wykona się nigdy")

# Ten kod jest liczbą od 0 do 255. Jest to informacja dla wiersza polecenia, czy program zakończyć się poprawnie, czy błędem.
# 0 = poprawnie
# Każda inna liczba - błąd. Między różnymi typami błędów można rozróżniać, np. 1 może oznaczać brak pliku, 2 może oznaczać brak uprawnień etc.
# Ten kod w praktyce znaczenie tylko, gdy będziesz pisać skrypty wiersza poleceń (.bat) lub skrypty shella/basha (.sh).

# Ten mechanizm zgłaszania błędów jest zupełnie niezależny od błędów/wyjątków w Pythonie!

# sys.exit wywołujemy tylko gdy zorientujemy się, że argumenty wiersza poleceń są niepoprawne, np. jest ich za mało, mają niepoprawny typ etc. We wszystkich pozostałych sytuacjach korzystamy ze standardowego mechanizmu błędów/wyjątków.

# Na MacOS oraz Linuxie kod błędu możesz sprawdzić w terminalu wpisując:
# $ echo $? 
# Na Windowsie trzeba wpisać w wierszu polecenia:
# echo %errorlevel%

### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby wyświetlał komunikat błędu, gdy użytkownik nie poda nazwy pliku. Wyświetl błąd także wtedy, gdy poda więcej niż jeden plik.