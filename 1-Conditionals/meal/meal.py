def main():
    time = input("What is the time? ")

    x = convert(time)

    if x >= 7 and x <= 8:
        print("Breakfast time")
    elif x >= 12 and x <= 13:
        print("Lunch time")
    elif x >= 18 and x <= 19:
        print("Dinner time")
    else:
        print("Not time for food")


def convert(time):
    hours, mins = time.split(":")
    hours = float(hours)
    mins = float(mins)
    converts = hours + (mins / 60)
    print(converts)
    return converts


if __name__ == "__main__":

    main()
