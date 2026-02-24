def main():

    fuel_percent = get_value("What is fuel level? ")

    fuel_converted = calculate(fuel_percent)

    if fuel_converted <= 1:
        print("E")
    elif fuel_converted >= 1 and fuel_converted < 99:
        print(fuel_converted)
    else:
        print("F")


def get_value(fuel_percentage):
    while True:
        try:
            return input(fuel_percentage)
        except (ValueError, ZeroDivisionError):
            pass


def calculate(fuel_percent):
    try:
        x, y = fuel_percent.split("/")
        x = float(x)
        y = float(y)
    except ValueError:
        pass

    try:
        fuel_converted = (x / y) * 100
        return fuel_converted
    except ZeroDivisionError:
        pass


main()
