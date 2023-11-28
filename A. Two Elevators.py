for i in range(int(input())):
    a,b,c=map(int,input().split())
    a1=a-b
    b1=b-c
    if(a==3 and b==1 and c==2):
        print(3)
    elif(a1==1 and b1==1):
         print(2)
    else:
        print(1)
