def main():
    word = input("Name: ")

    for character in word:
        if character.isupper():
            print("_" + character.lower(), end="")
        else:
            print(character, end="")
    print()


main()
