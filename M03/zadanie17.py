## 🔴 Ćwiczenie
# Wczytaj listę komentarzy z pliku comments.txt. Każdy komentarz to osobna linia. Zapisz komentarze w zmiennej, pod którą kryje się lista list. Każdy komentarz reprezentuj jako listę słów, a nie jako string.
# Następnie pozwól użytkownikowi wprowadzić słowo i wyświetl w ilu komentarzach pojawia się to słowo?
# Wielkość liter nie powinna mieć znaczenia.
# Pozbądź się znaków interpunkcji.
INPUT_FILE = "M03/comments.txt"
PUNCTUATIONS = "$%^&*()_+=-,.:;?!"
comments_list = []
count = 0

with open(INPUT_FILE) as stream:
    comments = stream.read()
    for word in comments.split("\n"):
        for symbol in PUNCTUATIONS:
            line = word.replace(symbol, '')
            words = line.split()
        comments_list.append(words)
word = input("Podaj słwo: ")
word_lower = word.lower()
for comment in comments_list:
    if word_lower in comment:
        count +=1
print(f"Słowo '{word}' pojawiło się w {count} komentarzach")