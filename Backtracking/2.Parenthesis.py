n=int(input())
arr=[0]*2*n
def parenthesis(arr,index,n,open,closed):
    if closed==n:
        print(arr)

    if open>closed:
        arr[index]="}"
        parenthesis(arr,index+1,n,open,closed+1)
    if open<n:
        arr[index]="{"
        parenthesis(arr,index+1,n,open+1,closed)

parenthesis(arr,0,n,0,0)
