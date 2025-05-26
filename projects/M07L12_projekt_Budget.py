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
from typing import List, Dict
import pickle
import sys
import csv

import click

DATABASE_FILE = "budget.db"

@dataclass
class Expenses:
    id: int
    description: str
    amount: int
    big: bool = False

    def __repr__(self):
        return (f"Expenses("
                f"id={self.id},"
                f"description={self.description!r},"
                f"amount={self.amount},"
                f"big={self.big})"
                )

    def __post_init__(self):
        if not self.description or self.description.strip() == "":
            raise ValueError("Required description")

        self.amount = int(self.amount)
        if self.amount <= 0:
            print(self.amount)
            raise ValueError("Amount must be positive")


def find_next_id(expense: List[Expenses])->int:
    ids = {e.id for e in expense}
    counter = 1
    while counter in ids:
        counter += 1
    return counter


def read_db_or_init()->List[Expenses]:
    try:
        with open(DATABASE_FILE, 'rb') as stream:
            expense = pickle.load(stream)
    except FileNotFoundError:
        expense = []
    return expense


def save_db(expense: List[Expenses], overwrite: bool = True)->None:
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'
    with open(DATABASE_FILE, mode) as stream:
        pickle.dump(expense, stream)


def print_expenses(expense: List[Expenses])-> None:
    print(f'--ID-- -AMOUNT- -BIG- ----DESCRIPTION-----')
    for e in expense:
        if e.amount >= 1000:
            big = "(!)"
        else:
            big = ""
        print(f'{e.id:4} {e.amount:>8} {big:^10} {e.description}')
    print_expense_summary(expense)


def print_expense_summary(expense: List[Expenses])-> None:
    total = sum(e.amount for e in expense)
    print(f'TOTAL: {total:>5} {""} {""}')


def add_expense(description: str, amount: int, expense: List[Expenses]) ->None:

    b = Expenses(
        id = find_next_id(expense),
        description=description,
        big=False,
        amount=amount
    )
    expense.append(b)


def export_expense_as_python(expense: List[Expenses]) -> None:
    for e in expense:
        print(e)


def import_expenses_from_csv(filename: str) -> List[Expenses]:
    with open(filename) as stream:
        expenses = []
        reader = csv.DictReader(stream)
        for row in reader:
            expense = create_expense_from_dict(row, expenses)
            expenses.append(expense)
    return expenses

def create_expense_from_dict(row: Dict[str, str], expense: List[Expenses]) -> Expenses:
    return Expenses(
        id=find_next_id(expense),
        description=row['description'],
        amount=int(float(row['amount'])),
        big= False
    )


def assign_ids_and_merge_expenses(current_expense: List[Expenses], new_expenses: List[Expenses]) -> None:
    """Assigns unique IDs to new expenses and adds them to the existing budget.

    Args:
        current_expense: List of current expenses
        new_expenses: List of new expenses to be added
    """
    for expense in new_expenses:
        expense.id = find_next_id(current_expense)
        current_expense.append(expense)

@click.group()
def cli():
    pass

@cli.command()
def report():
    """Print report of all expenses."""
    expense: List[Expenses]
    expense = read_db_or_init()
    print_expenses(expense)

@cli.command()
@click.argument("amount", type=int)
@click.argument("description", required=True)
def add(amount: int, description: str):
    """Add new expense to expense.

    AMOUNT must be positive.

    DESCRIPTION is required with non-empty string""
    """

    expense = read_db_or_init()
    try:
        add_expense(description, amount, expense)
    except ValueError as e:
        print(">>>", e, "<<<")
        sys.exit(1)

    save_db(expense)
    print(f"Added expense: {amount} {description}")

@cli.command("import-csv")
@click.argument("import-csv")
def import_expenses_from_csv_file(import_csv: str):
    """Import expenses from CSV file to database in budget.db"""
    current_expense: List[Expenses] = read_db_or_init()
    imported_expenses: List[Expenses] = import_expenses_from_csv(import_csv)

    assign_ids_and_merge_expenses(current_expense, imported_expenses)

    save_db(current_expense)
    print(f"Imported {len(imported_expenses)} expenses from {import_csv}")

@cli.command("export-python")
def export_expense_as_python_file():
    """Export expense as Python code"""
    expense: List[Expenses] = read_db_or_init()
    print(expense)

if __name__ == "__main__":
    cli()