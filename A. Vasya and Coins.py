for i in range(int(input())):
    a,b=map(int,input().split())
    if(a==1 and b==1):
        print(4)
    elif(a>=1 and b>=1):
        print(a*1+b*2+1)
    elif(a==0 and b==0):
        print(1)
    elif(a==0 and b>0):
        print(1)
    elif(a>0 and b==0):
        print(a*1+1)
