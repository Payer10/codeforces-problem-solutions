for i in range(int(input())):
    a,b=map(int,input().split())
    x,y=map(int,input().split())
    if(a==0 and b==0):
        print('0')
    else:
        a1=(b-1)*x
        print(a1+y)
