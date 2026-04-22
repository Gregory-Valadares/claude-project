from configuracao_pc import todos_os_pcs

class Cliente:
    def __init__(self, id, tipo, nome, nascimento, cidade):
        self.id = id
        self.tipo = tipo
        self.nome = nome
        self.nascimento = nascimento
        self.cidade = cidade

    def __repr__(self):
        return(
            f"ID: {self.id}\n"
            f"Tipo: {self.tipo}\n"
            f"Nome: {self.nome}\n"
            f"Nascimento: {self.nascimento}\n"
            f"Cidade: {self.cidade}\n"
        )

    def calcular_total(self, valor_compra):
        return valor_compra


class ClienteVIP(Cliente):
    def __init__(self, id, tipo, nome, nascimento, cidade, desconto):
        super().__init__(id, tipo, nome, nascimento, cidade)
        self.desconto = desconto

    def __repr__(self):
        return(
            f"ID: {self.id}\n"
            f"Tipo: {self.tipo}\n"
            f"Nome: {self.nome}\n"
            f"Nascimento: {self.nascimento}\n"
            f"Cidade: {self.cidade}\n"
            f"Desconto: {self.desconto}\n"
        )

    def calcular_total(self, valor_compra):
        valor_desconto = list(self.desconto.values())[0]
        print(f"Você é um cliete VIP {list(self.desconto.keys())[0]}.\nVocê tem {100.00 - (100*valor_desconto)}% de desconto.")
        return valor_compra * valor_desconto


# Lista de Clientes Normais
clientes_normais = [
    Cliente("001", "Normal", "João Silva", "1990-05-15", "São Paulo"),
    Cliente("002", "Normal", "Maria Oliveira", "1985-10-22", "Rio de Janeiro"),
    Cliente("003", "Normal", "Carlos Souza", "1998-02-03", "Belo Horizonte"),
    Cliente("004", "Normal", "Ana Costa", "2001-07-12", "Curitiba"),
    Cliente("005", "Normal", "Ricardo Santos", "1975-12-30", "Salvador"),
    Cliente("006", "Normal", "Fernanda Lima", "1993-04-18", "Porto Alegre")
]

# Lista de Clientes VIP
clientes_vip = [
    ClienteVIP("007", "VIP", "Roberto Justus", "1960-01-20", "São Paulo", {'Black' : 0.90}),
    ClienteVIP("008", "VIP", "Juliana Paes", "1982-03-26", "Niterói", {'Black' : 0.90}),
    ClienteVIP("009", "VIP", "Marcos Pontes", "1963-06-11", "Bauru", {'Gold' : 0.95}),
    ClienteVIP("010", "VIP", "Luiza Trajano", "1951-09-13", "Franca", {'Gold' : 0.95}),
    ClienteVIP("011", "VIP", "Gisele Bündchen", "1980-07-20", "Horizontina", {'Black' : 0.90}),
    ClienteVIP("012", "VIP", "Eduardo Kobra", "1975-01-01", "São Paulo", {'Gold' : 0.95})
    ]

todos_clientes = clientes_normais + clientes_vip

cadastros_validos = []
for cliente in todos_clientes:
    cadastros_validos.append(cliente.id)

# VAMOS INICIAR A INTERAÇÃO COM O USUÁRIO A PARTIR DAQUI:

print(">>> LOJA DE MÁQUINAS FURIOSAS DO GREG <<<\n")

while True:
    try:
        usuario = input("Digite o seu ID: ")
        if usuario in cadastros_validos:
            break
        print("ID não cadastrado.")
    except:
        print("ERRO na entrada do ID.")

cliente_logado = None
for cliente in todos_clientes:
    if cliente.id == usuario:
        cliente_logado = cliente
        break

pcs_validos = []
for pc in todos_os_pcs:
    pcs_validos.append(pc.code)

print("Lista de Máquinas disponíveis a pronta entrega:\n")
for pc in todos_os_pcs:
    print(f"{pc}\n")

while True:
    try:
        carrinho = input("Digite o código do PC que deseja comprar. Ex.: [pc001]: ")
        if carrinho in pcs_validos:
            break
        print("Código inexistente.")
    except:
        print("ERRO na entrada do código do PC.")

valor_compra = 0
for pc in todos_os_pcs:
    if pc.code == carrinho:
        valor_compra = valor_compra + pc.preco
        print(f"\n{pc}")

        print(f"\nEste é o valor do {pc.configuracao}: R${valor_compra}")


# AGORA DEVO MOSTRAR O PREÇO COM DESCONTO CASO O USUÁRIO SEJA UM CLIENTE VIP.
total = cliente_logado.calcular_total(valor_compra)
print(f"\nValor final: R${total:.2f}")