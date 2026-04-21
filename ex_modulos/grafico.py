import matplotlib.pyplot as plt

def plotar_grafico(tempos):

    lista_tempos = list(tempos.values())
    lista_voltas = list(tempos.keys())

    plt.plot(lista_voltas, lista_tempos)
    plt.xlabel("Voltas digitadas")
    plt.ylabel("Tempo (s)")
    plt.title("Gráfico de Tempo Gasto por frase")
    plt.tight_layout()
    plt.show()