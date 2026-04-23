import requests
from pprint import pprint

while True:
    city_code = input("Digite o código da cidade: ") # Três Marias: 3170206
    try:
        response = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{city_code}")

        if response.status_code != 200:
            print(f"Status Code: {response.status_code}")

        elif response.status_code == 200:
            city_code_response = str(response.json()['id'])
            dados = response.json()

            if city_code != city_code_response:
                print(f"O código da cidade que você digitou: {city_code} , é inválido.")
            elif city_code == city_code_response:
                #print(f"{pprint(dados)}\n")
                print(
                    f"\n"
                    f"Município: {dados['nome']}\n"
                    f"Estado:    {dados['microrregiao']['mesorregiao']['UF']['nome']}\n"
                )
        else:
            print(f"Erro de fluxo de código.")
    except:
        print("Erro na recepção da Response.")