n = int(input('Digite o numero: '))

str_number = str(n)
str_len = len(str_number)

str_len = str_len - 1 
while str_len >= 0:
    print(str_number[str_len], end='')
    str_len = str_len - 1 

print()
