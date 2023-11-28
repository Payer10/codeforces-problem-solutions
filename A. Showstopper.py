for i in range(int(input())):
    Number=int(input())
    aNum=list(map(int,input().split()))
    bNum=list(map(int,input().split()))
    newlist=[]
    restlist=[]
    for j in range(Number):
        maxNum=max(aNum[j],bNum[j])
        minNum=min(aNum[j],bNum[j])
        newlist.append(maxNum)
        restlist.append(minNum)
    if((newlist[0]<=newlist[Number-1] and max(newlist)==newlist[Number-1] and restlist[0]<=restlist[Number-1] and max(restlist)==restlist[Number-1])):
        print('YES')
    else:
        print('NO')
