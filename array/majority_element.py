arr = [1, 1, 2, 1, 3, 5, 1,1,1,1,1,5,5,5]
count=1
elem=arr[0]
for i in range(1,len(arr)):
    if arr[i]==elem:
        count=count+1
    else:
        count=count-1
        if count==0:
            elem=arr[i]
            count+=1




print(elem)