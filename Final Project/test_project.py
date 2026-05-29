from project import get_file_parts, split_name, apply_style

def test_get_file_parts():
    assert get_file_parts("vacation_photo.JPG") == ("vacation_photo", ".jpg")
    assert get_file_parts("archive.tar.gz") == ("archive.tar", ".gz")
    assert get_file_parts("README") == ("README", "")

def test_split_name():
    assert split_name("my_cool_file") == ["my", "cool", "file"]
    assert split_name("some-data-points") == ["some", "data", "points"]
    assert split_name("Mixed_styles-here and_there") == ["Mixed", "styles", "here", "and", "there"]

def test_apply_style():
    words = ["hello", "world"]
    assert apply_style(words, "snake") == "hello_world"
    assert apply_style(words, "kebab") == "hello-world"
    assert apply_style(words, "title") == "Hello World"
    assert apply_style(words, "upper") == "HELLO WORLD"
