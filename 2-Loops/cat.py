"""
i = 0
while i < 3:
    print("meow")
    i += 1


for _ in range(3):
    print("Meow")

print("meow\n" * 3, end = "")

while true:
    n = int(input("Enter number: "))
    if n > 0:
        break

for _ in range(n):
    print("Meow")



def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("number: "))
        if n > 0:
            break
    return n

def meow(n)

"""
