# W poprzednim ćwiczeniu zmień zachowanie programu tak, że jeżeli baza danych nie istnieje, wówczas zamiast wyświetlać błąd automatycznie stwórz w pamięci nową, pustą bazę.

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


def read_db_or_init()->List[TodoItem]:
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        todos = []
    return todos


def save_db(todos: List[TodoItem], overwrite: bool = True)->None:
    if overwrite:
        mode = 'wb'
    else:
        mode = 'xb'
    with open(DB_FILENAME, mode) as stream:
        pickle.dump(todos, stream)


def print_todos(todos: List[TodoItem])->None:
    print(f'=ID= DONE? ==DESC==')
    for todo in todos:
        if todo.done:
            done = 'x'
        else:
            done = '-'
        print(f'{todo.id:4} {done:5} {todo.description}')


def add_todo(description: str, todos: List[TodoItem])-> None:
    todo = TodoItem(
        id=find_next_id(todos),
        description=description,
        done=False
    )
    todos.append(todo)

@click.group()
def cli():
    pass

@cli.command()
@click.option('--example', is_flag=True)
def init(example: bool):
    todos: List[TodoItem]
    if example:
        todos = [
            TodoItem(id=1, description='Zadanie pierwsze', done=False),
            TodoItem(id=2, description='Zadanie drugie', done=True),
            TodoItem(id=3, description='Zadanie trzecie', done=False),
        ]
    else:
        todos = []

    try:
        save_db(todos, overwrite=False)
    except FileExistsError:
        print("Nie można stworzyć bazy - baza już istnieje!")
    else:
        print("Stworzono")
@cli.command()
def list():
    todos = read_db_or_init()
    print_todos(todos)

@cli.command()
@click.argument('description')
def add(description: str)-> None:
    todos = read_db_or_init()
    add_todo(description, todos)
    save_db(todos)
    print('Dodano')


if __name__ == '__main__':
    cli()