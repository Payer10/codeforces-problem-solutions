for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l[0]
    m=sorted(l[1:])
    for i in m:
        if(a<i):
            a+=(i-a+1)//2
    print(a)