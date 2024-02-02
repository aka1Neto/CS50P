months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ").title().strip();
    if date.find("/") != -1:
        date = date.split("/");

        if not date[0].isnumeric():
            continue;

    else:
        if date.find(",") == -1:
            continue;

        else:
            date = date.replace(',', '').split();

    if len(date) < 3:
        continue;


    try:
        d = int(date[1]);
        y = int(date[2]);
        m = int(date[0]);

    except ValueError:
        if not date[0] in months:
            continue;
        m = months.index(date[0]) + 1;
        d = int(date[1]);
        y = int(date[2]);

    if d > 31 or m > 12:
        continue;

    break;

print(f"{y:04}-{m:02}-{d:02}");
