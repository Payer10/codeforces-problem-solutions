for i in range(int(input())):
    a,b,n=map(int,input().split())
    c=0
    for j in range(n):
        m=min(a,b)
        a+=(m*j)
        if(a>=n):
            break
        else:
            c+=1
    print(c)
