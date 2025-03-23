# Bonusowe minićwiczenia:

# 1. Napisz program, który zlicza ile jest słów w pliku tekstowym.

# 2. Napisz program, który wczytuje z pliku słowa, a następnie zapisuje w innym pliku tylko te słowa, które są samymi wielkimi literami.

# 3. Napisz program, który wczytuje z pliku liczby, a następnie zapisuje w innym pliku tylko te liczby, które są dodatnie.


print("Zadanie 1")
with open('M03/slowa.txt') as stream:
    words = stream.read()
words_split= words.split()
number_words = len(words_split)
# Zadanie 2
has_upper= False
upper = []
file = 'M03/upper.txt'
for word in words_split:
    if word.isupper():
        has_upper = True
        if has_upper:
            upper.append(word)
if upper:
    with open(file, "w") as writer:
        writer.write('\n'.join(upper))
    result = f"Zapisano do pliku: {file}"
else:
    result = "W plku nie ma słów z dużymi literami"
print(result)      
print("Słów w pliku jest:",number_words)

# Zadanie 3
with open('M03/numbers.txt') as stream:
    numbers = stream.read()
content = numbers.split()
numbers = []
for number in content:
    if number.isalnum():
        numbers.append(int(number))
string_numbers = []
for number in numbers:
    string_numbers.append(str(number))
# print(string_numbers)
with open('M03/dodatnie.txt', 'w') as writer:
    writer.write(str(string_numbers))

