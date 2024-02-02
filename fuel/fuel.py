while True:
    try:
        text = input("Fraction: ").split("/")
        result = int(text[0]) / int(text[1]);

    except (ValueError, ZeroDivisionError):
        text = input("Fraction: ")
        result = int(text[0]) / int(text[1]);

    if 0 <= result <=1:
        break;


if result <= 0.1:
    print("E");
elif result >= 0.9:
    print("F");
else:
    print(f"{result:.0%}");