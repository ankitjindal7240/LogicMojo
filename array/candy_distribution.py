arr=[1,7,6,5,2,7,6,5]
#ca=[1,4,3,2,1,3,2,1]


arr.insert(0,0)
arr.insert(-1,0)

candies=[0]*len(arr)

max_index=0
for i in range(1,len(arr)-1):
    if arr[i]>arr[i-1] :
        candies[i] = candies[i - 1] + 1
        if arr[i]>arr[i+1]:
            max_index = i
    elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
        candies[i]=1
        j=i-1
        while j>=max_index:
            candies[j]=candies[j+1]+1
            j=j-1

print(candies)


