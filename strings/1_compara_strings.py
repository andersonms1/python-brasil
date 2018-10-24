print('Digite duas strings: ')
str1 = input()
str2 = input()

print('String 1:' + str1)
print('String 2:' + str2)

print('Tamanho de '+str1, end=' ')
print(len(str1))
print('Tamanho de '+str2, end=' ')
print(len(str2))

if len(str1) != len(str2):
    print('As duas strings possuem tamanhos diferentes')
else:
    print('As duas strings possume tamanhos iguais')

if str1 == str2:
    print('As strings sao iguais')
else:
    print('As strings sao diferentes')

