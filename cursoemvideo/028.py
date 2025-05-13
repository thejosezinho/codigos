import random

n = [1,2,3,4,5]
n_aleatorio = random.choice(n)
pedido = int(input('escolha um número entre 1 e 5: '))
if pedido == n_aleatorio:
    print('Parabéns, você acetou')
else:
    print('Horrível, você errou')


'''METÓDO DA AULA
from random imporr ranint
import time #blibioteca de tempo
computador = randint(0, 5)
jogador = int(input('Em que número eu pensei: ))
print('processando)
sleep(3)
if jogador == computador:
    print('Parabéns)
else:
    print('Você perdeu' )

'''


