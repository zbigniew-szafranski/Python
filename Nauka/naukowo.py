# Napisz program, który ocenia jak bardzo "naukowo" brzmi dany tekst. W tym celu policz jak często w tym zdaniu pojawiają się liczby. Wyświetl jaki procent wszystkich "słów" to właśnie liczby.
# Postaraj się, aby program nie zwracał uwagi na interpunkcję. To znaczy, że w zdaniu "Numer 1234." drugie słowo to "1234.". Potraktuj je jako liczbę, pomimo że zawiera kropkę.
# To oznacza, że zdefiniujesz stałą zawierającą kilka znaków interpunkcyjnych.
# Samodzielnie znajdź metodę do określania, czy dany string jest liczbą.

content = input('Podaj tekst: ')
PUNCTUATION_CHARACTERS = '!@#$&*()_+?!:;,.-% \n'
numbers_digit = 0
numbers_word = 0
for word in content.split():
    for symbol in PUNCTUATION_CHARACTERS:
        word = word.replace(symbol, '')
    if word.isnumeric():
        numbers_digit += 1
    if word.isalpha() or word.isalnum():
        numbers_word += 1
print(numbers_word)
print(numbers_digit)
print(f'{numbers_digit / numbers_word*100}%')