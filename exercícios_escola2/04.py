n1 = int(input('Digite a primeira nota:'))
n2 = int(input('Digite a segunda nota:'))
media = (n1 + n2) * 0.5
if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')
print(f'sua media foi{media}')