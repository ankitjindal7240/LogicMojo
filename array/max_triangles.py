arr = [10, 21, 22, 100, 101, 200, 300]
arr.sort()
no_of_triangles=0
for i in range(len(arr)-2):
    k=i+2
    for j in range(i+1,len(arr)):
        sum_of_two_sides=arr[i]+arr[j]
        while k<len(arr) and arr[k]<sum_of_two_sides:
            k=k+1
        if k>j:
            no_of_triangles=no_of_triangles+ (k-j-1)
print(no_of_triangles)

