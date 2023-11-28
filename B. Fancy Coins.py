for i in range(int(input())):
    m,k,a1,ak=map(int,input().split())
    x=min(m%k,a1)
    m=m-x
    print(max(m//k-(a1-x)//k-ak,0)+m%k)
