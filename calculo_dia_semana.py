def calcular_dia_da_semana(dia, mes, ano):
    dia_semana = (ano - 1901) * 365 + (ano - 1901) // 4 + dia + (mes - 1) * 31 \
                 - ((mes * 4 + 23) // 10) * ((mes + 12) // 15) \
                 + ((4 - ano % 4) // 4) * ((mes + 12) // 15)
    
    dias_da_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    dia_semana = dia_semana % 7
    
    return dias_da_semana[dia_semana]

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

dia_da_semana = calcular_dia_da_semana(dia, mes, ano)

print(f"A data {dia}/{mes}/{ano} caiu numa {dia_da_semana}.")