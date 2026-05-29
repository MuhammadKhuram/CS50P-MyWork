import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for j in range(3):
            answer = input(f"{x} + {y} = ")
            if int(answer) == x + y:
                score = score + 1
                break
            elif j < 2:
                print("EEE")

            else:
                print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")

def get_level():
    level = int(input("Level: "))
    while level < 1 or level > 3 or type(level) != int:
        level = int(input("Level: "))
    return level

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
