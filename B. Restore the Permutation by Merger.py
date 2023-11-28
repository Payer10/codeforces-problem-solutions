for i in range(int(input())):
    Number=int(input())
    listdigit=list(map(int,input().split()))
    newlist=[]
    for j in range(0,Number*2):
        if(listdigit[j] not in newlist):
            newlist.append(listdigit[j])
    print(*newlist)
