for i in range(int(input())):
    Num=int(input())
    a,b,c=map(int,input().split())
    s=(a,b,c)
    s=sorted(s)
    if(s[1]==b):
        print('YES')
    else:
        print('NO')
