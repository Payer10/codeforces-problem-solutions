n,a,b=map(int,input().split())
if(b>a and b<=n):
    print(b)
elif(b==a and b<n or a>b and b<=0):
    print(n-a)
else:
    print(a)
