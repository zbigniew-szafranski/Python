# Napisz program, który będzie bazował na pliku todos.db stworzonym w poprzednim ćwiczeniu.
# Załaduj plik do pamięci i wyświetl wszystkie zadania w formie tabeli.

import pickle
import sys

import click

DB_FILENAME = 'todos.db'

class TodoItem:
    def __init__(self, id: int, description: str, done: bool):
        self.id = id
        self.description = description
        self.done = done
    def __repr__(self):
        return f'TodoItem(id={self.id}, description={self.description}, done={self.done})'
    def __eq__(self, other):
        return self.id == other.id and self.description == other.description and self.done == other.done

@click.command()
def main():
    try:
        with open(DB_FILENAME, 'rb') as strean:
            todos = pickle.load(strean)
    except FileExistsError:
        print('Brak bazy danych - najpierw zainicjuj bazę programem init')
        sys.exit(1)
    print(f'=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:5} {todo.description}')

if __name__ == '__main__':
    main()