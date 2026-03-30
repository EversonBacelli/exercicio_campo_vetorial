
def criar_matriz():
    n = 4  # Tamanho da matriz (5x5)
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    matriz[0][0] = 7
    matriz[0][1] = 5
    matriz[0][2] = 3
    matriz[0][3] = 2        
    matriz[1][0] = 0
    matriz[1][1] = 0
    matriz[1][2] = 1
    matriz[1][3] = 4
    matriz[2][0] = 3
    matriz[2][1] = 2
    matriz[2][2] = 1
    matriz[2][3] = 0
    matriz[3][0] = 4
    matriz[3][1] = 3
    matriz[3][2] = 2
    matriz[3][3] = 1  
    return matriz