preco = int(input("Insira o preço do produto: "))

notas = [100, 50, 20, 10, 5, 2, 1]
quantidade_notas = {}

for nota in notas:
    quantidade_notas[nota] = preco // nota
    preco %= nota

for nota, qtd in quantidade_notas.items():
    print(f"Notas de {nota}: {qtd}")