from M06L03 import average_word_length


def test_avg_zero():
    assert average_word_length('') == 0


def test_avg_numbers():
    assert average_word_length('1 2 3 4 5') == 0


def test_avg_words():
    assert average_word_length('one two three four five') == 3.8


def test_punctuation():
    assert average_word_length('one! two2. three? four five') == 3.8


def test_multiple_spaces():
    assert average_word_length('one  two  three four five  ') == 3.8


def test_whitespace():
    assert average_word_length(' one two three four five\n') == 3.8
