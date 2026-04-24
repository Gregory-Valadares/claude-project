'''
Exercício: Mês de nascimento
1) Em um novo programa, crie uma tupla para guardar os meses do ano.
Em seguida peça ao usuário a sua data de nascimento no formato DD-MM-AAAA e guarde-a na variável data_nasc.
Ao final imprima "Você nasceu no mês de ", utilizando o nome do mês da tupla correspondente ao mês informado pelo utilizador.
Dica: Você vai precisar fazer slicing na data de nascimento informada para ter o mês.
Depois você terá que buscar o mês na tupla através do índice.
'''

meses = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

while True:
    while True:
        data_nasc = input("Digite sua data de nascimento no formato (DD-MM-AAAA): ")

        if 1 <= int(data_nasc[0:2]) <= 31 and 1 <= int(data_nasc[3:5]) <= 12 and 1900 <= int(data_nasc[6:10]) <= 2027: #atualizar o ano
            dia_usr = int(data_nasc[0:2])                                                                                  #todos os anos
            mes_usr = int(data_nasc[3:5])
            ano_usr = int(data_nasc[6:10])
            break
        else:
            print("Digite uma data válida no formato DD-MM-AAAA.")

    print(f"Você nasceu no dia {dia_usr} de {meses[mes_usr - 1]} de {ano_usr}.")

    end_or_reset = input("Deseja reiniciar? [s/n]: ").lower()
    if end_or_reset != "s":
        break
    else:
        continue
print("Fim do programa")

