for i in range(int(input())):
    a1,a2,a3,a4=map(int,input().split())
    if(a1!=0):
        print(a1+min(a2,a3)*2+min(a1+1,abs(a2-a3)+a4))
    else:
        print(1)
    
    
