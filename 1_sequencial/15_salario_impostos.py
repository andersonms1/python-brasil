salario_bruto = float(input('Digite o seu Salário: '))

pr

print('+ Salário Bruto : R$' + str(salario_bruto))

ir = (11 * salario_bruto)/100
print('- IR (11%) : R$' + str(salario_bruto - ir))

s = (5 * salario_bruto)/100
print('- Sindicato ( 5%) : R$' + str(salario_bruto - s))

salario_liquido = salario_bruto -ir -s
print('= Salário Liquido : R$' + str(salario_liquido))
