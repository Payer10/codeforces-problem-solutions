for i in range(int(input())):
    Num=int(input())
    li=list(map(int,input().split()))
    newli=[]
    if(Num<=2 or min(li)==max(li)):
        print(*li)
    else:
        for a in range(Num//2):
            newli.append(li[a])
            newli.append(li[Num-1-a])
        if(Num%2==1):
            newli.append(li[Num//2])
        print(*newli)
