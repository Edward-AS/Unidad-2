a = [[4,3],[9,3]]
#print(a)

def newMatrix(f,c,n):
    matriz = []
    for i in range(f):
        a = [n]*c
        matriz.append(a)
    return matriz

#print(newMatrix(3, 5, 1))

def sumaMatriz(A,B):
    # Obtenemos las dimensiones de la matriz
    numFilasA = len(A)
    numFilasB = len(B)
    numColumnasA = len(A[0])
    numColumnasB = len(B[0])

    if numFilasA == numFilasB and numColumnasA == numColumnasB:
        C = newMatrix(numFilasA, numColumnasA, 0) # Creamos una matriz
        for i in range(numFilasA):
            for j in range(numColumnasA):
                # En la nueva matriz plasmamaos los resultados
                C[i][j] = A[i][j] + B[i][j]
    # Retornamos la matriz con los resultados
    return C

suma = sumaMatriz([[1,2,3],[7,8,9],[13,14,15]], [[4,5,6],[10,11,12],[16,17,18]])
#print(suma)

def multiplicacionMatriz(A,B):
    # Obtenemos las dimensiones de la matriz
    numFilasA = len(A)
    numFilasB = len(B)
    numColumnasA = len(A[0])
    numColumnasB = len(B[0])

    if numFilasA == numFilasB and numColumnasA == numColumnasB:
        C = newMatrix(numFilasA, numColumnasA, 0) # Creamos una matriz
        for i in range(numFilasA):
            for j in range(numColumnasA):
                # En la nueva matriz plasmamaos los resultados
                C[i][j] = A[i][j] * B[i][j]
    # Retornamos la matriz con los resultados
    return C

multiplicacionMatriz([[1,2,3],[7,8,9],[13,14,15]], [[4,5,6],[10,11,12],[16,17,18]])

def show_matrix(M):
    """ Imprime los valores almacenados en la matriz """
    filas = len(M)
    columnas = len(M[0])
    for i in range(filas):
        for j in range(columnas):
            # Imprime de una forma elegante la matriz
            print("| {0} ".format(M[i][j]), sep=',', end='')
        print('|\n')

a = [[1,2,3],[7,8,9],[4,5,6]]
show_matrix(a)

show_matrix(suma)