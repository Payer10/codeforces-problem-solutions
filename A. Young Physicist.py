n=int(input())
a=0
b=0
c=0
for i in range(n):
    x,y,z=map(int,input().split())
    a+=x
    b+=y
    c+=z
if(a==b==c==0):
    print("YES")
else:
    print("NO")
