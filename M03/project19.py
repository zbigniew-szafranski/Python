# Pomóż zespołowi Stanford AI Lab przeanalizować zbiór danych składający się z 50 tys. recenzji filmów, dzięki czemu będą mogli automatycznie określać sentyment nowych komentarzy i wypowiedzi w internecie. W szczególności zależy im, aby zidentyfikować te najbardziej pozytywne i negatywne wypowiedzi wśród milionów neutralnych komentarzy - dzięki temu będą mogli udostępnić te najbardziej pozytywne, a w przypadku tych najbardziej negatywnych będą mogli zareagować i odpowiedzieć zanim taki komentarz dotrze do szerszego grona.
#
# 1. Wszystkie pliki znajdują się w katalogu M03/data/aclImdb/train. W podkatalogu "pos" znajdują się pozytywne komentarze, tzn. minimum 7/10. W podkatalogu "neg" znajdują się negatywne komentarze, czyli te 6/10, 5/10 i niżej. Każda recenzja to osobny plik.
# 2. W recenzjach znajdują się fragmenty HTML - "<br />" oznaczający znak końca linii. Takie fragmenty zastąp spacją.
# 3. Wczytaj wszystkie pozytywne i negatywne recenzje do dwóch osobnych zmiennych. Będzie łatwiej, jeśli każdą recenzję będziesz reprezentować nie jako string, tylko jako listę słów. Tak więc każda z tych dwóch osobnych zmiennych będzie listą list.
# 4. Następnie poproś użytkownika, aby wpisał komentarz, którego sentyment chce wyliczyć. Podziel ten komentarz na słowa.
# # 5. Sentyment poszczególnych słów w tym komentarzu liczymy wg wzoru (positive-negative)/all_, gdzie positive to liczba pozytywnych recenzji, w których pojawiło się to słowo. Negative to liczba negatywnych recenzji, w których pojawiło się to słowo. Natomiast all_ to liczba wszystkich recenzji, w których pojawiło się to słowo. Na przykład, jeśli dane słowo pojawia się w 5 pozytywnych i 5 negatywnych recenzjach, to jego sentyment wynosi (5-5)/10 = 0.0. Jeśli dane słowo pojawia się w 9 pozytywnych i 1 negatywnej recenzji, to jego sentyment wynosi (9-1)/10 = +0.8. Jeśli dane słowo pojawia się w 90 pozytywnych i 10 negatywnych recenzjach, to jego sentyment wynosi (90-10)/100 = +0.8, tak samo jak wcześniej. Tak więc liczba zawsze jest z zakresu od -1.0 do +1.0.
# # 6. Sentyment całego tego komentarza to średnia arytmetyczna sentymentu wszystkich słów. Tak więc wystarczy zsumować sentyment poszczególnych słów i następnie taką sumę podzielić przez liczbę słów. W ten sposób sentyment całego komentarza też będzie z zakresu od -1.0 do +1.0.
# # 7. Cały komentarz uznajemy za pozytywny, gdy jego sentyment jest > 0, a negatywny gdy jest < 0.
import os
LINE = str= '-'
lists_of_path_negative = []
lists_of_path_positive =[]
negative = []
positive = []
REMOVE_BR = "<br"
PUNCTATIONS =".>/,()-?!"
NEGATIVE_COMMENTS_PATH = 'M03/data/aclImdb/train/neg'
POSITIVE_COMMENTS_PATH = 'M03/data/aclImdb/train/pos'
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
        words_neg = lines.split()
        negative.append(words_neg)

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
        words_pos= lines.split()
        positive.append(words_pos)
user_comments = input("Write a comment, please: ").lower()
for punc in PUNCTATIONS:
    user_comments= user_comments.replace(punc, '')
user_comments = user_comments.replace(REMOVE_BR, '')
user_comments = user_comments.split()

total_sentiment = 0
for word in user_comments:
    negative_count = 0
    positive_count = 0
    comments_all = positive_count + negative_count
    for comments in positive:
        if word in comments:
            positive_count+=1
    for comments in negative:
        if word in comments:
            negative_count+=1
    comments_all = positive_count + negative_count
    if comments_all ==0:
        sentiment = 0.0
        print("Słowo nie występuje w recenzji", "sentyment: ", sentiment)
    else:
        sentiment = (positive_count-negative_count)/comments_all
        print(f"Słowo '{word}' ma sentyment: {sentiment}")
        total_sentiment+=sentiment
for r in range(10):
    print(LINE, end="")
print()
sentiment_all = 0
if len(user_comments)>0:
    sentiment_all = total_sentiment / len(user_comments)
    sentiment_pos = "pozytywny"
else:
    sentiment_all = 0
    print("brak komentarza")
if sentiment_all > 0:
    sentiment_result = "pozytywny"
else:
    sentiment_result = "negatywny"
print(f"Sentyment recenzji jest - {sentiment_result} i wynosi {sentiment_all}")