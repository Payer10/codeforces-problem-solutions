for i in range(int(input())):
    Num=int(input())
    newli=[]
    if(Num==3):
        print(-1)
    else:
        for a in range(1,Num+1):
            newli.append(a)
        newli.reverse()
        print(*newli)
