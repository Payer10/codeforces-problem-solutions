t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    if(a>b)and(b>c):
        print(b)
    elif(a<b)and(b<c):
        print(b)
    elif(a>c)and(c>b):
        print(c)
    elif(b>c)and(c>a):
        print(c)
    else:
        print(a)
        
