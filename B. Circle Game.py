for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if(n%2==1):
        print('Mike')
    else:
        if l.index(min(l))%2==0:
            print('Joe')
        else:
            print('Mike')
