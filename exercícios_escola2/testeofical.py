import sys
#Entrada de dados
nome_responsavel = input('Qual o nome do respónsavel da reserva: ').strip()
if nome_responsavel == '':
    print('Você precisa escrever o nome do respónsavel')
    sys.exit()
#processamento
check_in_dia = int(input('Qual o dia da reserva: ')) 
if check_in_dia > 31 or check_in_dia <= 0:
    print('Erro. data inválida')
    sys.exit()
check_in_mes = int(input('Qual o mês da reserva: ')) * 30
if check_in_mes > 360 or check_in_mes <= 29:
    print('Erro. data inválida')
    sys.exit()
check_in_ano = int(input('Qual o ano da reserva: ')) * 365
if check_in_ano < 365:
    print('Erro. data inválida')
    sys.exit()
check_out_dia = int(input('Qual o dia da saída: '))
if check_out_dia > 31 or check_out_dia <= 0:
    print('Erro. data inválida')
    sys.exit()
check_out_mes = int(input('Qual o mês da saída: ')) * 30
if check_out_mes > 360 or check_out_mes <= 29:
    print('Erro. data inválida')
    sys.exit()
check_out_ano = int(input('Qual o ano da saída: ')) * 365
if check_out_ano < 365:
    print('Erro. data inválida')
    sys.exit()
soma_in = (check_in_dia + check_in_mes + check_in_ano)
soma_out = (check_out_dia + check_out_mes + check_out_ano)
e_possível = soma_out - soma_in
if e_possível <= 0:
    print('A sua data de check-in é superior a data de check-out')
    sys.exit()
tipo_quarto = int(input('''Qual o tipo de quarto: 
Digite (1) para stander 
Digite (2) para premuim 
Digite (3) para Luxo 
:'''))
calc_dias = soma_out - soma_in 
if tipo_quarto == 1:
    valor_dias = calc_dias * 100

elif tipo_quarto == 2:
    valor_dias = calc_dias * 180

elif tipo_quarto == 3:
    valor_dias = calc_dias * 250

else:
    print('escreva um número possível para o quarto')
    sys.exit()
#Saída de dados
print('O valor da sua hospedagem foi de R${:.2f} você ficara no quarto luxo por {} dias'.format(valor_dias, calc_dias))

