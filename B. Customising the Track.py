for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    r=sum(l)%n
    print((n-r)*r)