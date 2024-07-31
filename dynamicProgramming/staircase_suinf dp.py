d={}
def stairs(n):
    if n in d:
        return d[n]
    if n==0 or n==1:
        return 1
    else:
        d[n]=stairs(n-1)+stairs(n-2)
    return d[n]



n=int(input())
print(stairs(n))
