for i in range(int(input())):
    num=int(input())
    even=[]
    odd=[]
    for i in range(1,num*2+1):
        if(i%2==1):
            odd.append(num-i)
            odd.append(i)
        else:
            even.append(num-i)
            even.append(i)
    print(*even)
    print(*odd)
    
            
        
