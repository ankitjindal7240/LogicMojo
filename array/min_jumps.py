arr=[1,3,5,8,9,2,6,7,6,8,9]
initial=0
b=arr[0]
a=arr[0]
jump=0
for i in range(1,len(arr)):
    if i==len(arr)-1:
        jump=jump+1
        break
    a=a-1
    b=b-1
    if b<arr[i]:
        b=arr[i]
    if a==0 :
        jump=jump+1
        a=b
print(jump)


