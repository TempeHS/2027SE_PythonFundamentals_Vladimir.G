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
            price = food_dict[item]
            total += price
            print("You have ordered", item)
            print(f"${item} for ${price}")
        except (EOFError, KeyboardInterrupt):
            break

    print(f"\ntotal: ${total:.2f}")


main()
