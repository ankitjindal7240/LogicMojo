str1="abcde"
str2="adbce"

def subsequence(str1,str2):
    matrix=[[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for j in range(len(str2)):
        for i in range(len(str1)):
            if str2[j]==str1[i]:
                matrix[j+1][i+1]=matrix[j][i]+1
            else:
                matrix[j + 1][i + 1]=max(matrix[j ][i + 1],matrix[j + 1][i ])

    for item in matrix:
        print(item)
    return matrix[-1][-1]

a=subsequence(str1,str2)
print(a)