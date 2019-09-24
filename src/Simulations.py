import complexNumLib.src.Matrix
import complexNumLib.src.Complex
def product(a,b):
    if(len(a[0]) == len(b)):
        product = [[0 for x in range(len(b[0]))] for y in range(len(a))]
        for x in range(len(a)):
            for y in range(len(b[0])):
                for z in range(len(a[0])):
                    product[x][y] += a[x][z]*b[z][y]
        return product
    else:
        print("Error")

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0 for y in range(n)] for x in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]
    return result

def classicDinamicSystem(state,graph,clicks):
    sate = transpose(state)
    temp = graph
    for i in range(1,clicks):
        temp=product(temp,graph)
    return product(temp,state)

def nSlit(slits,targets,probability):
    clicks=2
    n = slits+targets+1
    result= [[0] for x in range(n)]
    result[0]=1
    graph = [[0 for y in range(n)] for x in range(n)]
    for j in range(n):
        for i in range(n):
            if(j==0 and i%n>0 and i+slits<n):
                graph[i][j]=[1/slits]
            elif(i%slits> 0 and i+slits<n and j%slits> 0 and j+slits<n):
                graph[i][j]=[1/probability]
            elif(i==j):
                graph[i][j]=[1]
    for i in range(1,clicks+1):
        result= product(graph,transpose(result))
    return graph,result

def quantumNSlit(slits,targets,probability):
    n = slits+targets+1
    result= [[Complex.Complex(0,0)] for x in range(n)]
    result[0]=Complex.Complex(1,0)
    graph = [[0 for y in range(n)] for x in range(n)]
    for j in range(n):
        for i in range(n):
            if(j==0 and i%n>0 and i+slits<n):
                graph[i][j]=[1/slits]
            elif(i%slits> 0 and i+slits<n and j%slits> 0 and j+slits<n):
                graph[i][j]=[1/probability]
            elif(i==j):
                graph[i][j]=[1]
    for i in range(n):
        result= product(graph,transpose(result))
    return graph,result

