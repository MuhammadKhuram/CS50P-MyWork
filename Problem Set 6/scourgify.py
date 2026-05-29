import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit(f"Could not read {sys.argv[1]}")

    else:
        table_format(sys.argv[1], sys.argv[2])


def table_format(before, after):
    with open(before) as before:
        reader = csv.DictReader(before)

        with open(after, 'w') as after:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(after, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                last_name, first_name = row['name'].split(", ")
                house = row['house']
                writer.writerow({'first': first_name, 'last': last_name, 'house': house.lstrip("")})


if __name__ == "__main__":
    main()
