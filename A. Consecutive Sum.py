for j in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in range(b):
        c+=(max(l[i::b]))
    print(c)