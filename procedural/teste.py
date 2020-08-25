"""Conceito de testes unitários."""
from unittest import TestCase


def soma(*args):
    """Recebe dois argumentos e retorna a soma."""
    concatena = ''
    if any(type(item) == str for item in args):
        for item in args:
            item = str(item)
            concatena += item
        return concatena
    return sum(args)

# Testes unitários ------------------------------------------------------------


class Test_soma(TestCase):
    """Teste da função soma."""

    def teste_soma_inteiros(self):
        """Testa a soma de inteiros."""
        resultado = soma(1, 2)
        esperado = 3
        self.assertEqual(esperado, resultado)

    def teste_soma_strings(self):
        """Testa a soma de strings."""
        resultado = soma('foo', 'bar')
        esperado = 'foobar'
        self.assertEqual(esperado, resultado)

    def teste_soma_strings_inteiros(self):
        """Testa a soma de strings e inteiros."""
        resultado = soma('foo', 'bar', 100)
        esperado = 'foobar100'
        self.assertEqual(esperado, resultado)

    def teste_soma_float(self):
        """Testa a soma de floats."""
        resultado = soma(1.5, -2)
        esperado = -0.5
        self.assertEqual(esperado, resultado)
