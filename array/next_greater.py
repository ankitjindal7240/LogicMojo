
arr=[2,1,8,7,6,5]

def next_no(arr):
    if arr[-1]>arr[-2]:
        arr[-1],arr[-2]=arr[-2],arr[-1]
        return
    else:
        for i in reversed(range(len(arr))):
            if i==0:
                return 0
            if arr[i]>arr[i-1]:
                next_grt=i
                for j in range(i,len(arr)):
                    if arr[j]>arr[i-1] and arr[j]<arr[next_grt]:
                        next_grt=j
                print(arr[next_grt],arr[i-1])
                arr[i-1],arr[next_grt]=arr[next_grt],arr[i-1]
                sorted(arr[i:])
                return


next_no(arr)
print(arr)

