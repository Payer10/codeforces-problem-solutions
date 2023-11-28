from math import ceil
for i in range(int(input())):
    x,y,n=map(int,input().split())
    if(n*(n-1))//2>y-x:
        print('-1')
    else:
        l=[y]
        c=1
        for i in range(n-2):
            l.append(l[i]-c)
            c+=1
        l.append(x)
        print(*list(reversed(l)))
