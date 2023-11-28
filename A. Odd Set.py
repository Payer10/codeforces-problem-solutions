for i in range(int(input())):
    Number=int(input())
    Numlist=list(map(int,input().split()))
    count=0
    sumNum=0
    for i in range(len(Numlist)):
        if(Numlist[i]%2==0):
            count+=1
        else:
            sumNum+=1
    if(count==sumNum):
        print("Yes")
    else:
        print("No")
