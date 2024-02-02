from csv import reader, writer;
from sys import argv, exit;

args = len(argv);
data = [];

if args < 3:
    exit("Too few command-line arguments");

elif args >= 4:
    exit("Too many comand-line arguments");

try:
    with open(argv[1]) as file:
        csv = reader(file);
        for row in csv:
            data.append([row[0], row[1]]);

except FileNotFoundError:
    exit(f"Could not read {argv[1]}");


table = data[1:];
with open(argv[2], 'w') as file:
    csv = writer(file);
    csv.writerow(['first','last','house']);
    for row in table:
        name = row[0].split(", ");
        csv.writerow([name[1], name[0], row[1]]);
