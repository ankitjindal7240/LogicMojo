arr=[1,2,2,3,4,4,4,5,5]
j=0
duplicate=0
i=0
while i<len(arr)-1:

    if arr[i]!=arr[i+1]:
        arr[j+1]=arr[i]
        j=j+1
    i+=1
arr[j+1]=arr[i]
print(arr)