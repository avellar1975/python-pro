"""Contar quantos caracteres possui uma string."""


def contar_caracter(palavra):
    """Recebe uma palavra e conta os caracteresself.

    Exemplo:
    >>> contar_caracter('evandro')
    a: 1
    d: 1
    e: 1
    n: 1
    o: 1
    r: 1
    v: 1

    >>> contar_caracter('banana')
    a: 3
    b: 1
    n: 2

    :param palavra: string a ser contada
    """
    lista = []
    quant = []
    pal_ordenada = sorted(palavra)
    for letra in pal_ordenada:
        if letra not in lista:
            lista.append(letra)
            cont = pal_ordenada.count(letra)
            quant.append(cont)

    for i in range(len(lista)):
        print(f'{lista[i]}: {quant[i]}')


if __name__ == '__main__':
    contar_caracter('banana')
