### 🔴 Podpolecenia z click

# W poprzednich trzech lekcjach napisałæś trzy programy pozwalające na zarządzanie listą zadań. Wszystkie trzy sporo łączy.
# Najczęściej takie skrypty łączy się w jeden, rozróżniając między nimi dzięki podpoleceniu:

# $ python todos.py init --example
# $ python todos.py list
# $ python todos.py add "Nowe zadanie"

# Biblioteka click pozwala na automatyczne rozróżnianie między różnymi podpoleceniami, tak aby na końcu została wywołana odpowiednia funkcja. W tym celu tworzymy grupę:

import click

@click.group()
def cli():
    pass  # Instrukcja pass nie robi nic, ale jest konieczna, ponieważ każdy blok kodu musi mieć conajmniej jedną instrukcję, inaczej mamy SyntaxError

# A następnie rejestrujemy kilka funkcji w tej grupie:

@cli.command()  # `cli` zamiast `click`!
def happy():
    print(':-)')
    
@cli.command()
def sad():
    print(':-(')

@cli.command()
@click.argument('msg')  # A tutaj już normalnie `click` zamiast `cli`
def custom(msg):
    print(f':-| {msg}')

if __name__ == "__main__":
    cli()

# Teraz ten program możemy wywołać na kilka sposobów:

# $ python M07/M07L08_subcommands.py happy
# $ python M07/M07L08_subcommands.py sad
# $ python M07/M07L08_subcommands.py custom "Custom text"

### 🔴 Ćwiczenie

# W poprzednich ćwiczeniach napisałæś trzy programy do zarządzania listą zadań umieszczoną w pliku todos.db. Połącz te trzy programy w jeden skrypt, tak aby miał podpolecenia init, list i add.
# Jak podzielisz cały kod na funkcje? Co będzie robiła każda z funkcji?
# Napisz testy! Które funkcje przetestujesz?