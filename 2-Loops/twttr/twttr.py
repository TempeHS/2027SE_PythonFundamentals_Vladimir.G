def main():
    word = input("String: ")

    vowels = ["a", "e", "o", "i", "u"]

    for character in word:
        if character.lower() in vowels:
            continue
        print(character, end="")
    print()


main()
