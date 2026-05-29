def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    first_digit = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not first_digit:
                if s[i] == "0":
                    return False
                first_digit = True
        else:
            if first_digit:
                return False

    return True


main()
