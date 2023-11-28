n,t=map(int,input().split())
a=list(map(int,input().split()))
b=sorted(a)
count=0
m=0
for i in range(n):
    if(b[i]<t):
        count+=a[i]
        m+=1
    if(count>t):
        count-=a[i]
        m-=1
    if(count==t):
        break
print(m)
        
