### 🔴 Ćwiczenie

# Popraw program M01L13. W tym programie sprawdzaliśmy złożoność tekstów licząc jaka jest średnia długość słów. Na tamtym etapie nie znaliśmy metody jak wyliczyć tą wielkość dokładnie, bez spacji, znaków interpunkcyjnych czy też pomijając liczby w tekście.

# Popraw kod tak, aby nie zliczał spacji ani znaków interpunkcyjnych. Dodatkowo, jeśli w tekście pojawiają się liczby, to również nie bierz ich pod uwagę.

# Rozwiązanie jakie sugeruje PP

PUNCTUATIONS = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def remove_punctuation(text):
    for punc in PUNCTUATIONS:
        text = text.replace(punc, '')
    return text

def calculate_word_length(text):
    words = remove_punctuation(text).split()
    words_without_numb = [w for w in words if not w.isnumeric()]
    lengths = [len(w) for w in words_without_numb]
    average = sum(lengths) / len(lengths)
    return average

def main():
    text = input("Podaj tekst do analizy: ")
    average = calculate_word_length(text)
    print(f"Średnia długość słowa wynosi:{average:.2f}")

if __name__ == "__main__":
    main()