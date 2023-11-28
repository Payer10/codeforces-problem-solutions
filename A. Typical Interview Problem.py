for _ in range(int(input())):
    n=int(input())
    s=input()
    b=0
    f=0
    for i in range(1,n):
        if(s[i]=='B'):
            b+=1
        if(s[i]=='F'):
            f+=1
    if(f>b):
        print('YES')
    else:
        print('NO')
