def isBeautiful(listnumber):
    listsum=[]
    beautiful=True
    for j in listnumber:
        if(j==sum(listsum)):
            beautiful=False
            break
        else:
            listsum.append(j)
    return beautiful

def makeBeautiful(listnumber, length):
    sortedList=sorted(listnumber)
    lastIndex=length-1
    beautifulList=[sortedList[lastIndex],*sortedList[0:lastIndex]]
    return beautifulList

testNumber=int(input())

for i in range(testNumber):
    number=int(input())
    listnumber=list(map(int,input().split()))
    beautiful=isBeautiful(listnumber)
    if(beautiful):
        print("YES")
        print(*listnumber)
    else:
        beautifulList=makeBeautiful(listnumber, number)
        if(isBeautiful(beautifulList)):
            print("YES")
            print(*beautifulList)
        else:
            print("NO")
        
        
