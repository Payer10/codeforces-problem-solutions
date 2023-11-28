for i in range(int(input())):
    Num=int(input())
    li=list(map(int,input().split()))
    mihai=0
    bianca=0
    for a in range(len(li)):
        if(li[a]%2==0):
            mihai+=li[a]
        else:
            bianca+=li[a]
    if(mihai>bianca):
        print('YES')
    else:
        print('NO')
