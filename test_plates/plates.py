def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for i in range(len(s)):
        if s[i].isnumeric():
            break;

    if len(s) < 2 or len(s) > 6:
        return False;

    elif s.isalpha():
        return True;

    elif not s[:2].isalpha():
        return False;

    elif s[i] == '0':
        return False;

    elif not s[i:].isnumeric():
        return False;

    else:
        return True;


if __name__ == "__main__":
    main()