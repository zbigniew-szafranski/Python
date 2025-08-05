from M06L03_PP import remove_punctuation

def test_remove_punctuation():
    assert remove_punctuation('Hello, world!') == 'Hello world'


def test_remove_punctuation_empty():
    assert remove_punctuation('') == ''