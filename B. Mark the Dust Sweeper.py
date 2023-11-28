for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li=0
    k=0
    for i in range(n-1):
        if l[i]!=0:
            k=1
            li+=l[i]
        if l[i]==0:
            li+=k
    print(li)
