space = 0
a = 0
e = 0
i = 0
o = 0
u = 0

frase = input('Digite a frase: ')

for w in frase:
    if w.lower() == ' ':
        space = space + 1
    elif w.lower() == 'a':
        a = a + 1
    elif w.lower() == 'e':
        e = e + 1
    elif w.lower() == 'i':
        i = i + 1
    elif w.lower() == 'o':
        o = o + 1
    elif w.lower() == 'u':
        u = u + 1

print('space: '+str(space))
print('a: '+str(a))
print('e: '+str(e))
print('i: '+str(i))
print('o: '+str(o))
print('u: '+str(u))
    