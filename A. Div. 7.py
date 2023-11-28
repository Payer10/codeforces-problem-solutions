for i in range(int(input())):
    Number=int(input())
    if(Number%7==0):
        print(Number)
    else:
        a=Number//7
        print(a*7)
