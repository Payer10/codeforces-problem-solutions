for i in range(int(input())):
    n=int(input())
    l=[]
    for j in range(1,n+1):
        l.append(j)
    if(n%2==0):
        print(*l)
    else:
        li=l[n//2]
        l[n//2]=l[n-1]
        l[n-1]=li
        print(*l)
