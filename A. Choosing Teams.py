fristNum,secondNum=map(int,input().split())
listNum=list(map(int,input().split()))
counts=0
for i in range(fristNum):
    if(listNum[i]+secondNum <= 5):
        counts+=1
print(counts//3)
        
