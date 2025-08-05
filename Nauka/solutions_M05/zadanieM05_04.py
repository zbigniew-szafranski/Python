### 🔴 Ćwiczenie

# Usprawnij kod z M04L07 (zliczanie liczby wystąpień poszczególnych słów), tak aby można było ponownie wywołać zawarty tam kod dla dwóch różnych napisów.
# W tym celu opakuj ten kod w dwie funkcje. Pierwsza funkcja jest odpowiedzialna za samo zliczenie słów i stworzenie słownika counter. Druga funkcja powinna wyświetlać raport, mając podany właśnie ten słownik.

PUNCTATIONS = ".,?!"


def counter_words(text):

    text = text.lower()
    for punc in PUNCTATIONS:
        text = text.replace(punc, '')
    words = text.split()

    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    return counter


def print_occurencies(counter):
    print('NUM WORD')
    print("--- ----------")
    for word, occurencies in counter.items():
        print(f'{occurencies:3} {word:}')
    print()


def main():
    first_text = "To jest przykładowy tekst. to to to"
    second_text = "To jest inny tekst. tam to tam"

    print_occurencies(counter_words(first_text))

    print_occurencies(counter_words(second_text))


if __name__ == "__main__":
    main()
