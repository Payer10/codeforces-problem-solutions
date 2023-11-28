for _ in range(int(input())):
    a,b=map(int,input().split())
    l=sorted(map(int,input().split()))
    c=0
    for i in set(l):
        c+=min(l.count(i),b)
    print(c)
    
