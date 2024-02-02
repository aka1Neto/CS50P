from um import count;

def main():
    test();

def test():
    assert count("Hello") == 0;
    assert count("Um, thanks for the album.") == 1;
    assert count("Um, thanks, um...") == 2;

if __name__ == "__main__":
    main();