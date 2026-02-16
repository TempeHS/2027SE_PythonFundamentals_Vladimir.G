answer = input("What is the meaning of life? ")
answerCasefold = answer.casefold()

match answerCasefold:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
