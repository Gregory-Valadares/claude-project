'''

Desafio 2 — Compreensões e escopos - VERSÃO 1

'''

valores = [1, -3, 5, -2, 8, -7, 4]

# 1. Crie uma list comprehension que retorne apenas os positivos ao quadrado
# 2. Crie um dict comprehension: {valor_original: valor_ao_quadrado} mas só para os negativos

positivos_quadrado = []
negativos_dict = {}

for i in range(len(valores)):
    if valores[i] >= 0:
        positivo_quad = valores[i] ** 2
        positivos_quadrado.append(positivo_quad)
    else:
        negativo_quad = valores[i] ** 2
        negativos_dict[i] = negativo_quad

print(positivos_quadrado)
print(negativos_dict)