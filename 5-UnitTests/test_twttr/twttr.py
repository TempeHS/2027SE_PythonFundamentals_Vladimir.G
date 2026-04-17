def main():

    word = input("String: ")

    print(shorten(word))


def shorten(word):

    new_word = ""

    vowels = ["a", "e", "o", "i", "u"]

    for character in word:
        if character.lower() in vowels:
            continue
        new_word += character.upper()

        # create error via .upper()

    return new_word


if __name__ == "__main__":
    main()
