### 🔴 Ćwiczenie

# Usprawnij kod z ćwiczenia M05L03. Zrób tak, aby inne skrypty mogły zaimportować Twój program i skorzystać z jego funkcjonalności - dokładnie tak jak w M05/M05L05_dodatek.py.

# Dzięki temu gdy ktoś będzie chciał ponownie użyć Twojego programu, może go nie tylko uruchomić w terminalu, ale może także go zaimportować i wywołać nową funkcję print_raport(filenames, ignore_missing).

# Nazwy plików (filenames) oraz przełącznik (ignore_missing) powinny być w tej funkcji przekazane jako parametry. Przy czym drugi parametr powinien być opcjonalny. Jaką wybierzesz domyślną wartość?

# W osobnej funkcji main() wywołaj funkcję print_raport przekazując wartości dla tych dwóch parametrów z sys.argv.
""" Aplication to display file content.
You can specify filenames to display their content in terminal.
if import this module, you can use function print_raport(filenames, ignore_missing).
"""

import sys


def print_raport(filenames, ignore_missing = False):
    """
    Prints a report describing the number of lines, words, and characters in each file listed in filenames.

    The function iterates over a list of filenames, reads the content of each file, and calculates the respective
    counts of lines, words, and characters. If a file is missing, behavior depends on the 'ignore_missing' parameter:
    it either skips the missing file with a warning or exits the program with an error.

    Parameters
    ----------
    filenames: list of str
        A list containing the names of the files to process.
    ignore_missing: bool, optional
        If True, missing files are ignored with exit. If False, missing files result in an error message only.

    Returns
    -------
    None
    """

    print(" LINES  WORDS  CHARS  FILENAME")
    for filename in filenames:
        try:
            with open(filename) as stream:
                content = stream.read()
        except FileNotFoundError:
            content = None
        if content is not None and ignore_missing:
            print(f"Missing file: {filename}")
            sys.exit(1)

        if content is None:
            lines_counter = '-'
            words_counter = '-'
            characters_counter = '-'
        else:
            lines = content.split('\n')
            lines_counter = len(lines)
            words_counter = len(content.split())
            characters_counter = len(content)

        print(f'{lines_counter:>6} {words_counter:>6} {characters_counter:>6} {filename:20}')

def main():
    filenames = sys.argv[1:]

    if not filenames:
        print("Missing filename(s).")
        sys.exit(1)

    ignore_missing = '--ignore-missing' in filenames
    if ignore_missing:
        filenames.remove('--ignore-missing')

    print_raport(sys.argv[1:])

if __name__ == "__main__":
    main()