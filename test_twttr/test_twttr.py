from twttr import shorten

def main():
    test_lower();
    test_upper();
    test_novowels();

def test_lower():
    assert shorten("love") == "lv";
    assert shorten("disgusting") == "dsgstng";
    assert shorten("subtle") == "sbtl";

def test_upper():
    assert shorten("KNIGHTS") == "KNGHTS";
    assert shorten("OF") == "F";
    assert shorten("ZODIAC") == "ZDC";

def test_novowels():
    assert shorten("CS50") == "CS50";
    assert shorten("Rhythm") == "Rhythm";
    assert shorten("Myths!") == "Myths!";

if __name__ == "__main__":
    main();