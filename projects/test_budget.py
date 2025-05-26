import pytest
from M07L12_projekt_Budget import find_next_id, Expenses, print_expenses

def test_empty():
    expense = []
    result = find_next_id(expense)
    assert result == 1


def test_one_task():
    expense = [Expenses(id=1, description='abc', amount=1, big=False)]
    result = find_next_id(expense)
    assert result == 2


def test_two_tasks():
    expense = [Expenses(id=1, description='abc', amount=1, big=False),
               Expenses(id=2, description='abc', amount=2, big=False)
               ]
    result = find_next_id(expense)
    assert result == 3


def test_between_id():
    expense = [Expenses(id=1, description='abc', amount=1, big=False),
               Expenses(id= 3, description='abc', amount=3, big=False),
               Expenses(id=4, description='abc', amount=2, big=False)
               ]
    result = find_next_id(expense)
    assert result == 2


def test_with_multiple_gaps():
    expense = [
        Expenses(id=1, description='abc', amount=1, big=False),
        Expenses(id=2, description='def', amount=2, big=False),
        Expenses(id=5, description='ghi', amount=3, big=False),
        Expenses(id=7, description='jkl', amount=4, big=False),
        Expenses(id=8, description='mno', amount=5, big=False)
    ]
    result = find_next_id(expense)
    assert result == 3


def test_empty_description():
    with pytest.raises(ValueError):
        Expenses(id=1, description='', amount=100, big=False)


def test_whitespace_description():
    with pytest.raises(ValueError):
        Expenses(id=1, description='   ', amount=100, big=False)


def test_negative_amount():
    with pytest.raises(ValueError):
        Expenses(id=1, description='abc', amount=-100, big=False)


def test_zero_amount():
    with pytest.raises(ValueError):
        Expenses(id=1, description='abc', amount=0, big=False)


def test_big_amount(capsys):
    expenses = [Expenses(id=1, description='abc', amount=1000, big=False)]
    print_expenses(expenses)
    captured = capsys.readouterr()
    assert "(!)" in captured.out


def test_small_amount(capsys):
    expenses = [Expenses(id=1, description='abc', amount=999, big=False)]
    print_expenses(expenses)
    captured = capsys.readouterr()
    assert "(!)" not in captured.out