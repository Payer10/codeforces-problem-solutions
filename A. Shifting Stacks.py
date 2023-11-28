for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=0
    b=0
    ans=True
    for i in range(n):
        a+=i
        b+=l[i]
        if(a>b):
            ans=False
    if ans:
        print('Yes')
    else:
        print('No')
