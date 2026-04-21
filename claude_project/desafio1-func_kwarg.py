'''

def resumo(**dados):
    # Complete a função
    # Ela deve retornar uma string formatada assim:
    # "nome: Ana | idade: 28 | cidade: BH"
    # para qualquer combinação de chaves passadas
    pass

print(resumo(nome="Ana", idade=28, cidade="BH"))

'''

def nome_idade(**info):
    dados = [f"{chave}: {valor}" for chave, valor in info.items()]
    return "\n----------\n".join(dados)

print(nome_idade(patricia = 21, marcela = 19, rayssa = 20, daniela = 21, elisangela = 22, rosangela = 20, angela = 16)) #salve estilo cachorro

'''
Sim! Você pegou o conceito. O código funciona e você usou **kwargs corretamente — isso é o que importava no desafio.
Duas observações pequenas:
O separador ficou ", " em vez de ": ", então a saída fica patricia, 21 em vez de patricia: 21. Só detalhe de formatação, a lógica está certa.
E repara que você inverteu o domínio — no original seria nome: valor como nome: Ana, mas aqui você usou nomes como chaves e idades como valores. Funcionou porque **kwargs não liga para o que você passa — mas em APIs isso importa: a chave deve descrever o dado, não ser o dado.
Versão alinhada com o enunciado original ficaria:

def resumo(**info):
    dados = [f"{chave}: {valor}" for chave, valor in info.items()]
    return " | ".join(dados)

print(resumo(nome="Patrícia", idade=21, cidade="BH"))
# nome: Patrícia | idade: 21 | cidade: BH

'''