def calcula_capacidade (altura, largura, comprimento):
    capacidade = altura * largura * comprimento
    return capacidade / 10

def calcula_autonomia(capacidade, consumo_medio):
    autonomia = capacidade / consumo_medio
    return autonomia

def classifica_consumo(autonomia):
    if autonomia < 2:
        print('Consumo elevado')
    elif autonomia >= 2 and autonomia <= 7:
        print('Consumo moderado')
    elif autonomia > 7:
        print('Consumo reduzido')
    
altura = float(input('Altura: '))
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
consumo_medio = float(input('Consumo médio: '))

capacidade = calcula_capacidade(altura, largura, comprimento)
autonomia = calcula_autonomia(capacidade, consumo_medio)
consumo = classifica_consumo(autonomia)

print(f'Capacidade: {capacidade:.2f}')
print(f'Autonomia: {autonomia:.2f}')