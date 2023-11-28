for i in range(int(input())):
    Num=int(input())
    if(Num<10):
        print(Num)
    else:
        if(Num<=100):
            a=Num//11
            print(a+9)
        elif(Num<=1000):
            a=Num//111
            print(a+18)
        elif(Num<=10000):
            a=Num//1111
            print(a+27)
        elif(Num<=100000):
            a=Num//11111
            print(a+36)
        elif(Num<=1000000):
            a=Num//111111
            print(a+45)
        elif(Num<=10000000):
            a=Num//1111111
            print(a+54)
        elif(Num<=100000000):
            a=Num//11111111
            print(a+63)
        else:
            a=Num//111111111
            print(a+72)


          
            
        
