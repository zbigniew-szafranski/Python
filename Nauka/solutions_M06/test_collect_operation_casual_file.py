from M06L05_pp import collect_operation, RenameOperation

def test_collect_operation_casual_file():
    got = collect_operation('file.txt')
    expected = RenameOperation('file.txt', 'file.bak')
    assert got == expected

def test_collect_operation_casual_file_missing_extension():
    got = collect_operation('file')
    expected = RenameOperation('file', 'file.bak')
    assert got == expected

def test_collect_operation_casual_file_multiple_dot():
    got = collect_operation('long.name.txt')
    expected = RenameOperation('long.name.txt', 'long.name.bak')
    assert got == expected

def test_collect_operation_casual_file_with_empty_extension():
    got = collect_operation('file.')
    expected = RenameOperation('file.', 'file.bak')
    assert got == expected

def test_collect_operation_dir():
    got = collect_operation('dir.with.dots/file.txt')
    expected = RenameOperation('dir.with.dots/file.txt', 'dir.with.dots/file.bak')
    assert got == expected
