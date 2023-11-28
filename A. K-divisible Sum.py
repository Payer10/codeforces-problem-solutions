for i in range(int(input())):
    a,b=map(int,input().split())
    if(a%b==0):
        print('1')
    elif(b%a==0):
        print(b//a)
    elif(a>b):
        print('2')
    else:
        print((b//a)+1)
