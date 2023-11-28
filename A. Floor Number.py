for i in range(int(input())):
    a,b=map(int,input().split())
    s=(a+b-3)//b
    if(s<=0):
        print(1)
    else:
        print(s+1)
