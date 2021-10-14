from sys import exit

from click import command, option, secho, prompt

from calculadora.parser import ParserError, parse


def pergunta(expressão=None):
    if not expressão:
        expressão = prompt("=>", prompt_suffix=" ")

    if expressão == "sair":
        exit("Até mais, arroba 💜")

    try:
        return parse(expressão)
    except ParserError as error:
        secho(str(error), fg="red", err=True)

    return pergunta()


@command()
@option("-e", "--expressão")
def cli(expressão=None):
    """Calculadora na sua linha de comando"""
    função, x, y = pergunta(expressão)
    resultado = função(x, y)
    secho(str(resultado), fg="green")


if __name__ == "__main__":
    cli()
