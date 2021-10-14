from unittest.mock import patch

from click.testing import CliRunner
from pytest import raises

from calculadora import adição
from calculadora.__main__ import cli, pergunta


def run_cli_with(expression=None):
    args = ("--expressão", expression) if expression else None
    runner = CliRunner()
    result = runner.invoke(cli, args)
    assert result.exit_code == 0
    return result.output.strip()


def test_pergunta_with_valid_argument():
    assert pergunta("40 + 2") == (adição, 40, 2)


def test_pergunta_with_invalid_argument():
    with patch("calculadora.__main__.prompt") as prompt:
        prompt.return_value = "40 + 2"
        assert pergunta("etc") == (adição, 40, 2)


def test_pergunta_without_argument_and_without_recursion():
    with patch("calculadora.__main__.prompt") as prompt:
        prompt.return_value = "40 + 2"
        assert pergunta() == (adição, 40, 2)


def test_pergunta_without_argument_and_with_recursion():
    with patch("calculadora.__main__.prompt") as prompt:
        prompt.side_effect = ("etc", "40 + 2")
        assert pergunta() == (adição, 40, 2)


def test_pergunta_with_exit_command():
    with raises(SystemExit), patch("calculadora.__main__.prompt") as prompt:
        prompt.return_value = "sair"
        pergunta()


def test_cli_without_expression():
    with patch("calculadora.__main__.prompt") as prompt:
        prompt.return_value = "40 + 2"
        assert run_cli_with() == "42"


def test_cli_with_valid_expression():
    assert run_cli_with("40 + 2") == "42"


def test_cli_with_invalid_expression():
    with patch("calculadora.__main__.prompt") as prompt:
        prompt.return_value = "40 + 2"
        assert run_cli_with("etc") == "etc não é uma expressão válida\n42"
