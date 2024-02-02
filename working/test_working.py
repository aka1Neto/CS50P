from pytest import raises;
from working import convert;

def main():
    test();
    test_value_errors();

def test():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_value_errors():
    with raises(ValueError):
        assert convert("9:60 AM to 5:60 PM");

    with raises(ValueError):
        assert convert("9AM-5PM");

    with raises(ValueError):
        assert convert("17 AM 22 PM");

if __name__ == "__main__":
    main();