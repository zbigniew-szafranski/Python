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

def find_next_id(todos: List[TodoItem])->int:
    ids = {todo.id for todo in todos}
    counter = 1
    while counter in ids:
        counter += 1
    return counter

@click.command()
@click.argument('description')
def main(description: str)-> None:
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
    except FileNotFoundError:
        print("Brak bazy danych - najpierw  zainicjalizuj baze programem init")
        sys.exit(1)

    todo = TodoItem(
        id=find_next_id(todos),
        description=description,
        done=False
    )
    todos.append(todo)

    with open(DB_FILENAME, 'wb') as stream:
        pickle.dump(todos, stream)

if __name__ == '__main__':
    main()