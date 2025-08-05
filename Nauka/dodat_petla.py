# Napisz program, który wyświetla w kolejnych liniach liczby 0, 1, 2, 3 itd. aż do 10. Użyj konstrukcji `for i in range(11)`.
#2. Fizzbuzz. Rozwiń poprzedni program tak, aby jeżeli liczba jest podzielna przez 3 (co sprawdzisz warunkiem `i % 3 == 0`, czyli reszta z dzielenia przez 3 równa 0), to wypisz "fizz", a jeśli podzielna przez 5, to wypisz "buzz".
for i in range(11):
    
    if i % 3 == 0:
        print("fizzz")
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)