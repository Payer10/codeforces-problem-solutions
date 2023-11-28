for i in range(int(input())):
    a,b=map(int,input().split())
    n=abs(a-b)
    if(n%2==0 or a%2==0):
        print('YES')
    else:
        print('NO')
