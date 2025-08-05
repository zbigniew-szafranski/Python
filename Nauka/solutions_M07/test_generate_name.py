from M07L04 import generate_name

def test_generate_name_when_no_collision(tmpdir):
    with tmpdir.as_cwd():
        filename = 'file.txt'
        got = generate_name(filename)
        assert got == filename

def test_generate_name_when_two_collisions(tmpdir):
    with tmpdir.as_cwd():
        open('file.txt', 'w').close()
        open('file_2.txt', 'w').close()
        got = generate_name('file.txt')
        expected = 'file_3.txt'
        assert got == expected