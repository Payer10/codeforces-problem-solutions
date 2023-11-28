n,m=map(int,input().split())
f=list(map(int,input().split()))
s=sorted(f)
a=[]
b=0
for i in s:
    a.append(i)
    b+=1
    if(b==n):
        break
c=max(a)-min(a)
if(c<n):
    print(0)
else:
    print(c)

    
