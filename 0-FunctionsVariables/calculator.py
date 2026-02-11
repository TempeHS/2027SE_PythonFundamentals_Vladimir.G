"""
# When entering a value, the value will then become an int

x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x / y, 2)

print(f"{z:.2f}")

# 4 + 4 = 44 because inputs are str, change to int
# tab can auto finish terminal code

# print(f"{z}")
"""


def main():
    x = int(input("What is X? "))
    print("X squared is", sqaure(x))


def sqaure(n):
    return pow(n, 2)


main()
