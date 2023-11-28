from bisect import bisect_left
for _ in range(int(input())):
    n,q=map(int,input().split())
    l=sorted(map(int,input().split()),reverse=True)
    for i in range(1,n):
        l[i]+=l[i-1]
    for j in range(q):
        a=int(input())
        if(l[-1]<a):
            print(-1)
        else:
            print(bisect_left(l,a)+1)
            
