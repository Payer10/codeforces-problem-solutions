from math import ceil
m,s=map(int,input().split())
bug=ceil(s//5)
bug2=bug*3
bug3=s-bug2
s1=str(bug2)+str(bug3)
s2=str(bug3)+str(bug2)
if(s==0):
    print(-1,-1)
else:
    print(s2,s1)
