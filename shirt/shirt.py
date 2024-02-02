from PIL import Image, ImageOps;
from sys import argv, exit;

args = len(argv);
extensions = ['png', 'jpg', 'jpeg'];

if args < 3:
    exit("Too few command-lines arguments");

elif args >= 4:
    exit("Too many command-lines arguments");

ext1 = argv[1].split(".")[-1];
ext2 = argv[2].split(".")[-1];

if ext1 not in extensions or ext2 not in extensions:
    exit("Invalid output");

elif ext1 != ext2:
    exit("Input and output have different extensions");

try:
    shirt = Image.open("shirt.png");
    size = shirt.size;

except FileNotFoundError:
    exit("File does not exist");

try:
    img = Image.open(argv[1]);
    img = ImageOps.fit(img, size);

except FileNotFoundError:
    exit("Input does not exist");

img.paste(shirt, shirt);
img.save(argv[2]);