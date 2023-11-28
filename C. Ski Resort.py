for i in range(int(input())):
    n,k,q=map(int,input().split())
    l=list(map(int,input().split()))
    a,b=0,0
    for i in l:
        if i>q:
            b=0
        else:
            b+=1
        if b>=k:
            a+=b-k+1
    print(a)