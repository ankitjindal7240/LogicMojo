def sort_0_1_2(arr):
    low=mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low=low+1
            mid=mid+1
        elif arr[mid]==2:
            arr[high],arr[mid]=arr[mid],arr[high]
            high=high-1
        else:mid=mid+1



#driver code
if __name__ == '__main__':
    arr=[0,1,2,1,2,1,0,0,0,1,2]
    sort_0_1_2(arr)
    print(arr)