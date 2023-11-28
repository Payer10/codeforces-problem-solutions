for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    w=[0]*n
    a=n
    for i in range(n-1,0,-1):
        if(l[i]==l[i-1]):
            w[i]=i
            w[i-1]=a
        else:
            a=i
    if(sum(w)==(n*(n+1))//2):
        print(*w)
    else:
        print(-1)
            
