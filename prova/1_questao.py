import sys 

counter = int(input())
mulheres = []
homens = []



while counter > 0:
    
    pessoa = int(input())

    if pessoa % 2 == 0 :
        mulheres.append(pessoa)
    else:
        homens.append(pessoa)

    counter = counter -1


if len(mulheres) > len(homens):
    print('F')
    sys.exit()

else:
    
    for m in mulheres: 
        for h in homens:
            if m < h :
                mulheres.remove(m)
                homens.remove(h)

        

if len(mulheres) > 0:
    print('F')

else:
    print('S')

