'''
n1 = input('Digite o primero valor: ')
n2 = input('Digite o segundo valor: ')
n3 = input('Digite o terceiro valor: ')
print('Direi a você o maior termo e o mínimo desta lista')
lista = []
lista.append(n1)
lista.append(n2)
lista.append(n3)
print("o maior termo da lista é:" , max(lista))
print("o maior termo da lista é:" , min(lista))
'''

'''
n1 = input('Digite o primero valor: ')
n2 = input('Digite o segundo valor: ')
n3 = input('Digite o terceiro valor: ')
lista = [n1, n2, n3]
print('o maior termo desta lista é' ,max(lista))
print('O menor termo desta lista é' ,min(lista))'''

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor = a # menor
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
#maior
maior = a
if b > a and b > c:
    maior = b 
if c > a and c > b:
    maior = c
print('O maior termo é: {}'.format(maior))
print('O menor termo é: {}'.format(menor))
