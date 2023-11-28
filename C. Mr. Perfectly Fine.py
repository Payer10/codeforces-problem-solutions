for i in range(int(input())):
    n=int(input())
    a=10**9
    b=10**9
    ans=10**9
    for _ in range(n):
        x,y=map(str,input().split())
        if(y[0]=='1'):
            a=min(a,int(x))
        if(y[1]=='1'):
            b=min(b,int(x))
        if(y=='11'):
            ans=min(ans,int(x))
    if(a==10**9 or b==10**9):
        print(-1)
    else:
        print(min(a+b,ans))
