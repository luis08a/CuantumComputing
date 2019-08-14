import Complex as comp


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
            entry= comp.complex.product(scalar,entry)
    return matrix

def matrixProduct(a,b):
    if(len(a[1]) == len(b[0]) ):
        product = [ [0 for x in range(len(b[1]))] for y in range(a[0])]
        for x in range(len(a[0])):
            for y in range(len(b[1])):
                for z in range(a[1]):
                    product[x][y] = comp.complex.add(product[x][y],comp.complex.product(a[x][z],b[z][y]))
        return product
    else:
        pass
def transpose(matrix):
    pass

def conjugate(matrix):
    pass

def adjoint(matrix):
    pass