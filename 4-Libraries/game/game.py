import random


def main():

    while True:
        range = input("What is the level? ")
        range_int = int(range)
        if range_int > 0:
            break
        else:
            continue

    secret_number = random.randint(0, range_int)

    guess(secret_number)


def guess(secret_number):

    while True:
        user_guess = input("What is your guess: ")
        user_guess = int(user_guess)
        if user_guess < 0:
            continue
        elif user_guess > secret_number:
            print("Too High!")
        elif user_guess < secret_number:
            print("Too Low")
        elif user_guess == secret_number:
            print("You won!")
            break


if __name__ == "__main__":
    main()
