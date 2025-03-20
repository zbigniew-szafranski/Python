### 🔴 Obsługa błędów

# Do tej pory pojawienie się błędu (= wyjątku) powodowało zatrzymanie programu.
# Często jednak chcemy w razie błędu wykonać ratunkowe operacje, a potem wznowić program tak, jakby błędu nie było.
# Do tego służy instrukcja try-except.

### 🔴 Sad path

print("SAD PATH")  # Przedstawimy teraz sytuację nazywaną sad-path - czyli pojawi się błąd
first = 10  # float(input('Podaj liczbę: '))
second = 0  # float(input('Podaj drugą liczbę: '))
# result = first / second  # ==> ZeroDivisionError  # i cały program się zatrzymuje
try:
    result = first / second
    print('koniec try')  # ten kod się nie wykona - w przypadku błędu w TRY od razu skaczemy do EXCEPT
except ZeroDivisionError:  # zawsze podaj rodzaj wyjątku, który chcesz ŁAPAĆ
    print('except')
    result = 'błąd'  # ten kod jest wykonany tylko w przypadku błędu ZeroDivisionError (tzw. sad path)
print('Rezultat:', result)  # ==> Rezultat: błąd  # wykona się - po OBSŁUŻENIU błędu kontynuujemy tak, jakby go nie było

### 🔴 Happy path

print('HAPPY PATH')  # happy-path - co gdy nie będzie błędu
first = 10
second = 5
try:
    result = first / second
    print('koniec try')  # wykona się
except ZeroDivisionError:
    print('except')  # cały EXCEPT jest pomijany, bo nie było błędu
    result = 'błąd'
print('Rezultat:', result)  # wykona się - nie było błędu, więc dlaczego mielibyśmy się zatrzymać?

### 🔴 Very sad path

print('VERY SAD PATH')  # co, gdy pojawi się błąd inny niż ZeroDivisionError?
first = 10
second = 5
try:
    result = first / secodn  # (!) zwróć uwagę na celową literówkę w `secodn` - to generuje wyjątek NameError
    print('koniec try')  # nie wykona się
except ZeroDivisionError: 
    print('except')  # cały EXCEPT jest pomijany, bo mamy do czynienia z NameError, a nie z ZeroDivisionError
    result = 'błąd'
# Nie było except NameError, więc błąd jest dalej NIEobsłużony, a zatem zatrzymujemy cały program.
print('Rezultat:', result)  # nie wykona się

### 🔴 Ćwiczenie

# Zmodyfikuj program z ćwiczenia M03L16. W tamtym programie prosiłæś użytkownika o ścieżkę do wielu plików, a następnie program zmieniał rozszerzenie wszystkich plików na ".bak".
# Zmodyfikuj program tak, aby docelowe rozszerzenie można było podać jako argument wiersza poleceń. Przy czym jeśli nie zostanie on podany, wówczas użyj ".bak".

# Podpowiedź: używając składni lista[index], jeżeli index wykracza poza listę, wówczas otrzymujesz wyjątek IndexError.