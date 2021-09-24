n=int(input("dimension of board"))
mat = [[0 for x in range(n)] for y in range(n)]
def check_safe(mat,rows,columns):
    for column in range(columns):# check upside
        if mat[rows][column]:
            return False
    while 0<=rows<n and 0<=columns: #check left upside
        if mat[rows][columns]:
            return False
        rows = rows - 1
        columns = columns - 1

    while 0<=rows<n and 0<=columns:

        if mat[rows][column]:
            return False
        rows = rows + 1
        columns = columns - 1
    return True


def place_queen(mat,column):
    if column>=n:
        return True
    for row in range(n):
        if check_safe(mat,row,column):
            mat[row][column]=1
            if place_queen(mat,column+1):
                return True
            else:
                mat[row][column] = 0
    return False


place_queen(mat,0)
for i in mat:
    print(i)