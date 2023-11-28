for i in range(int(input())):
    a,b=map(int,input().split())
    if(a==b):
        print(0,0)
    else:
        g=abs(a-b)
        h=min(a%g,g-(a%g)) 
        print(g,h)
