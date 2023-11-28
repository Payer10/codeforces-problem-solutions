from itertools import groupby
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    groups = [0]*(2*n+1)
    ans=0
    for i, j in groupby(a):
        groups[i] = max(groups[i],len(list(j)))
        ans=max(ans,groups[i])
    for i, j in groupby(b):
        ans=max(ans,(groups[i]+len(list(j))))
    print(ans)