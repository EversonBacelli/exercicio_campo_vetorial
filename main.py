
from grafos.grafo import gerarGrafo
from grafos.Vertice import Vertice

matriz = gerarGrafo()

for linha in matriz:
    print(linha.valor,'  ', linha.distancia ,' ', linha.vizinhos)