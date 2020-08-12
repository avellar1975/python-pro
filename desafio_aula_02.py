"""
Função fizzbuzz recebe número int n.

Lista uma sequencia de n número inteiros
Substituindo por palavras
fizz para múltiplos de 2
buzz para múltiplos de 5
fizzbuzz para múltiplos de 10
"""


def fizzbuzz(n):
    """Recebe um argumento n inteiro."""
    for i in range(1, n+1):
        if i % 2 == 0 and i % 5 != 0:
            print('fizz')
        elif i % 5 == 0 and i % 2 != 0:
            print('buzz')
        elif i % 2 == 0 and i % 5 == 0:
            print('fizzbuzz')
        else:
            print(i)
