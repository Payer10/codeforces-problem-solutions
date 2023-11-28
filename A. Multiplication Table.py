n,x=map(int,input().split())
count=0
for i in range(1,n+1):
    if(x//i<=n and x%i==0):
        count+=1
print(count)

