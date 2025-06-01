import time
import random


def conflitos(queens_line, col, lin):
    '''Verifica a quantidade de conflitos de uma rainha'''
    quant = 0

    for i in range(col):
        if queens_line[i] == lin or abs(queens_line[i] - lin) == abs(i - col):
            quant += 1

    return quant


def simple_greedy(N):
    """
    Resolve o problema com a solução gulosa simples.
    Sempre posiciona a rainha na primeira posição com menos conflitos

    queens_lines[]: lista com as posições das linhas das rainhas (A coluna segue ordem crescente)
    min_conflitos: armazena a menor quantidade de conflitos de uma linha
    posicao: guarda a posição com menos conflitos em uma linha para o caso de não encontrar posição sem conflitos
    """
    queens_lines = [-1] * N

    for col in range(N):
        min_conflitos = float('inf')
        posicao = -1

        for lin in range(N):
            quant = conflitos(queens_lines, col, lin)

            if quant != 0:
                if quant < min_conflitos:
                    min_conflitos = quant
                    posicao = lin
            else:
                queens_lines[col] = lin
                break

        if queens_lines[col] == -1:
            queens_lines[col] = posicao

    return queens_lines

def random_greedy(N):
    """
    Resolve o problema com a solução gulosa aleatória.
    Posiciona a rainha em uma posição com menos conflitos.
    Decide aleatoriamente.

    queens_lines[]: lista com as posições das linhas das rainhas (A coluna segue ordem crescente)
    min_conflitos: armazena a menor quantidade de conflitos de uma linha
    melhores_posicoes: lista para as posições com menos conflitos em uma linha
    """
    queens_lines = [-1] * N

    for col in range(N):
        min_conflitos = float('inf')
        melhores_posicoes = []

        for lin in range(N):
            quant = conflitos(queens_lines, col, lin)

            if quant < min_conflitos:
                min_conflitos = quant
                melhores_posicoes = [lin]

            elif quant == min_conflitos:
                melhores_posicoes.append(lin)

        queens_lines[col] = random.choice(melhores_posicoes)

    return queens_lines


def analisa_conflitos(queens_lines, N):
    """
    Analise dos conflitos das rainhas

    Retorna dicionario com:
    - total_conflitos: número total de conflitos
    - rainhas_com_conflitos: quantidade de rainhas com conflitos
    - rainhas_conflitos_infos: lista com (posição(lin, col), quantidade de conflitos)
    - conflitos_por_tipo: quantidade de conflitos por linha e diagonal
    """
    resultado = {
        'total_conflitos': 0,
        'rainhas_com_conflitos': 0,
        'rainhas_conflitos_infos': [],
        'conflitos_por_tipo': {'linha': 0, 'diagonal': 0}
    }

    for col in range(N):
        lin = queens_lines[col]
        conflitos_dessa_rainha = 0

        for outras_col in range(N):
            if outras_col != col:
                outras_lin = queens_lines[outras_col]

                if outras_lin == lin:
                    conflitos_dessa_rainha += 1
                    resultado['conflitos_por_tipo']['linha'] += 1

                elif abs(outras_lin - lin) == abs(outras_col - col):
                    conflitos_dessa_rainha += 1
                    resultado['conflitos_por_tipo']['diagonal'] += 1

        if conflitos_dessa_rainha > 0:
            resultado['rainhas_conflitos_infos'].append(
                (lin, col, conflitos_dessa_rainha))
            resultado['rainhas_com_conflitos'] += 1

    resultado['total_conflitos'] = sum(
        resultado['conflitos_por_tipo'].values()) // 2
    resultado['conflitos_por_tipo']['linha'] //= 2
    resultado['conflitos_por_tipo']['diagonal'] //= 2

    return resultado


