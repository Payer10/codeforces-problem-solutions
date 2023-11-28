Number=int(input())
string=input()
count=0
sumNum=0
for i in range(Number):
    if(string[i]=="0"):
        count+=1
    elif(string[i]=="1"):
        sumNum+=1
print(abs(sumNum-count))

