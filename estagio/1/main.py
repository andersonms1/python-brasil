field_size = 40
text_size = 36
counter = 0
had_print = False


f = open('texto.txt', 'r')

for line in range(field_size):
    print('*', end='')


print()


while counter < 7:

    if had_print == True:
        # Do nothing
        pass
    else:
        print('*', end=' ')

    if counter == 0:
        text = f.readline(text_size + 1)
    else:
        text = f.readline(text_size + 1)

    if text[len(text) -1] == ' ':
        print('First if')
        for char in range(len(text) - 1):
            print(text[char], end='')
            print(' *', end='\n')
            had_print = False

    else:

        last_char = len(text) - 1
         

        while last_char != 0 and text[last_char] != ' ':
            last_char = last_char - 1

        # Copy string until space

        copy = ''
        for c in range(last_char):

            copy = copy + text[c]

        # text = copy

        print(copy.center(git ), end='')
        print(' *')


        if len(text[last_char: -1]) > 0:
            print('*', end=' ')
            print(text[last_char: -1].strip(), end='')
            had_print = True


    counter = counter + 1

print()
for line in range(field_size):
    print('*', end='')    
print()
