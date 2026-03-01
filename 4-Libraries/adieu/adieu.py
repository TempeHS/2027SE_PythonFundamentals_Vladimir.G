import inflect

p = inflect.engine()


def main():

    name_list = []

    while True:
        try:
            name = input("Enter names: ")
            name_list += [name]
        except KeyboardInterrupt:
            break

    print("\n")
    adieu = p.join(name_list)
    print(f"Adieu, adieu, to {adieu}")


if __name__ == "__main__":
    main()
