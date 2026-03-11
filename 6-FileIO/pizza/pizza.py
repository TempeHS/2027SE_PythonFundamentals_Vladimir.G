import sys
import csv
from tabulate import tabulate


def main():

    if len(sys.argv) != 2:
        sys.exit("Invalid")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Invalid")

    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            print(tabulate(rows, headers="keys", tablefmt="simple"))
    except FileNotFoundError:
        sys.exit("Invalid")


main()
