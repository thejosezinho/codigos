from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('=' * 20)
print('''Suas opções:'
[0] Pedra
[1] Papel
[2] Tesoura''')
print('=' * 20)
jogador = int(input('Qual a sua jogada?'))
print('=' * 20)
print('eu joguei {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('=' * 20)
if jogador == computador:
    print('Nós dois jogamos {}'.format(itens [computador]))
elif jogador == 0 and computador == 2:
    print('Você ganhou')
elif jogador == 1 and computador == 0:
    print('Você ganhou')
elif jogador == 2 and computador == 1:
    print('Você ganhou')
else:
    print('Eu ganhei')

