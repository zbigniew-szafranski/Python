from M06L04 import get_unique_words

def test_empty():
    assert get_unique_words([]) == []


def test_list_list():
    result  = get_unique_words([["one"], ["two"]])
    assert set(result) == set(["one", "two"])

def test_list_str():
    result  = get_unique_words([["one", "two"], ["three", "two"]])
    assert set(result) == set(["one", "two", "three"])