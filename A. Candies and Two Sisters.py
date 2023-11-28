for i in range(int(input())):
    Number=int(input())
    if(Number<=2):
        print(0)
    else:
        varNum=Number//2
        restNum=Number-varNum
        if(restNum>varNum):
            print(varNum)
        elif(restNum==varNum):
            print(varNum-1)
        else:
            print(restNum)
