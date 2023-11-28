n=int(input())
v=0
li=[]
for i in range(n):
    a,b=map(int,input().split())
    v+=(b-a)
    li.append(v)
print(max(*li))
  
        
    
