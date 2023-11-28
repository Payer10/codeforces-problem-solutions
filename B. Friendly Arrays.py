for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x,y,max=0,0,0
    for i in b:
        max|=i
    for i in a:
        x^=i
        y^=(i|max)
    if n%2==0:
        print(y,x)
    else:
        print(x,y)
