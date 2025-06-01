import time

# Mostrar a solução
def p_solucao(tabuleiro):
    for l in tabuleiro:
        print(''.join('R ' if i else '- ' for i in l))

    # print()
    # time.sleep(0.2)
    
    # desenho.desenhar_tabuleiro(tabuleiro)

# Função para verificar posição da rainha
def safe(tabuleiro, linha, coluna, n):
    # Colunas da esquerda
    for i in range(coluna):
        if tabuleiro[linha][i] == 1:
            return False

    # Diagonal superior a esquerda
    for i, j in zip(range(linha, -1, -1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    # Diagonal inferior a esquerda
    for i, j in zip(range(linha, n, 1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 1:
            return False

    return True

def recursao(tabuleiro, coluna, n):
    # Caso base
    if coluna >= n:
        return True
    
    # Tentativa de colocar a rainha em todas as linhas
    for i in range(n):
        if safe(tabuleiro, i, coluna, n):
            tabuleiro[i][coluna] = 1
            # p_solucao(tabuleiro)

            if recursao(tabuleiro, coluna + 1, n) == True:
                # p_solucao(tabuleiro)
                return True

            # Se não levar a uma solução então volta (backtracking)
            tabuleiro[i][coluna] = 0
            # p_solucao(tabuleiro)

    # Se não foi colocada em nenhuma linha da coluna
    return False

def rodar_n_rainhas(n):
    tabuleiro = [[0] * n for _ in range(n)]

    if not recursao(tabuleiro, 0, n):
        return False, []

    return True, tabuleiro


if (__name__ == '__main__'):
    from grafico import Desenho
    n = 8

    desenho = Desenho()
    tempo_comeco = time.perf_counter()
    existe, tabuleiro = rodar_n_rainhas(n)
    tempo_fim = time.perf_counter()

    if(not existe):
        print('A solução não existe!\n')

    tempo = tempo_fim - tempo_comeco

    p_solucao(tabuleiro)
    print(f'Tempo de execucao: {tempo:.6f} segundos')
