for _ in range(int(input())):
    m,n=map(int,input().split())
    newli=[]
    for _ in range(m):
        l=list(map(int,input().split()))
        newli.append(l)
    c=0
    for i in range(1,m):
        a=(newli[i][i])
        c+=(newli[i].count(a)*a)
    if(c==0):
        print(m)
    else:
        print(c)
