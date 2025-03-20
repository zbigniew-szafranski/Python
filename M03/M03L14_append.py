### 🔴 Budowanie listy od zera z .append()

text = 'Lorem ipsum przykładowy tekst'
words = text.split()
print('words =', words)

# Jak dostać listę [5, 5, 11, 5] czyli długości słów?

lengths = [len(words[0]), len(words[1]), len(words[2]), len(words[3])]
print('lengths =', lengths)

# Potrzebujemy metody .append()

my_list = [5, 10]
print('my_list =', my_list)
my_list.append(7)
print('my_list =', my_list)
my_list.append(3)
print('my_list =', my_list)

# Bardzo często spotykany idiom:
lengths = []
for word in words:
    word_length = len(word)
    lengths.append(word_length)
print('lengths =', lengths)

### 🔴 Ćwiczenie

# Popraw kod z M03L09 tak, aby wczytać wydatki do listy, a następnie wylicz sumę i średnią wydatków, a także jakiej kwoty był najmniejszy i największy wydatek. Użyj wbudowanych funkcji sum, min oraz max.