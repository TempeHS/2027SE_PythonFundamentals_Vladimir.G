import sys
from PIL import Image
from PIL import ImageOps
import os


def main():

    if len(sys.argv) != 3:
        sys.exit("Too few command lines")

    valid_file_name = (".jpeg", ".png", ".jpg")

    before = sys.argv[1].lower()
    after = sys.argv[2].lower()

    if not before.endswith(valid_file_name):
        sys.exit("Invalid file name")

    if not after.endswith(valid_file_name):
        sys.exit("Invalid file name")

    file_end_one = os.path.splitext(before)[1]
    file_end_two = os.path.splitext(after)[1]

    if file_end_one == file_end_two:
        pass
    else:
        sys.exit("Invalid extensions")

    try:
        with Image.open(sys.argv[1]) as test_file:
            test_file.load()
    except FileNotFoundError:
        sys.exit("File not found")

    with Image.open(sys.argv[1]) as input_file:

        input_file.load()

        shirt = Image.open("shirt.png")

        size = shirt.size

        fitted_image = ImageOps.fit(input_file, size)

        fitted_image.paste(shirt, shirt)

        shirt.close()

        fitted_image.save(sys.argv[2])


main()
