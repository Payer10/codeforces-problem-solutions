for i in range(int(input())):
    a,b=map(int,input().split())
    d=0
    e=0
    for _ in range(a):
        s,t=map(int,input().split())
        if(s==b):
            d=1
        if(b==t):
            e=1
    if(d>0 and e>0):
        print('YES')
    else:
        print('NO')
