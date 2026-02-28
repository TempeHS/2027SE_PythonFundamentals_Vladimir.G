def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_valid_length(s) and is_valid_prefix(s[0:2]) and is_valid_tail(s[2:])


def is_valid_length(s):
    if len(s) >= 2 and len(s) <= 6:
        return True
    else:
        return False


def is_valid_prefix(s):
    for c in s:
        if c.isalpha():
            continue
        else:
            return False
    return True


def is_valid_tail(s):
    checking_letters = True
    checking_numbers = False

    for c in s:
        if not s.isalnum:
            return False
        if checking_letters:
            if not c.isalpha():
                checking_letters = False
                checking_numbers = True
                if c == "0":
                    return False
        elif checking_numbers:
            if not c.isdigit():
                return False
    return True


main()
