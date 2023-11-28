for i in range(int(input())):
    a,b,c=map(int,input().split())
    a1=max(b,c)-a+1
    b1=max(a,c)-b+1
    c1=max(a,b)-c+1
    print(max(a1,0),max(b1,0),max(c1,0))
