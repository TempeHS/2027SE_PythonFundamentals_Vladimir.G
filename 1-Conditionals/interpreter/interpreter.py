def main():
    problem = input("What is math problem? ")
    x, y, z = problem.split()

    x = float(x)
    z = float(z)

    if y == "+":
        print(round(x + z, 1))
    elif y == "-":
        print(round(x - z, 1))
    elif y == "*":
        print(round(x * z, 1))
    elif y == "/":
        print(round(x / z, 1))
    else:
        print("Text invalid")


main()
