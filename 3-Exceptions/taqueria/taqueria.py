def main():

    food_dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    total = 0

    while True:
        try:
            item = input("What item would you like to order? ").title()
            print("You have ordered", item)
        except (EOFError, KeyboardInterrupt):
            break

    if item in food_dict:
        total += food_dict[item]
        print("total: $", item)

    print("program did not reach here")


main()
