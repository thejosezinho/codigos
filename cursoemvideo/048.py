soma = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        
print('soma de todos os valores é: {}'.format(soma))