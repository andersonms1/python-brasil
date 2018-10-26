valid = True
sum = 0
cpf = input('Digite o CPF desejado: ')
counter = 10

second_sum = 0
second_counter = 11

# verifica o tamanho
if len(cpf) != (11 + 3): 
    print('Invalid size!')
    valid = False
# verifica os digitos
elif not cpf[-2:].isdigit() or not cpf[4:7].isdigit() or not cpf[8:11].isdigit() or not cpf[-2:].isdigit():
    print('Digite numeros!')
    valid = False
# verifica formato
elif cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print('Digite no formato correto')
    valid = False

for w in cpf[:11]:
    if w.isdigit():
        sum = sum + int(w) * counter
        counter = counter - 1

for w in cpf[:13]:
    if w.isdigit():
        second_sum = second_sum + int(w) * second_counter
        second_counter = second_counter - 1
    

def valid_digits (any_sum, digit):
    v = False
    if any_sum % 11 == 0 or any_sum % 11 == 1:
        v = (digit == 0)
    else:
        v = (11 - (any_sum % 11) == digit)
    return v

if valid_digits(sum, cpf[len(cpf)-2]) or valid_digits(second_sum, cpf[len(cpf)-1]):
    valid = False

print(valid)

#  https://www.somatematica.com.br/faq/cpf.php