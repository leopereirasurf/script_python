velocidade = float(input ('qual é a velocidade do carro?'))
if velocidade > 80:
    print ('MULTADO! Voce exedeu o limite permitido que é 80km/h')
    multa = (velocidade-80) * 7
    print ('você deve pagar uma multa de R$ {:.2f}!'.format(multa))
print ('Tenha um bom dia dirija com segurança!')