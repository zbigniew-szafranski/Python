from M05_amazon_project import normalize_text
def test_method_strip():
    text = "abcd   efgh\n "
    got = normalize_text(text)
    expected = "abcd efgh"
    assert got == expected