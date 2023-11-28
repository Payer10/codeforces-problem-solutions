for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li=[0]*5000
    #li[0]=l[0]
    ans=0
    for i in range(n):
        if(l[i]==0):
            ans+=max(li)
            li.remove(max(li))
        else:
            li.append(l[i])
    print(ans)
                
