f = open('texto.txt', 'r')
counter = 10

while counter < 100:
    print(f.readline(counter))
    counter = counter + 10