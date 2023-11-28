n,m=map(int,input().split())
t=[]
for i in range(m):
    a,b=map(str,input().split())
    t.append(a)
    t.append(b)
string=input().split()
for j in range(n):
    if(string[j]==t[a] and t[a]<=t[b]):
        print(t[a])
