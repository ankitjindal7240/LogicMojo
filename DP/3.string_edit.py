word1="sunday"
word2="saturday"
matrix=[[0 for i in range( len(word2))]  for j in range(len(word1))]

for j in range(len(word1)):
    for i in range(len(word2)):
        if i==0:
            matrix[j][i]=j
        elif j==0:
            matrix[j ][i ]=i

        elif word1[j]==word2[i]:
            matrix[j][i]=matrix[j-1][i-1]
        else:
            min_value=min(matrix[j-1][i]  # delete beacause we are moving 1 cell upward
                ,matrix[j][i-1] # insert because we are moving 1 cell left
                ,matrix[j-1][i-1])  # replace

            matrix[j][i]= min_value + 1

for item in matrix:
    print(item)