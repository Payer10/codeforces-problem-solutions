for i in range(int(input())):
    Number=int(input())
    liNum=list(map(int,input().split()))
    newlist=[]
    if(Number==1):
        print(0)
    else:
        for j in range(len(liNum)):
            if((j+1)>Number):
                break
            if(liNum[j] not in newlist):
                newlist.append(liNum[j])
        if(len(newlist)==Number):
            print(1)
        else:
            print(Number-len(newlist))
        
