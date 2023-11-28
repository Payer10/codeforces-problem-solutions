for i in range(int(input())):
    Number=int(input())
    if(Number%2==0):
        a=Number//2
        print(a,Number-a)
    elif(Number%3==0):
        a=Number//3
        print(a,Number-a)
    else:
        print(1,Number-1)
