from datetime import date
ano = int (input ('que ano quero analizar? coloque 0 para analizar o ano atual:'))
if ano ==0:
    ano = date.today() .year
if ano % 4== 0:
    print('o ano {} é Bissexto'.format(ano))
else:
    print (' o ano {} não é Bissexto'.format(ano))
