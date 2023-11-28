fristNum,secondNum=map(int,input().split())
listNum=sorted(map(int,input().split()))
count=0
sumNum=0
for i in range(fristNum):
    if(listNum[i]<0):
        count+=listNum[i]
        sumNum+=1
    if(sumNum==secondNum):
        break
print(abs(count))
