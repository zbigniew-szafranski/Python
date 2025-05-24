# Napisz program, który ułatwi milionom Polaków śledzenie własnych wydatków oraz ich analizę. Program pozwala na łatwe dodawanie nowych wydatków i generowanie raportów. Aplikacja działa także pomiędzy uruchomieniami, przechowując wszystkie dane w pliku. Każdy wydatek ma id, opis oraz wielkość kwoty.

# 1. Program posiada podkomendy add, report, export-python oraz import-csv. 

# 2. Podkomenda add pozwala na dodanie nowego wydatku. Należy wówczas podać jako kolejne argumenty wiersza poleceń wielkość wydatku (jako int) oraz jego opis (w cudzysłowach). Na przykład:
# $ python budget.py add 100 "stówa na zakupy". 
# Jako id wybierz pierwszy wolny id - np. jeśli masz już wydatki z id = 1, 2, 4, 5, wówczas wybierz id = 3.

# 3. Podkomenda report wyświetla wszystkie wydatki w tabeli. W tabeli znajduje się także kolumna "big?", w której znajduje się ptaszek, gdy wydatek jest duży, tzn. co najmniej 1000. Dodatkowo, na samym końcu wyświetlona jest suma wszystkich wydatów.

# 4. Podkomenda export-python wyświetla listę wszystkich wydatków jako obiekt (hint: zaimplementuj poprawnie metodę __repr__ w klasie reprezentującej pojedynczy wydatek).

# 5. Podkomenda import-csv importuję listę wydatków z pliku CSV.

# 6. Program przechowuje pomiędzy uruchomieniami bazę wszystkich wydatków w pliku budget.db. Zapisuj i wczytuj stan używając modułu pickle. Jeżeli plik nie istnieje, to automatycznie stwórz nową, pustą bazę. Zauważ, że nie potrzebujemy podpolecenia init.

# 7. Wielkość wydatku musi być dodatnią liczbą. Gdzie umieścisz kod sprawdzający, czy jest to spełnione? W jaki sposób zgłosisz, że warunek nie jest spełniony?

from dataclasses import dataclass
from typing import List
import pickle

import click


DATABASE_FILE = "budget.db"

@dataclass
class Budget:
    id: int
    description: str
    amount: int
    big: bool = False

    def __post_init__(self):
        if not self.description:
            raise ValueError("Required description")


def find_next_id(budget: List[Budget])->int:
    ids = {b.id for b in budget}
    counter = 1
    while counter in ids:
        counter += 1
    return counter


def read_db_or_init()->List[Budget]:
    try:
        with open(DATABASE_FILE, 'rb') as stream:
            budget = pickle.load(stream)
    except FileNotFoundError:
        budget = []
    return budget


def save_db(budget: List[Budget], overwrite: bool = True)->None:
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'
    with open(DATABASE_FILE, mode) as stream:
        pickle.dump(budget, stream)


def print_budget(budget: List[Budget])-> None:
    print(f'--ID-- -AMOUNT- -BIG- ----DESCRIPTION-----')
    for b in budget:
        if b.amount >= 1000:
            big = "(!)"
        else:
            big = ""
        print(f'{b.id:4} {b.amount:>5} {big} {b.description}')
        print_budget_summary(budget)


def print_budget_summary(budget: List[Budget])-> None:
    total = sum(b.amount for b in budget)
    print(f'{total:>5} {total:>5} {""} {""}')


def add_budget(description: str, amount: int, budget: List[Budget]) ->None:
    if amount < 0:
        raise ValueError("Amount must be positive")
    b = Budget(
        id = find_next_id(budget),
        description=description,
        big=False,
        amount=amount
    )
    budget.append(b)


@click.group()
def cli():
    pass
@cli.command()
@click.argument("amount", type=int)
@click.argument("description")
def add(amount: int, description: str):
    budget = read_db_or_init()
    add_budget(description, amount, budget)
    save_db(budget)
    print(f"Added budget: {amount} {description}")

@cli.command()
def report():
    budget: List[Budget]
    budget = read_db_or_init()
    print_budget(budget)

if __name__ == "__main__":
    cli()