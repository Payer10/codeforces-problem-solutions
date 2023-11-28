for _ in range(int(input())):
    input()
    n,k=map(int,input().split())
    l=input().split()
    first={}
    last={}
    for i,j in enumerate(l):
        if j not in first:
            first[j]=i
        last[j]=i
    for i in range(k):
        a,b=map(str,input().split())
        if a in first and b in last and first[a]<=last[b]:
            print('YES')
        else:
            print('NO')