for i in range(int(input())):
    Number=int(input())
    listdi=list(map(int,input().split()))
    count=0
    if(len(listdi)==1):
        print('YES')
    else:
        for j in range(Number):
            if((j+1)==Number):
                break
            if(listdi[j]<100):
                count+=1
            else:
                restNum=listdi[j+1]-listdi[j]
                if(restNum==240):
                    count+=2
                if(restNum>=120):
                    count+=1
        if(count>=2):
            print('YES')
        else:
            print('NO')
