import sys

if len(sys.argv) != 2:
    sys.exit("Invalid")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Invalid")

count = 0

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            whitespace = line.strip()
            if whitespace == "" or whitespace.startswith("#"):
                continue
            count += 1
except (FileNotFoundError, FileExistsError):
    sys.exit("File is invalid")


print(count)
