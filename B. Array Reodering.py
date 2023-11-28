import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(l[i]*2,l[j])>1 or math.gcd(l[i],l[j]*2)>1:
                ans+=1
    print(ans)

