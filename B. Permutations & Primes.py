for i in range(int(input())):
    n=int(input())
    l=[]
    for i in range(1,n+1):
        if i%2==0:
            l.append(i)
    l.append(1)
    for i in range(n,1,-1):
        if i%2==1:
            l.append(i)
    print(*l)
