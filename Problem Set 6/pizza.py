import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        print(table_format(sys.argv[1]))


def table_format(menu):
    with open(menu) as file:
        mule = csv.reader(file)
        return tabulate(mule, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()
