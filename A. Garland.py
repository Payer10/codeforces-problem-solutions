for i in range(int(input())):
    li=sorted(input())
    if(li[0]==li[3]):
        print(-1)
    elif(li[0]==li[2] or li[1]==li[3]):
        print(6)
    else:
        print(4)
        
              
