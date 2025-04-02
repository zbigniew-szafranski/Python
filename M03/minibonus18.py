# Bonusowe minićwiczenia:
#
# 1. Napisz program, który wydrukuje prostokąt o wymiarach m x n, składający się z znaku *. Rozmiar prostokąta powinien być określony przez dwie zmienne: m (ilość wierszy) oraz n (ilość kolumn). Podpowiedź: użyj `for i in range(10)`, aby dokonać 10 powtórzeń.
#
# 2. Napisz program, który wydrukuje tabliczkę mnożenia dla liczb od 1 do 10. Podpowiedź: sprawdź jakie jeszcze argumenty przyjmuje funkcja range.
# ad.1
m = 5
n = 7

for i in range(m):
    for j in range(n):
        print('*', end=' ')
    print()
# ad.2
for i in range(1,21):
    for j in range(1,21):
        print(i*j , end='\t')
    print()
