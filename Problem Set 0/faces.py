def main():
    x = input("Enter something: ")
    print(convert(x))

def convert(x):
    return x.replace(":)", "🙂").replace(":(", "🙁")


main()
