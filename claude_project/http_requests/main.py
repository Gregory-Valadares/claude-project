import requests
from pprint import pprint

finalizar = False
while not finalizar:
    while True:
        try:
            cep = input("Digite um CEP: ")
            if len(cep) != 8:
                raise ValueError("Digite no máximo 8 caracteres.")

            resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
            if resposta.status_code != 200:
                print(f"Erro: {resposta.status_code}")

            resposta_json = resposta.json()
            if "erro" in resposta_json:
                print("CEP inválido.")
            else:
                break
        except ValueError:
            print(f"Erro na entrada do CEP: {cep}")

    print(f"Status: {resposta.status_code}")
    dados = resposta.json()
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
    
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