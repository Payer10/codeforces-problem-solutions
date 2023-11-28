for i in range(int(input())):
    Number=int(input())
    modNum=Number%2020
    divNum=Number//2020
    if(modNum<=divNum):
        print('YES')
    else:
        print('NO')
        
