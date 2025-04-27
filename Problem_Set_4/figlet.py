import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    f = sys.argv[2]
    if f not in figlet.getFonts():
        sys.exit("Invalid Input!!!")
    figlet.setFont(font=f)
else:
    sys.exit("use '-f' or '--font'.")

s = input("Input: ")

print(figlet.renderText(s))