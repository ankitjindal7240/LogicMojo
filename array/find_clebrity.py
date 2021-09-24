matrix=[
    [0,0,1,0],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

def celebrity(matrix):
    n = len(matrix)
    i = 0
    j = n - 1

    while i<n and j>=0 :
        elem = matrix[i][j]
        if i==j:
            return i
        elif elem==1:
            i=i+1
        else:
            j=j-1

    return i

print(celebrity(matrix))