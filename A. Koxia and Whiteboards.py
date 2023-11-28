for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=sorted(a+b)
    if(m==1 and n==1):
        print(b[0])
    else:
        print(sum(c[m:]))

        
