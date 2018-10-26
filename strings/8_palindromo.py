frase = input('Digite a frase: ')
f = ''

for w in frase:
    if w.isalpha():
        f = f + w

if f == f[::-1]:
    print('T')
else:
    print('F')

