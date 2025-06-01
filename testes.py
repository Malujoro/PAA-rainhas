from backtracking import *
from greedy import *
from grafico import *
import time
import csv
import tracemalloc


# if (__name__ == '__main__'):
#     n = 8

#     tempo_comeco = time.perf_counter()
#     existe, tabuleiro = rodar_n_rainhas(n)
#     tempo_fim = time.perf_counter()

#     if (not existe):
#         print('A solução não existe!\n')

#     tempo = tempo_fim - tempo_comeco

#     Desenho().desenhar_tabuleiro(tabuleiro, show=True)

#     print(f'Tempo de execucao: {tempo:.6f} segundos')


def linha(char: str = "=", tam: int = 70):
    print(char * tam)


with open("tempos_rainhas.csv", mode="w", newline="") as arquivoCSV:
    writer = csv.writer(arquivoCSV)
    writer.writerow(["rainhas", "algoritmo", "iteracao",
                    "tempo", "memoria_pico_b"])

    random.seed(2025)
    iteracoes = 30
    lista_rainhas = [10, 25, 26, 100, 1000]
    limite_backtracking = lista_rainhas[2]
    desenho = Desenho(folder="imagens")

    for rainha in lista_rainhas:
        linha()
        for funcao in [backtracking, simple_greedy, random_greedy]:
            tabuleiro = funcao(rainha)

            # Ajusta o retorno para os gulosos
            if (funcao != backtracking):
                tabuleiro = converter_tabuleiro(rainha, tabuleiro)

            desenho.desenhar_tabuleiro(tabuleiro)

            if (funcao != backtracking or (funcao == backtracking and rainha <= limite_backtracking)):
                print(
                    f"{rainha} RAINHAS DE FORMA [{(funcao.__name__).upper()}]")
                for it in range(iteracoes):
                    tracemalloc.start()
                    tracemalloc.reset_peak()
                    inicio = time.perf_counter()

                    funcao(rainha)

                    fim = time.perf_counter()
                    memoria_atual_b, memoria_pico_b = tracemalloc.get_traced_memory()
                    tracemalloc.stop()

                    tempo = fim - inicio
                    print(
                        f"[{it + 1}ª Iteração] {tempo:.6f} segundos, com pico de {memoria_pico_b:.2f} bytes")
                    writer.writerow(
                        [rainha, funcao.__name__, it + 1, f"{tempo:.6f}", f"{memoria_pico_b:.2f}"])
                linha(char="-", tam=60)
