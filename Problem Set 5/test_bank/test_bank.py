from bank import value


def test_uppercase():
    assert value("HELLO") == 0


def test_lowercase():
    assert value("hello") == 0


def test_start_with_h():
    assert value("hi") == 20
    assert value("HI") == 20


def test_else():
    assert value("What's Happening?") == 100
