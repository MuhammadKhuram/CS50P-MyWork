import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("File does not exist")

    else:
        print(line_count(sys.argv[1]))


def line_count(file):
    count = 0
    with open(file, "r") as file:
        for line in file:
            if line.strip().startswith("#") or len(line.strip()) == 0:
                pass
            else:
                count = count+1
    return count


if __name__ == "__main__":
    main()
