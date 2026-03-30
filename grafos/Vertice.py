class Vertice:
    VERTICES = []
    MATRIZ = []
    def __init__(self, valor, posicao):
        self.valor = valor
        self.visitado = False
        self.vizinhos = []
        self.posicaoVizinhos(posicao)
        Vertice.VERTICES.append(self)
        self.distancia = self.distancia(posicao, [3,3])

    def posicaoVizinhos(self, posicao):
        # direita
        if posicao[0] < len(Vertice.MATRIZ[0]) - 1:
            if Vertice.podarGalhos(self.valor, Vertice.MATRIZ[posicao[1]][posicao[0] + 1]):
                self.vizinhos.append((posicao[0] + 1, posicao[1]))
        # baixo
        if posicao[1] < len(Vertice.MATRIZ) - 1:
            if Vertice.podarGalhos(self.valor, Vertice.MATRIZ[posicao[1] + 1][posicao[0]]):
                self.vizinhos.append((posicao[0], posicao[1] + 1))
        # esquerda
        if posicao[0] > 0:
            if Vertice.podarGalhos(self.valor, Vertice.MATRIZ[posicao[1]][posicao[0] - 1]):
                self.vizinhos.append((posicao[0] - 1, posicao[1]))
        # cima
        if posicao[1] > 0:
            if Vertice.podarGalhos(self.valor, Vertice.MATRIZ[posicao[1] - 1][posicao[0]]):
                self.vizinhos.append((posicao[0], posicao[1] - 1))

    def podarGalhos(valor1, valor2):
        diferenca = abs(valor1 - valor2)
        if diferenca < 3:
            return True
        return False
    
    def distancia(self, posicao, alvo):
        return abs(posicao[0] - alvo[0]) + abs(posicao[1] - alvo[1])