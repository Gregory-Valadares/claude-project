import requests

def buscar_cep(cep):
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/") # Três Marias: 39205000
        dados = response.json()
    except:
        print(f"Dados inválidos. Digite um CEP válido.")
        return None

    if response.status_code != 200:
        print(f"Erro: {response.status_code}")
        return None

    elif 'erro' in dados:
        return None

    else:
        print(
            f"\n"
            f"Logradouro: {dados['logradouro']}\n"
            f"Bairro:     {dados['bairro']}\n"
            f"Cidade:     {dados['localidade']}\n"
            f"Estado:     {dados['uf']}\n"
        )
        return(
            f"\n"
            f"Logradouro: {dados['logradouro']}\n"
            f"Bairro:     {dados['bairro']}\n"
            f"Cidade:     {dados['localidade']}\n"
            f"Estado:     {dados['uf']}\n"
        )

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

    buscar_cep(cep)

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