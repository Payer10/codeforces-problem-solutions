for i in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    if(l.index(min(l))<=b):
        print('Yes')
    else:
        print('No')
