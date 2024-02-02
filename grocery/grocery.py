grocery = {};

while True:
    try:
        item = input().upper();
        grocery[item] += 1;

    except KeyError:
        grocery[item] = 1;

    except EOFError:
        break;

for key, value in sorted(grocery.items()):
    print(value, key);