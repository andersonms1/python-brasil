user = input('Digite seu usuário: ')
password = input('Digite a sua senha: ')

while user == password:
    print('Invalido! Sua senha não pode ser ser seu usuario')
    user = input('Digite seu usuário: ')
    password = input('Digite a sua senha: ')