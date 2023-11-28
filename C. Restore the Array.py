for i in range(int(input())):
    n=int(input())
    n=n-1
    li=list(map(int,input().split()))
    newli=[0]*(n+1)
    newli[0]=li[0]
    for a in range(n-1):
        newli[a+1]=min(li[a],li[a+1])
    newli[-1]=li[-1]
    print(*newli)
    
