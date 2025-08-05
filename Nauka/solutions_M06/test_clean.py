from M06L03 import clean_text

def test_numbers():
    assert clean_text('1 2 3 4 5') == ''

def test_punctation():
    assert clean_text('!@#$%^&*()') == ''