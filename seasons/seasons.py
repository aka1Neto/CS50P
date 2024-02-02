from datetime import date
from sys import exit
import inflect
import re

def main():
    print(difference(input("Date of Birth: ")));


def difference(birth):
    match = re.match(r"^\d{4}-\d\d-\d\d$", birth.strip())
    if not match:
        exit("Invalid date");

    try:
        birth = date.fromisoformat(birth);

    except ValueError:
        exit("Invalid date");

    difference = date.today() - birth;
    minutes = round (difference.total_seconds() / 60)
    return convert(minutes);

def convert(minutes):
    i = inflect.engine()
    return f"{i.number_to_words(minutes, andword='').capitalize()} minutes";


if __name__ == "__main__":
    main()