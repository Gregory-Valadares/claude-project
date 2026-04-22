# -*- coding: utf-8 -*-
from configuracao_pc import todos_os_pcs
from dataclasses import dataclass

@dataclass
class Cliente:
    id: str
    tipo: str
    nome: str
    nascimento: str
    cidade: str

    def calcular_total(self, valor_compra):
        return valor_compra

@dataclass
class ClienteVIP(Cliente):
    desconto: dict

    def calcular_total(self, valor_compra):
        valor_desconto = list(self.desconto.values())[0]
        print(f"Você e um cliete VIP {list(self.desconto.keys())[0]}.\nVocê tem {100.00 - (100*valor_desconto)}% de desconto.")
        return valor_compra * valor_desconto


# Lista de Clientes Normais
clientes_normais = [
    Cliente("001", "Normal", "Joao Silva", "1990-05-15", "Sao Paulo"),
    Cliente("002", "Normal", "Maria Oliveira", "1985-10-22", "Rio de Janeiro"),
    Cliente("003", "Normal", "Carlos Souza", "1998-02-03", "Belo Horizonte"),
    Cliente("004", "Normal", "Ana Costa", "2001-07-12", "Curitiba"),
    Cliente("005", "Normal", "Ricardo Santos", "1975-12-30", "Salvador"),
    Cliente("006", "Normal", "Fernanda Lima", "1993-04-18", "Porto Alegre")
]

# Lista de Clientes VIP
clientes_vip = [
    ClienteVIP("007", "VIP", "Roberto Justus", "1960-01-20", "Sao Paulo", {'Black' : 0.90}),
    ClienteVIP("008", "VIP", "Juliana Paes", "1982-03-26", "Niteroi", {'Black' : 0.90}),
    ClienteVIP("009", "VIP", "Marcos Pontes", "1963-06-11", "Bauru", {'Gold' : 0.95}),
    ClienteVIP("010", "VIP", "Luiza Trajano", "1951-09-13", "Franca", {'Gold' : 0.95}),
    ClienteVIP("011", "VIP", "Gisele Bundchen", "1980-07-20", "Horizontina", {'Black' : 0.90}),
    ClienteVIP("012", "VIP", "Eduardo Kobra", "1975-01-01", "Sao Paulo", {'Gold' : 0.95})
    ]

todos_clientes = clientes_normais + clientes_vip

cadastros_validos = []
for cliente in todos_clientes:
    cadastros_validos.append(cliente.id)

# VAMOS INICIAR A INTERAÇÃO COM O USUÁRIO A PARTIR DAQUI:

print(">>> LOJA DE MAQUINAS FURIOSAS DO GREG <<<\n")

while True:
    try:
        usuario = input("Digite o seu ID: ")
        if usuario in cadastros_validos:
            break
        print("ID nao cadastrado.")
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

print("Lista de Maquinas disponiveis a pronta entrega:\n")
for pc in todos_os_pcs:
    print(f"{pc}\n")

while True:
    try:
        carrinho = input("Digite o codigo do PC que deseja comprar. Ex.: [pc001]: ")
        if carrinho in pcs_validos:
            break
        print("Codigo inexistente.")
    except:
        print("ERRO na entrada do codigo do PC.")

valor_compra = 0
for pc in todos_os_pcs:
    if pc.code == carrinho:
        valor_compra = valor_compra + pc.preco
        print(f"\n{pc}")

        print(f"\nEste e o valor do {pc.configuracao}: R${valor_compra}")


# AGORA DEVO MOSTRAR O PRECO COM DESCONTO CASO O USUARIO SEJA UM CLIENTE VIP.
total = cliente_logado.calcular_total(valor_compra)
print(f"\nValor final: R${total:.2f}")