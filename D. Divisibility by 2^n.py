def d(x):
    res = 0
    while x%2 == 0:
        res+=1
        x//=2
    return res
for i in range(int(input())):
    n=int(input())
    a=[*map(int,input().split())]
    p2=0
    for i in range(n):
        p2+=d(a[i])
    d2=[]
    for i in range(1,n+1):
        d2.append(d(i))
    d2.sort(reverse=True)
    i=0
    while i<n and p2<n:
        p2+=d2[i]
        i+=1
    if p2>=n:
        print(i)
    else:
        print(-1)