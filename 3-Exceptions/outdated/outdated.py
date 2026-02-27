def main():

    date = input("Enter date in Month/Day/Year or Month Day, Year format: ")

    months_list = [
        {"January": "01"},
        {"February": "02"},
        {"March": "03"},
        {"April": "04"},
        {"May": "05"},
        {"June": "06"},
        {"July": "07"},
        {"August": "08"},
        {"September": "09"},
        {"October": "10"},
        {"November": "11"},
        {"December": "12"},
    ]

    month = 2
    day = 2

    try:
        if "/" in date:
            month, day, year = date.split("/")
            print(f"year + (" - ") + {month:02} + (" - ") + {day:02}")

        else:
            month, day, year = date.split(" " + ", ")
            print(year, ("-"), {month == months_list}, ("-"), day)
    except ValueError:
        pass

    main()


main()
