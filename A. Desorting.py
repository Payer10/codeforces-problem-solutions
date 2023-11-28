for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=sorted(l)
    if(s!=l):
        print(0)
    else:
        ans=[]
        for i in range(n-1):
            ans.append((s[i+1]-s[i])//2 +1)
        print(min(ans))
