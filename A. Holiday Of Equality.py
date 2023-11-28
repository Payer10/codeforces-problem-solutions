Number=int(input())
listNum=list(map(int,input().split()))
restlist=sorted(listNum)
maxlist=max(restlist)
newlistNum=[]
for i in range(Number):
    if((i+1)==Number):
        break
    else:
        restNum=maxlist - restlist[i]
        newlistNum.append(restNum)
print(sum(newlistNum))
