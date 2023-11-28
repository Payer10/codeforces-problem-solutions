for i in range(int(input())):
    a,b=map(int,input().split())
    l=sorted(map(int,input().split()))
    ans=1
    count=1
    for i in range(a-1):
        if abs(l[i]-l[i+1])<=b:
            count+=1
        else:
            count=1
        if count>ans:
            ans=count
    print(a-ans)