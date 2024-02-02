from random import randint;
from sys import exit;

while True:
    while True:
        try:
            level = int(input("Level: "));

        except ValueError:
            level = int(input("Level: "));

        if level <= 0:
            level = int(input("Level: "));

        else:
            break;

    number = randint(1, level);

    while True:
        try:
            guess = int(input("Guess: "));

        except ValueError:
            guess = int(input("Guess: "));

        if guess <= 0:
            guess = int(input("Guess: "));

        else:
            break;

    if guess < number:
        print("Too small!");

    elif guess > number:
        print("Too large!");

    else:
        exit("Just right!");