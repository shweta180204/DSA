d={0:0,1:1}
def fib(n):
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]

n=int(input())
print(fib(n))


