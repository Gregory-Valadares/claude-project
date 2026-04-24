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

def imc(peso, altura):
    valor_imc = peso / (altura * altura)
    return round(valor_imc, 2)