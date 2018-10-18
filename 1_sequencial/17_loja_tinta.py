tinta = float(input("Digite a área do local que desejar pintar(m^): "))

litros = tinta / 6

latas = litros / 18
galoes = litros / 3.6

preco_latas = latas * 80
preco_galoes = galoes * 25


print('Quantidade de latas eh: '+str(latas))
print('O preco total eh de: '+str(preco_latas))
print('O preco total eh de: '+str(preco_galoes))