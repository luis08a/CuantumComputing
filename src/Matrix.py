import Complex as comp
import math


def add(a, b):
    if (len(a) != len(b) and len(a[0]) != len(b[0])):
        pass
    else:
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = comp.Complex.add(a[i][j], b[i][j])
        return a


def inverse(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j].inverse()
    return matrix


def scalarProduct(scalar, matrix):
    for row in matrix:
        for entry in row:
            entry = comp.Complex.mult(scalar, entry)
    return matrix


def matrixProduct(a, b):
    if(len(a[0]) == len(b)):
        product = [[comp.Complex(0,0) for x in range(len(b[0]))] for y in range(len(a))]
        for x in range(len(a)):
            for y in range(len(b[0])):
                for z in range(len(a[0])):
                    product[x][y] = comp.Complex.add(
                        product[x][y], comp.Complex.mult(a[x][z], b[z][y]))
        return product
    else:
        pass


def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[comp.Complex(0, 0) for y in range(n)] for x in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result


def conjugate(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j]= matrix[i][j].conjugate()
    return matrix


def adjoint(matrix):
    return conjugate(transpose(matrix))


def innerVector(v1, v2):
    pass


def innerMatrix(A, B):
    result = matrixProduct(transpose(A), B)
    inner = 0
    for i in range(len(A)):
        inner += result[i][i].real
    return inner


def norm(matrix):
    return math.sqrt(innerMatrix(matrix, matrix))


def distance(A, B):
    dif = add(A, inverse(B))
    return norm(dif)


def unitary(matrix):
    unit = True
    temp = matrixProduct(adjoint(matrix), matrix)
    for i in range(len(temp)):
        for j in range(i):
            if(i == j and temp[i][j].real != 1 and temp[i][j].imag != 1):
                unit=False;
                return unit
            elif (i != j and temp[i][j].real != 0 and temp[i][j].imag != 0):
                unit=False
                return unit
    return unit


def hermitian(matrix):
    flag=True
    t=transpose(matrix)
    c=conjugate(matrix)
    if (len(t) == len(c)):
        for i in range(len(t)):
            for j in range(len(t[0])):
                if(t[i][j].real != c[i][j].real and t[i][j].imag != c[i][j].imag):
                    flag=False
                    break
    else:
        flag=False
    return flag

def tensorProduct(A, B):
    p = []
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                for m in range(len(B[0])):
                    p[i+k][j+m]= comp.Complex.mult(A[i][j],B[k][m])
    return p
