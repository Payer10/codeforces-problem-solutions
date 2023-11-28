for i in range(int(input())):
    a=int(input())
    n=len(str(a))
    if(n==1):
        print(a-1)
    elif(n==2):
        print(a-10)
    elif(n==3):
        print(a-100)
    elif(n==4):
        print(a-1000)
    elif(n==5):
        print(a-10000)
    elif(n==6):
        print(a-100000)
    elif(n==7):
        print(a-1000000)
    elif(n==8):
        print(a-10000000)
    elif(n==9):
        print(a-100000000)
    else:
        print(a-a)
        
