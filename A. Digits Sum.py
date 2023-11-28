for i in range(int(input())):
    n=int(input())
    if(n<9):
        print('0')
    elif(n==9 or n==99 or n==999 or n==9999 or n==99999 or n==999999 or n==9999999 or n==99999999 or n==999999999):
        a=n+1
        print(a//10)
    else:
        a=n//10
        a1=n%10
        if(a1==9):
            print(a+1)
        else:
            print(a)
