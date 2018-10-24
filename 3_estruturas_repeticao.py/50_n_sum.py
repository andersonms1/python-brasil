n = int(input('Digite o valor de n: '))
count = 2 
sum = 1

while count <= n:
    sum = sum + 1/count
    count = count + 1

print(sum)