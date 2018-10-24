f = open('texto.txt', 'r')
counter = 0
max_line_size = 40
rest_letters = 0

def sum_char(line):
    space = 1
    counter = 0
    for w in line:
        counter = counter + len(w)
        counter = counter + space
    
    return counter

def until_space(f, line):
    counter = 1
    char = ''
    while char != ' ':
        char = f.readline(counter)
        if char == ' ':
            break
        line = line + char
    return str(line)


def same_line(char, times):
    for l in range(times):
        print(char, end='')
    print()

def list_2_string(l):
    s = ''
    for word in l:
        s = s + word
        s = s + ' '
    return s.strip()

while counter < 6:
    line = f.readline(max_line_size - rest_letters)
    rest_letters = 0

    

    if line[-1] != ' ':
        line = until_space(f, line)

    line = line.split(" ")
    
    remainder = line[-1]

    line = list_2_string(line[0:-1])

    

    
    if sum_char(line) > max_line_size:
        
        print(line, end='\n')
        print(remainder, end=' ')
        

    else:
        print(line)


        

    counter = counter + 1