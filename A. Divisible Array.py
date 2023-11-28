from math import ceil
for i in range(int(input())):
    n=int(input())
    l=[]
    for i in range(1,n+1):
        l.append(i)
    if(sum(l)%n==0):
        print(*l)
    else:
        a=ceil(sum(l)/n)
        b=n*a-sum(l)
        l[0]=b+1
        print(*l)
        
