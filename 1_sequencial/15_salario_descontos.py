horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
pagamento_hora = float(input("Digite o seu salário bruto: "))

salario_bruto = horas_trabalhadas * pagamento_hora
ir =  salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato =  salario_bruto * 5 / 100
salario_liquido = salario_bruto - ir - inss - sindicato

print('+ Salário Bruto : R$ '+str(salario_bruto))
print('- IR (11%) : R$ '+str(ir))
print('- INSS (8%) : R$ '+str(inss))
print('- Sindicato (5%) : R$ '+str(sindicato))
print('= Salário Liquido : R$ '+str(salario_liquido))
