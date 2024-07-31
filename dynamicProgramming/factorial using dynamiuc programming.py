#using memoization

def fact(n):
    if n==0 or n==1:
        return 1
    if n in d:
        return d[n]
    else:
        
        d[n]=n*fact(n-1)
    return d[n]
d={}
n=int(input())
if n<0:
    print("invalid number")
else:
    print(fact(n))





#using tabular method:
def facto(n):
    d=[1]*(n+1)
    d[0]=1
    d[1]=1
    for i in range(2,n+1):
        d[i]=i*d[i-1]
    return d[n]
n=int(input())
print(facto(n))
