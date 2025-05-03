from M06L03_PP import calculate_word_length


def test_spaces():
    assert calculate_word_length('one two') == 3.0


def tes_numbers():
    assert calculate_word_length('one two2') == 3.0


def test_punctuations():
    assert calculate_word_length('one two,') == 3.0


def test_nicknames():
    assert calculate_word_length('one two123') == 4.5