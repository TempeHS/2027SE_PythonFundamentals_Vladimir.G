def main():
    fuel_percent = get_value("What is fuel level? ")

    try:
        fuel_converted = calculate(fuel_percent)

        if fuel_converted <= 1:
            print("E")
        elif fuel_converted >= 1 and fuel_converted < 99:
            print(fuel_converted)
        else:
            print("F")
    except (ValueError, ZeroDivisionError):
        main()


def get_value(fuel_percentage):
    return input(fuel_percentage)


def calculate(fuel_percent):
    x, y = fuel_percent.split("/")
    x = float(x)
    y = float(y)
    if x > y:
        raise ValueError
    fuel_converted = (x / y) * 100
    return fuel_converted


main()
