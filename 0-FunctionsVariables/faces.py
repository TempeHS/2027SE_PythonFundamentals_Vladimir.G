def convert(message):
    return message.replace(":)", "🙂").replace(":(", "🙁")


def main():
    message = input()
    print(convert(message))


main()
