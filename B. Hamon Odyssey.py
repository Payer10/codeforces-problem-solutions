for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    a=-1
    for i in range(n):
        a&=l[i]
        if(a==0):
            c+=1
            a=-1
    if(c==0):
        print(1)
    else:
        print(c)
