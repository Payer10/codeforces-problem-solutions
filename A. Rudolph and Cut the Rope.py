for i in range(int(input())):
    c=0
    for i in range(int(input())):       
        a,b=map(int,input().split())
        if(a>b):
            c+=1
    print(c)
    