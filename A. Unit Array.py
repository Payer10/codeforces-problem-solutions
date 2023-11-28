for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    neg=l.count(-1)
    pos=l.count(1)
    count=0
    while neg>pos or neg%2==1:
        neg=neg-1
        pos+=1
        count=count+1
    print(count)