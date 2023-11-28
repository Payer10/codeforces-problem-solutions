for i in range(int(input())):
    a,b=map(int,input().split())
    m=list(map(int,input().split()))
    n=list(map(int,input().split()))
    if(sum(m)>sum(n)):
        print('Tsondu')
    elif(sum(m)==sum(n)):
        print('Draw')
    else:
        print('Tenzing')
        