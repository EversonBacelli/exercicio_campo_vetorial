import sys
import os

caminho_da_lib = os.path.join(os.getcwd(), 'grafos')
sys.path.append(caminho_da_lib)

from matriz_origem import criar_matriz
from Vertice import Vertice

matriz = criar_matriz()
Vertice.MATRIZ = matriz

def gerarGrafo():
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            Vertice(matriz[linha][coluna], (linha, coluna))
    
    return Vertice.VERTICES, Vertice 
