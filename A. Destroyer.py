for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    for  i in range(1,max(l)+1):
        if l.count(i)>l.count(i-1):
            print('No')
            break
    else:
        print('Yes')