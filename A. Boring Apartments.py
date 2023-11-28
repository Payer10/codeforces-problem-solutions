for i in range(int(input())):
    n=input()
    x=len(n)
    restNum=int(((int(n[0])-1) *10)+ (x*(x+1))//2)
    print(restNum)
    
