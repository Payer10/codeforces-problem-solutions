for i in range(int(input())):
    Num=int(input())
    if(Num<10):
        print(Num)
    elif(Num<18):
        n=str(Num)
        sumn=(int(n[0])+int(n[1]))
        subn=Num-sumn
        print(str(sumn)+str(subn))
    elif(Num<25):
        n=(Num-18)*100
        print(189+n)
    elif(Num<31):
        n=(Num-24)*1000
        print(n+789)
    elif(Num<36):
        n=(Num-30)*10000
        print(n+6789)
    elif(Num<40):
        n=(Num-35)*100000
        print(n+56789)
    elif(Num<43):
        n=(Num-39)*1000000
        print(n+456789)
    elif(Num<45):
        n=(Num-42)*10000000
        print(n+3456789)
    elif(Num<46):
        n=(Num-45)
        print(n+123456789)
    else:
        print('-1')