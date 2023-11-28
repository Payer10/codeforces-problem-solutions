n,k=map(int,input().split())
res=240-k
v=0
m=0
i=1
while i<=n:
    v+=(i*5)
    if(v>res):
        break
    else:
        m=m+1
    i+=1
if(n>m):
    print(m)
else:
    print(n)
