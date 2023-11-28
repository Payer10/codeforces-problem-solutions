for _ in range(int(input())):
    c=0
    ans=0
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if(a==1):
            c=max(c,b)
        else:
            if b!=1:
                ans+=b
    print(c+ans)
        
