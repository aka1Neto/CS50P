from fuel import convert, gauge
from pytest import raises

def main():
    test_convert();
    test_gauge();

def test_convert():
    with raises(ValueError):
        assert convert("cat/dog");

    with raises(ZeroDivisionError):
        assert convert("10/0");

    assert convert("5/10") == 50;
    assert convert("3/4") == 75;

def test_gauge():
    assert gauge(1) == "E";
    assert gauge(50) == "50%";
    assert gauge(99) == "F";


if __name__ == "__main__":
    main();