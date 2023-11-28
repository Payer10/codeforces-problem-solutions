n=int(input())
s=list(map(int,input().split()))
v=[]
a=[]
for i in s:
    if(i%2==0):
        v.append(i)
    else:
        a.append(i)
if(len(v)>len(a)):
    print(s.index(*a)+1)
else:
    print(s.index(*v)+1)
