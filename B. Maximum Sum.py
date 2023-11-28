for _ in range(int(input())):
    n,k=map(int,input().split())
    l=sorted(map(int,input().split()))
    ans=0
    arr=[0]*(n+1)
    for i in range(n):
        arr[i+1]=arr[i]+l[i]
    for i in range(k+1):
        ans=max(ans,arr[n-(k-i)]-arr[2*i])
    print(ans)