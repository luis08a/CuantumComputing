import Matrix
def classicDinamicSystem(state,graph,clicks):
    sate = Matrix.transpose(state)
    temp = graph
    for i in range(1,clicks):
        temp=Matrix.matrixProduct(temp,graph)
    return Matrix.matrixProduct(temp,state)

def nSlit(slits,targets,probability):
    n = slits+targets+1
    result= [[0] for x in range(n)]
    result[0]=1
    graph = [[0 for y in range(n)] for x in range(n)]
    for i in range(n):
        for j in range(n):
            if(j==0 and j%n>0 and j%n<=nSlit):
                graph[i][j]=[1/slits]
            elif(j%n>0 and j%n<=nSlit):
                graph[i][j]=[1/probability]
            elif(True):
                graph[i][j]=[1]


def quantumNSlit(state,graph,clicks,slits):
    pass

