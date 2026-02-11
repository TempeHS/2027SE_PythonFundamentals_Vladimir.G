def main():
    mass = int(input("Enter mass value: "))
    energy = calculate(mass)
    print(energy)


def calculate(mass):
    c = 300000000
    return mass * pow(c, 2)


main()
