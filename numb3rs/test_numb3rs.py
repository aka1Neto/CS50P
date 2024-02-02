from numb3rs import validate

def main():
    test();

def test():
    assert validate("0.0.0.0") == True;
    assert validate("255.255.255.255") == True;
    assert validate("256.0.0.0") == False;
    assert validate("0.0.0.256") == False;
    assert validate("cat") == False;

if __name__ == "__main__":
    main();