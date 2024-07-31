#using memoization
d={}
def four(n):
    if n>=1 and n<=4:
        return n
    if n in d:
        return d[n]
    else:
        d[n]=four(n-1)+four(n-2)+four(n-3)+four(n-4)
        return d[n]
    
n=int(input())
print(four(n))



#using tabulation
def four_sum(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=2
    dp[3]=3
    dp[4]=4
    for i in range(5,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]
    return dp[n]

n=int(input())
print(four_sum(n))
    
    