def exibir_resultado(resultado):
    """Exibe o resultado da análise de forma organizada"""
    print(f"\n📊 RESULTADO DA ANÁLISE:")
    print(f"   • Total de conflitos: {resultado['total_conflitos']}")
    print(f"   • Rainhas com conflito: {resultado['rainhas_com_conflitos']}")

    print(f"\n🔥 Conflitos por tipo:")
    print(f"   • Linha: {resultado['conflitos_por_tipo']['linha']}")
    print(f"   • Diagonal: {resultado['conflitos_por_tipo']['diagonal']}")

    if resultado['rainhas_conflitos_infos']:
        print(f"\n⚔️  Rainhas em conflito:")
        for lin, col, qtd in resultado['rainhas_conflitos_infos']:
            print(f"   • Posição ({lin}, {col}) - {qtd} conflito(s)")
    else:
        print(f"\n✅ Nenhuma rainha em conflito!")


def board(queens_lines, N):
    """Exibe o tabuleiro com as rainhas"""
    print(f"\n👑 Tabuleiro {N}x{N}:")
    print("  " + " ".join([str(i) for i in range(N)]))
    print("  " + "─" * (N * 2 - 1))

    for lin in range(N):
        linha = f"{lin}│"
        for col in range(N):
            if queens_lines[col] == lin:
                linha += "♛ "
            else:
                linha += "· "
        print(linha)

    print(f"\n Posições: {queens_lines}")


def converter_tabuleiro(N, queens_lines):
    tabuleiro = [[0] * N for _ in range(N)]

    for col in range(N):
        lin = queens_lines[col]
        tabuleiro[lin][col] = 1
    
    return tabuleiro


def executar_greedy_algorithm(N, analisar, greedy):
    """
    Executa a solução gulosa e monta a matriz do tabuleiro.
    Útil para gerar o gráfico

    Retorna o tabuleiro, o tempo de execução e o resultado da análise de conflito, se solicitado
    """
    tempo_inicio = time.perf_counter()
    queens_lines = greedy(N)
    tempo_fim = time.perf_counter()

    tempo = tempo_fim - tempo_inicio

    board(queens_lines, N)
    print()

    tabuleiro = converter_tabuleiro(N, queens_lines)

    if analisar:
        resultado = analisa_conflitos(queens_lines, N)
        return tabuleiro, tempo, resultado

    return tabuleiro, tempo


def testes():
    N = [4, 5, 6, 8]

    # Testes com solução gulosa simples:
    for i in range(len(N)):
        print("ALGORITMO GULOSO SIMPLES:")
        print(f"🧪 TESTE {i + 1}:")
        tempo_inicio = time.perf_counter()
        queens_lines_simple = simple_greedy(N[i])
        tempo_fim = time.perf_counter()

        tempo = tempo_fim - tempo_inicio

        board(queens_lines_simple, N[i])
        print()
        print(f"Tempo de execucao: {tempo:.6f} segundos")

        resultado = analisa_conflitos(queens_lines_simple, N[i])
        exibir_resultado(resultado)

        print("\n" + "=" * 50)

    # Testes com solução gulosa randômica:
    for i in range(len(N)):
        print("ALGORITMO GULOSO RANDÔMICO:")
        print(f"🧪 TESTE {i + 1}:")
        tempo_inicio = time.perf_counter()
        queens_lines_random = random_greedy(N[i])
        tempo_fim = time.perf_counter()

        tempo = tempo_fim - tempo_inicio

        board(queens_lines_random, N[i])
        print()
        print(f"Tempo de execucao: {tempo:.6f} segundos")

        resultado = analisa_conflitos(queens_lines_random, N[i])
        exibir_resultado(resultado)

        print("\n" + "=" * 50)


if __name__ == "__main__":
    # Executar a função testes:
    # testes()

    N = 4
    from grafico import Desenho

    desenho = Desenho(folder="greedy")
    funcoes = {"simples": simple_greedy, "randômico": random_greedy}

    for nome, func in funcoes.items():
        print(f"ALGORITMO GULOSO {nome.upper()}")
        analisa = True

        # Executar a função executar_greedy_algorithm:
        tabuleiro, tempo, resultado = executar_greedy_algorithm(
            N, analisa, func)
        
        for lin in tabuleiro:
            print(lin)
        print(f"\nTempo de execucao: {tempo:.6f} segundos")
        exibir_resultado(resultado)
        desenho.desenhar_tabuleiro(tabuleiro, show=True)
