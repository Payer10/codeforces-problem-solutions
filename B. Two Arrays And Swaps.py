for i in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    asum=sum(a)
    bsum=sum(b)
    if(asum>=bsum):
        print(asum)
    else:
        if(k > max(a)):
            print(bsum)
        else:
            print(bsum - (k*k))
