"""Contar quantos caracteres possui uma string."""


def contar_caracter(palavra):
    """Recebe uma palavra e conta os caracteresself.

    Exemplo:
    >>> contar_caracter('evandro')
    {'a': 1, 'd': 1, 'e': 1, 'n': 1, 'o': 1, 'r': 1, 'v': 1}

    >>> contar_caracter('banana')
    {'a': 3, 'b': 1,'n': 2}

    :param palavra: string a ser contada
    """
    dicionario = {}

    for letra in palavra:
        dicionario[letra] = dicionario.get(letra, 0) + 1

    return dicionario


if __name__ == '__main__':
    print(contar_caracter('banana'))
    print(contar_caracter('evandro'))
