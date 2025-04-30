### 🔴 Ćwiczenie

# Popraw program M01L13. W tym programie sprawdzaliśmy złożoność tekstów licząc jaka jest średnia długość słów. Na tamtym etapie nie znaliśmy metody jak wyliczyć tą wielkość dokładnie, bez spacji, znaków interpunkcyjnych czy też pomijając liczby w tekście.

# Popraw kod tak, aby nie zliczał spacji ani znaków interpunkcyjnych. Dodatkowo, jeśli w tekście pojawiają się liczby, to również nie bierz ich pod uwagę.


PUNCTUATIONS_AND_NUMBERS = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"

def clean_text(text):
    cleaned_text = text
    for p in PUNCTUATIONS_AND_NUMBERS:
        cleaned_text = cleaned_text.replace(p, '')
    return cleaned_text

def average_word_length(cleaned_text):
    try:
        words = cleaned_text.split()
        total_chars = sum(len(word) for word in words)
        return total_chars / len(words)

    except ZeroDivisionError:
        return 0

def print_average(average_word):
    print(f"Średnia długość słowa w Twoim tekście wynosi: {average_word} znaków")


def main():
    print_average(average_word_length(clean_text(input("Podaj tekst do analizy: "))))
if __name__ == "__main__":
    main()