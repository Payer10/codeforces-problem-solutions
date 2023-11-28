for i in range(int(input())):
    a,b=map(int,input().split())
    x=a
    y=a*b
    z=a*b+a
    if(b==1):
        print('NO')
    else:
        print('YES')
        print(x,y,z)
