for i in range(int(input())):
    a,b,x,y,n=map(int,input().split())
    if(a==b and a>n):
        b=b-n
        print(a*b)
    elif(a>b and a>n):
        a=a-1
        b=b-1
        print(a*b)
    elif(a==n):
        print(b-y)
    elif(a<n or b<n):
        print(x*y)
    elif(a<b):
        a=a-n
        print(a*b)
    
