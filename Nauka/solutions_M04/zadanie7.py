### 🔴 Ćwiczenie
#[zadanie]
# 1. Mając podany tekst zlicz poszczególne słowa.
# 2. Wyświetl w tabeli ile razy występuje każde ze słów.
# 3. Nie zwracaj uwagi na wielkość liter w słowach, to znaczy "A" oraz "a" to jest to samo słowo.
# 4. W jaki jeszcze sposób przetworzył(a)byś tekst zanim podzielisz go na słowa?
#[rozwiązanie]
import sys
import re
# Oczyszczamy zawartość tekstu z niepożądanych znaków przy użyciu re.sub
cleaned_input = re.sub(r'[^a-zA-Z0-9 ]', '', ' '.join(sys.argv[1:])).lower()
words = cleaned_input.split()
words_counter = {}
# dzielenie słów i zliczanie
for word in words:
    if not word:
        continue
    words_counter[word] = words_counter.get(word, 0) + 1
print('NUM WORD')
for word, count in words_counter.items():
    print(f'{count:3} {word:12}')