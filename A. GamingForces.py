for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=l.count(1)
    print(n-s //2)
