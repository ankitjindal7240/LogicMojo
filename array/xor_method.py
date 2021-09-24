arr=[6,2,4,3,4,2,3,6]
a=arr[0]
for i in range(1,len(arr)):
    a=a^arr[i]

print(a)