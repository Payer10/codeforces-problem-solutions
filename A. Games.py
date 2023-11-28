a1=[]
b1=[]
count=0
for i in range(int(input())):
    a,b=map(int,input().split())
    a1.append(a)
    b1.append(b)
for j in a1:
    n=j
    for a in b1:
        if(n==a):
            count+=1
print(count)
