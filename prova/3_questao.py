counter = 0
senhas = 3

base = ''
lista = '' 
resposta = ''
erro = False

def descobre(senhas):

    base = ''
    lista = ''
    counter = 0
    resposta = ''

    while counter < senhas:
        lista = lista + input()
        if counter == 0:
            base = lista
        counter = counter + 1

    for l in base:
        if lista.count(l) == 3:
            resposta = resposta + l
    
    return resposta

resposta =  descobre(3)
if len(resposta) != 1:
    erro = True

resposta =  descobre(3)
if len(resposta) != 1:
    erro = True

resposta =  descobre(3)
if len(resposta) != 1:
    erro = True


if erro:
    print ('0')
else:
    print('1')