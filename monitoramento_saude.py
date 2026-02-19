import random

def cadastro_exercicios():
    exercicios = []
    total_calorias = 0
    while True:
        nome_exercicio = input('Digite o nome do exercício ou "sair": ')
        if nome_exercicio == 'sair':
            break
        tempo = float(input('Tempo gasto: '))
        calorias = int(input('Calorias queimadas: '))
        dia_semana = input('Dia da semana: ')
        
        exercicio = [nome_exercicio, tempo, calorias, dia_semana]
        exercicios.append(exercicio)

        print(f'\nExercício cadastrado:')
        print(f'Nome: {nome_exercicio}')
        print(f'Tempo: {tempo} min')
        print(f'Calorias: {calorias}')
        print(f'Dia: {dia_semana}')
        
        total_calorias += calorias
        
    return exercicios, total_calorias

def resumo_diario(lista_exercicios):
    print('\nResumo diário:')
    for exercicio in lista_exercicios:
        nome_exercicio = exercicio[0]
        tempo = exercicio[1]
        calorias = exercicio[2]
        dia = exercicio[3]
        print(f"{dia}: {nome_exercicio}, {tempo} min, {calorias} kcal\n")

def calcula_imc():
    print('Cálculo do IMC')
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    imc = peso / (altura ** 2)
    print(f'IMC = {imc:.2f}')
    if imc < 20:
        print('Baixo peso')
    elif 20 <= imc < 25:
        print('Peso Normal')
    elif 25 <= imc < 30:
        print('Sobrepeso')
    else:
        print('Obesidade')

def meta_semanal(total_calorias):
    meta_calorias = float(input('\nMeta de calorias queimadas: '))
    if meta_calorias <= total_calorias:
        print('Meta atingida!')
    else:
        print('Meta não atingida')

def frases_motivacionais():
    frases = [
        'Acredite em si mesmo.',
        'Cada dia é uma nova oportunidade de brilhar.',
        'A persistência leva ao sucesso',
        'O sucesso é a soma de pequenos esforços repetidos dia após dia'
    ]
    frase_aleatoria = random.choice(frases)
    print(f'Frase motivacional: {frase_aleatoria}')

def media_calorias(lista_exercicios):
    total_exercicios = len(lista_exercicios)
    if total_exercicios == 0:
        print('Nenhum exercício cadastrado.')
        return

    soma_calorias = 0
    for exercicio in lista_exercicios:
        soma_calorias += exercicio[2]  

    media = soma_calorias / total_exercicios
    print(f"Média de calorias por exercício: {media:.2f} kcal")

def grafico_barras(lista_exercicios):
    max_calorias = max(exercicio[2] for exercicio in lista_exercicios)

    print('\n Gráfico de barras - Calorias queimadas por exercício\n')
    for exercicio in lista_exercicios:
        nome = exercicio[0]
        calorias = exercicio [2]
        barras = '|' * (calorias * 40 // max_calorias)
        print(f'{calorias}kcal {barras} {nome}')

# main
lista_exercicios = []
total_calorias = 0

opcao = None  

while opcao != '0':
    print('\nMenu de opções:\n'
          'Opção 1: Cadastro de exercícios\n'
          'Opção 2: Relatório diário\n'
          'Opção 3: Cálculo de IMC\n'
          'Opção 4: Meta semanal\n'
          'Opção 5: Frases motivacionais\n' 
          'Opção 6: Média de calorias por exercício\n'
          'Opção 7: Gráfico de barras\n'
          'Opção 0: Encerrar\n')

    opcao = input('Selecione uma opção: ')

    if opcao == '1':
        lista_exercicios, total_calorias = cadastro_exercicios()

    elif opcao == '2':
        if lista_exercicios:
            resumo_diario(lista_exercicios)
        else:
            print('Nenhum exercício cadastrado ainda. Retorne para a opção 1.')

    elif opcao == '3':
        calcula_imc()

    elif opcao == '4':
        if lista_exercicios:
            meta_semanal(total_calorias)
        else:
            print('Não foi possível verificar pois não há exercícios cadastrados ainda. Retorne para a opção 1.')

    elif opcao == '5':
        frases_motivacionais()

    elif opcao == '6':
        if lista_exercicios:
            media_calorias(lista_exercicios)
        else:
            print('Nenhum exercício cadastrado ainda. Retorne para a opção 1.')

    elif opcao == '7':
        grafico_barras(lista_exercicios)

    elif opcao == '0':
        print('Programa encerrado.')

    else:
        print('Opção inválida. Tente novamente.')
