arr=[]
sum=8
def subset_sum(arr,sum):
    matrix=[[0 for i in range(sum+1)] for j in range(len(arr)+1)]
    for i in range(sum+1):
        matrix[0][i]=0
    for j in range(len(arr)+1):
        matrix[j][0]=1

    for j in range(1,len(arr)+1):
        for i in range(1,sum+1):
            array_elem=arr[j-1]
            if array_elem>i:
                matrix[j][i] = matrix[j - 1][i]
            else:
                matrix[j][i]=matrix[j-1][i] + matrix[j-1][i-array_elem]


    for item in matrix:
        print(item)



subset_sum(arr,sum)