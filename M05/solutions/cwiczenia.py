# # . Napisz funkcję abs, która zwraca wartość bezwzględną liczby. To znaczy, że dla liczby ujemnej zwraca tę liczbę bez znaku, czyli dodatnią:
# #
# # abs(5) == 5
# #
# # abs(-3) == 3
# x = 4
#
#
# def print_abs(x):
#     if x < 0:
#         return -x
#     else:
#         return x
#
# def main():
#     x=-4
#     print(abs(x))
#
#
# if __name__ == "__main__":
#         main()
#Masz listę imion:

names = ["Ala", "Bartek", "Ola", "Wojtek", "Ewa"]

#Stwórz nową listę, w której będą tylko imiona dłuższe niż 3 litery, zamienione na duże litery.
list_of_names = []
list_of_names = [name.upper() for name in names if len(name) >3]
print(list_of_names)

# No to lecimy dalej z menu! 🍽️ Tym razem serwuję coś w stylu sałatki, ale z twistem — będzie **słodko-pikantnie** z `zip()` i `enumerate()`. 😎

### 🧁 Mini zadanie à la `zip`

# Masz dwie listy:


names = ["Ala", "Bartek", "Ola"]
ages = [10, 15, 8]

# 🎯 Zrób listę stringów, w których każdy element wygląda tak:

# ```
# "Ala ma 10 lat"
# "Bartek ma 15 lat"
# "Ola ma 8 lat"
# ```

# Wskazówka: użyj **`zip()`** i list comprehension — składniki, które zawsze dobrze się mieszają! 🥣
#
# Jak myślisz, jak połączyć `names` i `ages` w zgrabną pętlę? Zrób próbę, a ja sprawdzę, czy sałatka nie jest za sucha 😄
# list_of_names = list(zip(names, ages))
# added_words = [f"{name} ma {age} lat" for name, age in list_of_names]
# print(added_words)
#
# numbers = list(range(11))
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)

from math import isqrt

numbers = list(range(1,21))
prime_numbers = [
    x for x in numbers
    if x > 1 and all(x % i !=0 for i in range(2, isqrt(x) + 1))
]
print(prime_numbers)
