testcase=int(input())
for j in range(testcase):
    Number=int(input())
    newlist=[]
    sumNum=0
    for i in range(1,Number+1):
        newNum=2**i
        newlist.append(newNum)
    ns=(Number//2 - 2)
    for a in range(Number-2,ns,-1):
        sumNum+=newlist[a]
        newlist.remove(newlist[a])
    Number=sum(newlist)
    mode=abs(sumNum - Number)
    print(mode)
