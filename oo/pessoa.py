"""Classe Pessoa."""


class Pessoa():
    """Classe que cria objeto pessoa."""

    def __init__(self, nome):
        """Recebe o parametro nome na criação do objeto."""
        self.nome = nome

    def cumprimentar(self):
        return f'Olá! Sou o {self.nome}'

if __name__ == '__main__':
    evandro = Pessoa('Evandro')
    print(evandro.cumprimentar())
