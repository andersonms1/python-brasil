name = input('Digite o seu nome: ')

while len(name) <= 3:
    print('Invalido! Seu nome deve possuir ao menos 4 letras:')
    name = input('Digite o seu nome: ')

age = int(input('Digite a sua idade: '))

while age < 0 or age > 150:
    print('Invalid age!')
    age = int(input('Digite a sua idade: '))

payment = float(input('Digite o seu salario: '))

while payment < 0 :
    print('Invalid age!')
    payment = float(input('Digite o seu salario: '))

sex = input('Digite o sexo: ')

while sex != 'f' and sex != 'm':
    sex = input('Digite o sexo: ')



