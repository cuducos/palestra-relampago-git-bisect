from re import compile, match

from calculadora import adição, divisão, multiplicação, subtração

REGEX = compile(r"(?P<x>\d+)\s?(?P<função>[+\-*/×])\s?(?P<y>\d+)")
MAPPING = {"+": adição, "-": subtração, "*": multiplicação, "/": divisão}


class ParserError(Exception):
    pass


def parse(expressão):
    matches = match(REGEX, expressão)
    if not matches:
        raise ParserError(f"{expressão} não é uma expressão válida")

    sinal = matches.group("função")
    função = MAPPING.get(sinal)
    if not função:
        raise ParserError(f"{sinal} não é um sinal válido")

    x, y = int(matches.group("x")), int(matches.group("y"))
    return função, x, y
