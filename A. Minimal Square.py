for i in range(int(input())):
    a,b=map(int,input().split())
    c=min(a,b)
    restNum=max(a,b,c*2)
    print(restNum**2)
