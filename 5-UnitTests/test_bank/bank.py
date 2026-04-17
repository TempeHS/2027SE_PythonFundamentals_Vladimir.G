def main():

    greeting = input("Greeting: ")

    # Error implemented by removing casefold(), will result in errors.
    greeting_casefold = greeting.strip()

    print(greeting_value(greeting_casefold))


def greeting_value(greeting_casefold):

    if greeting_casefold.startswith("hello"):
        return 0
    elif greeting_casefold.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
