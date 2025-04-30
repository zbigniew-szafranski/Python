from M06L02 import extension

def test_files_txt():
    files = ["one.txt", "two.txt", "three.zip"]
    got = extension(files)
    expected = ["one.txt", "two.txt"]
    assert got == expected
def test_files_zip():
    files = ["one.zip", "two.zip", "three.zip"]
    got = extension(files)
    expected = []
    assert got == expected
def test_empty():
    files = []
    got = extension(files)
    expected = []
    assert got == expected
