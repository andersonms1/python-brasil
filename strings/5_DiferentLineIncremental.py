name = input('Digite o seu nome, caro padawan: ')
aux = ''
counter = len(name) 
lista = []

while counter >= 0:
    print(name[:counter], end='')
    print()
    counter = counter - 1

