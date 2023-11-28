for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a==10 and c==1 or a<10 and c==1):
        print('YES')
    else:
        a1=a
        for _ in range(b):
            a1=a1//2 + 10
        b=a1 - c*10
        if(b>0):
            print('NO')
        else:
            print('YES')
