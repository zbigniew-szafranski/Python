### 🔴 Ćwiczenie

# Rozwiń program z poprzedniej lekcji tak, aby mógł przyjmować wiele nazw plików. Dla każdego pliku wyświetl ile ma linii, słów i znaków.
import sys

filenames = sys.argv[1:]

PUNCTATIONS = ".,?!"
if not filenames:
    print("Missing filename(s)")
    sys.exit(1)
for filename in filenames:
    with open(filename) as stream:
        content = stream.read().strip()
        for punc in PUNCTATIONS:
            content = content.replace(punc, "")
    lines = content.split('\n')
    lines_counter = len(lines)
    words_counter = len(content.split())
    characters_counter = len(content)
    print(lines_counter, words_counter, characters_counter, filename)
