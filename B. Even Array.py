test_input=int(input())
for i in range(test_input):
    Number=int(input())
    listdigit=list(map(int,input().split()))
    evenNum=0
    oddNum=0
    for j in range(Number):
        if(j%2!=listdigit[j]%2):
            if(j%2==0):
                evenNum+=1
            else:
                oddNum+=1
    if(evenNum==oddNum):
        print(evenNum)
    else:
        print(-1)
