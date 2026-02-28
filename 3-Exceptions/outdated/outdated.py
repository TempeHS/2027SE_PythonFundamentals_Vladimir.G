def main():

    date = input("Enter date in Month/Day/Year or Month Day, Year format: ")

    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    try:
        if "/" in date:
            month, day, year = date.split("/")
            if int(day) > 31:
                raise ValueError
            if int(month) > 12:
                raise ValueError
            print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        else:
            clean_date = date.replace(",", "")
            month, day, year = clean_date.split()
            if month not in month_list:
                raise ValueError
            if int(day) > 31:
                raise ValueError
            month = str(month_list.index(month))
            print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
    except ValueError:
        main()


main()
