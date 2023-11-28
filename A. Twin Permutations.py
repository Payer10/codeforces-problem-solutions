for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    sort=list(reversed(sorted(l)))
    s=[]
    for i in range(n):
        s.append(sort[l[i]-1])
    print(*s)
 
