### 🔴 Korzystanie z topical guides w praktyce

### 🔴 Ćwiczenie

# W poprzedniej lekcji napisałæś program z wykorzystaniem biblioteki click. Sam(a) znalazłæś wszystkie potrzebne Ci informacje. Wszystkie znajdowały się w Quickstarcie. Tym razem Twoim zadaniem jest znalezienie dodatkowych informacji, których nie znajdziesz w Quickstarcie. Trzeba będzie przeglądnąć topical guides.

# 1. Przepisz program z M05L07 (word count) tak, aby wykorzystywał bibliotekę click zamiast ręcznego operowania na sys.argv.

# 2. W jaki sposób zaimplementujesz przełącznik --ignore-missing? Znajdź w dokumentacji biblioteki click.

# 3. W jaki sposób sprawisz, że można podać wiele nazw plików (a nie tylko jeden)? Ponownie, znajdź w dokumentacji biblioteki click. Jeśli nie dasz rady zrealizować tej cześci, to zrób tak, żeby Twój program przyjmował jeden plik i wyświetlał dane dla jednego pliku.
import sys
import click


@click.command()
@click.argument('filenames', nargs=-1)
@click.option('--ignore-missing', is_flag=True, help='No error on missing file.')

def print_raport(filenames, ignore_missing):
    """
        Prints number of lines, words and characters for each file in 'filenames' list.
        If 'ignore-missing' is True, then it ignores missing files and continues. Otherwise, it stops the program.
    """

    print(" LINES  WORDS  CHARS  FILENAME")
    for filename in filenames:
        try:
            with open(filename) as stream:
                content = stream.read()
        except FileNotFoundError:
            content = None

        if content is None and not ignore_missing:
            print(f"Missing file: {filename}")
            sys.exit(1)

        if content is None:
            lines_counter = '-'
            words_counter = '-'
            characters_counter = '-'
        else:
            lines = content.split('\n')

            lines_counter = 0
            words_counter = 0
            characters_counter = 0
            for line in lines:
                lines_counter += 1
                words_counter += len(line.split())
                characters_counter += len(line)
        print(f'{lines_counter:>6} {words_counter:>6} {characters_counter:>6} {filename:20}')

if __name__ == "__main__":
    print_raport()