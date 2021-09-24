matrix = [
          [1,  2,  3,  4 ],
          [5,  6,  7,  8],
          [9,  10, 11, 12],
          [13, 14, 15, 16]
        ]

n=len(matrix)
total_rounds=n//2

rounds=1
i=0
j=n-1
a=matrix[rounds][i+rounds]
b=matrix[i+rounds][n-1-rounds]
c=matrix[n-1-rounds][j-rounds]
d=matrix[j-rounds][rounds]

for rounds in range(total_rounds):
    i=0
    j=n-1
    while i<n-1- 2*rounds:
        a = matrix[rounds][i + rounds]
        b = matrix[i + rounds][n - 1 - rounds]
        c = matrix[n - 1 - rounds][j - rounds]
        d = matrix[j - rounds][rounds]
        # a, b, c, d = d,a,b,c
        matrix[rounds][i + rounds],matrix[i + rounds][n - 1 - rounds],matrix[n - 1 - rounds][j - rounds],matrix[j - rounds][rounds]= matrix[j - rounds][rounds], matrix[rounds][i + rounds],matrix[i + rounds][n - 1 - rounds],matrix[n - 1 - rounds][j - rounds]
        i=i+1
        j = j - 1



for item in matrix:
    print(item)
# a,b,c,d four corners of matrix

# a,b,c,d=b,c,d,a
# print(a,b,c,d)
