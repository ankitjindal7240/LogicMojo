array = [ 5, 1, 4, 3,6, 8, 10, 7, 9 ]
ans=-1
previous_max=array[0]
max=array[0]
for i in range(len(array)):
    if ans==-1 and array[i]>previous_max:
        ans=i
        max=array[i]
        previous_max=array[i]
    elif array[i]< previous_max:
        ans=-1
        previous_max=max
    elif array[i]>max:
        max=array[i]
print(ans)
