for i in range(int(input())):
    a,b,n=map(int,input().split())
    l=list(map(int,input().split()))
    for i in l:
        b+=min(i,a-1)
    print(b)