def calcula_soma(n1, n2):
   soma = n1 + n2
   if operacao == 1:
    print(f'Resultado: {soma}')
    
def calcula_subtracao(n1, n2):
   subtracao = n1 - n2
   if operacao == 2:
    print(f'Resultado: {subtracao}')

def calcula_multiplicacao(n1, n2):
   multiplicacao = n1 * n2
   if operacao == 3:
    print(f'Resultado: {multiplicacao}')

def calcula_divisao(n1, n2):
   if operacao == 4 and n2 != 0:
    divisao = n1 / n2
    print(f'Resultado: {divisao}')
   elif operacao == 4 and n2 == 0:
     ZeroDivisionError
     print('Não é possível fazer divisão por zero')
 
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))

print('''Qual operação você deseja?
1-Soma
2-Subtração
3-Multiplicação
4-Divisão ''')
operacao = int(input('Operação desejada: '))

op1 = calcula_soma(n1, n2)
op2 = calcula_subtracao(n1, n2)
op3 = calcula_multiplicacao(n1, n2)
op4 = calcula_divisao(n1, n2)