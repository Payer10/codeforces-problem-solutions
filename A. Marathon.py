for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    listdigit=(b,c,d)
    count=0
    for j in listdigit:
        if(a<j):
            count+=1
    print(count)
