import Complex as comp
import math

def add(a, b):
    """ dfsf"""
    if (len(a) == len(b) and len(a[0]) == len(b[0])):
        pass
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = comp.add(a[i][j], b[i][j])
        return a


def inverse(matrix):
    for i in matrix:
        for j in i:
            j = -j
    return matrix


def scalarProduct(scalar, matrix):
    for row in matrix:
        for entry in row:
            entry = comp.complex.product(scalar, entry)
    return matrix


def matrixProduct(a, b):
    if(len(a[1]) == len(b[0])):
        product = [[0 for x in range(len(b[1]))] for y in range(a[0])]
        for x in range(len(a[0])):
            for y in range(len(b[1])):
                for z in range(a[1]):
                    product[x][y] = comp.complex.add(
                        product[x][y], comp.complex.product(a[x][z], b[z][y]))
        return product
    else:
        pass


def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[comp.Complex(0, 0) for y in range(n)] for x in range(m)]
    for i in range(n):
        for j in range(m):
            result[m][n] = matrix[n][m]
    return result


def conjugate(matrix):
    for i in matrix:
        for j in i:
            i = i.conjugate()


def adjoint(matrix):
    matrix = transpose(matrix)
    return conjugate(matrix)


def innerVector(v1,v2):
    pass


def innerMatrix(A,B):
    result = matrixProduct(transpose(A),B)
    inner=0
    for i in range(len(A)):
        inner += result[i][i]
    return inner


def norm(matrix):
    return math.sqrt(innerMatrix(matrix,matrix))


def distance(A,B):
    dif = add(A,inverse(B))
    norm(dif)


def unitary(matrix):
    pass


def hermitian(matrix):
    flag=True;
    t = transpose(matrix)
    c = conjugate(matrix)
    if (len(t)==len(c)):
        for i in range(len(t)):
            for j in range(len(t[0])):
                if(t[i][j] != c[i][j]):
                    flag=False
                    break
    else:
        flag=False
    return flag