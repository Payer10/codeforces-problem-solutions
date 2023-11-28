for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=(l[::-1])
    if(max(l)==min(l)):
        print(l[0])
    else:
        c=0 
        for i in range(n):
            if(abs(l[i]-s[i])<2):
                c+=1
        print(c)
        
        
