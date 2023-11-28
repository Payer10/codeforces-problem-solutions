for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    s=0
    for i in range(n):
        c=0
        for a in li:
            if(a<=i):
                c+=1
        if(i==(n-c)):
            s=1
            break
    if(s==1):
        print(i)
    else:
        print(-1)
