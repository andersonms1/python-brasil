n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
sum = 0

if n1 < n2:
    bigger = n2
    smaller = n1
else:
    bigger = n1
    smaller = n2

while smaller <= bigger:
    print(smaller, end=' ')
    sum = sum + smaller
    smaller = smaller + 1

print()
print(sum)


