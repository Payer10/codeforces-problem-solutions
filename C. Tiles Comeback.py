for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c0=0
    c1=0
    if(l[0]==l[-1]):
        c0=k
    for i in range(n):
        if(c0<k):
            if(l[i]==l[0]):
                c0+=1
        elif(c1<k):
            if(l[i]==l[-1]):
                c1+=1
    print('YES' if c1==k else 'NO')
