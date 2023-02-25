a = int (input ('primeiro valor'))
b = int (input ('segundo valor'))
c = int (input ('terceito valor'))
#verificando quem é o menor 
menor = a
if b<a and b<c:
    nenor = b
if c<a and c<b:
    menor = c
# Verificando o falor Maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print ('O menor valor digitado foi {}'.format (menor))
print ('O maior valor digitado foi {}'.format(maior))
