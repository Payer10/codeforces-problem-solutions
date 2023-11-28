for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c0=0
    c1=0
    p0=-1
    p1=-1
    ans=0
    for i in range(n-1,-1,-1):
        if l[i]==0:
            c0+=1
            p0=i
        else:
            if c1==0:
                p1=i
            c1+=1
            ans+=c0
    print(max(ans,ans+(c0-1)-p0,ans-(n-p1-1)+(c1-1)))






            
