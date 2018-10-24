n = int(input('Digite o n termo: '))
count = 2
m = count + 1 

print('S = 1/1', end='')

while count <= n:
    print(' + '+str(count)+'/'+str(m), end='')

    count = count + 1

    m = m + 1
    while m % 2 == 0:
        m = m + 1

print()
