stoneNumber=int(input())
colorText=input()
count=0
for i in range(stoneNumber):
    if((i + 1) == stoneNumber):
        break
    elif colorText[i] == colorText[i+1]:
        count+=1
print(count)
