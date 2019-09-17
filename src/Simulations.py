import Matrix
def classicDinamicSystem(state,graph,clicks):
    sate = Matrix.transpose(state)
    temp = graph
    for i in range(clicks):
        temp=Matrix.matrixProduct(temp,graph)
    return Matrix.matrixProduct(temp,state)

def nSlit():
    pass

