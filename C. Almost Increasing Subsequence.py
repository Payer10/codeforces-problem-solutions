a,b=map(int,input().split())
li=list(map(int,input().split()))
for _ in range(b):
    x,y=map(int,input().split())
    if(x==y):
        print(1)
    else:
        c=0
        for i in range(x-1,y-1):
            if(li[i+1]!=li[i]):
                c+=1
        print(c+1)
            
