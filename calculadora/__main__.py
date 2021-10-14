from click import secho, prompt

from calculadora.parser import ParserError, parse


def pergunta():
    expressão = prompt("=>", prompt_suffix=" ")
    try:
        return parse(expressão)
    except ParserError as error:
        secho(str(error), fg="red", err=True)

    return pergunta()


def cli():
    """Calculadora na sua linha de comando"""
    função, x, y = pergunta()
    resultado = função(x, y)
    secho(str(resultado), fg="green")


if __name__ == "__main__":
    cli()
