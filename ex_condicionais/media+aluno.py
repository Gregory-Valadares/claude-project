'''

Exercício: If
1) Peça ao usuário as seguintes informações sobre um aluno:
Nome
Nota prova 1
Nota prova 2
Total de faltas
Considere que foram dadas 20 aulas e que para passar o aluno precisa de pelo menos 70% de presença e média 6,0 ou mais.

Ao final imprima:
Nome do aluno
Média
Percentual de Presença (assiduidade)
Resultado (Reprovado por faltas e por média, Reprovado por faltas, Reprovado por média, Aprovado)

'''

nome = input('Digite o nome do aluno: ')

nota1 = float(input('Digite a nota da Prova 1: '))
nota2 = float(input('Digite a nota da Prova 2: '))
faltas = int(input('Digite o total de faltas: '))

media = (nota1+nota2)/2
assid = (20-faltas)/20

if media >= 6 and assid >= 0.7:
    resultado = 'Aprovado'

elif media < 6 and assid < 0.7:
    resultado = 'Reprovado por média e por faltas'

elif media < 6:
    resultado = 'Reprovado por média'

elif assid < 0.7:
    resultado = 'Reprovado por faltas'

else:
    print('Erro')

print('Nome:',nome)
print('Média:',media)
print('Assiduidade:',str(assid*100)+'%')
print('Resultado:',resultado)
