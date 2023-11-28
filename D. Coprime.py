from math import gcd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    d={}
    ans=-1
    for i in range(n):
        d[l[i]]=i+1
    for i in d:
        for j in d:
            if gcd(i,j)==1:
                ans=max(ans,d[i]+d[j])
    print(ans)