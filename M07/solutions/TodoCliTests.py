from click.testing import CliRunner
import pytest
from M07L08 import cli, TodoItem
import os
import pickle

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def cleanup():
    # Wykonuje się przed każdym testem
    if os.path.exists('todos.db'):
        os.remove('todos.db')
    yield
    # Wykonuje się po każdym teście
    if os.path.exists('todos.db'):
        os.remove('todos.db')

def test_init_command(runner, cleanup):
    result = runner.invoke(cli, ['init'])
    assert result.exit_code == 0
    assert "Stworzono" in result.output

def test_init_with_example_data(runner, cleanup):
    result = runner.invoke(cli, ['init', '--example'])
    assert result.exit_code == 0
    assert "Stworzono" in result.output
    
    # Sprawdzamy czy przykładowe dane zostały rzeczywiście zapisane
    with open('todos.db', 'rb') as f:
        todos = pickle.load(f)
    assert len(todos) == 3
    assert todos[0].description == 'Zadanie pierwsze'

def test_list_without_db(runner, cleanup):
    result = runner.invoke(cli, ['list'])
    assert result.exit_code == 1
    assert "Brak bazy danych" in result.output

def test_add_todo(runner, cleanup):
    # Najpierw inicjalizujemy pustą bazę
    runner.invoke(cli, ['init'])
    
    # Dodajemy nowe zadanie
    result = runner.invoke(cli, ['add', 'Nowe zadanie testowe'])
    assert result.exit_code == 0
    
    # Sprawdzamy czy jest na liście
    list_result = runner.invoke(cli, ['list'])
    assert 'Nowe zadanie testowe' in list_result.output