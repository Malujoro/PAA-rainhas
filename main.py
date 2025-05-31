from backtracking import *
import matplotlib.pyplot as plt
import numpy as np

def desenhar_tabuleiro(matriz):
    n = len(matriz)

    _, ax = plt.subplots()
    tabuleiro = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            # Padrão de xadrez
            tabuleiro[i, j] = (i + j) % 2

    
    ax.imshow(tabuleiro, cmap="gray", extent=[0, n, 0, n])

    for i in range(n):
        for j in range(n):
            if(matriz[i][j]):
                ax.text(j + 0.5, n - i - 0.5, '♛', ha='center', va='center', fontsize=24, color='red')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_aspect('equal')
    plt.show()



if (__name__ == '__main__'):
    n = 8

    tempo_comeco = time.perf_counter()
    existe, tabuleiro = rodar_n_rainhas(n)
    tempo_fim = time.perf_counter()

    if(not existe):
        print('A solução não existe!\n')

    tempo = tempo_fim - tempo_comeco

    desenhar_tabuleiro(tabuleiro)
    print(f'Tempo de execucao: {tempo:.6f} segundos')
