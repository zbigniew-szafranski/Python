import sys

filenames = sys.argv[1:]

PUNCTATIONS = ".,?!"
if not filenames:
    print("Missing filename(s)")
    sys.exit(1)

print(" LINES  WORDS  CHARS  FILENAME")
for filename in filenames:
    with open(filename) as stream:
        content = stream.read().strip()
        for punc in PUNCTATIONS:
            content = content.replace(punc, "")
    lines = content.split('\n')
    lines_counter = len(lines)
    words_counter = len(content.split())
    characters_counter = len(content)
    print(f'{lines_counter:6} {words_counter:6} {characters_counter:6} {filename:20}')