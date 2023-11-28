Number=list(map(int,input().split()))
newlist=[]
for i in range(len(Number)):
    if Number[i] not in newlist:
        newlist.append(Number[i])
exumple=4 - len(newlist)
print(exumple)
        
    
