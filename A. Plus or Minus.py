for i in range(int(input())):
    a,b,c=map(int,input().split())
    if(a<c and b<c):
        print('+')
    else:
        print('-')
