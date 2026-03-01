from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

random_choice = random.choice(figlet.getFonts())

s = input("What is text: ")

if len(sys.argv) == 1:
    figlet.setFont(font=random_choice)
    print(figlet.renderText(s))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(s))
    else:
        sys.exit("invalid font")
else:
    sys.exit("Invalid")
