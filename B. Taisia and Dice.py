for i in range(int(input())):
    n,s,r=map(int,input().split())
    k=r//(n-1)
    d=r - k*(n-1)
    ans=[k]*(n-1-d)+[k+1]*d+[s-r]
    print(*ans)
