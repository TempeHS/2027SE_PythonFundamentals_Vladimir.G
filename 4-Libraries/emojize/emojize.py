import emoji


def main():
    user = input("Enter text: ")

    print(emoji.emojize(user))


if __name__ == "__main__":
    main()
