### 🔴 Projekt

# Napisz dla BBC program sprawdzający złożoność artykułów i wpisów, dzięki czemu pracę dziennikarzy będzie można sparametryzować i automatycznie ustalić, czy piszą teksty proste i łatwe w zrozumieniu. Policz jaka jest średnia długość słów i wyświetl rezultat.

# Podpowiedzi:

import string

text = str(input("Podaj tekst do analizy: "))
text_no_space = text.translate(str.maketrans("", "", string.punctuation + " "))

char = len(text_no_space)
words = len(text.split())  # liczba słów

a = char
b = words
average_words_count = char / words
print(f"Średnia długość słowa w Twoim tekście wynosi: {average_words_count} znaków")

# Aby policzyć średnią długość słowa, możesz bazować na liczbie wszystkich znaków oraz liczbie słów.