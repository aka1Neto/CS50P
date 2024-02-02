from jar import Jar;
from pytest import raises;

def main():
    test_init();
    test_str();
    test_deposit();
    test_withdraw();

def test_init():
    jar = Jar();

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar();
    jar.deposit(1);
    assert jar.size == 1;

    with raises(ValueError):
        assert jar.deposit(12);

def test_withdraw():
    jar = Jar();
    jar.deposit(2);
    jar.withdraw(1)
    assert jar.size == 1;

    with raises(ValueError):
        assert jar.withdraw(2);

if __name__ == "__main__":
    main();