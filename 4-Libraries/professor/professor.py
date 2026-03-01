import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        x, y = generate_integer(level)

        for i in range(3):
            try:
                answer = int(input(f"{x} + {y}: \n"))
            except ValueError:
                print("EEE \n")
                continue

            if answer == x + y:
                score += 1
                print("Your score is now: ", score)
                break
            else:
                print("EEE \n")

        else:
            print(f"{x} + {y}\n")

    print("Your final score is now:", score)


def get_level():
    while True:
        try:
            level = input("Choose a difficulty, 1, 2 or 3 \n ")
            level = int(level)
            if level == 1 or level == 3 or level == 2:
                print(level)
                return level
        except ValueError:
            pass


def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        print("level 1 numbers have been generated \n")
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        print("level 2 numbers have been generated \n")
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        print("level 3 numbers have been generated \n")
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()
