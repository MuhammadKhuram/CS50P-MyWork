def main():
    word = input("Input: ")
    print("Output: " + shorten(word))


def shorten(word):
    for vowel in "aeiouAEIOU":
        word = word.replace(vowel, "")

    return word


if __name__ == "__main__":
    main()
