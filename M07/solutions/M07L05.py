import pickle

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

@click.command()
@click.option('--example', is_flag=True)
def main(example: bool):
    if example:
        todos = [
            TodoItem(id=1, description='Zadanie pierwsze', done=False),
            TodoItem(id=2, description='Zadanie drugie', done=True),
            TodoItem(id=3, description='Zadanie trzecie', done=False),
        ]
    else:
        todos = []

    try:
        with open(DB_FILENAME, 'xb') as strean:
            pickle.dump(todos, strean)
    except FileExistsError:
        print("Nie można stworzyć bazy - baza już istnieje!")
    else:
        print("Stworzono")

if __name__ == '__main__':
    main()