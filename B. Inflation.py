for i in range(int(input())):
    a,k=map(int,input().split())
    l=list(map(int,input().split()))
    s=l[0]
    ans=0
    for i in range(1,a):
        ans=max(ans,((100*l[i]+k-1)//k)-s)
        s+=l[i]
    print(ans)