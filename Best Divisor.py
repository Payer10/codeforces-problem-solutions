n=int(input())
l=[]
s=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
        b=0
        for j in str(i):
            b+=int(j)
        s.append(b)
            
a=s.index(max(s))
print(l[a])
