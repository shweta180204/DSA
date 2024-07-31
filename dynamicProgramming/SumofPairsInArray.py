l=list(map(int,input().split()))
p=list(map(int,input().split()))

ps=[]
c=0
for i in l:
    c+=i
    ps.append(c)
sum=0
for j in range(len(ps)-1):
    a=min(p[j],p[j+1])
    b=max(p[j],p[j+1])
    if a:

        sum+=ps[b]-ps[a-1]
    else:
        sum+=ps[b]
print(sum)


