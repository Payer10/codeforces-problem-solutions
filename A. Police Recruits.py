Number=int(input())
listNumber=list(map(int,input().split()))
countNum=0
sumNum=0
for i in range(Number):
    if(listNumber[i]== -1):
        countNum+=1
    else:
        sumNum+=1
if(countNum>sumNum):
    print(countNum)
else:
    print(1)
