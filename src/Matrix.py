def add(a,b):
    """ dfsf"""
    if (a.lenght == b.lenght and a[0].lenght == b[0].lenght):
        pass
    else:
        for i in range(a.lenght):
            for j in range(a[0].lenght):
                a[i][j]+=b[i][j]
        return a

def inverse(matrix):
    for i in matrix:
        for j in i:
            j= -j
    return matrix

