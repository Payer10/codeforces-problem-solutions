for i in range(int(input())):
    n,k=map(int,input().split())
    l=[((int(i)-1)%k) for i in input().split()]
    l=sorted((-x,y)for y,x in enumerate(l))
    print(*[i[1]+1 for i in l])
    