"""Exercício carro."""


class Motor:
    """
    Testes da Classe Motor.

    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    2
    >>> motor.frear()
    >>> motor.velocidade
    1
    """

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'


class Direcao:
    """Testando Direcao.

    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    """

    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_direita(self):
        rotacionar_direita = {
            NORTE: LESTE,
            LESTE: SUL,
            SUL: OESTE,
            OESTE: NORTE
        }
        self.valor = rotacionar_direita[self.valor]

    def girar_a_esquerda(self):
        rotacionar_esqueda = {
            NORTE: OESTE,
            LESTE: NORTE,
            SUL: LESTE,
            OESTE: SUL
        }
        self.valor = rotacionar_esqueda[self.valor]


class Carro:
    """Testes da Classe Carro.
    >>> motor = Motor()
    >>> direcao = Direcao()
    >>> carro = Carro(motor, direcao)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    1
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    """

    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()
