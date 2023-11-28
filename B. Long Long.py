for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    b=0
    c=0
    for i in range(n):
        if l[i]>0:
            a+=c
            c=0
        if l[i]<0:
            c=1
        b+=abs(l[i])
    print(b,c+a)