listNumber=list(map(int,input().split()))
maxNumber=max(listNumber)
listNumber.remove(max(listNumber))
newlist=[]
for i in range(len(listNumber)):
    restNumber=maxNumber-listNumber[i]
    newlist.append(restNumber)
print(*newlist[::-1])
