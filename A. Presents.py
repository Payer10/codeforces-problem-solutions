Number=int(input())
FrindlistNumber=list(map(int,input().split()))
sortedlist=sorted(FrindlistNumber)
NewFrindlist=[]
for i in range(Number):
    serpiseFrind=FrindlistNumber.index(sortedlist[i])+1
    NewFrindlist.append(serpiseFrind)
print(*NewFrindlist)
    
