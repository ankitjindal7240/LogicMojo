def permutations(str,left,right):
    if left==right:
        print(''.join(str))
    else:
        for i in range(left,right+1):
            str[i],str[left]=str[left],str[i]   # bring the element at left most
            permutations(str,left+1,right)      # handle all cases when this element is left most
            str[i],str[left]=str[left],str[i]   #backtrack

str="abcd"
right=len(str)-1
left=0
permutations(list(str),left,right)

