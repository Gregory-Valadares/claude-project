print("Exercício - Média Ponderada")

peso1 = float(input("Digite o peso da prova 1: "))
nota1 = float(input("Digite a nota da prova 1: "))

peso2 = float(input("Digite o peso da prova 2: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = float(((peso1 * nota1) + (peso2 * nota2))/(peso1 + peso2))

print("A média do aluno é:",media)

