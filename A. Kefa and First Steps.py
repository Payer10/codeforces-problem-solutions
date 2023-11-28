n=int(input())
numlist=list(map(int,input().split()))
l=0
ml=1
for i in range(0,n+1):
    if(i==n):
        break
    elif(numlist[i]>=numlist[i-1]):
        l+=1
        ml=max(ml,l)
    else:
        l=1
print(ml)

        
