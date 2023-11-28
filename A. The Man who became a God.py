for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=[]
    for i in range(n-1):
        m.append(abs(l[i]-l[i+1]))
    m.sort()
    print(sum(m[:n-k]))