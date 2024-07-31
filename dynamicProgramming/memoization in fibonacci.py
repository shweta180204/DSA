def fib(n):
    if n==0 or n==1:
        return n
    if n in d:
        return d[n]
    else:
        d[n]=fib(n-1)+fib(n-2)
        return d[n]
n=int(input())
d={}
print(fib(n))

