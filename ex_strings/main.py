print("Exercício - Operação com strings")

nome = input("Digite seu nome: ").lower()
sobrenome_mae = input("Digite o sobrenome da sua mãe: ").lower()
sobrenome_pai = input("Digite o sobrenome do seu pai: ").lower()

iniciais = nome[0]+sobrenome_mae[0]+sobrenome_pai[0]

email = nome + "." + sobrenome_pai + "@" + nome[0] + sobrenome_pai + "tech" + ".com"

print("Suas iniciais são",iniciais,"e seu email é:",email)