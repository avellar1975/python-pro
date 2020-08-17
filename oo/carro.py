"""Exercício carro."""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
        return self.velocidade

    def frear(self):
        self.velocidade -= 1
        return self.velocidade


class Direcao:
    def __init__(self, valor='norte'):
        self.valor = valor

    def girar_a_direita(self):
        if self.valor == 'norte':
            self.valor = 'leste'
        elif self.valor == 'leste':
            self.valor = 'sul'
        elif self.valor == 'sul':
            self.valor = 'oeste'
        else:
            self.valor = 'norte'
        return self.valor

    def girar_a_esquerda(self):
        if self.valor == 'norte':
            self.valor = 'oeste'
        elif self.valor == 'oeste':
            self.valor = 'sul'
        elif self.valor == 'sul':
            self.valor = 'leste'
        else:
            self.valor = 'norte'
        return self.valor


class Carro:

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


"""
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
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
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
    'Norte'
    >>> carro = Carro(direcao, motor)
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
    0
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
# Testando
if __name__ == '__main__':
    motor = Motor()
    motor.velocidade
    motor.acelerar()
    motor.acelerar()
    direcao = Direcao()
