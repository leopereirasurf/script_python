velocidade = float (input ('qual é a velocidade Atual do carro?'))
if velocidade > 50:
    print ('MULTADO! Você essedeu o limite que de 50km/h')
    multa = (velocidade-50) * 7
    print('você deve pagar multa R${:.2f}!'.format(multa))
print ('tenha um bom dia dirija com segurança')
