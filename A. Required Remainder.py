for i in range(int(input())):
    x,y,n=map(int,input().split())
    m=n%x
    if(m>y):
        print(n-m+y)
    elif(m==y):
        print(n)
    else:
        print(n-m-x+y)
