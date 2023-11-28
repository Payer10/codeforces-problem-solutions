for i in range(int(input())):
    Num=int(input())
    li=sorted(map(int,input().split()))
    newli=[]
    for a in range(Num-1):
        newli.append(li[a]*li[a+1])
    print(max(newli))

