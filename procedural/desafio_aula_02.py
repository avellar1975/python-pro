"""
Função fizzbuzz recebe número int n.

Lista uma sequencia de n número inteiros
Substituindo por palavras
fizz para múltiplos de 2
buzz para múltiplos de 5
fizzbuzz para múltiplos de 10
"""


import unittest


class TesteFizzBuzz(unittest.TestCase):
    """Classe para teste da função fizzbuzz."""

    def test_com_10(self):
        entrada = 10
        resultado = fizzbuzz(entrada)
        esperado = [
            1,
            'fizz',
            3,
            'fizz',
            'buzz',
            'fizz',
            7,
            'fizz',
            9,
            'fizzbuzz'
            ]
        self.assertListEqual(esperado,  resultado)


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
