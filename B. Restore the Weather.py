for _ in range(int(input())):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    s=[(x[i],i)for i in range(a)]
    s.sort()
    y.sort()
    n=[0]*a
    for i in range(a):
       n[s[i][1]]=y[i]
    print(*n)
