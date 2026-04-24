'''
1. capitalize() (Primeira letra da frase)
Este método coloca a primeira letra da string em maiúscula e todas as outras em minúsculas.
python
'''

texto = input("Digite algo: ")
resultado = texto.capitalize()
print(resultado)
# Entrada: "olá MUNDO" -> Saída: "Olá mundo"


'''
2. title() (Primeira letra de cada palavra)
Este método coloca a primeira letra de cada palavra em maiúscula.
Flexiple
Flexiple
python
'''

texto = input("Digite seu nome completo: ")
resultado = texto.title()
print(resultado)
# Entrada: "joão silva" -> Saída: "João Silva"

'''
3. Fatiamento (Apenas a primeira, sem alterar o resto)
Se você precisa que apenas a primeira letra seja maiúscula, mas quer manter as outras letras como o usuário digitou, use fatiamento:
Sentry
Sentry
python
'''

texto = input("Digite algo: ")
# Pega o primeiro caractere [0], coloca em upper(), e soma com o restante [1:]
resultado = texto[0].upper() + texto[1:]
print(resultado)
# Entrada: "iphone" -> Saída: "Iphone"