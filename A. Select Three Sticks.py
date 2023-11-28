for _ in range(int(input())):
    n=int(input())
    l=sorted(map(int,input().split()))
    c=[]
    for i in range(1,n-1):
        c.append(abs(l[i-1]-l[i+1]))
    print(min(c))
        
