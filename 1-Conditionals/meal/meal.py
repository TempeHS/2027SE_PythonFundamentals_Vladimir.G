def main():
    time = input("What is the time? ")

    convert(time)

    print(time)


def convert(time):
    time = float(time)
    time = time / 60


if __name__ == "__main__":

    main()
