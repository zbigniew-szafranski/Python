### 🔴 Jeszcze więcej wyrażeń listowych

# Do realizacji kolejnego ćwiczenia potrzebujesz wbudowanej funkcji sum():

numbers = [2, 3, 4]
sum_ = sum(numbers)
print('sum_ =', sum_)  # ==> sum_ = 9

# Ta funkcja jest przydatna, kiedy zliczamy pewne elementy. Nie musimy wtedy tworzyć licznika `total`, tak jak poniżej:

total = 0
for n in numbers:
    total += n
print('total =', total)

### 🔴 Ćwiczenie

# Popraw program M01L13. W tym programie sprawdzaliśmy złożoność tekstów licząc jaka jest średnia długość słów. Na tamtym etapie nie znaliśmy metody jak wyliczyć tą wielkość dokładnie, bez spacji, znaków interpunkcyjnych czy też pomijając liczby w tekście.

# Popraw kod tak, aby nie zliczał spacji ani znaków interpunkcyjnych. Dodatkowo, jeśli w tekście pojawiają się liczby, to również nie bierz ich pod uwagę.

# Napisz testy!