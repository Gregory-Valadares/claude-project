import requests

while True:
    try:
        cep = input("Digite um CEP: ")
        if len(cep) == 8:
            break
    except:
        print("Caracteres inválidos na entrada do CEP.")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
except:
    None

while True:
    print(resposta.json())
    if list(resposta.json().values())[0] == "true":
        print("CEP inválido.")
    else:
        break

print(f"Status: {resposta.status_code}")
dados = resposta.json()
print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
print(f"Estado: {dados['uf']}")