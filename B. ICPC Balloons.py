for i in range(int(input())):
    N=int(input())
    s=input()
    c=0
    l=[]
    for j in range(N):
        if(s[j] not in l):
            c+=2
            l.append(s[j])
        else:
            c+=1
            l.append(s[j])
    print(c)
    
        
