def main():
    percentage = convert()
    print(gauge(percentage))


def convert():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = fraction.split("/")

            if x.isdigit() == False or y.isdigit() == False or int(x) > int(y):
                raise ValueError

            if int(y) == 0:
                raise ZeroDivisionError

            else:
                return round(int(x)/int(y) * 100)

        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):

    if 0 <= percentage <= 1:
        return ("E")
    elif 99 <= percentage <= 100:
        return ("F")
    elif 1 < percentage < 99:
        return str(round(percentage)) + "%"


if __name__ == "__main__":
    main()
