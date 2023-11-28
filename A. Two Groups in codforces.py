number=int(input())
listNumber=list(map(int,input().split()))
sortlist=sorted(listNumber)[::-1]
sumlist=sum(listNumber)
maxlist=max(listNumber)
count=0
for i in range(number):
    if sumlist <= maxlist:
        break
    else:
        anslist=sumlist-sortlist[i]
        sumlist=anslist
        count+=1
print(count)
    
    
    
    
    
