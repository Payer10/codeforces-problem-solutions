Number=int(input())
sumNum=0
newNum=0
count=0
while(sumNum<=Number):
    newNum+=1
    count+=newNum
    sumNum+=count
print(newNum-1)