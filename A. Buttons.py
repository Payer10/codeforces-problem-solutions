for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a+c%2>b):
        print('First')
    else:
        print('Second')