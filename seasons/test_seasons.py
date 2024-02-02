from seasons import convert;

def main():
    test();

def test():
    assert convert(525600) == "Five hundred twenty-five thousand, six hundred minutes";
    assert convert(1051200) == "One million, fifty-one thousand, two hundred minutes"

if __name__ == "__main__":
    main();