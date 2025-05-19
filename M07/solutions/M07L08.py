# W poprzednich ćwiczeniach napisałæś trzy programy do zarządzania listą zadań umieszczoną w pliku todos.db. Połącz te trzy programy w jeden skrypt, tak aby miał podpolecenia init, list i add.
# Jak podzielisz cały kod na funkcje? Co będzie robiła każda z funkcji?
# Napisz testy! Które funkcje przetestujesz?

from typing import List
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
    def __str__(self):
        return f'{self.id:<4} | {self.description:<30} | {str(self.done):<5}'

def find_next_id(todos: List[TodoItem])->int:
    ids = {todo.id for todo in todos}
    counter = 1
    while counter in ids:
        counter += 1
    return counter

@click.group()
def cli():
    pass

@cli.command(name='init')
@click.option('--example', is_flag=True)
def init(example: bool):
    if example:
        todos = [
            TodoItem(id=1, description='Zadanie pierwsze', done=False),
            TodoItem(id=2, description='Zadanie drugie', done=True),
            TodoItem(id=3, description='Zadanie trzecie', done=False),
        ]
    else:
        todos = []

    try:
        with open(DB_FILENAME, 'xb') as stream:
            pickle.dump(todos, stream)
    except FileExistsError:
        print("Nie można stworzyć bazy - baza już istnieje!")
    else:
        print("Stworzono")
@cli.command(name='list')
def list_todos():
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        print('Brak bazy danych - najpierw zainicjuj bazę programem init')
        sys.exit(1)
    print(f'=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:5} {todo.description}')

@cli.command(name='add')
@click.argument('description')
def add_todo(description: str)-> None:
        try:
            with open(DB_FILENAME, 'rb') as stream:
                todos = pickle.load(stream)
        except FileNotFoundError:
            print("Brak bazy danych - najpierw zainicjalizuj bazę programem init")
            sys.exit(1)

        todo = TodoItem(
            id=find_next_id(todos),
            description=description,
            done=False
        )
        todos.append(todo)

        with open(DB_FILENAME, 'wb') as stream:
            pickle.dump(todos, stream)

def main():
    cli()

if __name__ == '__main__':
    main()