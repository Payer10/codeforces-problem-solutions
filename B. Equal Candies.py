for i in range(int(input())):
    count=0
    Number=int(input())
    listdi=list(map(int,input().split()))
    count=0
    minlist=min(listdi)
    for j in range(Number):
        count+=(listdi[j]-minlist)
    print(count)
