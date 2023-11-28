import math
n=int(input())
li=[]
for i in range(1,int(math.sqrt(n)+1)):
    if(n%i==0):
        y=n//i
        li.append(i)
        li.append(y)
print(len(li))
print(sorted(li))
