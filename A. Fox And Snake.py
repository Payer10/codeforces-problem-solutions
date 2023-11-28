n,m=map(int,input().split())
v,s="#","."
for i in range(1,n+1):
    if(i%2==1):
        print(v*m)
    else:
        a=i//2
        if(a%2==1):
            print(s*(m-1)+v)
        else:
            print(v+s*(m-1))
    
