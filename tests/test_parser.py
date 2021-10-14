from pytest import raises

from calculadora import adição
from calculadora.parser import ParserError, parse


def test_parse_with_good_expression():
    assert parse("40 + 2") == (adição, 40, 2)


def test_parse_with_bad_expression():
    with raises(ParserError, match="matemática não é uma expressão válida"):
        parse("matemática")


def test_parse_with_bad_signal():
    with raises(ParserError, match="× não é um sinal válido"):
        parse("40 × 2")
