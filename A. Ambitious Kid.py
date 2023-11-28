n=int(input())
l=list(map(int,input().split()))
m=abs(max(l))
for i in l:
    m=min(m,abs(i))
print(m)
