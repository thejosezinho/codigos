nome_responsavel = str(input('Qual o nome do respónsavel da reserva: ')).strip()
if nome_responsavel == '':
    print('Você precisa escrever o nome do respónsavel')
elif nome_responsavel != '':
    check_in_dia = int(input('Qual o dia da reserva: ')) 
    check_in_mes = int(input('Qual o mês da reserva: ')) * 30
    check_in_ano = int(input('Qual o ano da reserva: ')) * 365
    check_out_dia = int(input('Qual o dia da saída: '))
    check_out_mes = int(input('Qual o mês da saída: ')) * 30
    check_out_ano = int(input('Qual o ano da saída: ')) * 365
    soma_in = (check_in_dia + check_in_mes + check_in_ano)
    soma_out = (check_out_dia + check_out_mes + check_out_ano)
    e_possível = soma_out - soma_in
    if e_possível <= 0:
        print('NÃO É POSSÍVEL FAZER RESERVA! A data de check_in é maior que a de check_out')
    else:
        tipo_quarto = int(input('''Qual o tipo de quarto: 
Digite (1) para stander 
Digite (2) para premuim 
Digite (3) para Luxo 
:'''))
        calculando_dias =  (soma_out) - (soma_in)
        if tipo_quarto == 1:
            valor_dias = calculando_dias * 100
            print('O valor da sua hospedagem foi de R${:.2f} você ficara no quarto {} por {} dias'.format(valor_dias, tipo_quarto, calculando_dias))
        elif tipo_quarto == 2:
            valor_dias = calculando_dias * 180
            print('O valor da sua hospedagem foi de R${:.2f} você ficara no quarto {} por {} dias'.format(valor_dias, tipo_quarto, calculando_dias))
        elif tipo_quarto == 3:
            valor_dias = calculando_dias * 250
            print('O valor da sua hospedagem foi de R${:.2f} você ficara no quarto {} por {} dias'.format(valor_dias, tipo_quarto, calculando_dias))
        else:
            valor_dias = 0
            print('escreva um número possível para o quarto')
    


