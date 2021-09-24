arr=[5,2,7,7,5,5,2]
n=len(arr)
for i in range(n):
    arr[i]=arr[i]-1
    value=arr[i]%n
    arr[value]=arr[value]+n
for i in range(n):
    print(f"frequency of {i+1} = {arr[i]//n}")