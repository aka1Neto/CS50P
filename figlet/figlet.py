from pyfiglet import Figlet;
from random import choice;
from sys import argv, exit;

figlet = Figlet();
fonts = figlet.getFonts();

if len(argv) == 1:
    f = Figlet(font=choice(fonts));

elif len(argv) == 3:
    if argv[1] == "-f" or argv[1] == "--font":
        if argv[2] in fonts:
            f = Figlet(font=argv[2]);

        else:
            exit("Invalid usage");

    else:
        exit("Invalid usage");

else:
    exit("Invalid usage");

text = input("Input: ");
print(f"Output: {f.renderText(text)}");