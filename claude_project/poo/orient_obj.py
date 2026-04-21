class Produto:
    def __init__(self, nome, preco):
        self.nome = nome    # "pega o parâmetro e guarda no objeto"
        self.preco = preco

    def __str__(self):
        return f"nome: {self.nome} | preco: {self.preco}"

    def aplicar_desconto(self, desconto):
        try:
            desconto = float(desconto)
            if desconto >= 0.0 and desconto <= 100.0:
                self.preco -= self.preco * (desconto/100) #Considera o valor de desconto em %
                print(f"Desconto de {desconto}% aplicado com sucesso")
                return self.preco
        except ValueError as e:
            print(f"Erro: {e}")
        except TypeError:
            print("Caractere inválido.")







''' INTERAÇÃO COM O USUÁRIO COMEÇA AQUI '''


#Lista de produtos:
p1 = Produto("caderno", 25.00)
p2 = Produto("caneta", 10.00)
p3 = Produto("fichario", 50.00)
p4 = Produto("resma", 30.00)
p5 = Produto("lapiseira", 8.00)
p6 = Produto("lapis", 5.00)
p7 = Produto("diamante", 10000.00)
p8 = Produto("livro", 100.00)

lista_produtos = [p1, p2, p3, p4, p5, p6, p7, p8]

#Definindo desconto:
desconto = input("Digite o valor do desconto em %. Ex.: [10]: ")

#Printando lista de produtos:
print("LISTA DE PRODUTOS")
for produto in lista_produtos:
    print(f"Nome: {produto.nome} - R${produto.preco}")

#Escolhendo produto para desconto.
produto_para_desconto = input("Digite o nome do produto para aplicar desconto: ")

produto_encontrado = None
for produto in lista_produtos:
    if produto_para_desconto == produto.nome:
        produto_encontrado = produto
        break

if produto_encontrado:
    produto_encontrado.aplicar_desconto(desconto)
else:
    print("Produto não encontrado.")

print(produto_encontrado)

# ÁREA ABAIXO DESTINADA A FUNÇÕES E INPUTS FORA DA CLASSE:

'''

def define_desconto():
    while True:
        try:
            desconto = input("Digite o valor do desconto em %. Ex.: [10.0]: ")
            desconto = float(desconto)
            if desconto < 0 or desconto > 100:
                print("Desconto deve ser entre 0 e 100.")
            break
        except ValueError:
            print("Digite um número decimal, separado por ponto.")
    return desconto

'''



'''
class Usuario:
    def __init__(self, nome, email, idade):
        self.nome = nome
        self.email = email
        self.idade = idade

    def __str__(self):
        return f"nome: {self.nome} | email: {self.email} | idade: {self.idade}"

u1 = Usuario("Gregory", "gregorygbmv@outlook.com", 31)
u2 = Usuario("Cypher", "cypher_red@matrix.com", 39)
u3 = Usuario("Neo", "neo_the_chosen@matrix.com", 33)
u4 = Usuario("Trinity", "trin_zion@matrix.com", 34)

print(u1)
print(u2)
print(u3)
print(u4)
print("\n")
print([u1])
print([u2])
print([u3])
print([u4])
'''



'''

print(u1.nome)
print(u1.email)
print(u1.idade)
print("\n")

print(u2.nome)
print(u2.email)
print(u2.idade)
print("\n")

print(u3.nome)
print(u3.email)
print(u3.idade)
print("\n")

print(u4.nome)
print(u4.email)
print(u4.idade)
print("\n")

'''