def revarray(arr):
    for i in range(len(arr)//2):
        temp=arr[i]
        arr[i]=arr[len(arr)-i-1]
        arr[len(arr)-i-1]=temp
    return arr
arr=list(map(int,input("enter an array").split()))
print(revarray(arr))
