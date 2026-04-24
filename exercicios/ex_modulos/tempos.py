import time

def pega_tempos(frase_definida): #Função com 3 objetivos: 1- Mostrar a frase escolhida. 2- Mandar o usuário digitar 5 vezes, 3 - Pegar os tempos
    tempos_dic = {}
    for i in range(5):
        inicio_tempo = time.perf_counter()
        while True: #Faça uma validação se o usuário escreveu a palavra corretamente. Se não, mande-o escrever novamente até acertar.
            frase_digitada = input("ESCREVA: ")
            if frase_digitada == frase_definida:
                break
            else:
                print("ERRO! Escreva corretamente.")

        fim_tempo = time.perf_counter()
        tempo_gasto = fim_tempo - inicio_tempo
        print(f"FRASE {i+1} - Tempo: {tempo_gasto} segundos")
        tempos_dic[i+1] = round(tempo_gasto, 2)
        i += 1
    return tempos_dic