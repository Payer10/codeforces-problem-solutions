n,x=map(int,input().split())
c=0
for i in range(n):
    s,a=map(str,input().split())
    if(s=="+"):
        x+=int(a)
    if(s=="-"):
        if(int(a)<=x):
            x-=int(a)
        else:
            c+=1
print(x,c)
            

