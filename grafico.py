import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patheffects as path_effects
import numpy as np
import os


class Desenho:

    def __init__(self, folder="frames"):
        self._frame_id_global = 0
        self._folder = folder
        os.makedirs(folder, exist_ok=True)

    def converte_coordenadas(self, n, lin, col):
        y = n - lin - 0.5
        x = col + 0.5

        return x, y

    def remover_linhas(self, linhas_ataque):
        for l in linhas_ataque:
            l.remove()
        linhas_ataque.clear()

    def desenhar_tabuleiro(self, matriz, show=False):
        n = len(matriz)

        fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
        ax.set_position([0, 0, 1, 1])
        tabuleiro = np.zeros((n, n))

        for i in range(n):
            for j in range(n):
                # Padrão de xadrez
                tabuleiro[i, j] = (i + j) % 2

        cmap = ListedColormap(['#f0d9b5', '#b58863'])
        ax.imshow(tabuleiro, cmap=cmap, extent=[0, n, 0, n])
        rainhas = []

        # Desenha as rainhas
        for i in range(n):
            for j in range(n):
                if (matriz[i][j]):
                    x, y = self.converte_coordenadas(n, i, j)
                    rainhas.append((j, i))
                    texto = ax.text(x, y, '♛', ha='center', va='center',
                                    fontsize=36, color='crimson')
                    texto.set_path_effects([
                        path_effects.Stroke(linewidth=2, foreground='black'),
                        path_effects.Normal(),
                    ])

        linhas_ataque = []

        def desenhar_ataques(self, col, lin):
            # Remover linhas existentes
            self.remover_linhas(linhas_ataque)

            # Desenhar 8 direções
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                x, y = col, lin
                while 0 <= x + dx < n and 0 <= y + dy < n:
                    x += dx
                    y += dy
                    # Conversão para coordenadas do gráfico
                    col_plot, lin_plot = self.converte_coordenadas(n, y, x)
                    linha, = ax.plot([col + 0.5, col_plot],
                                     [n - lin - 0.5, lin_plot], color='deepskyblue', linestyle='--', linewidth=3)
                    linhas_ataque.append(linha)

            fig.canvas.draw_idle()

        def on_click(event):
            if event.inaxes != ax:
                return
            col = int(event.xdata)
            lin = n - int(event.ydata) - 1

            if (col, lin) in rainhas:
                desenhar_ataques(col, lin)
            else:
                # Remove linhas ao clicar fora da rainha
                self.remover_linhas(linhas_ataque)
                fig.canvas.draw_idle()

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(0, n)
        ax.set_ylim(0, n)
        ax.set_aspect('equal')

        fig.canvas.mpl_connect('button_press_event', on_click)

        self._frame_id_global += 1
        plt.savefig(
            f"{self._folder}/frame_{self._frame_id_global:03d}.png", bbox_inches="tight")

        if (show):
            plt.show()
        else:
            plt.close(fig)
