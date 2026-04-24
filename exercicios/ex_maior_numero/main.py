'''
3. Peça para o usuário digitar x entradas de números em uma lista, no máximo 10 números.
O programa deve retornar o maior número digitado e a quantidade de vezes que ele se repete.
'''

while True:
    while True:
        quant = int(input("Digite quantos números deseja incluir na lista.[De 1 a 10]: "))
        if 1 <= quant <= 10:
            break
        else:
            print("Digite um número maior que 0 e menor ou igual a 10.")

    numeros = [input(f"Digite o {i + 1}º número: ") for i in
               range(quant)]  # i será o for correndo o número [quant] vezes. i começa sempre como 0.
    numeros.sort()
    repetidos = []
    print(f"O maior número é o número {numeros[quant - 1]}")

    for i in numeros:
        if numeros[quant - 1] == i:
            repetidos.append(numeros[quant - 1])
            print(f"O número {numeros[quant - 1]} se repetiu pela {len(repetidos)} vez.")
        else:
            print(f"{numeros[quant - 1]} é diferente de {i}")
    print(f"O número {numeros[quant - 1]} é o maior número e se repete {len(repetidos)} vezes.")