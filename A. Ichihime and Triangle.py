for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    if(a==b and c==d):
        print(a,c,d)
    elif(b==c):
        print(b,c,c)
    elif(c==d):
        print(b,d,c)
    else:
        print(b,d-b,c)
