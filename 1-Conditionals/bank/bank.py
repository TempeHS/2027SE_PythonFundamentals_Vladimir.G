greeting = input(" ")

greetingCasefold = greeting.casefold().strip()

if greetingCasefold.startswith("hello"):
    print("$0")
elif greetingCasefold.startswith("h"):
    print("$20")
else:
    print("$100")
