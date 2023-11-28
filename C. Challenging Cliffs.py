for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n-1):
        a=max(l)
        if(l[i]==a):
            l[i]=l[i+1]
            l[i+1]=a
            break
    print(*l)
    
