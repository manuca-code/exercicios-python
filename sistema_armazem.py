produtos = []
produto = None
qntd = 0
valor = 0

def cadastro_produto(produto, qntd, valor):
    produto = input('Nome: ')
    qntd = int(input('Quantidade: '))
    valor = float(input('Valor: '))
    produtos.append(produto)
    produtos.append(qntd)
    produtos.append(valor)
    return produtos

def remover_produto(produto):
    produto_remover = input('Nome: ')
    if produto_remover in produtos:
        produtos.remove(produto_remover)
    return produtos

while True:

    print ('****ARMAZÉM DA VILA****\n'
        '1. Cadastrar produto\n'
        '2. Remover produto\n'
        '3. Calcular valor do estoque\n'
        '4. Exibir produtos\n'
        '5. Sair\n')

    opcao = int(input('Opção: '))

    if opcao == 1:
        cadastro_produto(produto, qntd, valor)
        print(produtos)

    if opcao == 2:
        remover_produto(produto)
        print(produtos)