"""
def main():
    print_columun(3)


def print_columun(height):
    for _ in range(height):
        print("#")


main()



def main():
    print_row(4)


def print_row(width):
    print("?" * width)


main()
"""


def main():
    print_sqaure(3)


def print_sqaure(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
