for i in range(int(input())):
    a,b,c,n=map(int,input().split())
    s=max(a,b,c)
    if((a+b+c+n) % 3 == 0 and (a+b+c+n)/3>=s):
        print('YES')
    else:
        print('NO')
