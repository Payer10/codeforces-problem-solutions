n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(n):
    count+=l[i]
print(count)
