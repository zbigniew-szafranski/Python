## 🔴 Ćwiczenie
# Wczytaj listę komentarzy z pliku comments.txt. Każdy komentarz to osobna linia. Zapisz komentarze w zmiennej, pod którą kryje się lista list. Każdy komentarz reprezentuj jako listę słów, a nie jako string.
# Następnie pozwól użytkownikowi wprowadzić słowo i wyświetl w ilu komentarzach pojawia się to słowo?
# Wielkość liter nie powinna mieć znaczenia.
# Pozbądź się znaków interpunkcji.
from typing import List

INPUT_FILE = "M03/comments.txt"
PUNCTUATIONS = "$%^&*()_+=-,.:;?!"
comments_list = []
word_list = []

with open(INPUT_FILE) as stream:
    content = stream.read()
lines = content.split('\n')
for line in lines:
    line = line.lower()
    for punc in PUNCTUATIONS:
        line = line.replace(punc, '')
    words: List[str] = line.split()
    comments_list.append(words)
answer = input("Podaj słwo: ").lower()
answer = answer.lower().split()

count = 0
for comment in comments_list:
    found = False
    for word in answer:
        if word in comment:
            found = True
    count+= found

# print(f"{count} komentarze zawiera przynajmniej jedno ze słów: '{answer}'")
print(count, 'komentarzy zawiera przynajmniej jedno ze słów: ', end=' ')
for word in answer:
    print(word, end=' ')
print()