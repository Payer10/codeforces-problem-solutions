for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    l=0
    for i in range(len(li)):
        if(0>li[i]):
            l+=1
            li[i]=-li[i]
    if(l%2==0):
        print(sum(li))
    else:
        print(sum(li)-2*min(li))
