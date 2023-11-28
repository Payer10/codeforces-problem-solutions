s=int(input())
n=0
for i in range(s):
    a,b=map(int,input().split())
    if(b-a) >=2:
        n+=1
    else:
        n+=0
print(n)
