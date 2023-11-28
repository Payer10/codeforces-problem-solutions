def fun(s):
    for i in range(2,int(s**.5)+1):
        if s%i==0:
            return print(i,s-i)
    else:
        print(-1)

for _ in range(int(input())):
    l,r=map(int,input().split())
    if r<4:
        print(-1)
    else:
        fun(r-(r%2)*(l<r))
