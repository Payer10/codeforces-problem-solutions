from heapq import *
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    li=[0]
    ans=0
    for i in range(n):
        if(l[i]==0):
            ans-= heappop(li)
        heappush(li,-l[i])
    print(ans)
                
