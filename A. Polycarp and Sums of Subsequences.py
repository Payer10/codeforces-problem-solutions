for i in range(int(input())):
    b=list(map(int,input().split()))
    if(b[1]+b[2]==b[5]):
        print(b[0],b[2],b[1])
    else:
        print(b[3],b[0],b[1])
