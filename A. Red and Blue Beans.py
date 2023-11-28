for i in range(int(input())):
    r,b,n=map(int,input().split())
    if(r<b):
        c=b-r
        if(c<=r):
            if((b-r)<=n):
                print('YES')
            else:
                print('NO')
        else:
            a=b//r
            if((a-r)<=n):
                print('YES')
            else:
                print('NO')
    else:
        if((r-b)<=n):
            print('YES')
        else:
            print('NO')
            
