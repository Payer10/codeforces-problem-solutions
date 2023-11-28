for i in range(int(input())):
    Number=int(input())
    listNum=list(map(int,input().split()))
    count=0
    for j in range(Number):
        if((j+1)==Number):
            break
        elif(listNum[j]==listNum[j-1] or listNum[j]==listNum[j+1]):
            count+=1
        else:
            break
    print(count+1)

