'''

Exercício: Validação de dados
Abra o programa que calcula a média e imprime a situação do aluno, feito no exercício sobre condicionais. Aplique a validação de dados para que:
- O programa nunca seja interrompido por erro
- A nota seja entre 0 e 10
O número de faltas seja entre 0 e 20

'''                                                 #Requisitos para passar:
                                                    #Média: 6,0
                                                    #Assiduidade 70% (De 20 aulas, precisa de no mínimo 14 presenças.)

#Loop para reiniciar o programa:
reset_program = False
while reset_program == False:

    print("\n<<< PROGRAMA DE CÁLCULO DE MÉDIA E ASSIDUIDADE >>>")

    #Validando a entrada do nome do aluno:
    valid_nome = False
    while valid_nome == False:
        nome = input("\nDigite o nome do aluno: ")
        try:
            nome = (str(nome)).title()
            if len(nome) < 1 or len(nome) > 50:
                print("Escreva um nome de 1 a 50 caracteres.")
            else:
                valid_nome = True
        except:
            print("Escreva o nome em um formato válido.")

    #Validando a nota da prova 1:
    valid_nota1 = False
    while valid_nota1 == False:
        nota_prova1 = input("Digite a nota da primeira prova: ")
        try:
            nota_prova1 = float(nota_prova1)
            if nota_prova1 < 0.0 or nota_prova1 > 10.0:
                print("Digite um valor de 0 a 10.")
            else:
                valid_nota1 = True
        except:
            print("Formato inválido. Utilize números e separe com ponto. [Ex.:10.0].")

    #Validando a nota da prova 2:
    valid_nota2 = False
    while valid_nota2 == False:
        nota_prova2 = input("Digite a nota da segunda prova: ")
        try:
            nota_prova2 = float(nota_prova2)
            if nota_prova2 < 0.0 or nota_prova2 > 10.0:
                print("Digite um valor de 0 a 10.")
            else:
                valid_nota2 = True
        except:
            print("Formato inválido. Utilize números e separe com ponto. [Ex.:10.0].")

    # Validando as faltas:
    valid_faltas = False
    while valid_faltas == False:
        faltas = input(f"Digite a quantidade de faltas do aluno {nome}: ")
        try:
            faltas = int(faltas)
            if faltas < 0 or faltas > 20:
                print("Digite um valor de 0 a 20.")
            else:
                valid_faltas = True
        except:
            print("Formato inválido. Utilize números inteiros. [Ex.:5].")

    #Calculando a média e assiduidade:
    media = float((nota_prova1 + nota_prova2) / 2)
    assiduidade = (100 - (faltas * 100) / 20)

    #Verificando se aluno foi reprovado ou aprovado:
    if media < 6.0 and assiduidade < 70.0:
        print(f"\nAluno: {nome}")
        print(f"Média: {media}")
        print(f"Assiduidade: {assiduidade}%")
        print(f"O aluno {nome} foi REPROVADO.")
        print("Motivo: Excedeu o número de faltas e também sua nota ficou abaixo de 6.0.")

    elif media < 6.0:
        print(f"\nAluno: {nome}")
        print(f"Média: {media}")
        print(f"Assiduidade: {assiduidade}%")
        print(f"O aluno {nome} foi REPROVADO.")
        print("Motivo: Sua nota ficou abaixo de 6.0")

    elif assiduidade < 70.0:
        print(f"\nAluno: {nome}")
        print(f"Média: {media}")
        print(f"Assiduidade: {assiduidade}%")
        print(f"O aluno {nome} foi REPROVADO.")
        print("Motivo: Excedeu o número de faltas. A assiduidade mínima para aprovação é de 70%.")

    elif media >= 6.0 and assiduidade >= 70.0:
        print(f"\nAluno: {nome}")
        print(f"Média: {media}")
        print(f"Assiduidade: {assiduidade}%")
        print(f"O(A) aluno(a) {nome} foi APROVADO(A)!")
        print("PARABÉNS!")

    else:
        print("ERRO. Procure a Equipe de Análise de Software.")

    #Validação do input de reinício de programa:
    valid_reset = False
    while valid_reset == False:
        reset = input("Deseja reiniciar o programa? [s/n]: ")
        try:
            reset = (str(reset)).lower()
            if reset == 's':
                valid_reset = True

            elif reset == 'n':
                valid_reset = True
                reset_program = True    #Alterando o valor do primeiro loop do programa para True para finalizar o programa.

            else:
                print("Digite [s] para SIM e [n] para NÃO."
                      )
        except:
            print("Caractere inválido. Digite [s] ou [n].")

print("Fim do Programa.")




