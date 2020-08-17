"""Classe Pessoa."""
from datetime import datetime

class Pessoa:
    """Classe que cria objeto pessoa."""

    olhos = 2

    def __init__(self, nome, idade=35, *filhos):
        """Recebe o parametro nome na criação do objeto."""
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        """Método cumprimentar."""
        return f'Olá! Sou o {self.nome}'

    @staticmethod
    def metodo_estatico():
        return datetime.now()

    @classmethod
    def nome_atributo_classe(cls):
        return f'{cls.olhos}'


class Homem(Pessoa):
    pass


if __name__ == '__main__':
    yanni = Homem(nome='Yanni', idade=22)
    evandro = Pessoa('Evandro', 44, yanni)
    print(f'{evandro.nome} tem {evandro.idade} e seus filhos são:')
    for filho in evandro.filhos:
        print(filho.nome)
    print(evandro.cumprimentar())
    yanni.sobrenome = 'Avellar'
    print(yanni.sobrenome)
    print(evandro.__dict__)
    print(yanni.__dict__)
    del evandro.filhos
    print(evandro.__dict__)
    print(Pessoa.olhos)
    print(yanni.olhos)
    print(Pessoa.metodo_estatico())
    print(evandro.metodo_estatico())
    print(Pessoa.nome_atributo_classe())
    print(evandro.nome_atributo_classe())
