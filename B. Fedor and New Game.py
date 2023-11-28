n,m,k=map(int,input().split())
newli=[]
for i in range(m+1):
    a=int(input())
    newli.append(a)
sort=sorted(newli)
count=0
for i in range(m):
    if((abs(max(sort)-sort[i]))<=k):
        count+=1
print(count)
