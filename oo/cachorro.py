"""Estudo de Classes e Objetos."""


class Cachorro():
    """Classe cachorro."""

    olhos = 2

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


class Fila(Cachorro):
    """Classe Fila que herda da classe Cachorro."""

    def __repr__(self):
        """Representação do objeto."""
        return f'Fila({self.nome!r})'

    def __str__(self):
        """Imprime o nome do objeto."""
        return f'Fila: {self.nome}'


if __name__ == "__main__":
    rex = Cachorro('Rex', 'junior', 'dama')
    print(type(rex))
    print(rex)
    toto = Fila('Totó', rex)
    print(type(toto))
    print(toto)
    print(toto.olhos)
