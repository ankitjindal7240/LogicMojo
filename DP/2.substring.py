str1="edbcar"
str2="baducar"

def substring(str1,str2):
    ans=0
    matrix=[[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
    for j in range(len(str2)):
        for i in range(len(str1)):
            if str2[j]==str1[i]:
                next=matrix[j][i]+1
                matrix[j+1][i+1]=next
                if next>ans:
                    ans=next
    for item in matrix:
        print(item)
    return ans

print(substring(str1,str2) )