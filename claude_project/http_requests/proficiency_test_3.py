import requests
from pprint import pprint

def buscar_cep(cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/") # Três Marias: 39205000 ou Manaus: 69058842
        dados = response.json()
        #print(pprint(dados))
    except:
        print(f"Dados inválidos. Digite um CEP válido.")
        return None

    if response.status_code != 200:
        print(f"Erro: {response.status_code}")
        return None

    elif 'erro' in dados:
        return None

    else:
        info = {
            "Logradouro": dados.get("logradouro"),
            "Bairro": dados.get("bairro"),
            "Cidade": dados.get("localidade"),
            "Estado": dados.get("estado")
        }
        return info

# FUNÇÃO ACIMA ^^^  ---(XXX)--- INTERAÇÃO COM O USUÁRIO ABAIXO vvv:
finalizar = False
while not finalizar:
    while True:
        try:
            cep = input("Digite o CEP: ")
            if len(cep) != 8:
                print("Digite 8 números.")
            else:
                if not cep.isdigit():
                    print("Digite apenas números.")
                    continue
                break
        except:
            print("Caracteres inválidos. Digite 8 números")

    resultado = buscar_cep(cep)
    if resultado:
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")

    while True:
        try:
            sair = input("Para finalizar o programa digite 'sair': ").lower()
            if sair == "sair":
                finalizar = True
                print("Programa finalizado.")
                break
            break
        except ValueError:
            print(f"Erro ao sair do programa.")