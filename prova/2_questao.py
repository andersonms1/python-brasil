w, h = 4, 8;
matrix = [[0 for x in range(w)] for y in range(h)] 


matrix[0] = ["a", "b", "c"]
matrix[1] = ["d", "e", "f"]
matrix[2] = ["g", "h", "i"]
matrix[3] = ["j", "k", "l"]
matrix[4] = ["m", "n", "o"]
matrix[5] = ["p", "q", "r", "s"]
matrix[6] = ["t", "u", "v"]
matrix[7] = ["w", "x", "y", "z"]

palavra = input()


linha_contador = 0
coluna_contador = 0


for letra in palavra:

    for linha in matrix:
        for coluna in linha:
            if coluna == letra:
                
                print('#'+str(linha_contador + 2)+'='+str(coluna_contador + 1))
        
            coluna_contador = coluna_contador + 1
        
        linha_contador = linha_contador + 1
        coluna_contador = 0
    linha_contador = 0