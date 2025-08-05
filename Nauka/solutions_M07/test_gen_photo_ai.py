from M07L04_ai import generate_photo_name
import pytest

def test_first_photo_name(tmpdir):
    with tmpdir.as_cwd():
        existing_photos = []
        got = generate_photo_name(existing_photos)
        expected = "IMG_0001.jpg"
        assert got == expected

def test_second_photo_name(tmpdir):
    with tmpdir.as_cwd():
        open("IMG_0001.jpg", "w").close()
        existing_photos = ["IMG_0001.jpg"]
        got = generate_photo_name(existing_photos)
        expected = "IMG_0002.jpg"
        assert got == expected

def test_middle_photo_name(tmpdir):
    with tmpdir.as_cwd():
        open("IMG_0001.jpg", "w").close()
        open("IMG_0003.jpg", "w").close()
        existing_photos = ["IMG_0001.jpg", "IMG_0003.jpg"]
        got = generate_photo_name(existing_photos)
        expected = "IMG_0002.jpg"

def test_last_photo_name(tmpdir):
    with tmpdir.as_cwd():
        open("IMG_9999.jpg", "w").close()
        existing_photos = ["IMG_9999.jpg"]

        with pytest.raises(ValueError, match="Przekroczono maksymalny numer zdjęcia.*"):
            generate_photo_name(existing_photos)