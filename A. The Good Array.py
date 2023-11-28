for _ in range(int(input())):
    a,b=map(int,input().split())
    if(b==1):
        print(a)
    else:
        c=1
        for i in range(1,a):
            if(i%b==1):
                c+=1
        print(c)
