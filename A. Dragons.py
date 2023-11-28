s,n=map(int,input().split())
v=0
b=0
for i in range(n):
    x,y=map(int,input().split())
    if(s>=x):
        s+=y
        print('YES')
        break
else:
    print('NO')
