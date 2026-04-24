'''
var1 = "Python é uma linguagem poderosa!"
"""
var1 = "21098765432109876543210987654321"
var1 = "--3---------2---------1---------"


"""
print(var1[-9:-1])
print(var1[-19:-10])
'''
#####################################################################3

palavras = ['oto', 'bob', 'patrick', 'ana', 'gregory', 'ovo', 'sam']
palindromos = []

for x in palavras:
        if x == x[::-1]:
            palindromos.append(x)
            print(x,"é um palíndromo.")
        else:
            print(x,"não é um palíndromo.")
print("Os palíndromos identificados são:",palindromos)