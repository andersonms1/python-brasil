count = 0

num = int(input('Digite o numero desejado: '))
bigger = num

while count < 4:
    num = int(input('Digite o numero desejado: '))
    
    if num > bigger:
        bigger = num
    
    count = count + 1

print (bigger)