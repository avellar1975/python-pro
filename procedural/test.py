"""Teste da função fizzbuzz."""
import unittest


class TesteFizzBuzz(unittest.TestCase):
    """Classe para teste da função fizzbuzz."""

    def test_com_10(self):
        """Teste com entrada igual a 10."""
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
    lista = []
    for i in range(1, n+1):
        if i % 2 == 0 and i % 5 != 0:
            lista.append('fizz')
        elif i % 5 == 0 and i % 2 != 0:
            lista.append('buzz')
        elif i % 2 == 0 and i % 5 == 0:
            lista.append('fizzbuzz')
        else:
            lista.append(i)
    return lista
