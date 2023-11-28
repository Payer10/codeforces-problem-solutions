for i in range(int(input())):
    n,m,k,h=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in l:
        if(abs(h-i)%k==0 and 0<abs(h-i)//k<m):
            c+=1
    print(c)