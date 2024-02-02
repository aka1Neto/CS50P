from sys import argv, exit;

args = len(argv);
n_lines = 0;

if args == 1:
    exit("Too few command-line arguments");

elif args >= 3:
    exit("Too many comand-line arguments");

elif not argv[1].endswith(".py"):
    exit("Not a Python file");

try:
    with open(argv[1]) as file:
        lines = file.readlines();

except FileNotFoundError:
    exit("File does not exit");


for line in lines:
    if not line.split() or line.strip().startswith("#"):
        continue;

    else:
        n_lines += 1;

print(n_lines);