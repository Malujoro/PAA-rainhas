from backtracking import *
from greedy import *
from grafico import *
import time
import csv
import tracemalloc

def linha(char: str = "=", tam: int = 70):
    print(char * tam)


with open("tempos_rainhas.csv", mode="w", newline="") as arquivoCSV:
    writer = csv.writer(arquivoCSV)
    writer.writerow(["rainhas", "algoritmo", "iteracao", "tempo", "memoria_pico_kb",
                    "total_conflitos", "rainhas_conflitos", "conflitos_linha", "conflitos_diagonais",])

    random.seed(2025)
    iteracoes = 30
    lista_rainhas = [10, 25, 26, 100, 250]
    limite_backtracking = lista_rainhas[2]
    desenho = Desenho(folder="imagens")

    for rainha in lista_rainhas:
        linha()
        for funcao in [backtracking, simple_greedy, random_greedy]:
            # Evita aplicar backtracking em siutações elevadas
            if (funcao == backtracking and rainha > limite_backtracking):
                continue

            tabuleiro = funcao(rainha)

            print(
                f"{rainha} RAINHAS DE FORMA [{(funcao.__name__).upper()}]")

            # Ajusta o retorno para os gulosos
            resultado = {}
            if (funcao != backtracking):
                resultado = analisa_conflitos(tabuleiro, rainha)

                print()
                tabuleiro = converter_tabuleiro(rainha, tabuleiro)

            desenho.desenhar_tabuleiro(tabuleiro)

            for it in range(iteracoes):
                tracemalloc.start()
                tracemalloc.reset_peak()
                inicio = time.perf_counter()

                funcao(rainha)

                fim = time.perf_counter()
                memoria_atual_b, memoria_pico_b = tracemalloc.get_traced_memory()
                tracemalloc.stop()

                tempo = fim - inicio

                csv_tempo = f"{tempo:.6f}"
                csv_memoria_pico = f"{memoria_pico_b / 1024:.2f}"

                if (resultado):
                    csv_total_conflitos = resultado['total_conflitos']
                    csv_rainhas_conflitos = resultado['rainhas_com_conflitos']
                    csv_conflitos_linha = resultado['conflitos_por_tipo']['linha']
                    csv_conflitos_diagonais = resultado['conflitos_por_tipo']['diagonal']
                else:
                    csv_total_conflitos = 0
                    csv_rainhas_conflitos = 0
                    csv_conflitos_linha = 0
                    csv_conflitos_diagonais = 0

                print(
                    f"[{it + 1}ª Iteração] {csv_tempo} segundos, com pico de {csv_memoria_pico} bytes | [Conflitos] Total: {csv_total_conflitos}, Rainhas: {csv_rainhas_conflitos}, Linhas: {csv_conflitos_linha}, Diagonais: {csv_conflitos_diagonais}")

                writer.writerow(
                    [rainha, funcao.__name__, it + 1, csv_tempo, csv_memoria_pico, csv_total_conflitos, csv_rainhas_conflitos, csv_conflitos_linha, csv_conflitos_diagonais])
            linha(char="-", tam=60)
