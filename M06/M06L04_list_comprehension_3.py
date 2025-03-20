### 🔴 Znowu wyrażenia listowe?!

# Wiesz już, że wyrażenia listowe mogą przybierać jedną z dwóch form:
#   [_ for _ in _]
# lub:
#   [_ for _ in _ if _]

# Okazuje się jednak, że wyrażenia listowe pozwalają na zastąpienie nawet dwóch lub więcej zagnieżdżonych pętli for, dzięki czemu możesz iterować po zagnieżdżonych listach!

# Weźmy poniższy problem - chcemy zsumować te liczby:

matrix = [
    [1, 5, 3],
    [4, 9, 10],
    [9, 7, 5],
]

# print(sum(matrix))  # ❌ nie zadziała

# Niestety, powyższy kod nie działa, bo funkcja sum zakłada, że ma doczynienia z PŁASKĄ listą, tzn. po prostu listą liczb. Tymczasem my mamy zagnieżdżone listy.

# Jak możemy stworzyć płaską listę? Na przykład tak jak poniżej:

flat = []
for row in matrix:
    for elem in row:
        flat.append(elem)
print('flat =', flat)
print(sum(flat))

# Ale można szybciej, używając wyrażeń listowych:

flat = [elem for row in matrix for elem in row]
print(sum(flat))

### 🔴 Ćwiczenie

# Masz listę komentarzy. Każdy komentarz reprezentujesz jako listę słów.

# Zbuduj listę zawierającą wszystkie słowa ze wszystkich recenzji. Chodzi o płaską, tzn. niepozagnieżdżaną listę. Taka lista może być później używana dalej.

# Napisz testy!

comments = [
    ['pierwszy', 'komentarz'],
    ['drugi', 'komentarz'],
]