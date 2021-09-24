arr=[6,7,8,9,2,3,4,5]
l=0
r=len(arr)-1
def find_key(arr,l,r,x):
    mid = l + (r - l) // 2
    if arr[mid]==x:
        return mid
    elif arr[mid]>arr[l]:
        # left part of sorted array
        if x>=arr[l] and x<=arr[mid]:
            return find_key(arr,l,mid-1,x)
        else:
            return find_key(arr,mid+1,r,x)
    else:
        if x <= arr[r] and x >= arr[mid]:
            return find_key(arr, mid+1,r, x)
        else:
            return find_key(arr, l,mid-1 ,x)
print(find_key(arr,l,r,2))