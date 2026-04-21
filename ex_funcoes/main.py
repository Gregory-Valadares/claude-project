'''
Exercício: Funções
Faça um programa que receba o sexo, peso e altura do usuário e em seguida apresente:
- IMC (Índice de massa corporal)
- Classificação do IMC baseado na seguinte tabela:

Condição                abaixo do peso      peso normal     marginalmente acima do peso     acima do peso ideal     obeso
IMC em Mulheres         < 19,1              19,1-25,8       25,8-27,3                       27,3-32,3               > 32,3
IMC em Homens           < 20,7              20.7-26.4       26,4-27,8                       27.8-31,1               > 31.1

-Use funções para fazer os cálculos e não esqueça de validar os inputs.
'''
#Importando funções.
from calculo_imc import imc
from condicao_imc import condicao

#Loop para reset do programa até que o usuário decida fechar no final.
reset_program = True
while reset_program == True:

    #Iniciando o programa.
    print("\n<<< PROGRAMA DE CÁLCULO DE IMC >>>\n")

    #Validando a entrada do sexo.
    while True:
        sexo = input("Digite seu gênero (M/F): ")
        try:
            sexo = str(sexo).lower()
            if sexo == 'm' or sexo == 'f':
                break
            else:
                print("Digite 'M' para Macho e 'F' para Fêmea.")
        except:
            print("Caractere inválido. Digite 'M' para Macho e 'F' para Fêmea.")

    #Validando a entrada do peso.
    while True:
        peso = input("Digite seu peso em kg [Ex.: 75.5]: ")
        try:
            peso = float(peso)
            if peso >= 0.0 and peso <= 1000.0:
                break
            else:
                print("Digite um peso entre 0 e 1000.")
        except:
            print("Caractere inválido. Digite um número entre 0 e 1000 no seguinte formato: [75.5].")

    #Validando a entrada da altura.
    while True:
        altura = input("Digite sua altura, em metros, no formato [Ex.: 1.75]: ")
        try:
            altura = float(altura)
            if altura >= 0.0 and altura <= 3.00:
                break
            else:
                print("Digite um altura entre 0 e 3.00.")
        except:
            print("Caractere inválido. Digite um altura entre 0 e 3.00 no seguinte formato: [1.75].")

    #Utilizando as funções para definir os valores do IMC e a condição.
    valor_imc = (imc(peso, altura))
    print(condicao(valor_imc, sexo))

    #Validação de dados da decisão do usuário, se deseja reiniciar o programa.
    while True:
        reset_decision = input("Deseja reiniciar o programa? [S/N]: ")
        try:
            reset_decision = str(reset_decision)
            if reset_decision == 's':
                break

            elif reset_decision == 'n':
                reset_program = False
                break

            else:
                print("Digite 's' para SIM e 'n' para NÃO.")

        except:
            print("Caractere inválido. Digite 's' para SIM e 'n' para NÃO.")

print("\nPrograma finalizado com sucesso!")









