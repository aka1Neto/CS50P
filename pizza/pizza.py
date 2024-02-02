from csv import reader;
from tabulate import tabulate;
from sys import argv, exit;

args = len(argv);
menu = [];

if args == 1:
    exit("Too few command-line arguments");

elif args >= 3:
    exit("Too many comand-line arguments");

elif not argv[1].endswith(".csv"):
    exit("Not a CSV file");

try:
    with open(argv[1]) as file:
        csv = reader(file);
        for row in csv:
            menu.append([row[0], row[1], row[2]]);

except FileNotFoundError:
    exit("File does not exit");

headers = menu[0];
table = menu[1:];
print(tabulate(table, headers, tablefmt='grid'));