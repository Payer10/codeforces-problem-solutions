for i in range(int(input())):
    Number=int(input())
    listdi=list(map(int,input().split()))
    sortlist=sorted(listdi)
    if(Number==1):
        print('YES')
    else:
        count=1
        for a in range(Number):
            if((a+1)==Number):
                break
            if(sortlist[a]<sortlist[a+1]):
                count+=1
        if(count==Number):
            print('YES')
        else:
            print('NO')
