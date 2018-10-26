import random
forca = ''
segredo = ''
erros = 0
tentativas = 6

f = open('palavras.txt', 'r')

palavra = f.readlines()

palavra = random.choice(palavra)

# passa do formato lista p/ string
for w in palavra:
    if w.isalpha():
        forca = forca + w
        segredo = segredo + '_ '

# retira ultimo espaço
segredo = segredo.strip()

while erros < tentativas:

    tentativa = input('Digite uma letra')

    for w in forca:
        if w == tentativa:
            segredo = segredo. 

    erros = erros + 1
