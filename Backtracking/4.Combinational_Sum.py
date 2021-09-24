def Combinational_Sum(arr,target,sum,temp,index):
    if sum==target:
        result.append(list(temp))
    elif sum>target:
        return
    else:
        for i in range(index,len(arr)):
            temp.append(arr[i])
            Combinational_Sum(arr,target,sum+arr[i],temp,index)
            temp.pop()


result=[]
temp=[]
arr=[1,2,3,4]
target=4
arr.sort
Combinational_Sum(arr,target,0,temp,0)
print(result)
