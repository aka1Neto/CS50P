def main():
    time = input("What time is it?");
    num = convert(time);
    if num >= 7 and num <= 8:
        print("breakfast time");

    elif num >= 12 and num <= 13:
        print("lunch time");

    elif num >= 18 and num <= 19:
        print("dinner time");

def convert(time):
    num = time.split(":");
    num[0] = float(num[0]);
    num[1] = float(num[1]) / 60;
    return(sum(num));


if __name__ == "__main__":
    main()