"""Estudo de Classes e Objetos."""


class Cachorro():
    """Classe cachorro."""

    def __init__(self, nome, *filhotes):
        """Define o atributo nome do objeto."""
        self.nome = nome
        self.filhotes = list(filhotes)

    def __repr__(self):
        """Representação do objeto."""
        return f'Cachorro({self.nome!r})'

    def __str__(self):
        """Imprime o nome do objeto."""
        return f'Cachorro: {self.nome}'


if __name__ == "__main__":
    rex = Cachorro('Rex', 'junior', 'dama')
    print(type(rex))
    print(rex)
    toto = Cachorro('Totó', rex)
    print(type(toto))
    print(toto)
