for i in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    s=sum(l)
    c=l.count(1)
    if s-n>=c and n!=1:
        print('YES')
    else:
        print('NO')