for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(max(l))
    b=l.count(min(l))
    if(max(l)-min(l)==0):
        print(n*(n-1))
    else:
        print(2*a*b)
