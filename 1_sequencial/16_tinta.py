tinta = float(input("Digite a área do local que desejar pintar(m^): "))

litros = tinta / 3
latas = litros / 18
preco = latas * 80

print('Quantidade de latas eh: '+str(latas))
print('O preco total eh de: '+str(preco))