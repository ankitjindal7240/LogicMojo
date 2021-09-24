arr=[1,2,3,4,0,5,0,0,0]
profit =0
i=0
buy=0
sell=0
while i <len(arr)-1:
    while i <len(arr)-1 and arr[i]>=arr[i+1] :
        i=i+1
    buy=arr[i]
    while   i <len(arr)-1 and arr[i]<=arr[i+1]:
        i=i+1
    sell=arr[i]
    profit=profit+(sell-buy)


print(profit)
ascii()