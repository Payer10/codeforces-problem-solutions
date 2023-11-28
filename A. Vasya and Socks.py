n,m=map(int,input().split())
a=n//m
if((a+n)%m==0):
    print(a+n+1)
else:
    print(a+n)
