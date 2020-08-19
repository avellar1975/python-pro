"""Módulo fase."""
# from itertools import chain
from atores import ATIVO


VITORIA = 'VITORIA'
DERROTA = 'DERROTA'
EM_ANDAMENTO = 'EM_ANDAMENTO'


class Ponto():
    """Classe Ponto()."""

    def __init__(self, x, y, caracter):
        """Método que inicializa um Ponto.

        :param x:
        :param y:
        :param caracter:
        """
        self.caracter = caracter
        self.x = round(x)
        self.y = round(y)

    def __eq__(self, other):
        """Método mágico."""
        sc = self.caracter
        return self.x == other.x and self.y == other.y and sc == other.caracter

    def __hash__(self):
        """Método mágico."""
        return hash(self.x) ^ hash(self.y)

    def __repr__(self, *args, **kwargs):
        """Representação do Ponto."""
        return "Ponto(%s,%s,'%s')" % (self.x, self.y, self.caracter)


class Fase():
    """Classe Fase()."""

    def __init__(self, intervalo_de_colisao=1):
        """Método que inicializa uma fase.

        :param intervalo_de_colisao:
        """
        self.intervalo_de_colisao = intervalo_de_colisao
        self._passaros = []
        self._porcos = []
        self._obstaculos = []

    def adicionar_obstaculo(self, *obstaculos):
        """
        Adiciona obstáculos em uma fase.

        :param obstaculos:
        """
        for obs in obstaculos:
            self._obstaculos.append(obs)

    def adicionar_porco(self, *porcos):
        """
        Adiciona porcos em uma fase.

        :param porcos:
        """
        for porco in porcos:
            self._porcos.append(porco)

    def adicionar_passaro(self, *passaros):
        """
        Adiciona pássaros em uma fase.

        :param passaros:
        """
        for birdo in passaros:
            self._passaros.append(birdo)

    def status(self):
        """
        Método que indica com mensagem o status do jogo.

        Se o jogo está em andamento (ainda tem porco ativo e pássaro ativo),
        retorna essa mensagem.

        Se o jogo acabou com derrota (ainda existe porco ativo), retorna essa
        mensagem

        Se o jogo acabou com vitória (não existe porco ativo), retorna essa
        mensagem

        :return:
        """
        po = 'inativo'
        pa = 'inativo'

        for porco in self._porcos:
            if porco.status == ATIVO:
                po = 'ativo'
        for passaro in self._passaros:
            if passaro.status == ATIVO:
                pa = 'ativo'
        if pa == 'ativo' and po == 'ativo':
            return EM_ANDAMENTO
        elif pa == 'ativo' and po == 'inativo':
            return VITORIA
        elif pa == 'inativo' and po == 'ativo':
            return DERROTA
        else:
            return VITORIA

    def lancar(self, angulo, tempo):
        """
        Método que executa lógica de lançamento.

        Deve escolher o primeiro pássaro não lançado da lista e chamar seu
        método lançar

        Se não houver esse tipo de pássaro, não deve fazer nada

        :param angulo: ângulo de lançamento
        :param tempo: Tempo de lançamento
        """
        for passaro in self._passaros:
            if not passaro.foi_lancado():
                passaro.lancar(angulo, tempo)
                return

    def calcular_pontos(self, tempo):
        """
        Lógica que retorna os pontos a serem exibidos na tela.

        Cada ator deve ser transformado em um Ponto.

        :param tempo: tempo para o qual devem ser calculados os pontos
        :return: objeto do tipo Ponto
        """
        for passaro in self._passaros:
            passaro.calcular_posicao(tempo)
            for alvo in self._obstaculos + self._porcos:
                passaro.colidir(alvo, self.intervalo_de_colisao)
            passaro.colidir_com_chao()

        pontos = [
            self._transformar_em_ponto(a)
            for a in self._passaros + self._obstaculos + self._porcos
            ]

        return pontos

    def _transformar_em_ponto(self, ator):
        return Ponto(ator.x, ator.y, ator.caracter())
