import logging
import click
from typing import List
import pickle

# Konfiguracja loggera
logging.basicConfig(
    level=logging.INFO,  # pokazuj wszystko od poziomu INFO w górę
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('todos.log'),  # zapisuj do pliku
        logging.StreamHandler()  # pokazuj w konsoli
    ]
)

DB_FILENAME = 'todos.db'

class TodoItem:
    def __init__(self, id: int, description: str, done: bool):
        self.id = id
        self.description = description
        self.done = done
        logging.debug(f'Utworzono nowe zadanie: {self}')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--example', is_flag=True)
def init(example: bool):
    logging.info(f'Inicjalizacja bazy danych (example={example})')
    if example:
        todos = [
            TodoItem(id=1, description='Zadanie pierwsze', done=False),
            TodoItem(id=2, description='Zadanie drugie', done=True),
            TodoItem(id=3, description='Zadanie trzecie', done=False),
        ]
    else:
        todos = []

    try:
        with open(DB_FILENAME, 'wb') as stream:
            pickle.dump(todos, stream)
        logging.info('Baza danych została utworzona pomyślnie')
    except Exception as e:
        logging.error(f'Błąd podczas tworzenia bazy danych: {str(e)}')
        raise

@cli.command()
@click.argument('description')
def add(description: str):
    logging.info(f'Próba dodania nowego zadania: {description}')
    try:
        with open(DB_FILENAME, 'rb') as stream:
            todos = pickle.load(stream)
        
        new_id = max((todo.id for todo in todos), default=0) + 1
        todos.append(TodoItem(id=new_id, description=description, done=False))
        
        with open(DB_FILENAME, 'wb') as stream:
            pickle.dump(todos, stream)
        logging.info(f'Pomyślnie dodano zadanie z ID={new_id}')
    except FileNotFoundError:
        logging.error('Nie znaleziono bazy danych')
        print('Błąd: Najpierw zainicjuj bazę danych')
    except Exception as e:
        logging.error(f'Wystąpił nieoczekiwany błąd: {str(e)}')
        raise

if __name__ == '__main__':
    cli()