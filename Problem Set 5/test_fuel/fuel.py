def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")

    if int(y) == 0:
        raise ZeroDivisionError

    if x.isdigit() == False or y.isdigit() == False or int(x) > int(y):
        raise ValueError

    else:
        return round(int(x)/int(y) * 100)


def gauge(percentage):

    if 0 <= percentage <= 1:
        return ("E")
    elif 99 <= percentage <= 100:
        return ("F")
    elif 1 < percentage < 99:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
