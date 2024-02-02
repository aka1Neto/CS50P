from bank import value

def main():
    test();

def test():
    assert value("hello") == 0;
    assert value("How are you?") == 20;
    assert value("WHATS'UP?") == 100;


if __name__ == "__main__":
    main();
