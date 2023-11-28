for i in range(int(input())):
    a,b=tuple(map(int,input().split()))
    c=0
    for i in range(a):
        li=list(map(int,input().split()))
        if(max(li)<5):
            c+=sum(li)
        else:
            s=sum(li)-max(li)
            c+=s
    print(c)
            
            
            
