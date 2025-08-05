### 🔴 Ćwiczenie

# Popraw program M01L13. W tym programie sprawdzaliśmy złożoność tekstów licząc jaka jest średnia długość słów. Na tamtym etapie nie znaliśmy metody jak wyliczyć tą wielkość dokładnie, bez spacji, znaków interpunkcyjnych czy też pomijając liczby w tekście.

# Popraw kod tak, aby nie zliczał spacji ani znaków interpunkcyjnych. Dodatkowo, jeśli w tekście pojawiają się liczby, to również nie bierz ich pod uwagę.


PUNCTUATIONS_AND_NUMBERS = "!\"#$%&'()*+,-./:;<=>?@[\n]^_`{|}~0123456789"

def clean_text(text):
    """
    Cleans a given text by removing punctuations, numbers, and converting it to lowercase.

    This function iterates through a predefined list of punctuations and numbers, stripping
    them from the input text and replacing them with spaces. The result is returned in
    lowercase format. This can be useful for text normalization in natural language
    processing tasks or text preprocessing pipelines.

    Args:
        text (str): The input string that needs to be cleaned.

    Returns:
        str: The cleaned version of the input text with punctuations removed,
        replaced with spaces, and converted to lowercase.
    """

    cleaned_text = text
    for p in PUNCTUATIONS_AND_NUMBERS:
        cleaned_text = cleaned_text.strip().replace(p, ' ').lower()
    return cleaned_text


def average_word_length(text):
    """
    Calculates the average length of words in a given string of text after
    cleaning it. The function ensures to handle edge cases such as empty text,
    returning zero if there are no words to process.

    Parameters:
    text : str
        A string input representing the text that needs to be analyzed.

    Returns:
    float
        The average word length in the provided text. If the text contains no
        words, the function returns 0.
    """
    cleaned_text = clean_text(text)
    try:
        words = cleaned_text.split()
        total_chars = sum(len(word) for word in words)
        return total_chars / len(words)

    except ZeroDivisionError:
        return 0


def print_average(average_word):
    """
    Prints the average length of words in a text.

    This function takes the average length of words in a given text and displays
    a formatted message that includes this average word length.

    Args:
        average_word: float or int
            The average word length to be displayed.
    """
    print(f"Średnia długość słowa w Twoim tekście wynosi: {average_word} znaków")


def main():
    print_average(average_word_length(clean_text(input("Podaj tekst do analizy: "))))


if __name__ == "__main__":
    main()