def findpower(x,n):
    if n==0:
        return 1
    result=findpower(x,n//2)
    if n%2==0:
        return result*result
    else:
        return x*result*result