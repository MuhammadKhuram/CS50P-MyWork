from plates import is_valid


def test_alphanumeric():
    assert is_valid("HM3302") == True


def test_other_charecters():
    assert is_valid("CS50!") == False


def test_start_with_two_letters():
    assert is_valid("MV") == True
    assert is_valid("33") == False
    assert is_valid("M") == False
    assert is_valid("3") == False


def test_number_plate_length():
    assert is_valid("H") == False
    assert is_valid("HMRR234") == False


def test_number_inbetween():
    assert is_valid("HM34R") == False


def test_first_number_zero():
    assert is_valid("HMR034") == False
