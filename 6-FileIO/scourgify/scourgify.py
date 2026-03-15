import csv
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit("Invalid")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Invalid")

    with open(sys.argv[1], "r") as source_file:
        reader = csv.DictReader(source_file)

        with open("after.csv", "w") as write_file:
            order = ["first_name", "last_name", "house"]
            writer = csv.DictWriter(write_file, fieldnames=order)
            writer.writeheader()

            for row in reader:

                print(row)

                full_name = row["name"].strip()

                if "," not in full_name:
                    print("Invalid")
                    continue

                last_name, first_name = [
                    part.strip() for part in full_name.split(",", 1)
                ]

                writer.writerow(
                    {
                        "first_name": first_name,
                        "last_name": last_name,
                        "house": row["house"],
                    }
                )


if __name__ == "__main__":
    main()
