### 🔴 Ćwiczenie

# W projekcie M03L19 analizowaliśmy sentyment 25 tys. recenzji filmowych. Wymagało to m.in. zliczenia w ilu recenzjach pojawiają się poszczególne słowa. W pierwotnym rozwiązaniu prosiliśmy użytkownika o nową recenzję, dzieliliśmy ją na słowa, a następnie dla każdego słowa przechodziliśmy przez wszystkie recenzje, aby zliczyć ile razy to słowo pojawia się w negatywnych, a ile razy w pozytywnych komentarzach.
# Nie jest to najefektywniejszy sposób. W tym ćwiczeniu poprawisz kod z tamtego projektu tak, aby na etapie wczytywania plików zliczył liczbę wystąpień poszczególnych słów, zapamiętał rezultat w dwóch osobnych słownikach (jeden dla pozytywnych recenzji, jeden dla negatywnych). Następnie poproś użytkownika o nową recenzję i wylicz jej sentyment korzystając już tylko z tych dwóch słowników.
# Zwróć uwagę, że nawet jeśli jakieś słowo pojawia się w recenzji dwa razy, wówczas jego licznik chcemy zwiększyć tylko o jeden. W końcu interesuje nas liczba recenzji zawierających dane słowo, a nie ile razy to słowo pojawia się we wszystkich recenzjach. Potrzebujemy więc w ramach pojedynczej recenzji pozbyć się powtórzeń tych samych słów.

# Dzięki tym modyfikacjom program wykorzystuje mniej pamięci, bo nie musi zapamiętywać wszystkich recenzji w pamięci, a jedynie liczbę wystąpień słów.
# Po drugie, program będzie dużo szybciej wyliczał sentyment nowych recenzji. W wielu zastosowaniach Machine Learning kluczowe jest, aby czas predykcji (czyli czas wyliczania sentymentu dla nowej recenzji) był wystarczająco krótki.

import os
LINE = str= '-'
lists_of_path_negative = []
lists_of_path_positive =[]
words_count_pos = {}
words_count_neg = {}
REMOVE_BR = "<br"
PUNCTATIONS =".>/,()-?!"
NEGATIVE_COMMENTS_PATH = 'M03/data/aclImdb/train/neg'
POSITIVE_COMMENTS_PATH = 'M03/data/aclImdb/train/pos'
# Load and parse negative reviews in order to count occurencies
with os.scandir(NEGATIVE_COMMENTS_PATH) as entries:
    for entry in entries:
        files = entry.path
        lists_of_path_negative.append(files)

for path in lists_of_path_negative:
    with open(path) as stream:
        lines = stream.read().strip().lower()
        for punc in PUNCTATIONS:
            lines = lines.replace(punc, '')
        for punc in REMOVE_BR:
            lines = lines.replace(punc, '')
        words = lines.split()
        for word in set(words):
            words_count_neg[word] = words_count_neg.get(word, 0) + 1

# Load and parse positivies reviews in order to count occurencies
with os.scandir(POSITIVE_COMMENTS_PATH) as entries:
    for entry in entries:
        files = entry.path
        lists_of_path_positive.append(files)

for path in lists_of_path_positive:
    with open(path) as stream:
        lines = stream.read().strip().lower()
        for punc in PUNCTATIONS:
            lines = lines.replace(punc, '')
        lines = lines.replace(REMOVE_BR, '')
        words= lines.split()
        for word in set(words):
            words_count_pos[word] = words_count_pos.get(word, 0) + 1
# Get sentence sentiment
sentence = input("Write a comment, ONLY English please: ").lower()
for punc in PUNCTATIONS:
    words= sentence.replace(punc, '')
words = sentence.replace(REMOVE_BR, '').split()

# Compute sentence sentiment
sentence_sentiment = 0
for word in words:
    positive = words_count_pos.get(word, 0)
    negative = words_count_neg.get(word, 0)
    comments_all = positive + negative

    if comments_all ==0:
        word_sentiment = 0.0
        print("Słowo nie występuje w recenzji", "sentyment: ", word_sentiment)
    else:
        word_sentiment = (positive-negative)/comments_all
        print(f"Słowo '{word}' ma sentyment: {word_sentiment}")
        sentence_sentiment+=word_sentiment
for r in range(10):
    print(LINE, end="")
print()
sentence_sentiment /=len(words)
# Raport
sentiment_all = 0
if sentence_sentiment > 0:
    label = "pozytywny"
else:
    sentiment_all = 0
    print("brak komentarza")
if sentence_sentiment > 0:
    label = "pozytywny"
else:
    label = "negatywny"
print(f"Sentyment recenzji jest - {label} i wynosi {sentiment_all}")