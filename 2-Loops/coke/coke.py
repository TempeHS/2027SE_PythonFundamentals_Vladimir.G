def main():
    total_amount = 0
    coke_price = 50

    while coke_price > total_amount:
        amount = int(input("Insert coin: "))
        if amount != 25 and amount != 10 and amount != 5:
            print("Amount due:", coke_price - total_amount)
            continue
        total_amount += amount
        amount_due = coke_price - total_amount
        if amount_due < 0:
            print("Change owed:", -amount_due)
        else:
            print("Amount due:", amount_due)


main()
