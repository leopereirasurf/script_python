distancia = float (input ('qual é a distancia da sua viagem?'))
print ('você esta preste a começar uma viagem de {} Km.'.format (distancia))
if distancia <= 200:
    preço =distancia * 0.50
else:
    preço = distancia * 0.45
print ('e o preço da sua passagem será de R$ {:.2f}'.format (preço))
