from calculadora import adição, divisão, multiplicação, subtração


def test_adição():
    assert adição(40, 2) == 42


def test_subtração():
    assert subtração(50, 8) == 42


def test_multiplicação():
    assert multiplicação(21, 2) == 42


def test_divisão():
    assert divisão(84, 2) == 42
