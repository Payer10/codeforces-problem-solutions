for i in range(int(input())):
    n,k,b,s=map(int,input().split())
    if(s<k*b or s>k*b+(k-1)*n):
        print(-1)
    else:
        a=[0]*n
        a[-1]=k*b
        s=s-k*b
        i=n-1
        while i>=0 and s>0:
            a[i]+=min(s,k-1)
            s-=min(s,k-1)
            i-=1
        print(*a)