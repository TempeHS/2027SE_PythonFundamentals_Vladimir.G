import sys


def main():

    if len(sys.argv) == 1:
        sys.exit("No bitcoin inputted")
    elif len(sys.argv) == 2:
        if sys.argv[1].isdigit() is True:
            n = sys.argv[1]
            print(f"You have inputted {n} bitcoin")
        else:
            sys.exit("Invalid number")

    bitcoin = convert(n)

    print(f"You have {bitcoin:,} bitcoin")


def convert(n):

    n = float(n)

    return n * 6586220


if __name__ == "__main__":
    main()
