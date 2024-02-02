import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"((?:1[0-2]|\d)(?::[0-5]\d)? [AP]M) to ((?:1[0-2]|\d)(?::[0-5]\d)? [AP]M)", s);

    if matches == None:
        raise ValueError;

    time1, time2 = matches.groups();

    time1 = time1.split();
    if ":" in time1[0]:
        hour1, minute1 = time1[0].split(":");
        hour1 = int(hour1);
        minute1 = int(minute1);

    else:
        hour1 = int(time1[0]);
        minute1 = 0;

    if time1[1] == "PM":
        if hour1 != 12:
            hour1 += 12

    else:
        if hour1 == 12:
            hour1 = 0;


    time2 = time2.split();
    if ":" in time2[0]:
        hour2, minute2 = time2[0].split(":");
        hour2 = int(hour2);
        minute2 = int(minute2);

    else:
        hour2 = int(time2[0]);
        minute2 = 0;

    if time2[1] == "PM":
        if hour2 != 12:
            hour2 += 12

    else:
        if hour2 == 12:
            hour2 = 0;

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}";

if __name__ == "__main__":
    main()