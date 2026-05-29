from twttr import shorten

def test_upper():
    assert shorten("HELLO") == "HLL"

def test_lower():
    assert shorten("hello") == "hll"

def test_punctuation():
    assert shorten("Hello!") == "Hll!"

def test_numbers():
    assert shorten("Hello123") == "Hll123"
