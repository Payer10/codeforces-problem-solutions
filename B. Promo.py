
a,b=map(int,input().split())
l=sorted(map(int,input().split()))
n=[0]
for i in l[::-1]:
    n.append(n[-1]+i)
for _ in range(b):
    x,y=map(int,input().split())
    print((n[x]-n[x-y]))
