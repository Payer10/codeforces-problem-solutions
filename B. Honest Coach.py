for a in range(int(input())):
    Number=int(input())
    listNum=list(map(int,input().split()))
    sortli=sorted(listNum)
    li=[]
    for i in range(len(sortli)-1):
        li.append(abs(sortli[i+1] - sortli[i]))
    print(min(li))
