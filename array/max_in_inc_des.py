arr=[50]
l=0
r=len(arr)-1
def maxim(arr,l,r):
    mid = l+(r-l)//2
    if mid ==(0 or len(arr)-1):
        return arr[mid]
    elif ( arr[mid]>arr[mid-1]) and (arr[mid]>arr[mid+1]):
        return arr[mid]
    elif arr[mid-1]<arr[mid]<arr[mid+1]:
        l=mid+1
        # r=len(arr)
        return maxim(arr,l,r)
    else:
        r = mid -1
        # l=0
        return maxim(arr, l, r)

print(maxim(arr,l,r))
