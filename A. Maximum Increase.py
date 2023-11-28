Number=int(input())
listNum=list(map(int,input().split()))
count=1
for i in range(Number):
    if((i+1)==Number):
        break
    if(listNum[i+1]>listNum[i]):
        count+=1
    elif(listNum[i+1]<listNum[i]):
        count-=1
print(count)
