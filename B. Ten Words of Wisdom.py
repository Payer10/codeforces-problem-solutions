for i in range(int(input())):
    n=int(input())
    ans=1
    m=0
    for i in range(n):
        a,b=map(int,input().split())
        if(a<=10):
            if(ans<=b):
                ans=b
                m=i+1
    print(m)
