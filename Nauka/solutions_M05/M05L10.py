"""
Usage:
    python M05/M05L10.py <file_name> <search_word>

Print all lines (from the file) that includes given word.
"""
import click

@click.command()
@click.argument('file_name')
@click.argument('search_word')
def main(file_name, search_word):
    try:
        search_word = search_word.lower()
        with open(file_name, 'r') as file:
            for line in file:
                if search_word in line.lower():
                    print(line, end='')  # żeby nie robiło podwójnych enterów
            print()
    except FileNotFoundError:
        print("Missing file.")
        exit(1)

if __name__ == "__main__":
    main()


