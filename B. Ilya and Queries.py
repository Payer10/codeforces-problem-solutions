N=input()
m=int(input())
c=0
d=[100005]
for i in range(m):
    a,b=map(int,input().split())
    for j in range(len(N)):
        if(j==len(N)):
            break
        if(N[j]==N[j-1]):
            c+=1
        else:
            d[j]=c
    print([b-1]-d[a-1])
    
