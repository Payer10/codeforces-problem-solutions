import math
for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    s=0
    for i in range(a):
        s+=math.ceil(l[i]/b)
    t=math.ceil(sum(l)/b)
    print(t,s)
