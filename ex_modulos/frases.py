
frases = {
    1: "A jornada de mil milhas começa com um único passo.",
    2: "O sucesso é a soma de pequenos esforços repetidos.",
    3: "Errar é humano, persistir é sabedoria.",
    4: "O conhecimento é a única riqueza que ninguém pode te tirar.",
    5: "Pequenos passos todos os dias levam a grandes distâncias."
}

def mostra_frases():
    for key, value in frases.items():
        print(f"[{key}] - {value}")


def escolhe_frase():
    while True:
        frase_definida = input("\nEscolha o número correspondente à frase escolhida: ")  # Faça validação de entrada neste input:
        try:
            frase_definida = int(frase_definida)
            if frase_definida in [1, 2, 3, 4, 5, 6]:  # Será que funciona if frase_definida in frases:   ??? [RETIRE O 6 DEPOIS DO TESTE]
                break
            else:
                print("Escolha a sua frase [0 - 5]: ")
                mostra_frases()
        except:
            print("Caractere inválido. Escolha uma frase [0 - 5]: ")
            mostra_frases()
    return frases[frase_definida]




'''
while True:
    frase_definida = input("Escolha o número correspondente à frase escolhida: ")  # Faça validação de entrada neste input:
    try:
        frase_definida = int(frase_definida)
        if frase_definida in [1,2,3,4,5]: #Será que funciona if frase_definida in frases:   ???
            break
        else:
            print("Escolha a sua frase [0 - 5]: ")
            fr.mostra_frases()
    except:
        print("Caractere inválido. Escolha uma frase [0 - 5]: ")
        fr.mostra_frases()
'''

# print("[1] - Um hacker experiente vale mais que 1000 soldados na linha de frente da guerra.\n")
# print("[2] - All Star cano médio é o tênis mais maneiro que existe na face da terra..\n")
# print("[3] - Qual guitarra você prefere? Gibson Les Paul ou Fender Stratocaster?\n")
# print("[4] - Quando você viajar para o Amazonas, deverász comer um tambaqui assado.\n")
# print("[5] - Ave Maria! Cheia de Graça! O Senhor é convosco. Bendita sois vós entre as mulheres...\n")