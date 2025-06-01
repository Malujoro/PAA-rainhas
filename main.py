from backtracking import *
from grafico import *


if (__name__ == '__main__'):
    n = 8

    tempo_comeco = time.perf_counter()
    existe, tabuleiro = rodar_n_rainhas(n)
    tempo_fim = time.perf_counter()

    if (not existe):
        print('A solução não existe!\n')

    tempo = tempo_fim - tempo_comeco

    Desenho().desenhar_tabuleiro(tabuleiro)
    
    print(f'Tempo de execucao: {tempo:.6f} segundos')
