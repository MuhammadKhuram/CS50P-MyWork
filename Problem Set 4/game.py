import random
import sys


def main():

    while True:
        try:
            level = int(input("Level: "))
            if level >= 0:
                random_number = random.randint(0, level)
                break
        except ValueError:
            pass

    while True:
        try:
            guess = int(input("Guess: "))

            if guess < 0:
                raise ValueError

            elif guess > random_number:
                print("Too large!")

            elif guess < random_number:
                print("Too small!")

            else:
                sys.exit("Just right!")

        except ValueError:
            pass


main()
