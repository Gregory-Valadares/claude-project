'''
Exercício: Funções
Faça um programa que receba o sexo, peso e altura do usuário e em seguida apresente:
- IMC (Índice de massa corporal)
- Classificação do IMC baseado na seguinte tabela:

Condição                Abaixo do peso      Peso normal     Marginalmente acima do peso     Acima do peso ideal      Obesidade
IMC em Mulheres [F]      < 19,1              19,1-25,8       25,8-27,3                       27,3-32,3               > 32,3
IMC em Homens [M]        < 20,7              20.7-26.4       26,4-27,8                       27.8-31,1               > 31.1

-Use funções para fazer os cálculos e não esqueça de validar os inputs.
'''

condicoes = ("Abaixo do peso", "Peso normal", "Marginalmente acima do peso", "Acima do peso ideal", "Obesidade")

def condicao(imc, sexo):
    if sexo == 'm':
        if imc < 20.7:
            print(f"\nRESULTADO: {imc} {condicoes[0]}.")
            return condicoes[0]

        elif 20.7 <= imc < 26.4:
            print(f"\nRESULTADO: {imc} {condicoes[1]}.")
            return condicoes[1]

        elif 26.4 <= imc < 27.8:
            print(f"\nRESULTADO: {imc} {condicoes[2]}.")
            return condicoes[2]

        elif 27.8 <= imc < 31.1:
            print(f"\nRESULTADO: {imc} {condicoes[3]}.")
            return condicoes[3]

        elif imc >= 31.1:
            print(f"\nRESULTADO: {imc} {condicoes[4]}.")
            return condicoes[4]

        else:
            print("ERRO")

    elif sexo == 'f':
        if imc < 19.1:
            print(f"\nRESULTADO: {imc} {condicoes[0]}.")
            return condicoes[0]

        elif 19.1 <= imc < 25.8:
            print(f"\nRESULTADO: {imc} {condicoes[1]}.")
            return condicoes[1]

        elif 25.8 <= imc < 27.3:
            print(f"\nRESULTADO: {imc} {condicoes[2]}.")
            return condicoes[2]

        elif 27.3 <= imc < 32.3:
            print(f"\nRESULTADO: {imc} {condicoes[3]}.")
            return condicoes[3]

        elif imc >= 32.3:
            print(f"\nRESULTADO: {imc} {condicoes[4]}.")
            return condicoes[4]

        else:
            print("ERRO")

    else:
        print("ERRO. Suposto erro na entrada do sexo.")