matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20]]
columns=len(matrix[0])
rows=len(matrix)
for i in range(rows):
    j=0
    while i>=0 and j<columns:
        print(matrix[i][j],end=" ")
        i=i-1
        j=j+1
for i in range(1,columns):
    j=rows-1
    while i<columns and j>=0:
        print(matrix[j][i],end=" ")
        i=i+1
        j=j-1