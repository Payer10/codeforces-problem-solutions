for i in range(int(input())):
    n,m,k=map(int,input().split())
    x,y=map(int,input().split())
    c='YES'
    for i in range(k):
        a,b=map(int,input().split())
        if(abs(x-y)%2==abs(a-b)%2):
            c='NO'
    print(c)