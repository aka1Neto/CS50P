import random


def main():
    level = get_level();

    score = 0;
    for _ in range(10):
        n1 = generate_integer(level);
        n2 = generate_integer(level);
        a = n1 + n2;
        for i in range(4):
            if(i == 3):
                print(f"{n1} + {n2} = {a}");

            else:
                answer = int(input(f"{n1} + {n2} = "))
                if answer == a:
                    score += 1;
                    break;

                else:
                    print("EEE");

    print(f"Score: {score}");



def get_level():
    while True:
        try:
            level = int(input("Level: "));

        except ValueError:
            level = int(input("Level : "));

        if level < 1 or level > 3:
            level = int(input("Level: "));

        else:
            break;

    return level;


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9);

    elif level == 2:
        return random.randint(10, 99);

    else:
        return random.randint(100, 999);


if __name__ == "__main__":
    main()