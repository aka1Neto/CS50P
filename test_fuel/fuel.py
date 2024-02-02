def main():
    text = input("Fraction: ");
    fraction = convert(text);
    print(gauge(fraction));



def convert(fraction):
    fraction = fraction.split("/");
    while True:
        try:
            result = (int(fraction[0]) / int(fraction[1])) * 100;

        except ValueError:
            raise ValueError;

        except ZeroDivisionError:
            raise ZeroDivisionError;

        if not 0 < result <= 100:
            fraction = input("Fraction: ");

        else:
            return result;


def gauge(percentage):
    if percentage <= 1:
        return "E";
    elif percentage >= 99:
        return "F";
    else:
        return f"{percentage:.0f}%";


if __name__ == "__main__":
    main()



