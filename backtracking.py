import time

x = 8
tabuleiro = [[0] * x for _ in range(x)]

#mostrar a solucao
def p_solucao(tabuleiro):
    for l in tabuleiro:
        print(''.join('R ' if x else '- ' for x in l))

#funcao para verificar posicao da rainha
def safe(tabuleiro,l,c):
    #coluna a esquerda
    for i in range(c):
        if tabuleiro[l][i] == 1:
            return False
    #diagonal superior a esquerda
    for i, j in zip(range(l,-1,-1), range(c,-1,-1)):
        if tabuleiro[i][j] == 1:
            return False
    #diagonal inferior a esquerda
    for i, j in zip(range(l,x,1), range(c,-1,-1)):
        if tabuleiro[i][j] == 1:
            return False
        
    return True

def recursao(tabuleiro,c):
    #caso base
    if c >= x:
        return True
    #tentativa de colocar a rainha em todas as linhas
    for i in range(x):
        if safe(tabuleiro,i,c):
            tabuleiro[i][c]= 1
            
            if recursao(tabuleiro,c+1) == True:
                return True
            
            #se nao levar a uma solucao entao volta(backtracking)
            tabuleiro[i][c] = 0
            
    #se nao foi colocada em nenhuma linha da coluna
    return False

def roda():
    if not recursao(tabuleiro,0):
        print('A solucao nao existe!\n')
        return False
    p_solucao(tabuleiro)
    return True
tempo_comeco = time.perf_counter()         
roda()
tempo_fim = time.perf_counter()

tempo = tempo_fim - tempo_comeco
print(f'tempo de execucao: {tempo:.6f} segundos')