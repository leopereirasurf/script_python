n1 = float(input('digite a primeira nota:'))
n2 = float(input('digite a segunda nota:'))
m = (n1 + n2)/2
print ('a sua média foi: {:.1f}'.format(m))
if m >= 6.0:
    print('sua media foi Boa! PARAbÈNS')
else: 
    print ('sua media foi ruim! ESTUDE MAIS')
