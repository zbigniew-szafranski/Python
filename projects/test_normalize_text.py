from M05_amazon_project import normalize_text

def test_method_strip():
    text = " abcd efgh "
    got = normalize_text(text)
    expected = "abcd efgh"
    assert got == expected

def test_method_replace():
    text = "abcd\nefgh"
    got = normalize_text(text)
    expected = "abcd efgh"
    assert got == expected


def test_multiple_spaces():
    text = "abcd   efgh"
    got = normalize_text(text)
    expected = "abcd efgh"
    assert got == expected

def test_multiple_spaces_and_newlines():
    text = "abcd\n\nefgh\n\n"
    got = normalize_text(text)
    expected = "abcd efgh"
    assert got == expected


def test_polish_chars():
    text = "ęąśćżź ółń"
    got = normalize_text(text)
    expected = "ęąśćżź ółń"
    assert got == expected