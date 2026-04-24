'''
Exercício: Módulos
Usando o módulo Time (Built-in) e o Matplotlib (Externo),
faça um programa que pede que o usuário digite uma palavra 5 vezes seguidas.
Conte o tempo que ele leva para digitar a palavra a cada repetição e
ao final gere um gráfico com os tempos, como no exemplo da aula da Udemy.
'''
import time
import frases as fr
import grafico as gr
import tempos as tp
#import matplotlib.pyplot as plt

#Apresenta o nome do programa e manda o usuário escolher um dos textos:
print("\n\n\n<<<PROGRAMA - GRÁFICO DE TEMPO DE DIGITAÇÃO>>>\n Escolha um dos textos para escrever 5 vezes:\n")

#Mostrando as frases disponíveis:
fr.mostra_frases()

#Dá a oportunidade para o usuário escolher a frase:
frase_definida = fr.escolhe_frase()

#Pergunta se o usuário está pronto. Se sim, tecle ENTER:
input(f"Esta é sua frase: {frase_definida}\nEstá pronto? Tecle ENTER para começar: ")

#Manda o usuário escrever 5 vezes a frase escolhida pegando o tempo gasto em cada digitação correta da frase:
tempos_dic = tp.pega_tempos(frase_definida)


#Mostra o gráfico com os tempos:
#crie uma função que mostre o gráfico
gr.plotar_grafico(tempos_dic)