def main():
    item_list = {}
    while True:
        try:
            item = input("Enter grocery: ").upper()
            if item == "":
                continue
            print("You have added ", item + " to your grocery list")
            item_list[item] = item_list.get(item, 0) + 1
        except (EOFError, KeyboardInterrupt):
            break

    print("")
    for item in sorted(list(item_list)):
        print(item_list[item], item)


main()
