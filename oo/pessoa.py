"""Classe Pessoa."""


class Pessoa:
    """Classe que cria objeto pessoa."""

    def __init__(self, nome, idade=35, *filhos):
        """Recebe o parametro nome na criação do objeto."""
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        """Método cumprimentar."""
        return f'Olá! Sou o {self.nome}'


if __name__ == '__main__':
    yanni = Pessoa(nome='Yanni', idade=22)
    evandro = Pessoa('Evandro', 44, yanni)
    print(f'{evandro.nome} tem {evandro.idade} e seus filhos são:')
    for filho in evandro.filhos:
        print(filho.nome)
    print(evandro.cumprimentar())
