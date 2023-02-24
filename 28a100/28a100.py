from random import randint 
from time import sleep
computador = randint (0,5) #faz comoutador pensar
print ('-=-' *20)
print ('vou pensar em um numero entre 0 e 5. tente advinhar...')
print ('-=-' *20)
jogador = int (input ('Em que numero eu Pensei?')) #jogador tenta adivinhar
print ('PROCESSANDO...')
sleep (4)
if jogador == computador:
    print ('PARABÉNS vecê è o Grande Campeão')
else:
    print('GANHEI! eu pensei no numero {} e nao no {}!'.format(computador , jogador))
