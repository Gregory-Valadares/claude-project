import requests

while True:
    input("Tecle Enter para iniciar: ")
    try:
        response = requests.get("https://httpbin.org/status/404")
        if response.status_code != 200:
            print(f"Status Code: {response.status_code}")
        else:
            print(response.json())
    except:
        print("Erro na recepção da Response.")

'''
Eu esperava que aparecesse um status_code 404
mesmo tendo em vista aquele 404 na url. Tava na cara. kkkk.
Eu só pensei também que mudando o status_code para 200 poderia retornar alguma informação.
Por isso coloquei a linha 10.
'''
