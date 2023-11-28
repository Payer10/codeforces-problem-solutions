Number=int(input())
evenNum=[]
oddNum=[]
listNum=list(map(int,input().split()))
for i in range(Number):
    if(listNum[i]%2==0):
        evenNum.append(listNum[i])
    else:
        oddNum.append(listNum[i])
if(sum(evenNum)>sum(oddNum)):
    print(sum(evenNum))
elif(sum(evenNum)==sum(oddNum)):
    print(sum(evenNum)+1)
else:
    print(sum(oddNum))
