n,m=map(int,input().split())
if(n>m and m==1):
    a=n*2
    print(a,a)
if(n==m):
    a=2
    b=n+m
    print(a,b)
if(m>1 and n>m):
    if(n%m==0):
        print(m,n)
    else:
        a=n-m
        b=n-m
        print(a,b)
