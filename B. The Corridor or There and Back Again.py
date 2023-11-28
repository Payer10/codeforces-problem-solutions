for i in range(int(input())):
    n=int(input())
    d,s=map(int,input().split())
    ans=2*10**9
    c=1
    if s+1>=d:
        ans=min(ans,(d-c)+s//2)
        c+=1
    print(ans)
       