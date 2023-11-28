for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a>(b+c)):
        print(2*(b+c)+1)
    else:
        print(a+a-1)

