for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=-1
    r=0
    for i in range(n):
        if a[i]!=b[i]:
            r=i
            if l==-1:
                l=i
    while l>0 and b[l-1]<=b[l]:
        l-=1
    while r<n-1 and b[r]<=b[r+1]:
        r+=1
    print(l+1,r+1)