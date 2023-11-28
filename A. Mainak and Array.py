for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    c=max(l[-1]-min(l),max(l)-l[0])
    for a in range(n):
        c=max(c,(l[a-1]-l[a]))
    print(c)
