for i in range(int(input())):
    Num=int(input())
    li=list(map(int,input().split()))
    sortli=sorted(li)
    newli=[]
    for i in range(Num-1):
        newli.append(sortli[i] - max(li))
    newli.append(max(li) - sortli[Num-2])
    print(*newli)
