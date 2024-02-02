names = [];

while True:
    try:
        name = input("Name: ");
        names.append(name);

    except EOFError:
        break;

print("Adieu, adieu, to", end="");

for i in range(len(names)):
    if i == 0:
        print(f" {names[i]}", end="");

    elif i == len(names) - 1:
        if i != 1:
            print(",", end="");
        
        print(f" and {names[i]}", end="");

    else:
        print(f", {names[i]}", end="");


print();