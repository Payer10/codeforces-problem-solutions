for _ in range(int(input())):
    s=input()
    if(len(set(s))==1):
        print('No')
    else:
        if(len(set(s[:len(s)//2]))>1):
           print('Yes')
        else:
           print('No')
            
