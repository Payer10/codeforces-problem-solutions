for i in range(int(input())):
    a,b=map(int,input().split())
    if(a<=0 or b<=0):
        print('0')
    elif((a*2)<=b):
        print(a)
    elif((b*2)<=a):
        print(b)
    else:
        print((a+b)//3)
