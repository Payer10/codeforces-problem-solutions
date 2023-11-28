a,b=map(int,input().split())
s=(a,b)
n=max(s)-min(s)
m=max(s)-n
sum=min(s)+m
print(sum//2,n//2)
