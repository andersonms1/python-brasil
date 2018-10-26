
gabarito = int(input())
contador = 0

lista = [1, 2, 4, 8, 16, 32, 64]
resposta = []

def soma_lista(lista):
    soma = 0
    for number in lista:
        soma = soma + number

    return soma

def get_maior(lista):

    for numero in lista:

        if numero < gabarito:
            resposta.append(numero)

    maior_numero = resposta[-1]

    return maior_numero


resposta_final = []

while soma_lista(resposta_final) != gabarito:
    resposta_final.append(get_maior(lista))
    lista = lista[:lista.index(get_maior(lista))]

print(resposta_final)