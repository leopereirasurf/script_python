nome = str (input ('qual é seu nome?'))
if nome == 'leo':
    print ('que nome bonito!'.format (nome))
elif nome == 'pedro' or nome == 'Maria' or nome == 'paulo':
    print ('seu nome é normal do brasil')
else:
    print  ('seu nome é tao normalzinho')
print ('tenha um bom dia, {}!'.format (nome))
